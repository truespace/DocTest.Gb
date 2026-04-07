---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2018. 12. 27."
section: "2018. 12. 27."
order: 64
---

### 2018. 12. 27.

#### 기능 추가
* Console
	* Push - 반복발송 기능 추가

#### 기능 개선/변경
* [SDK] 1.14.5
	* deprecated 되었던 다음 API가 제거되었습니다.
		* (void)Gamebase.WebView.showWebBrowser(Activity, String)
		* (void)Gamebase.Network.addOnChangedListener(NetworkManager.OnChangedListener)
		* (void)Gamebase.Network.removeOnChangedListener(NetworkManager.OnChangedListener)
		* (void)Gamebase.Launching.addOnUpdatedListener(LaunchingOnUpdateListener)
		* (void)Gamebase.Launching.removeOnUpdatedListener(LaunchingOnUpdateListener)
	* 결제 모듈(gamebase-adapter-purchase-iap) 수정되었습니다.
		* IAP SDK를 1.5.2로 업데이트
		* Client에서는 사용되지 않는 IAP TEST Store 제거
		* 결제 재처리 로직(requestRetryTransaction)에서 데이터가 불완전할 때 호출이 실패하는 문제를 수정
		* 크래시를 방지하기 위해 모든 IAP SDK 호출부에 예외 처리
* Console
	* 인증이 풀렸을 때 Rest API 요청에도 로그인페이지로 이동하도록 수정
	* IAP Transaction 조회 필터 추가
