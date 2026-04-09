---
source: oper-analytics.md
section: "Sales Statistics"
order: 3
split: true
created_date_time: 20260408_184906
keyword: Console, Login, Purchase
---

## Sales Statistics
### Payment Amount
![analytics_10](./image/analytics_10_kr_240103.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔의 결제 금액(Payment Amount) 조회 화면
    구성: 상단에 조회 기간 설정 및 필터 옵션이 있고, 중앙에 결제 금액 현황 표(총 결제금액, 국가별 금액)와 매출 추이를 보여주는 바 차트(신규 매출/재구매 매출)와 라인 그래프(PU)가 표시됨. 하단에 스토어/국가/IdP별 매출 상세 데이터 테이블이 나열됨
    Keyword: Analytics, Console, Screenshot, Payment Amount, 결제금액, 매출 추이
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
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔의 유료 이용자(Paying User) 조회 화면
    구성: 상단에 조회 기간 및 필터가 있고, 좌측에 PU/NPU/재구매PU를 보여주는 바 차트, 우측에 ARPPU 추이 라인 그래프가 표시됨. 하단에 일자별 결제금액, DAU, PU, NPU, PUR, ARPU, ARPPU 등 상세 지표가 테이블로 나열됨
    Keyword: Analytics, Console, Screenshot, Paying User, PU, ARPPU, NPU
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
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔의 아이템 매출(Item Sales) 조회 화면
    구성: 상단에 조회 기간 및 필터가 있고, 좌측에 Best Item Top 10 테이블(아이템명, 스토어, 결제금액, 결제건수, PU, 결제비율), 우측에 스토어별 결제 비율을 보여주는 도넛 차트가 표시됨. 하단에 스토어별 아이템 상세 매출 데이터 테이블이 나열됨
    Keyword: Analytics, Console, Screenshot, Item Sales, 아이템 매출, 도넛 차트
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
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔의 첫 구매(First Purchase) 조회 화면
    구성: 상단에 조회 기간 및 필터가 있고, 중앙에 신규 유료 이용자의 가입 후 첫 구매까지 소요 기간을 D+0일부터 D+90일 경과까지 보여주는 테이블이 표시됨. 하단에 신규 PU가 구매한 아이템 목록(아이템명, 스토어, NPU, 결제금액)이 테이블로 나열됨
    Keyword: Analytics, Console, Screenshot, First Purchase, NPU, 첫 구매
-->

신규 유료 이용자의 첫 구매에 관한 정보를 확인할 수 있습니다.

신규 유료 이용자의 가입 후 첫 구매까지의 소요 기간을 D+0일부터 D+90일 경과까지 보여줍니다.

신규 유료 이용자가 구입한 모든 아이템을 결제 금액 순으로 보여줍니다.

* 아이템: 신규 PU가 구매한 아이템 목록
* 스토어: 앱스토어, 구글플레이스토어 등과 같은 스토어
* 신규 PU(NPU): 유료 상품을 처음 결제한 이용자 (New Paying Users)
* 신규 결제금액: 신규 PU가 발생시킨 결제금액
