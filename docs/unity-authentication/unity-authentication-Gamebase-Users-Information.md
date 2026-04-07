---
source: unity-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, Login, IdP, GetLastLoggedInProvider, GetUserID, GetAccessToken, RequestLastLoggedInProvider, LoginForLastLoggedInProvider, IsSuccess"
section: "Gamebase User's Information"
order: 5
---

## Gamebase User's Information

Gamebase를 통하여 인증절차를 진행 후, 앱을 제작할 때 필요한 정보를 획득할 수 있습니다.

### Get Authentication Information for Gamebase
Gamebase를 통하여 인증절차를 진행 후, 앱을 제작할 때 필요한 정보를 획득할 수 있습니다.

#### UserID

Gamebase에서 발급한 UserID를 가져올 수 있습니다.
**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#5319E7; font-size: 10pt">■</span> UNITY_WEBGL
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static string GetUserID()
```

**Example**
```cs
public void GetUserID()
{
    string userID = Gamebase.GetUserID();
}
```

#### AccessToken

Gamebase에서 발급한 Access Token을 가져올 수 있습니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#5319E7; font-size: 10pt">■</span> UNITY_WEBGL
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static string GetAccessToken()
```

**Example**
```cs
public void GetAccessToken()
{
    string accessToken = Gamebase.GetAccessToken();
}
```

#### Last LoggedIn Provider Name

Gamebase에서 마지막 로그인에 성공한 ProviderName을 가져올 수 있습니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

```cs
static string RequestLastLoggedInProvider()
static string GetLastLoggedInProvider()
```

**Example**
```cs
public void GetLastLoggedInProvider()
{
    // Obtaining Last Logged In Provider - Sync
    string lastLoggedInProviderSync = Gamebase.GetLastLoggedInProvider();
    
    // Obtaining Last Logged In Provider - Async
    // If Gamebase.GetLastLoggedInProvider() returns 'NOT_INITIALIZED_YET',
    // use the following async function instead:
    Gamebase.RequestLastLoggedInProvider(lastLoggedInProviderAsync, error)=> 
    {
        if (Gamebase.IsSuccess(error) == true) 
        {
            Debug.Log(string.Format("lastLoggedInProvider:{0}", lastLoggedInProviderAsync));
        }
    });
}
```

### Get Authentication Information for External IdP

* 외부 인증 IdP의 Access Token, 사용자 ID, Profile 등의 정보는 로그인 후 게임 서버에서 Gamebase Server API를 호출하여 가져올 수 있습니다.
    * [Game > Gamebase > API 가이드 > Authentication > Get IdP Token and Profiles](../../api-guide.md#get-idp-token-and-profiles)

> <font color="red">[주의]</font><br/>
>
> * 외부 IdP의 인증 정보는 보안을 위해 게임 서버에서 호출할 것을 권장합니다.
> * IdP에 따라 Access Token이 빠른 시간에 만료될 수 있습니다.
>     * 예를 들어 Google은 로그인 2시간 후에는 Access Token이 만료되어 버립니다.
>     * 사용자 정보가 필요하다면 로그인 후 바로 Gamebase Server API를 호출하시기 바랍니다.
> * "Gamebase.LoginForLastLoggedInProvider()" API로 로그인한 경우에는 인증 정보를 가져올 수 없습니다.
>     * 사용자 정보가 필요하다면 "Gamebase.LoginForLastLoggedInProvider()" 대신, 사용하고자 하는 IDPCode와 동일한 {IDP_CODE}를 파라미터로 하여 "Gamebase.Login(IDP_CODE, callback)" API로 로그인 해야 합니다.

### Get Banned User Information

Gamebase Console에 제재된 게임 유저로 등록될 경우,
로그인을 시도하면 아래와 같은 이용 제한 정보 코드가 표시될 수 있습니다. **GamebaseResponse.Auth.BanInfo.from(GamebaseError error)** 메서드를 이용해 제재 정보를 확인할 수 있습니다.

* BANNED_MEMBER(7)
