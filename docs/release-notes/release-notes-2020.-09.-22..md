---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v2.16.0, 기능개선, 기능추가, 변경, Analytics, Notice, Contact"
section: "2020. 09. 22."
order: 17
---

### 2020. 09. 22.

#### 기능 추가
* 고객센터 기능 추가
    * [Console] 고객 센터 메뉴 오픈: 고객 문의 처리, FAQ/공지 사항 관리 
    * [SDK] 2.16.0
	* (공통) API 추가(Gamebase.Contact.requestContactURL): 고객 센터 URL 리턴
	* (공통) 고객 센터 API 에 userName 을 설정할 수 있도록 ContactConfiguration 파라미터 추가 
		
#### 기능 개선/변경
* [Console] 
    * Analytics 메뉴 공통: 국가별 필터 정렬 기준 변경(지표 내림차순 -> 국가 이름 오름차순)     
    * Analytics > 매출지표: 스토어별 대시보드에 해당 스토어의 국가별 결제 금액 이외에 결제 금액 총합도 함께 표시
