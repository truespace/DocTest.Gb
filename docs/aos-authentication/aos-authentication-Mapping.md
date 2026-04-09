---
source: aos-authentication.md
section: "Mapping"
order: 4
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Logout, Mapping, Authentication, Error
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
<!-- LLM_Image_DESC_20260408_185735
    유형: Flowchart
    내용: 계정 매핑 추가 흐름도
    구성: 기존 계정에 새로운 IdP를 매핑하는 처리 흐름을 나타내는 순서도
    Keyword: Flowchart, Add Mapping Flow
-->

#### 1. 로그인

매핑은 현재 계정에 IdP 계정 연동을 추가하는 것이므로 우선 로그인이 돼 있어야 합니다.
먼저 로그인 API를 호출해 로그인합니다.

#### 2. 매핑

**Gamebase.addMapping(activity, idpType, callback)**을 호출해 매핑을 시도합니다.

#### 2-1. 매핑이 성공한 경우

* 축하합니다! 현재 계정과 연동중인 IdP 계정이 추가되었습니다.
* 매핑에 성공해도 '현재 로그인 중인 IdP'가 바뀌지는 않습니다. 즉, Google 계정으로 로그인한 후, Facebook 계정 매핑 시도가 성공했다고 해서 '현재 로그인 중인 IdP'가 Google에서 Facebook으로 변경되지는 않습니다. Google 상태로 유지됩니다.
    * <font color="red">[주의]</font> : Guest 계정은 예외입니다. Guest 계정으로 로그인한 상태에서 시도한 매핑이 성공했다면 Guest IdP는 **삭제**되고 '현재 로그인 중인 IdP'도 매핑된 IdP로 변경됩니다.
* 매핑은 단순히 IdP 연동만 추가해 줍니다.

#### 2-2. 매핑이 실패한 경우

* 네트워크 오류
    * 오류 코드가 **SOCKET_ERROR(110)** 또는 **SOCKET_RESPONSE_TIMEOUT(101)**인 경우, 일시적인 네트워크 문제로 인증이 실패한 것이므로 **Gamebase.addMapping()**을 다시 호출하거나, 잠시 대기했다가 재시도 합니다.
* 이미 다른 계정에 연동 중일 때 발생하는 오류
    * 오류 코드가 **AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302)**인 경우, 매핑하려는 IdP의 계정이 이미 다른 계정에 연동 중이라는 뜻입니다. 이때 획득한 **ForcingMappingTicket**으로 강제 매핑(**Gamebase.AddMappingForcibly()**)이나 로그인 계정 변경(**Gamebase.ChangeLogin()**)을 시도할 수 있습니다.
* 이미 동일한 IdP 계정에 연동돼 발생하는 오류
    * 오류 코드가 **AUTH_ADD_MAPPING_ALREADY_HAS_SAME_IDP(3303)**인 경우 매핑하려는 IdP와 같은 종류의 계정이 이미 연동 중이라는 뜻입니다.
        * Gamebase 매핑은 한 IdP당 하나의 계정만 연동 가능합니다. 예를 들어 PAYCO 계정에 이미 연동 중이라면 더 이상 PAYCO 계정을 추가할 수 없습니다.
        * 동일 IdP의 다른 계정을 연동하기 위해서는 **Gamebase.removeMapping()**을 호출해 연동을 해제한 후 다시 매핑을 시도하세요.
* 그 외의 오류
    * 매핑 시도가 실패했습니다.

### Add Mapping

특정 IdP에 로그인된 상태에서 다른 IdP로 매핑을 시도합니다.<br/>

* AdditionalInfo 파라미터 설정 방법

