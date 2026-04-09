---
source: release-notes.md
section: "2020. 03. 24."
order: 32
split: true
created_date_time: 20260408_184906
keyword: Login, Purchase, Analytics, Initialize, Authentication, Android, Unity, Release Notes, 2.8.0
---

### 2020. 03. 24.

#### 기능 추가
* [Console] 
	* 신규 메뉴 오픈: Analytics > 이용자 지표 > Frequency 7
		* DAU의 일주일간 방문수와 비율 정보를 제공합니다. 게임몰입도, 충성도 등을 한 눈에 파악할 수 있습니다.
	* 쿠폰 > 쿠폰 발급: 쿠폰 문자 발송 기능 추가
* [SDK] 2.8.0
	* (공통) 결제 및 상품 정보에 상품 타입 및 지역 가격 등의 정보를 추가
	* (Unity) StandaloneWebviewAdapter 내부의 CefWebview가 v2.0.1 버전으로 업데이트
		* PopupType이 PASS_INFO일 경우, 팝업을 띄우지 않고 팝업 정보를 전달하는 기능을 추가
 	* (Javascript) 한게임 채널링 지원: 한게임 IdP 인증, 한코인 결제 추가


#### 기능 개선/변경
* [Console] 
	* 앱 > 전송 지표 세팅: 미리 등록한 메타 필터만 전송 지표에 사용할 수 있도록 제한
		* 메타필터 개수 제한하여 그 이상 전송하는 경우 지표가 노출되지 않으니 주의해 주세요.: 레벨(5,000개), 월드/서버/채널(100개), 직업/클래스(100개)
* [SDK] 2.8.0 
	* (공통) 콘솔에 등록되지 않은 앱 버전으로 초기화 실패할 때 스토어로 이동할 수 있는 팝업이 추가로 노출하도록 개선
	* (Android) 로그인 직후 결제 관련 API를 호출할 때 초기화 타이밍 문제로 실패가 발생할 수 있는 코드를 수정

#### 버그 수정
* [Console] 
	* 매출 지표 > 결제 금액
		* 차트 툴 팁에 통화가 원(KRW)으로 고정되어 노출되어 앱에서 설정한 통화로 보이도록 수정
		* 월별 조회시 2월 지표가 노출안되는 이슈 수정
