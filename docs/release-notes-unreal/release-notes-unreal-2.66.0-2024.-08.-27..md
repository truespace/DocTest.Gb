---
source: release-notes-unreal.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, v2.66.0, 기능개선, 변경, 제거"
section: "2.66.0 (2024. 08. 27.)"
order: 22
---

### 2.66.0 (2024. 08. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* API 사용 방식이 변경되었습니다.
    * `IModuleInterface`를 상속 받은 **IGamebase**에서 제공하던 API를 `UGameInstanceSubsystem`을 상속 받은 **UGamebaseSubsytem**에서 제공하도록 변경했습니다.
    * **UGamebaseSubsytem**은 GameInstance의 서브시스템이므로 GameInstance 생명 주기를 따르며 SDK API 호출 시 사용하는 GameInstance를 통해 해당 서브시스템을 찾아서 API를 사용해야 합니다.
* GamebaseInterface 모듈이 제거되었습니다. Gamebase 플러그인 사용 시 GamebaseInterface 모듈을 삭제 후 사용하시길 바랍니다.
* (Windows) GameInstance가 여러 개인 환경에서 사용할 수 있습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.66.2](../../release-notes-android.md#2662-2024-08-27)
* [Gamebase iOS SDK 2.66.2](../../release-notes-ios.md#2662-2024-08-27)
