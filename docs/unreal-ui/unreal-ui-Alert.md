---
source: unreal-ui.md
section: "Alert"
order: 6
split: true
created_date_time: 20260408_184906
keyword: Unreal, Alert, Ui
---

## Alert

시스템 알림을 표시할 수 있습니다.
시스템 알림에 콜백을 등록할 수도 있습니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void ShowAlert(const FString& Title, const FString& Message);
void ShowAlert(const FString& Title, const FString& Message, const FGamebaseAlertCloseDelegate& CloseCallback);
```

**Example**
```cpp
void USample::ShowAlert(const FString& Title, const FString& Message)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetUtil()->ShowAlert(Title, Message);
}

void USample::ShowAlertEvent(const FString& Title, const FString& Message)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetUtil()->ShowAlert(Title, Message, FGamebaseAlertCloseDelegate::CreateLambda([]()
    {
        UE_LOG(LogTemp, Display, TEXT("ShowAlert ButtonClick."));
    }));
}
```
