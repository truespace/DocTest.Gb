---
source: unreal-purchase.md
section: "List Non-Consumed Items-to-Event by Purchase"
order: 2
created_date: 2026-04-03
---

### List Non-Consumed Items

아이템을 구매했지만, 정상적으로 아이템이 소비(배송, 지급)되지 않은 미소비 결제 내역을 요청합니다.
미결제 내역이 있는 경우에는 게임 서버(아이템 서버)에 요청하여, 아이템을 배송(지급)하도록 처리해야 합니다.


**FGamebasePurchasableConfiguration**

| API                             | Mandatory(M) / Optional(O) | Description                                                                    |
| ------------------------------- | -------------------------- | ------------------------------------------------------------------------------ |
| bAllStores                       | O                          | 동일한 UserID로 다른 스토어에서 구매한 미소비 내역도 반환합니다.<br/>기본값은 **false**입니다. |

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void RequestItemListOfNotConsumed(const FGamebasePurchasableConfiguration& Configuration, const FGamebasePurchasableReceiptListDelegate& Callback);
```

**Example**
```cpp
void USample::RequestItemListOfNotConsumed(bool bAllStores)
{
    FGamebasePurchasableConfiguration Configuration;
    Configuration.bAllStores = bAllStores;

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPurchase()->RequestItemListOfNotConsumed(Configuration, FGamebasePurchasableReceiptListDelegate::CreateLambda(
        [](const TArray<FGamebasePurchasableItem>* PurchasableItemList, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            // Should Deal With This non-consumed Items.
            // Send this item list to the game(item) server for consuming item.

            UE_LOG(LogTemp, Display, TEXT("RequestItemListOfNotConsumed succeeded."));

            for (const FGamebasePurchasableReceipt& PurchasableReceipt : *purchasableReceiptList)
            {
                UE_LOG(LogTemp, Display, TEXT(" - GamebaseProductId= %s, price= %f, currency= %s, paymentSeq= %s, purchaseToken= %s"),
                    *PurchasableReceipt.GamebaseProductId, PurchasableReceipt.Price, *PurchasableReceipt.Currency, *PurchasableReceipt.PaymentSeq, *PurchasableReceipt.PurchaseToken);
            }
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("RequestItemListOfNotConsumed failed. (Error: %d)"), Error->Code);
        }
    }));
}
```

### List Actived Subscriptions

현재 사용자 ID 기준으로 활성화된 구독 목록을 조회합니다.
결제가 완료된 구독 상품(자동 갱신형 구독, 자동 갱신형 소비성 구독 상품)은 만료되기 전까지 계속 조회할 수 있습니다.
사용자 ID가 같다면 Android와 iOS에서 구매한 구독 상품이 모두 조회됩니다.

> <font color="red">[주의]</font><br/>
>
> Android에서는 Google Play 스토어에서만 현재 구독 상품을 지원합니다.

**FGamebasePurchasableConfiguration**

| API                             | Mandatory(M) / Optional(O) | Description                                                                    |
| ------------------------------- | -------------------------- | ------------------------------------------------------------------------------ |
| bAllStores                       | O                          | 동일한 UserID로 다른 스토어에서 구매한 미소비 내역도 반환합니다.<br/>기본값은 **false**입니다. |

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void RequestActivatedPurchases(const FGamebasePurchasableConfiguration& Configuration, const FGamebasePurchasableReceiptListDelegate& Callback);
```

**Example**
```cpp
void USample::RequestActivatedPurchases(bool bAllStores)
{
    FGamebasePurchasableConfiguration Configuration;
    Configuration.bAllStores = bAllStores;

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPurchase()->RequestActivatedPurchases(Configuration, FGamebasePurchasableReceiptListDelegate::CreateLambda(
        [](const TArray<FGamebasePurchasableReceipt>* purchasableReceiptList, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RequestActivatedPurchases succeeded."));

            for (const FGamebasePurchasableReceipt& PurchasableReceipt : *purchasableReceiptList)
            {
                UE_LOG(LogTemp, Display, TEXT(" - GamebaseProductId= %s, price= %f, currency= %s, paymentSeq= %s, purchaseToken= %s"),
                    *PurchasableReceipt.GamebaseProductId, PurchasableReceipt.Price, *PurchasableReceipt.Currency, *PurchasableReceipt.PaymentSeq, *PurchasableReceipt.PurchaseToken);
            }
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("RequestActivatedPurchases failed. (Error: %d)"), Error->Code);
        }
    }));
}
```

### List Subscriptions Status

현재 사용자 ID 기준으로 구독 상품들의 상태를 조회합니다.
콜백으로 반환되는 목록 안에는 구독 상품들의 정보가 담겨 있습니다.

