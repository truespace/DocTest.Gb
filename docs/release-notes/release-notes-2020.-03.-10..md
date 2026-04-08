---
source: release-notes.md
section: "2020. 03. 10."
order: 33
split: true
created_date_time: 20260408_191848
keyword: Purchase, WebView, Alert, Analytics, Initialize, Android, iOS, Release Notes
---

### 2020. 03. 10.

#### 기능 추가

- [Console] 
	- 앱  >  앱: Analytics 매출 지표를 표시할 때 테스트 결제 포함 여부 설정  
    		- '테스트 결제 제외'로 설정하면 Analytics 매출 지표에서 테스트 결제는 모두 제외하고 보여줍니다. 
		- 구매(IAP): 구매(IAP) 메뉴 최초 접근 시 결제 지표 통화 코드 설정 
	- 최초 한 번만 설정 가능하며 Analytics 매출 지표에는 설정된 통화 코드로 지표가 표시됩니다.  
  	- 모바일 콘솔(TOAST 앱 포함)에 '데스크톱 보기' 기능 추가

#### 기능 개선/변경

- [Console] 
  	- 앱  >  설치 URL: URL 입력 가능한 스킴(scheme) 추가 적용 
    		- 기존: 공통('http://', 'https://'), Android('market://') 
    		- 추가: iOS('itms://', 'itmss://', 'itms-apps://'), Android('intent://')
- [SDK] 2.7.2 
  	- (Unity) FacebookAdapter 개선 
    		- v7.9.4~v7.18.1 버전까지 호환성 테스트
    		- Null 예외 처리 
  	- (Unity) StandaloneWebviewAdapter 개선 
    		- 웹 페이지를 텍스처(texture)로 내보내기 추가
    		- 멀티 웹뷰 지원 
    		- 쿠키 삭제 옵션 추가 
    		- 텍스처(texture) 크기 조절 지원 
		- 스크롤바 표시/숨기기 지원 
    		- 페이지 로드 완료 알림 
    		- 투명 배경 지원 
  	- (Unity) 에디터에서 Android/iOS 플랫폼을 선택하고 Initialize API를 호출하면 오류가 발생하는 문제 해결

#### 버그 수정
- [Console] 
  	- Analytics: 통화 코드가 코인성인 경우 매출 지표가 '0'으로 표시되는 문제 해결
