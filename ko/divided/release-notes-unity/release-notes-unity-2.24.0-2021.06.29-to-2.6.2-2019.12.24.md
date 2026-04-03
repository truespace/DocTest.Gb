---
source: release-notes-unity.md
section: "2.24.0 (2021.06.29)-to-2.6.2 (2019.12.24)"
order: 4
created_date: 2026-04-03
---

### 2.24.0 (2021.06.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.24.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 내부 론칭 URL 변경

### 2.23.0 (2021.06.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.23.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Unity SDK(0.22.1)
* Unity 2020.2 이후 버전에서 발생하는 Warning 제거
* Standalone과 Unity Editor에서 초기화 속도 개선

#### 버그 수정
* 약관 동의를 했음에도 ShowTermsView API 호출하면 PushConfiguration 결과가 null이 아닌 문제 수정

### 2.22.0 (2021.05.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.22.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Unity SDK(0.22.0)

### 2.21.0 (2021.04.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.21.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 인증 추가: 일본 한게임(Hange)

### 2.20.0 (2021.02.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.20.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 공통 약관 기능 추가
    * 약관 웹뷰를 여는 API 추가
    * 약관 리스트 및 유저별 동의 여부를 조회하는 API 추가
    * 유저별 약관 동의 여부를 Gamebase 서버에 저장하는 API 추가

#### 기능 개선/변경
* 고객 센터 타입이 TOAST 조직 상품(Online Contact)인 경우 로그인을 하지 않아도 고객 센터가 표시되도록 변경
* Warning 로그 제거
* Standalone 웹뷰에 CEF 2.1.2 업데이트
    * URL의 길이가 2,048보다 길 경우 크래시가 발생하는 이슈 수정
    * Unity 2019에서 빌드 시 라이브러리 경로가 변경되어 PostProcessBuild 개선
    * string 초기화를 하지 않아 간헐적으로 발생하는 오류 수정
    * Gamebase 웹뷰 사용 중 웹뷰가 신(scene)을 이동한 이후에는 다시 열리지 않는 버그 수정

### 2.19.0 (2020.12.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.19.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.19.0
    * (공통) Weibo 인증 추가
    
#### 기능 개선/변경
* [SDK] 2.19.0
    * (공통) 론칭 상태 코드 추가: 베타 서비스(205)

#### 버그 수정
* [SDK] 2.19.0
    * (Unity) WebSocket에서 재시도 시 OutOfMemoryException이 발생하는 문제 수정
    
### 2.18.2 (2020.12.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.2/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.18.2
    * (공통) 개발사 자체 고객 센터 오픈 시 additionalURL 필드 추가
    * (공통) 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription

#### 기능 개선/변경
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
* [SDK] 2.18.2
    * (Android) 5.0~6.0 OS 단말기에서 웹뷰 커스텀 스킴이 동작하지 않는 문제 수정

### 2.18.0 (2020.11.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.0/GamebaseSDK-Unity.zip)

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

### 2.17.1 (2020.10.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.17.1/GamebaseSDK-Unity.zip)

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
    * (Unity) Unity 2017.2.5 지원

#### 버그 수정
* [SDK] 2.17.1
    * (Unity) 이미지 공지와 웹뷰를 차례로 호출하면 뒤에 호출한 API가 동작하지 않는 오류 수정    

### 2.17.0 (2020.10.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.17.0/GamebaseSDK-Unity.zip)

