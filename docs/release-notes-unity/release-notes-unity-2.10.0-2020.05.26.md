---
source: release-notes-unity.md
section: "2.10.0 (2020.05.26)"
order: 87
split: true
created_date_time: 20260408_191848
keyword: Unity, Mapping, Purchase, Push, WebView, Error, iOS, Release Notes, 2.10.0
---

### 2.10.0 (2020.05.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.10.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.10.0
    * (공통) 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
        * ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트도 확인 가능

#### 기능 개선/변경
* [SDK] 2.10.0 
    * (Unity) StandaloneWebviewAdapter 내부의 CefWebview 버전 업데이트: v2.0.4
        * WebviewIndex 검증 로직을 개선
        * 웹뷰 생성 시, 간헐적으로 NullReferenceException이 발생하는 오류를 개선
    * (Unity) GamebaseErrorCode에 소켓 연결에 관한 에러 코드 추가: SOCKET_CONNECTION_TIMEOUT, SOCKET_CONNECTION_FAIL

#### 버그 수정
* [SDK] 2.9.1
    * (Andoird) 매핑 이후 지표 레벨이 null이 되어 결제 지표에 정상적으로 반영되지 않는 오류 수정
    * (iOS) unreal 엔진에서 빌드 하면, warning을 빌드 오류로 판정해서 빌드가 안되는 부분을 수정
