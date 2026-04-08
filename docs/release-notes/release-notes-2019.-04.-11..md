---
source: release-notes.md
section: "2019. 04. 11."
order: 59
split: true
created_date_time: 20260408_191848
keyword: Analytics, Initialize, TransferAccount, Android, iOS, Release Notes, 2.2.2
---

### 2019. 04. 11.

#### 기능 개선/변경
* [SDK] 2.2.2
	* (Unity)SDK 로그 개선
* [Console]
	* Analytics 메뉴 다국어 적용
	* 보안검수 관련 취약점 패치

#### 버그수정
* [SDK] 2.2.2
	* (Android)Gamebase 초기화 이전 TransferAccount API 호출시, 콜백이 오지 않는 이슈를 수정
	* (iOS)showBlockingPopup을 NO로 설정 할 경우 Gamebase 초기화 콜백이 호출되지 않는 이슈를 수정
	* (Unity)AddMappingForcibly API를 호출하면 크래시가 발생하여 수정
