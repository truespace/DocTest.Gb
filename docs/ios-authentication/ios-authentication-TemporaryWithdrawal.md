---
source: ios-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, Login, Withdraw, TemporaryWithdrawal, Error, isSuccessWithError, withdrawWithViewController, requestTemporaryWithdrawalWithViewController, cancelTemporaryWithdrawalWithViewController, WithdrawCompletion"
section: TemporaryWithdrawal
order: 7
---

## TemporaryWithdrawal

'탈퇴 유예' 기능입니다.
임시 탈퇴를 요청하여 즉시 탈퇴가 진행되지 않고 일정 기간의 유예 기간이 지나면 탈퇴가 이루어집니다.
유예 기간은 콘솔에서 변경할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> 탈퇴 유예 기능을 사용하는 경우에는 **[TCGBGamebase withdrawWithViewController:completion:]** API를 사용하지 마세요.
> **[TCGBGamebase withdrawWithViewController:completion:]** API 는 즉시 계정을 탈퇴합니다.

로그인이 성공하면 AuthToken.getTemporaryWithdrawalInfo() API를 호출하여 탈퇴 유예 상태인 유저인지 판단할 수 있습니다.

### Request TemporaryWithdrawal

임시 탈퇴를 요청합니다.
콘솔에 지정된 기간이 지나면 자동으로 탈퇴 진행이 완료됩니다.

**API**

```objectivec
+ (void)requestTemporaryWithdrawalWithViewController:(nullable UIViewController *)viewController completion:(nullable TemporaryWithdrawCompletion)completion;
```

**ErrorCode**

|Error Code | Description |
| --- | --- |
| TCGB\_ERROR\_AUTH\_WITHDRAW\_ALREADY\_TEMPORARY\_WITHDRAW(3602) | 이미 임시 탈퇴를 요청한 유저입니다. |

**Example**

```objectivec
- (void)testRequestWithdraw {
    [TCGBGamebase requestTemporaryWithdrawalWithViewController:parentViewController completion:^(TCGBTemporaryWithdrawalInfo *info, TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == NO) {
            if (error.code == TCGB_ERROR_AUTH_WITHDRAW_ALREADY_TEMPORARY_WITHDRAW) {
                // Already requested temporary withdrawal before.
            }
            else {
                // Request temporary withdrawal failed.
                return;
            }
        }

        // Request temporary withdrawal success.
    }];
}
```

### Check TemporaryWithdrawal User

탈퇴 유예를 사용하는 게임은 로그인 후 항상 **TCGBAuthToken.tcgbMember.temporaryWithdrawal** 를 사용하여, 결과가 null 이 아닌 유효한 TemporaryWithdrawalInfo 객체를 반환한다면 해당 유저에게 탈퇴 진행중이라는 사실을 알려주어야 합니다.

**Example**


```objectivec
- (void)testLogin {
    [TCGBGamebase loginWithType:@"appleid" viewController:parentViewController completion:^(TCGBAuthToken *authToken, TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == NO) {
            // Login failed
            return;
        }

        // Check if user is requesting withdrawal
        if (authToken.tcgbMember.temporaryWithdrawal != nil) {
            // User is under temporary withdrawal
            long gradePeriod = authToken.tcgbMember.temporaryWithdrawal.gracePeriodDate;
        }
        else {
            // Login Success
        }
    }];
}
```


### Cancel TemporaryWithdrawal

탈퇴 요청을 취소합니다.
탈퇴 요청 후 기간이 만료되어 탈퇴가 완료되면 취소가 불가능합니다.

**API**

```objectivec
+ (void)cancelTemporaryWithdrawalWithViewController:(UIViewController *)viewController completion:(WithdrawCompletion)completion;
```

**ErrorCode**

|Error Code | Description |
| --- | --- |
| TCGB\_ERROR\_AUTH\_WITHDRAW\_NOT\_TEMPORARY\_WITHDRAW(3603) | 임시 탈퇴를 요청한 유저가 아닙니다. |

**Example**

```objectivec
- (void)testCancelWithdraw {
    [TCGBGamebase cancelTemporaryWithdrawalWithViewController:parentViewController completion:^(TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == NO) {
            if (error.code == TCGB_ERROR_AUTH_WITHDRAW_NOT_TEMPORARY_WITHDRAW) {
                // Never requested temporary withdrawal before.
            }
            else {
                // Cancel temporary withdrawal failed.
                return
            }
        }

        // Cancel temporary withdrawal success.
    }];
}
```

### Withdraw Immediately

탈퇴 유예 기간을 무시하고 즉시 탈퇴를 진행합니다.
실제 내부 동작은 **[TCGBGamebase withdrawWithViewController:completion:]** API 와 동일합니다.

즉시 탈퇴는 취소가 불가능하므로 유저에게 실행 여부를 거듭 확인하시기 바랍니다.

**API**

```objectivec
+ (void)withdrawImmediatelyWithViewController:(UIViewController *)viewController completion:(WithdrawCompletion)completion;
```


**Example**

```objectivec
- (void)testWithdrawImmediately {
    [TCGBGamebase withdrawImmediatelyWithViewController:parentViewController completion:^(TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == NO) {
            // withdraw failed.
            return;
        }

        // Withdraw success.
    }];
}
```
