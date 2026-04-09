---
source: unreal-push.md
section: "Request Push Settings"
order: 4
split: true
created_date_time: 20260408_184906
keyword: Unreal, Push, Alert
---

### Request Push Settings

사용자의 푸시 설정을 조회하려면 다음 API를 이용합니다.
콜백으로 받은 FGamebasePushTokenInfo 값으로 사용자 설정값을 얻을 수 있습니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void QueryTokenInfo(const FGamebasePushTokenInfoDelegate& Callback);

// Legacy API
void QueryPush(const FGamebasePushConfigurationDelegate& Callback);
```

**Example**

```cpp
void USample::QueryTokenInfo()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPush()->QueryTokenInfo(FGamebasePushTokenInfoDelegate::CreateLambda([](const FGamebasePushTokenInfo* TokenInfo, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("QueryTokenInfo succeeded. (pushEnabled= %s, adAgreement= %s, adAgreementNight= %s, TokenInfo= %s)"),
                TokenInfo->Agreement.bPushEnabled ? TEXT("true") : TEXT("false"),
                TokenInfo->Agreement.bAdAgreement ? TEXT("true") : TEXT("false"),
                TokenInfo->Agreement.bAdAgreementNight ? TEXT("true") : TEXT("false"),
                *TokenInfo->Token);
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("QueryTokenInfo failed. (Error: %d)"), Error->Code);
        }
    }));
}
```


#### FGamebasePushTokenInfo

| Parameter           | Values                 | Description         |
| --------------------| -----------------------| ------------------- |
| PushType            | FString                | Push 토큰 타입       |
| Token               | FString                | 토큰                 |
| UserId              | FString                | 사용자 아이디         |
| DeviceCountryCode   | FString                | 국가 코드           |
| Timezone            | FString                | 표준시간대           |
| RegisteredDateTime  | FString                | 토큰 업데이트 시간    |
| LanguageCode        | FString                | 언어 설정            |
| Agreement           | FGamebasePushAgreement | 수신 동의 여부        |
| bSandbox             | bool                   | sandbox 여부(iOS에 한함)        |

#### FGamebasePushAgreement

| Parameter        | Values  | Description               |
| -----------------| --------| ------------------------- |
| bPushEnabled      | bool | 알림 표시 동의 여부           |
| bAdAgreement      | bool | 광고성 알림 표시 동의 여부      |
| bAdAgreementNight | bool | 야간 광고성 알림 표시 동의 여부  |
