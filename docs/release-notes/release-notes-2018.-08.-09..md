---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v1.12.1, 버그수정, 기능개선, 기능추가, 변경, Maintenance, Guest, IdP, IAP"
section: "2018. 08. 09."
order: 71
---

### 2018. 08. 09.

#### 기능 개선/변경
* [SDK] 1.12.1
	* (공통)IAP SDK 최신버전 적용 (1.5.0)
	* (공통)Gamebase 점검페이지에서 점검시간을 단말기 설정 국가시간에 맞추어 노출하도록 개선
	* (공통)점검페이지를 외부 페이지로 사용할 때 Console에 입력한 점검 정보를 사용할 수 있도록 기능 추가
	* (공통)IdP 매핑된 사용자의 Guest 매핑시도시 에러 발생(TCGB_ERROR_AUTH_ADD_MAPPING_CANNOT_ADD_GUEST_IDP)
	* (공통)인증 API 중복 호출시 에러 발생(AUTH_ALREADY_IN_PROGRESS_ERROR)
	* (Android)TencentPush SDK 업데이트 (3.2.3)
	* (Android)Onestore v17(API v5) 지원 : Gamebase에서는 v16(스토어코드=TS)은 제공하지 않습니다.
	* (iOS)에러코드 추가 : Gamecenter 로그인 거부(TCGB_ERROR_IOS_GAMECENTER_DENIED)
* [SDK] Setting Tool
	* 폴더명 변경 : TOAST -> Toast
	* 에러발생시 팝업 알림 추가 : File Download 실패, File Extract 실패, XML 파싱 실패
	
#### 버그수정
* [SDK] 1.12.1
	* (iOS)Naver 로그인 시 프로필 정보 조회 실패로 인해 로그인이 불가능한 버그 수정 : 프로필 정보 조회 실패하더라도 로그인은 성공하도록 변경	
* Console
	* 결제 내역: 'Reserved'상태에서 결제 상태 변경이 되지 않는 버그와 엑셀 다운로드 시 필터링이 적용되지 않던 문제 수정
