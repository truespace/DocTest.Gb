---
source: unreal-etc.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, Error, GetAgeSignal, GetSubsystem, GetGameInstance, IsSuccess"
section: "Additional Features > Age Signals Support"
order: 9
---

### Age Signals Support

Texas SB 2420 및 유사한 주 법률은 미성년자 보호를 위해 앱에서 사용자의 연령 확인을 요구합니다.
Gamebase는 Google Play Age Signals API를 래핑하여 이러한 요구사항을 충족할 수 있는 API를 제공합니다.

Android에서 Age Signals 기능을 설정하는 방법은 다음 문서를 참고하세요.

* [Android Age Signals](../../aos-etc.md#age-signals-support)

#### GetAgeSignal

연령 정보를 확인합니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID

```cpp
void GetAgeSignal(const FGamebaseAgeSignalResultDelegate& Callback);
```

**ErrorCode**

| Error Code | Description |
| --- | --- |
| NOT\_SUPPORTED(10)                   | Android API 23 미만 기기에서 호출되었습니다. |
| AUTH\_EXTERNAL\_LIBRARY\_ERROR(3009) | Google Play Age Signals API에서 오류를 반환했습니다. |

**Handle results**

FGamebaseAgeSignalResult의 UserStatus로 유저의 상태를 확인할 수 있습니다.
Status 값에 따라 사용자 규제 여부를 판단하시기 바랍니다.

**EGamebaseAgeSignalsVerificationStatus**

사용자 검증 상태 상수입니다.

| Status                      | Description          |
| --------------------------- | -------------------- |
| Verified                    | 18세 이상 성인          |
| Supervised                  | 보호자 동의가 있는 미성년자 |
| SupervisedApprovalPending   | 보호자 승인 대기 중       |
| SupervisedApprovalDenied    | 보호자 승인 거부됨        |
| Unknown                     | 검증되지 않은 사용자       |

**Example**

```cpp
void USample::GetAgeSignal()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetUtil()->GetAgeSignal(
        FGamebaseAgeSignalResultDelegate::CreateLambda([](const FGamebaseAgeSignalResult* AgeSignalResult, const FGamebaseError* Error)
        {
            if (Gamebase::IsSuccess(Error))
            {
                if (!AgeSignalResult->UserStatus.IsSet())
                {
                    // 사용자가 규제 지역(텍사스, 유타, 루이지애나)에 있지 않음을 의미합니다.
                    // 규제 대상이 아닌 사용자에 대한 앱의 로직을 진행할 수 있습니다.
                    UE_LOG(LogTemp, Display, TEXT("Not legally applicable"));
                }
                else
                {
                    EGamebaseAgeSignalsVerificationStatus UserStatus =
                        static_cast<EGamebaseAgeSignalsVerificationStatus>(AgeSignalResult->UserStatus.GetValue());
                    
                    switch (UserStatus)
                    {
                        case EGamebaseAgeSignalsVerificationStatus::Verified:
                        {
                            // 18세 이상 성인 사용자
                            // 모든 기능에 대한 접근 허용
                            // AgeLower와 AgeUpper는 설정되지 않음
                            UE_LOG(LogTemp, Display, TEXT("Age 18 or older"));
                            break;
                        }
                        case EGamebaseAgeSignalsVerificationStatus::Supervised:
                        {
                            // 보호자 동의가 있는 미성년자
                            // Texas SB 2420에 따라 미성년자를 위한 제한된 기능 제공
                            
                            // 연령대를 확인할 수 있습니다.
                            if (AgeSignalResult->AgeLower.IsSet() && AgeSignalResult->AgeUpper.IsSet())
                            {
                                int32 AgeLower = AgeSignalResult->AgeLower.GetValue(); // 예: 13
                                int32 AgeUpper = AgeSignalResult->AgeUpper.GetValue(); // 예: 17
                                UE_LOG(LogTemp, Display, TEXT("Supervised user, age range: %d - %d"), AgeLower, AgeUpper);
                            }

                            if (AgeSignalResult->InstallId.IsSet())
                            {
                                FString InstallId = AgeSignalResult->InstallId.GetValue();
                                UE_LOG(LogTemp, Display, TEXT("InstallId: %s"), *InstallId);
                            }
                            
                            break;
                        }
                        case EGamebaseAgeSignalsVerificationStatus::SupervisedApprovalPending:
                        {
                            // 보호자 승인을 기다리는 동안 제한된 기능만 제공
                            // 사용자에게 승인 대기 중임을 알림
                            if (AgeSignalResult->MostRecentApprovalDate.IsSet())
                            {
                                int64 ApprovalDate = AgeSignalResult->MostRecentApprovalDate.GetValue();
                                UE_LOG(LogTemp, Display, TEXT("Approval pending since: %lld"), ApprovalDate);
                            }
                            break;
                        }
                        case EGamebaseAgeSignalsVerificationStatus::SupervisedApprovalDenied:
                        {
                            // 보호자가 승인을 거부한 경우
                            // 제한된 기능만 제공하거나 서비스 이용 불가 안내
                            UE_LOG(LogTemp, Display, TEXT("Parent or guardian has denied changes"));
                            break;
                        }
                        case EGamebaseAgeSignalsVerificationStatus::Unknown:
                        {
                            // 해당 관할 지역에서 검증되지 않은 사용자 또는 연령 확인 정보를 사용할 수 없는 경우
                            // 사용자에게 Play 스토어를 방문하여 상태를 해결하도록 요청하세요.
                            UE_LOG(LogTemp, Display, TEXT("User is not verified or supervised"));
                            break;
                        }
                    }
                }
            }
            else
            {
                UE_LOG(LogTemp, Display, TEXT("GetAgeSignal failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
                
                if (Error->Code == GamebaseErrorCode::NOT_SUPPORTED)
                {
                    // Android API 23 미만 기기에서는 지원되지 않습니다.
                    UE_LOG(LogTemp, Display, TEXT("Age Signals API is not supported on this device"));
                }
                else if (Error->Code == GamebaseErrorCode::AUTH_EXTERNAL_LIBRARY_ERROR)
                {
                    // Google Play 서비스에서 오류가 발생했습니다.
                    UE_LOG(LogTemp, Display, TEXT("Google Play Age Signals error"));
                }
            }
        }));
}
```
