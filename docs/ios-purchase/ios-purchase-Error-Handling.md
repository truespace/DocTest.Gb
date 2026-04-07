---
source: ios-purchase.md
split: true
created_date_time: 20260406_141859
keyword: "Error Handling"
section: "Error Handling"
order: 12
---

### Error Handling

| Error                                                | Error Code | Description                              |
| ---------------------------------------------------- | ---------- | ---------------------------------------- |
| TCGB_ERROR_NOT_SUPPORTED                             | 10         | GamebaseAdapter가 포함되지 않았습니다.<br/>Error 객체의 도메인이 "TCGB.Gamebase.TCGBPurchase" 인 경우, PurchaseAdapter의 존재 유무를 확인해주시길 바랍니다. |
| TCGB_ERROR_PURCHASE_NOT_INITIALIZED                  | 4001       | Gamebase PurchaseAdapter가 초기화되지 않았습니다.   |
| TCGB_ERROR_PURCHASE_USER_CANCELED                    | 4002       | 구매가 취소되었습니다.                             |
| TCGB_ERROR_PURCHASE_NOT_FINISHED_PREVIOUS_PURCHASING | 4003       | 이전 구매가 완료되지 않았습니다.                       |
| TCGB_ERROR_PURCHASE_NOT_ENOUGH_CASH                  | 4004       | 해당 스토어의 캐쉬가 부족하여 결제할 수 없습니다.             |
| TCGB_ERROR_PURCHASE_INACTIVE_PRODUCT_ID              | 4005       | 해당 상품이 활성화 상태가 아닙니다.             |
| TCGB_ERROR_PURCHASE_NOT_EXIST_PRODUCT_ID             | 4006       | 존재하지 않은 GamebaseProductID로 결제를 요청하였습니다.             |
| TCGB_ERROR_PURCHASE_LIMIT_EXCEEDED                   | 4007       | 월 구매 한도를 초과했습니다.             |
| TCGB_ERROR_PURCHASE_PENDING                          | 4008       | 결제를 완료하려면 추가 확인이 필요합니다. |
| TCGB_ERROR_PURCHASE_NOT_SUPPORTED_MARKET             | 4010       | 지원하지 않는 스토어입니다. iOS의 지원가능한 스토어는 "AS"입니다. |
| TCGB_ERROR_PURCHASE_EXTERNAL_LIBRARY_ERROR           | 4201       | NHN Cloud IAP 라이브러리 오류입니다.<br/>상세 오류를 확인하십시오. |
| TCGB_ERROR_PURCHASE_UNKNOWN_ERROR                    | 4999       | 정의되지 않은 구매 오류입니다.<br>전체 로그를 [고객 센터](https://toast.com/support/inquiry)에 올려 주시면 가능한 한 빠르게 답변 드리겠습니다. |

* 전체 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [오류 코드](../../error-code.md#client-sdk)



**TCGB_ERROR_PURCHASE_EXTERNAL_LIBRARY_ERROR**

* 이 오류는 NHN Cloud IAP 라이브러리에서 오류가 발생했을 때 반환됩니다.
* NHN Cloud IAP 라이브러리에서 발생한 오류 정보는 상세 오류에 포함되어 있으며 상세한 오류 코드 및 메시지는 다음과 같이 확인할 수 있습니다. 


```objectivec
TCGBError *tcgbError = error; // TCGBError object via callback

NSInteger detailErrorCode = [error detailErrorCode];
NSString *detailErrorMessage = [error detailErrorMessage];

// If you use **description** method, you can get entire information of this object by JSON Format
NSLog(@"TCGBError: %@", [tcgbError description]);
```

* NHN Cloud IAP 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [NHN Cloud > NHN Cloud SDK 사용 가이드 > NHN Cloud IAP > iOS > 오류 코드](https://docs.toast.com/en/TOAST/en/toast-sdk/iap-ios/#error-codes)
