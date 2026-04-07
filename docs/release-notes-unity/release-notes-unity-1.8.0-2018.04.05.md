---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "1.8.0 (2018.04.05)"
section: "1.8.0 (2018.04.05)"
order: 124
---

### 1.8.0 (2018.04.05)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.8.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* Kick out 기능 추가
    * 현재 게임 중인 전체 사용자의 연결을 끊는 기능(점검시 게임에서 전체 사용자의 연결을 끊고 싶을 때 사용할 수 있음)
    * (SDK 공통)kick out 이벤트를 받을 수 있는 API 추가
* 점검 웹페이지를 사용자가 Console에서 입력한 HTML 페이지로 사용할 수 있도록 기능을 개선
    * 이전에는 Gamebase에서 제공하는 웹페이지나 외부 웹페이지 연결만 가능했음
    * 웹서버가 없는 경우에도 점검페이지를 사용자가 원하는 형태로 만들 수 있음
* Observer 기능 개발 및 API 추가
    * (SDK 공통) 점검 등 앱 상태/네트워크 상태/유저 상태(이용 정지) 변경사항에 대한 Listener를 Observer 등록을 통하여 일괄 처리할 수 있도록 API 추가

#### 기능 개선/변경
* [SDK] 1.8.0
    * (공통)Observer 기능 추가에 따라 다음 API Deprecated : LaunchingStatus Listener, Network Listener(기존 사용자는 계속 사용 가능)
    * (iOS)페이코 간편로그인 3rd SDK v1.2.2 적용 : 로그인 성공 시 토큰 만료 정보(expires_in) 제공, iPhoneX 로그인 UI 개선
    * (iOS)iPhoneX 지원을 위하여, 웹뷰 사용 인터페이스 수정

#### 버그 수정
* 국가코드(contry code)가 10자 이상인 경우 동접 데이터가 저장되지 않는 현상 수정
* [SDK] 1.8.0
    * (Setting Tool)Unity Facebook Adapter를 체크하면 에러가 나는 버그 수정
