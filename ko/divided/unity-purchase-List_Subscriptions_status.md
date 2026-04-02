## Game > Gamebase > Unity SDK 사용 가이드 > 결제

### List Subscriptions status

현재 사용자 ID 기준으로 구독 상품들의 상태를 조회합니다.
콜백으로 반환되는 목록 안에는 구독 상품들의 정보가 담겨 있습니다.

> <font color="red">[주의]</font><br/>
>
> * 아래 가이드에 따라 구독 이벤트를 설정해야 구독 상태 코드가 정상적으로 반환됩니다.
>     * [Game > Gamebase > 스토어 콘솔 가이드 > Google 콘솔 가이드 > Google 시스템 내 실시간 구독 정보 이벤트 전파 설정](./console-google-guide/#google_1)
>     * 이벤트 설정을 하지 않은 상태에서 구매한 구독 상품의 상태 코드는 항상 0(PURCHASED)이 반환됩니다.
> * 현재 구독 상품은 Google Play 스토어만 지원합니다.


**GamebaseRequest.Purchase.PurchasableConfiguration**

| API                             | Mandatory(M) / Optional(O) | Description                                                 |
| ------------------------------- | -------------------------- | ----------------------------------------------------------- |
|  includeExpiredSubscriptions    | O                          | 만료된 구독 상품까지 포함하여 조회합니다.<br/>기본값은 **false**입니다.   |

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

```cs
static void RequestSubscriptionsStatus(GamebaseRequest.Purchase.PurchasableConfiguration configuration, GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback)
```

**Example**
```cs
public void RequestSubscriptionsStatusSample(bool includeExpiredSubscriptions)
{
    var configuration = new GamebaseRequest.Purchase.PurchasableConfiguration
    {
        includeExpiredSubscriptions = includeExpiredSubscriptions
    };
    Gamebase.Purchase.RequestSubscriptionsStatus(configuration, (subscriptionStatusList, error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            Debug.Log("RequestSubscriptionsStatus succeeded");

            foreach (GamebaseResponse.Purchase.PurchasableSubscriptionStatus subscriptionStatus in subscriptionStatusList)
            {
                var message = new StringBuilder();
                message.AppendLine(string.Format("storeCode:{0}", subscriptionStatus.storeCode));
                message.AppendLine(string.Format("itemSeq:{0}", subscriptionStatus.itemSeq));
                message.AppendLine(string.Format("price:{0}", subscriptionStatus.price));

                // Subscription status
                // Refer to the following document for the entire status code.
                // https://docs.nhncloud.com/en/TOAST/en/toast-sdk/iap-unity/#iapsubscriptionstatusstatus
                message.AppendLine(string.Format("statusCode:{0}", subscriptionStatus.statusCode));
                message.AppendLine(string.Format("gamebaseProductId:{0}", subscriptionStatus.gamebaseProductId));
                Debug.Log(message);
            }
        }
        else
        {
            // Check the error code and handle the error appropriately.
            Debug.Log(string.Format("RequestSubscriptionsStatus failed. error is {0}", error));
        }
    });
}
```

**VO**
```cs
public class PurchasableSubscriptionStatus
{
    /// <summary>
    /// 앱이 설치된 스토어에 대해 Gamebase에서 내부적으로 정의한 코드입니다.
    /// </summary>
    public string storeCode;

    /// <summary>
    /// 스토어의 결제 식별자입니다.
    /// </summary>
    public string paymentId;

    /// <summary>
    /// 구독 상품은 갱신될 때마다 paymentId가 변경됩니다.
    /// 이 필드는 구독 상품을 최초 결제했을 때의 paymentId를 알려줍니다.
    /// 스토어 및 결제 서버 상태에 따라 값이 존재하지 않을 수 있으므로
    /// 항상 유효한 값을 보장하지는 않습니다.
    /// </summary>
    public string originalPaymentId;

    /// 결제 식별자입니다.
    /// purchaseToken과 함께 'Consume' 서버 API를 호출하는 데 사용하는 중요한 정보입니다.
    ///    
    /// 주의: Consume API는 게임 서버에서 호출하세요!
    /// <para/><see href="https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap">Consume API</see>
    public string paymentSeq;

    /// <summary>
    /// 구매한 상품의 상품 ID입니다.
    /// </summary>
    public string marketItemId;

    /// <summary>
    /// IAP 웹 콘솔의 항목 고유 식별자
    /// </summary>
    public long itemSeq;

    /// <summary>
    /// 다음 값 중 하나를 가집니다.
    /// * UNKNOWN: 알 수 없는 유형입니다. Gamebase SDK를 업데이트하거나 Gamebase 고객 센터에 문의하세요.
    /// * CONSUMABLE: 소모품입니다.
    /// * AUTO_RENEWABLE: 구독 상품입니다.
    /// </summary>
    public string productType;

    /// <summary>
    /// 상품을 구매한 사용자 아이디입니다.
    /// 상품 구매에 사용하지 않은 사용자 아이디로 로그인하면 구매한 상품을 받을 수 없습니다.
    /// </summary>
    public string userId;

    /// <summary>
    /// 상품의 가격입니다.
    /// </summary>
    public float price;

    /// <summary>
    /// 통화 정보입니다.
    /// </summary>
    public string currency;

    /// <summary>
    /// Payment 식별자.
    /// paymentSeq로 'Consume' 서버 API를 호출하는 데 사용되는 중요한 정보입니다.
    /// Consume API에서 매개변수 이름을 'accessToken'으로 지정해야 전달됩니다.
    ///
    /// <para/><see href="https://docs.toast.com/ko/Game/Gamebase/ko/api-guide/#purchase-iap">Purchase IAP</see>
    /// </summary>
    public string purchaseToken;

    /// <summary>
    /// 이 값은 Google에서 구매할 때 사용되며 다음 값을 가질 수 있습니다.
    /// 단, Google 서버의 오류로 인해 Gamebase 결제 서버에서 일시적으로 인증 로직이 비활성화된 경우
    /// null만 반환하므로 항상 유효한 값을 보장하지 않을 수 있습니다.
    /// * null: 정상 결제
    /// * 테스트: 테스트 결제
    /// * 프로모션: 프로모션 결제
    /// </summary>
    public string purchaseType;

    /// <summary>
    /// 상품을 구매한 시간.(epoch time)
    /// </summary>
    public long purchaseTime;

    /// <summary>
    /// 구독이 만료되는 시간.(epoch time)
    /// </summary>
    public long expiryTime;

    /// <summary>
    /// Gamebase.Purchase.requestPurchase API 호출 시 페이로드에 전달되는 값입니다.
    /// 스토어 서버 상태에 따라 정보가 유실되는 경우가 있으므로 사용을 권장하지 않습니다.
    /// </summary>
    public string payload;

    /// <summary>
    /// 구독 상태
    /// 전체 상태 코드는 다음 문서를 참조하세요.
    /// <para/><see href="https://docs.nhncloud.com/en/TOAST/en/toast-sdk/iap-unity/#iapsubscriptionstatus">IAP Subscription Status</see>
    /// </summary>
    public int statusCode;

    /// <summary>
    /// 구독 상태에 대한 설명입니다.
    /// </summary>
    public string statusDescription;

    /// <summary>
    /// Gamebase 콘솔에 등록된 상품 ID입니다.
    /// Gamebase.Purchase.requestPurchase API로 상품을 구매할 때 사용됩니다.
    /// </summary>
    public string gamebaseProductId;
}
```
