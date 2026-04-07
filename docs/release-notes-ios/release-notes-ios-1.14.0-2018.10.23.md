---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "1.14.0 (2018.10.23)"
section: "1.14.0 (2018.10.23)"
order: 120
---

### 1.14.0 (2018.10.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* Gamebase 웹뷰에서 파일첨부 기능 추가
    
#### 기능 개선/변경
* 이용 정지/점검에 대해 사용자가 콘솔에 작성한 메시지들을 URL 인코딩하여 전송하고 클라이언트에서 디코딩하여 처리하도록 수정
* PAYCO iOS SDK 업데이트 (1.2.4)
* Remove API: Webview, Network, Launching
    * **[TCGBUtil showToastWithMessage:duration:]**
    * **[TCGBWebView showWebBrowserWithURL:viewController:]**
    * **[TCGBWebView showWebViewWithURL:viewController:configuration:]**
    * **[TCGBLaunching addObserverOnChangedStatusNotification:]**
    * **[TCGBLaunching removeObserverOnChangedStatusNotification:]**
    * **[TCGBLaunching addUpdateStatusNotification]**
    * **[TCGBLaunching removeUpdateStatusNotification]**
    * **[TCGBNetwork addObserverOnChangedNetworkStatusWithHandler:]**
    * **[TCGBNetwork removeObserverOnChangedNetworkStatusWithHandler:]**
* Deprecated API 
    * **[TCGBGamebase languageCode]**
