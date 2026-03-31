## Game > Gamebase > Unity SDK 사용 가이드 > UI

## GameNotice

콘솔에 이미지와 함께 등록한 공지 사항을 표시하는 기능입니다.

![GameNotice Example](https://static.toastoven.net/prod_gamebase/DevelopersGuide/gameNotice_guide_001.png)

### Open GameNotice

게임 공지를 화면에 표시합니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE


```cs
public static void OpenGameNotice(GamebaseCallback.ErrorDelegate callback)
```

**ErrorCode**

| Error                                | Error Code | Description                         |
|--------------------------------------| --- |-------------------------------------|
| NOT\_INITIALIZED                     | 1 | Gamebase가 초기화되어 있지 않습니다.            |
| UI\_GAME\_NOTICE\_FAIL\_INVALID\_URL            | 6941 | 게임 공지 URL 생성에 실패했습니다.               |
| UI\_GAME\_NOTICE\_FAIL\_ANDROID\_DUPLICATED\_VIEW | 6942 | 게임 공지 팝업을 종료하기 전에 다시 게임 공지를 호출했습니다. |
| WEBVIEW\_TIMEOUT                | 7002 | 웹뷰 표시 시간이 초과되었습니다.(10초)             |
| WEBVIEW\_HTTP\_ERROR                 | 7003 | 웹뷰 내부에서 HTTP 에러가 발생했습니다.            |
| WEBVIEW\_UNKNOWN\_ERROR           | 7999 | 알 수 없는 웹뷰 에러가 발생했습니다.               |

**Example**

```cs
public void SampleOpenGameNotice()
{
    Gamebase.GameNotice.OpenGameNotice(
        (error) =>
        {
            // Called when the entire gameNotice is closed.
        });
}
```
