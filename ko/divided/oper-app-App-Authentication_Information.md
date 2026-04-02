## Game > Gamebase > 콘솔 사용 가이드 > 앱

### Authentication Information

#### 1. Facebook
Facebook 개발자 사이트에 등록한 앱의 {앱 아이디}와 {앱 시크릿 코드}를 Gamebase Console에 입력합니다.

**입력 필드**

- Client ID: {AppID}
- Secret Key: {App Secret Code}
- 추가정보: Facebook Permission & Facebook Client Token (json format)


![gamebase_app_18_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_18_ko_240105.png)
![gamebase_app_19_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_19_ko_240105.png)

##### Additional Info Settings
* **NHN Cloud Console > Gamebase > App > 인증 정보 > 추가 정보** 항목에 JSON string 형태의 정보를 설정해야 합니다.
* Facebook의 경우, OAuth 인증 시도 시 Facebook에 요청할 권한 정보인 **facebook_permission**과 **facebook_client_token**을 설정해야 합니다.
* Facebook 추가 인증 정보 입력 예제

        { "facebook_permission": ["public_profile", "email"], "facebook_client_token": "Your Facebook Client Token" }

![gamebase_app_20_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_20_ko_240105.png)

**Reference URL**<br />

- [Facebook 개발자 사이트](https://developers.facebook.com/)
- [Facebook 권한](https://developers.facebook.com/docs/facebook-login/permissions/)

##### Android
* [Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > Facebook IdP](./aos-started/#facebook-idp)

##### iOS
* [Gamebase > iOS SDK 사용 가이드 > 시작하기 > IdP Settings > Facebook](./ios-started/#facebook)

#### 2. Google

##### Google Cloud Console - Common

* Gamebase에서 Google 인증을 하기 위한 준비로 우선 **Google Cloud Console > APIs & Services > Credentials > + CREATE CREDENTIALS > OAuth client ID** 메뉴에서 **Web application** 유형의 Client id를 생성합니다.
    * 이미 생성된 Web application 유형의 Client id가 존재한다면 해당 Client id를 사용해도 됩니다.
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_001_en_20250122.png) 
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_002_en_20250122.png) 
* **승인된 리디렉션 URI** 란에는 다음 값을 입력해야 합니다. 
    * https://id-gamebase.toast.com/oauth/callback 
    * https://alpha-id-gamebase.toast.com/oauth/callback
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_003_en_20250122.png)
* 생성한 Client id 정보를 **NHN Cloud Console > Game > Gamebase > 앱 > 인증 정보 > Google > Client ID > Web Application ID** 란에 입력합니다. 
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_004_en_20250122.png)
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_012_en_20250122.png) 
* **NHN Cloud Console > Game > Gamebase > 앱 > 인증 정보 > Google > Secret Key** 란에는 Web application 유형의 Client secret을 입력합니다. 
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_013_en_20250122.png)

##### Google Cloud Console - Android

* Android 단말기에서 Google 인증을 하기 위해서는 Google Cloud Console에서 추가적으로 Android 유형의 Client id를 생성해야 합니다.
* **Google Cloud Console > APIs & Services > Credentials > + CREATE CREDENTIALS > OAuth client ID** 메뉴에서 **Android** 유형의 Client id를 생성합니다. 
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_005_en_20250122.png)
* Android 유형은 Package name과 SHA-1 서명 정보가 필요합니다.
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_006_en_20250122.png)
* Android 빌드는 업로드 서명과 앱 서명이 다르므로 두 종류의 SHA-1 값을 모두 등록해야 빌드 테스트가 원활하게 진행됩니다.
    * Firebase나 GPGS와 같은 일부 Google 플랫폼을 사용하는 경우 자동으로 Android 유형의 Client id 설정이 추가되는 경우도 있습니다.
    * ![all type created](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_007_en_20250122.png)
