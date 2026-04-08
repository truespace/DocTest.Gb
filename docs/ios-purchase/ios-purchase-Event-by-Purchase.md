---
source: ios-purchase.md
section: "Event by Purchase"
order: 10
split: true
created_date_time: 20260408_191848
keyword: iOS, Purchase, Authentication, Console
---

### Event by Purchase

App Store 프로모션 상품 구매가 완료되거나, Ask to Buy 등으로 지연된 결제가 완료되었을 때, GamebaseEventHandler를 이용해 이벤트를 받아 처리할 수 있습니다.
GamebaseEventHandler로 지연 결제 이벤트를 처리하는 방법은 아래 가이드를 확인하세요.
[Game > Gamebase > iOS SDK 사용 가이드 > ETC > Gamebase Event Handler](../ios-etc.md#purchase-updated)


#### Caution for Usage
Facebook SDK, Google Mobile Ads SDK와 같이 SDK 내에 In App Purchase(App Store 결제) 기능이 있는 경우 Gamebase Login을 하기 전에 App Store 프로모션 결제를 시작하면 정상적으로 결제창이 나타나지 않을 수 있습니다.

* 해결 방법
  * Facebook
    * Facebook Console > 설정 > 기본 설정 > **앱 내 이벤트를 자동으로 로깅(권장)** 기능을 비활성화
    * Facebook 인증 기능을 사용하지 않을 경우: **GamebaseAuthFacebookAdapter.xcframework 파일을 제외**시킨 후 빌드
