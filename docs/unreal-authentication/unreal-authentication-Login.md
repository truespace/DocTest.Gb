---
source: unreal-authentication.md
section: "Login"
order: 1
split: true
created_date_time: 20260408_191848
keyword: Unreal, Login, Logout, Initialize, Authentication, Error, LoginForLastLoggedInProvider, Console
---

## Game > Gamebase > Unreal SDK 사용 가이드 > 인증

## Login

Gamebase에서는 게스트 로그인을 기본으로 지원합니다.<br/>

* 게스트 이외의 Provider에 로그인하려면 해당 Provider AuthAdapter가 필요합니다.
* AuthAdapter 및 3rd-Party Provider SDK에 대한 설정은 다음을 참고하시기 바랍니다.
    * [3rd-Party Provider SDK Guide](../aos-started.md#3rd-party-provider-sdk-guide)


### Login Flow

많은 게임이 타이틀 화면에 로그인을 구현합니다.

* 앱을 설치하고 처음 실행했을 때 타이틀 화면에서 게임 유저가 어떤 IdP(identity provider)로 인증할지 선택할 수 있게 합니다.
* 한 번 로그인한 후에는 IdP 선택 화면을 표시하지 않고 이전에 로그인한 IdP 유형으로 인증합니다.

위에서 설명한 로직은 다음과 같은 순서로 구현할 수 있습니다.

![last provider login flow](./image/login_for_last_logged_in_provider_flow_2.19.0.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Flowchart
    내용: 최근 로그인 Provider 자동 로그인 흐름도
    구성: 마지막으로 로그인한 Provider 정보를 이용한 자동 로그인 처리 흐름
    Keyword: Flowchart, Login Flow
-->
![idp login flow](./image/idp_login_flow_2.19.0.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Flowchart
    내용: IdP 로그인 처리 흐름도
    구성: Gamebase SDK의 IdP 로그인 요청부터 인증 결과 반환까지의 처리 흐름을 나타내는 순서도
    Keyword: Flowchart, Login Flow
-->

#### 1. 이전 로그인 유형으로 인증

* 이전에 인증했던 기록이 있다면 ID와 비밀번호를 입력받지 않고 인증을 시도합니다.
* **LoginForLastLoggedInProvider API**를 호출합니다.

#### 1-1. 인증에 성공한 경우

* 축하합니다! 인증에 성공했습니다.
* **GetUserID API**로 사용자 ID를 획득하여 게임 로직을 구현하시면 됩니다.

#### 1-2. 인증에 실패한 경우

* 네트워크 오류
    * 오류 코드가 **SOCKET_ERROR(110)** 또는 **SOCKET_RESPONSE_TIMEOUT(101)** 인 경우, 일시적인 네트워크 문제로 인증이 실패한 것이므로 **LoginForLastLoggedInProvider API**를 다시 호출하거나, 잠시 후 다시 시도합니다.
* 이용 정지 게임 유저
    * 오류 코드가 **BANNED_MEMBER(7)**인 경우, 이용 정지 게임 유저이므로 인증에 실패한 것입니다.
    * **FGamebaseBanInfo::From API**로 제재 정보를 확인하여 게임 유저에게 게임을 플레이할 수 없는 이유를 알려주시기 바랍니다.
    * Gamebase 초기화 시 **FGamebaseConfiguration.bEnablePopup** 및 **FGamebaseConfiguration.bEnableBanPopup** 값을 true로 한다면 Gamebase가 이용 정지에 관한 팝업 창을 자동으로 띄웁니다.
* 그 외 오류
    * 이전 로그인 유형으로 인증에 실패했습니다. **'2. 지정된 IdP로 인증'**을 진행합니다.

#### 2. 지정된 IdP로 인증

* IdP 유형을 직접 지정하여 인증을 시도합니다.
    * 인증 가능한 유형은 **GamebaseAuthProvider** 클래스에 선언돼 있습니다.
* **Login(ProviderName, callback) API**를 호출합니다.

#### 2-1. 인증에 성공한 경우

* 축하합니다! 인증에 성공했습니다.
* **GetUserID API**로 사용자 ID를 획득하여 게임 로직을 구현하시면 됩니다.

#### 2-2. 인증에 실패한 경우

* 네트워크 오류
    * 오류 코드가 **SOCKET_ERROR(110)** 또는 **SOCKET_RESPONSE_TIMEOUT(101)**인 경우, 일시적인 네트워크 문제로 인증에 실패한 것이므로 **Login(ProviderName, callback) API**를 다시 호출하거나, 잠시 후 다시 시도합니다.
* 이용 정지 게임 유저
    * 오류 코드가 **BANNED_MEMBER(7)**인 경우, 이용 정지 게임 유저이므로 인증에 실패한 것입니다.
    * **FGamebaseBanInfo::From API**로 제재 정보를 확인하여 게임 유저에게 게임을 플레이할 수 없는 이유를 알려 주시기 바랍니다.
    * Gamebase 초기화 시 **FGamebaseConfiguration.bEnablePopup** 및 **FGamebaseConfiguration.bEnableBanPopup** 값을 **true**로 지정하면 Gamebase가 이용 정지에 관한 팝업 창을 자동으로 표시합니다.
* 그 외의 오류
    * 오류가 발생했다는 것을 게임 유저에게 알리고, 게임 유저가 인증 IdP 유형을 선택할 수 있는 상태(주로 타이틀 화면 또는 로그인 화면)로 되돌아갑니다.

### Login as the Latest Login IdP

가장 최근에 로그인한 IdP로 로그인을 시도합니다.
해당 로그인에 대한 토큰이 만료되었거나, 토큰에 대한 검증 등에 실패하면 실패를 반환합니다.
이때는 [해당 IdP에 대한 로그인](#login-with-idp)을 구현해야 합니다.

* AdditionalInfo 파라미터 설정 방법

| keyname                                  | a use                                    | 값 종류                                     |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| GamebaseAuthProviderCredential::ShowLoadingAnimation | API 호출이 끝날 때까지 로딩 애니메이션을 표시<br>**Android에 한함** | **bool**<br>**default**: true |

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void LoginForLastLoggedInProvider(const FGamebaseAuthTokenDelegate& Callback);
void LoginForLastLoggedInProvider(const FGamebaseVariantMap& AdditionalInfo, const FGamebaseAuthTokenDelegate& Callback);
```

**Example**

```cpp
void USample::LoginForLastLoggedInProvider()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->LoginForLastLoggedInProvider(FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("LoginForLastLoggedInProvider succeeded."));
        }
        else
        {
            if (Error->Code == GamebaseErrorCode::SOCKET_ERROR || Error->Code == GamebaseErrorCode::SOCKET_RESPONSE_TIMEOUT)
            {
                UE_LOG(LogTemp, Display, TEXT("Retry LoginForLastLoggedInProvider or notify an Error message to the user. : %s"), *Error->Message);
            }
            else if (Error->Code == GamebaseErrorCode::BANNED_MEMBER)
            {
                auto BanInfo = FGamebaseBanInfo::From(Error);
                if (BanInfo.IsValid())
                {
                    UE_LOG(LogTemp, Display, TEXT("This user has been banned. Gamebase userId is %s"), *BanInfo->UserId);
                }
            }
            else
            {
                UE_LOG(LogTemp, Display, TEXT("Try to login using a specifec IdP"));
            }
        }
    }));
}
```

### Login with GUEST

Gamebase는 게스트 로그인을 지원합니다.

* 디바이스의 유일한 키를 생성하여 Gamebase에 로그인을 시도합니다.
* 게스트 로그인은 디바이스 키는 초기화될 수 있고 디바이스 키의 초기화 시에 계정이 삭제될 수 있으므로 IdP를 활용한 로그인 방식을 권장합니다.

> <font color="red">[주의]</font><br/>
>
> Windows 환경에서는 GUEST 로그인은 개발 용도로 제공되었기 때문에 실제 게임에서 사용 시 주의가 필요합니다.
>

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void Login(const FString& ProviderName, const FGamebaseAuthTokenDelegate& Callback);
```

