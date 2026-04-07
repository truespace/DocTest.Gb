---
source: oper-analytics.md
split: true
created_date_time: 20260406_141859
keyword: "Console, Analytics, Concurrent Group User"
section: "Concurrent Group User"
order: 4
---

## Concurrent Group User
### Concurrent Group User
![analytics_14](./image/analytics_14_kr_240103.png)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Gamebase Analytics 그룹 지표 - 그룹 동접 현황
    구성: 상단에 그룹 지표 탭과 날짜/필터 선택이 있음. 실시간 그룹 동접을 보여주는 누적 막대 그래프(OS별 색상 구분)가 있고, 프로젝트 그룹 동접 추이 꺾은선 그래프, 신규 가입자 추이, 결제 금액 추이 그래프가 세로로 배치됨
    Keyword: 그룹 동접, CCU, 프로젝트별, 누적 막대그래프, 신규 가입자, 결제 금액
-->

Gamebase 서비스 이용자가 속한 모든 프로젝트의 동접 지표를 확인할 수 있습니다.

* 실시간 그룹 동접: Gamebase 서비스 이용자가 속한 프로젝트의 실시간 동접자(CCU)를 나타냅니다.
* 프로젝트 그룹 동접: 선택된 기간, 필터를 기준으로 앱 이용자 수가 나타납니다.

### Group Comparison
![analytics_15](./image/analytics_15_kr_240103.png)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Gamebase Analytics 그룹 비교 지표
    구성: 상단에 그룹 비교 탭과 날짜/필터/그룹 선택이 있음. DAU, NRU, PU, 결제금액 각각의 추이를 프로젝트 그룹별로 색상이 다른 꺾은선 그래프로 비교하여 세로 나열함
    Keyword: 그룹 비교, DAU, NRU, PU, 결제금액, 꺾은선 그래프, 프로젝트별
-->

Gamebase 서비스 이용자가 속한 프로젝트들을 필터와 조합하여 그룹으로 비교할 수 있습니다.

* DAU: 일간 memberno 기준 로그인 1회 이상 액티브 이용자 수 (Daily Active Users)
* NRU: 당일 신규 가입자
* PU: 유료상품을 결제한 이용자 (Paying User). (=재구매 PU + 신규 PU)
* 결제금액: 이용자가 결제한 결제금액

※ 그래프에 표시되는 그룹명은 **{appId} _ {OS} _ {국가}** 형태입니다.
