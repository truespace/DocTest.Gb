---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2018. 11. 15."
section: "2018. 11. 15."
order: 65
---

### 2018. 11. 15.

#### 기능 추가
* Console
	* 중국어 적용
	* 회원 : 구매이력에 App Store 영수증 검증 기능 추가	

#### 기능 개선/변경
* Console
	* 달력 다국어 지원 추가
* [SDK] 1.14.2
	* (Android)점검시, 데이터구조에서 점검 시작/종료 시간을 의미하는 epoch time의 타입을 기존 String에서 long으로 타입 변경 : 기존 Gamebase Unity와 연동 후 점검 호출 시 타입불일치로 콜백이 내려오지 않는 현상으로 인한 수정
	* (iOS)Provider Profile 획득 메서드 호출 시, 반환하는 TCGBAuthProviderProfile 객체의 description 메서드의 JSON 문자열 구조 변경으로 인하여 Gamebase iOS SDK 1.14.0와 Unity Plugin 1.14.0 적용시 crash가 발생될 수 있는 구조 수정

#### 버그수정
* Console
	* 푸시 : 특정대상 발송 이후 등록된 푸시건을 복사하여 등록할 때 등록 실패하던 문제 수정	
* [SDK] 1.14.2
	* (Android)에뮬레이터 환경에서 스토어앱(PlayStore, OneStore 등)이 없는 상태에서 "앱 설치/업데이트"시 스토어 미체크로 인한 crash 버그를 수정
	* (Unity)ShowWebView API 호출시 파라메타에 Callback을 넣지 않으면 crash가 발생되는 부분 수정
	* (Unity)iOS SDK의 Deleted API를 호출하는 코드가 있어 컴파일시 오류가 발생 되는 버그 수정
