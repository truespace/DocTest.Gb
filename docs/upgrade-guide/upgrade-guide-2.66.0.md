---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "Initialize, GetSubsystem, GetGameInstance"
section: 2.66.0
order: 16
---

## 2.66.0

### Unreal

* API 사용 방식이 변경되었습니다.
    * `IModuleInterface`를 상속 받은 **IGamebase**에서 제공하던 API를 `UGameInstanceSubsystem`을 상속 받은 **UGamebaseSubsytem**에서 제공하도록 변경했습니다.
    * **UGamebaseSubsytem**은 GameInstance의 서브시스템이므로 GameInstance 생명 주기를 따르며 SDK API 호출 시 사용하는 GameInstance를 통해 해당 서브시스템을 찾아서 API를 사용해야 합니다.
    * 언리얼 코딩 표준에 명명 규칙을 따르도록 변경되었습니다.

```cpp
if (UGamebaseSubsystem* GamebaseSubsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance()))
{
    GamebaseSubsystem->Initialize(...);
}
```

* **GamebaseInterace** 모듈이 제거되었으므로 Gamebase 사용 시 모듈 의존성에서 제거해야 합니다.

        PrivateDependencyModuleNames.AddRange(
            new[]
            {
                "Gamebase"
            }
        );
