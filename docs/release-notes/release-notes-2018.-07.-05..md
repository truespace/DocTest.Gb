---
source: release-notes.md
section: "2018. 07. 05."
order: 73
split: true
created_date_time: 20260408_184906
keyword: Login, Android, iOS, Release Notes, 1.11.1
---

### 2018. 07. 05.

#### 기능 추가
* Line IdP 추가 : iOS

#### 기능 개선/변경
* [SDK] 1.11.1
	* (공통)Guest로그인 후 AddMapping 성공 시, loginForLastLoggedInPrivder를 하게되면, AddMapping 성공한 IdP계정을 사용하여 로그인하도록 변경
	
#### 버그수정
* [SDK] 1.11.1
	* (공통)점검 해제 후 후속 API 진행(login/push/purchase 등)이 되지 않던 버그 수정
	* (Android)Gamebase.addObserver()를 통해 ObserverMessage를 수신하였을 경우, ObserverMessage.data.code의 타입이 int가 아니라 String인 버그를 수정
* Console
	* Windows client 등록 시 스토어코드가 잘못 등록되던 문제 수정
