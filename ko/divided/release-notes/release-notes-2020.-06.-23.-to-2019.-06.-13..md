---
source: release-notes.md
section: "2020. 06. 23.-to-2019. 06. 13."
order: 2
created_date: 2026-04-03
---

### 2020. 06. 23.

#### 기능 추가
* [SDK] 2.11.0
	* 결제 API 추가: 상품 ID로 결제 요청, 추가 정보(UserPayload) 입력해 결제 완료 시 확인할 수 있음

#### 기능 개선/변경
* [Console] 
	* 구매(IAP) > 상품: 스토어 아이템 ID에 여러 개의 Gamebase 상품을 등록해 관리할 수 있도록 개선

### 2020. 06. 09.

#### 기능 개선/변경
* [Console] 
	* 멤버 > 회원:  **탈퇴 이력 조회** 화면에 탈퇴 유예 상태(탈퇴 유예, 탈퇴 취소, 즉시 탈퇴) 추가 표시
* [SDK] 2.10.1
	* (iOS) 사용자 푸시 설정 초기화 시 언어 코드가 설정되어 있지 않으면 디바이스 언어로 설정되도록 변경

#### 버그 수정
* [Console] 
	* 쿠폰 > 쿠폰 발급: 쿠폰 통계 다운로드 시 SMS로 발송한 내역이 다운로드되지 않는 문제 수정

* [SDK] 2.10.1
	* (Unity) iOS Plugin에서 ViewController가 설정되지 않아 로그인 호출 시 실패하는 문제 수정
	* (JavaScript) 초기화 시 StoreCode를 입력하지 않으면 오류가 발생하는 문제 수정

### 2020. 05. 26.

#### 기능 추가
* [Console] 
	* 쿠폰 > 쿠폰 발급: 발송 통계 기능, 쿠폰 발송 내역 다운로드 기능 추가
* [SDK] 2.10.0
	* (공통) 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
		* ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트도 확인 가능

#### 기능 개선/변경
* [Console] 
	* 전체: 공통 디자인 가이드에 맞도록 버튼/태그 UI 수정
* [SDK] 2.10.0 
	* (Unity) StandaloneWebviewAdapter 내부의 CefWebview 버전 업데이트: v2.0.4
		* WebviewIndex 검증 로직을 개선
		* Webview 생성 시, 간헐적으로 NullReferenceException이 발생하는 오류를 개선
	* (Unity) GamebaseErrorCode에 소켓 연결에 관한 에러 코드 추가: SOCKET_CONNECTION_TIMEOUT, SOCKET_CONNECTION_FAIL

### 2020. 05. 12.

#### 기능 추가
* [SDK] 2.9.0
	* (Unreal) SDK 신규 배포
	
#### 기능 개선/변경
* [Console] 
	* 앱 > 앱: 탈퇴 유예 기간을 변경한 사용자의 토스트 계정을 저장하도록 개선
	* 멤버 > 회원: 매핑 이력 조회 시 정보가 제대로 보이지 않는 문제 수정
	* 구매(IAP) > 스토어: 테스트, 구) 원스토어는 신규 등록이 되지 않도록 수정

#### 버그 수정
* [SDK] 2.9.1
	* (Andoird) 매핑 이후 지표 레벨이 null이 되어 결제 지표에 정상적으로 반영되지 않는 오류 수정
	* (iOS) unreal 엔진에서 빌드 하면, warning을 빌드 오류로 판정해서 빌드가 안되는 부분을 수정

### 2020. 04. 29.

#### 버그 수정
* [SDK] 2.9.1 
	* (Unity) Initialize 이후 콘솔에서 클라이언트의 서비스 상태를 변경하면 오류가 발생하는 문제를 수정
		* 이슈 발생 버전: v2.8.0 이상	
		* 이슈가 있는 플랫폼: Standalone, WebGL, Editor
		
### 2020. 04. 28.

#### 기능 추가
* 탈퇴 유예 기능
	* [SDK] 2.9.0
		* (공통) API 추가: 탈퇴 유예 신청, 탈퇴 유예 신청 취소, 탈퇴 유예 상태에서 즉시 탈퇴, 유저의 탈퇴 유예 여부 확인
	* [Console]
		* 앱 > 앱: 탈퇴 유예 기간 설정할 수 있도록 기능 추가
		
