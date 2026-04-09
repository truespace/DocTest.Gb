---
source: release-notes-console.md
section: "2020. 03. 10."
order: 84
split: true
created_date_time: 20260408_184906
keyword: Console, Purchase, Analytics, Android, iOS, Release Notes
---

### 2020. 03. 10.

#### 기능 추가

- [Console]
	- 앱  >  앱: Analytics 매출 지표를 표시할 때 테스트 결제 포함 여부 설정  
	  - '테스트 결제 제외'로 설정하면 Analytics 매출 지표에서 테스트 결제는 모두 제외하고 보여줍니다.
		- 구매(IAP): 구매(IAP) 메뉴 최초 접근 시 결제 지표 통화 코드 설정
	- 최초 한 번만 설정 가능하며 Analytics 매출 지표에는 설정된 통화 코드로 지표가 표시됩니다.
		- 모바일 콘솔(NHN 게임플랫폼 앱 포함)에 '데스크톱 보기' 기능 추가

#### 기능 개선/변경

- [Console]
  - 앱  >  설치 URL: URL 입력 가능한 스킴(scheme) 추가 적용
  - 기존: 공통('http://', 'https://'), Android('market://')
  - 추가: iOS('itms://', 'itmss://', 'itms-apps://'), Android('intent://')

#### 버그 수정
- [Console]
  - Analytics: 통화 코드가 코인성인 경우 매출 지표가 '0'으로 표시되는 문제 해결
