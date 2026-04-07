---
source: unity-push.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, Push, Additional, SetSandboxMode, isSandbox, SetSandboxModeSample"
section: "Event Handling"
order: 5
---

### Event Handling

* 푸시 메시지가 도착했거나 푸시 메시지를 클릭했을 때 이벤트를 처리할 수 있습니다.
* 이벤트 등록 방법은 GamebaseEventHandler 가이드를 참고하시기 바랍니다.
    * [ Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Push Received Message](../unity-etc.md#push-received-message)
    * [ Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Push Click Message](../unity-etc.md#push-click-message)
    * [ Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Push Click Action](../unity-etc.md#push-click-action)

#### Setting for APNS Sandbox
* SandboxMode를 켜면, APNS Sandbox로 Push를 발송하도록 등록할 수 있습니다.
* 콘솔 발송 방법
    * Push 메뉴의 **대상**에서 **iOS Sandbox**를 선택한 후 발송합니다.

**API**

Supported Platforms

<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS

```cs
public static void SetSandboxMode(bool isSandbox)
```

**Example**

```cs
public void SetSandboxModeSample()
{
    Gamebase.Push.SetSandboxMode(true);
}
```
