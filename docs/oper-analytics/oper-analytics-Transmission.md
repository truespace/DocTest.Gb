---
source: oper-analytics.md
section: "Transmission"
order: 5
split: true
created_date_time: 20260408_184906
keyword: Console, Login, Purchase, Analytics
---

## Transmission

**전송 지표** 탭은 게임에서 API로 지표를 전송할 때 확인할 수 있습니다.
전송 지표의 종류는 아래 3개입니다.

* 이용자 레벨: 이용자 레벨별로 접속과 매출 정보를 확인할 수 있습니다.
* 월드/서버/채널: 월드/서버/채널별로 접속과 매출 정보를User IdUser Id 확인할 수 있습니다.
* 클래스/직업: 클래스/직업별로 접속과 매출 정보를 확인할 수 있습니다.

> [참고] 
>
> 월드/서버/채널, 클래스/직업은 사전에 등록된 정보만 처리 합니다.
> 등록 방법은 다음 문서를 참고하시기 바랍니다
>
> - [앱 > Analytics Indicator](../oper-app.md#analytics-indicator)

### Concurrent Status

선택된 전송 지표 종류와 날짜의 접속, 매출 정보를 확인할 수 있습니다.
동시 접속자는 당일은 CCU를 제공하며, 일자별은 DAU 정보를 제공합니다. 당일이면 10분 단위로 정보가 갱신됩니다.
![analytics_16](./image/analytics_16_kr_240103.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔 Concurrent Status 화면 #16
    구성: Gamebase Analytics 콘솔의 Concurrent Status 기능 설정/조회 화면 스크린샷
    Keyword: Analytics, Console, Screenshot, Concurrent Status
-->

* CCU (Concurrent User): 10분 단위로 측정된 실시간 동시 접속자 수(로그인 이용자 수)
* DAU (Daily Active User): 일간 이용자 아이디 기준, 로그인 1회 이상 액티브 이용자 수
* NRU (New Registered User): 당일 신규 가입자
* 결제 건수: 유료 상품 결제 건수
* 결제 금액: 유료 상품 결제 금액

### Status By Level

레벨별로 접속, 매출 현황을 확인할 수 있습니다.
![analytics_17](./image/analytics_17_kr_240103.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔 Status By Level 화면 #17
    구성: Gamebase Analytics 콘솔의 Status By Level 기능 설정/조회 화면 스크린샷
    Keyword: Analytics, Console, Screenshot, Status By Level
-->

* DAU (Daily Active User): 일간 이용자 아이디 기준, 로그인 1회 이상 액티브 이용자 수
* Avg.Playtime: 해당 레벨의 일자별 전체 Playtime의 평균(DAU의 Playtime의 합 / DAU)
* 결제 금액: 유료 상품 결제 금액
* 신규 결제: 신규 결제 이용자(NPU)가 결제한 금액
* 재구매 결제: 재구매 결제 이용자가 결제한 금액
* PU (Paying User): 유료 상품을 결제한 이용자.(=재구매 PU + 신규 PU)
* 신규 PU: 유료 상품을 처음 결제한 이용자
* 재구매 PU: 전체 PU - 신규 PU(재구매 PU는 일간 데이터로 전일 기준으로 계산)

### Status By Channel

월드/서버/채널별로 접속, 매출 현황을 확인할 수 있습니다.
![analytics_18](./image/analytics_18_kr_240103.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔 Status By Channel 화면 #18
    구성: Gamebase Analytics 콘솔의 Status By Channel 기능 설정/조회 화면 스크린샷
    Keyword: Analytics, Console, Screenshot, Status By Channel
-->

* DAU (Daily Active User): 일간 이용자 아이디 기준, 로그인 1회 이상 액티브 이용자 수
* Avg.Playtime: 해당 레벨의 일자별 전체 Playtime의 평균(DAU의 Playtime의 합 / DAU)
* 결제 금액: 유료 상품 결제 금액
* 신규 결제: 신규 결제 이용자(NPU)가 결제한 금액
* 재구매 결제: 재구매 결제 이용자가 결제한 금액
* PU (Paying User): 유료 상품을 결제한 이용자(= 재구매 PU + 신규 PU)
* 신규 PU: 유료 상품을 처음 결제한 이용자
* 재구매 PU: 전체 PU - 신규 PU(재구매 PU는 일간 데이터로 전일 기준으로 계산)

### Status By Class

클래스/직업별로 접속, 매출 현황을 확인할 수 있습니다.
![analytics_19](./image/analytics_19_kr_240103.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔 Status By Class 화면 #19
    구성: Gamebase Analytics 콘솔의 Status By Class 기능 설정/조회 화면 스크린샷
    Keyword: Analytics, Console, Screenshot, Status By Class
-->

* DAU (Daily Active Users): 일간 이용자 아이디 기준, 로그인 1회 이상 액티브 이용자 수
* Avg.Playtime: 해당 레벨의 일자별 전체 Playtime의 평균(DAU의 Playtime의 합 / DAU)
* 결제 금액: 유료 상품 결제 금액
* 신규 결제: 신규 결제 이용자(NPU)가 결제한 금액
* 재구매 결제: 재구매 결제 이용자가 결제한 금액
* PU (Paying User): 유료 상품을 결제한 이용자.(=재구매 PU + 신규 PU)
* 신규 PU: 유료 상품을 처음 결제한 이용자
* 재구매 PU: 전체 PU - 신규 PU(재구매 PU는 일간 데이터로 전일 기준으로 계산)

### Level Up

이용자들의 레벨 업 정보를 확인할 수 있습니다.

* 달성 레벨: 달성한 레벨
* 레벨 업 달성 이용자: 해당 레벨을 달성한 이용자 수
* 레벨 업 평균 달성 시간(분): 해당 레벨을 달성한 이용자들의 평균 달성 시간(분)
![analytics_20](./image/analytics_20_kr_240103.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔 Level Up 화면 #20
    구성: Gamebase Analytics 콘솔의 Level Up 기능 설정/조회 화면 스크린샷
    Keyword: Analytics, Console, Screenshot, Level Up
-->

### Item Sales Status
선택된 전송 지표 종류에 따른 아이템 판매 현황을 확인할 수 있습니다.
**조건** 버튼을 클릭해, 아래의 조횟값을 선택할 수 있습니다.

* 결제 금액
* 결제 건수
* PU (Paying User)
* 신규 PU
![analytics_21](./image/analytics_21_kr_240103.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔 Item Sales Status 화면 #21
    구성: Gamebase Analytics 콘솔의 Item Sales Status 기능 설정/조회 화면 스크린샷
    Keyword: Analytics, Console, Screenshot, Item Sales Status
-->

### Item Sales TOP 50

선택된 전송 지표 종류 및 값에 따른 아이템 판매 상위 50개 항목을 확인할 수 있습니다.

![analytics_22](./image/analytics_22_kr_240103.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Gamebase Analytics 콘솔 Item Sales TOP 50 화면 #22
    구성: Gamebase Analytics 콘솔의 Item Sales TOP 50 기능 설정/조회 화면 스크린샷
    Keyword: Analytics, Console, Screenshot, Item Sales TOP 50
-->
