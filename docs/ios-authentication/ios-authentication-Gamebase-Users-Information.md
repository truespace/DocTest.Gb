---
source: ios-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, IdP, loginForLastLoggedInProvider, loginWithType, loginForLastLoggedInProviderWithViewController"
section: "Gamebase User's Information"
order: 5
---

## Gamebase User's Information
Gamebase로 인증 절차를 진행한 후, 앱을 제작할 때 필요한 정보를 얻을 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> "[TCGBGamebase loginForLastLoggedInProvider]" API로 로그인한 경우에는 인증 정보를 가져올 수 없습니다.
>
> 인증 정보가 필요하다면 "[TCGBGamebase loginForLastLoggedInProvider]" 대신, 사용하고자 하는 IDPCode 와 동일한 {IDP_CODE} 를 파라미터로 하여 "[TCGBGamebase loginWithType:IDP_CODE viewController:topViewController completion:completion];" API로 로그인 해야 정상적으로 인증정보를 획득할 수 있습니다.

### Get Authentication Information for Gamebase
Gamebase에서 발급한 인증 정보를 가져올 수 있습니다.

```objectivec
// Obtaining Gamebase UserID
NSString* gamebaseUserID = [TCGBGamebase userID];

// Obtaining Gamebase AccessToken
NSString* gamebaseAccessToken = [TCGBGamebase accessToken];

// Obtaining Last Logged In Provider
NSString* lastProviderName = [TCGBGamebase lastLoggedInProvider];
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
> * "[TCGBGamebase loginForLastLoggedInProviderWithViewController:completion:]" API로 로그인한 경우에는 인증 정보를 가져올 수 없습니다.
>     * 사용자 정보가 필요하다면 "[TCGBGamebase loginForLastLoggedInProviderWithViewController:completion:]" 대신, 사용하고자 하는 IDPCode와 동일한 {IDP_CODE}를 파라미터로 하여 "[TCGBGamebase loginWithType:viewController:completion:]" API로 로그인 해야 합니다.

> <font color="red">[주의]</font><br/>
>
> iOS 12 이하 appleid 로그인의 경우 인증 정보를 조회할 수 없습니다.
>

### Get Banned User Information

Gamebase Console에 제재된 게임 유저로 등록될 경우,
로그인을 시도하면 아래와 같은 이용 제한 정보 코드가 표시될 수 있습니다. **[TCGBBanInfo banInfoFromError:error]** 메서드를 이용해 제재 정보를 확인할 수 있습니다.

* TCGB_ERROR_BANNED_MEMBER
