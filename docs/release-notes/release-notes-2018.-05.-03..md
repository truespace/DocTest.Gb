---
source: release-notes.md
section: "2018. 05. 03."
order: 79
split: true
created_date_time: 20260408_191848
keyword: Login, Mapping, Error, Android, iOS, Release Notes, 1.9.0
---

### 2018. 05. 03.

#### 기능 추가
* Transfer 기능 추가
    - guest 사용자가 매핑없이 새로운 기기로 이전할 수 있는 기능
    - (SDK공통)추가된 API 
		* Transfer Key 발급 API (IssueTransferKey)
		* 발급된 TransferKey를 사용하여 계정 이전을 요청하는 API (RequestTransfer)
    - (console)회원메뉴의 매핑이력조회 탭에서 Transfer 이력 확인이 가능
* 이용정지 등록시 사용자의 리더보드(랭킹) 데이터를 삭제할 수 있는 옵션 추가(TOAST Leaderboard를 사용하는 경우에 한함)
    - 이용정지 등록 메뉴를 이용하거나 App Guard 연동 페이지에서 사용 가능

#### 버그 수정
* [SDK] 1.9.0
	* (iOS) Naver계정을 이용한 로그인 중 App to Web 로그인 시도 시, 서버로부터 받아온 Scheme의 형식이 변경되어, 로그인이 되지 않는 현상 수정
    * (iOS) Adapter로부터 UnderlyingError 객체를 받아서 유저에게 전달되는 에러객체를 생성하는 로직에서 메시지 및 Underlying Error의 설정이 되지 않는 버그 수정
    * (Android) Heartbeat 에서 잘못된 사용자로 판정되는 경우 이용정지 팝업이 뜨지 않도록 수정(iOS 와 동일한 로직으로 수정)
