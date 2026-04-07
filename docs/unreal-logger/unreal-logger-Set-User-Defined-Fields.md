---
source: unreal-logger.md
split: true
created_date_time: 20260406_141859
keyword: "Set User-Defined Fields"
section: "Set User-Defined Fields"
order: 4
---

### Set User-Defined Fields
원하는 사용자 정의 필드를 설정합니다. 
사용자 정의 필드를 설정하면 로그 전송 API를 호출할 때마다 설정한 값을 로그와 함께 서버로 전송합니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void SetUserField(const FString& key, const FString& value);
```

**Example**
```cpp
void USample::SetLoggerUserField()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetLogger()->SetUserField("KEY", "VALUE");
}
```
