---
source: unreal-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal SDK 사용 가이드, 결제, Settings"
section: Settings
order: 1
---

## Game > Gamebase > Unreal SDK 사용 가이드 > 결제

여기에서는 Unreal에서 인앱 결제 기능을 사용하기 위해 필요한 설정 방법을 알아보겠습니다.
Gamebase는 하나의 통합된 결제 API를 제공해 게임에서 손쉽게 많은 스토어의 인앱 결제를 연동할 수 있도록 돕습니다.

### Settings

Android나 iOS에서 인앱 결제 기능을 설정하는 방법은 다음 문서를 참고하시기 바랍니다.<br/>

* [Android Purchase Settings](aos-purchase#settings)
* [iOS Purchase Settings](ios-purchase#settings)
* [Windows Purchase Settings](unreal-started/#windows-settings)

#### Unreal Plugin 설정

> <font color="red">[주의]</font><br/>
>
> 외부 플러그인에서 결제 관련 처리가 있는 경우, Gamebase 결제 기능이 정상적으로 동작하지 않을 수 있습니다.

* Unreal에서 기본으로 활성화되어있는 Online SubSystem 플러그인을 비활성화 혹은 스토어 기능을 이용하지 못하도록 변경해야 합니다.
    * Online SubSystem GooglePlay 플러그인 사용 시 /Config/Android/AndroidEngine.ini 파일을 편집합니다.
            
            [OnlineSubsystemGooglePlay.Store]
            bSupportsInAppPurchasing=False
            bUseGooglePlayBillingApiV2=False
            
    * Online SubSystem iOS 플러그인 사용 시 /Config/IOS/IOSEngine.ini 파일을 편집합니다.
            
            [OnlineSubsystemIOS.Store]
            bSupportsInAppPurchasing=False