**Example**

```cpp
void USample::Login()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Login(GamebaseAuthProvider::Guest, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {1
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("Login succeeded. Gamebase userId is %s"), *AuthToken->Member.UserId);
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("Login failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);

            if (Error->Code == GamebaseErrorCode::SOCKET_ERROR || Error->Code == GamebaseErrorCode::SOCKET_RESPONSE_TIMEOUT)
            {
                UE_LOG(LogTemp, Display, TEXT("Retry LoginForLastLoggedInProvider or notify an Error message to the user. : %s"), *Error->Message);
            }
            else if (Error->Code == GamebaseErrorCode::BANNED_MEMBER)
            {
                auto BanInfo = FGamebaseBanInfo::From(Error);
                if (BanInfo.IsValid())
                {
                    UE_LOG(LogTemp, Display, TEXT("This user has been banned. Gamebase userId is %s"), *BanInfo->userId);
                }
            }
        }
    }));
}
```

### Login with IdP

다음은 특정 IdP로 로그인할 수 있게 하는 예시 코드입니다
로그인할 수 있는 IdP 유형은 **GamebaseAuthProvider** 클래스에서 확인할 수 있습니다.

> [참고]
>
> 로그인할 때 추가 정보를 필요로 하는 IdP도 있습니다.
> 이러한 추가 정보들을 설정할 수 있게 void Login(const FString& ProviderName, const FGamebaseVariantMap& AdditionalInfo, const FGamebaseAuthTokenDelegate& Callback) API를 제공합니다.
>AdditionalInfo 파라미터에 필수 정보들을 dictionary 형태로 입력하시면 됩니다.
>AdditionalInfo 값이 있을 경우에는 해당 값을 사용하고 null일 경우에는 [NHN Cloud Console](../oper-app.md#authentication-information)에 등록된 값을 사용합니다.

> [참고]
>
> LINE IdP는 Gamebase SDK 2.43.0부터 LINE 서비스 제공 지역을 설정할 수 있습니다.
> 해당 지역은 AdditionalInfo에 설정할 수 있습니다. 

* AdditionalInfo 파라미터 설정 방법

| keyname                                  | a use                                    | 값 종류                                     |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| GamebaseAuthProviderCredential::LineChannelRegion | LINE 서비스 제공 지역 설정 | "japan"<br/>"thailand"<br/>"taiwan"<br/>"indonesia" |

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void Login(const FString& ProviderName, const FGamebaseAuthTokenDelegate& Callback);
void Login(const FString& ProviderName, const FGamebaseVariantMap& AdditionalInfo, const FGamebaseAuthTokenDelegate& Callback);
```

**Example**

```cpp
void USample::Login()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Login(GamebaseAuthProvider::Facebook, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("Login succeeded. Gamebase userId is %s"), *AuthToken->Member.UserId);
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("Login failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);

            if (Error->Code == GamebaseErrorCode::SOCKET_ERROR || Error->Code == GamebaseErrorCode::SOCKET_RESPONSE_TIMEOUT)
            {
                UE_LOG(LogTemp, Display, TEXT("Retry LoginForLastLoggedInProvider or notify an Error message to the user. : %s"), *Error->Message);
            }
            else if (Error->Code == GamebaseErrorCode::BANNED_MEMBER)
            {
                auto BanInfo = FGamebaseBanInfo::From(Error);
                if (BanInfo.IsValid())
                {
                    UE_LOG(LogTemp, Display, TEXT("This user has been banned. Gamebase userId is %s"), *BanInfo->UserId);
                }
            }
        }
    }));
}

