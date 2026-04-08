---
source: upgrade-guide.md
section: "2.70.0"
order: 8
split: true
created_date_time: 20260408_191848
keyword: Login, Purchase, Gradle, Java, Android, Unity, Upgrade Guide, 2.70.0
---

## 2.70.0

### Android

* Gamebase Android SDK 2.70.0에서 사용하는 Google Play Billing Library 7.1.1은 Android 7.0(API Level 24) 미만 단말기에서 결제를 시도하는 경우 크래시가 발생합니다.
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
