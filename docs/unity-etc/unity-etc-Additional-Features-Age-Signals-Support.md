---
source: unity-etc.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, Error, GetAgeSignal, IsSuccess"
section: "Additional Features > Age Signals Support"
order: 9
---

### Age Signals Support

Texas SB 2420 및 유사한 주 법률은 미성년자 보호를 위해 앱에서 사용자의 연령 확인을 요구합니다.
Gamebase는 Google Play Age Signals API를 래핑하여 이러한 요구사항을 충족할 수 있는 API를 제공합니다.

Android에서 Age Signals 기능을 설정하는 방법은 다음 문서를 참고하세요.<br/>
* [Android Age Signals](../../aos-etc.md#age-signals-support)<br/>
  
Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

#### GetAgeSignal

연령 정보를 확인합니다.

**API**

```cs
static void GetAgeSignal(GamebaseCallback.GamebaseDelegate<GamebaseResponse.Util.AgeSignalResult> callback)
```

**ErrorCode**

| Error Code | Description |
| --- | --- |
| NOT\_SUPPORTED(10)                   | Android API 23 미만 기기에서 호출되었습니다. | 
| AUTH\_EXTERNAL\_LIBRARY\_ERROR(3009) | Google Play Age Signals API에서 오류를 반환했습니다. | 


**Handle results**

AgeSignalResult.userStatus로 유저의 상태를 확인할 수 있습니다.
Status 값에 따라 사용자 규제 여부를 판단하시기 바랍니다.

**GamebaseAgeSignalsVerificationStatus**

사용자 검증 상태 상수입니다.

| Status                        | Code | Description          | 
| ----------------------------- | ---- | -------------------- | 
| VERIFIED                      | 0    | 18세 이상 성인          | 
| SUPERVISED                    | 1    | 보호자 동의가 있는 미성년자 | 
| SUPERVISED\_APPROVAL\_PENDING | 2    | 보호자 승인 대기 중       | 
| SUPERVISED\_APPROVAL\_DENIED  | 3    | 보호자 승인 거부됨        | 
| UNKNOWN                       | 4    | 검증되지 않은 사용자       | 


**Example**

``` cs
public static void SampleGetAgeSignal()
{
    Gamebase.Util.GetAgeSignal((data, error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            HandleAgeSignalsResult(data);
        }
        else
        {
            var errorCode = error.code;
            var errorMessage = error.message;
            switch (errorCode)
            {
                case GamebaseErrorCode.NOT_SUPPORTED:
                    // Android API 23 미만 기기에서는 지원되지 않습니다.
                    Debug.LogError("Age Signals API is not supported on this device");
                    break;
                case GamebaseErrorCode.AUTH_EXTERNAL_LIBRARY_ERROR:
                    // Google Play 서비스에서 오류가 발생했습니다. 
                    Debug.LogErrorFormat("Google Play Age Signals error: {0}", errorMessage);
                    break;
            }
        }
    });
}

private static void HandleAgeSignalsResult(GamebaseResponse.Util.AgeSignalResult result)
{
    if(result.userStatus.HasValue == false)
    {
        // 사용자가 규제 지역(텍사스, 유타, 루이지애나)에 있지 않음을 의미합니다.
        // 규제 대상이 아닌 사용자에 대한 앱의 로직을 진행할 수 있습니다.
        return;
    }
    
    GamebaseAgeSignalsVerificationStatus userStatus = (GamebaseAgeSignalsVerificationStatus)result.userStatus.Value;
    switch (userStatus)
    {
        case GamebaseAgeSignalsVerificationStatus.VERIFIED:
            // 18세 이상 성인 사용자
            // 모든 기능에 대한 접근 허용
            // ageLower와 ageUpper는 null입니다.
            HandleAdultUser(result);
            break;
        case GamebaseAgeSignalsVerificationStatus.SUPERVISED:
            // 보호자 동의가 있는 미성년자
            // Texas SB 2420에 따라 미성년자를 위한 제한된 기능 제공

            // 연령대를 확인할 수 있습니다.
            var ageLower = result.ageLower.Value; // 예: 13
            var ageUpper = result.ageUpper.Value; // 예: 17
            var installId = result.installId;
            HandleSupervisedMinor(result);
            break;
        case GamebaseAgeSignalsVerificationStatus.SUPERVISED_APPROVAL_PENDING:
            // 보호자 승인을 기다리는 동안 제한된 기능만 제공
            // 사용자에게 승인 대기 중임을 알림
            HandleApprovalPending(result);
            break;
        case GamebaseAgeSignalsVerificationStatus.SUPERVISED_APPROVAL_DENIED:
            // 보호자가 승인을 거부한 경우
            // 제한된 기능만 제공하거나 서비스 이용 불가 안내
            HandleApprovalDenied(result);
            break;
        case GamebaseAgeSignalsVerificationStatus.UNKNOWN:
            // 해당 관할 지역에서 검증되지 않은 사용자 또는 연령 확인 정보를 사용할 수 없는 경우
            // 사용자에게 Play 스토어를 방문하여 상태를 해결하도록 요청하세요.
            HandleUnknownUser(result);
            break;
    }
}
```
