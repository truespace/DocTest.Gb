## Game > Gamebase > iOS SDK 사용 가이드 > 결제

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
