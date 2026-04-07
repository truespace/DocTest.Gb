---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2019. 07. 11."
section: "2019. 07. 11."
order: 51
---

### 2019. 07. 11.

#### 기능 개선/변경
* [Console]Analytics
	* 레벨업 쿼리 성능 개선
	* 차트 내 min, max 정보 노출
	* 다국어 적용(중국어)

#### 버그 수정
* [SDK] 2.4.3
	* (iOS)인증 시도 시 오류가 발생했을 경우, 형식에 맞지 않는 오류 메시지 파싱 시도에 따른 크래시 발생 이슈 수정
	* (Unity)iOS와 Android로 빌드시 AddMappingForcibly API 가 동작하지 않는 오류 수정
	* (Unity)RequestRetryTransaction API 호출시 iOSPlugin에서 JSON 파싱 오류가 있어 수정
