---
source: unreal-initialization.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, SetDebugMode, GetSubsystem, GetGameInstance"
section: "Debug Mode"
order: 3
---

### Debug Mode

* Gamebase는 경고(warning)와 오류 로그만을 표시합니다.
* 개발에 참고할 수 있는 시스템 로그를 켜려면 **GamebaseSubsystem->SetDebugMode(true)**를 호출하시기 바랍니다.

> <font color="red">[주의]</font><br/>
>
> 게임을 **릴리스**할 때는 반드시 소스 코드에서 SetDebugMode 호출을 제거하거나 파라미터를 false로 바꿔서 빌드하세요.

디버그 설정은 Console에서도 가능하며 Console에서 설정된 값을 우선시합니다.
Console 설정 방법은 아래 가이드를 참고하십시오.

* [Console 테스트 단말기 설정](../oper-app.md#test-device)
* [Console Client 설정](../oper-app.md#client)

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void SetDebugMode(bool bIsDebugMode);
```

**Example**

```cpp
void USample::SetDebugMode(bool bIsDebugMode)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->SetDebugMode(bIsDebugMode);
}
```
