---
source: unreal-initialization.md
section: "Get Launching Information"
order: 6
split: true
created_date_time: 20260408_191848
keyword: Unreal, Initialize, Initialization
---

### Get Launching Information

GetLaunchingInformations API를 이용하면 Initialize 이후에도 LaunchingInfo 객체를 얻을 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> GetLaunchingInformations API 는 실시간으로 서버에서 정보를 가져오는 비동기 API가 아닙니다.
> 2분 주기로 업데이트 되는 캐시 정보를 반환하므로, 실시간으로 현재의 점검 여부를 판단하는 용도로는 적합하지 않습니다.
> 이런 경우에는 Launching Status Code가 변경되었을때 이벤트가 동작하는 GamebaseEventHandler 를 활용하시기 바랍니다.
> [Game > Gamebase > Unreal SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Observer](../unreal-etc.md#observer)

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#B60205; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
const FGamebaseLaunchingInfoPtr GetLaunchingInformations() const;
```

**Example**

```cpp
void USample::GetLaunchingInformations()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    auto LaunchingInformation = Subsystem->GetLaunching().GetLaunchingInformations();
    if (LaunchingInformation.IsValid() == false)
    {
        UE_LOG(LogTemp, Display, TEXT("Not found launching info."));
        return;
    }
}
```
