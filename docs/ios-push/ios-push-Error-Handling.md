---
source: ios-push.md
split: true
created_date_time: 20260406_141859
keyword: "Error Handling"
section: "Error Handling"
order: 7
---

### Error Handling

| Error                                    | Error Code | Description                              |
| ---------------------------------------- | ---------- | ---------------------------------------- |
| TCGB_ERROR_PUSH_EXTERNAL_LIBRARY_ERROR   | 5101       | NHN Cloud Push 라이브러리 오류입니다.<br/>상세 오류를 확인하십시오. |
| TCGB_ERROR_PUSH_ALREADY_IN_PROGRESS_ERROR | 5102       | 이전 푸시 API 호출이 완료되지 않았습니다.<br>이전 푸시 API의 콜백이 실행된 이후에 다시 호출하세요. |
| TCGB_ERROR_PUSH_UNKNOWN_ERROR            | 5999       | 정의되지 않은 푸시 오류입니다.<br>전체 로그를 [고객 센터](https://toast.com/support/inquiry)에 올려 주시면 가능한 한 빠르게 답변 드리겠습니다. |

**TCGB_ERROR_PUSH_EXTERNAL_LIBRARY_ERROR**

* 이 오류는 NHN Cloud Push 라이브러리에서 오류가 발생했을 때 반환됩니다.
* NHN Cloud Push 라이브러리에서 발생한 오류 정보는 상세 오류에 포함되어 있으며 상세한 오류 코드 및 메시지는 다음과 같이 확인할 수 있습니다. 

```objectivec
TCGBError *tcgbError = error; // TCGBError object via callback

NSInteger detailErrorCode = [error detailErrorCode];
NSString *detailErrorMessage = [error detailErrorMessage];

// If you use **description** method, you can get entire information of this object by JSON Format
NSLog(@"TCGBError: %@", [tcgbError description]);
```


* NHN Cloud Push 오류 코드는 다음과 같습니다.
    
| 오류 코드 |  설명 |
| --- | --- |
| NHNCloudPushErrorUnknown |           알 수 없음 |
| NHNCloudPushErrorNotInitialized |    초기화하지 않음 |
| NHNCloudPushErrorUserInvalid |       사용자 아이디 미설정 |
| NHNCloudPushErrorPermissionDenied |  권한 획득 실패 |
| NHNCloudPushErrorSystemFailed |      시스템에 의한 실패 |
| NHNCloudPushErrorTokenInvalid |      토큰 값이 없거나 유효하지 않음 |
| NHNCloudPushErrorAlreadyInProgress | 이미 진행 중 |
| NHNCloudPushErrorParameterInvalid |  매개변수 오류 |
| NHNCloudPushErrorNotSupported |      지원하지 않는 기능 |
| NHNCloudPushErrorClientFailed |      서버 오류 |