#### 기능 개선/변경
* [SDK] 2.9.0
	* (공통) TOAST SDK 업데이트: Android(v0.21.0), iOS(v0.23.0), Unity(0.20.1)
	* (공통) PAYCO Login SDK 업데이트: Android(v1.5.0), iOS(v1.4.0)
* [Console]
	* 전체 메뉴: 콘솔 버튼, 태그 디자인 수정
	* 운영 > 점검, 운영 > 공지, 푸시: 다국어 자동 번역 기능 지원
	* 멤버 > 회원: 탈퇴 유예 유저의 회원 조회 시 유예 만료 기간을 추가로 표시

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
	
### 2020. 03. 24.

#### 기능 추가
* [Console] 
	* 신규 메뉴 오픈: Analytics > 이용자 지표 > Frequency 7
		* DAU의 일주일간 방문수와 비율 정보를 제공합니다. 게임몰입도, 충성도 등을 한 눈에 파악할 수 있습니다.
	* 쿠폰 > 쿠폰 발급: 쿠폰 문자 발송 기능 추가
* [SDK] 2.8.0
	* (공통) 결제 및 상품 정보에 상품 타입 및 지역 가격 등의 정보를 추가
	* (Unity) StandaloneWebviewAdapter 내부의 CefWebview가 v2.0.1 버전으로 업데이트
		* PopupType이 PASS_INFO일 경우, 팝업을 띄우지 않고 팝업 정보를 전달하는 기능을 추가
 	* (Javascript) 한게임 채널링 지원: 한게임 IdP 인증, 한코인 결제 추가


#### 기능 개선/변경
* [Console] 
	* 앱 > 전송 지표 세팅: 미리 등록한 메타 필터만 전송 지표에 사용할 수 있도록 제한
		* 메타필터 개수 제한하여 그 이상 전송하는 경우 지표가 노출되지 않으니 주의해 주세요.: 레벨(5,000개), 월드/서버/채널(100개), 직업/클래스(100개)
* [SDK] 2.8.0 
	* (공통) 콘솔에 등록되지 않은 앱 버전으로 초기화 실패할 때 스토어로 이동할 수 있는 팝업이 추가로 노출하도록 개선
	* (Android) 로그인 직후 결제 관련 API를 호출할 때 초기화 타이밍 문제로 실패가 발생할 수 있는 코드를 수정

#### 버그 수정
* [Console] 
	* 매출 지표 > 결제 금액
		* 차트 툴 팁에 통화가 원(KRW)으로 고정되어 노출되어 앱에서 설정한 통화로 보이도록 수정
		* 월별 조회시 2월 지표가 노출안되는 이슈 수정
		
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

### 2020. 02. 25.

#### 기능 추가
* [Console] 
	* 쿠폰 > 쿠폰 발급: 발급한 쿠폰을 설정한 스토어에서만 사용할 수 있도록 기능 추가
	
#### 기능 개선/변경
* [SDK] 2.7.1
	* (Common) Guest로 Login 후 GetAuthProviderUserID 호출하면 값을 반환하도록 수정
* [Console]
	* 앱 > 앱: 동일한 클라이언트 버전 삭제 이후 재등록 시 알림 로직 추가
	* 구매(IAP) > Item: 등록 시 구독 상품 등록을 위한 등록 필드값 추가(App Store - Shared secret,Google store - Domain authentication File Names)

#### 버그 수정
* [Console]
	* Analytics > 실시간 모니터링 > 실시간 지표: 간헐적으로 푸시 발송 후 ccu 항목에 빈 값 혹은 infinity로 나타나는 현상 수정
	* Analytics > 전송 지표
		* 그리드에 데이터가 있다가 없어지면 No Data로 갱신되지 않는 버그 수정
		* 필터 이름이 짧을 때 버튼 정렬이 세로로 나오는 현상 수정

### 2020. 02. 11.

