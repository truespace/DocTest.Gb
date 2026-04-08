---
source: release-notes-unity.md
section: "2.25.0 (2021.07.26)"
order: 69
split: true
created_date_time: 20260408_191848
keyword: Unity, Purchase, Push, Terms, Error, ShowTermsView, Release Notes, 2.25.0
---

### 2.25.0 (2021.07.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.25.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 월 결제 한도 기능 추가
    * 월 결제 한도를 넘는 경우 **PURCHASE_LIMIT_EXCEEDED(4007)** 에러가 발생합니다.

#### 기능 개선/변경
* Push 항목이 존재하는 약관에서 PushConfiguration 객체 보장
    * 약관 UI에서 Push 수신 동의를 하지 않을 경우 Gamebase.Terms.ShowTermsView API 호출 결과로 생성되는 PushConfiguration이 null이었으나, 약관에 Push 항목이 존재한다면 PushConfiguration 객체가 항상 반환되도록 변경되었습니다.
    * Push 수신 거부 시 PushConfiguration 객체는 (푸시 동의 여부 = false, 광고성 푸시 동의 여부 = false, 야간 광고성 푸시 동의 여부 = false)로 생성됩니다.
    * 약관에 Push 항목이 존재하지 않는다면 PushConfiguration 객체는 null입니다.
* Unity 최소 지원 버전 변경: 2018.4.0f1
* 외부 SDK 업데이트: TOAST Unity SDK(0.23.0)
