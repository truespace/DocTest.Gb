---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v1.14.0, 기능개선, 기능추가, 변경, WebView, Launching"
section: "1.14.0 (2018.10.23)"
order: 114
---

### 1.14.0 (2018.10.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 1.14.0
    * (공통)Gamebase 웹뷰에서 파일첨부 기능 추가 : Android의 API 19, Kitcat 에서는 정상 동작하지 않습니다.
    
#### 기능 개선/변경
* [SDK] 1.14.0
    * (공통)이용 정지/점검에 대해 사용자가 콘솔에 작성한 메시지들을 URL 인코딩하여 전송하고 클라이언트에서 디코딩하여 처리하도록 수정
    * (Unity)GamebaseSDKSetting 오브젝트가 있는 씬으로 돌아갈 경우 오브젝트가 중복으로 생기지 않도록 개선
    * Remove API : Webview, Network, Launching
        * ShowWebBrowser(string url)
        * ShowWebView(GamebaseRequest.Webview.GamebaseWebViewConfiguration configuration)
        * ShowToast(string message, int duration)
        * AddUpdateStatusListener(GamebaseCallback.DataDelegate<GamebaseResponse.Launching.LaunchingStatus> callback) 
        * RemoveUpdateStatusListener(GamebaseCallback.DataDelegate<GamebaseResponse.Launching.LaunchingStatus> callback)
        * AddOnChangedStatusListener(GamebaseCallback.DataDelegate<GamebaseNetworkType> callback)
        * RemoveOnChangedStatusListener(GamebaseCallback.DataDelegate<GamebaseNetworkType> callback)
    * Deprecated  API 
        * GetLanguageCode()
* [SDK] Setting Tool        
    * 팝업 창 및 UI 개선
