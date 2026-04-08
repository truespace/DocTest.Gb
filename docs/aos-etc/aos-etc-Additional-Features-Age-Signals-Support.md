---
source: aos-etc.md
section: "Additional Features > Age Signals Support"
order: 7
split: true
created_date_time: 20260408_191848
keyword: Android, Error, Alert
---

### Age Signals Support

Texas SB 2420 및 유사한 주 법률은 미성년자 보호를 위해 앱에서 사용자의 연령 확인을 요구합니다.
Gamebase는 Google Play Age Signals API를 래핑하여 이러한 요구사항을 충족할 수 있는 API를 제공합니다.

#### Dependencies

SDK 내부적으로 아래 의존성을 갖습니다.

`implementation 'com.google.android.play:age-signals'`

#### Requirements

* 최소 Android API Level: API 23 (Android 6.0) 이상
* Gamebase SDK 버전: 2.78.0 이상

#### Google guide

자세한 내용은 Play Age Signals 가이드의 [개요](https://developer.android.com/google/play/age-signals)를 참고하세요.


> <font color="red">[주의]</font><br/>
>
> Play Age Signals API (베타)는 2026년 1월 1일까지 예외를 발생시킵니다. 1월 1일부터 API는 실시간 응답을 반환합니다.
>

#### Check age signal

**Gamebase.AgeSignals.checkAgeSignals(Context, GamebaseAgeSignalsRequest)**를 호출하여 연령 정보를 확인합니다.

**GamebaseAgeSignalsRequest**

| API | Mandatory(M) / Optional(O) | Description |
| --- | --- | --- |
| newBuilder() | **M** | GamebaseAgeSignalsRequest 객체는 newBuilder() 함수를 통해 생성할 수 있습니다. |
| build() | **M** | 설정을 마친 Builder를 Request 객체로 변환합니다. |

**API**

```java
+ (void)Gamebase.AgeSignals.checkAgeSignals(@NonNull Context context,
                                            @NonNull GamebaseAgeSignalsRequest request,
                                            @NonNull GamebaseDataCallback<GamebaseAgeSignalsResult> callback) 
```

**ErrorCode**

| Error Code | Description |
| --- | --- |
| NOT\_SUPPORTED(10)                   | Android API 23 미만 기기에서 호출되었습니다. |
| AUTH\_EXTERNAL\_LIBRARY\_ERROR(3009) | Google Play Age Signals API에서 오류를 반환했습니다. |


**Example**

```kotlin
// Age Signals 요청 생성
val request = GamebaseAgeSignalsRequest.newbuilder().build()

// Age Signals 확인 요청
Gamebase.AgeSignals.checkAgeSignals(context, request) { result, exception ->
    if (Gamebase.isSuccess(exception)) {
        // 성공: 연령 확인 정보 처리
        handleAgeSignalsResult(result)
    } else {
        // 실패: 오류 처리

        val errorCode = exception?.code
        val errorMessage = exception?.message
        when (errorCode) {
            GamebaseError.NOT_SUPPORTED -> {
                // Android API 23 미만 기기에서는 지원되지 않습니다.
                Log.e(TAG, "Age Signals API is not supported on this device")
            }
            GamebaseError.AUTH_EXTERNAL_LIBRARY_ERROR -> {
                // Google Play 서비스에서 오류가 발생하였습니다.

                Log.e(TAG, "Google Play Age Signals error: $errorMessage")
            }
        }
    }
}
```

#### Handle results

**GamebaseAgeSignalsResult.userStatus()**로 유저의 상태를 확인할 수 있습니다.
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

```kotlin
private fun handleAgeSignalsResult(result: GamebaseAgeSignalsResult) {
    val userStatus = result.userStatus()

    if (userStatus == null) {
        // 사용자가 규제 지역(텍사스, 유타, 루이지애나)에 있지 않음을 의미합니다.
        // 규제 대상이 아닌 사용자에 대한 앱의 로직을 진행할 수 있습니다.
        return
    }

    when (userStatus) {
        GamebaseAgeSignalsVerificationStatus.VERIFIED -> {
            // 18세 이상 성인 사용자
            // 모든 기능에 대한 접근 허용
            // ageLower와 ageUpper는 null입니다.

            handleAdultUser(result)
        }
        GamebaseAgeSignalsVerificationStatus.SUPERVISED -> {
            // 보호자 동의가 있는 미성년자
            // Texas SB 2420에 따라 미성년자를 위한 제한된 기능 제공

            // 연령대를 확인할 수 있습니다.
            val ageLower = result.ageLower() // 예: 13
            val ageUpper = result.ageUpper() // 예: 17
            val installId = result.installId()
            handleSupervisedMinor(result)
        }
        GamebaseAgeSignalsVerificationStatus.SUPERVISED_APPROVAL_PENDING -> {
            // 보호자 승인을 기다리는 동안 제한된 기능만 제공
            // 사용자에게 승인 대기 중임을 알림
            handleApprovalPending(result)
        }
        GamebaseAgeSignalsVerificationStatus.SUPERVISED_APPROVAL_DENIED -> {
            // 보호자가 승인을 거부한 경우
            // 제한된 기능만 제공하거나 서비스 이용 불가 안내
            handleApprovalDenied(result)
        }
        GamebaseAgeSignalsVerificationStatus.UNKNOWN -> {
            // 해당 관할 지역에서 검증되지 않은 사용자 또는 연령 확인 정보를 사용할 수 없는 경우
            // 사용자에게 Play 스토어를 방문하여 상태를 해결하도록 요청하세요.
            handleUnknownUser(result)
        }
        else -> {
          // 이 케이스를 로깅하여 잠재적인 미래 상태에 대해서도 유연하게 처리할 수 있도록 합니다.
        }
    }
}
```

**GamebaseAgeSignalsResult**

자세한 내용은 Play Age Signals 가이드의 [연령 신호 응답](https://developer.android.com/google/play/age-signals/use-age-signals-api#age-signals-responses)을 참고하세요.
