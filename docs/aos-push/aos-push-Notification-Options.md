---
source: aos-push.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Push, Notification, getNotificationOptions, setPriority, setSmallIconName, setSoundFileName, isSuccess"
section: "Notification Options"
order: 3
---

### Notification Options

* 단말기에 표시하는 알림을 어떤 형태로 표시할 것인지 Notification Options 를 통해 변경할 수 있습니다.
* Notification Options 는 AndroidManifest.xml 에 설정하거나 런타임에 registerPush API를 호출하여 변경할 수 있습니다.

#### Set Notification Options with AndroidManifest.xml

알림 옵션은 AndroidManifest.xml 에 정의하여 설정할 수 있습니다.<br/>
설정 방법은 아래 가이드를 확인해주시기 바랍니다.

[Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > Notification Options](../aos-started.md#notification-options)

#### Set Notification Options with RegisterPush in Runtime

알림 옵션을 AndroidManifest.xml 에 정의하지 않고 런타임에 설정할 수도 있습니다. 또는 AndroidManifest.xml 에 정의한 값을 런타임에 변경할 수도 있습니다.
registerPush API 호출 시 GamebaseNotificationOptions 인자를 추가하여 알림 옵션을 설정합니다.
GamebaseNotificationOptions.newBuilder() 의 인자로 Gamebase.Push.getNotificationOptions() 호출 결과를 전달하면, 현재의 알림 옵션으로 초기화 된 Builder 가 생성되므로, 필요한 값만 변경할 수 있습니다.<br/>
설정 가능한 값은 아래와 같습니다.

| API                   | Parameter       | Description        |
| --------------------  | ------------ | ------------------ |
| enableForeground      | boolean      | 앱이 포그라운드 상태일 때의 알림 노출 여부<br/>**default**: false |
| enableBadge           | boolean      | 배지 아이콘 사용 여부<br/>**default**: true |
| setPriority           | int          | 알림 우선 순위. 아래 5가지 값을 설정할 수 있습니다.<br/>NoticationComapt.PRIORITY_MIN : -2<br/> NoticationComapt.PRIORITY_LOW : -1<br/>NoticationComapt.PRIORITY_DEFAULT : 0<br/>NoticationComapt.PRIORITY_HIGH : 1<br/>NoticationComapt.PRIORITY_MAX : 2<br/>**default**: NoticationComapt.HIGH |
| setSmallIconName         | String       | 알림용 작은 아이콘 파일 이름.<br/>설정하지 않을 경우 앱 아이콘이 사용됩니다.<br/>**default**: null |
| setSoundFileName      | String       | 알림음 파일 이름. Android 8.0 미만 OS에서만 동작합니다.<br/>'res/raw' 폴더의 mp3, wav 파일명을 지정하면 알림음이 변경됩니다.<br/>**default**: null |

**Example**

```java
boolean enableForeground;
boolean enableBadge;
// NotificationCompat.PRIORITY_MIN     : -2
// NotificationCompat.PRIORITY_LOW     : -1
// NotificationCompat.PRIORITY_DEFAULT :  0
// NotificationCompat.PRIORITY_HIGH    :  1
// NotificationCompat.PRIORITY_MAX     :  2
int priority;
String smallIconName;
String soundFileName;

GamebaseNotificationOptions currentOptions = Gamebase.Push.getNotificationOptions(activity);
GamebaseNotificationOptions notificationOptions = GamebaseNotificationOptions.newBuilder(currentOptions)
        .enableForeground(enableForeground)
        .enableBadge(enableBadge)
        .setPriority(priority)
        .setSmallIconName(smallIconName)
        .setSoundFileName(soundFileName)
        .build();

Gamebase.Push.registerPush(activity, pushConfiguration, notificationOptions, new GamebaseCallback() {
    @Override
    public void onCallback(GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            // Succeeded.
        } else {
            // Failed.
        }
    }
});
```

#### Get NotificationOptions

푸시를 등록할 때 기존에 설정했던 알림 옵션값을 가져옵니다.
AndroidManifest.xml 에 설정한 값과 런타임에 변경된 값을 포함하여 가장 최근 설정을 가져옵니다.

**API**

```java
+ (GamebaseNotificationOptions)Gamebase.Push.getNotificationOptions(@NonNull Context context);
```
