---
source: release-notes.md
section: "2021. 04. 13."
order: 2
split: true
created_date_time: 20260408_191848
keyword: Purchase, Push, Authentication, Error, ShowWebView, Android, iOS, Release Notes, 2.21.0
---

### 2021. 04. 13.

#### 기능 추가
* [SDK] 2.21.0
	* (공통) Hangame 일본 인증 추가

#### 기능 개선/변경
* [Console] 
	* 회원 > 멤버: 푸시 토큰 조회 시 광고성 수신 동의, 야간 광고 수신 여부가 ture인 경우 수신한 일자도 함께 표시되도록 개선 
	* 구매(IAP) > 결제 정보: 추가 정보 표시되는 팝업 창에 문자열이 줄 바꿈 되어 보이도록 개선
	* 구매(IAP) > 결제 어뷰징 모니터링
		* 1시간으로 고정되어 있던 자동 제재 감지 기간을 사용자가 입력(1시간~48시간)할 수 있도록 개선
		* AND 조건만 설정 가능하던 건수, 금액 자동 제재 조건 입력을 OR 조건도 입력할 수 있도록 개선
* [SDK] 2.21.0	
	* (Android) 외부 SDK 업데이트: Facebook Android SDK(6.5.1), Line Android SDK(5.4.0)
	* (iOS) bitcode 지원이 가능하도록 변경
	* (iOS) showWebView 호출 시, 닫기 버튼을 가장 먼저 화면에 표시되도록 수정
	
#### 버그 수정
* [SDK] 2.21.0
	* (Android) Proguard를 적용한 빌드에서 결제 API 호출 시 크래시가 발생하는 오류 수정
