---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2019. 09. 10."
section: "2019. 09. 10."
order: 47
---

### 2019. 09. 10.

#### 기능 추가
* [Console]
	* Analytics: 채널/월드/서버, 직업/클래스 전송지표에 레벨 지표 추가 노출
	
#### 기능 개선/변경
* [Console]
	* Analytics: Grid 렌더링 성능 개선(tui-grid 4.4.x 적용)
* [SDK] 2.5.1
	* (iOS) GamebasePushAdapter에서 사용중인 TCPushSDK를 1.7.0으로 업데이트
		* TCPushSDK가 Static Library에서 Framework 파일로 변경되었으므로 프로젝트에 TCPushSDK.framework를 추가해야 합니다.
