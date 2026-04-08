---
source: release-notes-android.md
section: "2.40.0 (2022. 05. 24.)"
order: 56
split: true
created_date_time: 20260408_191848
keyword: Android, Purchase, Push, Release Notes, 2.40.0
---

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
