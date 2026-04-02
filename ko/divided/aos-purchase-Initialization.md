## Game > Gamebase > Android SDK 사용 가이드 > 결제

### Initialization

> <font color="red">[주의]</font><br/>
>
> ONE Store는 v17, v19, v21을 지원합니다.
> ONE Store는 버전별로 v17, v19, v21, external 중 하나만 사용이 가능하며, 동시에 사용이 불가능합니다.

* Gamebase 초기화 시 스토어 코드를 지정해야 합니다.
* **STORE_CODE**는 다음 값 중에서 선택합니다.
    * GG: Google Play
    * ONESTORE: ONE Store
    * GALAXY: Galaxy Store
    * HUAWEI: Huawei AppGallery
    * MYCARD: MyCard

```java
String STORE_CODE = "GG";	// Google

GamebaseConfiguration configuration = GamebaseConfiguration.newBuilder(APP_ID, APP_VERSION, STORE_CODE)
        .build();

Gamebase.initialize(activity, configuration, callback);
```
