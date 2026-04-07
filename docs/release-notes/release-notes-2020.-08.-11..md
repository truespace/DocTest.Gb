---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v2.14.0, 기능개선, 기능추가, 변경, 제거, Analytics, Coupon, Error"
section: "2020. 08. 11."
order: 22
---

### 2020. 08. 11.

#### 기능 개선/변경
* [Console]
    * Analytics > 이용자 지표 > Retention: % 외에 수치를 추가로 표시
* [SDK] 2.14.0
    * (iOS) PAYCO IdP의 상수값 제거: PAYCO 문자열로 인한 애플 검수가 리젝되는 경우가 발생하여 제거
    * (iOS, Unity) TCGBWebViewConfiguration에 contentMode 설정 추가
* [Server]
    * 쿠폰 소진 API의 오류 코드 추가: 쿠폰 코드에 영문, 숫자 이외의 값을 입력한 경우(Error Code:-4000205)
