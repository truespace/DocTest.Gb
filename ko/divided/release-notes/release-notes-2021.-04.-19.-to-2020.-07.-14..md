---
source: release-notes.md
section: "2021. 04. 19.-to-2020. 07. 14."
order: 1
created_date: 2026-04-03
---

## Game > Gamebase > 릴리스 노트

### 2021. 04. 19.

#### 버그 수정
* [SDK] 2.21.1
	* (Android) Hangame 로그인을 PAYCO로 진행하다 취소하면 크래시가 발생하는 문제 수정
	* (iOS) bitcode를 지원 가능하도록 설정해도 설정값이 반영되지 않는 문제 수정

### 2021. 04. 13.

#### 기능 추가
* [SDK] 2.21.0
	* (공통) Hangame 일본 인증 추가

#### 기능 개선/변경
* [Console] 
	* 회원 > 멤버: 푸시 토큰 조회 시 광고성 수신 동의, 야간 광고 수신 여부가 ture인 경우 수신한 일자도 함께 표시되도록 개선 
	* 구매(IAP) > 결제 정보: 추가 정보 표시되는 팝업 창에 문자열이 줄 바꿈 되어 보이도록 개선
	* 구매(IAP) > 결제 어뷰징 모니터링
		* 1시간으로 고정되어 있던 자동 제재 감지 기간을 사용자가 입력(1시간~48시간)할 수 있도록 개선
		* AND 조건만 설정 가능하던 건수, 금액 자동 제재 조건 입력을 OR 조건도 입력할 수 있도록 개선
* [SDK] 2.21.0	
	* (Android) 외부 SDK 업데이트: Facebook Android SDK(6.5.1), Line Android SDK(5.4.0)
	* (iOS) bitcode 지원이 가능하도록 변경
	* (iOS) showWebView 호출 시, 닫기 버튼을 가장 먼저 화면에 표시되도록 수정
	
#### 버그 수정
* [SDK] 2.21.0
	* (Android) Proguard를 적용한 빌드에서 결제 API 호출 시 크래시가 발생하는 오류 수정

### 2021. 03. 30.

#### 기능 개선/변경
* [SDK] 2.20.2
	* (Android) Google Play 스토어의 Android 11 단말기에서의 결제 오류가 해결된 Billing Client 3.0.3 버전으로 업데이트

### 2021. 03. 23.

#### 기능 개선/변경
* [Console] 회원 > 다운로드: 하나의 파일에 저장되는 데이터 수 개선(5만 -> 50만)
* [SDK] 2.20.2
	* (iOS) Facebook iOS SDK 업데이트 (9.1.0)
	* (iOS) 특정 경우에 GamebaseAuthFacebookAdapter에서 openURL delegate가 호출되지 않았던 이슈 수정

### 2021. 03. 09.

#### 기능 추가
* [Console] 앱 > 약관: GDPR 약관 추가
* [Server API] IdP ID로 Gamebase user ID를 획득하는 API 추가 

#### 기능 개선/변경
* [SDK] 2.20.1
	* (iOS) iOS 14에 대응하여 IDFA 획득 로직 수정: info.plist에 NSUserTrackingUsageDescription 필드 추가

### 2021. 02. 23.

#### 기능 추가
* [Console] 
	* 운영 > 킥아웃: 클라이언트 버전별로 킥아웃이 가능하도록 기능 추가
	* 구매(IAP) > 스토어: Google Play 스토어의 일회성 영수증 검증 단계를 설정할 수 있도록 기능 추가
	
#### 버그 수정
* [SDK] 2.20.1
	* (Android) push-fcm 모듈 초기화 중 크래시가 발생할 수 있는 로직을 수정

### 2021. 02. 15.

#### 버그 수정
* [Console] 구매(IAP) > 결제 내역: 파일 다운로드 시 상품 이름이 잘못 노출되는 오류 수정

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

### 2021. 01. 26.

```
푸시 > 푸시(구) 콘솔 메뉴 기능이 제외되었습니다.
```

#### 기능 추가
* [Console] 
	* 이용 정지 > 앱가드: 조건 차단 기능 추가
	* 구매(IAP) > 결제 어뷰징 모니터링: Apple App Store 추가 
