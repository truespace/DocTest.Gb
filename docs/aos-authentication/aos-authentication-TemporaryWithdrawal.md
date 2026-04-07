---
source: aos-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Login, Withdraw, TemporaryWithdrawal, Error, getTemporaryWithdrawalInfo, isSuccess, requestWithdrawal, cancelWithdrawal, withdrawImmediately"
section: TemporaryWithdrawal
order: 7
---

## TemporaryWithdrawal

'탈퇴 유예' 기능입니다.
임시 탈퇴를 요청하여 즉시 탈퇴가 진행되지 않고 일정 기간의 유예 기간이 지나면 탈퇴가 이루어집니다.
유예 기간은 콘솔에서 변경할 수 있습니다.

> `주의`
>
> 탈퇴 유예 기능을 사용하는 경우에는 **Gamebase.withdraw()** API를 사용하지 마세요.
> **Gamebase.withdraw()** API 는 즉시 계정을 탈퇴합니다.

로그인이 성공하면 AuthToken.getTemporaryWithdrawalInfo() API를 호출하여 탈퇴 유예 상태인 유저인지 판단할 수 있습니다.

### Request TemporaryWithdrawal

임시 탈퇴를 요청합니다.
콘솔에 지정된 기간이 지나면 자동으로 탈퇴 진행이 완료됩니다.

**API**

```java
+ (void)Gamebase.TemporaryWithdrawal.requestWithdrawal(@NonNull Activity activity,
                                                       @Nullable GamebaseDataCallback<TemporaryWithdrawalInfo> callback);
```

**ErrorCode**

|Error Code | Description |
| --- | --- |
| AUTH\_WITHDRAW\_ALREADY\_TEMPORARY\_WITHDRAW(3602) | 이미 임시 탈퇴를 요청한 유저입니다. |

**Example**

```java
public static void testRequestWithdraw() {
    Gamebase.TemporaryWithdrawal.requestWithdrawal(new GamebaseCallback() {
        @Override
        public void onCallback(TemporaryWithdrawalInfo data GamebaseException exception) {
            if (!Gamebase.isSuccess(exception)) {
                if (exception.getCode() == GamebaseError.AUTH_WITHDRAW_ALREADY_TEMPORARY_WITHDRAW) {
                    // Already requested temporary withdrawal before.
                } else {
                    // Request temporary withdrawal failed.
                    return;
                }
            }

            // Request temporary withdrawal success.
        }
    });
}
```

### Check TemporaryWithdrawal User

탈퇴 유예를 사용하는 게임은 로그인 후 항상 AuthToken.getTemporaryWithdrawalInfo() API를 호출하여, 결과가 null 이 아닌 유효한 TemporaryWithdrawalInfo 객체를 반환한다면 해당 유저에게 탈퇴 진행중이라는 사실을 알려주어야 합니다.

**Example**

```java
public static void testLogin() {
    Gamebase.login(activity, provider, new GamebaseDataCallback<AuthToken>() {
        @Override
        public void onCallback(AuthToken data, GamebaseException exception) {
            if (!Gamebase.isSuccess(exception)) {
                // Login failed
                return;
            }

            // Check if user is requesting withdrawal
            if (data.getTemporaryWithdrawalInfo() != null) {
                // User is under temporary withdrawal
                long gracePeriodDate = data.getTemporaryWithdrawalInfo().getGracePeriodDate();
            } else {
                // Login success.
            }
        }
    });
}
```

### Cancel TemporaryWithdrawal

탈퇴를 요청을 취소합니다.
탈퇴 요청 후 기간이 만료되어 탈퇴가 완료되면 취소가 불가능합니다.

**API**

```java
+ (void)Gamebase.TemporaryWithdrawal.cancelWithdrawal(@NonNull Activity activity,
                                                      @Nullable GamebaseCallback callback);
```

**ErrorCode**

|Error Code | Description |
| --- | --- |
| AUTH\_WITHDRAW\_NOT\_TEMPORARY\_WITHDRAW(3603) | 임시 탈퇴를 요청한 유저가 아닙니다. |

**Example**

```java
public static void testCancelWithdraw() {
    Gamebase.TemporaryWithdrawal.cancelWithdrawal(new GamebaseCallback() {
        @Override
        public void onCallback(final GamebaseException exception) {
            if (!Gamebase.isSuccess(exception)) {
                if (exception.getCode() == GamebaseError.AUTH_WITHDRAW_NOT_TEMPORARY_WITHDRAW) {
                    // Never requested temporary withdrawal before.
                } else {
                    // Cancel temporary withdrawal failed.
                    return;
                }
            }

            // Cancel temporary withdrawal success.
        }
    });
}
```

### Withdraw Immediately

탈퇴 유예 기간을 무시하고 즉시 탈퇴를 진행합니다.
실제 내부 동작은 Gamebase.withdraw() API 와 동일합니다.

즉시 탈퇴는 취소가 불가능하므로 유저에게 실행 여부를 거듭 확인하시기 바랍니다.

**API**

```java
+ (void)Gamebase.TemporaryWithdrawal.withdrawImmediately(@NonNull Activity activity,
                                                         @Nullable GamebaseCallback callback);
```

**Example**

```java
public static void testWithdrawImmediately() {
    Gamebase.TemporaryWithdrawal.withdrawImmediately(activity, new GamebaseCallback() {
        @Override
        public void onCallback(final GamebaseException exception) {
            if (!Gamebase.isSuccess(exception)) {
                // Withdraw failed.
                return;
            }

            // Withdraw success.
        }
    });
}
```
