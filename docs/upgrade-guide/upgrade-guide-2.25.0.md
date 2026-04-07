---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "Gradle, Java, IdP, IAP, setProperty"
section: 2.25.0
order: 46
---

## 2.25.0

### Android

#### Changed Minimum Support Version

* 최소 지원 Android Gradle Plugin(AGP) 버전이 2.3.0 에서 3.2.0 으로 변경되었습니다.
    * 하지만 targetSdkVersion 을 30 이상으로 설정하는 경우, Android 11 단말기 대응을 위해서는 AGP 3.3.3 이상이 필요합니다.
        * 다음 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Android 11](../aos-started.md#android-11)
* 하위 버전의 AGP 지원이 필요하다면 [고객 센터](https://toast.com/support/inquiry)로 문의해 주시기 바랍니다.

#### AndroidX

* Android Support Library 의존성이 AndroidX 로 변경되었으므로 Gradle 에 다음 변경사항을 적용하시기 바랍니다.

* gradle.properties 파일에 AndroidX 대응이 되어 있지 않은 라이브러리들을 위한 마이그레이션 선언을 추가하세요.

```groovy
# >>> [AndroidX]
android.useAndroidX=true
android.enableJetifier=true
```

* build.gradle 파일에 최신 AndroidX 를 위한 Java 8 빌드 설정을 추가하세요.

```groovy
android {
    compileOptions {
        // >>> [AndroidX]
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}
```

#### Under AGP 3.4.0

* Android Gradle Plugin 버전이 3.4.0 미만인 경우 빌드가 실패하므로 gradle.properties 파일에 다음 선언이 필요합니다.

```groovy
# gradle.properties
# >>> Fix for AGP under 3.4.0
android.enableD8.desugaring=true
android.enableIncrementalDesugaring=false
```

#### LINE IdP

* LINE IdP 를 사용하는 경우, LINE SDK 내부에 **&lt;queries&gt;** 태그가 존재하여 AGP 버전에 따라서는 빌드가 실패할 수 있습니다.
    * 다음 가이드를 참고하여 'queries' 태그 빌드가 가능한 AGP 버전으로 업그레이드 하시기 바랍니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Android 11](../aos-started.md#android-11)
* LINE IdP 를 사용하는 경우, LINE SDK 내부에 **android:allowBackup="false"** 로 선언되어 있어 애플리케이션 빌드시 Manifest merger 에서 fail 이 발생할 수 있습니다. 이렇게 빌드가 실패한다면 다음과 같이 application 태그에 **tools:replace="android:allowBackup"** 선언을 추가하시기 바랍니다.

```xml
<application
      tools:replace="android:allowBackup"
      ... >
```

### iOS

* Sign In with Apple 의 ASAuthorizationErrorUnknown 에러가 발생했을 경우, TCGB_ERROR_AUTH_EXTERNAL_LIBRARY_ERROR (3009) 에러를 반환하도록 변경되었습니다.

### Unity

* 해당 버전을 사용 시에는 **Assets/Gamebase/Toast/IAP/Plugins**를 직접 삭제한 후 사용하시기 바랍니다.
    * Gamebase Unity SDK 2.27.0 이상 버전이 적용된 경우에는 삭제할 필요가 없습니다.

#### Changed Minimum Support Version

* 최소 지원 Unity 버전이 2017.4.16 에서 2018.4.0 으로 변경되었습니다.
* 하위 버전의 Unity 지원이 필요하다면 [고객 센터](https://toast.com/support/inquiry)로 문의해 주시기 바랍니다.

#### AndroidX Build

* Gamebase Android SDK 의 AndroidX 이전으로 인해 Android 빌드시 다음 선언을 추가하시기 바랍니다.
* 2019.3 미만

```groovy
// mainTemplate.gradle
([rootProject] + (rootProject.subprojects as List)).each {
    ext {
        it.setProperty("android.useAndroidX", true)
        it.setProperty("android.enableJetifier", true)
    }
}
```

* 2019.3 이상

```groovy
// gradleTemplate.properties
android.useAndroidX=true
android.enableJetifier=true
```

#### Under AGP 3.4.0

* Unity Editor 버전이 2018.4.3 이하이거나 2019.1.6 이하인 경우, AGP 버전이 낮아서(3.2.0) 빌드가 실패하므로 다음 선언을 추가하세요.

```groovy
// mainTemplate.gradle
([rootProject] + (rootProject.subprojects as List)).each {
    ext {
        // >>> Fix for AGP under 3.4.0
        it.setProperty("android.enableD8.desugaring", true)
        it.setProperty("android.enableIncrementalDesugaring", false)
    }
}
```

### Unreal

#### AndroidX Build

* Gamebase Android SDK 의 AndroidX 이전으로 인해 Android 빌드시 UPL 에 다음 선언을 추가하시기 바랍니다.

```xml
<gradleProperties>    
  <insert>      
    android.useAndroidX=true      
    android.enableJetifier=true    
  </insert>  
</gradleProperties>
```
