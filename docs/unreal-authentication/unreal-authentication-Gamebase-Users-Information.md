---
source: unreal-authentication.md
section: "Gamebase User's Information"
order: 5
split: true
created_date_time: 20260408_184906
keyword: Unreal, Login, Authentication, LoginForLastLoggedInProvider
---

## Gamebase User's Information

Gamebase에서 인증 절차를 진행한 후, 앱을 제작할 때 필요한 정보를 획득할 수 있습니다.

### Get Authentication Information for Gamebase
Gamebase를 통하여 인증절차를 진행 후, 앱을 제작할 때 필요한 정보를 얻을 수 있습니다.

#### UserID

Gamebase에서 발급한 UserID를 가져올 수 있습니다.
**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
FString GetUserID() const;
```

**Example**
```cpp
void USample::GetUserID()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    FString UserID = Subsystem->GetUserID();
}
```

#### AccessToken

Gamebase에서 발급한 Access Token을 가져올 수 있습니다.

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
FString GetAccessToken() const;
```

**Example**
```cpp
void USample::GetAccessToken()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    FString AccessToken = Subsystem->GetAccessToken();
}
```

#### Last LoggedIn Provider Name

Gamebase에서 마지막 로그인에 성공한 ProviderName을 가져올 수 있습니다.

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void RequestLastLoggedInProvider(const FGamebaseLastLoggedInProviderDelegate& Callback) const;
FString GetLastLoggedInProvider() const;
```

**Example**
```cpp
void USample::GetLastLoggedInProvider()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());

    // Obtaining Last Logged In Provider - Sync
    FString LastLoggedInProvider = Subsystem->GetLastLoggedInProvider();
    
    // Obtaining Last Logged In Provider - Async
    // If GetLastLoggedInProvider() returns 'NOT_INITIALIZED_YET',
    // use the following async function instead:
    Subsystem->RequestLastLoggedInProvider(FGamebaseLastLoggedInProviderDelegate::CreateLambda([](const FString& lastLoggedInProviderAsync, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("LastLoggedInProvider: %s"), *lastLoggedInProviderAsync);
        }
    }));
}
```

### Get Authentication Information for External IdP

* 외부 인증 IdP의 Access Token, 사용자 ID, Profile 등의 정보는 로그인 후 게임 서버에서 Gamebase Server API를 호출하여 가져올 수 있습니다.
    * [Game > Gamebase > API 가이드 > Authentication > Get IdP Token and Profiles](../api-guide.md#get-idp-token-and-profiles)

> <font color="red">[주의]</font><br/>
>
> * 외부 IdP의 인증 정보는 보안을 위해 게임 서버에서 호출할 것을 권장합니다.
> * IdP에 따라 Access Token이 빠른 시간에 만료될 수 있습니다.
>     * 예를 들어 Google은 로그인 2시간 후에는 Access Token이 만료되어 버립니다.
>     * 사용자 정보가 필요하다면 로그인 후 바로 Gamebase Server API를 호출하시기 바랍니다.
> * "Gamebase.LoginForLastLoggedInProvider()" API로 로그인한 경우에는 인증 정보를 가져올 수 없습니다.
>     * 사용자 정보가 필요하다면 "Gamebase.LoginForLastLoggedInProvider()" 대신, 사용하고자 하는 IDPCode와 동일한 {IDP_CODE}를 파라미터로 하여 "Gamebase.Login(IDP_CODE, callback)" API로 로그인 해야 합니다.

### Get Banned User Information

Gamebase Console에 제재된 게임 유저로 등록될 경우, 로그인을 시도하면 아래와 같은 이용 제한 정보 코드(**BANNED_MEMBER(7)**)가 표시될 수 있습니다.
**FGamebaseBanInfo::From API**를 이용해 제재 정보를 확인할 수 있습니다.
