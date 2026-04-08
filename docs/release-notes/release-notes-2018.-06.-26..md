---
source: release-notes.md
section: "2018. 06. 26."
order: 74
split: true
created_date_time: 20260408_191848
keyword: Login, Initialize, Authentication, Error, Android, iOS, Release Notes, 1.11.0
---

### 2018. 06. 26.

#### 기능 추가
* iOS Google IdP 추가 : iOS
* Twitter IdP 추가 : Android, iOS
* Line IdP 추가 : Android만 제공. iOS는 2018년 7월 제공 예정입니다.
* Server API 추가 
	* getSimpleLaunching : 클라이언트 앱 기동시 제공되는 Launching 정보 확인용 API
	
#### 기능 개선/변경
* [SDK] 1.11.0
	* (공통)LocalizedString 일본어 번역 추가
	* (공통)인증 API 호출시 초기화, 로그인을 하지 않은 경우 명확히 에러 코드를 구분하도록 내부 로직을 개선
	* (Android)'android.permission.READ_PHONE_STATE' 권한 제거
	* (Android)GamebaseConfiguration.Builder의 필수 설정값인 setAppId, setAppVersion을 생성자에서 입력할 수 있도록 변경
	* (Android)GamebaseConfiguration.Builder 의 setServerApiVerseion API를 제거
	* (Android)getAuthBanInfo() API, class AuthBanInfo 이름을 변경 : getBanInfo(), class BanInfo
	* Naver ID Login SDK 업데이트 : iOS(4.0.10)
* Sample App 
	* ServerPush 기능 및 Observer 기능 추가
	* Gamebase SDK 업데이트 : Android(1.9.0), iOS(1.9.0), Unity(1.10.1)
