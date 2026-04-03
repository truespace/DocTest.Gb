---
source: unity-authentication.md
section: "Mapping"
order: 4
created_date: 2026-04-03
---

## Mapping

매핑은 기존에 로그인된 계정에 다른 IdP의 계정을 연동하거나 해제시키는 기능입니다.

대다수의 게임에서는 게임 유저 계정 하나에 여러 IdP를 연동(매핑)할 수 있습니다.<br/>
Gamebase의 매핑 API를 사용하면 기존에 로그인된 계정에 다른 IdP 계정을 연동하거나 해제할 수 있습니다.

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

#### 1. 로그인
매핑은 현재 계정에 IdP 계정 연동을 추가하는 것이므로 우선 로그인이 돼 있어야 합니다.
먼저 로그인 API를 호출해 로그인합니다.

#### 2. 매핑

**Gamebase.AddMapping()**을 호출해 매핑을 시도합니다.

#### 2-1. 매핑이 성공한 경우

* 축하합니다! 현재 계정과 연동중인 IdP 계정이 추가되었습니다.
* 매핑에 성공해도 '현재 로그인 중인 IdP'가 바뀌지는 않습니다. <br>즉, Google 계정으로 로그인한 후, Facebook 계정 매핑 시도가 성공했다고 해서 '현재 로그인 중인 IdP'가 Google에서 Facebook으로 변경되지는 않습니다. Google 상태로 유지됩니다.
* 매핑은 단순히 IdP 연동만 추가해 줍니다.

#### 2-2. 매핑이 실패한 경우

* 네트워크 오류
    * 오류 코드가 **SOCKET_ERROR(110)** 또는 **SOCKET_RESPONSE_TIMEOUT(101)**인 경우, 일시적인 네트워크 문제로 인증이 실패한 것이므로 **Gamebase.AddMapping()**을 다시 호출하거나, 잠시 대기했다가 재시도 합니다.
* 이미 다른 계정에 연동 중일 때 발생하는 오류
    * 오류 코드가 **AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302)**인 경우, 매핑하려는 IdP의 계정이 이미 다른 계정에 연동 중이라는 뜻입니다. 이미 연동된 계정을 해제하려면 해당 계정으로 로그인하여 **Gamebase.Withdraw()**를 호출하여 탈퇴하거나 **Gamebase.RemoveMapping()**를 호출하여 연동을 해제한 후 다시 매핑을 시도하세요.
* 이미 동일한 IdP 계정에 연동돼 발생하는 오류
	* 오류 코드가 **AUTH_ADD_MAPPING_ALREADY_HAS_SAME_IDP(3303)**인 경우 매핑하려는 IdP와 같은 종류의 계정이 이미 연동 중이라는 뜻입니다.
	* Gamebase 매핑은 한 IdP당 하나의 계정만 연동 가능합니다. 예를 들어 PAYCO 계정에 이미 연동 중이라면 더 이상 PAYCO 계정을 추가할 수 없습니다.
	* 동일 IdP의 다른 계정을 연동하기 위해서는 **Gamebase.RemoveMapping()**을 호출해 연동을 해제한 후 다시 매핑을 시도하세요.
* 그 외의 오류
    * 매핑 시도가 실패했습니다.

### Add Mapping

특정 IdP에 로그인 된 상태에서 다른 IdP로 Mapping을 시도합니다.
Mapping을 하려는 IdP의 계정이 이미 다른 계정에 연동이 되어있다면
**AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302)** 오류를 반환합니다.<br/>

Mapping이 성공 하더라도 '현재 로그인 중인 IdP'가 바뀌지는 않습니다. 즉, Google 계정으로 로그인 한 후, Facebook 계정 Mapping 시도가 성공했다고 해서 '현재 로그인 중인 IdP'가 Google에서 Facebook으로 변경되지는 않습니다. Google 상태로 유지됩니다.
Mapping은 단순히 IdP 연동만 추가 해줍니다.

* additionalInfo 파라미터 설정 방법

