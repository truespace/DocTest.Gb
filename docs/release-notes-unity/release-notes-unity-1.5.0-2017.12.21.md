---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v1.5.0, 신규, 버그수정, 기능추가, Login"
section: "1.5.0 (2017.12.21)"
order: 128
---

### 1.5.0 (2017.12.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.5.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 1.5.0
    * 웹뷰가 닫힐 때 발생하는 Close Callback 추가
    * 웹뷰에서 사용하는 Custom Scheme의 Event를 받을 수 있는 기능 추가
    * Unity Setting Tool 신규 배포

#### 버그 수정
* [SDK] 1.5.0
    * (Unity)UnityEditor에서 Guest로그인이 되지 않는 현상 수정
    * (Unity)TOAST Console에 Facebook 인증 정보를 등록하지 않고 Gamebase.Login("facebook") API를 호출할 경우, KeyNotFoundException이 발생하여 방어코드 추가
