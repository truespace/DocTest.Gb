---
source: unreal-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "Mapping, Add Mapping Flow, Add Mapping, AddMapping with Credential, Add Mapping Forcibly"
section: Mapping
order: 4
---

## Mapping

매핑은 기존에 로그인된 계정에 다른 IdP의 계정을 연동하거나 해제시키는 기능입니다.

대다수의 게임에서는 게임 유저 계정 하나에 여러 IdP를 연동(매핑)할 수 있습니다.<br/>Gamebase의 매핑 API를 사용하면 기존에 로그인된 계정에 다른 IdP 계정을 연동하거나 해제할 수 있습니다.

즉, 연동 중인 IdP 계정으로 로그인을 시도하면 항상 같은 사용자 ID로 로그인됩니다.<br/><br/>

주의할 점은, IdP마다 하나의 계정만 연동할 수 있다는 점입니다.<br/>
예를 들어 Google 계정을 연동 중이면, 다른 Google 계정을 추가로 연동할 수 없습니다.<br/>
계정 연동 예시는 다음과 같습니다.<br/><br/>

* Gamebase 사용자 ID: 123bcabca
    * Google ID: aa
    * Facebook ID: bb
    * AppleID ID: cc
    * Twitter ID: dd
* Gamebase 사용자 ID : 456abcabc
    * Google ID: ee
    * Google ID: ff **-> 이미 Google ee 계정이 연동 중이므로 Google 계정을 추가로 연동할 수 없습니다.**

매핑 API에는 매핑 추가와 매핑 해제 API가 있습니다.

> <font color="red">[주의]</font><br/>
>
> Guest 로그인 중에 매핑을 성공하면 Guest IdP는 사라집니다.
>

### Add Mapping Flow

매핑은 다음 순서로 구현할 수 있습니다.

![add mapping flow](./image/auth_add_mapping_flow_2.30.0.png)
<!-- LLM_Image_DESC_20260406
    유형: Flowchart
    내용: AddMapping(계정 연동 추가) 흐름도
    구성: Login 후 AddMapping 호출, 성공/실패 분기, SOCKET_RESPONSE_TIMEOUT 에러 처리 및 Retry 로직, 실패 시 Case 1(이미 연동된 IdP) Case 2(Logout 후 Login) Case 3(Nothing) Case 4(Cancel) 등 다양한 분기 처리를 보여주는 플로우차트
    Keyword: 매핑, AddMapping, 계정연동, 인증, 플로우차트, Gamebase
-->

#### 1. 로그인
매핑은 현재 계정에 IdP 계정 연동을 추가하는 것이므로 우선 로그인이 돼 있어야 합니다.
먼저 로그인 API를 호출해 로그인합니다.

#### 2. 매핑

**AddMapping API**를 호출해 매핑을 시도합니다.

#### 2-1. 매핑에 성공한 경우

* 축하합니다! 현재 계정과 연동 중인 IdP 계정이 추가되었습니다.
* 매핑에 성공해도 '현재 로그인 중인 IdP'가 바뀌지는 않습니다. <br>즉, Google 계정으로 로그인한 후, Facebook 계정 매핑 시도가 성공했다고 해서 '현재 로그인 중인 IdP'가 Google에서 Facebook으로 변경되지는 않습니다. Google 상태로 유지됩니다.
* 매핑은 단순히 IdP 연동만 추가합니다.

#### 2-2. 매핑에 실패한 경우

* 네트워크 오류
    * 오류 코드가 **SOCKET_ERROR(110)** 또는 **SOCKET_RESPONSE_TIMEOUT(101)**인 경우, 일시적인 네트워크 문제로 인증에 실패한 것이므로 **AddMapping API**를 다시 호출하거나, 잠시 대기했다가 재시도 합니다.
* 이미 다른 계정에 연동 중일 때 발생하는 오류
    * 오류 코드가 **AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302)**인 경우, 매핑하려는 IdP의 계정이 이미 다른 계정에 연동 중이라는 뜻입니다. 이미 연동된 계정을 해제하려면 해당 계정으로 로그인하여 **Withdraw API**를 호출하여 탈퇴하거나 **RemoveMapping API**를 호출하여 연동을 해제한 후 다시 매핑을 시도하세요.
* 이미 동일한 IdP 계정에 연동돼 발생하는 오류
    * 오류 코드가 **AUTH_ADD_MAPPING_ALREADY_HAS_SAME_IDP(3303)** 인 경우, 매핑하려는 IdP와 같은 종류의 계정이 이미 연동 중이라는 뜻입니다.
    * Gamebase 매핑은 한 IdP당 하나의 계정만 연동 가능합니다. 예를 들어 PAYCO 계정에 이미 연동 중이라면 더 이상 PAYCO 계정을 추가할 수 없습니다.
    * 동일 IdP의 다른 계정을 연동하기 위해서는 **RemoveMapping API**를 호출해 연동을 해제한 후 다시 매핑을 시도하세요.