#### 기능 추가
* [Console] 
	* Analytics > 이용자 지표 > Life Cycle 메뉴 신규 오픈 프로젝트 생성부터 이용자 지표의 흐름을 그래프로 한눈에 파악할 수 있도록 기능 제공
	* 관리 > 권한: 위클리 리포트 수신 권한 항목 추가
		* 실제 '위클리 리포트' 메일은 3월부터 전송될 예정입니다.

#### 기능 개선/변경
* [서버 API] 탈퇴 API 호출 시 regUser 길이에 대한 유효성 검사(validation) 추가
* [Console] 
	* Analytics: Grid, Chart에 일본어 폰트 적용
	* 구매: 오류 발생 시 나타나는 팝업 메시지를 사용자가 직관적으로 알 수 있게 개선

#### 버그 수정
* [Console]
	* Analytics: 일본어로 언어 변경 시 통화가 '엔(JPY)'으로 표시되던 것을 '원(KRW)'으로 표시되도록 수정

### 2020. 01. 21.

#### 기능 추가
* [SDK] 2.7.0
	* (Unity) NaverCafePLUG 지원

#### 버그 수정
* [SDK] 2.7.0
	* (Android) 서버 응답(response)에서 traceError 필수 파라미터가 없더라도 크래시가 발생하지 않도록 수정
	* (Android) Firebase 설정이 누락되어 있을 때 예외가 발생하지 않도록 수정
	* (Unity) Web Login 시, gamebase://dismiss 스킴 처리 추가
	* (Unity) 릴리스 빌드 시, 간헐적으로 Webview가 노출되지 않는 문제 수정	
* [Console]
	* Analytics: 유저 세션 만료 시 로그인 페이지로 리디렉트되지 않는 현상 수정

### 2020. 01. 14.

#### 기능 추가
* [서버 API] 사용자 탈퇴 API 추가

#### 기능 개선/변경
* [SDK] 2.6.3
	* (Unity) Standalone Webview 개선: CefWebview 업데이트	
	* (Unity) 로그인 이후 오류가 발생하여 누락된 .dll 파일 추가
		* ToastCommon.dll, vcruntime140.dll

#### 버그 수정
* [SDK] 2.6.3
	* (Unity) Login(CredentialInfo) API 호출 시 오류가 발생하여 수정
	
### 2019. 12. 24.

#### 기능 추가
* 쿠폰 > 쿠폰 발급: 키워드 쿠폰 기능 추가

#### 기능 개선/변경
* [Console]
	* 구매 > 결제 정보 조회: 추가 정보 칼럼 추가
* [SDK] 2.6.2
	* (공통) TOAST SDK 업데이트: Android(0.19.4), iOS(0.20.1), Unity(0.18.0)
	* (iOS) Naver SDK 버전 업데이트(4.1.0)
	
### 2019. 12. 10.

#### 기능 추가
* 앱 > 앱: 점검 중 QA 테스트 단말기 등록시 IP 로도 등록할 수 있는 기능 추가	

#### 버그 수정
* [Console]
	* 의미에 맞지 않는 일본어 문구 수정
* [SDK] 2.6.1
	* (Android)Gamebase.initialize() 호출 전에 Gamebase.login() 을 호출할 때 크래시가 발생하는 문제 수정
	* (Android)TOAST Analytics User Data 를 java 주소 값으로 잘못 전송하는 문제 수정
	* (Android)IAP 상품을 활성화 시키지 않은 경우 발생하는 크래시 수정
	* (iOS)AddMapping(강제, Forcibly) 사용 시, 매핑이 되지 않는 문제 수정
	* (iOS)Unity Plugin으로 PushConfiguration의 displayLanguageCode를 설정하지 않을 경우, NSNull 객체에 의하여 크래시가 발생하는 문제를 수정
	
### 2019. 11. 26.

#### 버그 수정
* [Console]
	* 쿠폰 > 쿠폰발급: 세션 만료 후 쿠폰 다운로드 시 비정상적인 파일로 다운로드 되던 문제 수정
	* Analytics > 실시간 모니터링 > 대시보드: 어제 데이터 0으로 노출되는 현상 수정
	* TOAST상품(IAP, Push, AppGuard 등) 관련 메뉴 접근 시 상품이 비활성화 된 경우 비활성화 페이지가 정상 노출되지 않던 문제 수정	

