---
source: Overview.md
section: "Service Architecture"
order: 4
split: true
created_date_time: 20260408_184906
keyword: Mapping, Console, Overview
---

## Service Architecture
다음은 Gamebase 서비스 구조도와 간단한 설명입니다.
![논리 구성도](./image/Gamebase_overview_03_202203.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Diagram
    내용: Gamebase 서비스 아키텍처 구조도
    구성: 게임 서버와 게임 클라이언트가 Gamebase SDK, Gamebase 서버, Gamebase 콘솔, 데이터베이스와 연동되는 구조를 나타내며, NHN Cloud 서비스(IAP, Push, LeaderBoard, AppGuard, Launching)와의 연결 관계를 보여주는 시스템 아키텍처 다이어그램
    Keyword: Diagram, Service Architecture, Gamebase Server, NHN Cloud
-->
<br>

| 컴포넌트명           | 설명                                       |
| --------------- | ---------------------------------------- |
| Gamebase SDK    | - 클라이언트 개발을 위한 SDK                       |
| Gamebase Server | - 내부/외부 모듈 간의 매시업 API(mashup API)를 제공하고 내부 로직을 처리 <br>- 클라이언트 초기 실행 시 데이터 제공 <br>- 사용자 구분 키 발급과 관리, 매핑 관리 <br>- 게임별 동시 접속 지표 수집 및 관리 |
| Console         | - 웹 Console                              |
