---
source: unity-ui.md
section: "Webview"
order: 4
created_date: 2026-04-03
---

## Webview

### Show WebView

웹뷰를 표시합니다.<br/>

##### Required 파라미터
* url : 파라미터로 전송되는 url은 유효한 값이어야 합니다.

##### Optional 파라미터
* configuration : Configuration으로 웹뷰의 레이아웃을 변경 할 수 있습니다.
* closeCallback : 웹뷰가 종료될 때 사용자에게 콜백으로 알려 줍니다.
* schemeList : 사용자가 받고 싶은 커스텀 스킴 목록을 지정합니다.
* schemeEvent : schemeList로 지정한 커스텀 스킴을 포함하는 url을 콜백으로 알려 줍니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE

```cs
static void ShowWebView(string url, GamebaseRequest.Webview.Configuration configuration = null, GamebaseCallback.ErrorDelegate closeCallback = null, List<string> schemeList = null, GamebaseCallback.GamebaseDelegate<string> schemeEvent = null)
```

> Standalone에서는 WebViewAdapter를 통해서 웹뷰를 지원하며 웹뷰가 열려 있을 때 UI로 입력되는 Event를 Blocking하지 않습니다.

**Example**
```cs
private void SchemeEvent(string scheme, GamebaseError error)
{
    Debug.Log(string.Format("[SchemeEvent] scheme:{0}", scheme));
}

private void CloseCallback(GamebaseError error)
{
    Debug.Log("CloseCallback");
}
    
public void ShowWebView()
{
    GamebaseRequest.Webview.Configuration configuration = new GamebaseRequest.Webview.Configuration();
     configuration.title = "Title";
     configuration.orientation = GamebaseScreenOrientation.Portrait;
     configuration.navigationColor = new Color(0.5f, 0.5f, 0.5f, 1);
     configuration.barHeight = 40;
     configuration.isBackButtonVisible = true;
    
    var schemeList = new List<string>() { "customScheme://openBrowser" };
    
    Gamebase.Webview.ShowWebView("https://www.toast.com/", configuration, CloseCallback, schemeList, SchemeEvent);
}
```

#### Configuration

| Parameter                             | Values                                      | Description                                                        |
|---------------------------------------|---------------------------------------------|--------------------------------------------------------------------|
| title                                 | string                                      | 웹뷰의 제목                                                             |
| orientation                           | GamebaseScreenOrientation.UNSPECIFIED       | 미지정(**default**)                                                   |
|                                       | GamebaseScreenOrientation.PORTRAIT          | 세로 모드                                                              |
|                                       | GamebaseScreenOrientation.LANDSCAPE         | 가로 모드                                                              |
|                                       | GamebaseScreenOrientation.LANDSCAPE_REVERSE | 가로 모드를 180도 회전                                                     |
| contentMode<br>(iOS 전용)               | GamebaseWebViewContentMode.RECOMMENDED      | 현재 플랫폼 추천 브라우저(**default**)                                        |
|                                       | GamebaseWebViewContentMode.MOBILE           | 모바일 브라우저                                                           |
|                                       | GamebaseWebViewContentMode.DESKTOP          | 데스크톱 브라우저                                                          |
| navigationColor                       | Color                                       | 내비게이션 바 색상 <br>**default**: GamebaseColor.RGB255(18, 93, 230)      |
| navigationTitleColor                  | Color                                       | 내비게이션 바 제목 색상 <br>**default**: GamebaseColor.RGB255(255, 255, 255) |
| navigationIconTintColor               | Color                                       | 내비게이션 바 아이콘 색상 <br>**default**: null                               |
| barHeight                             | height                                      | 내비게이션 바 높이                                      |
| isNavigationBarVisible                | true or false                               | 내비게이션 바 활성 또는 비활성<br>**default**: true                             |
| isBackButtonVisible                   | true or false                               | 뒤로 가기 버튼 활성 또는 비활성<br>**default**: true                            |
| backButtonImageResource               | ID of resource                              | 뒤로 가기 버튼 이미지                                                       |
| closeButtonImageResource              | ID of resource                              | 닫기 버튼 이미지                                                          |
| enableFixedFontSize<br>(Android 전용)   | true or false                               | 약관 창의 글자 크기 고정 여부를 결정합니다.<br>**default**: false                    |
| renderOutSideSafeArea<br>(Android 전용) | true or false                               | Safe Area 영역 밖 렌더링 여부를 결정합니다.<br>**default**: false                |
| cutoutColor<br>(Android 전용)           | Color                                       | SafeArea 밖의 Cutout 영역 바탕 색상 <br>**default**: null                  |

> [TIP]
>
> iPadOS 13 이상에서 웹뷰는 기본적으로 데스크톱 모드입니다.
> contentMode =`GamebaseWebViewContentMode.MOBILE` 설정으로 모바일 모드로 변경할 수 있습니다.

#### Predefined Custom Scheme

Gamebase에서 지정해 놓은 스킴입니다.

| scheme | 용도 |
| ----------------------------- | ------------------------------ |
| gamebase://dismiss | 웹뷰 닫기 |
| gamebase://goBack | 웹뷰 뒤로 가기 |
| gamebase://getUserId          | 현재 로그인중인 있는 게임 유저의 사용자 ID를 표시 |
| gamebase://getMaintenanceInfo | 점검 내용을 WebPage에 표시 |
| gamebase://showwebview?link={URLEncodedURL} | link 파라메터의 URL 을 웹뷰로 열기.<br>URLEncodedURL : 웹뷰로 열 URL.<br>URL 디코딩 필요. |
| gamebase://openbrowser?link={URLEncodedURL} | link 파라메터의 URL을 외부 브라우저로 열기<br/>URLEncodedURL : 외부 브라우저로 열 URL<br/>URL 디코딩 필요 |

### Close WebView

다음 API를 이용하여 보여지고 있는 웹뷰를 닫을 수 있습니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE

```cs
static void CloseWebView()
```

**Example**CloseWebView
```cs
public void CloseWebView()
{
    Gamebase.Webview.CloseWebView();
}
```
