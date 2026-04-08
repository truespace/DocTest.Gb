---
source: unity-authentication.md
section: "TemporaryWithdrawal"
order: 7
split: true
created_date_time: 20260408_191848
keyword: Unity, Login, Withdraw, TemporaryWithdrawal, Console
---

## TemporaryWithdrawal

'탈퇴 유예' 기능입니다.
임시 탈퇴를 요청하여 즉시 탈퇴가 진행되지 않고 일정 기간의 유예 기간이 지나면 탈퇴가 이루어집니다.
유예 기간은 콘솔에서 변경할 수 있습니다.

> `주의`
>
> 탈퇴 유예 기능을 사용하는 경우에는 **Gamebase.Withdraw()** API를 사용하지 마세요.
> **Gamebase.Withdraw()** API 는 즉시 계정을 탈퇴합니다.

로그인이 성공하면 AuthToken.member.temporaryWithdrawal로 탈퇴 유예 상태인 유저인지 판단할 수 있습니다.

### Request TemporaryWithdrawal

임시 탈퇴를 요청합니다.
콘솔에 지정된 기간이 지나면 자동으로 탈퇴 진행이 완료됩니다.

**API**

```cs
public static void RequestWithdrawal(GamebaseCallback.GamebaseDelegate<GamebaseResponse.TemporaryWithdrawalInfo> callback)
```

**Example**

```cs
public void SampleRequestWithdrawal()
{
    Gamebase.TemporaryWithdrawal.RequestWithdrawal((data, error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            long gracePeriodDate = data.gracePeriodDate;
            Debug.Log(string.Format("RequestWithdrawal succeeded. The date when you can withdraw your withdrawal is {0}", gracePeriodDate));
        }
        else
        {
            Debug.Log(string.Format("RequestWithdrawal failed. error:{0}", error));
        }
    });
}
```

### Check TemporaryWithdrawal User

탈퇴 유예를 사용하는 게임은 로그인 후 항상 AuthToken.member.temporaryWithdrawal가 null이 아니라면 해당 유저에게 탈퇴 진행중이라는 사실을 알려주어야 합니다.

**Example**

```cs
public void LoginSample()
{
    Gamebase.Login(GamebaseAuthProvider.XXX, (authToken, error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            if(authToken.member.temporaryWithdrawal != null)
            {
                long gracePeriodDate = authToken.member.temporaryWithdrawal.gracePeriodDate;
                Debug.Log(string.Format("User is under temporary withdrawa. GracePeriodDate: {0}", error));
            }            
            else
            {
                string userId = authToken.member.userId;            
                Debug.Log(string.Format("Login succeeded. Gamebase userId is {0}", userId));
            }
        }
        else
        {
            // Check the error code and handle the error appropriately.            
            Debug.Log(string.Format("Login failed. error is {0}", error));
        }
    });
}

```

### Cancel TemporaryWithdrawal

탈퇴를 요청을 취소합니다.
탈퇴 요청 후 기간이 만료되어 탈퇴가 완료되면 취소가 불가능합니다.

**API**

```cs
static void CancelWithdrawal(GamebaseCallback.ErrorDelegate callback)
```
**Example**

```cs
public void SampleCancelWithdrawal()
{
    Gamebase.TemporaryWithdrawal.CancelWithdrawal((error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            Debug.Log("CancelWithdrawal succeeded.");
        }
        else
        {
            Debug.Log(string.Format("CancelWithdrawal failed. error:{0}", error));
        }
    });
}
```

### Withdraw Immediately

탈퇴 유예 기간을 무시하고 즉시 탈퇴를 진행합니다.
실제 내부 동작은 Gamebase.Withdraw() API 와 동일합니다.

즉시 탈퇴는 취소가 불가능하므로 유저에게 실행 여부를 거듭 확인하시기 바랍니다.

**API**

```cs
static void WithdrawImmediately(GamebaseCallback.ErrorDelegate callback)
```

**Example**

```cs
public void SampleWithdrawImmediately()
{
    Gamebase.TemporaryWithdrawal.WithdrawImmediately((error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            Debug.Log("WithdrawImmediately succeeded.");
        }
        else
        {
            Debug.Log(string.Format("SampleWithdrawImmediately failed. error:{0}", error));
        }
    });
}
```