### 2019. 11. 20.

#### 버그 수정
* [SDK] 2.6.1
	* (Unity)iOS Plugin 파일이 Package에 누락되어 iOS 빌드 시 에러가 발생하여 해당 파일을 추가: 'toast_sdk_wrap.m'
	* (Unity)UnityEditor에서 Standalone 이외의 플랫폼으로 실행시 Store Code가 Empty로 입력되어 초기화에 실패하는 오류 수정
	* (Unity)Initialize API 내부 zone type 처리 부분에서의 오류로 NullReferenceException 발생하던 오류 수정

### 2019. 11. 13.

#### 버그 수정
* GamebaseSettingTool
	* Gamebase v2.6.0 업데이트 시, 파일이 정상적으로 변경되지 않는 오류 수정


### 2019. 11. 12.

```
Gamebase SDK 2.6.0 미만 버전에서 2.6.0으로 업그레이드 하는 경우
반드시 Upgrade Guide문서에 설명된 변경 사항을 반영해 주시기 바랍니다. 
가이드 위치: Game > Gamebase > Upgrade Guide
```

#### 기능 추가
* 쿠폰 서비스 신규 오픈: 쿠폰을 대량으로 생성하고 관리하는 기능
	* [Console] Coupon 메뉴 신규 오픈
	* [Server API] 쿠폰 확인 및 소비 API 추가
* 자동 결제 어뷰징 기능 추가
	* [Console] 구매(IAP) > 결제 어뷰징 모니터링 메뉴 신규 오픈
		* 결제 어뷰징 자동 제재 설정 기능
		* 결제 어뷰징 조건 검색 후 수동 이용 정지 가능
* Google 구독 결제 기능 추가
	* [SDK] 2.6.0 Android
* [SDK] 2.6.0
	* (공통) 데이터를 Log&Crash 에 전송하여 각종 분석에 이용할 수 있도록 TOAST Logger 추가
	* (iOS) Sign In with Apple 인증 추가
	* (Android) Gamebase Android SDK 가 Bintray 를 통해 배포되므로 gradle 설정만으로 Gamebase 를 사용할 수 있음

#### 기능 개선/변경
* [SDK] 2.6.0
	* (Unity) 로그인시 LaunchingStatus를 갱신하는 로직에 오류가 있어 수정
	* (Unity) Debug Log를 전송하는 기능을 Gamebase 콘솔에서 설정할 경우 Client에서 로그 전송을 무한 반복하는 오류 수정
* [Console]
	* 앱 > 앱: 서버 주소를 서비스 상태별(테스트, 심사중, 서비스)로 입력 받을 수 있도록 변경
	* 구매(IAP) > 결제 정보: 검색 조건 선택하여 검색할 수 있도록 UI 변경

### 2019. 10. 29.

#### 기능 개선/변경
* [Console]
	* Analytics: 파이 차트 툴팁 변경
	* Analytics > 실시간 모니터링: Push 발송 대상 추가 작업

### 2019. 10. 15.

#### 기능 개선/변경
* [SDK] 2.5.2
	* (iOS) UIWebView를 WKWebView로 교체
* Sample App
	* Gamebase SDK 업데이트(v2.4.0)
	* Smart Downloader 적용(v1.5.8), Leaderboard 적용
	* 기능 추가: 게임리소스 다운로드, Leaderboard, TAA 지표 연동, 단말기 이전 기능, 강제 매핑 기능
	* 개선/변경: ServerPush 리스너 추가, Observer 점검 여부 감지 추가
	* 게임 리뉴얼
		
#### 버그 수정
* [Console]	
	* 관리 > 권한: 권한 수정이 정상적으로 되지 않는 문제 수정
	* 모바일
		* Datepicker 선택 시 키보드가 활성화되는 현상 수정
		* Analytics: ARPPU 항목에 NRU 값이 노출되는 현상 수정
		
### 2019. 09. 24.

#### 기능 개선/변경
* [Console]
	* 앱 > 클라이언트: Web 클라이언트 등록 시에도 스토어를 선택하여 등록할 수 있도록 UI 수정
		
