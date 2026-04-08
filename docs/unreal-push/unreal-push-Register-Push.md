---
source: unreal-push.md
section: "Register Push"
order: 2
split: true
created_date_time: 20260408_191848
keyword: Unreal, Login, Push, RegisterPush, Android
---

### Register Push

다음 API를 호출하여, NHN Cloud Push에 해당 사용자를 등록합니다.
푸시 동의 여부(enablePush), 광고성 푸시 동의 여부(enableAdPush), 야간 광고성 푸시 동의 여부(enableAdNightPush)값을 사용자로부터 받아, 다음 API를 호출해 등록을 완료합니다.

> <font color="red">[주의]</font><br/>
>
> UserID 마다 푸시 설정이 다를 수 있고, 푸시 토큰이 만료되는 경우도 발생할 수 있으므로 로그인 이후에는 매번 RegisterPush API를 호출할 것을 권장합니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void RegisterPush(const FGamebasePushConfiguration& Configuration, const FGamebaseErrorDelegate& Callback);
void RegisterPush(const FGamebasePushConfiguration& Configuration, const FGamebaseNotificationOptions& NotificationOptions, const FGamebaseErrorDelegate& Callback);
```

#### FGamebasePushConfiguration

| Parameter     | Mandatory(M) /<br/>Optional(O) | Values            | Description        |
| ------------- | ------------- | ---------------------------------- | ------------------ |
| bPushEnabled                   | M             | bool         | 푸시 동의 여부 |
| bADAgreement                   | M             | bool         | 광고성 푸시 동의 여부 |
| bADAgreementNight | M          | bool         | 야간 광고성 푸시 동의 여부 |
| bRequestNotificationPermission | O             | bool         | Android 13 이상의 OS에서 RegisterPush API를 호출했을 때 푸시 권한 요청 팝업 자동 출력 여부<br>**default**: true<br/>**Android에 한함** |
| bAlwaysAllowTokenRegistration  | O             | bool         | 사용자가 푸시 권한을 거부해도 토큰을 등록할지 여부<br>true로 설정할 경우 푸시 권한을 획득하지 못하더라도 토큰을 등록합니다.<br>**default**: false<br/>**iOS에 한함** |

**Example**

```cpp
void USample::RegisterPush(bool bPushEnabled, bool bADAgreement, bool bADAgreementNight)
{
    FGamebasePushConfiguration Configuration;
    Configuration.bPushEnabled = bPushEnabled;
    Configuration.bADAgreement = bADAgreement;
    Configuration.bADAgreementNight = bADAgreementNight;
    Configuration.bRequestNotificationPermission = bRequestNotificationPermission;
    Configuration.bAlwaysAllowTokenRegistration = bAlwaysAllowTokenRegistration;
    
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPush()->RegisterPush(Configuration, FGamebasePushConfigurationDelegate::CreateLambda([](const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RegisterPush succeeded"));
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("RegisterPush failed. (Error: %d)"), Error->Code);
        }
    }));
}
```
