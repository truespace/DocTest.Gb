---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Kotlin, v2.25.0, 기능개선, 기능추가, 변경, Push, TermsView"
section: "2.25.0 (2021.07.27)"
order: 72
---

### 2.25.0 (2021.07.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.25.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 월 결제 한도 기능 추가
    * 월 결제 한도를 넘는 경우 **PURCHASE_LIMIT_EXCEEDED(4007)** 에러가 발생합니다.

#### 기능 개선/변경
* Android Support Library 의존성을 AndroidX 로 변경
* Push 항목이 존재하는 약관에서 PushConfiguration 객체 보장
    * 약관 UI에서 Push 수신 동의를 하지 않을 경우 Gamebase.Terms.showTermsView API 호출 결과로 생성되는 PushConfiguration이 null이었으나, 약관에 Push 항목이 존재한다면 PushConfiguration 객체가 항상 반환되도록 변경되었습니다.
    * Push 수신 거부 시 PushConfiguration 객체는 (푸시 동의 여부 = false, 광고성 푸시 동의 여부 = false, 야간 광고성 푸시 동의 여부 = false) 로 생성됩니다.
    * 약관에 Push 항목이 존재하지 않는다면 PushConfiguration 객체는 null입니다.
* 외부 SDK 업데이트
    * TOAST Android SDK(0.26.0)
    * Kotlin(1.5.21)
    * Google Play Services Auth(19.0.0)
    * Facebook Android SDK(11.1.0)
    * NAVER Android SDK(4.4.1)
    * LINE Android SDK(5.6.2)
    * Weibo Android SDK(11.6.0)
* Weibo 로그인시 발생하는 크래시 수정
