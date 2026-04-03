---
source: unreal-etc.md
section: "App Tracking AuthorizationStatus"
order: 7
created_date: 2026-04-03
---

### App Tracking AuthorizationStatus

* ATT 활성화 여부를 확인합니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
UENUM(BlueprintType)
enum class EGamebaseAppTrackingAuthorizationStatus : uint8
{
    
    Authorized,     // 앱의 추적 요청 허용 동의, iOS 14 미만 기기에서는 항상 Authorized를 반환
    Denied,         // 앱의 추적 요청 허용 거부
    NotDetermined,  // 앱의 추적 요청 허용 미결정
    Restricted,     // 앱의 추적 요청 제한
    Unknown         // 다른 OS이거나 OS에서 정의되지 않은 경우
};

EGamebaseAppTrackingAuthorizationStatus GetAppTrackingAuthorizationStatus();
```

**Example**

```cpp
void USample::GetAppTrackingAuthorizationStatus()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    EGamebaseAppTrackingAuthorizationStatus Status = Subsystem->GetUtil()->GetAppTrackingAuthorizationStatus();
    
    switch (Status)
    {
    case EGamebaseAppTrackingAuthorizationStatus::Authorized:
        break;
    case EGamebaseAppTrackingAuthorizationStatus::Denied:
        break;
    case EGamebaseAppTrackingAuthorizationStatus::NotDetermined:
        break;
    case EGamebaseAppTrackingAuthorizationStatus::Restricted:
        break;
    case EGamebaseAppTrackingAuthorizationStatus::Unknown:
        break;
    }
    
}
```
