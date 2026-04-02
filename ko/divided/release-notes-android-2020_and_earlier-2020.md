## Game > Gamebase > 릴리스 노트 > Android

### 2.19.1 (2020.12.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.19.1/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.19.0
    * (공통) Weibo 인증 추가
    * (Android) Sign In with Apple 인증 추가
    
#### 기능 개선/변경
* [SDK] 2.19.0
    * (공통) 론칭 상태 코드 추가: 베타 서비스(205)

#### 버그 수정
* [SDK] 2.19.1
    * (Android) Weibo 로그인 시도 후 다른 IdP로 로그인 시 크래시가 발생하는 문제 수정
    
### 2.18.2 (2020.12.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.2/GamebaseSDK-Android.zip)

#### 기능 추가
* Gamebase 고객 센터 페이지 오픈 시 게임에서 정의한 extra data 전달: SDK 2.18.2
    * [Console] 고객 센터 > 고객 문의: 고객 문의 상세 조회 화면에서 추가로 등록한 extra data 확인 가능
* [SDK] 2.18.2
    * (공통) 개발사 자체 고객 센터 오픈 시 additionalURL 필드 추가
    * (공통) 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription

#### 기능 개선/변경
* [SDK] 2.18.2
    * (공통) TOAST SDK 업데이트: Android(0.24.2), iOS(0.27.1), Unity(0.21.3)
    * (Android) 암호화 로직 보안 경고 해결을 위한 외부 SDK 업데이트: PAYCO Login SDK(1.5.3), Hangame ID SDK(1.3.2)
    * (Android) Tencent Push 모듈 제거
    * (Android) Gamebase Android SDK 2.6.0에서 deprecated된 함수 제거
        * GamebaseConfiguration.Builder.setFCMSenderId()
        * GamebaseConfiguration.Builder.setTencentAccessKey()
        * GamebaseConfiguration.Builder.setTencentAccessId()

#### 버그 수정
* [SDK] 2.18.2
    * (Android) 5.0~6.0 OS 단말기에서 웹뷰 커스텀 스킴이 동작하지 않는 문제 수정

### 2.18.1 (2020.11.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.1/GamebaseSDK-Android.zip)

#### 기능 추가
* Galaxy 스토어 추가: SDK 2.18.0

#### 기능 개선/변경
* [SDK] 2.18.0
    * (Android) TOAST SDK 업데이트: Android(0.24.1) - GooglePlay Billing Library v.3.0.1 적용
    * (Android) WebView SSL 보안 경고 대응 처리 추가

#### 버그 수정
* [SDK] 2.18.1
    * (Android) 2.18.0 에서 Google 결제 후 크래시가 발생하는 문제 수정

### 2.17.1 (2020.10.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.17.1/GamebaseSDK-Android.zip)
```
한게임 인증 사용을 원하는 경우 고객 센터로 미리 연락주세요.
```

#### 기능 추가
* Hangame IdP 인증 추가: SDK 2.17.0

#### 기능 개선/변경
* [SDK] 2.17.0
    * (공통) 고객 센터 첨부 이미지 클릭 시 다운로드 지원
    * (공통) TOAST SDK 업데이트: Android(0.23.2), Unity(0.21.2)

#### 버그 수정
* [SDK] 2.17.1
    * (Android) 2.17.0에서 ImageNotice API 호출 시 kotlinx-coroutine 모듈에서 크래시가 발생하는 문제 수정
    
### 2.16.0 (2020.09.22)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.16.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 고객 센터 기능 추가
    * [SDK] 2.16.0
        * (공통) API 추가(Gamebase.Contact.requestContactURL): 고객 센터 URL 반환
        * (공통) 고객 센터 API 에 userName 을 설정할 수 있도록 ContactConfiguration 파라미터 추가 
        
### 2.15.0 (2020.08.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.15.0/GamebaseSDK-Android.zip)

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

### 2.13.0 (2020.07.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.13.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.13.0
    * (Android) 이미지 공지의 팝업 창 이미지 비율 계산 로직 수정

#### 버그 수정
* [SDK] 2.13.0
    * (Android) 웹뷰 종료 시 종료 콜백에서 ANDROID_ACTIVITY_DESTROYED(31) 오류가 반환되는 문제 수정
    * (Android) 결제 모듈에 ProGuard 선언이 누락된 오류 수정
    
### 2.12.0 (2020.07.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.12.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 이미지 공지: 표시 기간과 우선순위에 따라 게임 내 이미지 팝업 창 표시
    * [SDK] 2.12.0: 이미지 공지 표시 API 추가
    
### 2.11.0 (2020.06.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.11.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.11.0
    * 결제 API 추가: 상품 ID로 결제 요청, 추가 정보(UserPayload) 입력해 결제 완료 시 확인할 수 있음

### 2.10.0 (2020.05.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.10.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.10.0
    * (공통) 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
        * ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트도 확인 가능

### 2.9.1 (2020.05.12)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.9.1/GamebaseSDK-Android.zip)

#### 버그 수정
* [SDK] 2.9.1
    * (Android) 매핑 이후 지표 레벨이 null이 되어 결제 지표에 정상적으로 반영되지 않는 오류 수정

### 2.9.0 (2020.04.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.9.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 탈퇴 유예 기능
    * [SDK] 2.9.0
        * (공통) API 추가: 탈퇴 유예 신청, 탈퇴 유예 신청 취소, 탈퇴 유예 상태에서 즉시 탈퇴, 유저의 탈퇴 유예 여부 확인
        
#### 기능 개선/변경
* [SDK] 2.9.0
    * (공통) TOAST SDK 업데이트: Android(v0.21.0), iOS(v0.23.0), Unity(0.20.1)
    * (공통) PAYCO Login SDK 업데이트: Android(v1.5.0), iOS(v1.4.0)

### 2.8.1 (2020.04.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.8.1 
    * (공통) Analytics 전송 결과 확인을 위한 내부 지표 추가
    * (Android) 프로세스 재시작 이후 크래시가 발생할 수 있는 코드를 수정
    
### 2.8.0 (2020.03.24)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.8.0/GamebaseSDK-Android.zip)

#### 기능 추가
* [SDK] 2.8.0
    * (공통) 결제 및 상품 정보에 상품 타입 및 지역 가격 등의 정보를 추가

#### 기능 개선/변경
* [SDK] 2.8.0 
    * (공통) 콘솔에 등록되지 않은 앱 버전으로 초기화 실패할 때 스토어로 이동할 수 있는 팝업 창이 추가로 노출하도록 개선
    * (Android) 로그인 직후 결제 관련 API를 호출할 때 초기화 타이밍 문제로 실패가 발생할 수 있는 코드를 수정

### 2.7.2 (2020.03.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.7.2 
      * Gamebase 초기화중 ToastLogger 초기화 부분에서 크래시가 발생할 수 있는 코드를 수정
      * 서버 버전을 v1.2.1 로 업데이트 하였습니다.

### 2.7.1 (2020.02.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.1/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 2.7.1
    * (공통) Guest로 Login 후 GetAuthProviderUserID 호출하면 값을 반환하도록 수정

### 2.7.0 (2020.01.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.0/GamebaseSDK-Android.zip)

#### 버그 수정
* [SDK] 2.7.0
    * (Android) 서버 응답(response)에서 traceError 필수 파라미터가 없더라도 크래시가 발생하지 않도록 수정
    * (Android) Firebase 설정이 누락되어 있을 때 예외가 발생하지 않도록 수정
