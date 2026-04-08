---
source: ios-purchase.md
section: "Settings"
order: 1
split: true
created_date_time: 20260408_191848
keyword: iOS, Purchase, XCode, Unity, Unreal
---

## Game > Gamebase > iOS SDK 사용 가이드 > 결제

> <font color="red">[주의]</font><br/>
>
> Unreal, Unity 등 3rd party 결제 플러그인 또는 모듈을 사용할 경우, Gamebase 결제 기능에 영향을 줄 수 있습니다.
>

여기에서는 앱에서 인앱 결제 기능을 사용하기 위해 필요한 설정 방법을 알아보겠습니다.

Gamebase는 하나의 통합된 결제 API를 제공해 게임에서 손쉽게 많은 스토어의 인앱 결제를 연동할 수 있도록 돕습니다.

### Settings

#### Apple iTunes-Connect
1. 테스트용 앱 빌드 업로드
2. In-App Purchases 아이템 등록 및 승인
3. Sandbox Tester 계정 등록
* Detail Guide for iTunes-Connect: [Apple Guide](https://help.apple.com/itunes-connect/developer/#/devb57be10e7)

#### Gamebase Console 등록
다음은 Gamebase Console에서 설정해야 하는 내용입니다.

1. **Gamebase > Purchase(IAP) > 스토어**에서 이용할 스토어를 등록합니다.
    * 스토어: **App Store**를 선택합니다.
2. **Gamebase > Purchase(IAP) > 상품**에서 아이템을 등록합니다.
    * 상품 ID: 결제 요청 시 사용할 상품 ID를 입력합니다.
    * 상품 이름: 결제 시 표시할 상품 이름을 입력합니다.
    * 사용 여부: 아이템의 사용여부를 결정합니다.
    * 스토어: **App Store**를 선택합니다.
    * 스토어 아이템 ID: iTunes-Connect에 등록한 Product ID를 입력합니다.
3. 아이템을 설정했다면, **저장**을 누릅니다.

#### Xcode Project 설정
1. **Targets > Capabilities > In-App Purchase**를 **ON**으로 설정합니다.
2. **Targets > General > Identity**의 Bundle Identifier, Version, Build의 값을 알맞게 설정합니다.

#### Import Header File

구매 API를 구현하고자 하는 ViewController에 다음의 헤더 파일을 가져옵니다.

```objectivec
#import <Gamebase/Gamebase.h>
```
