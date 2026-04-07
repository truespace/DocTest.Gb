---
source: unreal-push.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, Push, Error, IsSuccess"
section: "Error Handling"
order: 6
---

### Error Handling

| Error                          | Error Code | Description                              |
| ------------------------------ | ---------- | ---------------------------------------- |
| PUSH_EXTERNAL_LIBRARY_ERROR    | 5101       | NHN Cloud Push 라이브러리 오류입니다.<br/>상세 오류를 확인하십시오. |
| PUSH_ALREADY_IN_PROGRESS_ERROR | 5102       | 이전 푸시 API 호출이 완료되지 않았습니다.<br>이전 푸시 API의 콜백이 실행된 이후에 다시 호출하세요. |
| PUSH_UNKNOWN_ERROR             | 5999       | 정의되지 않은 푸시 오류입니다.<br>전체 로그를 [고객 센터](https://toast.com/support/inquiry)에 올려 주시면 가능한 한 빠르게 답변 드리겠습니다. |

* 전체 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [오류 코드](../error-code.md#client-sdk)

**PUSH_EXTERNAL_LIBRARY_ERROR**

* 이 오류는 NHN Cloud Push 라이브러리에서 오류가 발생했을 때 반환됩니다.
* NHN Cloud Push 라이브러리에서 발생한 오류 정보는 상세 오류에 포함되어 있으며 상세한 오류 코드 및 메시지는 다음과 같이 확인할 수 있습니다. 

```cpp
GamebaseError* gamebaseError = Error; // GamebaseError object via callback

if (Gamebase::IsSuccess(Error))
{
    // succeeded
}
else
{
    UE_LOG(LogTemp, Display, TEXT("code: %d, message: %s"), Error->Code, *Error->Message);

    GamebaseInnerError* moduleError = gamebaseError.Error; // GamebaseError.Error object from external module
    if (moduleError.Code != GamebaseErrorCode::SUCCESS)
    {
        UE_LOG(LogTemp, Display, TEXT("moduleErrorCode: %d, moduleErrorMessage: %s"), moduleerror->Code, *moduleerror->Message);
    }
}
```

* NHN Cloud Push 오류 코드를 확인하시기 바랍니다.
    * [Android](../aos-push.md#Error-handling)
    * [iOS](../ios-push.md#Error-handling)
