---
source: aos-ui.md
section: "GameNotice"
order: 1
split: true
created_date_time: 20260408_184906
keyword: Android, WebView, Error, Console
---

## Game > Gamebase > Android SDK 사용 가이드 > UI

## GameNotice

콘솔에 이미지와 함께 등록한 공지 사항을 표시하는 기능입니다.

![GameNotice Example](./image/gameNotice_guide_001.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: GameNotice 관련 화면
    구성: GameNotice 관련 스크린샷
    Keyword: Android, Screenshot, GameNotice
-->
![GameNotice Example](./image/gameNotice_guide_002.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: GameNotice 관련 화면
    구성: GameNotice 관련 스크린샷
    Keyword: Android, Screenshot, GameNotice
-->

### Open GameNotice

게임 공지를 화면에 표시합니다.

#### Required 파라미터
* Activity: 게임 공지가 노출되는 Activity입니다.


#### Optional 파라미터
* GameNoticeConfiguration: 게임 공지 설정을 변경할 수 있습니다.

* GamebaseCallback: 게임 공지가 정상적으로 종료되거나 에러로 표시하지 못했을 때 사용자에게 콜백으로 알려 줍니다.


**API**

```java
+ (void)Gamebase.GameNotice.openGameNotices(@NonNull Activity activity,
                                            @Nullable GamebaseCallback onCloseCallback);
+ (void)Gamebase.GameNotice.openGameNotices(@NonNull Activity activity,
                                            @Nullable GameNoticeConfiguration configuration,
                                            @Nullable GamebaseCallback onCloseCallback);
```

**ErrorCode**

| Error | Error Code | Description |
| ---- | ------- | ----------- |
| - | 0 | 성공 |
| NOT\_INITIALIZED | 1 | Gamebase.initialize가 호출되지 않았습니다. |
| UI\_GAME\_NOTICE\_FAIL\_INVALID\_URL | 6941 | 게임 공지 URL 생성에 실패했습니다. |
| UI\_GAME\_NOTICE\_FAIL\_ANDROID\_DUPLICATED\_VIEW | 6942 | 게임 공지 팝업을 종료하기 전에 다시 게임 공지를 호출했습니다. |
| WEBVIEW\_TIMEOUT | 7002 | 웹뷰 표시 시간이 초과되었습니다.(10초) |
| WEBVIEW\_HTTP\_ERROR | 7003 | 웹뷰 내부에서 HTTP 에러가 발생했습니다. |
| WEBVIEW\_UNKNOWN\_ERROR | 7999 | 알 수 없는 웹뷰 에러가 발생했습니다. |

**Example**

```java
Gamebase.GameNotice.openGameNotice(activity, (GamebaseCallback) exception -> {
    if (Gamebase.isSuccess(exception)) {
        // Game Notice was opened and closed successfully.
    } else {
        // Game Notice did not opened with error.
    }
});
```

### Custom GameNotice

사용자 설정 게임 공지를 표시합니다.
GameNoticeConfiguration으로 표시 설정을 변경할 수 있습니다.

**Example**

```java
GameNoticeConfiguration configuration = GameNoticeConfiguration.newBuilder()
        .setBackgroundColor("#80FFFF00")
        .build();
Gamebase.GameNotice.openGameNotice(
        activity,
        configuration,
        (GamebaseCallback) exception -> {
            if (Gamebase.isSuccess(exception)) {
                // Game Notice was opened and closed successfully.
            } else {
                // Game Notice did not opened with error.
            }
        });
```

#### GameNoticeConfiguration

| API | Mandatory(M) / Optional(O) | Description |
| --- | --- | --- |
| newBuilder() | **M** | GameNoticeConfiguration.Builder 객체는 newBuilder() 함수를 통해 생성할 수 있습니다. |
| build() | **M** | 설정을 마친 Builder를 Configuration 객체로 변환합니다. |
| setBackgroundColor(int backgroundColor)<br>setBackgroundColor(String backgroundColor) | O | 게임 공지 배경색입니다.<br>색상은 ARGB 순서입니다.<br>String 은 android.graphics.Color.parseColor(String) API로 변환한 값을 사용합니다.<br>**default**: #CC000000 |
