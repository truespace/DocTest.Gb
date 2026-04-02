## Game > Gamebase > 릴리스 노트 > iOS

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
