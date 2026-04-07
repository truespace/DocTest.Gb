---
source: unreal-push.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, Notification, Error, GetNotificationOptions, GetSubsystem, GetGameInstance, RegisterPushWithOption, IsSuccess"
section: "Notification Options"
order: 3
---

### Notification Options

* 단말기에 표시하는 알림을 어떤 형태로 표시할 것인지 Notification Options 를 통해 변경할 수 있습니다.
* 런타임에 RegisterPush API를 호출하여 변경할 수 있습니다.

#### Set Notification Options with RegisterPush in Runtime

RegisterPush API 호출 시 FGamebaseNotificationOptions 인자를 추가하여 알림 옵션을 설정할 수 있습니다.
FGamebaseNotificationOptions 의 생성자에 GamebaseSubsystem->GetPush()->GetNotificationOptions() 호출 결과를 전달하면 현재의 알림 옵션으로 초기화된 오브젝트가 생성되므로 필요한 값만 변경할 수 있습니다.<br/>
설정 가능한 값은 아래와 같습니다.

| API                    | Parameter       | Description        |
| ---------------------  | ------------ | ------------------ |
| bForegroundEnabled      | bool         | 앱이 포그라운드 상태일 때의 알림 노출 여부<br/>**default**: false |
| bBadgeEnabled           | bool         | 배지 아이콘 사용 여부<br/>**default**: true |
| bSoundEnabled           | bool         | 알림음 사용 여부<br/>**default**: true<br/>**iOS에 한함** |
| Priority               | int32        | 알림 우선 순위. 아래 5가지 값을 설정할 수 있습니다.<br/>GamebaseNotificationPriority::Min : -2<br/> GamebaseNotificationPriority::Low : -1<br/>GamebaseNotificationPriority::Default : 0<br/>GamebaseNotificationPriority::High : 1<br/>GamebaseNotificationPriority::Max : 2<br/>**default**: GamebaseNotificationPriority::High<br/>**Android에 한함** |
| SmallIconName          | FString       | 알림용 작은 아이콘 파일 이름.<br/>설정하지 않을 경우 앱 아이콘이 사용됩니다.<br/>**default**: null<br/>**Android에 한함** |
| SoundFileName          | FString       | 알림음 파일 이름. Android 8.0 미만 OS에서만 동작합니다.<br/>'res/raw' 폴더의 mp3, wav 파일명을 지정하면 알림음이 변경됩니다.<br/>**default**: null<br/>**Android에 한함** |

**Example**

```cpp
void USample::RegisterPushWithOption(bool bPushEnabled, bool bADAgreement, bool bADAgreementNight, const FString& DisplayLanguage, bool bForegroundEnabled, bool bBadgeEnabled, bool bSoundEnabled, int32 Priority, const FString& SmallIconName, const FString& SoundFileName)
{
    FGamebasePushConfiguration Configuration;
    Configuration.bPushEnabled = bPushEnabled;
    Configuration.bADAgreement = bADAgreement;
    Configuration.bADAgreementNight = bADAgreementNight;
    Configuration.bRequestNotificationPermission = bRequestNotificationPermission;
    Configuration.bAlwaysAllowTokenRegistration = bAlwaysAllowTokenRegistration;
    
    FGamebaseNotificationOptions NotificationOptions;
    NotificationOptions.bForegroundEnabled = bForegroundEnabled;
    NotificationOptions.bBadgeEnabled = bBadgeEnabled;
    NotificationOptions.bSoundEnabled = bSoundEnabled;
    NotificationOptions.Priority = Priority;
    NotificationOptions.SmallIconName = SmallIconName;
    NotificationOptions.SoundFileName = SoundFileName;

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPush()->RegisterPush(Configuration, NotificationOptions, FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RegisterPush succeeded"));
        }
        else
        {
            // Check the Error code and handle the Error appropriately.
            UE_LOG(LogTemp, Display, TEXT("RegisterPush failed. (Error: %d)"), Error->Code);
        }
    }));
}
```

#### Get NotificationOptions

푸시를 등록할 때 기존에 설정했던 알림 옵션값을 가져옵니다.

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
FGamebaseNotificationOptionsPtr GetNotificationOptions();
```

**Example**

```cpp
void USample::GetNotificationOptions()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    auto NotificationOptions = Subsystem->GetPush()->GetNotificationOptions();
    if (result.IsValid())
    {
        NotificationOptions->bForegroundEnabled = true;
        NotificationOptions->SmallIconName = TEXT("notification_icon_name");
        
        FGamebasePushConfiguration Configuration;
        
        UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
        Subsystem->GetPush()->RegisterPush(Configuration, NotificationOptions, FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error) { }));
    }
    else
    {
        UE_LOG(LogTemp, Display, TEXT("No GetNotificationOptions"));
    }
}
```
