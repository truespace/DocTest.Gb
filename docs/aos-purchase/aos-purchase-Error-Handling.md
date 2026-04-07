---
source: aos-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Error Handling"
section: "Error Handling"
order: 11
---

### Error Handling

| Error                                     | Error Code | Description                              |
| ----------------------------------------- | ---------- | ---------------------------------------- |
| PURCHASE_NOT_INITIALIZED                  | 4001       | Purchase 모듈이 초기화되지 않았습니다.<br>gamebase-adapter-purchase-IAP 모듈을 프로젝트에 추가했는지 확인해주세요. |
| PURCHASE_USER_CANCELED                    | 4002       | 게임 유저가 아이템 구매를 취소하였습니다.                 |
| PURCHASE_NOT_FINISHED_PREVIOUS_PURCHASING | 4003       | 구매 로직이 아직 완료되지 않은 상태에서 API가 호출되었습니다.     |
| PURCHASE_INACTIVE_PRODUCT_ID              | 4005       | 해당 상품이 활성화 상태가 아닙니다.  |
| PURCHASE_NOT_EXIST_PRODUCT_ID             | 4006       | 존재하지 않는 GamebaseProductID 로 결제를 요청하였습니다. |
| PURCHASE_LIMIT_EXCEEDED                   | 4007       | 월 구매 한도를 초과했습니다.             |
| PURCHASE_PENDING                          | 4008       | 결제를 완료하려면 추가 확인이 필요합니다. |
| PURCHASE_NOT_SUPPORTED_MARKET             | 4010       | 지원하지 않는 스토어입니다.<br>선택 가능한 스토어는 GG(Google), ONESTORE, GALAXY, HUAWEI, MYCARD입니다. |
| PURCHASE_EXTERNAL_LIBRARY_ERROR           | 4201       | NHN Cloud IAP 라이브러리 오류입니다.<br/>상세 오류를 확인하십시오. |
| PURCHASE_UNKNOWN_ERROR                    | 4999       | 정의되지 않은 구매 오류입니다.<br>전체 로그를 [고객 센터](https://toast.com/support/inquiry)에 올려 주시면 가능한 한 빠르게 답변 드리겠습니다. |

* 전체 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [오류 코드](../../error-code.md#client-sdk)

**PURCHASE_EXTERNAL_LIBRARY_ERROR**

* 이 오류는 NHN Cloud IAP 라이브러리에서 오류가 발생했을 때 반환됩니다.
* NHN Cloud IAP 라이브러리에서 발생한 오류 정보는 상세 오류에 포함되어 있으며 상세한 오류 코드 및 메시지는 다음과 같이 확인할 수 있습니다. 

```java
Gamebase.Purchase.requestPurchase(activity, gamebaseProductId, new GamebaseDataCallback<PurchasableReceipt>() {
    @Override
    public void onCallback(PurchasableReceipt data, GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            Log.d(TAG, "Purchase successful");
            ...
        } else {
            Log.e(TAG, "Purchase failed");

            // Gamebase Error Info
            int errorCode = exception.getCode();
            String errorMessage = exception.getMessage();
            
            if (errorCode == GamebaseError.PURCHASE_EXTERNAL_LIBRARY_ERROR) {
                // IAP Error Info
                int moduleErrorCode = exception.getDetailCode();
                String moduleErrorMessage = exception.getDetailMessage();
                
                ...
            }
        }
    }
});
```

* NHN Cloud IAP SDK 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [NHN Cloud > NHN Cloud SDK 사용 가이드 > NHN Cloud IAP > Android > 오류 코드](https://docs.toast.com/en/TOAST/en/toast-sdk/iap-android/#error-codes)
