# HAMJI YouTube Showrunner

장르에 상관없이 사용자의 YouTube 채널을 분석하고 시장·아웃라이어·아이디어·패키징·대본·시청유지·채널 전략을 하나의 운영 시스템으로 묶는 Skill 패키지입니다.

## 목표

특정 성공 유튜버의 말투나 장르를 복제하지 않습니다. 대신 성공 채널과 성공 영상이 공통으로 보여주는 운영 원리를 추출해 사용자의 채널에 맞게 재조립합니다.

핵심 목표는 **조회수 보장**이 아니라 `50만 조회급 영상에서 기대되는 기획/패키징/훅/시청유지/보상 수준`을 제작 전에 통과시키는 것입니다.

## 구성

- `/yt-showrunner` : 전체 흐름을 지휘하는 총감독
- `/yt-market` : 시장·수요·콘텐츠 갭 탐색
- `/yt-outlier` : 채널 평균 대비 비정상적으로 잘된 영상 탐색
- `/yt-idea` : 성공 패턴을 사용자 고유 아이디어로 변환
- `/yt-package` : 제목 + 썸네일을 한 세트로 설계
- `/yt-script` : 5개 훅 생성 → 점수화 → 상위 2개 선정 → 촬영 가능한 대본 작성
- `/yt-retention` : 훅·전개·패턴 변화·보상 구조 설계
- `/yt-channel` : 단발 영상이 아니라 채널 성장 구조 설계
- `/yt-500k-gate` : 제작 전 100점 품질 심사

## `/yt-script` v0.2

`Jakeschincariol/youtube-agent-skill`의 MIT 라이선스 기반 `/yt-script` 구조에서 필요한 부분을 선별해 적용했습니다.

핵심 적용 사항:

- 21개 Hook mechanism
- Hook 5개 생성 후 실제 scorer 실행
- Specificity / Address / Stakes / Curiosity / Brevity 5개 항목 평가
- 상위 2개 Hook만 남김
- `[ON SCREEN: ...]`을 포함한 beat-by-beat 대본
- Creator Voice Profile
- 근거 없는 숫자·성과·출처 생성 금지
- 한국어 + 영어 Hook 평가 지원

실행 예:

```bash
python3 skills/yt-script/scripts/hookscore.py --hook "구독자 천 명 아래라면, 조회수 4배 차이를 만든 첫 15초부터 보여드리겠습니다."
```

점수는 **성공 예측값이 아니라 검토 신호**입니다. 낮은 점수는 다시 볼 이유이고 높은 점수가 조회수를 보장하지 않습니다.

## 500K Quality Gate

총 100점:

- Market Demand 15
- Outlier Evidence 15
- Promise Clarity 10
- Title + Thumbnail Synergy 15
- Hook Strength 10
- Retention Architecture 10
- Payoff Strength 10
- Channel Fit 5
- Series Potential 5
- Production Feasibility 5

판정:
- 80~100: GREEN — 제작 진행
- 70~79: YELLOW — 약한 항목 수정 후 재심사
- 0~69: RED — 제작 보류, 주제/패키지 재설계

## 기본 사용 순서

```text
/yt-showrunner
→ 채널 프로필 확인
→ /yt-market
→ /yt-outlier
→ /yt-idea
→ /yt-package
→ /yt-script
→ /yt-retention
→ /yt-500k-gate
→ 제작
→ 업로드 후 /yt-channel 또는 Postmortem
```

## Claude Code 설치

전역 설치:

```bash
cp -r skills/yt-* ~/.claude/skills/
```

프로젝트 로컬 설치:

```bash
mkdir -p .claude/skills
cp -r skills/yt-* .claude/skills/
```

## ChatGPT

이 저장소의 Skill들은 HAMJI YouTube Showrunner 개인 플러그인의 원본 소스로도 관리합니다. ChatGPT에서는 플러그인을 선택하거나 멘션한 뒤 `yt-script로 이 아이디어 대본 만들어줘`처럼 사용할 수 있습니다.

## 중요한 원칙

1. 성공 채널을 복제하지 않는다.
2. 성공한 이유를 구조로 추출한다.
3. 절대 조회수와 채널 평균 대비 Outlier Ratio를 함께 본다.
4. 제목과 썸네일을 따로 만들지 않는다.
5. 영상 제작 전에 패키징과 훅을 먼저 검증한다.
6. 한 편의 성공보다 다음 편으로 이어지는 구조를 우선한다.
7. 숫자·근거를 임의로 만들지 않는다.
8. 500K는 품질 기준 이름이지 조회수 보장이 아니다.

## 도구

모두 Python 표준 라이브러리만 사용합니다.

```bash
python3 tools/quality_gate.py examples/sample_quality_input.json
python3 tools/outlier_score.py templates/benchmark_log.csv
python3 tools/package_lint.py --title "제목" --thumb "썸네일 문구"
python3 skills/yt-script/scripts/hookscore.py --hook "한 줄 훅"
```

## 라이선스

HAMJI YouTube Showrunner 자체는 MIT License입니다. 오픈소스에서 실제로 참고·변형한 부분과 원 라이선스 전문은 `THIRD_PARTY_NOTICES.md`를 확인하세요.