* [SDK] 2.19.0
	* (Unreal) SDK 배포: 2.16.0 ~ 2.19.0 누적된 내역 반영
		* [Android 설정 툴](https://docs.toast.com/ko/Game/Gamebase/ko/unreal-started/#android-settings) 제공: Gamebase_Android_UPL.xml 파일을 수정하는 대신 설정 툴을 사용바랍니다.
		* 고객센터 기능 추가	
		* 인증 추가: Hangame, Weibo
		* Galaxy 스토어 추가
		* 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription
		* Android 설정 툴 제공
		* Unreal 4.26 지원

#### 기능 개선/변경
* [Console]
	* 관리 > 권한: 매출 접근 권한 제거 [관련 공지 바로 가기](https://www.toast.com/kr/support/notice/detail/2101)
* [SDK] 2.19.1
	* (iOS) Weibo IdPAdapter 구조 변경	

### 2021. 01. 12.

```
Gamebase의 XCode 최소 지원 버전이 10에서 11로 변경되었습니다. 
```

#### 기능 추가
* [Console] 푸시 신규 메뉴 추가
	* 통계: 푸시 발송, 수신, 토큰 등록 등의 푸시 통계를 확인
	* 이벤트 키: 푸시 발송 통계에 사용하는 이벤트 키를 관리
	* 인증서: 푸시 발송에 사용하는 인증서를 관리
	* 설정: 푸시 관련된 설정값을 관리
	
### 2020. 12. 29.

#### 기능 추가
* [SDK] 2.19.0
	* (공통) Weibo 인증 추가
	* (Android) Sign In with Apple 인증 추가
	
#### 기능 개선/변경
* [Console]
	* 앱 > 앱: 서버 주소 관리에 베타 서비스 서버 추가 
	* 앱 > 클라이언트: 클라이언트 상태에 베타 서비스 추가, 클라이언트 추가 정보 등록할 수 있도록 메모 기능 추가 
	* 구매(IAP) > 상품: 검색 조건 추가 - 사용여부
	* 구매(IAP) > 결제 정보: 결제 내역에 스토어 테스트 결제건 표시
	* 구매(IAP) > 판매 현황 메뉴 종료: Analytics > 매출 지표와 기능이 통합되었습니다.
	* Analytics > 이용 환경 > 설치 URL 메뉴 종료
* [SDK] 2.19.0
	* (공통) 론칭 상태 코드 추가: 베타 서비스(205)

#### 버그 수정
* [SDK] 2.19.0
    * (Unity) WebSocket에서 재시도 시 OutOfMemoryException이 발생하는 문제 수정
* [SDK] 2.19.1
	* (Android) Weibo 로그인 시도 후 다른 IdP로 로그인 시 크래시가 발생하는 문제 수정
	
### 2020. 12. 15.

#### 기능 추가
* Gamebase 고객센터 페이지 오픈 시 게임에서 정의한 extra data 전달: SDK 2.18.2
	* [Console] 고객센터 > 고객 문의: 고객 문의 상세 조회 화면에서 추가로 등록한 extra data 확인 가능
* [SDK] 2.18.2
	* (공통) 개발사 자체 고객센터 오픈 시 additionalURL 필드 추가
	* (공통) 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription

#### 기능 개선/변경
* [Console]
	* Analytics: 필터 검색 후 날짜 변경하여도 선택한 검색 조건이 유지되도록 개선
	* Push > 푸시: Tencent Push 제거
	* 구매(IAP) > 결제 정보: 환불 상태에서 영수증 검증 버튼 노출되지 않도록 변경
* [SDK] 2.18.2
    * (공통) TOAST SDK 업데이트: [Android(0.24.2)](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-android/#0242-20201124), [iOS(0.27.1)](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-ios/#0271-20201124), [Unity(0.21.3)](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-unity/#0213-20201124)
	* (Android) 암호화 로직 보안 경고 해결을 위한 외부 SDK 업데이트: Payco Login SDK(1.5.3), Hangame ID SDK(1.3.2)
	* (Android) Tencent Push 모듈 제거
	* (Android) Gamebase Android SDK 2.6.0에서 deprecated된 함수 제거
		* GamebaseConfiguration.Builder.setFCMSenderId()
		* GamebaseConfiguration.Builder.setTencentAccessKey()
		* GamebaseConfiguration.Builder.setTencentAccessId()
	* (iOS) showWebView: 잘못된 URL을 전달했을 경우 에러 반환, 전달받은 URL은 인코딩하지 않고 그대로 사용
	* (iOS) 대소문자 상관없이 커스텀 스킴이 동작하도록 변경
	* (Unity) GamebaseRequest.GamebaseConfiguration 클래스의 필드 deprecated: zoneType, fcmSenderId

#### 버그 수정
* [Console]
	* 구매(IAP) > 아이템: 파일로 아이템을 대량 등록하면 중복으로 등록되는 문제 수정
* [SDK] 2.18.2
    * (Android) 5.0~6.0 OS 단말기에서 웹뷰 커스텀 스킴이 동작하지 않는 문제 수정

### 2020. 12. 2.

#### 기능 추가
* [Console] 
	* Gamebase 권한 세분화 기능 추가: 24개
	* Analytics > 그룹 지표: 프로젝트별 신규 가입자, 결제 금액 비교 그래프 추가    
	* 멤버 > 회원: 하단에 고객센터 문의 내역 조회 탭 추가
	* 쿠폰 > 쿠폰 발급: 발급된 쿠폰에 추가로 쿠폰을 발급할 수 있도록 쿠폰 추가 발급 기능 추가(1회 10만 개)

#### 기능 개선/변경
* [Console]
    * Analytics > 실시간 모니터링: 전날 지표 대비 데이터가 상승, 하락했을 때 표시 색상 변경
		* 상승: 파란색->빨간색, 하락: 빨간색->파란색
	* Analytics > 매출 지표 > 결제 금액: 국가별로만 비교할 수 있던 매출 데이터를 스토어별, IdP 별로 데이터를 확인할 수 있도록 추가
	* 운영 > 공지: 자세히 보기 링크에 고객센터 연결할 수 있도록 설정 추가
	* 고객센터 > 고객 문의: 답변 발송 설정에 자동 번역 기능 추가
	* 쿠폰 > 쿠폰 발급: 쿠폰 최초 발급 수량을 최대 5만 개에서 최대 100만 개로 증가

#### 버그 수정
* [Console]
    * 구매(IAP) > 결제 정보: 조회한 데이터가 많은 경우 파일을 다운로드하지 못하는 문제 수정

### 2020. 11. 10.

#### 기능 추가
* Galaxy 스토어 추가: SDK 2.18.0

#### 기능 개선/변경
* [SDK] 2.18.0
    * (Android) TOAST SDK 업데이트: [Android(0.24.1)](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-android/#0240-20201027)-GooglePlay Billing Library v.3.0.1 적용
    * (Android) WebView SSL 보안 경고 대응 처리 추가
    * (iOS) iOS 13 이상부터 제공되는 SceneDelegate 대응 API 추가

#### 버그 수정
* [SDK] 2.18.1
    * (Android) 2.18.0 에서 Google 결제 후 크래시가 발생하는 문제 수정

### 2020. 10. 27.

#### 기능 추가
* Unreal SDK 기능 추가: SDK 2.15.0
    * 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
        * ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트 확인 가능
    * API 추가
    	* 상품 ID로 결제 요청하고 추가 정보(UserPayload)를 입력해 결제 완료 시 확인 가능한 결제 API 추가
    	* 이미지 공지 표시: showImageNotices
    	* Push 토큰 정보 확인: queryTokenInfo
    * 푸시 토큰 등록 시 NotificationOption 설정으로 앱이 포그라운드(foreground) 상태에서도 푸시 알림을 받을 수 있도록 기능 추가
    * WebViewConfiguration contentMode 설정 추가
    
#### 기능 개선/변경
* [SDK] 2.17.1
    * (iOS) 특정 지표 전송 시 오류 메시지를 추가하여 전송: 푸시 등록에 실패 시, 게임 지표 전송 시
    * (Unity) Unity 2017.2.5 지원
* [SDK] 2.15.0
    * (Unreal) TOAST SDK 업데이트: Android(0.23.0), iOS(0.26.0), Unity(0.21.0)    

#### 버그 수정
* [Console]
    * Analytics > 이용자 지표: 주간, 월간 평균 CCU 계산 로직 수정하여 비정상적으로 노출되는 문제 수정
    * Push > 푸시: 제목을 입력하지 않고 제목 글자색을 검은색이 아닌 색으로 설정하면 제목에 'null'이 표시되는 문제 수정
	* 쿠폰 > 쿠폰 발급: 발급된 쿠폰이 5만 개 이상인 경우 파일이 다운로드되지 않는 문제 수정
* [SDK] 2.17.1
    * (Unity) 이미지 공지와 웹뷰를 차례로 호출하면 뒤에 호출한 API가 동작하지 않는 오류 수정	
* [SDK] 2.15.0    
    * (Unreal) 결제 모듈에 ProGuard 선언이 누락된 오류 수정


### 2020. 10. 13.

```
한게임 인증 사용을 원하는 경우 고객센터로 미리 연락주세요.
```

#### 기능 추가
* Hangame IdP 인증 추가: SDK 2.17.0

#### 기능 개선/변경
* [SDK] 2.17.0
    * (공통) 고객 센터 첨부 이미지 클릭 시 다운로드 지원
    * (공통) TOAST SDK 업데이트: Android(0.23.2), Unity(0.21.2)
    * (iOS) TCGBMember.regDate, TCGBMember.lastLoginDate의 타입을 long long으로 변경
    * (iOS) 웹뷰에서 URL 및 타이틀 변경 시 타이틀을 재출력할 수 있도록 로직 변경

#### 버그 수정
* [SDK] 2.17.0
    * (iOS) PAYCO 인증: lastLoggedInProvider 로그인 후 로그아웃 호출 시 로그아웃 콜백이 오지 않는 문제 수정
* [SDK] 2.17.1
    * (Android) 2.17.0에서 ImageNotice API 호출 시 kotlinx-coroutine 모듈에서 크래시가 발생하는 문제 수정
	
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

### 2020. 09. 16.

#### 기능 개선/변경
* [SDK] 2.15.1
    * (iOS) TOAST SDK 업데이트: iOS(0.27.0)
	* iOS 14 beta 변경 사항을 대응한 IAP SDK 신규 버전이 적용되었습니다. [TOAST SDK Release Notes](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-ios/#0270-20200911)

### 2020. 09. 15.

#### 기능 추가
* [SDK] 2.15.0
    * (JavaScript) 한게임 포인트 결제 API에 GamebaseProductId 추가

#### 버그 수정
* [Console]
    * 구매(IAP) > 결제 정보: 영수증 검증 표시가 제대로 되지 않던 문제 수정

### 2020. 08. 25.

```
Gamebase SDK 2.15.0 버전에서 Google Billing Client 모듈이 업데이트 되었습니다.

'gamebase-adapter-purchase-google'을 사용한다면 Gamebase SDK 2.15.0 미만 버전에서 2.15.0 이상으로 업그레이드하는 경우 
반드시 이전 버전의 'Game Client Version'을 '업데이트 필수'로 설정해야 합니다.

아이템을 구매하다 오류가 발생하면 재처리를 수행하게 되는데 
여러 개의 단말기에서 서로 다른 Billing Client 버전이 적용된 상태에서는 재처리 수행 중에 문제가 생길 수 있기 때문입니다.
```

#### 기능 추가
* [SDK] 2.15.0
    * (공통) 푸시 토큰 등록시 NotificationOption 설정으로 앱이 포그라운드(foreground) 상태에서도 푸시 알림을 받을 수 있도록 기능 추가
    * (공통) 푸시 API 추가: Push 토큰 정보 확인(Gamebase.Push.queryTokenInfo API)
* [SDK] 2.9.1
    * (Unreal) Unreal 4.22 ~ 4.25 지원
    * (Unreal) PLCrashReporter 이슈 지원: [가이드](http://docs.toast.com/ko/Game/Gamebase/ko/unreal-started/#ios-settings)

#### 기능 개선/변경
* [Console]
    * 푸시 > 푸시: 홍보성 푸시 알림 발송 시 발신자 연락처, 수신 철회 동의 방법을 입력하지 않아도 발송이 가능하도록 수정
* [SDK] 2.15.0
    * (공통) TOAST SDK 업데이트: Android(0.23.0), iOS(0.26.0), Unity(0.21.0)
    * (iOS) 결제 payload의 null check 로직 추가
* [SDK] 2.9.1
    * (Unreal) iOS Plugin 내부 Gamebase SDK for iOS 버전 업데이트(2.9.1)
    * (Unreal) UObject 레퍼런싱 처리가 누락된 부분을 수정

#### 버그 수정
* [Console]
    * 푸시 > 푸시: 푸시 알림 반복 발송 시 시간 정보가 입력된 타임존과 상관없이 무조건 UTC+9로 계산되어 전송되던 문제 수정
    
### 2020. 08. 19.

#### 버그 수정
* [Console]
    * Analytics 전체 메뉴: 엑셀 다운로드가 되지 않는 문제 수정

### 2020. 08. 11.

#### 기능 개선/변경
* [Console]
    * Analytics > 이용자 지표 > Retention: % 외에 수치를 추가로 표시
* [SDK] 2.14.0
    * (iOS) PAYCO IdP의 상수값 제거: PAYCO 문자열로 인한 애플 검수가 리젝되는 경우가 발생하여 제거
    * (iOS, Unity) TCGBWebViewConfiguration에 contentMode 설정 추가
* [Server]
    * 쿠폰 소진 API의 오류 코드 추가: 쿠폰 코드에 영문, 숫자 이외의 값을 입력한 경우(Error Code:-4000205)

### 2020. 07. 28.

#### 기능 추가
* [Console]
    * Analytics: WAU(Weekly Active User), MAU(Monthly Active User) 지표 추가
* [SDK] 2.13.0
    * (Unity) Standalone: 이미지 공지 표시 API 추가    

#### 기능 개선/변경
* [Console]
    * 앱 > 앱: iOS 12 이하에서 Sign In With Apple 인증을 하기 위한 정보를 추가 입력할 수 있도록 수정
* [SDK] 2.13.0
    * (Android) 이미지 공지의 팝업 이미지 비율 계산 로직 수정
    * (iOS) Sign In With Apple 인증: iOS 12 이하 지원

#### 버그 수정
* [Console]
    * 운영 > 이미지 공지: 복사 기능 및 대상 국가 선택 후 전체 국가로 수정 시 반영되지 않는 오류 수정
* [SDK] 2.13.0
    * (Android) 웹뷰 종료 시 종료 콜백에서 ANDROID_ACTIVITY_DESTROYED(31) 오류가 반환되는 문제 수정
    * (Android) 결제 모듈에 ProGuard 선언이 누락된 오류 수정
    
### 2020. 07. 14.

#### 기능 추가
* 이미지 공지: 표시 기간과 우선순위에 따라 게임 내 이미지 팝업 표시
    * [Console] 운영 > 이미지 공지: 메뉴 추가
    * [SDK] 2.12.0: 이미지 공지 표시 API 추가

#### 기능 개선/변경
* [Console] 
    * 구매(IAP) > 상품: 아이템 번호로 상품 조회 가능하도록 추가
    * 멤버 > 회원: 탈퇴 유예 상태의 유저를 정상 상태로 변경할 수 있도록 개선
    * 멤버 > 다운로드: 로그인 로그 이력에 deveiceKey, IdP 코드 항목 추가
* [SDK] 2.12.0
    * (iOS) Facebook SDK 업데이트(7.1.1)
    * (iOS) configuartion에 설정된 storeCode(default=AS)로 Gamebase 초기화 시도
    * (iOS) 콘텐츠를 로딩할 수 없는 웹뷰 출력 시 **닫기** 버튼이 없어 닫을 수 없는 문제 수정
    * (Unity) TOAST Unity SDK 업데이트(0.20.1.1)