| keyname                                  | a use                                    | 값 종류                                     |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| GamebaseAuthProviderCredential.SHOW_LOADING_ANIMATION | API 호출이 끝날 때까지 로딩 애니메이션을 표시<br>**Android에 한함** | **bool**<br>**default**: true |
| GamebaseAuthProviderCredential.LINE_CHANNEL_REGION | LINE 서비스 제공 지역 설정 | [Login with IdP 참고](./unity-authentication-Login.md#login-with-idp) |

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static void AddMapping(string providerName, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback)
```

**Example**

```cs
public void AddMapping(string providerName)
{
    Gamebase.AddMapping(providerName, (authToken, error) =>
    {
        if (Gamebase.IsSuccess(error))
        {
            Debug.Log("AddMapping succeeded.");
        }
        else
        {
            Debug.Log(string.Format("AddMapping failed. error is {0}", error));
        }
    });
}
```

### AddMapping with Credential

게임에서 직접 IdP에서 제공하는 SDK로 먼저 인증을 하고 발급 받은 Access Token 등을 이용하여, Gamebase AddMapping을 할 수 있는 인터페이스입니다.

* Credential 파라미터의 설정 방법

| keyname | a use | 값 종류 |
| ---------------------------------------- | ------------------------------------ | ------------------------------ |
| GamebaseAuthProviderCredential.PROVIDER_NAME | IdP 유형 설정                           | google, gpgs_v2, facebook, payco, iosgamecenter, naver, twitter, line, appleid, steam, epicgames |
| GamebaseAuthProviderCredential.ACCESS_TOKEN | IdP 로그인 이후 받은 인증 정보(Access Token) 설정<br/>Google 인증 시에는 사용 안 함 |                                |
| GamebaseAuthProviderCredential.AUTHORIZATION_CODE | Google 로그인 이후 받은 인증 정보(Authorization Code) 설정 |                                          |
| GamebaseAuthProviderCredential.SHOW_LOADING_ANIMATION | API 호출이 끝날 때까지 로딩 애니메이션을 표시<br>**Android에 한함** | **bool**<br>**default**: true |
| GamebaseAuthProviderCredential.LINE_CHANNEL_REGION | LINE 서비스 제공 지역 설정 | [Login with IdP 참고](./unity-authentication-Login.md#login-with-idp) |

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
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static void AddMapping(Dictionary<string, object> credentialInfo, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback)
```

**Example**

```cs
public void AddMappingWithCredential()
{
    var credentialInfo = new Dictionary<string, object>();

    // facebook
    credentialInfo.Add(GamebaseAuthProviderCredential.PROVIDER_NAME, GamebaseAuthProvider.FACEBOOK);
    credentialInfo.Add(GamebaseAuthProviderCredential.ACCESS_TOKEN, "facebook access token");

    // google
    // credentialInfo.Add(GamebaseAuthProviderCredential.PROVIDER_NAME, GamebaseAuthProvider.GOOGLE);
    // credentialInfo.Add(GamebaseAuthProviderCredential.AUTHORIZATION_CODE, "google auchorization code");

    Gamebase.AddMapping(credentialInfo, (authToken, error) =>
    {
        if (Gamebase.IsSuccess(error))
        {
            Debug.Log("AddMapping succeeded.");
        }
        else
        {
            Debug.Log(string.Format("AddMapping failed. error is {0}", error));
        }
    });
}
```

### Add Mapping Forcibly
특정 IdP에 이미 매핑되어있는 계정이 있을 때, **강제로** 매핑을 시도합니다.
**강제 매핑**을 시도할 때는 AddMapping API에서 획득한 `ForcingMappingTicket`이 필요합니다.

다음은 Facebook에 강제 매핑을 시도하는 예시입니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static void AddMappingForcibly(GamebaseResponse.Auth.ForcingMappingTicket forcingMappingTicket, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback)
```

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

```cs
// Legacy API
static void AddMappingForcibly(string providerName, string forcingMappingKey, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback)
static void AddMappingForcibly(string providerName, string forcingMappingKey, Dictionary<string, object> additionalInfo, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback)
static void AddMappingForcibly(Dictionary<string, object> credentialInfo, string forcingMappingKey, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback)
```

**Example**

```cs
public void AddMappingForcibly(string idPName)
{
    Gamebase.AddMapping(idPName, (authToken, error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            // 매핑 추가 성공
        }
        else
        {
            // 우선 AddMapping API 호출 및 이미 연동되어 있는 계정으로 매핑을 시도하여, 다음과 같이 ForcingMappingTicket을 얻을 수 있습니다.
            if (error.code.Equals(GamebaseErrorCode.AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER) == true)
            {
                // ForcingMappingTicket 클래스의 From() 메소드를 이용하여 ForcingMappingTicket 인스턴스를 얻습니다.
                GamebaseResponse.Auth.ForcingMappingTicket forcingMappingTicket = GamebaseResponse.Auth.ForcingMappingTicket.From(error);

                // 강제 매핑을 시도합니다.
                Gamebase.AddMappingForcibly(forcingMappingTicket, (authTokenForcibly, errorForcibly) =>
                {
                    if (Gamebase.IsSuccess(error) == true)
                    {
                        // 강제 매핑 추가 성공
                    }
                    else
                    {
                        // 강제 매핑 추가 실패
                        // 오류 코드를 확인하고 적절한 처리를 진행합니다.
                    }
                });
            }
            else
            {
                // 오류 코드를 확인하고 적절한 처리를 진행합니다.
            }
        }
    });
}
```

### Change Login with ForcingMappingTicket

특정 IdP에 이미 매핑되어 있는 계정이 있을 때, 현재 계정을 로그아웃하고 이미 매핑되어 있던 해당 계정으로 로그인합니다.
이때, AddMapping API에서 획득한 `ForcingMappingTicket`이 필요합니다.

Change Login API 호출이 실패하는 경우, Gamebase 로그인 상태는 기존의 UserID로 유지됩니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static void ChangeLogin(GamebaseResponse.Auth.ForcingMappingTicket forcingMappingTicket, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Auth.AuthToken> callback)
```