| keyname                                  | a use                                    | 값 종류                                     |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| AuthProviderCredentialConstants.SHOW_LOADING_ANIMATION | API 호출이 끝날 때까지 로딩 애니메이션을 표시 | **boolean**<br>**default**: true |
| AuthProviderCredentialConstants.LINE_CHANNEL_REGION | LINE 서비스 제공 지역 설정 | [Login with IdP 참고](./aos-authentication-Login.md#login-with-idp) |

다음은 Facebook에 매핑을 시도하는 예시입니다.

**API**

```java
+ (void)Gamebase.addMapping(Activity activity, String providerName, GamebaseDataCallback<AuthToken> callback);
+ (void)Gamebase.addMapping(Activity activity, String providerName, Map<String, Object> additionalInfo, GamebaseDataCallback<AuthToken> callback);
```

**Example**

```java
private static void addMappingForFacebook(final Activity activity) {
    String mappingProvider = AuthProvider.FACEBOOK;
    Gamebase.addMapping(activity, mappingProvider, new GamebaseDataCallback<AuthToken>() {
        @Override
        public void onCallback(AuthToken result, GamebaseException exception) {
            if (Gamebase.isSuccess(exception)) {
                // 매핑 추가 성공
                Log.d(TAG, "Add Mapping successful");
                String userId = Gamebase.getUserID();
                return;
            }

            // 매핑 추가 실패
            if (exception.getCode() == GamebaseError.SOCKET_ERROR ||
                    exception.getCode() == GamebaseError.SOCKET_RESPONSE_TIMEOUT) {
                // Socket error 로 일시적인 네트워크 접속 불가 상태임을 의미합니다.
                // 네트워크 상태를 확인하거나 잠시 대기 후 재시도 하세요.
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            Thread.sleep(2000);
                            addMappingForFacebook(activity);
                        } catch (InterruptedException e) {}
                    }
                }).start();
            } else if (exception.getCode() == GamebaseError.AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER) {
                // Mapping을 시도하는 IdP계정이 이미 다른 계정에 연동되어 있습니다.
                // 강제로 연동을 해제하기 위해서는 해당 계정의 탈퇴나 Mapping 해제를 하거나, 다음과 같이
                // ForcingMappingTicket을 획득 후, addMappingForcibly() 메소드를 이용하여 강제 매핑을 시도합니다.
                Log.e(TAG, "Add Mapping failed- ALREADY_MAPPED_TO_OTHER_MEMBER");
                final ForcingMappingTicket forcingMappingTicket = ForcingMappingTicket.from(exception);
                Gamebase.addMappingForcibly(activity, forcingMappingTicket, new GamebaseDataCallback<AuthToken>() {
                    @Override
                    public void onCallback(AuthToken data, GamebaseException exception) {
                        ...
                        // 자세한 내용은 addMappingForcibly API 문서를 참고하세요.
                    }
                }
            } else if (exception.getCode() == GamebaseError.AUTH_ADD_MAPPING_ALREADY_HAS_SAME_IDP) {
                // Mapping을 시도하는 IdP의 계정이 이미 추가되어 있습니다.
                // Gamebase Mapping은 한 IdP당 하나의 계정만 연동 가능합니다.
                // IdP 계정을 변경하려면 이미 연동중인 계정은 Mapping 해제를 해야 합니다.
                Log.e(TAG, "Add Mapping failed- ALREADY_HAS_SAME_IDP");
            } else {
                // 매핑 추가 실패
                Log.e(TAG, "Add Mapping failed- "
                        + "errorCode: " + exception.getCode()
                        + "errorMessage: " + exception.getMessage());
            }
        }
    });
}
```

### Add Mapping with Credential

게임에서 직접 IdP에서 제공하는 SDK로 먼저 인증하고 발급 받은 Access Token 등을 이용하여, Gamebase AddMapping을 할 수 있는 인터페이스입니다.

* Credential 파라미터 설정방법

| keyname                                  | a use                                    | 값 종류                                     |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| AuthProviderCredentialConstants.PROVIDER_NAME | IdP 유형 설정                                | AuthProvider.GOOGLE<br> AuthProvider.FACEBOOK<br>AuthProvider.NAVER<br>AuthProvider.TWITTER<br>AuthProvider.LINE<br>AuthProvider.APPLEID<br>AuthProvider.WEIBO<br>AuthProvider.KAKAOGAME<br>AuthProvider.GPGS_V2<br>AuthProvider.STEAM<br>"payco" |
| AuthProviderCredentialConstants.ACCESS_TOKEN | IdP 로그인 이후 받은 인증 정보(Access Token) 설정.<br/>Google 인증 시에는 사용 안 함. |                                          |
| AuthProviderCredentialConstants.AUTHORIZATION_CODE | Google 로그인 이후 획득할 수 있는 OTAC(one time authorization code) 입력 |                                          |
| AuthProviderCredentialConstants.SHOW_LOADING_ANIMATION | API 호출이 끝날 때까지 로딩 애니메이션을 표시 | **boolean**<br>**default**: true |
| AuthProviderCredentialConstants.LINE_CHANNEL_REGION | LINE 서비스 제공 지역 설정 | [Login with IdP 참고](./aos-authentication-Login.md#login-with-idp) |

> [참고]
>
> 게임 내에서 외부 서비스(Facebook 등)의 고유 기능을 사용해야 할 때 필요할 수 있습니다.
>

<br/>

> <font color="red">[주의]</font><br/>
>
> 외부 SDK에서 지원 요구하는 개발사항은 외부 SDK의 API를 사용하여 구현해야 하며, Gamebase에서는 지원하지 않습니다.
>

**API**

```java
+ (void)Gamebase.addMapping(Activity activity, Map<String, Object> credentialInfo, null, GamebaseDataCallback<AuthToken> callback);
```

**Example**

```java
private static void addMappingWithCredential(final Activity activity) {
    Map<String, Object> credentialInfo = new HashMap<>();
    credentialInfo.put(AuthProviderCredentialConstants.PROVIDER_NAME, AuthProvider.FACEBOOK);
    credentialInfo.put(AuthProviderCredentialConstants.ACCESS_TOKEN, facebookAccessToken);

    Gamebase.addMapping(activity, credentialInfo, new GamebaseDataCallback<AuthToken>() {
        @Override
        public void onCallback(AuthToken data, GamebaseException exception) {
            if (Gamebase.isSuccess(exception)) {
                // 매핑 추가 성공
                Log.d(TAG, "Add Mapping successful");
                String userId = Gamebase.getUserID();
                return;
            }

            // 매핑 추가 실패
            if (exception.getCode() == GamebaseError.SOCKET_ERROR ||
                    exception.getCode() == GamebaseError.SOCKET_RESPONSE_TIMEOUT) {
                // Socket error 로 일시적인 네트워크 접속 불가 상태임을 의미합니다.
                // 네트워크 상태를 확인하거나 잠시 대기 후 재시도 하세요.
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            Thread.sleep(2000);
                            addMappingWithCredential(activity);
                        } catch (InterruptedException e) {}
                    }
                }).start();
            } else if (exception.getCode() == GamebaseError.AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER) {
                // Mapping을 시도하는 IdP계정이 이미 다른 계정에 연동되어 있습니다.
                // 강제로 연동을 해제하기 위해서는 해당 계정의 탈퇴나 Mapping 해제를 하거나, 다음과 같이
                // ForcingMappingTicket을 획득 후, addMappingForcibly() 메소드를 이용하여 강제 매핑을 시도합니다.
                Log.e(TAG, "Add Mapping failed- ALREADY_MAPPED_TO_OTHER_MEMBER");
                final ForcingMappingTicket forcingMappingTicket = ForcingMappingTicket.from(exception);
                Gamebase.addMappingForcibly(activity, forcingMappingTicket, new GamebaseDataCallback<AuthToken>() {
                    @Override
                    public void onCallback(AuthToken data, GamebaseException exception) {
                        ...
                        // 자세한 내용은 addMappingForcibly API 문서를 참고하세요.
                    }
                }
            } else if (exception.getCode() == GamebaseError.AUTH_ADD_MAPPING_ALREADY_HAS_SAME_IDP) {
                // Mapping을 시도하는 IdP의 계정이 이미 추가되어 있습니다.
                // Gamebase Mapping은 한 IdP당 하나의 계정만 연동 가능합니다.
                // IdP계정을 변경하려면 이미 연동중인 계정은 Mapping 해제를 해야 합니다.
                Log.e(TAG, "Add Mapping failed- ALREADY_HAS_SAME_IDP");
            } else {
                // 매핑 추가 실패
                Log.e(TAG, "Add Mapping failed- "
                        + "errorCode: " + exception.getCode()
                        + "errorMessage: " + exception.getMessage());
            }
        }
    });
}
```

### Add Mapping Forcibly

특정 IdP에 이미 매핑되어있는 계정이 있을 때, **강제로** 매핑을 시도합니다.
**강제 매핑**을 시도할 때는 AddMapping API에서 획득한 `ForcingMappingTicket`이 필요합니다.

다음은 Facebook에 강제 매핑을 시도하는 예시입니다.

**API**

```java
+ (void)Gamebase.addMappingForcibly(Activity activity, ForcingMappingTicket forcingMappingTicket, GamebaseDataCallback<AuthToken> callback);

// Legacy API
+ (void)Gamebase.addMappingForcibly(Activity activity, String providerName, String forcingMappingKey, GamebaseDataCallback<AuthToken> callback);
+ (void)Gamebase.addMappingForcibly(Activity activity, String providerName, String forcingMappingKey, Map<String, Object> additionalInfo, GamebaseDataCallback<AuthToken> callback);
+ (void)Gamebase.addMappingForcibly(Activity activity, Map<String, Object> credentialInfo, String forcingMappingKey, GamebaseDataCallback<AuthToken> callback);
```

**Example**

```java
private static void addMappingForciblyFacebook(final Activity activity) {
    String mappingProvider = AuthProvider.FACEBOOK;
    Gamebase.addMapping(activity, mappingProvider, new GamebaseDataCallback<AuthToken>() {
        @Override
        public void onCallback(AuthToken result, GamebaseException exception) {
            if (Gamebase.isSuccess(exception)) {
                // 매핑 추가 성공
                Log.d(TAG, "Add Mapping successful");
                String userId = Gamebase.getUserID();
                return;
            }

            // 우선 addMapping API 호출 및 이미 연동되어 있는 계정으로 매핑을 시도하여, 다음과 같이 ForcingMappingTicket을 얻을 수 있습니다.
            if (exception.getCode() == GamebaseError.AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER) {
                // ForcingMappingTicket 클래스의 from() 메소드를 이용하여 ForcingMappingTicket 인스턴스를 얻습니다.
                final ForcingMappingTicket forcingMappingTicket = ForcingMappingTicket.from(exception);

                // 강제 매핑을 시도합니다.
                Gamebase.addMappingForcibly(activity, forcingMappingTicket, new GamebaseDataCallback<AuthToken>() {
                    @Override
                    public void onCallback(AuthToken data, GamebaseException addMappingForciblyException) {
                        if (Gamebase.isSuccess(addMappingForciblyException)) {
                            // 강제 매핑 추가 성공
                            Log.d(TAG, "Add Mapping Forcibly successful");
                            String userId = Gamebase.getUserID();
                            return;
                        }

                        // 강제 매핑 추가 실패
                        // 오류 코드를 확인하고 적절한 처리를 진행합니다.
                    }
                }
            } else {
                ...
            }
        }
    });
}
```

### Change Login with ForcingMappingTicket

특정 IdP에 이미 매핑되어 있는 계정이 있을 때, 현재 계정을 로그아웃하고 이미 매핑되어 있던 해당 계정으로 로그인합니다.
이때, AddMapping API에서 획득한 `ForcingMappingTicket`이 필요합니다.

Change Login API 호출이 실패하는 경우, Gamebase 로그인 상태는 기존의 UserID로 유지됩니다.

다음은 Facebook으로 매핑 시도 후 Facebook에 이미 매핑된 계정이 존재하자, 해당 계정으로 로그인을 변경하는 예시입니다.

**API**

```java
+ (void)Gamebase.changeLogin(Activity activity, ForcingMappingTicket forcingMappingTicket, GamebaseDataCallback<AuthToken> callback);
```

**Example**

```java
private static void changeLoginFacebook(final Activity activity) {
    String mappingProvider = AuthProvider.FACEBOOK;
    Gamebase.addMapping(activity, mappingProvider, new GamebaseDataCallback<AuthToken>() {
        @Override
        public void onCallback(AuthToken result, GamebaseException exception) {
            if (Gamebase.isSuccess(exception)) {
                // 매핑 추가 성공
                Log.d(TAG, "Add Mapping successful");
                String userId = Gamebase.getUserID();
                return;
            }

            // 우선 addMapping API 호출 및, 이미 연동되어있는 계정으로 매핑을 시도하여, 다음과 같이, ForcingMappingTicket을 얻을 수 있습니다.
            if (exception.getCode() == GamebaseError.AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER) {
                // ForcingMappingTicket 클래스의 from() 메소드를 이용하여 ForcingMappingTicket 인스턴스를 얻습니다.
                final ForcingMappingTicket forcingMappingTicket = ForcingMappingTicket.from(exception);

                // ForcingMappingTicket의 UserID로 로그인합니다.
                Gamebase.changeLogin(activity, forcingMappingTicket, new GamebaseDataCallback<AuthToken>() {
                    @Override
                    public void onCallback(AuthToken data, GamebaseException changeLoginException) {
                        if (Gamebase.isSuccess(changeLoginException)) {
                            // 로그인 변경 성공
                            Log.d(TAG, "Change Login successful");
                            String userId = Gamebase.getUserID();
                            return;
                        }

                        // 로그인 변경 실패
                        // 오류 코드를 확인하고 적절한 처리를 진행합니다.
                    }
                }
            } else {
                ...
            }
        }
    });
}
```

### Remove Mapping

특정 IdP에 대한 연동을 해제합니다. 만약, 현재 로그인 중인 계정을 해제하려고 하면 실패를 반환합니다.<br/>
연동 해제 후에는 Gamebase 내부에서, 해당 IdP에 대한 로그아웃을 처리합니다.

**API**

```java
+ (void)Gamebase.removeMapping(Activity activity, String providerName, null, GamebaseDataCallback<AuthToken> callback);
```

**Example**

```java
private static void removeMappingForFacebook(final Activity activity) {
    Gamebase.removeMapping(activity, AuthProvider.FACEBOOK, new GamebaseCallback() {
        @Override
        public void onCallback(GamebaseException exception) {
            if (Gamebase.isSuccess(exception)) {
                // 매핑 해제 성공
                Log.d(TAG, "Remove mapping successful");
            } else {
                if (exception.getCode() == GamebaseError.SOCKET_ERROR ||
                        exception.getCode() == GamebaseError.SOCKET_RESPONSE_TIMEOUT) {
                    // Socket error 로 일시적인 네트워크 접속 불가 상태임을 의미합니다.
                    // 네트워크 상태를 확인하거나 잠시 대기 후 재시도 하세요.
                    new Thread(new Runnable() {
                        @Override
                        public void run() {
                            try {
                                Thread.sleep(2000);
                                removeMappingForFacebook(activity);
                            } catch (InterruptedException e) {}
                        }
                    }).start();
                } else if (exception.getCode() == GamebaseError.AUTH_REMOVE_MAPPING_LOGGED_IN_IDP) {
                    // 로그인중인 계정으로는 Mapping 해제를 할 수 없습니다.
                    // 다른 계정으로 로그인 하여 Mapping 해제 하거나 탈퇴하여야 합니다.
                    Log.e(TAG, "Remove Mapping failed- LOGGED_IN_IDP");
                } else {
                    // 매핑 해제 실패
                    Log.e(TAG, "Remove mapping failed- "
                            + "errorCode: " + exception.getCode()
                            + "errorMessage: " + exception.getMessage());
                }
            }
        }
    });
}
```
