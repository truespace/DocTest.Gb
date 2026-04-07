---
source: unity-ui.md
split: true
created_date_time: 20260406_141859
keyword: "Unity SDK 사용 가이드, UI, GameNotice, Open GameNotice"
section: GameNotice
order: 1
---

## Game > Gamebase > Unity SDK 사용 가이드 > UI

## GameNotice

콘솔에 이미지와 함께 등록한 공지 사항을 표시하는 기능입니다.

![GameNotice Example](./image/gameNotice_guide_001.png)
<!-- LLM_Image_DESC_20260406
    유형: UI
    내용: 게임 내 공지사항(GameNotice) 표시 예시 화면
    구성: 모바일 화면에 Notice 팝업이 표시되며, Gamebase 로고와 '게임 개발, 출시, 운영을 위한 게임 전문...' 텍스트가 포함된 공지 카드, '글로벌 진출도 Gamebase와 함께' 배너, 'NHN GamePlatform' 홍보 배너 등 여러 공지 항목이 스크롤 형태로 나열됨. 우측 상단에 닫기(X) 버튼이 있음
    Keyword: GameNotice, 공지사항, 팝업, Gamebase, 모바일 UI
-->

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
