## Game > Gamebase > Unreal SDK 사용 가이드 > 결제

### List Purchasable Items

아이템 목록을 조회하려면 다음 API를 호출합니다. 
콜백으로 반환되는 목록 안에는 각 아이템들에 대한 정보가 있습니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void RequestItemListPurchasable(const FGamebasePurchasableItemListDelegate& Callback);
```

**Example**
```cpp
void USample::RequestItemListPurchasable()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPurchase()->RequestItemListPurchasable(FGamebasePurchasableItemListDelegate::CreateLambda(
        [](const TArray<FGamebasePurchasableItem>* PurchasableItemList, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RequestItemListPurchasable succeeded."));

            for (const FGamebasePurchasableItem& PurchasableItem : *PurchasableItemList)
            {
                UE_LOG(LogTemp, Display, TEXT(" - GamebaseProductId= %s, price= %f, itemName= %s, itemName= %s, marketItemId= %s"),
                    *PurchasableItem.GamebaseProductId, PurchasableItem.Price, *PurchasableItem.Currency, *PurchasableItem.ItemName, *PurchasableItem.MarketItemId);
            }
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("RequestItemListPurchasable failed. (Error: %d)"), Error->Code);
        }
    }));
}
```

**VO**

```cpp
struct FGamebasePurchasableItem
{
    // Gamebase 콘솔에 등록된 상품 ID입니다.
    // Gamebase.Purchase.requestPurchase API로 상품을 구매할 때 사용됩니다.
    FString GamebaseProductId;

    // itemSeq 로 상품을 구매하는 Legacy API용 식별자입니다.
    int64 ItemSeq;

    // 상품의 가격입니다.
    float Price;

    // 통화 코드입니다.
    FString Currency;

    // Gamebase 콘솔에 등록된 상품 이름입니다.
    FString ItemName;

    // Google, Apple 과 같이 스토어 콘솔에 등록된 상품 ID입니다.
    FString MarketItemId;

    // 상품 타입으로, 다음 값들이 올 수 있습니다.
    // * UNKNOWN : 인식 불가능한 타입. Gamebase SDK 를 업데이트 하거나 Gamebase 고객 센터로 문의하세요.
    // * CONSUMABLE : 소비성 상품.
    // * AUTORENEWABLE : 구독형 상품.
    // * CONSUMABLE_AUTO_RENEWABLE : 구독형 상품을 구매한 유저에게 정기적으로 소비가 가능한 상품을 지급하고자 하는 경우 사용되는 '소비가 가능한 구독 상품'.
    FString ProductType;
    
    // 통화 기호가 포함된 현지화 된 가격 정보입니다.
    FString LocalizedPrice;
    
    // 스토어 콘솔에 등록된 현지화된 상품 이름입니다.
    FString LocalizedTitle;

    // 스토어 콘솔에 등록된 현지화된 상품 설명입니다.
    FString LocalizedDescription;

    // Gamebase 콘솔에서 해당 상품의 '사용 여부'를 나타냅니다.
    bool bIsActive;
};
```