void USample::LoginWithAdditionalInfo()
{
    FGamebaseVariantMap AdditionalInfo;
    AdditionalInfo.Add(TEXT("Key"), TEXT("Value"));

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Login(GamebaseAuthProvider::Facebook, AdditionalInfo, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("Login succeeded. Gamebase userId is %s"), *AuthToken->Member.UserId);
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("Login failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```

#### Cancel Login with External Browser

Windows 환경에서 SDK를 사용하지 않는 IdP의 경우 외부 브라우저를 통해 로그인을 진행합니다.
로그인 과정 중 외부 브라우저를 통한 로그인 플로우인 경우 해당 API를 호출하여 Login 과정을 중단하고 결과를 전달할 수 있습니다.

**API**

Supported Platforms

<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void CancelLoginWithExternalBrowser();
```

**Example**

```cpp
void USample::CancelLogin()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->CancelLoginWithExternalBrowser();
}
```

### Login with Credential

IdP에서 제공하는 SDK를 사용해 게임에서 직접 인증한 후 발급 받은 Access Token 등을 이용하여, Gamebase에 로그인할 수 있는 인터페이스입니다.

* Credential 파라미터의 설정 방법

| keyname | a use | 값 종류 |
| ---------------------------------------- | ------------------------------------ | ------------------------------ |
| GamebaseAuthProviderCredential::ProviderName | IdP 유형 설정                           | GamebaseAuthProvider::Google<br> GamebaseAuthProvider::Facebook<br>GamebaseAuthProvider::Naver<br>GamebaseAuthProvider::Twitter<br>GamebaseAuthProvider::Line<br>GamebaseAuthProvider::Hangame<br>GamebaseAuthProvider::AppleId<br>GamebaseAuthProvider::Weibo<br>GamebaseAuthProvider::GameCenter<br>GamebaseAuthProvider::Payco<br>GamebaseAuthProvider::Steam<br>GamebaseAuthProvider::EpicGames |
| GamebaseAuthProviderCredential::AccessToken | IdP 로그인 이후 받은 인증 정보(Access Token) 설정<br/>Google 인증 시에는 사용 안 함 |                                |
| GamebaseAuthProviderCredential::AuthorizationCode | Google 로그인 이후 받은 인증 정보(Authorization Code) 설정 |                                          |
| GamebaseAuthProviderCredential::GamebaseAccessToken | IdP 인증 정보가 아닌 Gamebase Access Token으로 로그인하는 경우 사용 |  |
| GamebaseAuthProviderCredential::IgnoreAlreadyLoggedIn | Gamebase에 로그인한 상태에서 로그아웃을 하지 않고 다른 계정을 이용해 로그인을 시도하는 것을 허용 | **bool** |
| GamebaseAuthProviderCredential::LineChannelRegion | LINE 서비스 제공 지역 설정 | [Login with IdP 참고](./unreal-authentication-Login.md#login-with-idp) |

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
void Login(const FGamebaseVariantMap& CredentialInfo, const FGamebaseAuthTokenDelegate& Callback);
```

**Example**

```cpp
void USample::LoginWithCredential()
{
    FGamebaseVariantMap CredentialInfo;

    // google
    //CredentialInfo.Add(GamebaseAuthProviderCredential::ProviderName, GamebaseAuthProvider::Google);
    //CredentialInfo.Add(GamebaseAuthProviderCredential::AuthorizationCode, TEXT("google auchorization code"));

    // facebook
    CredentialInfo.Add(GamebaseAuthProviderCredential::ProviderName, GamebaseAuthProvider::Facebook);
    CredentialInfo.Add(GamebaseAuthProviderCredential::AccessToken, TEXT("facebook access token"));

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Login(*CredentialInfo, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("Login succeeded. Gamebase userId is %s"), *AuthToken->Member.UserId);
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("Login failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```