* 여기서 주의할 점은, Gamebase Console에는 Web application 유형의 Client id만 입력해야 하므로 Android 유형의 Client id는 입력하지 않아야 합니다.
    * ![](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_012_en_20250122.png)
* Google Credential Manager로 전환된 이후 버전(2.68.0)부터는 Google Cloud Console에서 아래와 같이 설정해야 합니다.
* **Google Cloud Console > Google 인증 플랫폼 > 대상** 메뉴에서 **사용자 유형**을 **외부**로, **게시 상태**를 **프로덕션 단계**로 설정합니다.
    * 이렇게 설정되지 않은 상태에서 로그인 시도 시 무조건 취소됩니다.
    * ![](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/DevelopersGuide/aos-google-oauth-setting-production-en.png)

##### Google Cloud Console - iOS
 
* iOS 단말기에서 Google 인증을 하기 위해서는 Google Cloud Console에서 추가적으로 iOS 유형의 Client id를 생성해야 합니다.  
* **Google Cloud Console > APIs & Services > Credentials > + CREATE CREDENTIALS > OAuth client ID** 메뉴에서 **iOS** 유형의 Client id를 생성합니다. 
    * ![ios 1](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_009_en_20250122.png)
* Bundle ID를 입력합니다.
    * ![ios 2](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_010_en_20250122.png)
* iOS는 Android와 다르게 **NHN Cloud Console > Game > Gamebase > 앱 > 인증 정보 > Google > Client ID > iOS Client ID** 란에 iOS 유형으로 발급 받은 Client id를 입력해야 합니다.
    * ![gamebase console](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_014_en_20250122.png)

##### Gamebase Console

![gamebase console](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/en/gamebase_console_app_google_008_en_20250122.png)

**입력 필드**<br />

- Web Application ID: {Google Web Application Client ID}
- iOS Client ID: {Google iOS Client ID}
- Secret Key: {Google Web Application Client secret}
- 추가정보: OAuth 2.0 Scopes (json format)

##### Additional Info Settings

* **NHN Cloud Console > Game > Gamebase > 앱 > 인증 정보 > 추가 정보** 항목에 JSON string 형태의 정보를 설정할 수 있습니다.
* Google의 경우 OAuth 인증 후 프로필 정보에서 email 정보를 획득하려면 인증 권한 범위인 **scope**를 설정해야 합니다.
* email 외에 선언할 수 있는 다양한 scope는 다음 문서에서 확인할 수 있습니다.
    * https://developers.google.com/identity/protocols/oauth2/scopes#google-sign-in
    * https://developers.google.com/identity/protocols/oauth2/scopes
* Google 추가 인증 정보 입력 예제

        { "scope": ["email","myscope1","myscope2",...] }

##### iOS

