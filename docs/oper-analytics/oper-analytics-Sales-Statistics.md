---
source: oper-analytics.md
split: true
created_date_time: 20260406_141859
keyword: "Sales Statistics, Payment Amount, Paying User, Item Sales, First Purchase"
section: "Sales Statistics"
order: 3
---

## Sales Statistics
### Payment Amount
![analytics_10](./image/analytics_10_kr_240103.png)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Gamebase Analytics 매출 지표 - 결제 금액 현황
    구성: 상단에 매출 지표 탭과 날짜/필터 선택이 있고, 주요 결제 금액 수치 카드가 표시됨. 중앙에 일별 결제금액 추이를 보여주는 막대/꺾은선 복합 차트가 있으며, 하단에 스토어별/국가별 매출 상세 데이터 테이블이 배치됨
    Keyword: 매출 지표, 결제 금액, 막대차트, 꺾은선 그래프, 스토어별 매출
-->

결제 금액에 대한 지표를 확인할 수 있습니다.

#### 1. 결제 금액 현황 표
선택된 기간 동안의 결제 금액을 보여줍니다.
총 결제금액과 주요 스토어의 국가 별 결제금액을 확인할 수 있습니다.

#### 2. 매출 추이
일자별로 신규 매출, 재구매 매출, PU(결제 이용자)의 추이를 그래프로 확인할 수 있습니다.
아래의 표에서는 스토어, 국가, IdP별 매출을 확인할 수 있습니다.
일간 조회 시에만 월 단위 누적 결제 금액을 확인할 수 있습니다.

### Paying User
![analytics_11](./image/analytics_11_kr_240103.png)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Gamebase Analytics 매출 지표 - 유료 이용자(PU) 현황
    구성: 상단에 결제 이용자 탭과 날짜/필터 선택이 있고, 좌측에 PU 관련 막대 그래프(PU, 신규 PU, 재구매 PU), 우측에 ARPPU 추이 꺾은선 그래프가 있음. 하단에 날짜별 결제금액, DAU, PU, NPU, ARPU, ARPPU 등 상세 데이터 테이블이 배치됨
    Keyword: PU, 유료 이용자, ARPPU, ARPU, NPU, 결제 이용자
-->

유료 이용자(PU)에 관한 지표를 확인할 수 있습니다.
아래는 그래프와 표에 나온 용어 설명입니다.

* 결제금액: 이용자가 결제한 결제금액
* 신규 결제금액: 신규 결제 이용자(NPU)가 결제한 결제금액
* DAU: 일간 memberno 기준 로그인 1회 이상 액티브 이용자수 (Daily Active Users)
* PU: 유료상품을 결제한 이용자 (Paying User). PU=재구매PU + 신규PU
* 신규 PU(NPU): 유료 상품을 처음 결제한 이용자 (New Paying Users)
* 재구매 PU: 누적 PU - 신규 PU (재구매 PU 는 일간 data 로 전일자 기준으로 계산)
* PUR: 유료 이용자의 비율 (PU/DAU * 100)
* ARPU: 하루 동안 게임 이용자 수의 평균 결제 금액 (결제 금액/DAU)
* ARPPU: 결제 이용자 수의 평균 결제 금액 (결제 금액/PU)
* ARPNPU: 신규 유료 이용자의 평균 결제 금액 (결제 금액/NPU)
* 누적 PU(M): 월 단위의 결제 이용자 수(중복 제외)

### Item Sales
![analytics_12](./image/analytics_12_kr_240103.png)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Gamebase Analytics 매출 지표 - 아이템별 판매 현황
    구성: 상단에 아이템별 판매 탭과 날짜/필터 선택이 있고, 좌측에 Top 10 아이템 판매 순위 테이블이 있으며 우측에 스토어별 판매 비율을 보여주는 원형(도넛) 차트가 있음. 하단에 스토어별/아이템별 결제금액, 결제 건수, PU 등의 상세 데이터 테이블이 배치됨
    Keyword: 아이템 판매, Top 10, 도넛차트, 스토어별, 결제금액
-->

등록된 아이템의 판매 지표를 확인할 수 있습니다.

* 아이템: Gamebase에 등록한 아이템 목록
* Best Item Top 10: 판매금액별, 판매건수별 판매량이 높은 아이템 top 10의 List 출력
* 스토어: 앱스토어, 구글플레이스토어 등과 같은 스토어
* 결제금액: 이용자가 결제한 아이템별 결제금액
* 결제 건수: 아이템별 결제 건수
* PU: 아이템별 구매자 수
* 결제 비율: 아이템별 결제 비중

### First Purchase
![analytics_13](./image/analytics_13_kr_240103.png)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Gamebase Analytics 매출 지표 - 첫 구매(First Purchase) 현황
    구성: 상단에 첫 구매 탭과 날짜/필터 선택이 있고, 상부에 가입 후 첫 구매까지의 소요 기간을 D+0~D+90일로 보여주는 테이블이 있음. 하단에 신규 PU가 구매한 아이템 목록과 스토어, 결제금액 등의 상세 정보가 테이블로 표시됨
    Keyword: 첫 구매, First Purchase, NPU, 신규 PU, 소요 기간, 아이템
-->

신규 유료 이용자의 첫 구매에 관한 정보를 확인할 수 있습니다.

신규 유료 이용자의 가입 후 첫 구매까지의 소요 기간을 D+0일부터 D+90일 경과까지 보여줍니다.

신규 유료 이용자가 구입한 모든 아이템을 결제 금액 순으로 보여줍니다.

* 아이템: 신규 PU가 구매한 아이템 목록
* 스토어: 앱스토어, 구글플레이스토어 등과 같은 스토어
* 신규 PU(NPU): 유료 상품을 처음 결제한 이용자 (New Paying Users)
* 신규 결제금액: 신규 PU가 발생시킨 결제금액
