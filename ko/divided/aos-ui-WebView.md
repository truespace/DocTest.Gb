## Game > Gamebase > Android SDK 사용 가이드 > UI

## WebView

Gamebase에서는 기본적인 웹뷰를 지원합니다.


### Show WebView

웹뷰를 표시합니다.

##### Required 파라미터
* activity : 웹뷰가 노출되는 Activity입니다.
* url : 파라미터로 전송되는 url은 유효한 값이어야 합니다.

##### Optional 파라미터
* configuration : GamebaseWebViewConfiguration으로 웹뷰의 레이아웃을 변경 할 수 있습니다.
* GamebaseCallback : 웹뷰가 종료될 때 사용자에게 콜백으로 알려 줍니다.
* schemeList : 사용자가 받고 싶은 커스텀 스킴 목록을 지정합니다.
* GamebaseDataCallback : schemeList로 지정한 커스텀 스킴을 포함하는 url을 콜백으로 알려 줍니다.

**API**

```java
+ (void)Gamebase.WebView.showWebView(Activity activity,
                String urlString,
                GamebaseWebViewConfiguration configuration,
                GamebaseCallback onCloseCallback,
                List<String> schemeList,
                GamebaseDataCallback<String> onEvent);
```

**Example**

```java
Gamebase.WebView.showWebView(activity, "https://www.toast.com");
```

![Webview Example](https://static.toastoven.net/prod_gamebase/DevelopersGuide/aos-developers-guide-ui-001_1.0.0.png)

#### Custom WebView

사용자 지정 웹뷰를 표시합니다. <br/>
GamebaseWebViewConfiguration으로 사용자 지정 웹뷰를 만들 수 있습니다.

```java
GamebaseWebViewConfiguration configuration
        = new GamebaseWebViewConfiguration.Builder()
            .setTitleText("title")                              // 웹뷰 제목을 설정
            .setScreenOrientation(ScreenOrientation.PORTRAIT)   // 웹뷰 스크린 방향 설정
            .setNavigationBarColor(Color.RED)                   // 내비게이션 바 색상 설정
            .setNavigationBarTitleColor(Color.BLACK)            // 내비게이션 바 타이틀 색상 설정
            .setNavigationBarIconTintColor(Color.BLACK)         // 내비게이션 바 아이콘 틴트 색상 설정
            .setNavigationBarHeight(40)                         // 내비게이션 바 높이 설정
            .setBackButtonVisible(true)                         // 뒤로 가기 버튼 활성화 여부 설정
            .setBackButtonImageResource(R.id.back_button)       // 뒤로 가기 버튼 이미지 설정
            .setCloseButtonImageResource(R.id.close_button)     // 닫기 버튼 이미지 설정
            .build();
GamebaseWebView.showWebView(activity, "https://www.toast.com", configuration);
```

#### Custom Scheme

Gamebase 웹뷰에서 로딩한 웹 페이지 내에 스킴으로 특정 기능을 사용하거나 웹 페이지 내용을 변경할 수 있습니다.

##### Predefined Custom Scheme

Gamebase에서 지정해 놓은 스킴입니다.

| scheme               | 용도                                  |
| -------------------- | ------------------------------------- |
| gamebase://dismiss   | 웹뷰 닫기                          |
| gamebase://goback    | 웹뷰 뒤로 가기                     |
| gamebase://getuserid | 현재 로그인중인 있는 사용자의 아이디 표시 |
| gamebase://showwebview?link={URLEncodedURL} | link 파라메터의 URL 을 웹뷰로 열기.<br>URLEncodedURL : 웹뷰로 열 URL.<br>URL 디코딩 필요. |
| gamebase://openbrowser?link={URLEncodedURL} | link 파라메터의 URL 을 외부 브라우저로 열기.<br>URLEncodedURL : 외부 브라우저로 열 URL.<br>URL 디코딩 필요. |

#### User Custom Scheme

Gamebase에 스킴 이름과 블록을 지정해 원하는 기능을 추가할 수 있습니다.

```java
GamebaseWebViewConfiguration configuration = new GamebaseWebViewConfiguration.Builder()
        .setTitleText(title)
        .build();
List<String> schemeList = new ArrayList<>();
schemeList.add("mygame://test");
schemeList.add("mygame://opensomebrowser");
schemeList.add("closemywebview://");
showWebView(activity, urlString, configuration,
        new GamebaseCallback() {
            @Override
            public void onCallback(GamebaseException exception) {
                // When closed WebView, this callback will be called.
            }
        },
        schemeList,
        new GamebaseDataCallback<String>() {
            @Override
            public void onCallback(String fullUrl, GamebaseException exception) {
                if (Gamebase.isSuccess(exception)) {
                    if (fullUrl.contains("mygame://test")) {
                        // Do something.
                    } else if (fullUrl.contains("mygame://opensomebrowser")) {
                        Gamebase.WebView.openWebBrowser(someUrl);
                    } else if (fullUrl.contains("closemywebview://")) {
                        // We will close webview.
                        Gamebase.WebView.closeWebView(activity);
                    }
                } else {
                    // Something went wrong.
                }
            }
        });
```

#### GamebaseWebViewConfiguration

| Method                                   | Values                              | Description    |
| ---------------------------------------- | ----------------------------------- | -------------- |
| setTitleText(String title)               | title                               | 웹뷰의 제목         |
| setScreenOrientation(int orientation)    | ScreenOrientation.PORTRAIT          | 세로 모드          |
|                                          | ScreenOrientation.LANDSCAPE         | 가로 모드          |
|                                          | ScreenOrientation.LANDSCAPE_REVERSE | 가로 모드를 180도 회전 |
| setNavigationBarVisible(boolean enable)  | true or false                       | 내비게이션 바 활성 또는 비활성.<br>**default**: true |
| setNavigationBarColor(int color)         | Color.argb(a, r, g, b)              | 내비게이션 바 색상<br>**default**:#125DE6  |
| setNavigationBarTitleColor(int color)    | Color.argb(a, r, g, b)              | 내비게이션 바 타이틀 색상<br>**default**: Color.WHITE  |
| setNavigationBarIconTintColor(int color) | Color.argb(a, r, g, b)              | 내비게이션 바 아이콘 틴트 색상<br>**default**: 틴트 설정하지 않음   |
| setNavigationBarHeight(int height)       | height                              | 내비게이션 바 높이     |
| setBackButtonVisible(boolean visible)    | true or false                       | 뒤로 가기 버튼 활성 또는 비활성.<br>**default**: true |
| setBackButtonImageResource(int resourceId) | ID of resource                      | 뒤로 가기 버튼 이미지       |
| setCloseButtonImageResource(int resourceId) | ID of resource                      | 닫기 버튼 이미지      |
| enableAutoCloseByCustomScheme(boolean enable) | true or false | 커스텀 스킴 동작 시 자동으로 웹뷰 종료.<br>**default**: true |
| enableFixedFontSize(boolean enable)      | true or false | 시스템 글자 크기를 무시하고 고정된 크기로 웹뷰를 표시.<br>**default**: false |
| setRenderOutsideSafeArea(boolean render) | true or false | SafeArea를 무시하고 Cutout 영역에도 렌더링.<br>**default**: false |
| setCutoutAreaColor(int color) | Color.argb(a, r, g, b) | SafeArea 밖의 Cutout 영역 바탕 색상 |

### Close WebView
다음 API를 통해 현재 보여지는 웹뷰를 닫을 수 있습니다.

**API**

```java
+ (void)Gamebase.WebView.closeWebView(Activity activity);
```
