---
source: unreal-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "List Actived Subscriptions"
section: "List Actived Subscriptions"
order: 8
---

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
