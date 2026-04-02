## Game > Gamebase > Android SDK 사용 가이드 > 인증

## TransferAccount
게스트 계정을 다른 단말기로 이전하기 위해 계정 이전을 위한 키를 발급받는 기능입니다.

이 키를 **TransferAccountInfo** 라고 부릅니다.
발급 받은 TransferAccountInfo는 다른 단말기에서 **requestTransferAccount** API를 호출하여 계정 이전을 할 수 있습니다.

> <font color="red">[주의]</font><br/>
> TransferAccountInfo의 발급은 게스트 로그인 상태에서만 발급이 가능합니다.
> TransferAccountInfo를 이용한 계정 이전은 게스트 로그인 상태 또는 로그인되어 있지 않은 상태에서만 가능합니다.
> 로그인한 게스트 계정이 이미 다른 외부 IdP (Google, Facebook, PAYCO 등) 계정과 매핑이 되어 있다면 계정 이전이 지원되지 않습니다.

### Issue TransferAccount
게스트 계정 이전을 위한 TransferAccountInfo를 발급합니다.

**API**

```java
+ (void)Gamebase.issueTransferAccount(final GamebaseDataCallback<TransferAccountInfo> callback);
```

**Example**

```java
Gamebase.issueTransferAccount(new GamebaseDataCallback<TransferAccountInfo>() {
    @Override
    public void onCallback(final TransferAccountInfo transferAccount, final GamebaseException exception) {
        if (!Gamebase.isSuccess(exception)) {
            // Issuing TransferAccount failed.
            return;
        }

        // Issuing TransferAccount success.
        final String account = transferAccount.account.id;
        final String password = transferAccount.account.password;
    }
});
```

### Query TransferAccount
게스트 계정 이전을 위해 이미 발급 받은 TransferAccountInfo 정보를 게임베이스 서버에 질의합니다.

**API**

```java
+ (void)Gamebase.queryTransferAccount(final GamebaseDataCallback<TransferAccountInfo> callback);
```

**Example**

```java
Gamebase.queryTransferAccount(new GamebaseDataCallback<TransferAccountInfo>() {
    @Override
    public void onCallback(final TransferAccountInfo transferAccount, final GamebaseException exception) {
        if (!Gamebase.isSuccess(exception)) {
            // Querying TransferAccount failed.
            return;
        }

        // Querying TransferAccount success.
        final String account = transferAccount.account.id;
        final String password = transferAccount.account.password;
    }
});
```


### Renew TransferAccount
이미 발급 받은 TransferAccountInfo 정보를 갱신합니다.
"자동 갱신", "수동 갱신"의 방법이 있으며, "Password만 갱신", "ID와 Password 모두 갱신" 등의 설정을 통해
TransferAccountInfo 정보를 갱신 할 수 있습니다.

```java
+ (void)Gamebase.renewTransferAccount(final TransferAccountRenewConfiguration config, final GamebaseDataCallback<TransferAccountInfo> callback);
```

**Example**

```java
// If you want renew the account automatically, use this config.
final RenewalTargetType renewalTargetType = RenewalTargetType.ID_PASSWORD; // RenewalTargetType.PASSWORD
final TransferAccountRenewConfiguration autoConfig = TransferAccountRenewConfiguration.newAutoRenewConfiguration(renewalTargetType);

// If you want renew the account manually, use this config.
final TransferAccountRenewConfiguration manualConfig = TransferAccountRenewConfiguration.newManualRenewConfiguration("id", "password");
Gamebase.renewTransferAccount(autoConfig, new GamebaseDataCallback<TransferAccountInfo>() {
    @Override
    public void onCallback(final TransferAccountInfo transferAccountInfo, final GamebaseException exception) {
        if (!Gamebase.isSuccess(exception)) {
            // Renewing TransferAccount failed.
            return;
        }

        // Renewing TransferAccount success.
        final String renewedAccount = transferAccount.account.id;
        final String renewedPassword = transferAccount.account.password;
    }
});
```

### Transfer Guest Account to Another Device
**issueTransfer** API로 발급 받은 TransferAccount를 통해 계정을 이전하는 기능입니다.
계정 이전 성공 시 TransferAccount를 발급 받은 단말기에서 이전 완료 메시지가 표시될 수 있고, 게스트 로그인 시 새로운 계정이 생성됩니다.
계정 이전이 성공한 단말기에서는 TransferAccount를 발급받았던 단말기의 게스트 계정을 계속해서 사용할 수 있습니다.

> `주의`
>
> * 이미 게스트 로그인이 되어 있는 상태에서 이전이 성공하게 되면, 단말기에 로그인되어 있던 게스트 계정은 유실됩니다.
> * 만일 잘못된 id/password를 연속해서 입력하면 **AUTH_TRANSFERACCOUNT_BLOCK(3042)** 오류가 발생하며 계정 이전이 일정 시간 차단됩니다.
> 이 경우에는 아래의 예제와 같이 TransferAccountFailInfo 값을 통해 언제까지 계정 이전이 차단되는지 유저에게 알려줄 수 있습니다.

**API**

```java
+ (void)Gamebase.transferAccountWithIdPLogin(String accountId, String accountPassword, GamebaseDataCallback<AuthToken> callback);
```

**Example**

```java
Gamebase.transferAccountWithIdPLogin(accountId, accountPassword, new GamebaseDataCallback<AuthToken>() {
    @Override
    public void onCallback(AuthToken authToken, GamebaseException exception) {
        if (!Gamebase.isSuccess(exception)) {
            // Transfering Account failed.
            TransferAccountFailInfo failInfo = TransferAccountFailInfo.from(exception);
            if (failInfo != null) {
                // Transfering Account failed by entering the wrong id / pw multiple times.
                // You can tell when the account transfer is blocked by the TransferAccountFailInfo.
                String failedId = failInfo.id;
                int failCount = failInfo.failCount;
                Date blockedDate = new Date(failInfo.blockEndDate);
                return;
            }

            // Transfering Account failed by another reason.
            return;
        }

        // Transfering Account success.
        // TODO: implements post login process
    }
});
```
