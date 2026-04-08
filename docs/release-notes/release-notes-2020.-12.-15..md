---
source: release-notes.md
section: "2020. 12. 15."
order: 12
split: true
created_date_time: 20260408_191848
keyword: Login, Purchase, Push, WebView, Analytics, ShowWebView, Android, iOS, Release Notes, 2.18.2
---

### 2020. 12. 15.

#### 기능 추가
* Gamebase 고객센터 페이지 오픈 시 게임에서 정의한 extra data 전달: SDK 2.18.2
	* [Console] 고객센터 > 고객 문의: 고객 문의 상세 조회 화면에서 추가로 등록한 extra data 확인 가능
* [SDK] 2.18.2
	* (공통) 개발사 자체 고객센터 오픈 시 additionalURL 필드 추가
	* (공통) 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription

#### 기능 개선/변경
* [Console]
	* Analytics: 필터 검색 후 날짜 변경하여도 선택한 검색 조건이 유지되도록 개선
	* Push > 푸시: Tencent Push 제거
	* 구매(IAP) > 결제 정보: 환불 상태에서 영수증 검증 버튼 노출되지 않도록 변경
* [SDK] 2.18.2
    * (공통) TOAST SDK 업데이트: [Android(0.24.2)](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-android/#0242-20201124), [iOS(0.27.1)](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-ios/#0271-20201124), [Unity(0.21.3)](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-unity/#0213-20201124)
	* (Android) 암호화 로직 보안 경고 해결을 위한 외부 SDK 업데이트: Payco Login SDK(1.5.3), Hangame ID SDK(1.3.2)
	* (Android) Tencent Push 모듈 제거
	* (Android) Gamebase Android SDK 2.6.0에서 deprecated된 함수 제거
		* GamebaseConfiguration.Builder.setFCMSenderId()
		* GamebaseConfiguration.Builder.setTencentAccessKey()
		* GamebaseConfiguration.Builder.setTencentAccessId()
	* (iOS) showWebView: 잘못된 URL을 전달했을 경우 에러 반환, 전달받은 URL은 인코딩하지 않고 그대로 사용
	* (iOS) 대소문자 상관없이 커스텀 스킴이 동작하도록 변경
	* (Unity) GamebaseRequest.GamebaseConfiguration 클래스의 필드 deprecated: zoneType, fcmSenderId

#### 버그 수정
* [Console]
	* 구매(IAP) > 아이템: 파일로 아이템을 대량 등록하면 중복으로 등록되는 문제 수정
* [SDK] 2.18.2
    * (Android) 5.0~6.0 OS 단말기에서 웹뷰 커스텀 스킴이 동작하지 않는 문제 수정
