---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2017. 11. 30."
section: "2017. 11. 30."
order: 87
---

### 2017. 11. 30.

#### 기능 추가

* [Console]
	* [Management > 알람] Webhook 알람 등록하는 기능 추가
	* [Operating indicator > 모니터링] Push 발송 이력 조회 추가

#### 기능 개선/변경
* [Console]
	* [Operating indicator > 모니터링] 차트 색상 변경, Timezone 이슈. DAU 계산로직 변경(Login시간기준->접속시간기준)
* [API] [점검 조회 API](../../api-guide.md#check-under-maintenance) 결과를 List 에서 단일 객체로 변경

#### 버그 수정
* [Console]
	* [Push] Push 등록 시 기본언어가 선택되어 있지 않아도 등록되는 오류 수정
