---
source: console-apple-guide.md
section: "(구)영수증 검증+Notification V1 (Deprecated 예정)"
order: 3
split: true
created_date_time: 20260408_191848
keyword: Console, Purchase, Alert
---

## (구)영수증 검증+Notification V1 (Deprecated 예정)
- Apple 구독 상품 결제를 사용하려면 App Store Connect에서 **공유 암호** 생성 및 **Notification V1 URL** 설정이 필요합니다.
- 공유 암호는 스토어 정보에 등록합니다.
- Apple 일반 상품 결제는 별도 설정이 필요하지 않습니다.

### 공유 암호 생성
> **참고**
> 모든 앱에 대한 단일 암호인 **기본 공유 암호** 또는 개별 앱에 대한 **앱 공유 암호**를 생성할 수 있습니다.
> [https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-a-shared-secret-to-verify-receipts](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-a-shared-secret-to-verify-receipts)

#### 기본 공유 암호
1. **App Store Connect** > **사용자 및 액세스** > **통합** 탭 클릭
2. **생성** 클릭
![[]](http://static.toastoven.net/prod_gamebase/StoreConsoleGuide/AppStore/ko/app_store_connect_02_ko_240226.png)

#### 앱 공유 암호
1. **App Store Connect** > **앱** > **앱 선택** > **배포** > **일반 정보** > **앱 정보** > **앱 공유 암호** > **관리** 클릭
2. **생성** 클릭
![[]](http://static.toastoven.net/prod_gamebase/StoreConsoleGuide/AppStore/ko/app_store_connect_03_ko_240226.png)

### 스토어 정보 등록에 Shared Secret 입력
1. [콘솔](https://console.nhncloud.com)에서 조직 및 프로젝트를 선택하고 
**Game** > **Gamebase** > **구매(IAP)** > **스토어** > **등록** 또는 App을 선택하고 **수정**을 클릭
2. Store APP ID: **App Bundle ID** 입력
3. 영수증 검증 및 노티 방식: **(구)영수증 검증+Notification V1** 선택
4. Shared Secret 입력
![[]](http://static.toastoven.net/prod_gamebase/StoreConsoleGuide/AppStore/ko/store_info_02_ko_240226.png)

### Notification V1 URL 등록
1. **App Store Connect** > **앱** > **앱 선택** > **일반 정보** > **앱 정보** > **App Store 서버 알림**
2. **프로덕션 서버 URL** 또는 **Sandbox 서버 URL** 편집 클릭
3. 알림 버전: **버전 1 알림** 선택
4. 서버 URL: `https://api-iap.cloud.toast.com/callback/subscription/{APP_BUNDLE_ID}/AS` 입력
