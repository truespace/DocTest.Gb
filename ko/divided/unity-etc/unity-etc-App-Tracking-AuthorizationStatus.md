---
source: unity-etc.md
section: "App Tracking AuthorizationStatus"
order: 7
created_date: 2026-04-03
---

### App Tracking AuthorizationStatus

* ATT 활성화 여부를 확인합니다.

* AUTHORIZED: 앱의 추적 요청 허용 동의, iOS 14 미만 기기에서는 항상 AUTHORIZED를 반환
* DENIED: 앱의 추적 요청 허용 거부
* NOT_DETERMINED: 앱의 추적 요청 허용 미결정
* RESTRICTED: 앱의 추적 요청 제한
* UNKNOWN: 다른 OS이거나 OS에서 정의되지 않은 경우

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS

```cs
namespace Toast.Gamebase
{
    public enum GamebaseAppTrackingAuthorizationStatus
    {
        AUTHORIZED,
        DENIED,
        NOT_DETERMINED,
        RESTRICTED,
        UNKNOWN
    }
}

static Toast.Gamebase.GamebaseAppTrackingAuthorizationStatus GetAppTrackingAuthorizationStatus();
```

**Example**

``` cs
public void GetAppTrackingAuthorizationStatusSample()
{
#if UNITY_IOS
    switch (Gamebase.Util.GetAppTrackingAuthorizationStatus() ) iOS only
    {
        case GamebaseAppTrackingAuthorizationStatus.AUTHORIZED:
        {
        }
        break; 
        
        case GamebaseAppTrackingAuthorizationStatus.DENIED:
        {
        }
        break;
        
        case GamebaseAppTrackingAuthorizationStatus.NOT_DETERMINED:
        {
        }
        break;
        
        case GamebaseAppTrackingAuthorizationStatus.RESTRICTED:
        {
        }
        break;
        
        case GamebaseAppTrackingAuthorizationStatus.UNKNOWN:
        {
        }
        break;
    }
#endif
}
```