* 그 외의 오류
    * 매핑 시도에 실패했습니다.


### Add Mapping

특정 IdP에 로그인된 상태에서 다른 IdP로 매핑을 시도합니다.
매핑하려는 IdP의 계정이 이미 다른 계정에 연동되어 있다면
**AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302)** 오류를 반환합니다.<br/>

매핑에 성공하더라도 '현재 로그인 중인 IdP'가 바뀌지는 않습니다. 즉, Google 계정으로 로그인한 후, Facebook 계정 매핑 시도가 성공했다고 해서 '현재 로그인 중인 IdP'가 Google에서 Facebook으로 변경되지는 않습니다. Google 상태로 유지됩니다.
매핑은 단순히 IdP 연동만 추가합니다.

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void AddMapping(const FString& ProviderName, const FGamebaseAuthTokenDelegate& Callback);
void AddMapping(const FString& ProviderName, const FGamebaseVariantMap& AdditionalInfo, const FGamebaseAuthTokenDelegate& Callback)
```

**Example**

```cpp
void USample::AddMapping(const FString& ProviderName)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddMapping(ProviderName, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("AddMapping succeeded."));
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("AddMapping failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```

### AddMapping with Credential

게임에서 직접 IdP에서 제공하는 SDK로 먼저 인증하고 발급 받은 Access Token 등을 이용해, Gamebase AddMapping을 할 수 있는 인터페이스입니다.

* Credential 파라미터의 설정 방법

| keyname | a use | 값 종류 |
| ---------------------------------------- | ------------------------------------ | ------------------------------ |
| GamebaseAuthProviderCredential::ProviderName | IdP 유형 설정 | GamebaseAuthProvider::Google<br> GamebaseAuthProvider::Facebook<br>GamebaseAuthProvider::Naver<br>GamebaseAuthProvider::Twitter<br>GamebaseAuthProvider::Line<br>GamebaseAuthProvider::Hangame<br>GamebaseAuthProvider::AppleId<br>GamebaseAuthProvider::Weibo<br>GamebaseAuthProvider::GameCenter<br>GamebaseAuthProvider::Payco<br>GamebaseAuthProvider::Steam |
| GamebaseAuthProviderCredential::AccessToken | IdP 로그인 이후 받은 인증 정보(Access Token) 설정<br/>Google 인증 시에는 사용 안 함 |                                |
| GamebaseAuthProviderCredential::AuthorizationCode | Google 로그인 이후 받은 인증 정보(Authorization Code) 설정 |                                          |

> [TIP]
>
> 게임 내에서 외부 서비스(Facebook 등)의 고유 기능을 사용해야 할 때 필요할 수 있습니다.
>


> <font color="red">[주의]</font><br/>
>
> 외부 SDK에서 지원 요구하는 개발 사항은 외부 SDK의 API를 사용해 구현해야 하며, Gamebase에서는 지원하지 않습니다.
>

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void AddMapping(const FGamebaseVariantMap& CredentialInfo, const FGamebaseAuthTokenDelegate& Callback);
```

**Example**

```cpp
void USample::AddMappingWithCredential()
{
    FGamebaseVariantMap CredentialInfo;

    // google
    //CredentialInfo.Add(GamebaseAuthProviderCredential::ProviderName, GamebaseAuthProvider::Google);
    //CredentialInfo.Add(GamebaseAuthProviderCredential::AuthorizationCode, TEXT("google auchorization code"));

    // facebook
    CredentialInfo.Add(GamebaseAuthProviderCredential::ProviderName, GamebaseAuthProvider::Facebook);
    CredentialInfo.Add(GamebaseAuthProviderCredential::AccessToken, TEXT("facebook access token"));

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddMapping(*CredentialInfo, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("AddMapping succeeded."));
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("AddMapping failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```

### Add Mapping Forcibly

특정 IdP에 이미 매핑된 계정이 있을 때, **강제로** 매핑을 시도합니다.
**강제 매핑**을 시도할 때는 AddMapping API에서 획득한 `ForcingMappingTicket`이 필요합니다.

다음은 Facebook에 강제 매핑을 시도하는 예시입니다.

**API**

```cpp
void AddMappingForcibly(const FGamebaseForcingMappingTicket& ForcingMappingTicket, const FGamebaseAuthTokenDelegate& Callback);

// Legacy API
void AddMappingForcibly(const FString& ProviderName, const FString& ForcingMappingKey, const FGamebaseAuthTokenDelegate& Callback);
void AddMappingForcibly(const FString& ProviderName, const FString& ForcingMappingKey, const FGamebaseVariantMap& AdditionalInfo, const FGamebaseAuthTokenDelegate& Callback);
void AddMappingForcibly(const FGamebaseVariantMap& CredentialInfo, const FString& ForcingMappingKey, const FGamebaseAuthTokenDelegate& Callback);
```

**Example**

```cpp
void USample::AddMappingForcibly(const FString& ProviderName)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddMapping(GetProviderName(LoginType), FGamebaseAuthTokenDelegate::CreateLambda([Subsystem](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("AddMapping succeeded. Gamebase userId is %s"), *AuthToken->Member.UserId);
        }
        else
        {
            if (Error->Code == GamebaseErrorCode::AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER)
            {
                // ForcingMappingTicket 클래스의 From() 메서드를 이용하여 ForcingMappingTicket 인스턴스를 얻습니다.
                const FGamebaseForcingMappingTicketPtr ForcingMappingTicket = FGamebaseForcingMappingTicket::From(Error);
                if (!ForcingMappingTicket.IsValid())
                {
                    // Unexpected error occurred. Contact Administrator.
                }

                // 강제 매핑을 시도합니다.
                Subsystem->AddMappingForcibly(*ForcingMappingTicket, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* InnerAuthToken, const FGamebaseError* InnerError)
                {
                    if (Gamebase::IsSuccess(InnerError))
                    {
                        // 강제 매핑 추가 성공
                        UE_LOG(LogTemp, Display, TEXT("ChangeLogin succeeded. Gamebase userId is %s"), *InnerAuthToken->Member.UserId);
                    }
                    else
                    {
                        // 오류 코드를 확인하고 적절한 처리를 진행합니다.
                        UE_LOG(LogTemp, Display, TEXT("ChangeLogin failed."));
                    }
                }));
            }
            else
            {
                // 오류 코드를 확인하고 적절한 처리를 진행합니다.
                UE_LOG(LogTemp, Display, TEXT("AddMapping failed."));
            }
        }
    }));
}
```

### Change Login with ForcingMappingTicket

특정 IdP에 이미 매핑된 계정이 있다면 현재 계정에서 로그아웃하고 매핑된 계정으로 로그인합니다.
이때, AddMapping API에서 획득한 `ForcingMappingTicket`이 필요합니다.

Change Login API 호출이 실패하는 경우, Gamebase 로그인 상태는 기존의 UserID로 유지됩니다.

**API**

```cpp
void ChangeLogin(const FGamebaseForcingMappingTicket& ForcingMappingTicket, const FGamebaseAuthTokenDelegate& Callback);
```

**Example**

다음은 Facebook으로 매핑 시도 후 Facebook에 이미 매핑된 계정이 존재하자, 해당 계정으로 로그인을 변경하는 예시입니다.

```cpp
void USample::ChangeLoginWithFacebook(const FString& ProviderName)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddMapping(GamebaseAuthProvider::Facebook, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("AddMapping succeeded. Gamebase userId is %s"), *AuthToken->Member.UserId);
        }
        else
        {
            if (Error->Code == GamebaseErrorCode::AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER)
            {
                // ForcingMappingTicket 클래스의 From() 메서드를 이용하여 ForcingMappingTicket 인스턴스를 얻습니다.
                const FGamebaseForcingMappingTicketPtr ForcingMappingTicket = FGamebaseForcingMappingTicket::From(Error);
                if (!ForcingMappingTicket.IsValid())
                {
                    // Unexpected error occurred. Contact Administrator.
                }

                // 로그인 변경을 시도합니다.
                Subsystem->ChangeLogin(*ForcingMappingTicket, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* InnerAuthToken, const FGamebaseError* InnerError)
                {
                    if (Gamebase::IsSuccess(InnerError))
                    {
                        // 로그인 변경 성공
                        UE_LOG(LogTemp, Display, TEXT("ChangeLogin succeeded. Gamebase userId is %s"), *InnerAuthToken->Member.UserId);
                    }
                    else
                    {
                        // 로그인 변경 실패
                        // 오류 코드를 확인하고 적절한 처리를 진행합니다.
                        UE_LOG(LogTemp, Display, TEXT("ChangeLogin failed."));
                    }
                }));
            }
            else
            {
                // 오류 코드를 확인하고 적절한 처리를 진행합니다.
                UE_LOG(LogTemp, Display, TEXT("AddMapping failed."));
            }
        }
    }));
}
```

### Remove Mapping

특정 IdP에 대한 연동을 해제합니다. 만약, 해제할 IdP가 유일한 IdP라면, 실패를 반환합니다.
연동 해제 후에는 Gamebase 내부에서, 해당 IdP에 대한 로그아웃을 처리합니다.

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void RemoveMapping(const FString& ProviderName, const FGamebaseErrorDelegate& Callback);
```

**Example**

```cpp
void USample::RemoveMapping(const FString& ProviderName)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->RemoveMapping(ProviderName, FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RemoveMapping succeeded."));
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("RemoveMapping failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```

### Get Mapping List

사용자 ID에 연동된 IdP 목록을 반환합니다.<br/>

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
TArray<FString> GetAuthMappingList() const;
```

**Example**

```cpp
void USample::GetAuthMappingList()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    auto MappingList = Subsystem->GetAuthMappingList();
    
    for (FString provider : MappingList)
    {
        UE_LOG(LogTemp, Display, TEXT("GetAuthMappingList - %s"), *provider);
    }
}
```
