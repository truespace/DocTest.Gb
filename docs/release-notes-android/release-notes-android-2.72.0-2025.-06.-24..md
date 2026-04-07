---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, v2.72.0, 버그수정, 기능개선, 기능추가, 변경, Login, Guest"
section: "2.72.0 (2025. 06. 24.)"
order: 10
---

### 2.72.0 (2025. 06. 24.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.72.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경

* 웹소켓 모듈이 중복 호출되는 경우 ArrayIndexOutOfBoundsException이 발생할 수 있는 로직을 수정했습니다.
    * 이 문제는 Gamebase Android SDK 2.71.2에서만 발생합니다.

#### 버그 수정

* LINE IdP의 Region 추가 정보 대응이 되지 않아 매핑 관련 동작에서 발생하는 문제를 수정했습니다.
    * Gamebase.login("guest") -&gt; Gamebase.addMapping("line") -&gt; Gamebase.loginForLastLoggedInProvider() 호출 실패 이슈
    * Gamebase.login(idp) -&gt; Gamebase.addMapping("line") -&gt; AUTH\_ADD\_MAPPING\_ALREADY\_MAPPED\_TO\_OTHER\_MEMBER(3302) -&gt; Gamebase.changeLogin(ForcingMappingTicket) 호출 실패 이슈
    * Gamebase.login("line") -&gt; Gamebase.addMapping(idP) -&gt; AUTH\_ADD\_MAPPING\_ALREADY\_MAPPED\_TO\_OTHER\_MEMBER(3302) -&gt; Gamebase.changeLogin(ForcingMappingTicket) 호출 실패 이슈
