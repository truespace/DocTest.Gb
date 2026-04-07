---
source: release-notes-console.md
split: true
created_date_time: 20260406_141859
keyword: "2020. 02. 25."
section: "2020. 02. 25."
order: 85
---

### 2020. 02. 25.

#### 기능 추가
* [Console]
	* 쿠폰 > 쿠폰 발급: 발급한 쿠폰을 설정한 스토어에서만 사용할 수 있도록 기능 추가

#### 기능 개선/변경
* [Console]
	* 앱 > 앱: 동일한 클라이언트 버전 삭제 이후 재등록 시 알림 로직 추가
	* 구매(IAP) > Item: 등록 시 구독 상품 등록을 위한 등록 필드값 추가(App Store - Shared secret,Google store - Domain authentication File Names)

#### 버그 수정
* [Console]
	* Analytics > 실시간 모니터링 > 실시간 지표: 간헐적으로 푸시 발송 후 ccu 항목에 빈 값 혹은 infinity로 나타나는 현상 수정
	* Analytics > 전송 지표
		* 그리드에 데이터가 있다가 없어지면 No Data로 갱신되지 않는 버그 수정
		* 필터 이름이 짧을 때 버튼 정렬이 세로로 나오는 현상 수정
