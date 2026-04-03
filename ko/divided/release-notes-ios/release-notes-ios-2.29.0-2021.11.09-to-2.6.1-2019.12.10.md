---
source: release-notes-ios.md
section: "2.29.0 (2021.11.09)-to-2.6.1 (2019.12.10)"
order: 3
created_date: 2026-04-03
---

### 2.29.0 (2021.11.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.29.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Xcode 최소 지원 버전이 12에서 13으로 변경되었습니다. 
* 외부 SDK 업데이트: TOAST iOS SDK(0.29.1), ToastGamebaseIAP SDK(0.12.1)
* 콘솔에 등록한 점검 및 공지 자세히 보기의 URL을 인코딩하지 않고 화면에 출력하도록 변경되었습니다.

#### 버그 수정
* TCGBPushMessage.extras를 json 파싱할 때 에러가 발생하는 버그를 수정하였습니다.

### 2.28.0 (2021.09.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.28.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Kakaogame 인증 추가
* '결제 어뷰징 자동 해제' 기능이 추가되었습니다.
    * [Game > Gamebase > iOS SDK 사용 가이드 > 인증 > GraceBan](../../ios-authentication.md#graceban)
    * 결제 어뷰징 자동 해제 기능은 결제 어뷰징 자동 제재로 이용 정지가 되어야 할 사용자가 '이용 정지 유예 상태' 후 이용 정지가 되도록 합니다.
    * '이용 정지 유예 상태'일 경우, 설정한 기간 내에 이용 정지 해제 조건을 모두 만족하면 정상적으로 플레이할 수 있습니다.
    * 기간 내에 조건을 충족하지 못하면 이용 정지가 됩니다.
* 결제 어뷰징 자동 해제 기능을 사용하는 게임은 로그인 후 항상 TCGBAuthToken.tcgbMember.graceBanInfo 값을 확인하고, null이 아닌 유효한 TCGBGraceBanInfo 객체를 반환한다면 해당 유저에게 이용 정지 해제 조건, 기간 등을 안내해야 합니다.
    * 이용 정지 유예 상태인 유저의 게임 내 접근 제어는 게임에서 처리해야 합니다.

#### 기능 개선/변경
* PAYCO iOS SDK 업데이트 (1.5.2)

### 2.27.1 (2021.09.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.27.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* PAYCO iOS SDK 업데이트 (1.5.1)
    * 인증 플로우 및 UI 개선
* Hangame iOS SDK 업데이트 (1.6.1)
    * 본인인증에서 에러 상황 발생 시 콜백 호출 안되는 이슈 수정
    * iOS 15 beta에서 내비게이션바가 깨지는 이슈 수정

#### 버그 수정
* 이미 약관에 동의하여 약관 UI가 표시되지 않을 경우, PushConfiguration가 nil로 반환되지 않는 이슈를 수정했습니다.

### 2.27.0 (2021.08.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.27.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* PAYCO iOS SDK 업데이트 (1.5.0)
    * PAYCO 앱이 없을 때 이전에는 수동 로그인만 가능했으나, Safari에 로그인돼 있다면 간편 로그인 기능을 사용할 수 있도록 변경되었습니다.

#### 버그 수정
* Unity에서 이미지 공지가 출력되지 않는 이슈를 수정했습니다.
    * Gamebase iOS SDK 2.27.0 미만을 사용할 경우 Unity에서 이미지 공지가 출력되지 않을 수 있습니다.
    * 이미지 공지를 사용할 경우에는 Gamebase iOS SDK 2.27.0 이상을 사용하시기 바랍니다.


### 2.26.0 (2021.08.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.26.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Display Language 기능이 개선되었습니다.
    * 지금까지는 언어셋을 추가하기 위해 Gamebase.bundle 안에 있는 파일을 직접 수정해야 했습니다.
        * 이제 Xcode 프로젝트의 Copy Bundle Resources에 localizedstring.json 파일을 추가하면 되도록 개선하였습니다.
    * Display Language 언어셋에 중국어 간체(zh-CN), 중국어 번체(zh-TW), 태국어(th)가 추가되었습니다.
    * 기본 언어코드가 **en** 이었으나, Gamebase 콘솔에서 설정한 기본언어가 반영되도록 개선하였습니다.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > App > 언어 설정](../../oper-app.md#language-settings)
* showTermsView API 호출 후 생성할 수 있는 PushConfiguration 객체의 생성 기준이 다음과 같이 변경되었습니다.
    * 변경 전
        * 약관 항목 중에 **Push 수신** 항목이 존재하는 경우에만 nil이 아닌 유효한 PushConfiguration이 반환되었습니다.
        * 유저가 주간, 야간 홍보성 Push 수신에 모두 거부한 경우 PushConfiguration.pushEnabled는 false로 생성되었습니다.
    * 변경 후
        * 약관 UI가 표시되었다면 항상 nil이 아닌 유효한 PushConfiguration이 반환됩니다.
        * showTermsView가 반환하는 PushConfiguration 객체의 pushEnabled 값은 항상 true입니다.
    * 변경되지 않고 동일한 점
        * 이미 약관에 동의하여 약관 UI가 표시되지 않았다면 PushConfiguration은 nil로 반환됩니다.

#### 버그 수정
* Push 언어 설정은 별다른 보조 처리가 없이 단말기의 언어코드를 그대로 적용되어, Push 콘솔에서 전송한 메시지의 언어코드가 일치하지 않는 문제를 수정하였습니다.

### 2.25.0 (2021.07.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.25.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 월 결제 한도 기능 추가
    * 월 결제 한도를 넘는 경우 **PURCHASE_LIMIT_EXCEEDED(4007)** 에러가 발생합니다.

#### 기능 개선/변경
* Push 항목이 존재하는 약관에서 PushConfiguration 객체 보장
    * 약관 UI 에서 Push 수신 동의를 하지 않을 경우 Gamebase.Terms.showTermsView API 호출 결과로 생성되는 TCGBPushConfiguration 이 null이었으나, 약관에 Push 항목이 존재한다면 TCGBPushConfiguration 객체가 항상 반환되도록 변경되었습니다.
    * Push 수신 거부 시 TCGBPushConfiguration 객체는 (푸시 동의 여부 = false, 광고성 푸시 동의 여부 = false, 야간 광고성 푸시 동의 여부 = false)로 생성됩니다.
    * 약관에 Push 항목이 존재하지 않는다면 TCGBPushConfiguration 객체는 null입니다.
* 외부 SDK 업데이트: TOAST iOS SDK(0.29.0)
* Sign In with Apple 의 ASAuthorizationErrorUnknown 에러가 발생했을 경우, TCGB_ERROR_AUTH_EXTERNAL_LIBRARY_ERROR 에러를 반환하도록 변경

#### 버그 수정
* registerPush 를 통해 등록한 TCGBPushConfiguration 값과 TCGBPushTokenInfo 값이 달라지게 되는 버그 수정

### 2.24.0 (2021.06.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.24.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 내부 론칭 URL 변경

#### 버그 수정
* 약관 상세 보기 후 약관 새 창이 닫히지 않는 버그 수정

### 2.23.0 (2021.06.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.23.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST iOS SDK(0.28.0), ToastGamebaseIAP SDK(0.12.0)

### 2.22.0 (2021.05.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.22.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST iOS SDK(0.27.2), Hangame iOS SDK(1.6.0)

### 2.21.2 (2021.04.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.21.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Facebook iOS SDK 업데이트 (9.2.0)

#### 버그 수정
* 아카이브 빌드 시 bitcode 관련 오류가 발생하는 이슈 수정

### 2.21.1 (2021.04.19)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.21.1/GamebaseSDK-iOS.zip)

#### 버그 수정
* bitcode를 지원 가능하도록 설정해도 설정값이 반영되지 않는 문제 수정

### 2.21.0 (2021.04.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.21.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* Hangame 일본 인증 추가 

#### 기능 개선/변경
* bitcode 지원이 가능하도록 변경
* showWebView 호출 시, 닫기 버튼을 가장 먼저 화면에 표시되도록 수정

### 2.20.2 (2021.03.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.20.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Facebook iOS SDK 업데이트 (9.1.0)
* 특정 경우에 GamebaseAuthFacebookAdapter에서 openURL delegate가 호출되지 않았던 이슈 수정

### 2.20.1 (2021.03.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.20.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* iOS 14에 대응하여 IDFA 획득 로직 수정: info.plist에 NSUserTrackingUsageDescription 필드 추가

### 2.20.0 (2021.02.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.20.0/GamebaseSDK-iOS.zip)

* 공통 약관 기능 추가
    * 약관 웹뷰를 여는 API 추가
    * 약관 리스트 및 유저별 동의 여부를 조회하는 API 추가
    * 유저별 약관 동의 여부를 Gamebase 서버에 저장하는 API 추가

#### 기능 개선/변경
* 고객 센터 타입이 TOAST 조직 상품(Online Contact)인 경우 로그인을 하지 않아도 고객 센터가 표시되도록 변경

### 2.19.1 (2021.01.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.19.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Weibo IdPAdapter 구조 변경

### 2021. 01. 12.

```
Gamebase의 XCode 최소 지원 버전이 10에서 11로 변경되었습니다. 
```
    
### 2.19.0 (2020.12.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.19.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* Weibo 인증 추가
    
#### 기능 개선/변경

* 론칭 상태 코드 추가: 베타 서비스(205)

### 2.18.2 (2020.12.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.2/GamebaseSDK-iOS.zip)

#### 기능 추가

* 개발사 자체 고객 센터 오픈 시 additionalURL 필드 추가
* 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription

#### 기능 개선/변경

* 외부 SDK 업데이트: TOAST iOS SDK(0.27.1)
* showWebView: 잘못된 URL을 전달했을 경우 에러 반환, 전달받은 URL은 인코딩하지 않고 그대로 사용
* 대소문자 상관없이 커스텀 스킴이 동작하도록 변경


### 2.18.0 (2020.11.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* iOS 13 이상부터 제공되는 SceneDelegate 대응 API 추가

### 2.17.1 (2020.10.27)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.17.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* 특정 지표 전송 시 오류 메시지를 추가하여 전송: 푸시 등록에 실패 시, 게임 지표 전송 시

### 2.17.0 (2020.10.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.17.0/GamebaseSDK-iOS.zip)

```
한게임 인증 사용을 원하는 경우 고객 센터로 미리 연락주세요.
```

#### 기능 추가

* Hangame IdP 인증 추가

#### 기능 개선/변경

* 고객 센터 첨부 이미지 클릭 시 다운로드 지원
* TCGBMember.regDate, TCGBMember.lastLoginDate의 타입을 long long으로 변경
* 웹뷰에서 URL 및 타이틀 변경 시 타이틀을 재출력할 수 있도록 로직 변경

#### 버그 수정

* PAYCO 인증: lastLoggedInProvider 로그인 후 로그아웃 호출 시 로그아웃 콜백이 오지 않는 문제 수정
    
### 2.16.0 (2020.09.22)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.16.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* 고객 센터 기능 추가
    * API 추가(Gamebase.Contact.requestContactURL): 고객 센터 URL 반환
    * 고객 센터 API 에 userName 을 설정할 수 있도록 ContactConfiguration 파라미터 추가 
        
### 2.15.1 (2020.09.16)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.15.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: TOAST iOS SDK(0.27.0)
* iOS 14 beta 변경 사항을 대응한 IAP SDK 신규 버전이 적용되었습니다. [TOAST SDK Release Notes](https://docs.toast.com/ko/TOAST/ko/toast-sdk/release-notes-ios/#0270-20200911)

### 2.15.0 (2020.08.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.15.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* 푸시 토큰 등록시 NotificationOption 설정으로 앱이 포그라운드(foreground) 상태에서도 푸시 알림을 받을 수 있도록 기능 추가
* 푸시 API 추가: Push 토큰 정보 확인(Gamebase.Push.queryTokenInfo API)

#### 기능 개선/변경

* 외부 SDK 업데이트: TOAST iOS SDK(0.26.0)
* 결제 payload의 null check 로직 추가
    
### 2.14.0 (2020.08.11)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.14.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* PAYCO IdP의 상수값 제거: PAYCO 문자열로 인한 앱 스토어 심사에서 거절되는 경우가 발생하여 제거
* TCGBWebViewConfiguration에 contentMode 설정 추가

### 2.13.0 (2020.07.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.13.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* Sign In With Apple 인증: iOS 12 이하 지원
    
### 2.12.0 (2020.07.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.12.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 이미지 공지: 표시 기간과 우선순위에 따라 게임 내 이미지 팝업 창 표시
    * 이미지 공지 표시 API 추가

#### 기능 개선/변경
* Facebook SDK 업데이트(7.1.1)
* configuartion에 설정된 storeCode(default=AS)로 Gamebase 초기화 시도
* 콘텐츠를 로딩할 수 없는 웹뷰 출력 시 **닫기** 버튼이 없어 닫을 수 없는 문제 수정
    
### 2.11.0 (2020.06.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.11.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* 결제 API 추가: 상품 ID로 결제 요청, 추가 정보(UserPayload) 입력해 결제 완료 시 확인할 수 있음

### 2.10.1 (2020.06.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.10.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* 사용자 푸시 설정 초기화 시 언어 코드가 설정되어 있지 않으면 디바이스 언어로 설정되도록 변경

### 2.10.0 (2020.05.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.10.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
    * ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트도 확인 가능


### 2.9.1 (2020.05.12)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.9.1/GamebaseSDK-iOS.zip)

#### 버그 수정

* Unreal 엔진에서 빌드 하면, warning을 빌드 오류로 판정해서 빌드가 안되는 부분을 수정
        
### 2.9.0 (2020.04.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.9.0/GamebaseSDK-iOS.zip)

#### 기능 추가
* 탈퇴 유예 기능
    * API 추가: 탈퇴 유예 신청, 탈퇴 유예 신청 취소, 탈퇴 유예 상태에서 즉시 탈퇴, 유저의 탈퇴 유예 여부 확인
        
#### 기능 개선/변경

* 외부 SDK 업데이트: TOAST iOS SDK(0.24.0)
* PAYCO iOS SDK 업데이트 (1.4.0)

### 2.8.1 (2020.04.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Analytics 전송 결과 확인을 위한 내부 지표 추가
    
### 2.8.0 (2020.03.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.0/GamebaseSDK-iOS.zip)

#### 기능 추가

* 결제 및 상품 정보에 상품 타입 및 지역 가격 등의 정보를 추가

#### 기능 개선/변경

* 콘솔에 등록되지 않은 앱 버전으로 초기화 실패할 때 스토어로 이동할 수 있는 팝업 창이 추가로 노출하도록 개선

### 2.7.1 (2020.02.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.1/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Guest로 Login 후 GetAuthProviderUserID 호출하면 값을 반환하도록 수정

### 2.6.2 (2019.12.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* 외부 SDK 업데이트: TOAST iOS SDK(0.20.1)
* NAVER iOS SDK 업데이트 (4.1.0)
    
### 2.6.1 (2019.12.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.1/GamebaseSDK-iOS.zip)
    
#### 버그 수정
* AddMapping(강제, Forcibly) 사용 시, 매핑이 되지 않는 문제 수정
* Unity Plugin으로 PushConfiguration의 displayLanguageCode를 설정하지 않을 경우, NSNull 객체에 의하여 크래시가 발생하는 문제를 수정
