---
source: ios-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, Login, GraceBan, Ban, loginWithType, isSuccessWithError"
section: GraceBan
order: 8
---

## GraceBan

* '결제 어뷰징 자동 해제' 기능입니다.
    * 결제 어뷰징 자동 해제 기능은 결제 어뷰징 자동 제재로 이용 정지가 되어야 할 사용자가 '이용 정지 유예 상태' 후 이용 정지가 되도록 합니다.
    * '이용 정지 유예 상태'일 경우, 설정한 기간 내에 이용 정지 해제 조건을 모두 만족하면 정상적으로 플레이할 수 있습니다.
    * 기간 내에 조건을 충족하지 못하면 이용 정지가 됩니다.
* 결제 어뷰징 자동 해제 기능을 사용하는 게임은 로그인 후 항상 TCGBAuthToken.tcgbMember.graceBanInfo 값을 확인하고, null이 아닌 유효한 TCGBGraceBanInfo 객체를 반환한다면 해당 유저에게 이용 정지 해제 조건, 기간 등을 안내해야 합니다.
    * 이용 정지 유예 상태인 유저의 게임 내 접근 제어는 게임에서 처리해야 합니다.

**Example**

```objectivec
- (void)testGraceBanInfo {
    [TCGBGamebase loginWithType:kTCGBAuthAppleID viewController:viewController completion:^(TCGBAuthToken *authToken, TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == NO) {
            // Login failed
            return;
        }
        
        // Check if user is under grace ban
        if (authToken.tcgbMember.graceBanInfo != nil) {
            TCGBGraceBanInfo *graceBanInfo = authToken.tcgbMember.graceBanInfo;
            // gracePeriodDate: epoch time in milliseconds
            long long gracePeriodDate = graceBanInfo.gracePeriodDate;
            NSString *message = [graceBanInfo.message stringByRemovingPercentEncoding];
            if (graceBanInfo.paymentStatus != nil) {
                TCGBPaymentStatus *paymentStatus = graceBanInfo.paymentStatus;
                double paymentStatusAmount = paymentStatus.amount;
                int paymentStatusCount = paymentStatus.count;
            }
            if (graceBanInfo.releaseRuleCondition != nil) {
                TCGBReleaseRuleCondition *releaseRuleCondition = graceBanInfo.releaseRuleCondition;
                double releaseRuleConditionAmount = releaseRuleCondition.amount;
                int releaseRuleConditionCount = releaseRuleCondition.count;
                NSString *releaseRuleConditionCurrency = releaseRuleCondition.currency;
                // condition type: "AND", "OR"
                NSString *releaseRuleConditionType = releaseRuleCondition.conditionType;
            }
            // Guide the user through the UI how to finish the grace ban status.
        }
        else {
            // Login Success
        }
    }];
}
```
