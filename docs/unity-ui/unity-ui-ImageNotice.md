---
source: unity-ui.md
section: "ImageNotice"
order: 2
split: true
created_date_time: 20260408_191848
keyword: Unity, WebView, Initialize, ImageNotice, Error, Console
---

## ImageNotice

콘솔에 이미지를 등록한 후 사용자에게 공지를 띄울 수 있습니다.

![ImageNotice Example](./image/imageNotice-guide-landscape-ko_v3.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: ImageNotice 관련 화면
    구성: ImageNotice 관련 스크린샷
    Keyword: Unity, Screenshot, ImageNotice
-->

### Show ImageNotices

이미지 공지를 화면에 띄워 줍니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE

```cs
static void ShowImageNotices(GamebaseRequest.ImageNotice.Configuration configuration, GamebaseCallback.ErrorDelegate closeCallback, GamebaseCallback.GamebaseDelegate<string> eventCallback = null)
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| NOT\_INITIALIZED | 1 | Gamebase가 초기화되어 있지 않습니다. |
| UI\_IMAGE\_NOTICE\_TIMEOUT | 6901 | 이미지 공지 팝업 창 표시 중 시간이 초과되어 모든 팝업 창을 강제 종료합니다. |
| UI\_IMAGE\_NOTICE\_NOT\_SUPPORTED\_OS | 6902 | 롤링 타입의 경우 API 19 이하의 단말기에서는 이미지 공지를 지원하지 않습니다. |
| WEBVIEW\_HTTP\_ERROR | 7003 | 롤링 타입 이미지 공지 웹뷰 오픈 중 HTTP 오류가 발생했습니다. |
| SERVER\_INVALID\_RESPONSE | 8003 | 서버가 유효하지 않은 응답을 반환했습니다. |

**Example**

```cs
public void ShowImageNotices()
{
    Gamebase.ImageNotice.ShowImageNotices(
        null,
        (error) =>
        {
            // Called when the entire imageNotice is closed.
            ...
            
        },
        (scheme, error) =>
        {
            // Called when custom event occurred.
            ...
        });        
}
```

### Custom ImageNotices

사용자 설정 이미지 공지를 화면에 띄워 줍니다.
GamebaseRequest.ImageNotice.Configuration으로 사용자 설정 이미지 공지를 만들 수 있습니다.

**Example**

```cs
public void ShowImageNotices()
{
    GamebaseRequest.ImageNotice.Configuration configuration = new GamebaseRequest.ImageNotice.Configuration();
    configuration.backgroundColor = new Color(0, 0, 0, 0.5f);
    configuration.timeOut = 5000;

    Gamebase.ImageNotice.ShowImageNotices(
        configuration,
        (error) =>
        {
            // Called when the entire imageNotice is closed.
            ...
            
        },
        (scheme, error) =>
        {
            // Called when custom event occurred.
            ...
        });        
}
```

#### GamebaseRequest.ImageNotice.Configuration

| Parameter                              | Values                                  | Description                                                      |
| -------------------------------------- | --------------------------------------- |------------------------------------------------------------------|
| backgroundColor          | Color       | 배경 색상 <br>**default**: GamebaseColor.RGB255(0, 0, 0, 128) |
| timeoutMS                | long        | 이미지 공지 최대 로딩 시간(단위: millisecond)<br/>**default**: 5000           |


### Close ImageNotices

closeImageNotices API를 호출하여 현재 표시 중인 이미지 공지를 모두 종료할 수 있습니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE

```cs
static void CloseImageNotices()
```
