---
source: unreal-authentication.md
section: "GraceBan"
order: 8
created_date: 2026-04-03
---

## GraceBan

* '결제 어뷰징 자동 해제' 기능입니다.
    * 결제 어뷰징 자동 해제 기능은 결제 어뷰징 자동 제재로 이용 정지가 되어야 할 사용자가 '이용 정지 유예 상태' 후 이용 정지가 되도록 합니다.
    * '이용 정지 유예 상태'일 경우, 설정한 기간 내에 이용 정지 해제 조건을 모두 만족하면 정상적으로 플레이할 수 있습니다.
    * 기간 내에 조건을 충족하지 못하면 이용이 정지됩니다.
* 결제 어뷰징 자동 해제 기능을 사용하는 게임은 로그인 후 항상 AuthToken.member.graceBanInfo API 값을 확인하고, null이 아닌 유효한 GraceBanInfo 객체를 반환한다면 해당 유저에게 이용 정지 해제 조건, 기간 등을 안내해야 합니다.
    * 이용 정지 유예 상태인 유저의 게임 내 접근 제어는 게임에서 처리해야 합니다.

**Example**

```cpp
void USample::Login()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Login(GamebaseAuthProvider::Guest, FGamebaseAuthTokenDelegate::CreateLambda([](const FGamebaseAuthToken* AuthToken, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error) == false)
        {
            // Login failed
            return;
        }
        
        if (AuthToken->Member.GraceBan.IsSet())
        {
            const auto GraceBan = AuthToken->Member.raceBan.GetValue();

            // GracePeriodDate: epoch time in milliseconds
            const FDateTime PeriodDate = FDateTime(1970, 1, 1) + FTimespan::FromMilliseconds(GraceBan.GracePeriodDate);

            if (GraceBan.ReleaseRuleCondition.IsSet())
            {
                const auto ReleaseRuleCondition = GraceBan.ReleaseRuleCondition.GetValue();

                // condition type: "AND", "OR"
                FString releaseRule = FString::Printf(TEXT("%lld%s %s %dtime(s)"), ReleaseRuleCondition.Amount,
                    *ReleaseRuleCondition.Currency, *ReleaseRuleCondition.ConditionType, ReleaseRuleCondition.Count);
            }

            if (GraceBan.PaymentStatus.IsSet())
            {
                const auto paymentStatus = GraceBan.PaymentStatus.GetValue();

                FString paidAmount = FString::Printf(TEXT("%lld%s"), PaymentStatus.Amount, *PaymentStatus.Currency);
                FString paidCount = PaymentStatus.count + "time(s)";
            }
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("Login succeeded. Gamebase userId is %s"), *AuthToken->Member.UserId);
        }
    }));
}
```
