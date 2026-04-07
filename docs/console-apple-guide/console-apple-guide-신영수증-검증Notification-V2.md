---
source: console-apple-guide.md
split: true
created_date_time: 20260406_141859
keyword: "(신)영수증 검증+Notification V2, 앱 내 구입 키 생성, Gamebase 정보에 앱 내 구입 키 입력, Notification V2 URL 등록"
section: "(신)영수증 검증+Notification V2"
order: 2
---

## (신)영수증 검증+Notification V2
### 앱 내 구입 키 생성
> **참고** 
> [https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-keys-for-in-app-purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-keys-for-in-app-purchases)

1. **App Store Connect** > **사용자 및 액세스** > **통합** 탭 클릭
2. **키** > **앱 내 구입** 클릭
3. **앱 내 구입 키 생성** 클릭
4. 키 이름 입력 후 **생성** 클릭
5. **앱 내 구입 키 다운로드** 클릭
![[]](http://static.toastoven.net/prod_gamebase/StoreConsoleGuide/AppStore/ko/app_store_connect_01_ko_240226.png)

### Gamebase 정보에 앱 내 구입 키 입력
1. [콘솔](https://console.nhncloud.com)에서 조직 및 프로젝트를 선택하고 **Game** > **Gamebase** > **구매(IAP)** > **스토어** > **등록** 또는 App을 선택하고 **수정**을 클릭
2. Store APP ID: **App Bundle ID** 입력
3. 영수증 검증 및 노티 방식: **(신)영수증 검증+Notification V2** 선택
4. 다운로드한 앱 내 구입 키, Key ID, Issuer ID 입력
![[]](http://static.toastoven.net/prod_gamebase/StoreConsoleGuide/AppStore/ko/store_info_01_ko_240226.png)

### Notification V2 URL 등록
1. **App Store Connect** > **앱** > **앱 선택** > **일반 정보** > **앱 정보** > **App Store 서버 알림**
2. **프로덕션 서버 URL** 또는 **Sandbox 서버 URL** 편집 클릭
3. 알림 버전: **버전 2 알림** 선택
4. 서버 URL: `https://api-iap.cloud.toast.com/callback/subscription/{APP_BUNDLE_ID}/AS/v2` 입력
