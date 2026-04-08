---
source: unreal-authentication.md
section: "TransferAccount"
order: 6
split: true
created_date_time: 20260408_191848
keyword: Unreal, Login, Mapping, TransferAccount
---

## TransferAccount
게스트 계정을 다른 단말기로 이전하기 위해 계정 이전을 위한 키를 발급받는 기능입니다.

이 키를 **TransferAccountInfo**라고 부릅니다.
발급 받은 TransferAccountInfo는 다른 단말기에서 **requestTransferAccount** API를 호출하여 계정 이전을 할 수 있습니다.

> <font color="red">[주의]</font><br/>
> TransferAccountInfo의 발급은 게스트 로그인 상태에서만 발급이 가능합니다.
> TransferAccountInfo를 이용한 계정 이전은 게스트 로그인 상태 또는 로그인되어 있지 않은 상태에서만 가능합니다.
> 로그인한 게스트 계정이 이미 다른 외부 IdP (Google, Facebook, PAYCO 등) 계정과 매핑이 되어 있다면 계정 이전이 지원되지 않습니다.

### Issue TransferAccount
게스트 계정 이전을 위한 TransferAccountInfo를 발급합니다.

**API**

```cpp
void IssueTransferAccount(const FGamebaseTransferAccountDelegate& Callback);
```

**Example**

```cpp
void USample::IssueTransferAccount()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->IssueTransferAccount(FGamebaseTransferAccountDelegate::CreateLambda([](const FGamebaseTransferAccountInfo* TransferAccountInfo, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            // Issuing TransferAccount success.
        }
        else
        {
            // Issuing TransferAccount failed.
        }
    }));
}
```

### Query TransferAccount
게스트 계정 이전을 위해 이미 발급 받은 TransferAccountInfo 정보를 게임베이스 서버에 질의합니다.

**API**

```cpp
void QueryTransferAccount(const FGamebaseTransferAccountDelegate& Callback);
```

**Example**

```cpp
void USample::QueryTransferAccount()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->IssueTransferAccount(FGamebaseTransferAccountDelegate::CreateLambda([](const FGamebaseTransferAccountInfo* TransferAccountInfo, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            // Querying TransferAccount success.
        }
        else
        {
            // Querying TransferAccount failed.
        }
    }));
}
```

### Renew TransferAccount
이미 발급 받은 TransferAccountInfo 정보를 갱신합니다.
"자동 갱신", "수동 갱신"의 방법이 있으며, "Password만 갱신", "ID와 Password 모두 갱신" 등의 설정을 통해
TransferAccountInfo 정보를 갱신할 수 있습니다.

```cpp
void RenewTransferAccount(const FGamebaseTransferAccountRenewConfiguration& Configuration, const FGamebaseTransferAccountDelegate& Callback);
```

**Example**

```cpp
void USample::RenewTransferAccount(const FString& AccountId, const FString& AccountPassword)
{
    // 수동 설정
    FGamebaseTransferAccountRenewConfiguration Configuration;
    Configuration.AccountId = AccountId;
    Configuration.AccountPassword = AccountPassword;
    //FGamebaseTransferAccountRenewConfiguration Configuration { AccountPassword };

    // 자동 설정
    //FGamebaseTransferAccountRenewConfiguration Configuration{ type };

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->RenewTransferAccount(Configuration, FGamebaseTransferAccountDelegate::CreateLambda([](const FGamebaseTransferAccountInfo* TransferAccountInfo, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            // Renewing TransferAccount success.
        }
        else
        {
            // Renewing TransferAccount failed.
        }
    }));
}
```


### Transfer Guest Account to Another Device
**issueTransfer** API로 발급 받은 TransferAccount를 통해 계정을 이전하는 기능입니다.
계정 이전 성공 시 TransferAccount를 발급 받은 단말기에서 이전 완료 메시지가 표시될 수 있고, Guest 로그인 시 새로운 계정이 생성됩니다.
계정 이전이 성공한 단말기에서는 TransferAccount를 발급받았던 단말기의 게스트 계정을 계속해서 사용할 수 있습니다.

> <font color="red">[주의]</font><br/>
> 이미 게스트 로그인된 상태에서 이전에 성공하면, 단말기에 로그인되어 있던 게스트 계정은 유실됩니다.

**API**

```cpp
void TransferAccountWithIdPLogin(const FString& AccountId, const FString& AccountPassword, const FGamebaseAuthTokenDelegate& Callback);
```

**Example**

```cpp
void USample::TransferAccountWithIdPLogin(const FString& AccountId, const FString& AccountPassword)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->TransferAccountWithIdPLogin(AccountId, AccountPassword, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            // Transfering Account success.
            // TODO: implements post login process
        }
        else
        {
            // Transfering Account failed.
        }
    }));
}
```