* [Gamebase > iOS SDK 사용 가이드 > 시작하기 > IdP Settings > Google](./ios-started/#google)

#### 3. Apple Game Center
Apple 개발자 사이트에 등록된 BundleID를 Gamebase Console에 입력합니다.

**입력 필드**<br />

- Client ID: {Bundle ID}<br />

![gamebase_app_08_201812.png](https://static.toastoven.net/prod_gamebase/gamebase_app_08_201812.png)

**Reference URL**<br />

- [Apple Developer 사이트](https://developer.apple.com/)
- [Apple iTunes Connect](https://itunesconnect.apple.com/)


#### 4. PAYCO
PAYCO Client ID를 신청해서 발급 받은 {client_id} 및 {client_secret}을 Gamebase Console에 입력합니다.

**입력 필드**<br />

- Client ID: {PAYCO client_id}
- Secret Key: {PAYCO client_secret}
- 추가정보: PAYCO Service Code & Service Name (JSON format)

##### Additional Info Settings

* **NHN Cloud Console > Gamebase > App > 인증 정보 > 추가 정보** 항목에 JSON string 형태의 정보를 설정해야 합니다.
* PAYCO의 경우, PAYCO SDK에서 요구하는 **service_code**와 **service_name**을 설정해야 합니다.
* PAYCO 추가 인증 정보 입력 예제

        { "service_code": "Your Service Code", "service_name": "Your Service Name" }

##### iOS
* [Gamebase > iOS SDK 사용 가이드 > 시작하기 > IdP settings > PAYCO](./ios-started/#payco)

#### 5. NAVER
NAVER Developers 사이트에서 신청하여 발급 받은 {client_id} 및 {client_secret}을 Gamebase Console에 입력합니다.
이때, 로그인 동의 창에서 표시할 애플리케이션 이름인 **service_name**을 설정해야 합니다.

**입력 필드**

- Client ID: {NAVER client_id}
- Secret Key: {NAVER client_secret}
- 추가정보: NAVER Application Name (json format)

**Reference URL**

- [NAVER Developers - 애플리케이션 등록](https://developers.naver.com/apps/#/register)
- [NAVER Developers - 클라이언트 아이디와 클라이언트 시크릿 확인](https://developers.naver.com/docs/common/openapiguide/#/appregister.md)

##### Additional Info Settings

* **NHN Cloud Console > Gamebase > App > 인증 정보 > 추가 정보 & Callback URL**의 **추가 정보** 항목에 JSON String 형태의 정보를 설정해야 합니다.
* NAVER의 경우, 로그인 동의 창에 표시할 앱 이름인 **service_name**을 설정해야 합니다.
* 또한 NAVER Login SDK는 로그아웃 후에도 자동으로 로그인이 되어 계정을 변경할 수 없는데, 로그아웃 후 다른 NAVER 계정으로 로그인하려면 **logout_and_delete_token**을 **true**로 설정해야 합니다.

* NAVER 추가 인증 정보 입력 예제

        { "service_name": "Your Service Name", "logout_and_delete_token": true }

##### iOS
* [Gamebase > iOS SDK 사용 가이드 > 시작하기 > IdP settings > Naver](./ios-started/#naver)

#### 6. Twitter

##### Developer Portal

![gamebase_app_twitter_02_ko_241024](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/en/gamebase_app_twitter_02_en_241024.png)

![gamebase_app_twitter_03_ko_241024](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/en/gamebase_app_twitter_03_en_241024.png)

Twitter 인증을 위해서는 Developer Portal에서 Callback URI란에 다음 값을 입력합니다.
* https://id-gamebase.toast.com/oauth/callback

<br/>

##### Gamebase Console

Developer Portal에서 앱을 등록하고 **OAuth 2.0 Client ID와 Client Secret**을 발급 받아 Gamebase Console에 입력합니다.

**입력 필드**

- Client ID: {OAuth 2.0 Client ID}
- Secret Key: {OAuth 2.0 Client Secret}

![gamebase_app_twitter_01_ko_241024](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/en/gamebase_app_twitter_01_en_241024.png)

**Reference URL**
- [Twitter Application Management](https://developer.x.com/)

<br/>

##### Android
 > <font color="red">[주의]</font><br/>
 >
 > 2019년 7월 25일부로 Twitter에서는 TLS 1.0, TLS 1.1 지원을 중단하고, TLS1.2만 지원합니다.
 > 이에, Android 4.3(Jelly Bean, API Level 18) 이하의 단말기에서는 Android 웹뷰로 Twitter에 로그인할 수 없습니다.
 >
 > 즉, Android 4.4 이상(KitKat, API Level 19)인 기기에서만 Twitter 로그인을 사용할 수 있습니다.

#### 7. LINE

**입력 필드**

- Region: {LINE Channel Region}
- Client ID: {LINE Channel ID}
- Secret Key: {LINE Channel Secret}

**Reference URL**

- [LINE Developer Console](https://developers.line.me/console/)

##### iOS
* [Gamebase > iOS SDK 사용 가이드 > 시작하기 > IdP settings > LINE](./ios-started/#line)

#### 8. Sign In with Apple
Sign In with Apple 기능을 사용하려면 App Store Connect, Gamebase 콘솔, Xcode에 설정이 필요합니다.

##### AppStore Connect Settings
* [Certificates, Identifiers & Profiles \> Keys 로 바로가기](https://developer.apple.com/account/resources/authkeys/list)

###### Certificates, Identifiers & Profiles > Keys > 추가(+)
1. **Sign In with Apple** 체크 박스를 선택하고 설정을 진행합니다.
![Check SignInWithApple](http://static.toastoven.net/prod_gamebase/Operators_Guide/Console_App_Auth_appleid0_1.0.png)
2. **Sign in with Apple**을 사용할 Bundle ID를 선택합니다.
![ChooseAPrimaryAppID](http://static.toastoven.net/prod_gamebase/Operators_Guide/Console_App_Auth_appleid1_1.0.png)
3. <span style="color:#e11d21">Privatekey</span>를 다운로드 후 보관, 생성된 <span style="color:#e11d21">Key ID를 </span>확인합니다.
![DownloadPrivateKey](http://static.toastoven.net/prod_gamebase/Operators_Guide/Console_App_Auth_appleid2_1.0.png)
4. Certificates, Identifiers & Profiles > Identifiers > 대상 앱을 선택하고 **Sign In with Apple**을 활성화합니다.
    * `Enable as a primary App ID` 로 설정합니다.
![DownloadPrivateKey](http://static.toastoven.net/prod_gamebase/Operators_Guide/Console_App_Auth_appleid3_1.0.png)

##### Gamebase Console > App Settings
[NHN Cloud Console 바로가기](https://console.toast.com/)

* Gamebase
![SecretKey설정](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_22_ko_240105.png)


###### Client ID Settings
> 앱의 Bundle ID를 설정합니다.

###### Secret Key Settings
> Apple Developer Account 설정에서 획득한 값(**TeamID**, **KeyID**, **PrivateKey**)으로 JSON 문자열을 생성해 설정합니다.

* **teamId**: 개발자 계정 오른쪽 상단의 값을 설정합니다.
* **keyId**: Certificates, Identifiers & Profiles > Keys > Sign In with Apple을 선택하여 생성된 값을 설정합니다.
![SecretKey설정](http://static.toastoven.net/prod_gamebase/Operators_Guide/Console_App_Auth_appleid5_1.0.png)
* **privateKey**: 위의 Keys에서 키를 생성하면서 같이 생성된 PrivateKey 파일의 내용을 설정합니다. 다운로드한 파일을 열어서 아래 그림과 같이 빨간 사각형 부분의 값을 사용합니다.
![SecretKey설정](http://static.toastoven.net/prod_gamebase/Operators_Guide/Console_App_Auth_appleid7_1.0.png)

위의 값을 아래의 예제와 같이 JSON으로 만들어서 설정합니다.


```json
{
    "teamId":"2UH5Cxxxx",
    "keyId":"3C3FXYxxxx",
    "privateKey":"MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBA.. 중략"
}
```

> <font color="red">[주의]</font><br/>
>
> privateKey에 개행이 들어가지 않도록 주의해 주세요.

###### Additional Info Settings
[Sign In with Apple 의 AuthorizationScope 알아보기](https://developer.apple.com/documentation/authenticationservices/asauthorizationscope?language=occ)

Gamebase 콘솔 **App**에서 Apple을 추가하면 기본으로 아래의 JSON 값이 설정됩니다.
2019년 11월 기준으로 Scope의 종류는 `full_name`, `email`만 있으며, Gamebase에서는 이 두 가지 값을 기본값으로 설정합니다.

```json
{ "authorization_scope":["full_name", "email"] }
```

##### Xcode Project Settings
> <font color="red">[주의]</font><br/>
>
> Xcode 11 이상에서만 **Sign In with Apple** 기능을 사용하는 프로젝트를 빌드할 수 있습니다.


1. **Target**을 선택하고 **Signing & Capabilities**에서 **Sign In with Apple** 항목을 추가합니다.
![Capability_SignInWithApple](http://static.toastoven.net/prod_gamebase/Operators_Guide/Console_App_Auth_appleid8_1.0.png)
2. **Target**을 선택하고 **Build Phases > Link Binary With Libraries**에서 **Authentication.framework**를 **Optional**로 추가합니다.
![AuthenticationServices.framework](http://static.toastoven.net/prod_gamebase/Operators_Guide/Console_App_Auth_appleid9_1.0.png)

> <font color="red">[주의]</font><br/>
> Optional이 아닌 Required로 설정되어 있으면 iOS 12 이하의 단말기에서는 앱 실행 시 런타임 크래시가 발생합니다.





##### iOS 12 버전 이하를 지원하기 위한 설정 (Sign In with Apple JS)

> <font color="red">[주의]</font><br/>
>
> Gamebase SDK iOS 2.13.0 이상 버전에서는 iOS 12 이하 버전에서의 웹뷰를 이용한 Sign In with Apple 기능 사용이 가능합니다.
>
> 기존의 2.13.0 이전버전을 사용했던 게임의 경우에도 하단 **iOS 12 버전 이하를 지원하기 위한 설정** 을 참고하여 기존 프로젝트를 설정하고,
>
> Gambase SDK iOS 2.13.0 이상을 적용하면, iOS 12 이하버전에서 Sign In with Apple 기능을 사용할 수 있습니다.


* iOS 12 이하 버전에서 Sign In with Apple 을 사용하기 위해서는 Sign In with Apple JS 를 사용해서, 웹페이지를 통해 로그인을 해야합니다.
* Apple ID 로그인 웹페이지에서는 Apple 계정과 비밀번호를 입력해서 로그인을 할 수 있습니다.

**아래의 절차를 따라서 Apple 개발자 사이트에서 새로운 Service ID 를 등록해야 합니다.**

1. Service ID 를 추가<br/>
![Create new Service ID](https://static.toastoven.net/prod_gamebase/Operators_Guide/gamebase_SignInWithAppleJS_AppStore_01.png)
2. Service ID 로 사용할 식별자를 설정 (일반적으로는 bundle ID + **.구분할 문자열**)<br/>
![Create new Service ID](https://static.toastoven.net/prod_gamebase/Operators_Guide/gamebase_SignInWithAppleJS_AppStore_02.png)
3. 등록된 Service ID 를 확인 후 수정<br/>
![Create new Service ID](https://static.toastoven.net/prod_gamebase/Operators_Guide/gamebase_SignInWithAppleJS_AppStore_03.png)
4. 하단의 Sign In with Apple 항목의 Configure 를 클릭<br/>
![Create new Service ID](https://static.toastoven.net/prod_gamebase/Operators_Guide/gamebase_SignInWithAppleJS_AppStore_04.png)
5. Primary App ID 를 설정 (기존에 Sign In with Apple 을 사용하고 있었다면, 해당앱의 Bundle ID 를 설정)<br/>
![Create new Service ID](https://static.toastoven.net/prod_gamebase/Operators_Guide/gamebase_SignInWithAppleJS_AppStore_05.png)
6. Apple ID 로 인증한 이후 인증 정보를 받을 Callback URL 설정<br/>
![Create new Service ID](https://static.toastoven.net/prod_gamebase/Operators_Guide/gamebase_SignInWithAppleJS_AppStore_06.png)
7. 설정 후 저장<br/>
![Create new Service ID](https://static.toastoven.net/prod_gamebase/Operators_Guide/gamebase_SignInWithAppleJS_AppStore_07.png)


**위에서 설정한 Service ID 를 NHN Cloud Gamebase Console > Gamebase > 앱 > 인증 정보 > Apple > Service ID 에 입력합니다.***

> <font color="red">[주의]</font><br/>
>
> 기존에 Sign In with Apple 설정이 되어 있지 않다면, 나머지 항목도 설정이 필요합니다.

1. Apple 개발자 사이트에서 설정한 Service ID 를 아래와 같이 Service ID 항목에 추가합니다. (기존에 Sign In with Apple 설정값이 있다면, 다른 값들은 변경이 필요없습니다.)
![Set Service ID for Sign In with Apple JS](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_23_ko_240105.png)


#### 9. WEIBO

##### Weibo Console

1. Weibo Developers 사이트에서 신청하여 발급 받은 {client_id} 및 {client_secret}을 Gamebase Console에 입력합니다.
이때, 로그인 시 필요한 {scope} 또한 JSON String 형태로 추가 정보란에 입력해야 합니다.


![gamebase_app_29_202012.png](https://static.toastoven.net/prod_gamebase/Operators_Guide/gamebase_app_29_202012.png)

2. callback URL 란에 다음 값을 입력합니다.
	* Authorization callback page: https://api.weibo.com/oauth2/default.html
	* Cancel authorization callback page: https://api.weibo.com/oauth2/default.html


**입력 필드**

- Client ID: {App Key}
- Secret Key: {App Secret}
- 추가 정보: scope(json format)


**Additional Info Settings**

* Scope

Application 에서 필요로 하는 권한을 나타냅니다.
Weibo 가이드 문서에 따라 기본값으로 모든 권한이 선언되어 있습니다.
필요에 따라 추가/제거/변경하실 수 있습니다.

* oauthApiUrl

내부적으로 Weibo Open API를 호출하기 위한 도메인입니다.
변경해서는 안됩니다.

* universalLink

Weibo 가이드 문서에 따라 universalLink를 설정할 수 있습니다.
입력하지 않으면 임의의 값으로 설정됩니다.

![gamebase_app_24_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_24_ko_240105.png)


**Reference URL**
- [Weibo Developer](https://open.weibo.com/)

#### 10. Kakaogames

Kakao 인증 정보는 퍼블리싱 계약 관계에 따라 카카오 디벨로퍼스, 카카오 게임센터(채널링 게임), 카카오게임 3.0 어드민 등 다양한 곳에서 설정/확인이 가능합니다.

* 카카오 디벨로퍼스(https://developers.kakao.com/)
    * ![gamebase_console_app_kakaogames_01_20240723.png](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/ko/gamebase_console_app_kakaogames_01_20240723.png)
* 카카오 게임센터(https://gamecenter.kakao.com/)
    * ![gamebase_console_app_kakaogames_02_20240723.png](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/ko/gamebase_console_app_kakaogames_02_20240723.png)
* 카카오게임 3.0 어드민(https://admin-zinny3.game.kakao.com)
    * ![gamebase_console_app_kakaogames_03_20240723.png](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/ko/gamebase_console_app_kakaogames_03_20240723.png)

<br />
Kakaogames에서 발급 받은 {App ID}, {Native App Key} 및 {Admin Key}를 Gamebase Console에 입력합니다.
![gamebase_console_app_kakaogames_04_20240723.png](https://static.toastoven.net/prod_gamebase/ConsoleGuide/App/ko/gamebase_console_app_kakaogames_04_20240723.png)

##### Client ID Settings
App ID를 설정합니다.

##### Secret Key Settings
Gamebase 인증 정보로 Kakaogames를 추가하면 'Secret Key'에 아래의 JSON 값이 설정됩니다.
각각의 값을 Kakaogames 콘솔에서 발급 받은 값으로 변경하세요.

* **appSecret**: Native App Key
* **adminKey**: Admin Key

```json
{
    "appSecret":"...",
    "adminKey":"..."
}
```

##### Additional Info Settings
Gamebase 인증 정보로 Kakaogames를 추가하면 '추가 정보'에 아래의 JSON 값이 설정됩니다.
Unity 빌드인 경우 **AppDelegate**를 **UnityAppController**로 변경하세요.

```json
{"AppDelegateClassName" : "AppDelegate"}
```

#### 11. GPGS v2

GPGS(Google Play Games Services) v2 인증을 위해서는 Google 인증 타입 추가 방법과 동일하게 Google Cloud Console에서 **Web Application Client ID**를 발급 받고 승인된 리디렉션 URI란에 Gamebase Callback URL을 입력해야 합니다.
[Game > Gamebase > 콘솔 사용 가이드 > 앱 > App > Authentication Information > 2. Google](./oper-app/#2-google)

**입력 필드**

- Client ID: {Google Web Application Client ID}
- Secret Key: {Google Web Application Client secret}

##### Android
* [Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > GPGS v2 IdP](./aos-started/#gpgs-v2-idp)

#### 12. Steam

Steam 인증을 위해 Steamworks에서 **App ID**와 **Web API**를 발급 받아 Gamebase Console에 입력해야 합니다.

**입력 필드**

- Client ID: {App ID}
- Secret Key: {Web API}

![gamebase_app_steam_01_en_241025.png](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/en/gamebase_app_steam_01_en_241025.png)

![gamebase_app_steam_02_en_241025.png](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/en/gamebase_app_steam_02_en_241025.png)

#### 13. Epic Games
[Epic Games Dev Portal](https://dev.epicgames.com/portal)에서 발급 받은 {Client ID} 및 {Client Secret}을 Gamebase Console에 입력합니다.
이때, 디플로이 ID와 인증 시 필요한 {scope}를 JSON String 형태로 추가 정보란에 입력해야 합니다.

1. **제품 설정 > 샌드박스** 메뉴에서 디플로이를 생성합니다.
2. **제품 설정 > 클라이언트** 메뉴에서 클라이언트를 생성합니다.
3. **제품 설정 > SDK 다운로드 및 크리덴셜** 메뉴에서 **Client ID**, **Client Secret**, **Deployment ID**를 확인합니다.

> [참고]
>
> 디플로이 및 클라이언트 생성에 대한 자세한 내용은 다음 문서를 참고하시기 바랍니다.
> [Game > Gamebase > 스토어 콘솔 가이드 > Epic Games Store 콘솔 가이드](./console-epicgames-guide)

**입력 필드**

- Client ID: {Client ID}
- Secret Key: {Client Secret}
- 추가정보: deployment_id, scope (json format)

![에픽 앱 정보](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_iap/console_epic/epic_console_app_03_kor.png)

**Reference URL**

- [Epic Games Dev Portal](https://dev.epicgames.com/portal)
- [Epic Online Services 문서](https://dev.epicgames.com/docs/epic-online-services)

##### Additional Info Settings

* **NHN Cloud Console > Gamebase > App > 인증 정보 > 추가 정보** 항목에 JSON string 형태의 정보를 설정해야 합니다.
* Epic Games의 경우, **제품 설정 > SDK 다운로드 및 크리덴셜 > EOS SDK 크리덴셜 > 디플로이**에서 확인한 **deployment_id**와 OAuth 인증 시 요청할 권한 범위인 **scope**를 설정해야 합니다.
* **deployment_id**는 EOS(Epic Online Services) 서비스 환경을 식별하기 위해 반드시 설정해야 합니다.
* **scope**는 인증 시 사용자의 프로필, 친구 목록, 접속 상태 등의 정보를 획득하기 위해 설정합니다.
* 인증 시 요청 가능한 scope는 다음 문서에서 확인할 수 있습니다.
    * https://dev.epicgames.com/docs/web-api-ref/authentication#requesting-an-access-token
* Epic Games 추가 인증 정보 입력 예제

        { "deployment_id": "Your Deployment ID", "scope": ["basic_profile", "friends_list", "presence"] }
