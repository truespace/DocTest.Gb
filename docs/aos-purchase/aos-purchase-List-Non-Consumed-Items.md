---
source: aos-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "List Non-Consumed Items"
section: "List Non-Consumed Items"
order: 7
---

### List Non-Consumed Items

* 아직 소비되지 않은 일회성 상품(CONSUMABLE)과 소비성 구독 상품(CONSUMABLE_AUTO_RENEWABLE) 정보를 조회합니다.
* 미결제 내역이 있는 경우에는 게임 서버(아이템 서버)에 요청하여, 아이템을 배송(지급)하도록 처리해야 합니다.
* 정상적으로 결제가 완료되지 못한 경우 재처리의 역할도 하므로 다음 상황에서 호출해 주세요.
    * 게임 유저에게 지급되지 못한 아이템이 남아 있는지 확인
    	* 로그인 완료 후
    	* 게임 내 상점(또는 로비) 진입시
    	* 유저 프로필 또는 우편함 확인시
    * 재처리가 필요한 아이템이 있는지 확인
    	* 결제 전
    	* 결제 실패 후

**PurchasableConfiguration**

| API                             | Mandatory(M) / Optional(O) | Description                                                                    |
| ------------------------------- | -------------------------- | ------------------------------------------------------------------------------ |
| newBuilder()                    | **M**                      | Configuration 객체 생성을 위한 Builder를 생성합니다.                                |
| build()                         | **M**                      | 설정을 마친 Builder를 Configuration 객체로 변환합니다.                                |
| setAllStores(boolean allStores) | O                          | 동일한 UserID로 다른 스토어에서 구매한 미소비 내역도 반환합니다.<br/>기본값은 **false**입니다. |

**API**

```java
+ (void)Gamebase.Purchase.requestItemListOfNotConsumed(@NonNull final Activity activity,
                                                       @NonNull final PurchasableConfiguration configuration,
                                                       @NonNull final GamebaseDataCallback<List<PurchasableReceipt>> callback);
```

**Example**

```java
final PurchasableConfiguration configuration = PurchasableConfiguration.newBuilder().build();
Gamebase.Purchase.requestItemListOfNotConsumed(activity, configuration, new GamebaseDataCallback<List<PurchasableReceipt>>() {
    @Override
    public void onCallback(List<PurchasableReceipt> data, GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            // Succeeded.
        } else {
            // Failed.
            Log.e(TAG, "Request item list failed- "
                    + "errorCode: " + exception.getCode()
                    + "errorMessage: " + exception.getMessage());
        }
    }
});
```
