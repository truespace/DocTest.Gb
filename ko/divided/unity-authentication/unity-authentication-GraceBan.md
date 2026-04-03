---
source: unity-authentication.md
section: "GraceBan"
order: 8
created_date: 2026-04-03
---

## GraceBan

* '결제 어뷰징 자동 해제' 기능입니다.
    * 결제 어뷰징 자동 해제 기능은 결제 어뷰징 자동 제재로 이용 정지가 되어야 할 사용자가 '이용 정지 유예 상태' 후 이용 정지가 되도록 합니다.
    * '이용 정지 유예 상태'일 경우, 설정한 기간 내에 이용 정지 해제 조건을 모두 만족하면 정상적으로 플레이할 수 있습니다.
    * 기간 내에 조건을 충족하지 못하면 이용 정지가 됩니다.
* 결제 어뷰징 자동 해제 기능을 사용하는 게임은 로그인 후 항상 AuthToken.getGraceBanInfo() API를 호출하여, 결과가 null이 아닌 유효한 GraceBanInfo 객체를 반환한다면 해당 유저에게 이용 정지 해제 조건, 기간 등을 안내해야 합니다.
    * 이용 정지 유예 상태인 유저의 게임 내 접근 제어는 게임에서 처리해야 합니다.

**Example**

```cs
public void Login()
{
	Gamebase.Login(GamebaseAuthProvider.GUEST, (authToken, error) =>
    {
    	if (Gamebase.IsSuccess(error) == false)
        {
            // Login failed
            return;
        }

        // Check if user is under grace ban
        GamebaseResponse.Common.Member.GraceBanInfo graceBanInfo = authToken.member.graceBan;
        if (graceBanInfo != null)
        {
            string periodDate = string.Format("{0:yyyy/MM/dd HH:mm:ss}", 
                new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc).AddMilliseconds(graceBanInfo.gracePeriodDate));
            string message = graceBanInfo.message;
            
            GamebaseResponse.Common.Member.GraceBanInfo.ReleaseRuleCondition releaseRuleCondition = graceBanInfo.releaseRuleCondition;
            if (releaseRuleCondition != null)
            {
                // condition type: "AND", "OR"
                string releaseRule = string.Format("{0}{1} {2} {3}time(s)", releaseRuleCondition.amount,
                    releaseRuleCondition.currency, releaseRuleCondition.conditionType, releaseRuleCondition.count);
            }

            GamebaseResponse.Common.Member.GraceBanInfo.PaymentStatus paymentStatus = graceBanInfo.paymentStatus;
            if (paymentStatus != null) {
                String paidAmount = paymentStatus.amount + paymentStatus.currency;
                String paidCount = paymentStatus.count + "time(s)";
            }

            // Guide the user through the UI how to finish the grace ban status.
        }
        else
        {
            // Login success.
        }
    });
}
```
