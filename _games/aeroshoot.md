---
# ───────── Aeroshoot ─────────
# 게임 1개 = 이 파일 1개. 아래 값만 채우면 메인 카드 + 상세 페이지가 자동 생성됩니다.
title: Aeroshoot
order: 1                      # 메인 페이지 노출 순서 (작을수록 앞)
status: live                  # live(출시) | soon(출시 예정: 스토어 버튼 대신 '출시 예정' 표시)
store_url: "https://play.google.com/store/apps/details?id=com.neonknuckle.aeroshoot"
accent: "#38bdf8"             # 이 게임의 포인트 컬러

# 브라우저 탭 제목 / 검색 설명
title_en: "Aeroshoot — Arrow puzzle by Neon Knuckle"
title_ko: "Aeroshoot — 네온너클의 화살표 퍼즐"
description_en: "Aeroshoot is a one-tap arrow puzzle: shoot arrows off the board in the right order, clear the picture, and hear every clear add a note. Free on Google Play."
description_ko: "Aeroshoot는 탭 한 번으로 즐기는 화살표 퍼즐입니다. 올바른 순서로 화살표를 날려 그림을 완성하고, 성공할 때마다 쌓이는 음을 들어보세요. Google Play 무료."

genre:
  en: "Arrow puzzle"
  ko: "화살표 퍼즐"
tagline:
  en: "One tap. Endless puzzles."
  ko: "탭 한 번, 끝없는 퍼즐."

# 메인 페이지 카드 문구
pitch:
  en: "Tap an arrow and it shoots off along its path. Clear every line to finish the picture — each clear rings a note, so solving sounds as good as it feels."
  ko: "화살표를 탭하면 자기 길을 따라 날아갑니다. 모든 선을 빼내면 그림이 완성되고, 성공할 때마다 음이 쌓여 퍼즐이 음악이 됩니다."
highlights:
  - { en: "One-tap control, zero tutorial", ko: "튜토리얼 없이 탭 한 번으로" }
  - { en: "Picture levels, from portraits to famous paintings", ko: "초상화부터 명화까지, 그림이 되는 레벨" }
  - { en: "Undo, hints and zoom when you get stuck", ko: "막히면 되돌리기·힌트·확대" }

# 상세 페이지 문구
lead:
  en: "Every level is a picture drawn in tangled arrows. Tap an arrow and it shoots off along its path — but only if nothing is in the way. Find the right order, clear the board, and listen as every clear adds a note to the melody."
  ko: "모든 레벨은 얽힌 화살표로 그려진 한 장의 그림입니다. 화살표를 탭하면 자기 길을 따라 날아가지만, 길이 막혀 있으면 튕겨 나옵니다. 올바른 순서를 찾아 보드를 비우고, 성공할 때마다 쌓이는 음을 들어보세요."
badges:
  - { en: "Android", ko: "Android" }
  - { en: "Rated 3+", ko: "3세 이상" }
  - { en: "Contains ads", ko: "광고 포함" }

images:
  icon: /assets/img/aeroshoot-icon-sm.webp        # 192×192
  keyart: /assets/img/aeroshoot-keyart.webp       # 1024×500 (메인 카드 상단, 공유 이미지)
  logo: /assets/img/aeroshoot-logo.webp           # 투명 배경 로고 (없으면 제목 텍스트로 대체)
  logo_width: 440
  screenshots:                                    # 가로 600px 권장
    - { src: /assets/img/aeroshoot-shot-1.webp, alt: "Aeroshoot level: a portrait drawn in rainbow arrows" }
    - { src: /assets/img/aeroshoot-shot-2.webp, alt: "Aeroshoot level screenshot" }
    - { src: /assets/img/aeroshoot-shot-3.webp, alt: "Aeroshoot level: a high heel drawn in arrows over a city skyline" }
    - { src: /assets/img/aeroshoot-shot-4.webp, alt: "Aeroshoot level screenshot" }
    - { src: /assets/img/aeroshoot-shot-5.webp, alt: "Aeroshoot level: The Scream drawn in arrows" }
video:                                            # 없으면 첫 스크린샷이 대신 표시됨
  src: /assets/video/aeroshoot-play.mp4
  poster: /assets/video/aeroshoot-play-poster.jpg
hero_bg:                                          # 상세 페이지 상단의 흐릿한 배경. 없으면 keyart를 흐리게 사용
  video: /assets/video/aeroshoot-reveal.mp4

how_to_play_title:
  en: "Three rules. That's the whole tutorial."
  ko: "규칙은 셋. 튜토리얼은 그게 전부."
how_to_play:
  - title: { en: "Read the board", ko: "보드를 읽는다" }
    text:  { en: "Each arrow points the way it will fly. Look for one with a clear runway.", ko: "화살표는 자기가 날아갈 방향을 가리킵니다. 길이 비어 있는 것부터 찾아보세요." }
  - title: { en: "Tap to shoot", ko: "탭해서 쏜다" }
    text:  { en: "Tap it and it zips off the board. Blocked? It bounces back — try another.", ko: "탭하면 보드 밖으로 날아갑니다. 막혀 있으면 튕겨 돌아오니 다른 화살표를 찾아보세요." }
  - title: { en: "Clear the picture", ko: "그림을 완성한다" }
    text:  { en: "Empty the board to complete the artwork — and the melody.", ko: "보드를 모두 비우면 그림과 멜로디가 완성됩니다." }

features_title:
  en: "Simple to tap, surprisingly deep."
  ko: "탭은 단순하게, 깊이는 의외로."
features:                                         # icon: picture, music, bulb, heart, gem, boost, clock, plan, zap, repeat, star
  - icon: picture
    title: { en: "Picture levels", ko: "그림이 되는 레벨" }
    text:  { en: "Faces, landmarks, high heels, even The Scream — every board is a drawing waiting to be revealed.", ko: "인물, 랜드마크, 하이힐, 그리고 절규까지. 모든 보드가 하나의 그림입니다." }
  - icon: music
    title: { en: "Musical feedback", ko: "음악이 되는 클릭" }
    text:  { en: "Each successful tap plays a rising note. Chain them and the level plays its own melody.", ko: "성공할 때마다 한 음씩 올라갑니다. 이어서 맞추면 레벨이 스스로 멜로디를 연주합니다." }
  - icon: bulb
    title: { en: "Helpers when stuck", ko: "막힐 때의 도우미" }
    text:  { en: "Undo, restart, hint and zoom are one tap away.", ko: "되돌리기·재시작·힌트·확대가 한 탭 거리에 있습니다." }
  - icon: heart
    title: { en: "Three hearts", ko: "세 개의 하트" }
    text:  { en: "A wrong tap costs a heart — just enough tension to keep you sharp.", ko: "잘못 누르면 하트가 하나 줄어듭니다. 긴장감은 딱 그만큼." }

screenshots_title:
  en: "A gallery you solve."
  ko: "풀어서 완성하는 갤러리."
cta:
  en: "Ready to shoot some arrows?"
  ko: "화살표를 날릴 준비 되셨나요?"
---
