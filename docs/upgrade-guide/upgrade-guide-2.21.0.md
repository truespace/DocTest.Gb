---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "Gradle, IdP, 2.21.0"
section: 2.21.0
order: 48
---

## 2.21.0

### Android

* Gamebase Android SDK 2.21.0 은 jCenter 에는 잘못된 빌드가 배포되어, **jcenter()** 를 **mavenCentral()** 보다 먼저 선언 했다면 모든 Gamebase API 에서 크래시가 발생할 수 있습니다.
    * 정상적으로 배포된 Gamebase Android SDK 2.21.1 을 사용하시거나 **mavenCentral()** 을 **jcenter()** 보다 먼저 선언하시기 바랍니다.
* Maven Repository
    * jCenter가 일반 사용자를 위한 서비스를 종료하여 ( [https://jfrog.com/blog/into-the-sunset-bintray-jcenter-gocenter-and-chartcenter/](https://jfrog.com/blog/into-the-sunset-bintray-jcenter-gocenter-and-chartcenter/) ) 더 이상 새로운 빌드는 업로드는 할 수 없게 되었습니다.(jCenter 의 접근 또한 2022 년 2월 1일에 종료됩니다.)
    * 그래서 Gamebase Android SDK 2.21.0 부터는 **jcenter()**가 아닌 **mavenCentral()** 에서만 배포가 되므로 gradle repository 에 mavenCentral 을 추가하세요.

```groovy
repositories {
    // >>> For Gamebase SDK
    mavenCentral()
    ...
}
```

#### LINE IdP

* LINE IdP 를 사용하는 경우, LINE SDK 업데이트로 인해 아래와 같이 Gradle 에 **JavaVersion.VERSION_1_8** 설정을 하지 않으면 빌드가 실패합니다.

```groovy
android {
    compileOptions {
        // >>> [LINE IdP]
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}
```

### iOS

* Gamebase iOS SDK 2.21.0 에서 bitcode 를 사용할 경우 에러가 발생합니다.
    * bitcode 사용을 원하시는 경우엔 Gamebase iOS SDK 2.21.1 을 사용하시기 바랍니다.
