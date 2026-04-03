---
source: unity-purchase.md
section: "List Actived Subscriptions-to-Error Handling"
order: 2
created_date: 2026-04-03
---

### List Actived Subscriptions

현재 사용자 ID 기준으로 활성화된 구독 목록을 조회합니다.
결제가 완료된 구독 상품(자동 갱신형 구독, 자동 갱신형 소비성 구독 상품)은 만료되기 전까지 계속 조회할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> 현재 Android에서는 Google Play 스토어에서만 구독 상품을 지원합니다.


**GamebaseRequest.Purchase.PurchasableConfiguration**

| API                             | Mandatory(M) / Optional(O) | Description                                                                    |
| ------------------------------- | -------------------------- | ------------------------------------------------------------------------------ |
| allStores                       | O                          | 동일한 UserID로 다른 스토어에서 구매한 미소비 내역도 반환합니다.<br/>기본값은 **false**입니다. |

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

```cs
static void RequestActivatedPurchases(GamebaseRequest.Purchase.PurchasableConfiguration configuration, GamebaseCallback.GamebaseDelegate<List<GamebaseResponse.Purchase.PurchasableReceipt>> callback)
```

**Example**
```cs
public void RequestActivatedPurchasesSample(bool allStores)
{
    var configuration = new GamebaseRequest.Purchase.PurchasableConfiguration
    {
        allStores = allStores
    };
    
    Gamebase.Purchase.RequestActivatedPurchases(configuration, (purchasableReceiptList, error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            Debug.Log("RequestItemListPurchasable succeeded");

            foreach (GamebaseResponse.Purchase.PurchasableReceipt purchasableReceipt in purchasableReceiptList)
            {
                var message = new StringBuilder();
                message.AppendLine(string.Format("gamebaseProductId:{0}", purchasableReceipt.gamebaseProductId));
                message.AppendLine(string.Format("price:{0}", purchasableReceipt.price));
                message.AppendLine(string.Format("currency:{0}", purchasableReceipt.currency));
                
                // You will need paymentSeq and purchaseToken when calling the Consume API.
                // Refer to the following document for the Consume API.
                // https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchaseiap
                message.AppendLine(string.Format("paymentSeq:{0}", purchasableReceipt.paymentSeq));
                message.AppendLine(string.Format("purchaseToken:{0}", purchasableReceipt.purchaseToken));
                message.AppendLine(string.Format("marketItemId:{0}", purchasableReceipt.marketItemId));
                Debug.Log(message);
            }
        }
        else
        {
            // Check the error code and handle the error appropriately.
            Debug.Log(string.Format("RequestActivatedPurchases failed. error is {0}", error));
        }
    });
}
```

### List Subscriptions status

현재 사용자 ID 기준으로 구독 상품들의 상태를 조회합니다.
콜백으로 반환되는 목록 안에는 구독 상품들의 정보가 담겨 있습니다.