#### 버그 수정
* [Console]	
	* 관리 > 권한: 권한 수정이 정상적으로 되지 않는 문제 수정
	* 모바일
		* Datepicker 선택시 키보드가 활성화 되는 현상 수정
		* Analytics: ARPPU항목에 NRU 값이 노출되던 현상 수정
	
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
	
### 2019. 08. 27.

#### 기능 추가
* [SDK] 2.5.0
	* Console에서 입력한 CS URL을 웹뷰로 오픈하는 API 제공
	
#### 기능 개선/변경
* [Console]
	* Analytics: 차트 성능 개선

#### 버그 수정
* [SDK] Setting Tool 1.4.3
	* Script 파일의 위치를 Editor 폴더 아래로 이동하여 빌드 오류를 해결
	* Mac OS에서 Multilanguage에 Language 파일의 전체 경로를 지정하면 동작하지 않던 문제 수정
	
### 2019. 08. 02.

#### 버그 수정
* [SDK] Setting Tool 1.4.3
	* Script 파일의 위치를 Editor 폴더 아래로 이동하여 빌드 오류를 해결
	* Mac OS에서 Multilanguage에 Language 파일의 전체 경로를 지정하면 동작하지 않던 문제 수정

### 2019. 07. 23.

#### 기능 추가
* [Console]
	* 멤버 > 다운로드 신규 메뉴 오픈: 가입일, 마지막 로그인 시간 기준으로 게임 유저 목록을 조회하고 파일로 다운로드할 수 있음

#### 기능 개선/변경
* [Console] 모바일
	* 점검, 푸시 등록과 수정 가능
* [SDK] 2.4.4
	* (공통) 회원 오류 코드 포맷 변경
	* (Unity) GamebaseServerPushType에 키 추가(TRANSFER_KICKOUT)
* Setting Tool
	* 폴더 구조 변경: `기존 SettingTool을 완전히 삭제한 후 재설치해야 합니다.`
	* 다국어 지원 추가
	
#### 버그 수정
* [Console]
	* Analytics > 이용자 지표: 차트 X축 날짜 겹치는 문제 수정

#### 버그 수정
* [Console]
	* Analytics > 이용자 지표: 차트 x축 날짜 겹치는 이슈 수정
	
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

### 2019. 07. 01.

#### 버그 수정
* [Console]
	* 관리 > 알람: Webhook 설정 후 알람 설정값 수정에 실패하는 현상 수정

### 2019. 06. 27.

#### 버그수정
* [Console]
	* 이용정지: 이용정지 대량등록을 위한 파일 업로드 실패 현상 수정
* [SDK] Setting Tool 1.4.1
	* GamebaseSettingTool 실행시 기존 설정 정보를 가져오지 못하는 오류가 발생하여 수정

### 2019. 06. 25.

#### 기능 추가
* 전송 지표 기능 추가
    * [Console]Analytics > 전송지표: Level, Channel, Class별 지표 확인 메뉴 오픈
		* 실시간 현황
		* 레벨별 현황
		* 월드/서버/채널별 현황
		* 클래스/직업별 현황
		* 레벨업
		* 아이템 판매 현황
		* 아이템 판매 TOP 50

#### 기능 개선/변경
* [SDK] 2.4.2
	* (공통)LaunchingInfo에 JSON string 형식의 TOAST Launching 정보를 추가
	* (iOS)LINE SDK 업데이트(v5.0.1)
		* LINE Adpater의 최소 지원 OS 버전이 iOS 10으로 변경 
		* LINE 앱을 통한 로그인 기능 추가

#### 버그수정
* [SDK] 2.4.2
	* (공통)Analytics 버그 수정: 로그아웃, 탈퇴, 계정 이전 시 저장된 지표 데이터를 초기화 하도록 수정
	* (iOS)네트워크 연결 문제로 간헐적으로 크래시가 발생하던 현상 수정

### 2019. 06. 13.

#### 버그수정
* [SDK] 2.4.1
	* (iOS)Analytics 지표 전송 시 일부 파라미터가 누락 되어 지표가 제대로 출력되지 않는 버그 수정
