---
# ───────── 새 게임 템플릿 ─────────
# 1) 이 파일을 _games/새게임이름.md 로 복사 (파일명이 주소가 됨: /games/새게임이름/)
# 2) 아래 값 채우기  3) 이미지를 assets/img/ 에 넣기  4) GitHub에 push
title: New Game
order: 3                      # 메인 노출 순서
status: soon                  # live | soon  (soon이면 스토어 버튼 대신 '출시 예정' 표시)
store_url: ""                 # 출시 후 Google Play 주소 입력
accent: "#a855f7"             # 포인트 컬러

title_en: "New Game — Puzzle by Neon Knuckle"
title_ko: "New Game — 네온너클의 퍼즐"
description_en: "One-line description for search engines."
description_ko: "검색 결과에 보일 한 줄 설명."

genre:    { en: "Puzzle", ko: "퍼즐" }
tagline:  { en: "Short punchy tagline.", ko: "짧고 강한 한 줄." }

pitch:
  en: "Two sentences for the home-page card."
  ko: "메인 카드에 들어갈 두 문장."
highlights:
  - { en: "Highlight one", ko: "특징 하나" }
  - { en: "Highlight two", ko: "특징 둘" }
  - { en: "Highlight three", ko: "특징 셋" }

lead:
  en: "Three or four sentences for the detail page hero."
  ko: "상세 페이지 상단에 들어갈 서너 문장."
badges:
  - { en: "Android", ko: "Android" }
  - { en: "Contains ads", ko: "광고 포함" }

images:
  icon: /assets/img/newgame-icon-sm.webp        # 192×192
  keyart: /assets/img/newgame-keyart.webp       # 1024×500
  logo: /assets/img/newgame-logo.webp           # 투명 배경 로고. 없으면 이 줄 삭제 → 제목 텍스트로 표시
  logo_width: 420
  screenshots:                                  # 가로 600px 권장. 없으면 섹션 자체가 숨겨짐
    - { src: /assets/img/newgame-shot-1.webp, alt: "Screenshot 1" }
    - { src: /assets/img/newgame-shot-2.webp, alt: "Screenshot 2" }
video:                                          # 없으면 첫 스크린샷이 폰 프레임에 표시됨
  src: /assets/video/newgame-play.mp4
  poster: /assets/video/newgame-play-poster.jpg
# hero_bg:                                        # (선택) 상세 상단의 흐릿한 배경 영상/이미지. 없으면 keyart를 흐리게 사용
#   video: /assets/video/newgame-reveal.mp4
#   image: /assets/img/newgame-keyart.webp

how_to_play_title: { en: "How it works", ko: "이렇게 플레이해요" }
how_to_play:                                    # 섹션을 빼려면 how_to_play 블록 전체 삭제
  - title: { en: "Step one", ko: "첫 번째" }
    text:  { en: "What the player does first.", ko: "처음에 하는 것." }
  - title: { en: "Step two", ko: "두 번째" }
    text:  { en: "Then this.", ko: "그 다음." }
  - title: { en: "Step three", ko: "세 번째" }
    text:  { en: "And the payoff.", ko: "그리고 보상." }

features_title: { en: "Why you'll keep playing", ko: "계속 하게 되는 이유" }
features:                                       # icon: picture, music, bulb, heart, gem, boost, clock, plan, zap, repeat, star
  - icon: star
    title: { en: "Feature", ko: "특징" }
    text:  { en: "One sentence.", ko: "한 문장." }
  - icon: clock
    title: { en: "Feature", ko: "특징" }
    text:  { en: "One sentence.", ko: "한 문장." }

screenshots_title: { en: "Screenshots", ko: "스크린샷" }
cta: { en: "Ready to play?", ko: "플레이할 준비 되셨나요?" }
---
