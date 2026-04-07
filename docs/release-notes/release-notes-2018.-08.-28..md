---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "XCode, v1.12.2, 버그수정, 기능개선, 기능추가, 변경, 제거, Push, IAP"
section: "2018. 08. 28."
order: 70
---

### 2018. 08. 28.

#### 기능 추가
* Console	
	* 회원: 계정상태 변경 기능 추가, Push Token 조회 추가
	* 운영지표(유저통계) : 오늘 탈퇴자, 당일 가입 후 탈퇴자 지표 추가

#### 기능 개선/변경
* [SDK] 1.12.2
	* (Android)WebSocket 타입아웃시 (API 호출 시간 경과), 크래시가 날 수 있는 버그에 대해 방어로직 처리
	* (iOS)Google Auth Adapter, Naver Auth Adapter의 Callback URL Scheme 설정 개선
		* 콘솔에 "url_scheme_ios_only" 값을 설정하지 않으면 Default URL Scheme을 설정 하도록 개선 : Default URL Scheme을 사용하기 위해서는 XCode > Target > Info > URL Types에 tcgb.{Bundle ID}.google 또는 tcgb.{Bundle ID}.naver 등록 필요
	* (iOS)Payco Auth Adapter 개선
		* URL Scheme 미설정으로 인해 의도치 않은 URL Scheme을 호출하던 문제 수정 : 설정 방법이 변경되어 업데이트를 위해서는 반드시 URL Scheme 설정 필요 (XCode > Target > Info > URL Types에 tcgb.{Bundle ID}.payco를 등록)
* Console
	* 회원 : 아이디 매핑 이력 조회 기능 추가(최근 3개월 조회 -> 조회기간 직접 설정하도록 변경)
	* 구매(IAP) : 결제 정보 엑셀 다운로드 1일로 제한, 아이템 삭제 기능 삭제
	
#### 버그수정
* [SDK] 1.12.2
	* (Android)auth-twitter-adapter 를 포함한 상태에서 TargetSdk 28로 빌드시 초기화 에러가 발생하는 문제 수정
