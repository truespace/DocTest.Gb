---
source: release-notes.md
section: "2019. 05. 16."
order: 57
split: true
created_date_time: 20260408_191848
keyword: Login, Mapping, Purchase, Authentication, TransferAccount, Android, Console, Release Notes, 2.3.1
---

### 2019. 05. 16.

#### 기능 추가
* [Console]
	* 단말기 이전 기능 추가(신규 메뉴)
		* 앱 > 기기 이전(Transfer account): 기기이전 기능 사용을 위한 설정값 저장
		* 회원 > 기기 이전: 발급된 키의 상태 및 이력 조회

#### 기능 개선/변경
* [Console]
	* 앱: AppleGameCenter, China IdP에 '토큰재검증' 옵션 Off
		* 해당 IdP에서는 실제 외부IdP 체크하지않고 내부토큰만 체크하므로 의미없는 옵션이므로 제거
	* 회원: 매핑 추가 가능한 조건 변경
		* 기존:Guest계정
		* 변경:Guest계정, Missing 계정

#### 버그수정
* [SDK] 2.3.1
	* (Android)2.3.0버전에서 Twitter 로그인 되지 않던 문제 수정
* [Console]
	* 회원: 구매 이력에서 영수증 검증이 되지 않던 문제 수정
	* Kickout: 조회 요청시 인증체크 추가하여 비정상 동작하던 이슈 수정
