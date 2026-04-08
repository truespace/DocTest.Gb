---
source: release-notes-unity.md
section: "2.8.0 (2020.03.24)"
order: 91
split: true
created_date_time: 20260408_191848
keyword: Unity, Login, Purchase, Initialize, Android, Console, Release Notes, 2.8.0
---

### 2.8.0 (2020.03.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.8.0
    * (공통) 결제 및 상품 정보에 상품 타입 및 지역 가격 등의 정보를 추가
    * (Unity) StandaloneWebviewAdapter 내부의 CefWebview가 v2.0.1 버전으로 업데이트
        * PopupType이 PASS_INFO일 경우, 팝업 창을 띄우지 않고 팝업 창 정보를 전달하는 기능을 추가

#### 기능 개선/변경
* [SDK] 2.8.0 
    * (공통) 콘솔에 등록되지 않은 앱 버전으로 초기화 실패할 때 스토어로 이동할 수 있는 팝업 창이 추가로 노출하도록 개선
    * (Android) 로그인 직후 결제 관련 API를 호출할 때 초기화 타이밍 문제로 실패가 발생할 수 있는 코드를 수정