```
한게임 인증 사용을 원하는 경우 고객 센터로 미리 연락주세요.
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
    
### 2.16.0 (2020.09.22)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.16.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 고객 센터 기능 추가
    * [SDK] 2.16.0
    * (공통) API 추가(Gamebase.Contact.requestContactURL): 고객 센터 URL 반환
    * (공통) 고객 센터 API 에 userName 을 설정할 수 있도록 ContactConfiguration 파라미터 추가 
      
### 2.15.0 (2020.08.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.15.0/GamebaseSDK-Unity.zip)

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

#### 기능 개선/변경
* [SDK] 2.15.0
    * (공통) TOAST SDK 업데이트: Android(0.23.0), iOS(0.26.0), Unity(0.21.0)
    * (iOS) 결제 payload의 null check 로직 추가

### 2.14.0 (2020.08.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.14.0/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 2.14.0
    * (iOS) PAYCO IdP의 상수값 제거: PAYCO 문자열로 인한 앱 스토어 심사에서 거절되는 경우가 발생하여 제거
    * (iOS, Unity) TCGBWebViewConfiguration에 contentMode 설정 추가

### 2.13.0 (2020.07.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.13.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.13.0
    * (Unity) Standalone: 이미지 공지 표시 API 추가    

#### 기능 개선/변경
* [SDK] 2.13.0
    * (Android) 이미지 공지의 팝업 창 이미지 비율 계산 로직 수정
    * (iOS) Sign In With Apple 인증: iOS 12 이하 지원

#### 버그 수정
* [SDK] 2.13.0
    * (Android) 웹뷰 종료 시 종료 콜백에서 ANDROID_ACTIVITY_DESTROYED(31) 오류가 반환되는 문제 수정
    * (Android) 결제 모듈에 ProGuard 선언이 누락된 오류 수정
    
### 2.12.0 (2020.07.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.12.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 이미지 공지: 표시 기간과 우선순위에 따라 게임 내 이미지 팝업 창 표시
    * [SDK] 2.12.0: 이미지 공지 표시 API 추가

#### 기능 개선/변경
* [SDK] 2.12.0
    * (iOS) Facebook SDK 업데이트(7.1.1)
    * (iOS) configuartion에 설정된 storeCode(default=AS)로 Gamebase 초기화 시도
    * (iOS) 콘텐츠를 로딩할 수 없는 웹뷰 출력 시 **닫기** 버튼이 없어 닫을 수 없는 문제 수정
    * (Unity) TOAST Unity SDK 업데이트(0.20.1.1)
    
### 2.11.0 (2020.06.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.11.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.11.0
    * 결제 API 추가: 상품 ID로 결제 요청, 추가 정보(UserPayload) 입력해 결제 완료 시 확인할 수 있음

### 2.10.1 (2020.06.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.10.1/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 2.10.1
    * (iOS) 사용자 푸시 설정 초기화 시 언어 코드가 설정되어 있지 않으면 디바이스 언어로 설정되도록 변경

#### 버그 수정
* [SDK] 2.10.1
    * (Unity) iOS Plugin에서 ViewController가 설정되지 않아 로그인 호출 시 실패하는 문제 수정

### 2.10.0 (2020.05.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.10.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.10.0
    * (공통) 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
        * ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트도 확인 가능

#### 기능 개선/변경
* [SDK] 2.10.0 
    * (Unity) StandaloneWebviewAdapter 내부의 CefWebview 버전 업데이트: v2.0.4
        * WebviewIndex 검증 로직을 개선
        * 웹뷰 생성 시, 간헐적으로 NullReferenceException이 발생하는 오류를 개선
    * (Unity) GamebaseErrorCode에 소켓 연결에 관한 에러 코드 추가: SOCKET_CONNECTION_TIMEOUT, SOCKET_CONNECTION_FAIL

#### 버그 수정
* [SDK] 2.9.1
    * (Andoird) 매핑 이후 지표 레벨이 null이 되어 결제 지표에 정상적으로 반영되지 않는 오류 수정
    * (iOS) unreal 엔진에서 빌드 하면, warning을 빌드 오류로 판정해서 빌드가 안되는 부분을 수정

### 2.9.1 (2020.04.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.9.1/GamebaseSDK-Unity.zip)

#### 버그 수정
* [SDK] 2.9.1 
    * (Unity) Initialize 이후 콘솔에서 클라이언트의 서비스 상태를 변경하면 오류가 발생하는 문제를 수정
        * 이슈 발생 버전: v2.8.0 이상    
        * 이슈가 있는 플랫폼: Standalone, WebGL, Editor
        
### 2.9.0 (2020.04.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.9.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 탈퇴 유예 기능
    * [SDK] 2.9.0
        * (공통) API 추가: 탈퇴 유예 신청, 탈퇴 유예 신청 취소, 탈퇴 유예 상태에서 즉시 탈퇴, 유저의 탈퇴 유예 여부 확인
        
#### 기능 개선/변경
* [SDK] 2.9.0
    * (공통) TOAST SDK 업데이트: Android(v0.21.0), iOS(v0.23.0), Unity(0.20.1)
    * (공통) PAYCO Login SDK 업데이트: Android(v1.5.0), iOS(v1.4.0)

### 2.8.1 (2020.04.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.1/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 2.8.1 
    * (공통) Analytics 전송 결과 확인을 위한 내부 지표 추가
    
### 2.8.0 (2020.03.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.8.0
    * (공통) 결제 및 상품 정보에 상품 타입 및 지역 가격 등의 정보를 추가
    * (Unity) StandaloneWebviewAdapter 내부의 CefWebview가 v2.0.1 버전으로 업데이트
        * PopupType이 PASS_INFO일 경우, 팝업 창을 띄우지 않고 팝업 창 정보를 전달하는 기능을 추가

#### 기능 개선/변경
* [SDK] 2.8.0 
    * (공통) 콘솔에 등록되지 않은 앱 버전으로 초기화 실패할 때 스토어로 이동할 수 있는 팝업 창이 추가로 노출하도록 개선
    * (Android) 로그인 직후 결제 관련 API를 호출할 때 초기화 타이밍 문제로 실패가 발생할 수 있는 코드를 수정
    
### 2.7.2 (2020.03.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.2/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 2.7.2 
      * (Unity) FacebookAdapter 개선 
            * v7.9.4~v7.18.1 버전까지 호환성 테스트
            * Null 예외 처리 
      * (Unity) StandaloneWebviewAdapter 개선 
            * 웹 페이지를 텍스처(texture)로 내보내기 추가
            * 멀티 웹뷰 지원 
            * 쿠키 삭제 옵션 추가 
            * 텍스처(texture) 크기 조절 지원 
        * 스크롤바 표시/숨기기 지원 
            * 페이지 로드 완료 알림 
            * 투명 배경 지원 
      * (Unity) 에디터에서 Android/iOS 플랫폼을 선택하고 Initialize API를 호출하면 오류가 발생하는 문제 해결

### 2.7.0 (2020.01.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.7.0
    * (Unity) NaverCafePLUG 지원

#### 버그 수정
* [SDK] 2.7.0
    * (Android) 서버 응답(response)에서 traceError 필수 파라미터가 없더라도 크래시가 발생하지 않도록 수정
    * (Android) Firebase 설정이 누락되어 있을 때 예외가 발생하지 않도록 수정
    * (Unity) Web Login 시, gamebase://dismiss 스킴 처리 추가
    * (Unity) 릴리스 빌드 시, 간헐적으로 웹뷰가 노출되지 않는 문제 수정    

### 2.6.3 (2020.01.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.3/GamebaseSDK-Unity.zip)

#### 기능 개선/변경
* [SDK] 2.6.3
    * (Unity) Standalone 웹뷰 개선: CefWebview 업데이트    
    * (Unity) 로그인 이후 오류가 발생하여 누락된 .dll 파일 추가
        * ToastCommon.dll, vcruntime140.dll

#### 버그 수정
* [SDK] 2.6.3
    * (Unity) Login(CredentialInfo) API 호출 시 오류가 발생하여 수정
    
### 2.6.2 (2019.12.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.2/GamebaseSDK-Unity.zip)

#### 기능 추가
* 쿠폰 > 쿠폰 발급: 키워드 쿠폰 기능 추가

#### 기능 개선/변경
* [SDK] 2.6.2
    * (공통) TOAST SDK 업데이트: Android(0.19.4), iOS(0.20.1), Unity(0.18.0)
    * (iOS) NAVER SDK 버전 업데이트(4.1.0)
