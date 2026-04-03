---
source: aos-ui.md
section: "ImageNotice"
order: 2
created_date: 2026-04-03
---

## ImageNotice

콘솔에 이미지를 등록한 후 사용자에게 공지를 띄울 수 있습니다.

![ImageNotice Example](./image/imageNotice-guide-landscape-ko_v3.png)

### Show ImageNotices

이미지 공지를 화면에 띄워 줍니다.

#### Required 파라미터
* Activity : 이미지 공지가 노출되는 Activity입니다.

#### Optional 파라미터
* ImageNoticeConfiguration : 이미지 공지 설정을 변경할 수 있습니다.
* GamebaseCallback : 이미지 공지가 전체 종료될 때 사용자에게 콜백으로 알려 줍니다.
* GamebaseDataCallback : 이미지를 클릭했을 때, 콘솔에 등록한 payload 를 콜백으로 알려 줍니다.

**API**

```java
+ (void)Gamebase.ImageNotice.showImageNotices(@NonNull Activity activity,
                                              @Nullable GamebaseCallback onCloseCallback);
+ (void)Gamebase.ImageNotice.showImageNotices(@NonNull Activity activity,
                                              @Nullable ImageNoticeConfiguration configuration,
                                              @Nullable GamebaseCallback onCloseCallback,
                                              @Nullable GamebaseDataCallback<String> onEvent);
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| NOT\_INITIALIZED | 1 | Gamebase.initialize가 호출되지 않았습니다. |
| UI\_IMAGE\_NOTICE\_TIMEOUT | 6901 | 이미지 공지 팝업 창 표시 중 시간이 초과되어 모든 팝업 창을 강제 종료합니다. |
| UI\_IMAGE\_NOTICE\_NOT\_SUPPORTED\_OS | 6902 | 롤링 타입의 경우 API 19 이하의 단말기에서는 이미지 공지를 지원하지 않습니다. |
| SERVER\_INVALID\_RESPONSE | 8003 | 서버가 유효하지 않은 응답을 반환했습니다. |
| WEBVIEW\_HTTP\_ERROR | 7003 | 롤링 타입 이미지 공지 웹뷰 오픈 중 HTTP 에러가 발생하였습니다. |

**Example**

```java
Gamebase.ImageNotice.showImageNotices(getActivity(), null,
    new GamebaseCallback(){
        @Override
        public void onCallback(GamebaseException exception) {
        	// Called when the entire imageNotice is closed.
            ...
        }
    },
    new GamebaseDataCallback<String>() {
        @Override
        public void onCallback(String payload, GamebaseException exception) {
        	// Called when custom event occurred.
            ...
        }
    });
```

### Custom ImageNotices

사용자 설정 이미지 공지를 화면에 띄워 줍니다.
ImageNoticeConfiguration으로 사용자 설정 이미지 공지를 만들 수 있습니다.

**Example**

```java
ImageNoticeConfiguration configuration = ImageNoticeConfiguration.newBuilder()
		.setBackgroundColor("#FFFF0000")		// Red
        .setTimeout(10000L)						// 10000ms == 10s
        .enableAutoCloseByCustomScheme(false)
        .build();
Gamebase.ImageNotice.showImageNotices(getActivity(), configuration, null, null);
```

#### ImageNoticeConfiguration

| API | Mandatory(M) / Optional(O) | Description |
| --- | --- | --- |
| newBuilder() | **M** | ImageNoticeConfiguration.Builder 객체는 newBuilder() 함수를 통해 생성할 수 있습니다. |
| build() | **M** | 설정을 마친 Builder 를 Configuration 객체로 변환합니다. |
| setBackgroundColor(int backgroundColor)<br>setBackgroundColor(String backgroundColor) | O | 이미지 공지 뒷 배경색.<br>String 은 android.graphics.Color.parseColor(String) API로 변환한 값을 사용합니다.<br>**default**: #80000000 |
| setTimeout(long timeoutMs) | O | 이미지 공지 최대 로딩 시간(단위: millisecond)<br>**default**: 5000L (5s) |
| enableAutoCloseByCustomScheme(boolean enable) | O | 커스텀 스킴 이벤트가 발생하면 이미지 공지를 강제종료 할지 여부를 결정합니다.<br>**default**: true |


### Close ImageNotices

closeImageNotices API를 호출하여 현재 표시 중인 이미지 공지를 모두 종료할 수 있습니다.

**API**

```java
+ (void)Gamebase.ImageNotice.closeImageNotices(@NonNull Activity activity);
```
