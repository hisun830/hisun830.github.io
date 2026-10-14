# Neon Knuckle 홈페이지

GitHub Pages(`hisun830.github.io`)에서 바로 동작하는 Jekyll 템플릿 사이트입니다.
**게임 하나 = 파일 하나.** `_games/` 폴더에 파일을 추가하면 메인 카드, 상세 페이지, 개인정보처리방침의 게임 목록까지 자동으로 생성됩니다.

## 폴더 구조

```
_config.yml            회사 공통 정보 (사이트 주소, 이메일, SNS 링크, 설명문)
_games/                ★ 게임 데이터. 파일 1개 = 게임 1개  (aeroshoot.md, necklace-jam.md …)
_layouts/default.html  모든 페이지의 공통 틀 (head, 네비게이션, 푸터)
_layouts/game.html     게임 상세 페이지 템플릿
_includes/             네비게이션, 푸터, SNS 아이콘, 게임 카드, 스토어 버튼, 아이콘
index.html             메인 (히어로 · 게임 라인업 · 제작 철학 · 소개 · 문의)
privacy.html           개인정보처리방침 (스토어 심사용 URL: /privacy.html)
404.html               없는 주소 안내
assets/css, js         스타일 · 스크립트 (색·폰트 토큰은 site.css 맨 위 :root)
assets/img, video      웹용으로 경량화한 이미지·영상
app-ads.txt, google030c3959aadfb6c9.html   AdMob · 구글 인증 파일 (수정 금지)
tools/game-template.md 새 게임 추가용 템플릿
tools/preview.py       로컬 미리보기 빌더 (선택)
```

## 새 게임 추가하기 (3단계)

1. `tools/game-template.md`를 복사해 `_games/새게임.md`로 저장합니다. 파일명이 곧 주소가 됩니다 (`/games/새게임/`).
2. 파일 안의 값(제목, 스토어 링크, 문구, 이미지 경로)을 채웁니다. 모든 문구는 `en` / `ko` 쌍으로 넣습니다.
3. 이미지를 `assets/img/`에 넣고 GitHub에 push합니다. 1~2분 뒤 사이트에 반영됩니다.

- 아직 출시 전이면 `status: soon`으로 두세요. 스토어 버튼 대신 **출시 예정** 배지가 붙고, 메인의 "출시작 N종" 숫자에서도 제외됩니다. 출시 후 `status: live`와 `store_url`만 바꾸면 됩니다.
- `how_to_play`, `features`, `screenshots`, `video` 블록은 없으면 해당 섹션이 자동으로 숨겨집니다.
- 메인 노출 순서는 `order` 숫자로 정합니다.

### 이미지 규격

| 용도 | 파일 | 크기 |
|---|---|---|
| 아이콘 | `*-icon-sm.webp` | 192×192 |
| 키아트 (카드 상단·공유 이미지) | `*-keyart.webp` | 1024×500 |
| 로고 (투명 배경) | `*-logo.webp` | 가로 900 이하 |
| 스크린샷 | `*-shot-N.webp` | 가로 600 |
| 플레이 영상 | `*-play.mp4` + `*-poster.jpg` | 세로 540×960 내외, 10초 이내 |

## 공통 정보 수정

`_config.yml`에서 이메일, Google Play 개발자 페이지, 페이스북·인스타그램 주소를 고치면 모든 페이지에 반영됩니다. `social:` 아래에 `youtube:` 를 추가하면 유튜브 아이콘도 자동으로 붙습니다.

## 문구 수정 (영어 기본 + 한국어 전환)

모든 문구는 영어·한국어가 쌍으로 들어 있습니다. 한국어 브라우저 방문자는 자동으로 한국어가 먼저 보이고, 우상단 EN/KO 버튼으로 바꿀 수 있습니다.

```html
<span class="en">Casual puzzles that pack a punch.</span>
<span class="ko">가볍게 집어 들고, 확실하게 꽂히는 퍼즐.</span>
```

## 로컬 미리보기 (선택)

GitHub에 push하면 자동으로 빌드되므로 필수는 아닙니다. 올리기 전에 확인하고 싶을 때:

```bash
pip install python-liquid pyyaml
python tools/preview.py --serve
```

브라우저에서 `http://localhost:8787` 접속. 결과물은 `_site/` 폴더에 생성되며 git에는 올라가지 않습니다.

## 배포

`hisun830/hisun830.github.io` 레포의 루트에 이 폴더의 내용(`_site/` 제외)을 올리고 push하면 GitHub가 자동으로 빌드합니다.
스토어에 등록된 개인정보처리방침 주소 `https://hisun830.github.io/privacy.html`은 그대로 유지됩니다.
