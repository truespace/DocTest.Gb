---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.43.0 (2022. 09. 07.)"
section: "2.43.0 (2022. 09. 07.)"
order: 50
---

### 2.43.0 (2022. 09. 07.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.43.0/GamebaseSDK-Android.zip)

#### 기능 추가
* ONE store v19 Purchase Adapter가 추가되었습니다.
    * 빌드 의존성에 **gamebase-adapter-purchase-onestore-v19** 모듈 및 [ONE store v19 IAP SDK를 추가](https://github.com/ONE-store/onestore_iap_release/tree/iap19-release/android_app_sample/app/libs)하면 사용 가능합니다.
            
            dependencies {
                ...
                implementation files('libs/iap_sdk-v19.00.02.aar')
                implementation "com.toast.android.gamebase:gamebase-adapter-purchase-onestore-v19:$GAMEBASE_SDK_VERSION"
            }
            
#### 기능 개선/변경
* 외부 SDK 업데이트: Google Billing Client(5.0.0), NHN Cloud Android SDK(1.1.0), TOAST Gamebase IAP Android SDK(0.20.0), Kakaogame Android SDK(3.14.4)
* LINE 로그인을 수행 시 서비스를 제공할 Region을 입력할 수 있는 파라미터가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Login with IdP](../../aos-authentication.md#login-with-idp)
* LINE IdP 사용 시 LINE IdP에서 지원하지 않는 API 19 미만 단말기에서도 크래시가 발생하지 않도록 방어 로직을 추가했습니다.

#### 버그 수정
* Naver PLUG SDK나 Naver Cafe SDK 사용을 위해 Naver Login SDK 버전을 4.1.4로 강제로 낮추는 경우 크래시가 발생하는 이슈를 수정했습니다.
