---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Gradle, Java, v2.70.0, 신규, 버그수정, 기능개선, 기능추가, 변경, Notice"
section: "2.70.0 (2025. 03. 11.)"
order: 15
---

### 2.70.0 (2025. 03. 11.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.70.0/GamebaseSDK-Android.zip)

#### 기능 추가

* 외부 SDK 업데이트: NHN Cloud SDK(1.9.5)
    * Google Play Billing Library 7.1.1이 적용되었습니다.
    * Android 7.0(API Level 24) 미만 단말기에서 결제를 시도하는 경우 Google Play Billing Library에서 크래시가 발생합니다.
        * 이 문제를 해결하기 위해서는 Gradle에 하위 OS를 위한 [Java 8+ API 디슈가링 지원](https://developer.android.com/studio/write/java8-support#library-desugaring) 선언을 추가해야 합니다.
        * 앱 모듈의 Gradle, Unity의 경우 launcherTemplate.gradle에 다음 선언을 추가하세요.
        
                android {
                    compileOptions {
                        // Flag to enable support for the new language APIs
                        coreLibraryDesugaringEnabled true
                    }
                }

                dependencies {
                    // desugar_jdk_libs 2.+ needs AGP 7.4+
                    coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.1.5")
                }
        
        * desugar_jdk_libs 1.x 버전은 Kakaogame 로그인 시 크래시가 발생하므로 2.x 버전 적용을 권장합니다.
            * Unity Editor 버전에 따라 AGP 버전이 다르므로 AGP 및 Gradle 버전 업데이트가 필요할 수 있습니다.
* 'GPGS 자동 로그인' 기능 연동 시 유저에게 GPGS 로그인을 앱 설치 후 한번만 물어보는 초기화 옵션을 추가했습니다.
    * **GamebaseConfiguration.Builder.enableGPGSSignInCheck(boolean)**
    * 기본 설정은 true로, 유저가 GPGS 로그인을 거부하더라도 Gamebase 초기화 때 GPGS 로그인 창을 다시 표시합니다.
    * false로 설정하면 앱 최초 실행 시에만 GPGS 로그인 창이 한번 표시됩니다.
* 로그인 시 IdP 서버로부터 오류가 발생했음을 나타내는 신규 오류 코드가 추가되었습니다.
    * AUTH_AUTHENTICATION_SERVER_ERROR(3012)
* GamebaseWebView에 내비게이션 바 타이틀과 아이콘 틴트 컬러 설정 옵션을 추가했습니다.
    * **GamebaseWebViewConfiguration.Builder.setNavigationBarTitleColor(int)**
    * **GamebaseWebViewConfiguration.Builder.setNavigationBarIconTintColor(int)**

#### 기능 개선/변경

* 'GPGS 자동 로그인' 기능 연동시 유저가 GPGS 로그인을 하지 않으면 Gamebase 초기화, 로그인, 로그아웃 시 GPGS 로그인을 계속 시도하던 동작을 Gamebase 초기화 때만 시도하도록 변경했습니다.
* Apple ID, Steam, Twitter 로그인 내비게이션 바에 타이틀과 같은 색으로 X 버튼을 표시하도록 변경했습니다.

#### 버그 수정

* LaunchingInfo data가 유저 Event Handler에서 업데이트되지 않는 이슈를 수정했습니다.
* Unity 빌드에서 이미지 공지 비율이 원본 이미지 비율과 다르게 표시되는 문제를 수정했습니다.
