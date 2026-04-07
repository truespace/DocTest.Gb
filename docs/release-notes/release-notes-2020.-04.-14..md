---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v2.8.1, 버그수정, 기능개선, 기능추가, 변경, Analytics"
section: "2020. 04. 14."
order: 31
---

### 2020. 04. 14.

#### 기능 개선/변경
* [Console] 
	* Analytics 공통: TUI 차트 버전 업데이트, Frequency7 지표에 적용
* [SDK] 2.8.1 
	* (공통) Analytics 전송 결과 확인을 위한 내부 지표 추가
	
#### 버그 수정
* [Console] 
	* Analytics 공통: 국가명이 길어질 경우 스크롤이 영역을 벗어나는 이슈 수정
	* Analytics > 실시간 모니터링: 데이터 저장 중에 조회 요청시 지표가 0으로 보이는 현상 수정
* [SDK] 2.8.1 
	* (Android) 프로세스 재시작 이후 크래시가 발생할 수 있는 코드를 수정
	* (JavaScript) credentialInfo 로그인에서 Hangame IdP로 로그인이 안되는 문제를 수정
