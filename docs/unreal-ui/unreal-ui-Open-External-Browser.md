---
source: unreal-ui.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, GetSubsystem, GetGameInstance, GetWebView"
section: "Open External Browser"
order: 5
---

## Open External Browser

다음 API를 통하여 외부 브라우져를 열 수 있습니다. 파라미터로 전송되는 url은 유효한 값이어야 합니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void OpenWebBrowser(const FString& Url);
```

**Example**
```cpp
void USample::OpenWebBrowser(const FString& Url)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetWebView()->OpenWebBrowser(Url);
}
```
