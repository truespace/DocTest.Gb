---
source: aos-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "Gamebase User's Information, Get Authentication Information for Gamebase, Get Authentication Information for External IdP, Get Banned User Information"
section: "Gamebase User's Information"
order: 5
---

## Gamebase User's Information
Gamebase로 인증 절차를 진행한 후, 앱을 제작할 때 필요한 정보를 얻을 수 있습니다.

### Get Authentication Information for Gamebase
Gamebase에서 발급한 인증 정보를 가져올 수 있습니다.

**API**

```java
+ (String)Gamebase.getUserID();
+ (String)Gamebase.getAccessToken();
+ (String)Gamebase.getLastLoggedInProvider();
+ (String)Gamebase.requestLastLoggedInProvider(GamebaseDataCallback<String> callback);
```

**Example**

```java

// Obtaining Gamebase UserID
String userId = Gamebase.getUserID();

// Obtaining Gamebase AccessToken
String accessToken = Gamebase.getAccessToken();

// Obtaining Last Logged In Provider - Sync
String lastLoggedInProvider = Gamebase.getLastLoggedInProvider();

// Obtaining Last Logged In Provider - Async
// If Gamebase.getLastLoggedInProvider() returns 'NOT_INITIALIZED_YET',
// use the following async function instead:
Gamebase.requestLastLoggedInProvider((lastLoggedInProvider, exception) -> ...);
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
> * "Gamebase.loginForLastLoggedInProvider()" API로 로그인한 경우에는 인증 정보를 가져올 수 없습니다.
>     * 사용자 정보가 필요하다면 "Gamebase.loginForLastLoggedInProvider()" 대신, 사용하고자 하는 IDPCode와 동일한 {IDP_CODE}를 파라미터로 하여 "Gamebase.login(activity, IDP_CODE, callback)" API로 로그인 해야 합니다.

### Get Banned User Information

Gamebase Console에 제재된 게임 유저로 등록될 경우,
로그인을 시도하면 아래와 같은 이용 제한 정보 코드가 표시될 수 있습니다. **BanInfo.from(exception)** 메서드를 이용해 제재 정보를 확인할 수 있습니다.

* BANNED_MEMBER(7)