> <font color="red">[주의]</font><br/>
>
> * 아래 가이드에 따라 구독 이벤트를 설정해야 구독 상태 코드가 정상적으로 반환됩니다.
>     * [Game > Gamebase > 스토어 콘솔 가이드 > Google 콘솔 가이드 > Google 시스템 내 실시간 구독 정보 이벤트 전파 설정](../../console-google-guide.md#google_1)
>     * 이벤트 설정을 하지 않은 상태에서 구매한 구독 상품의 상태 코드는 항상 0(PURCHASED)이 반환됩니다.
> * 현재 구독 상품은 Google Play 스토어만 지원합니다.


**FGamebasePurchasableConfiguration**

| API                             | Mandatory(M) / Optional(O) | Description                                                 |
| ------------------------------- | -------------------------- | ----------------------------------------------------------- |
| bIncludeExpiredSubscriptions    | O                          | 만료된 구독 상품까지 포함하여 조회합니다.<br/>기본값은 **false**입니다.   |

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID

```cpp
void RequestSubscriptionsStatus(const FGamebasePurchasableConfiguration& Configuration, const FGamebasePurchasableSubscriptionStatusDelegate& Callback);
```

**Example**
```cpp
void USample::RequestSubscriptionsStatus(bool bIncludeExpiredSubscriptions)
{
    FGamebasePurchasableConfiguration Configuration;
    Configuration.bAllStores = bAllStores;

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPurchase()->RequestSubscriptionsStatus(Configuration, FGamebasePurchasableSubscriptionStatusDelegate::CreateLambda(
        [](const TArray<FGamebasePurchasableSubscriptionStatus>* purchasableReceiptList, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RequestSubscriptionsStatus succeeded."));

            for (const FGamebasePurchasableSubscriptionStatus& PurchasableReceipt : *purchasableReceiptList)
            {
                UE_LOG(LogTemp, Display, TEXT(" - GamebaseProductId= %s, price= %f, currency= %s, paymentSeq= %s, purchaseToken= %s"),
                    *PurchasableReceipt.GamebaseProductId, PurchasableReceipt.Price, *PurchasableReceipt.Currency, *PurchasableReceipt.PaymentSeq, *PurchasableReceipt.PurchaseToken);
            }
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("RequestSubscriptionsStatus failed. (Error: %d)"), Error->Code);
        }
    }));
}
```

**VO**
```cpp
struct FGamebasePurchasableSubscriptionStatus
{
    // 앱이 설치된 스토어에 대해 Gamebase에서 내부적으로 정의한 코드입니다.
    FString StoreCode;
    
    // 스토어의 결제 식별자입니다.
    FString PaymentId;

    // 구독 상품은 갱신될 때마다 paymentId가 변경됩니다.
    // 이 필드는 구독 상품을 최초 결제했을 때의 paymentId를 알려줍니다.
    // 스토어 및 결제 서버 상태에 따라 값이 존재하지 않을 수 있으므로
    // 항상 유효한 값을 보장하지는 않습니다.
    FString OriginalPaymentId;

    // 결제 식별자입니다.
    // purchaseToken과 함께 'Consume' 서버 API를 호출하는 데 사용하는 중요한 정보입니다.
    //    
    // 주의: Consume API는 게임 서버에서 호출하세요! (https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap)
    FString PaymentSeq;

    // 구매한 상품의 상품 ID입니다.
    FString MarketItemId;
    
    // IAP 웹 콘솔의 항목 고유 식별자
    int64 ItemSeq;

    // 다음 값 중 하나를 가집니다.
    // * UNKNOWN: 알 수 없는 유형입니다. Gamebase SDK를 업데이트하거나 Gamebase 고객 센터에 문의하세요.
    // * CONSUMABLE: 소모품입니다.
    // * AUTO_RENEWABLE: 구독 상품입니다.
    FString ProductType;

    // 상품을 구매한 사용자 아이디입니다.
    // 상품 구매에 사용하지 않은 사용자 아이디로 로그인하면 구매한 상품을 받을 수 없습니다.
    FString UserId;
    
    // 상품의 가격입니다.
    float Price;

    // 통화 정보입니다.
    FString Currency;

    // Payment 식별자.
    // paymentSeq로 'Consume' 서버 API를 호출하는 데 사용되는 중요한 정보입니다.
    // Consume API에서 매개변수 이름을 'accessToken'으로 지정해야 전달됩니다.
    // 참고: https://docs.toast.com/ko/Game/Gamebase/ko/api-guide/#purchase-iap
    FString PurchaseToken;

    // 상품을 구매한 시간.(epoch time)
    int64 PurchaseTime;
    
    // 구독이 만료되는 시간.(epoch time)
    int64 ExpiryTime;
    
    // RequestPurchase API 호출 시 페이로드에 전달되는 값입니다.
    // 스토어 서버 상태에 따라 정보가 유실되는 경우가 있으므로 사용을 권장하지 않습니다.
    FString Payload;
    
    // 구독 상태
    // 전체 상태 코드는 다음 문서를 참조하세요.
    // - https://docs.nhncloud.com/en/TOAST/en/toast-sdk/iap-unity/#iapsubscriptionstatus
    int32 StatusCode;
    
    // 구독 상태에 대한 설명입니다.
    FString StatusDescription;
    
    // Gamebase 콘솔에 등록된 상품 ID입니다.
    // RequestPurchase API로 상품을 구매할 때 사용됩니다.
    FString GamebaseProductId;

    // 이 값은 Google에서 구매할 때 사용되며 다음 값을 가질 수 있습니다.
    // 단, Google 서버의 오류로 인해 Gamebase 결제 서버에서 일시적으로 인증 로직이 비활성화된 경우
    // null만 반환하므로 항상 유효한 값을 보장하지 않을 수 있습니다.
    // * null: 정상 결제
    // * 테스트: 테스트 결제
    // * 프로모션: 프로모션 결제
    FString PurchaseType;
};
```

### Event by Purchase

Promotion 코드 입력을 통해 상품을 획득한 경우 또는 Pending 결제(느린 결제, 부모 동의 등)가 완료되었을 때 GamebaseEventHandler를 통해 이벤트를 받아 처리할 수 있습니다.
GamebaseEventHandler로 프로모션 결제 및 지연 결제 이벤트를 처리하는 방법은 아래 가이드를 확인하세요.
[Game > Gamebase > Unreal SDK 사용 가이드 > ETC > Gamebase Event Handler](../../unreal-etc.md#purchase-updated)

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

> <font color="red">[주의]</font><br/>
>
> iOS 프로모션 결제를 위해서는 반드시 아래 가이드를 따라 설정하세요.
> [Game > Gamebase > iOS SDK 사용 가이드 > 결제 > Event by Purchase](../../ios-purchase.md#event-by-purchase)
