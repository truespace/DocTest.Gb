---
source: unreal-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, Login, Withdraw, TemporaryWithdrawal, Error, Guest, RequestWithdrawal, WithdrawImmediately, GetSubsystem, GetGameInstance"
section: TemporaryWithdrawal
order: 7
---

## TemporaryWithdrawal

'탈퇴 유예' 기능입니다.
임시 탈퇴를 요청하여 즉시 탈퇴가 진행되지 않고 일정 기간의 유예 기간이 지나면 탈퇴가 이루어집니다.
유예 기간은 콘솔에서 변경할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> 탈퇴 유예 기능을 사용하는 경우에는 **Withdraw API**를 사용하지 마세요.
> **Withdraw API**는 즉시 계정을 탈퇴합니다.

로그인이 성공하면 AuthToken.member.temporaryWithdrawal로 탈퇴 유예 상태인 유저인지 판단할 수 있습니다.

### Request TemporaryWithdrawal

임시 탈퇴를 요청합니다.
콘솔에 지정된 기간이 지나면 자동으로 탈퇴 진행이 완료됩니다.

**API**

```cpp
void RequestWithdrawal(const FGamebaseTemporaryWithdrawalDelegate& Callback);
```

**Example**

```cpp
void USample::RequestWithdrawal()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetTemporaryWithdrawal()->RequestWithdrawal(FGamebaseTemporaryWithdrawalDelegate::CreateLambda([](const FGamebaseTemporaryWithdrawalInfo* Info, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RequestWithdrawal succeeded. The date when you can withdraw your withdrawal is %d"), Info->GracePeriodDate);
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("RequestWithdrawal failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```

### Check TemporaryWithdrawal User

탈퇴 유예를 사용하는 게임은 로그인 후 항상 AuthToken.member.temporaryWithdrawal가 null이 아니라면 해당 유저에게 탈퇴 진행 중이라는 사실을 알려야 합니다.

**Example**

```cpp
void USample::Login()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Login(GamebaseAuthProvider::Guest, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            if (AuthToken->Member.TemporaryWithdrawal.IsSet())
            {
                const auto TemporaryWithdrawal = AuthToken->Member.TemporaryWithdrawal.GetValue();
                // GracePeriodDate: epoch time in milliseconds
                const FDateTime PeriodDate = FDateTime(1970, 1, 1) + FTimespan::FromMilliseconds(TemporaryWithdrawal.GracePeriodDate);
                UE_LOG(LogTemp, Display, TEXT("User is under temporary withdrawa. GracePeriodDate : %s"), *PeriodDate.ToString());
            }
            else
            {
                UE_LOG(LogTemp, Display, TEXT("Login succeeded. Gamebase userId is %s"), *AuthToken->Member.UserId);
            }
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("Login failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```

### Cancel TemporaryWithdrawal

탈퇴 요청을 취소합니다.
탈퇴 요청 후 기간이 만료되어 탈퇴가 완료되면 취소가 불가능합니다.

**API**

```cpp
void CancelWithdrawal(const FGamebaseErrorDelegate& Callback);
```
**Example**

```cpp
void USample::CancelTemporaryWithdrawal()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetTemporaryWithdrawal()->CancelTemporaryWithdrawal(FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("CancelTemporaryWithdrawal succeeded."));
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("CancelTemporaryWithdrawal failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```

### Withdraw Immediately

탈퇴 유예 기간을 무시하고 즉시 탈퇴를 진행합니다.
실제 내부 동작은 Withdraw API와 동일합니다.

즉시 탈퇴는 취소가 불가능하므로 유저에게 실행 여부를 거듭 확인하시기 바랍니다.

**API**

```cpp
void WithdrawImmediately(const FGamebaseErrorDelegate& Callback);
```

**Example**

```cpp
void USample::WithdrawImmediately()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetTemporaryWithdrawal()->WithdrawImmediately(FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("WithdrawImmediately succeeded."));
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("WithdrawImmediately failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```
