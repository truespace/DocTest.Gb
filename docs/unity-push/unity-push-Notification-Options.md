---
source: unity-push.md
split: true
created_date_time: 20260406_141859
keyword: "Notification Options"
section: "Notification Options"
order: 3
---

### Notification Options

* 단말기에 표시하는 알림을 어떤 형태로 표시할 것인지 Notification Options 를 통해 변경할 수 있습니다.
* 런타임에 registerPush API를 호출하여 변경할 수 있습니다.

#### Set Notification Options with RegisterPush in Runtime

RegisterPush API 호출 시 GamebaseRequest.Push.NotificationOptions 인자를 추가하여 알림 옵션을 설정할 수 있습니다.
GamebaseRequest.Push.NotificationOptions 의 생성자에 Gamebase.Push.GetNotificationOptions() 호출 결과를 전달하면 현재의 알림 옵션으로 초기화된 오브젝트가 생성되므로 필요한 값만 변경할 수 있습니다.<br/>
설정 가능한 값은 아래와 같습니다.

| API                    | Parameter       | Description        |
| ---------------------  | ------------ | ------------------ |
| foregroundEnabled      | bool         | 앱이 포그라운드 상태일 때의 알림 노출 여부<br/>**default**: false |
| badgeEnabled           | bool         | 배지 아이콘 사용 여부<br/>**default**: true |
| soundEnabled           | bool         | 알림음 사용 여부<br/>**default**: true<br/>**iOS에 한함** |
| priority               | int          | 알림 우선 순위. 아래 5가지 값을 설정할 수 있습니다.<br/>GamebaseNotificationPriority.MIN : -2<br/> GamebaseNotificationPriority.LOW : -1<br/>GamebaseNotificationPriority.DEFAULT : 0<br/>GamebaseNotificationPriority.HIGH : 1<br/>GamebaseNotificationPriority.MAX : 2<br/>**default**: GamebaseNotificationPriority.HIGH<br/>**Android에 한함** |
| smallIconName          | string       | 알림용 작은 아이콘 파일 이름.<br/>설정하지 않을 경우 앱 아이콘이 사용됩니다.<br/>**default**: null<br/>**Android에 한함** |
| soundFileName          | string       | 알림음 파일 이름. Android 8.0 미만 OS에서만 동작합니다.<br/>'res/raw' 폴더의 mp3, wav 파일명을 지정하면 알림음이 변경됩니다.<br/>**default**: null<br/>**Android에 한함** |

**Example**

```cs
public void RegisterPush(bool pushEnabled, bool adAgreement, bool adAgreementNight, bool requestNotificationPermission, bool alwaysAllowTokenRegistration)
{
    GamebaseRequest.Push.PushConfiguration pushConfiguration = new GamebaseRequest.Push.PushConfiguration
    {
        pushEnabled = pushEnabled,
        adAgreement = adAgreement,
        adAgreementNight = adAgreementNight,
        requestNotificationPermission = requestNotificationPermission,
        alwaysAllowTokenRegistration = alwaysAllowTokenRegistration
    };

    var notificationOptions = new GamebaseRequest.Push.NotificationOptions
    {
        foregroundEnabled = true,
        priority = GamebaseNotificationPriority.HIGH
    };

    Gamebase.Push.RegisterPush(configuration, notificationOptions, (error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            Debug.Log("RegisterPush succeeded.");
        }
        else
        {
            // Check the error code and handle the error appropriately.
            Debug.Log(string.Format("RegisterPush failed. error is {0}", error));
        }
    });
}
```

#### Get NotificationOptions

푸시를 등록할 때 기존에 설정했던 알림 옵션값을 가져옵니다.

**API**

Supported Platforms

<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

```cs
public static GamebaseResponse.Push.NotificationOptions GetNotificationOptions();
```

**Example**

```cs
public void GetNotificationOptionsSample()
{
    GamebaseResponse.Push.NotificationOptions notificationOptions = Gamebase.Push.GetNotificationOptions();

    GamebaseRequest.Push.NotificationOptions options = new GamebaseRequest.Push.NotificationOptions(notificationOptions);
    options.foregroundEnabled = true;
    options.smallIconName = "notification_icon_name";

    GamebaseRequest.Push.PushConfiguration configuration = new GamebaseRequest.Push.PushConfiguration();
    Gamebase.Push.RegisterPush(configuration, options, (error)=> { });
}
```
