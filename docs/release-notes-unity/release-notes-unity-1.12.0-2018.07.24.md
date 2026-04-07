---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v1.12.0, 버그수정, 기능개선, 기능추가, 변경, 제거, Login"
section: "1.12.0 (2018.07.24)"
order: 117
---

### 1.12.0 (2018.07.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] Setting Tool
    * Setting Tool 최신 버전이 있을 경우 업데이트 알림 기능 추가 
    * 내부 null Exception 수정
    
#### 버그수정
* [SDK] 1.12.0
    * (Unity)IssueTransferKey API 호출 시 exception 발생하던 버그 수정
    * (Unity)Unity Google Adapter 제거 : 기존에 GoogleAdapter 사용중인 개발사는 아래 업데이트 가이드 참고
    

**Unity Google Adapter 업데이트 가이드**

* Unity SDK 1.6.0이상 1.11.0 이상 버전을 사용하는 경우 1.12.0 버전으로 업데이트 하기 전에 아래 내용을 필히 숙지하셔야 합니다.(1.6.0 미만 버전 사용중인 경우에는 GoogleAdapter를 미사용하기 때문에 영향이 없습니다.)
    1. Setting Tool 설정
        * GoogleAdapter가 제거됨에 따라 더이상 Unity 탭에서 Google 항목이 노출되지 않는다.
        * Google 인증을 사용할 경우에는 각 플랫폼 탭에서 Google 항목을 활성화한다.
            * Android > Authentication > Google 선택해서 설정
            * iOS > Authentication > Google 선택해서 설정
    2. Gamebase Login API (변경 없음)
        * Gamebase.Login(GamebaseAuthProvider.GOOGLE, callback);
    3. GPGS 기능을 사용하는 경우
        * GPGS SDK for Unity 유지
        * GPGS 관련 로직은 앱에서 별도로 관리
    4. GPGS 기능을 사용하지 않는 경우
        * GPGS SDK for Unity 삭제
