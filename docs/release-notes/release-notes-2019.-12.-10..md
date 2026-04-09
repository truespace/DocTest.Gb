---
source: release-notes.md
section: "2019. 12. 10."
order: 39
split: true
created_date_time: 20260408_184906
keyword: Mapping, Analytics, Android, iOS, Release Notes, 2.6.1
---

### 2019. 12. 10.

#### 기능 추가
* 앱 > 앱: 점검 중 QA 테스트 단말기 등록시 IP 로도 등록할 수 있는 기능 추가	

#### 버그 수정
* [Console]
	* 의미에 맞지 않는 일본어 문구 수정
* [SDK] 2.6.1
	* (Android)Gamebase.initialize() 호출 전에 Gamebase.login() 을 호출할 때 크래시가 발생하는 문제 수정
	* (Android)TOAST Analytics User Data 를 java 주소 값으로 잘못 전송하는 문제 수정
	* (Android)IAP 상품을 활성화 시키지 않은 경우 발생하는 크래시 수정
	* (iOS)AddMapping(강제, Forcibly) 사용 시, 매핑이 되지 않는 문제 수정
	* (iOS)Unity Plugin으로 PushConfiguration의 displayLanguageCode를 설정하지 않을 경우, NSNull 객체에 의하여 크래시가 발생하는 문제를 수정
