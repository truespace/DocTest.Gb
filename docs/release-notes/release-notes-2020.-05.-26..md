---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v2.10.0, 기능개선, 기능추가, 변경, WebView, Coupon"
section: "2020. 05. 26."
order: 27
---

### 2020. 05. 26.

#### 기능 추가
* [Console] 
	* 쿠폰 > 쿠폰 발급: 발송 통계 기능, 쿠폰 발송 내역 다운로드 기능 추가
* [SDK] 2.10.0
	* (공통) 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
		* ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트도 확인 가능

#### 기능 개선/변경
* [Console] 
	* 전체: 공통 디자인 가이드에 맞도록 버튼/태그 UI 수정
* [SDK] 2.10.0 
	* (Unity) StandaloneWebviewAdapter 내부의 CefWebview 버전 업데이트: v2.0.4
		* WebviewIndex 검증 로직을 개선
		* Webview 생성 시, 간헐적으로 NullReferenceException이 발생하는 오류를 개선
	* (Unity) GamebaseErrorCode에 소켓 연결에 관한 에러 코드 추가: SOCKET_CONNECTION_TIMEOUT, SOCKET_CONNECTION_FAIL
