---
source: ios-push.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, XCode, Push, Notification"
section: Settings
order: 1
---

## Game > Gamebase > iOS SDK 사용 가이드 > 푸시

> <font color="red">[주의]</font><br/>
>
> Unreal, Unity 등 3rd party 푸시 플러그인 또는 모듈을 사용할 경우, Gamebase 푸시 기능에 영향을 줄 수 있습니다.
>

### Settings

#### APNS JWT 인증 정보 얻기

여기에서는 푸시 알림 전송에 필요한 APNS JWT 인증 정보를 얻는 과정을 설명합니다.

* [Notification > Push > Console Guide > APNS JWT 인증 정보 얻기](https://docs.toast.com/en/Notification/Push/en/console-guide/#get-authentication-information-for-apns-jwt) 가이드를 참고하여 ANPS JWT 등록에 필요한 필수 인증 정보를 얻습니다.

#### Gamebase Console 등록
* **Gamebase > Push > Certificate**에서 **APNS JWT**에 위에서 얻은 정보를 입력합니다.

#### Notification Service Extension 구현
* 수신 지표 수집, 알림음 설정 등을 위해서는 [NHN Cloud Push 가이드](https://docs.toast.com/ko/TOAST/ko/toast-sdk/push-ios/#notification-service-extension)를 참고하여 애플리케이션에 **Notification Service Extension**을 구현해야 합니다.


#### Xcode Project 설정
* **Targets > Capabilities > Push Notifications **항목을 **ON**으로 설정합니다.
* 자동으로 생성된 .entitlements 파일을 열어서, **APS Environment** 키의 값을 알맞은 값으로 설정합니다.
    * **development**: Sandbox APNS
    * **production**:  APNS

#### Import Header File
푸시 API를 구현하고자 하는 ViewController에 다음의 헤더 파일을 가져옵니다.

```objectivec
#import <Gamebase/Gamebase.h>
```
