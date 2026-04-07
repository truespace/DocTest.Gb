---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v1.13.0, 버그수정, 기능개선, 기능추가, 변경, 제거, Push, IdP, IAP"
section: "2018. 09. 13."
order: 69
---

### 2018. 09. 13.

#### 기능 추가
* Console	
	* 회원: 계정의 IdP 추가 및 삭제 기능 추가, IdP ID 검색 기능 추가
	* 푸시: 푸시상태별로 발송이력 조회하는 기능 추가
* [SDK] 1.13.0
	* (iOS)App Store Promotion IAP를 지원하기 위한 API 추가


#### 기능 개선/변경
* [SDK] 1.13.0
	* (공통)IAP SDK 최신버전 적용 (android:1.5.1, iOS:1.6.0)
	* (Android)Push API 호출 시, Gamebase 초기화/로그인 상태에 따라 호출 실패에 대한 에러 메시지를 보다 명확하게 개선
		* 초기화 전 호출 : NOT_INITIALIZED(1)
		* 초기화 이후 호출시 Push 모듈이 없음 : NOT_SUPPORTED(10)
		* 초기화 성공 및 로그인 이전 호출 : NOT_LOGGED_IN(2)		
	* (iOS)authProviderProfileWithIDPCode api의 호출 결과의 구조가 1depth로 변경 (Android, Unity와 통일)
	* (Unity)로그에서 보여주는 json 데이터를 알아보기 쉽도록 출력 포맷 개선
* Console
	* 이용정지 : 앱가드를 이용한 이용정지 등록하는 UI 개선 - 기능 off시 데이터 초기화, Leaderboard 데이터 삭제 설정을 상태가 'on'인 경우에만 노출하도록 개선
	
#### 버그수정
* [SDK] 1.13.0
	* (Android)NaverCafe SDK와의 충돌로 Naver 로그인시 발생하던 오류 해결
	* (Unity)Unity 2017.2 이상 버전에서 Editor Play Mode 종료 시 websocke close 처리에서 발생하던 오류 수정
* Console
	* App : 정보 수정시 삭제버튼 뒤의 내용이 잘리는 현상 수정
