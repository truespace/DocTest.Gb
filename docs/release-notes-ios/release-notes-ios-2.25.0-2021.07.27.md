---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.25.0, 버그수정, 기능개선, 기능추가, 변경, Push, TermsView"
section: "2.25.0 (2021.07.27)"
order: 73
---

### 2.25.0 (2021.07.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.25.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 월 결제 한도 기능 추가
    * 월 결제 한도를 넘는 경우 **PURCHASE_LIMIT_EXCEEDED(4007)** 에러가 발생합니다.

#### 기능 개선/변경
* Push 항목이 존재하는 약관에서 PushConfiguration 객체 보장
    * 약관 UI 에서 Push 수신 동의를 하지 않을 경우 Gamebase.Terms.showTermsView API 호출 결과로 생성되는 TCGBPushConfiguration 이 null이었으나, 약관에 Push 항목이 존재한다면 TCGBPushConfiguration 객체가 항상 반환되도록 변경되었습니다.
    * Push 수신 거부 시 TCGBPushConfiguration 객체는 (푸시 동의 여부 = false, 광고성 푸시 동의 여부 = false, 야간 광고성 푸시 동의 여부 = false)로 생성됩니다.
    * 약관에 Push 항목이 존재하지 않는다면 TCGBPushConfiguration 객체는 null입니다.
* 외부 SDK 업데이트: TOAST iOS SDK(0.29.0)
* Sign In with Apple 의 ASAuthorizationErrorUnknown 에러가 발생했을 경우, TCGB_ERROR_AUTH_EXTERNAL_LIBRARY_ERROR 에러를 반환하도록 변경

#### 버그 수정
* registerPush 를 통해 등록한 TCGBPushConfiguration 값과 TCGBPushTokenInfo 값이 달라지게 되는 버그 수정