**Example**

다음은 Facebook으로 매핑 시도 후 Facebook에 이미 매핑된 계정이 존재하자, 해당 계정으로 로그인을 변경하는 예시입니다.

```cs
public void ChangeLoginWithFacebook()
{
    Gamebase.AddMapping(GamebaseAuthProvider.FACEBOOK, (authToken, error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            // 매핑 추가 성공
            return;
        }
        
        // 우선 AddMapping API 호출 및, 이미 연동되어있는 계정으로 매핑을 시도하여, 다음과 같이, ForcingMappingTicket을 얻을 수 있습니다.
        if (error.code.Equals(GamebaseErrorCode.AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER) == true)
        {
            // ForcingMappingTicket 클래스의 From() 메소드를 이용하여 ForcingMappingTicket 인스턴스를 얻습니다.
            GamebaseResponse.Auth.ForcingMappingTicket forcingMappingTicket = GamebaseResponse.Auth.ForcingMappingTicket.From(error);

            // ForcingMappingTicket의 UserID로 로그인합니다.
            Gamebase.ChangeLogin(forcingMappingTicket, (authTokenForcibly, errorForcibly) =>
            {
                if (Gamebase.IsSuccess(errorForcibly) == true)
                {
                    // 로그인 변경 성공
                }
                else
                {
                    // 로그인 변경 실패
                    // 오류 코드를 확인하고 적절한 처리를 진행합니다.
                }
            });
        }
        else
        {
            // Add Mapping Failed.
            // 오류 코드를 확인하고 적절한 처리를 진행합니다.
        }
    });
}
```

### Remove Mapping

특정 IdP에 대한 연동을 해제합니다. 만약, 해제하고자 하는 IdP가 유일한 IdP라면, 실패를 반환합니다.
연동 해제후에는 Gamebase 내부에서, 해당 IdP에 대한 로그아웃처리를 해줍니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static void RemoveMapping(string providerName, GamebaseCallback.ErrorDelegate callback)
```

**Example**

```cs
public void RemoveMapping(string providerName)
{
    Gamebase.RemoveMapping(providerName, (error) =>
    {
        if (Gamebase.IsSuccess(error))
        {
            Debug.Log("RemoveMapping succeeded.");
        }
        else
        {
            Debug.Log(string.Format("RemoveMapping failed. error is {0}", error));
        }
    });
}
```

### Get Mapping List

사용자 ID에 연동되어 있는 IdP 목록을 반환합니다.<br/>

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#5319E7; font-size: 10pt">■</span> UNITY_WEBGL
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static List<string> GetAuthMappingList()
```

**Example**

```cs
public void GetAuthMappingList()
{
    List<string> mappingList = Gamebase.GetAuthMappingList();
}
```
