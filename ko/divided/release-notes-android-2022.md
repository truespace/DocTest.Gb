## Game > Gamebase > 릴리스 노트 > Android

### 2.45.0 (2022. 12. 27.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.45.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: NHN Cloud Android SDK (1.4.0), Payco Android SDK (1.5.9), Hangame Android SDK (1.6.2)
* 미소비 내역 조회 API가 변경되어 신규 API로 변경해야 합니다.

        // Deprecated API
        Gamebase.Purchase.requestItemListOfNotConsumed(Activity,
                                                       GamebaseDataCallback<List<PurchasableReceipt>>);
        
        // New API
        Gamebase.Purchase.requestItemListOfNotConsumed(Activity,
                                                       PurchasableConfiguration,
                                                       GamebaseDataCallback<List<PurchasableReceipt>>);

* 활성화 구독 조회 API가 변경되어 신규 API로 변경해야 합니다.
    * 기존 API와 동일한 결과를 받으려면 **PurchasableConfiguration.setAllStores(true)**로 설정해야 합니다.

            // Deprecated API
            Gamebase.Purchase.requestActivatedPurchases(Activity,
                                                        GamebaseDataCallback<List<PurchasableReceipt>>);

            // New API
            Gamebase.Purchase.requestActivatedPurchases(Activity,
                                                        PurchasableConfiguration,
                                                        GamebaseDataCallback<List<PurchasableReceipt>>);

#### 버그 수정

* 앱 실행 시 간헐적으로 ConcurrentModification 예외가 발생하는 문제를 수정했습니다.
* Hangame thirdIdP 로그인 후 Gamebase.getAuthProviderUserID() 호출 시 NullPointerException이 발생하는 오류를 수정했습니다.

### 2.44.2 (2022. 11. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.2/GamebaseSDK-Android.zip)

#### 기능 추가
* PurchasableReceipt VO 클래스에 'storeCode' 필드가 추가되었습니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: Kotlin (1.7.20), Hangame Android SDK (1.6.1)
* Google '사전 출시 보고서'의 권고 사항을 반영하여 Gamebase 웹뷰를 수정했습니다.
    * 타이틀 바 사이즈 확대
    * 이미지 설명 문구 수정

#### 버그 수정
* PurchasableItem VO 클래스의 'itemName' 필드에 잘못 선언된 'deprecated' 어노테이션을 제거했습니다.

### 2.44.1 (2022. 10. 25.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.1/GamebaseSDK-Android.zip)

#### 기능 추가
* Android 13 이상의 OS에서 registerPush API를 호출했을 때 Push 권한 요청 팝업이 자동으로 뜨지 않도록 할 수 있는 **PushConfiguration.Builder.enableRequestNotificationPermission(boolean)** API가 추가되었습니다.

#### 기능 개선/변경
* Facebook Android SDK 13.2.0 이상에서는 Facebook Client Token 설정이 필요합니다.
    * Gamebase Android SDK 2.44.1 이상부터는 Gamebase Console의 additionalInfo에 다음과 같이 **facebook_client_token** 필드를 추가하는 경우 Facebook Client Token이 클라이언트 SDK에 자동으로 적용됩니다.

            { "facebook_permission": [...], "facebook_client_token": "a01234bc56de7fg89012hi3j45k67890" }

#### 버그 수정
* Android 6.0(M, API Level 23) 단말기에서 **Gamebase.Push.registerPush** API를 호출하면 **IllegalArgumentException** 예외가 발생하는 버그를 수정했습니다.

### 2.44.0 (2022. 10. 11.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.44.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud Android SDK(1.2.0), TOAST Gamebase IAP Android SDK(0.21.0), Google Play Services Auth(20.0.3)
* Android 13 OS에서 registerPush 호출 시 자동으로 알림 허용 권한을 요청하는 팝업을 표시합니다.
* Google 로그인 시 silentSignIn API를 활용하도록 내부 로직을 개선했습니다.

