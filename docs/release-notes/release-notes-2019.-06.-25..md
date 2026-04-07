---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2019. 06. 25."
section: "2019. 06. 25."
order: 54
---

### 2019. 06. 25.

#### 기능 추가
* 전송 지표 기능 추가
    * [Console]Analytics > 전송지표: Level, Channel, Class별 지표 확인 메뉴 오픈
		* 실시간 현황
		* 레벨별 현황
		* 월드/서버/채널별 현황
		* 클래스/직업별 현황
		* 레벨업
		* 아이템 판매 현황
		* 아이템 판매 TOP 50

#### 기능 개선/변경
* [SDK] 2.4.2
	* (공통)LaunchingInfo에 JSON string 형식의 TOAST Launching 정보를 추가
	* (iOS)LINE SDK 업데이트(v5.0.1)
		* LINE Adpater의 최소 지원 OS 버전이 iOS 10으로 변경 
		* LINE 앱을 통한 로그인 기능 추가

#### 버그수정
* [SDK] 2.4.2
	* (공통)Analytics 버그 수정: 로그아웃, 탈퇴, 계정 이전 시 저장된 지표 데이터를 초기화 하도록 수정
	* (iOS)네트워크 연결 문제로 간헐적으로 크래시가 발생하던 현상 수정
