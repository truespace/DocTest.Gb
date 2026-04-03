---
source: ios-authentication.md
section: "TransferAccount"
order: 6
created_date: 2026-04-03
---

## TransferAccount
게스트 계정을 다른 단말기로 이전하기 위해 계정 이전을 위한 키를 발급받는 기능입니다.

이 키를 **TransferAccountInfo** 라고 부릅니다.
발급 받은 TransferAccountInfo는 다른 단말기에서 **requestTransferAccount** API를 호출하여 계정 이전을 할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> TransferAccountInfo의 발급은 게스트 로그인 상태에서만 발급이 가능합니다.
> TransferAccountInfo를 이용한 계정 이전은 게스트 로그인 상태 또는 로그인되어 있지 않은 상태에서만 가능합니다.
> 로그인한 게스트 계정이 이미 다른 외부 IdP (Google, Facebook 등) 계정과 매핑이 되어 있다면 계정 이전이 지원되지 않습니다.

### Issue TransferAccount
게스트 계정 이전을 위한 TransferAccountInfo를 발급합니다.

**API**

```objectivec
+ (void)issueTransferAccountWithCompletion:(TransferAccountCompletion)completion;
```

**Example**

```objectivec
 - (void)issueTransferAccount {
     [TCGBGamebase issueTransferAccountWithCompletion:^(TCGBTransferAccountInfo* transferAccount, TCGBError *error) {
        NSLog(@"Issued TransferAccount => %@, error => %@", [transferAccount description], [error description]);
     }];
 }
```

### Query TransferAccount
게스트 계정 이전을 위해 이미 발급 받은 TransferAccountInfo 정보를 게임베이스 서버에 질의합니다.

**API**

```objectivec
+ (void)queryTransferAccountWithCompletion:(TransferAccountCompletion)completion;
```

**Example**

```objectivec
 - (void)queryTransferAccount {
     [TCGBGamebase queryTransferAccountWithCompletion:^(TCGBTransferAccountInfo* transferAccount, TCGBError *error) {
        NSLog(@"Published TransferAccount => %@, error => %@", [transferAccount description], [error description]);
     }];
 }
```


### Renew TransferAccount
이미 발급 받은 TransferAccountInfo 정보를 갱신합니다.
"자동 갱신", "수동 갱신"의 방법이 있으며, "Password만 갱신", "ID와 Password 모두 갱신" 등의 설정을 통해
TransferAccountInfo 정보를 갱신 할 수 있습니다.

```objectivec
+ (void)renewTransferAccountWithConfiguration:(TCGBTransferAccountRenewConfiguration *)config completion:(TransferAccountCompletion)completion;
```

**Example**

```objectivec
- (void)renewTransferAccount {
    // If you want renew the account automatically, use this config.
    TCGBTransferAccountRenewalTargetType renewalTargetType = TCGBTransferAccountRenewalTargetTypeIdPassword;
    TCGBTransferAccountRenewConfiguration* autoConfig = [TCGBTransferAccountRenewConfiguration autoRenewConfigurationWithRenewalTarget:renewalTargetType];
    
    // If you want renew the account manually, use this config.
    TCGBTransferAccountRenewConfiguration* manualConfig = [TCGBTransferAccountRenewConfiguration manualRenewConfigurationWithAccountId:@"ID" accountPassword:@"PASSWORD"];
    [TCGBGamebase renewTransferAccountWithConfiguration:autoConfig completion:^(TCGBTransferAccountInfo *transferAccount, TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error]) {
            // Renewing TransferAccount success.
            NSString* accountId = transferAccount.account.accountId;
            NSString* accountPw = transferAccount.account.accountPassword;
            return;
        }
        else {
            // Renewing TransferAccount failed.
        }
    }];
}
```




### Transfer Guest Account to Another Device
**issueTransfer** API로 발급 받은 TransferAccount를 통해 계정을 이전하는 기능입니다.
계정 이전 성공 시 TransferAccount를 발급 받은 단말기에서 이전 완료 메시지가 표시될 수 있고, 게스트 로그인 시 새로운 계정이 생성됩니다.
계정 이전이 성공한 단말기에서는 TransferAccount를 발급받았던 단말기의 게스트 계정을 계속해서 사용할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> 이미 게스트 로그인이 되어 있는 상태에서 이전이 성공하게 되면, 단말기에 로그인되어 있던 게스트 계정은 유실됩니다.
> 만일 잘못된 id/password를 연속해서 입력하면 **AUTH_TRANSFERACCOUNT_BLOCK(3042)** 오류가 발생하며 계정 이전이 일정 시간 차단됩니다.
> 이 경우에는 아래의 예제와 같이 TCGBTransferAccountFailInfo 값을 통해 언제까지 계정 이전이 차단되는지 유저에게 알려줄 수 있습니다.



**API**

```objectivec
+ (void)transferAccountWithIdPLoginWithAccountId:(NSString *)accountId accountPassword:(NSString *)accountPassword completion:(void(^)(TCGBAuthToken* authToken, TCGBError* error))completion;
```

**Example**

```objectivec
 - (void)transferOtherDevice {
    [TCGBGamebase transferAccountWithIdPLoginWithAccountId:@"1Aie0198" accountPassword:@"1Aie0199" completion:^(TCGBAuthToken* authToken, TCGBError* error) {
       if (error.code == TCGB_ERROR_AUTH_TRANSFERACCOUNT_BLOCK) {
            // Transfering Account failed.
            TCGBTransferAccountFailInfo* failInfo = [TCGBTransferAccountFailInfo transferAccountFailInfoFrom:error];
            if (failInfo == nil) {
                // Transfering Account failed by entering the wrong id / pw multiple times.
                // You can tell when the account transfer is blocked by the TransferAccountFailInfo.

                NSString *failedId = failInfo.accountId;
                NSInteger failCount = failInfo.failCount;
                NSDate *blockedDate = [NSDate dateTimeIntervalSince1970:(failInfo.blockEndDate / 1000.0)];
                return;
            }
            // Transfering Account failed by another reason.
            return;  
        }
        // Transfering Account success.
        // TODO: implements post login process
    }];
 }
```
