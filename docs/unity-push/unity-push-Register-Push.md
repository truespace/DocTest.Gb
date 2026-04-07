---
source: unity-push.md
split: true
created_date_time: 20260406_141859
keyword: "Register Push"
section: "Register Push"
order: 2
---

### Register Push

다음 API를 호출하여, NHN Cloud Push에 해당 사용자를 등록합니다.
푸시 동의 여부(enablePush), 광고성 푸시 동의 여부(enableAdPush), 야간 광고성 푸시 동의 여부(enableAdNightPush) 값을 사용자로부터 받아, 다음의 API 호출을 통해 등록을 완료합니다.

> <font color="red">[주의]</font><br/>
>
> UserID 마다 푸시 설정이 다를 수 있고, 푸시 토큰이 만료되는 경우도 발생할 수 있으므로 로그인 이후에는 매번 RegisterPush API를 호출할 것을 권장합니다.

**API**

Supported Platforms

<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

```cs
public static void RegisterPush(GamebaseRequest.Push.PushConfiguration pushConfiguration, GamebaseCallback.ErrorDelegate callback);
public static void RegisterPush(GamebaseRequest.Push.PushConfiguration pushConfiguration, GamebaseRequest.Push.NotificationOptions options, GamebaseCallback.ErrorDelegate callback);
```

#### GamebaseRequest.Push.PushConfiguration

| Parameter     | Mandatory(M) /<br/>Optional(O) | Values            | Description        |
| ------------- | ------------- | ---------------------------------- | ------------------ |
| pushEnabled                   | M             | bool         | 푸시 동의 여부 |
| adAgreement                   | M             | bool         | 광고성 푸시 동의 여부 |
| ADAgreemadAgreementNightentNight | M          | bool         | 야간 광고성 푸시 동의 여부 |
| requestNotificationPermission | O             | bool         | Android 13 이상의 OS에서 RegisterPush API를 호출했을 때 푸시 권한 요청 팝업 자동 출력 여부<br>**default**: true<br/>**Android에 한함** |
| alwaysAllowTokenRegistration  | O             | bool         | 사용자가 푸시 권한을 거부해도 토큰을 등록할지 여부<br>true로 설정할 경우 푸시 권한을 획득하지 못하더라도 토큰을 등록합니다.<br>**default**: false<br/>**iOS에 한함** |

**Example**

```cs
public void RegisterPush(bool pushEnabled, bool adAgreement, bool adAgreementNight, bool requestNotificationPermission, bool alwaysAllowTokenRegistration)
{
    GamebaseRequest.Push.PushConfiguration pushConfiguration = new GamebaseRequest.Push.PushConfiguration
    {
        pushEnabled = pushEnabled,
        adAgreement = adAgreement,
        adAgreementNight = adAgreementNight,
        displayLanguageCode = displayLanguage,
        requestNotificationPermission = requestNotificationPermission,
        alwaysAllowTokenRegistration = alwaysAllowTokenRegistration
    };

	// You should receive the above values to the logged-in user.
    Gamebase.Push.RegisterPush(pushConfiguration, (error) =>
    {
        if (Gamebase.IsSuccess(error))
        {
        	Debug.Log("RegisterPush succeeded.");
        }
        else
        {
            Debug.Log(string.Format("RegisterPush failed. error is {0}", error));
        }
    });
}
```
