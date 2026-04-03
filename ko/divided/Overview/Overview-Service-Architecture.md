---
source: Overview.md
section: "Service Architecture"
order: 4
created_date: 2026-04-03
---

## Service Architecture
다음은 Gamebase 서비스 구조도와 간단한 설명입니다.
![논리 구성도](./image/Gamebase_overview_03_202203.png)
<br>

| 컴포넌트명           | 설명                                       |
| --------------- | ---------------------------------------- |
| Gamebase SDK    | - 클라이언트 개발을 위한 SDK                       |
| Gamebase Server | - 내부/외부 모듈 간의 매시업 API(mashup API)를 제공하고 내부 로직을 처리 <br>- 클라이언트 초기 실행 시 데이터 제공 <br>- 사용자 구분 키 발급과 관리, 매핑 관리 <br>- 게임별 동시 접속 지표 수집 및 관리 |
| Console         | - 웹 Console                              |