#### 버그 수정
* Hangame IdP 로그인 시 유효한 타사 IdP를 이용한 뒤 유효하지 않은 타사 IdP로 다시 시도하면 오류가 발생하지 않고 이전 IdP로 로그인을 시도하여 크래시가 발생하는 문제를 수정했습니다.

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
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Login with IdP](./aos-authentication/#login-with-idp)
* LINE IdP 사용 시 LINE IdP에서 지원하지 않는 API 19 미만 단말기에서도 크래시가 발생하지 않도록 방어 로직을 추가했습니다.

#### 버그 수정
* Naver PLUG SDK나 Naver Cafe SDK 사용을 위해 Naver Login SDK 버전을 4.1.4로 강제로 낮추는 경우 크래시가 발생하는 이슈를 수정했습니다.

### 2.42.1 (2022. 07. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Facebook Android SDK(11.3.0)

### 2.42.0 (2022. 07. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.42.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.5.2)
* ForcingMappingTicket VO 클래스에 매핑 유저 상태를 나타내는 mappedUserValid 필드가 추가되었습니다.
* Gamebase Adapter 버전이 Gamebase 버전과 일치하지 않는 경우 런타임 예외가 발생할 수 있으므로, 초기화가 실패하도록 변경되었습니다.

#### 버그 수정
* LDPlayer에서 Naver 웹 로그인에 실패하는 현상이 수정되었습니다.
* OS 버전이 낮아 Twitter 로그인에 실패하는 경우 크래시가 발생하는 문제가 수정되었습니다.

### 2.41.2 (2022. 07. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.41.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 기본 웹뷰 설정을 '쿠키 허용'으로 변경했습니다.

### 2.41.1 (2022. 07. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.41.1/GamebaseSDK-Android.zip)

#### 버그 수정
* 약관 창의 '보기' 버튼이 동작하지 않는 버그를 수정했습니다.

### 2.41.0 (2022. 07. 05.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.41.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.31.1), Hangame Android SDK(1.4.6)
* 웹뷰에 등록한 커스텀 스킴 이벤트가 동작할 때 자동으로 웹뷰가 종료됩니다.
    * 커스텀 스킴 이벤트가 동작하더라도 웹뷰를 유지하려면 **GamebaseWebViewConfiguration.Builder.enableAutoCloseByCustomScheme(false)** API를 호출하세요.

#### 버그 수정
* Hangame IdP 로그아웃 후 로그인을 바로 시도하면 간헐적으로 크래시가 발생하거나 로그인에 실패하는 문제를 수정했습니다.

### 2.40.0 (2022. 05. 24.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.40.0/GamebaseSDK-Android.zip)

#### 기능 추가
* ONE store 외부 결제를 위한 Purchase Adapter가 추가되었습니다.
    * 빌드 의존성에 **gamebase-adapter-purchase-onestore-external** 모듈을 추가하시면 사용 가능합니다.
            
            dependencies {
                ...
                implementation "com.toast.android.gamebase:gamebase-adapter-purchase-onestore-external:$GAMEBASE_SDK_VERSION"
            }
            
#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.31.0), TOAST Gamebase IAP Android SDK(0.18.5), LINE Android SDK(5.8.0)
* 서로 다른 앱이 하나의 Gamebase 프로젝트를 공유하는 경우 푸시가 정상적으로 동작하지 않는 이슈가 수정되었습니다.
    * AndroidManifest.xml에 앱마다 서로 다른 **com.nhncloud.sdk.push.deviceId.salt** 값을 선언하시기 바랍니다.

            <!-- When you have multiple applications sharing an Gamebase project, use this field to identify each application. -->
            <meta-data android:name="com.nhncloud.sdk.push.deviceId.salt"
                       android:value="ApplicationForGoogleStore" />

### 2.39.0 (2022. 05. 10.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.39.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.30.1)

### 2.38.0 (2022. 05. 03.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.38.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Amazon(ADM) Push Adapter가 추가되었습니다.
    * 빌드 의존성에 **gamebase-adapter-push-adm** 모듈을 추가하시면 사용 가능합니다.
            
            dependencies {
                ...
                implementation "com.toast.android.gamebase:gamebase-adapter-push-adm:$GAMEBASE_SDK_VERSION"
            }
            
    * Proguard를 적용하는 경우, 다음 가이드를 확인하여 적용하셔야 합니다.
        * [NHN Cloud > SDK 사용 가이드 > TOAST Push > Android > Amazon Device Messaging 설정 > ADM SDK 다운로드](https://docs.toast.com/ko/TOAST/ko/toast-sdk/push-android/#adm-sdk)
        * [NHN Cloud > SDK 사용 가이드 > TOAST Push > Android > Amazon Device Messaging 설정 > Proguard 설정](https://docs.toast.com/ko/TOAST/ko/toast-sdk/push-android/#proguard)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.30.0)
* Display Language의 중국어 번체(zh-TW) 언어셋에서 어색한 문장을 수정했습니다.

### 2.37.0 (2022. 04. 26.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.37.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 고객 센터 URL 뒤에 파라미터를 추가할 수 있도록 다음 필드가 추가되었습니다.
    * **ContactConfiguration.Builder.setAdditionalParameters(Map&lt;String, String&gt;)**

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Gamebase IAP Android SDK(0.18.3)
* Amazon Appstore 결제 데이터에서 userId, gamebaseProductId가 누락될 시 userId, gamebaseProductId를 자동으로 채우도록 개선되었습니다.

### 2.36.0 (2022. 04. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.36.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.29.2), TOAST Gamebase IAP Android SDK(0.18.2), Hangame Android SDK(1.4.5)
* Hangame Android SDK v1.4.5에서 sms_hash가 내부에서 생성되도록 개선되었습니다.
    * 더 이상 sms_hash를 설정하지 않아도 됩니다.

### 2.35.0 (2022. 03. 29.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.35.0/GamebaseSDK-Android.zip)

```
Gamebase Android SDK는 이제 Maven Central로만 배포합니다.
더 이상 배포용 ZIP 파일에서 AAR 파일을 포함하지 않습니다.
```

#### 기능 추가
* 약관 창이 표시되었는지를 알 수 있는 API가 추가되었습니다.
    * **Gamebase.Terms.isShowingTermsView()**
* 웹뷰에서 글자 크기를 고정할 수 있는 옵션이 추가되었습니다.
    * **GamebaseWebViewConfiguration.Builder.enableFixedFontSize(boolean)**
* 약관 창에서 글자 크기를 고정할 수 있는 옵션이 추가되었습니다.
    * **GamebaseTermsConfiguration.Builder.enableFixedFontSize(boolean)**
* Facebook, NAVER 로그인 시 Facebook, NAVER 앱이 설치되어 있더라도 강제로 웹 로그인을 진행하는 기능이 추가되었습니다.
    * 이 기능을 사용하려면 Gamebase Console의 AdditionalInfo에 다음과 같이 설정하세요.

```
{"enforce_app2web":true}
```

* 이제 NAVER 로그아웃 시 토큰을 삭제하지 않습니다.
    * 재로그인할 때 정보 제공 동의 창이 나타나지 않습니다.
    * 웹 로그인 시에는 계정이 변경되지 않습니다.
    * 이전 동작을 유지하려면 Gamebase Console의 AdditionalInfo에 다음과 같이 설정하세요.

```
{"logout_and_delete_token":true}
```

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.29.1), Hangame Android SDK(1.4.4)
* 약관 창이 표시될 때 흰색 배경이 길게 표시되지 않도록 개선했습니다.

#### 버그 수정
* 웹뷰의 내비게이션 바를 숨기는 **GamebaseWebViewConfiguration.Builder.setNavigationBarVisible()** API가 정상적으로 동작하지 않는 문제를 수정했습니다.

### 2.34.0 (2022. 02. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Gamebase 콘솔의 업데이트 필수 설정에서 **팝업 버튼 추가**를 선택하면 클라이언트의 업데이트 필수 팝업 창에 **자세히 보기** 버튼이 추가됩니다.
* 단말기에서 알림을 허용했는지 여부를 알 수 있는 API가 추가되었습니다.
    * **Gamebase.Push.queryNotificationAllowed()**
* 공통 약관 API 호출 후 약관 UI가 표시되었는지 여부를 알 수 있는 VO 클래스가 추가되었습니다.
    * **GamebaseShowTermsViewResult**

#### 기능 개선/변경
* 킥아웃 팝업 창 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 다음 필드가 deprecated되었습니다.
    * **UIPopupConfiguration.enableKickoutPopup**

#### 버그 수정
* 이미지 공지에서 **오늘은 다시 보지 않기**를 선택했을 때, 24시간이 지났는데도 이미지 공지가 표시되지 않는 버그를 수정했습니다.

### 2.33.0 (2022.01.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.33.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 공통 약관 창의 설정을 변경할 수 있는 신규 API가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > UI > Terms > showTermsView](./aos-ui/#showtermsview)

#### 기능 개선/변경
* 외부 SDK 업데이트: PAYCO Android SDK(1.5.7), Hangame Android SDK(1.4.3.1), TOAST Gamebase IAP Android SDK(0.18.1)
* 로그인 성공 직후 론칭 정보가 변경되지 않았는지 확인하는 로직을 추가하였습니다.