> <font color="red">[주의]</font><br/>
>
> * 아래 가이드에 따라 구독 이벤트를 설정해야 구독 상태 코드가 정상적으로 반환됩니다.
>     * [Game > Gamebase > 스토어 콘솔 가이드 > Google 콘솔 가이드 > Google 시스템 내 실시간 구독 정보 이벤트 전파 설정](../../console-google-guide.md#google_1)
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

### Event by Promotion

프로모션 결제가 완료되었을때 GamebaseEventHandler 를 통해 이벤트를 받아 처리할 수 있습니다.
GamebaseEventHandler 로 프로모션 결제 이벤트를 처리하는 방법은 아래 가이드를 확인하세요.
[Game > Gamebase > Unity SDK 사용 가이드 > ETC > Gamebase Event Handler](../../unity-etc.md#purchase-updated)

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

> <font color="red">[주의]</font><br/>
>
> iOS 프로모션 결제를 위해서는 반드시 아래 가이드를 따라 설정하세요.
> [Game > Gamebase > iOS SDK 사용 가이드 > 결제 > Event by Promotion](../../ios-purchase.md#event-by-promotion)

### Error Handling

| Error                                     | Error Code | Description                              |
|-------------------------------------------|------------| ---------------------------------------- |
| PURCHASE_NOT_INITIALIZED                  | 4001       | Purchase 모듈이 초기화되지 않았습니다.<br>gamebase-adapter-purchase-IAP 모듈을 프로젝트에 추가했는지 확인해 주세요. |
| PURCHASE_USER_CANCELED                    | 4002       | 게임 유저가 아이템 구매를 취소하였습니다.                  |
| PURCHASE_NOT_FINISHED_PREVIOUS_PURCHASING | 4003       | 구매 로직이 아직 완료되지 않은 상태에서 API가 호출되었습니다. |
| PURCHASE_NOT_ENOUGH_CASH                  | 4004       | 해당 스토어의 캐시가 부족해 결제할 수 없습니다.              |
| PURCHASE_INACTIVE_PRODUCT_ID              | 4005       | 해당 상품이 활성화 상태가 아닙니다.  |
| PURCHASE_NOT_EXIST_PRODUCT_ID             | 4006       | 존재하지 않는 GamebaseProductID 로 결제를 요청하였습니다. |
| PURCHASE_LIMIT_EXCEEDED                   | 4007       | 월 구매 한도를 초과했습니다.             |
| PURCHASE_PENDING                          | 4008       | 결제를 완료하려면 추가 확인이 필요합니다. |
| PURCHASE_NOT_SUPPORTED_MARKET             | 4010       | 지원하지 않는 스토어입니다.<br>선택 가능한 스토어는 AS(App Store), GG(Google), ONESTORE, GALAXY, HUAWEI, MYCARD 입니다. |
| PURCHASE_EXTERNAL_LIBRARY_ERROR           | 4201       | NHN Cloud IAP 라이브러리 오류입니다.<br/>상세 오류를 확인하십시오. |
| PURCHASE_UNKNOWN_ERROR                    | 4999       | 정의되지 않은 구매 오류입니다.<br>전체 로그를 [고객 센터](https://toast.com/support/inquiry)에 올려 주시면 가능한 한 빠르게 답변 드리겠습니다. |

* 전체 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [오류 코드](../../error-code.md#client-sdk)

**PURCHASE_EXTERNAL_LIBRARY_ERROR**

* 이 오류는 NHN Cloud IAP 라이브러리에서 오류가 발생했을 때 반환됩니다.
* NHN Cloud IAP 라이브러리에서 발생한 오류 정보는 상세 오류에 포함되어 있으며 상세한 오류 코드 및 메시지는 다음과 같이 확인할 수 있습니다. 

```cs
GamebaseError gamebaseError = error; // GamebaseError object via callback

if (Gamebase.IsSuccess(gamebaseError))
{
    // succeeded
}
else
{
    Debug.Log(string.Format("code:{0}, message:{1}", gamebaseError.code, gamebaseError.message));

    GamebaseError moduleError = gamebaseError.error; // GamebaseError.error object from external module
    if (null != moduleError)
    {
        int moduleErrorCode = moduleError.code;
        string moduleErrorMessage = moduleError.message;

        Debug.Log(string.Format("moduleErrorCode:{0}, moduleErrorMessage:{1}", moduleErrorCode, moduleErrorMessage));
    }
}
```

* NHN Cloud IAP 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [NHN Cloud > SDK 사용 가이드 > IAP > Android > 오류 코드](https://docs.nhncloud.com/ko/nhncloud/ko/nhncloud-sdk/iap-android/#_32)
    * [NHN Cloud > SDK 사용 가이드 > IAP > iOS > 에러 코드](https://docs.nhncloud.com/ko/nhncloud/ko/nhncloud-sdk/iap-ios/#_17)
