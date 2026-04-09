---
source: release-notes.md
section: "2021. 02. 09."
order: 8
split: true
created_date_time: 20260408_184906
keyword: Login, WebView, Initialize, Terms, Contact, Unity, Unreal, Release Notes, 2.20.0
---

### 2021. 02. 09.

#### 기능 추가
* 공통약관 기능 추가
	* [Console] 신규 메뉴 오픈: 앱 > 약관, 앱 > 약관 배포
	* [SDK] 2.20.0
		* (공통) 약관 WebView를 여는 API 추가
		* (공통) 약관 리스트 및 유저별 동의 여부를 조회하는 API 추가
		* (공통) 유저별 약관 동의 여부를 Gamebase 서버에 저장하는 API 추가

#### 기능 개선/변경
* [Console] 앱 > 클라이언트: 클라이언트 버전을 스토어별로 구분하여 표시하도록 화면 개선
* [SDK] 2.20.0
	* (공통) 고객센터 타입이 TOAST 조직 상품(Online Contact)인 경우 로그인을 하지 않아도 고객센터가 표시되도록 변경
	* (Unity) Warning 로그 제거
	* (Unity) Standalone WebView에 CEF 2.1.2 업데이트
		* URL의 길이가 2,048보다 길 경우 크래시가 발생하는 이슈 수정
		* Unity 2019에서 빌드 시 라이브러리 경로가 변경되어 PostProcessBuild 개선
		* string 초기화를 하지 않아 간헐적으로 발생하는 오류 수정
		* Gamebase WebView 사용 중 WebView가 신(scene)을 이동한 이후에는 다시 열리지 않는 버그 수정

#### 버그 수정
* [SDK] 2.20.0
	* (JavaScript) 콘솔에 고객센터 정보를 입력하지 않으면 초기화 시 오류가 발생하여 수정
* [SDK] 2.19.1
	* (Unreal) Unity 빌드 중 제외되는 파일이 생길 때 발생하는 컴파일 오류 수정
