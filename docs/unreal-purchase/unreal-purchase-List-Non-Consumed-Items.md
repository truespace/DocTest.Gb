---
source: unreal-purchase.md
section: "List Non-Consumed Items"
order: 7
split: true
created_date_time: 20260408_191848
keyword: Unreal, Purchase, Consume
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
