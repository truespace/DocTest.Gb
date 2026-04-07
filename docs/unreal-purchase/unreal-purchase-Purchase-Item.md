---
source: unreal-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, Purchase, Consume, Error, RequestPurchase, GetSubsystem, GetGameInstance, GetPurchase, IsSuccess, RequestPurchaseWithPayload"
section: "Purchase Item"
order: 5
---

### Purchase Item

구매하고자 하는 아이템의 gamebaseProductId를 이용해 다음의 API를 호출하여 구매를 요청합니다.
게임 유저가 구매를 취소하는 경우 **PURCHASE_USER_CANCELED** 오류가 반환됩니다.

느린 결제나 부모 동의와 같이 결제 완료를 기다려야 하는 상황이 발생하는 경우에는 **PURCHASE_PENDING** 오류가 반환됩니다.
이후에 결제가 정상적으로 완료되는 경우, GamebaseEventHandler에서 결제 완료 이벤트를 수신할 수 있습니다.
[Game > Gamebase > Unreal SDK 사용 가이드 > ETC > Gamebase Event Handler](../unreal-etc.md#purchase-updated)

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void RequestPurchase(const FString& GamebaseProductId, const FGamebasePurchasableReceiptDelegate& Callback);
void RequestPurchase(const FString& GamebaseProductId, const FString& payload, const FGamebasePurchasableReceiptDelegate& Callback);
```

**Example**
```cpp
void USample::RequestPurchase(const FString& GamebaseProductId)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPurchase()->RequestPurchase(GamebaseProductId, FGamebasePurchasableReceiptDelegate::CreateLambda(
        [](const FGamebasePurchasableReceipt* PurchasableReceipt, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RequestPurchase succeeded. (GamebaseProductId= %s, price= %f, currency= %s, paymentSeq= %s, purchaseToken= %s)"),
                *PurchasableReceipt->GamebaseProductId, PurchasableReceipt->Price, *PurchasableReceipt->Currency,
                *PurchasableReceipt->PaymentSeq, *PurchasableReceipt->PurchaseToken);
        }
        else
        {
            if (Error->Code == GamebaseErrorCode::PURCHASE_USER_CANCELED)
            {
                UE_LOG(LogTemp, Display, TEXT("User canceled purchase."));
            }
            else
            {
                // Check the Error code and handle the Error appropriately.
                UE_LOG(LogTemp, Display, TEXT("RequestPurchase failed. (Error: %d)"), Error->Code);
            }

        }
    }));
}

void USample::RequestPurchaseWithPayload(const FString& GamebaseProductId)
{
    FString UserPayload = TEXT("{\"description\":\"This is example\",\"channelId\":\"delta\",\"characterId\":\"abc\"}");
    
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPurchase()->RequestPurchase(GamebaseProductId, UserPayload, FGamebasePurchasableReceiptDelegate::CreateLambda(
        [](const FGamebasePurchasableReceipt* PurchasableReceipt, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("RequestPurchase succeeded. (GamebaseProductId= %s, price= %f, currency= %s, paymentSeq= %s, purchaseToken= %s)"),
                *PurchasableReceipt->GamebaseProductId, PurchasableReceipt->price, *PurchasableReceipt->Currency,
                *PurchasableReceipt->PaymentSeq, *PurchasableReceipt->PurchaseToken);

            FString payload = PurchasableReceipt->payload;
        }
        else
        {
            if (Error->Code == GamebaseErrorCode::PURCHASE_USER_CANCELED)
            {
                UE_LOG(LogTemp, Display, TEXT("User canceled purchase."));
            }
            else
            {
                // Check the Error code and handle the Error appropriately.
                UE_LOG(LogTemp, Display, TEXT("RequestPurchase failed. (Error: %d)"), Error->Code);
            }
        }
    }));
}
```

**VO**

```cpp
struct FGamebasePurchasableReceipt
{   
    // 구매한 아이템의 상품 ID입니다.
    FString GamebaseProductId;

    // itemSeq 로 상품을 구매하는 Legacy API용 식별자입니다.
    int64 ItemSeq;

    // 구매한 상품의 가격입니다.
    float Price;

    // 통화 코드입니다.
    FString Currency;

    // 결제 식별자입니다.
    // purchaseToken과 함께 'Consume' 서버 API를 호출하는 데 사용하는 중요한 정보입니다.
    // Consume API : https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap
    // 주의 : Consume API 는 게임 서버에서 호출하세요! 
    FString PaymentSeq;

    // 결제 식별자입니다.
    // paymentSeq 와 함께 'Consume' 서버 API를 호출하는데 사용하는 중요한 정보입니다.
    // Consume API 에서는 'accessToken' 라는 이름의 파라메터로 전달해야 합니다.
    // Consume API : https://docs.toast.com/en/Game/Gamebase/en/api-guide/#purchase-iap
    // 주의 : Consume API 는 게임 서버에서 호출하세요! 
    FString PurchaseToken;

    // Google, Apple 과 같이 스토어 콘솔에 등록된 상품 ID입니다.
    FString MarketItemId;

    // 상품 타입으로, 다음 값들이 올 수 있습니다.
    // * UNKNOWN : 인식 불가능한 타입. Gamebase SDK 를 업데이트 하거나 Gamebase 고객 센터로 문의하세요.
    // * CONSUMABLE : 소비성 상품.
    // * AUTO_RENEWABLE : 구독형 상품.
    // * CONSUMABLE_AUTO_RENEWABLE : 구독형 상품을 구매한 유저에게 정기적으로 소비가 가능한 상품을 지급하고자 하는 경우 사용되는 '소비가 가능한 구독 상품'.
    FString ProductType;

    // 상품을 구매했던 User ID.
    // 상품을 구매하지 않은 User ID 로 로그인 한다면 구매한 아이템을 획득할 수 없습니다.
    FString UserId;

    // 스토어의 결제 식별자입니다.
    FString PaymentId;

    // 구독 상품은 갱신될 때마다 paymentId가 변경됩니다.
    // 이 필드는 맨 처음 구독 상품을 결제 했을때의 paymentId 를 알려줍니다.
    // 스토어에 따라, 결제 서버 상태에 따라 값이 존재하지 않을 수 있으므로
    // 항상 유효한 값을 보장하지는 않습니다.
    FString OriginalPaymentId;
    
    // 상품을 구매했던 시각입니다.(epoch time)
    int64 PurchaseTime;
    
    // 구독이 종료되는 시각입니다.(epoch time)
    int64 ExpiryTime;
    
    // 결제한 스토어 코드입니다.
    // GamebaseStoreCode 클래스에서 스토어 코드 목록을 확인할 수 있습니다.
    FString StoreCode;
    
    // RequestPurchase API 호출 시 payload로 전달했던 값입니다.
    // 스토어 서버 상태에 따라 정보가 유실되는 경우가 있으므로 사용을 권장하지 않습니다.
    FString Payload;
    
    // 프로모션 결제 여부
    // - (Android) Gamebase 결제 서버에서 일시적으로 검증 로직을 끄는 경우에는 false로만 출력되므로 유효한 값이 보장되지 않습니다.
    bool bIsPromotion;

    // 테스트 결제 여부
    // - (Android) Gamebase 결제 서버에서 일시적으로 검증 로직을 끄는 경우에는 false로만 출력되므로 유효한 값이 보장되지 않습니다.
    bool bIsTestPurchase;
};
```
