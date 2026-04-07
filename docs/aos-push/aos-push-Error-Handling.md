---
source: aos-push.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Push, Error, isSuccess, getMessage, getDetailCode, getDetailMessage"
section: "Error Handling"
order: 6
---

### Error Handling

| Error                          | Error Code | Description                              |
| ------------------------------ | ---------- | ---------------------------------------- |
| PUSH_EXTERNAL_LIBRARY_ERROR    | 5101       | NHN Cloud Push 라이브러리 오류입니다.<br>상세 오류를 확인하십시오. |
| PUSH_ALREADY_IN_PROGRESS_ERROR | 5102       | 이전 푸시 API 호출이 완료되지 않았습니다.<br>이전 푸시 API의 콜백이 실행된 이후에 다시 호출하세요. |
| PUSH_UNKNOWN_ERROR             | 5999       | 정의되지 않은 푸시 오류입니다.<br>전체 로그를 [고객 센터](https://toast.com/support/inquiry)에 올려 주시면 가능한 한 빠르게 답변 드리겠습니다. |

* 전체 오류 코드는 다음을 참고하시기 바랍니다.
    * [오류 코드](../../error-code.md#client-sdk)

**PUSH_EXTERNAL_LIBRARY_ERROR**

* 이 오류는 NHN Cloud Push 라이브러리에서 오류가 발생했을 때 반환됩니다.
* NHN Cloud Push 라이브러리에서 발생한 오류 정보는 상세 오류에 포함되어 있으며 상세한 오류 코드 및 메시지는 다음과 같이 확인할 수 있습니다. 

```java
Gamebase.Push.registerPush(activity, pushConfiguration, new GamebaseCallback() {
    @Override
    public void onCallback(GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            Log.d(TAG, "Register push successful");
            ...
        } else {
            Log.e(TAG, "Register push failed");

            // Gamebase Error Info
            int errorCode = exception.getCode();
            String errorMessage = exception.getMessage();
            
            if (errorCode == GamebaseError.PUSH_EXTERNAL_LIBRARY_ERROR) {
                // TOAST Push Error Info
                int moduleErrorCode = exception.getDetailCode();
                String moduleErrorMessage = exception.getDetailMessage();
                
                ...
            }
        }
    }
});
```

* NHN Cloud Push SDK 의 오류 코드는 다음과 같습니다.

| Error | Error Code | Description |
| --- | --- | --- |
| OK | 0 | API 호출 성공 |
| NOT_INITIALIZE | 100 | NHN Cloud SDK 또는 NHN Cloud Push SDK가 초기화되지 않은 경우 |
| PROVIDER_SDK_ERROR | 101 | 외부 SDK(Firebase)에서 오류가 발생한 경우 |
| USER_ID_NOT_REGISTERED | 102 | 로그인하지 않은 경우 |
| UNSUPPORTED_PUSH_TYPE | 103 | PushType을 잘못 입력했거나 푸시 라이브러리가 프로젝트에 포함되지 않은 경우 |
| API_SERVER_ERROR | 104 | NHN Cloud Push 서버 API 호출에 실패한 경우 |
| TOKEN_NOT_REGISTERED | 105 | 내부에 캐시된 푸시 토큰이 없는 경우 |
| INVALID_PARAMETER | 106 | 잘못된 파라미터인 경우 |
