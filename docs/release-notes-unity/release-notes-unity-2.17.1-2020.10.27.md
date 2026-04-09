---
source: release-notes-unity.md
section: "2.17.1 (2020.10.27)"
order: 78
split: true
created_date_time: 20260408_184906
keyword: Unity, Purchase, Push, WebView, Alert, ImageNotice, ShowImageNotices, Unreal, Release Notes, 2.17.1
---

### 2.17.1 (2020.10.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.17.1/GamebaseSDK-Unity.zip)

#### 기능 추가
* Unreal SDK 기능 추가: SDK 2.15.0
    * 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
        * ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트 확인 가능
    * API 추가
        * 상품 ID로 결제 요청하고 추가 정보(UserPayload)를 입력해 결제 완료 시 확인 가능한 결제 API 추가
        * 이미지 공지 표시: showImageNotices
        * Push 토큰 정보 확인: queryTokenInfo
    * 푸시 토큰 등록 시 NotificationOption 설정으로 앱이 포그라운드(foreground) 상태에서도 푸시 알림을 받을 수 있도록 기능 추가
    * WebViewConfiguration contentMode 설정 추가
    
#### 기능 개선/변경
* [SDK] 2.17.1
    * (Unity) Unity 2017.2.5 지원

#### 버그 수정
* [SDK] 2.17.1
    * (Unity) 이미지 공지와 웹뷰를 차례로 호출하면 뒤에 호출한 API가 동작하지 않는 오류 수정
