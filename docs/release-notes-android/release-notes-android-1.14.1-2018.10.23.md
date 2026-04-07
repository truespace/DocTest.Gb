---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "1.14.1 (2018.10.23)"
section: "1.14.1 (2018.10.23)"
order: 113
---

### 1.14.1 (2018.10.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.1/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 1.14.0
    * (공통)Gamebase 웹뷰에서 파일첨부 기능 추가 : Android의 API 19, Kitcat 에서는 정상 동작하지 않습니다.
    
#### 기능 개선/변경
* [SDK] 1.14.0
    * (공통)이용 정지/점검에 대해 사용자가 콘솔에 작성한 메시지들을 URL 인코딩하여 전송하고 클라이언트에서 디코딩하여 처리하도록 수정
    * Remove API : Webview, Network, Launching
        * (void)Gamebase.WebView.showWebBrowser(Activity, String)
        * (void)Gamebase.Network.addOnChangedListener(NetworkManager.OnChangedListener)
        * (void)Gamebase.Network.removeOnChangedListener(NetworkManager.OnChangedListener)
        * (void)Gamebase.Launching.addOnUpdatedListener(LaunchingOnUpdateListener)
        * (void)Gamebase.Launching.removeOnUpdatedListener(LaunchingOnUpdateListener)        
    * Deprecated  API 
        * (void)Gamebase.WebView.showWebView(Activity, String)
        * (void)Gamebase.WebView.showWebView(Activity, String, GamebaseWebViewConfiguration)
    
#### 버그수정
* [SDK] 1.14.1
    * (Android)Auth API 호출 후 콜백에서 다시 Auth API 중복 호출 시 정상 호출이 되지 않는 버그 수정
