"""
Neon Knuckle 홈페이지 — 로컬 미리보기 빌더 (Ruby/Jekyll 없이 실행)

GitHub Pages가 하는 Jekyll 빌드를 파이썬으로 흉내 내어 _site/ 폴더에 정적 HTML을 만듭니다.
지원 범위: front matter, _layouts(중첩), _includes(인자 없는 include), collections(_games),
          relative_url / absolute_url 필터, 정적 파일 복사.

사용법:
  pip install python-liquid pyyaml        (최초 1회)
  python tools/preview.py                 → _site/ 생성
  python tools/preview.py --serve         → 빌드 후 http://localhost:8787 로 서빙
"""
import io, os, re, sys, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.environ.get("NK_PYLIB"):
    sys.path.insert(0, os.environ["NK_PYLIB"])
import yaml
from liquid import Environment

FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
INC = re.compile(r"{%-?\s*include\s+([\w./-]+)\s*-?%}")


def read(p):
    return io.open(p, encoding="utf-8").read()


def split_fm(text):
    m = FM.match(text)
    if not m:
        return None, text
    return (yaml.safe_load(m.group(1)) or {}), text[m.end():]


cfg = yaml.safe_load(read(os.path.join(ROOT, "_config.yml"))) or {}
BASE = cfg.get("baseurl") or ""
URL = cfg.get("url") or ""

env = Environment()
env.filters["relative_url"] = lambda v: (BASE + str(v)) if str(v).startswith("/") else str(v)
env.filters["absolute_url"] = lambda v: (URL + BASE + str(v)) if str(v).startswith("/") else str(v)


def expand_includes(src, depth=0):
    if depth > 10:
        raise RuntimeError("include recursion")
    return INC.sub(lambda m: expand_includes(read(os.path.join(ROOT, "_includes", m.group(1))), depth + 1), src)


_layouts = {}


def layout(name):
    if name not in _layouts:
        fm, body = split_fm(read(os.path.join(ROOT, "_layouts", name + ".html")))
        _layouts[name] = ((fm or {}), expand_includes(body))
    return _layouts[name]


def render(src, ctx):
    return env.from_string(src).render(**ctx)


def wrap(layout_name, content, ctx):
    while layout_name:
        fm, body = layout(layout_name)
        content = render(body, dict(ctx, content=content))
        layout_name = fm.get("layout")
    return content


# ---- collections ----
site = dict(cfg)
defaults = cfg.get("defaults", [])


def default_vals(type_):
    vals = {}
    for d in defaults:
        if d.get("scope", {}).get("type") == type_:
            vals.update(d.get("values", {}))
    return vals


docs = []
for cname, cc in (cfg.get("collections") or {}).items():
    folder = os.path.join(ROOT, "_" + cname)
    items = []
    if os.path.isdir(folder):
        for fn in sorted(os.listdir(folder)):
            if fn.startswith(("_", ".")) or not fn.endswith((".md", ".html", ".markdown")):
                continue
            fm, body = split_fm(read(os.path.join(folder, fn)))
            name = os.path.splitext(fn)[0]
            page = dict(default_vals(cname))
            page.update(fm or {})
            page["url"] = (cc.get("permalink") or "/%s/:name/" % cname).replace(":name", name)
            page["name"] = name
            page["collection"] = cname
            items.append(page)
            docs.append((page, body))
    site[cname] = items

# ---- pages ----
EXCLUDE = set(cfg.get("exclude") or []) | {"_site"}
pages = []
for fn in sorted(os.listdir(ROOT)):
    if fn.startswith(("_", ".")) or fn in EXCLUDE:
        continue
    p = os.path.join(ROOT, fn)
    if os.path.isfile(p) and fn.endswith((".html", ".md")):
        fm, body = split_fm(read(p))
        if fm is None:
            continue  # no front matter → static copy
        page = dict(fm)
        page["url"] = page.get("permalink") or ("/" if fn == "index.html" else "/" + fn)
        pages.append((page, body))

OUT = os.path.join(ROOT, "_site")
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)


def write_out(url, html):
    if url.endswith("/"):
        path = os.path.join(OUT, url.strip("/"), "index.html") if url != "/" else os.path.join(OUT, "index.html")
    else:
        path = os.path.join(OUT, url.lstrip("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8", newline="\n").write(html)


for page, body in pages + docs:
    ctx = {"site": site, "page": page}
    html = wrap(page.get("layout"), render(expand_includes(body), ctx), ctx)
    write_out(page["url"], html)
    print("built", page["url"])


def copy_static(rel=""):
    src = os.path.join(ROOT, rel)
    for fn in os.listdir(src):
        if fn.startswith(("_", ".")) or (rel == "" and fn in EXCLUDE):
            continue
        sp = os.path.join(src, fn)
        rp = os.path.join(rel, fn) if rel else fn
        if os.path.isdir(sp):
            copy_static(rp)
            continue
        if rel == "" and fn.endswith((".html", ".md")) and split_fm(read(sp))[0] is not None:
            continue
        dp = os.path.join(OUT, rp)
        os.makedirs(os.path.dirname(dp), exist_ok=True)
        shutil.copy2(sp, dp)


copy_static()
print("output:", OUT)

if "--serve" in sys.argv:
    import http.server, functools
    port = 8787
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=OUT)
    print("serving http://localhost:%d  (Ctrl+C to stop)" % port)
    http.server.ThreadingHTTPServer(("", port), handler).serve_forever()
