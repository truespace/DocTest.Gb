---
source: unreal-push.md
section: "Event Handling"
order: 5
split: true
created_date_time: 20260408_184906
keyword: Unreal, Push, iOS, Console
---

### Event Handling

* 푸시 메시지가 도착했거나 푸시 메시지를 클릭했을 때 이벤트를 처리할 수 있습니다.
* 이벤트 등록 방법은 GamebaseEventHandler 가이드를 참고하시기 바랍니다.
    * [ Game > Gamebase > Unreal SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Push Received Message](../unreal-etc.md#push-received-message)
    * [ Game > Gamebase > Unreal SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Push Click Message](../unreal-etc.md#push-click-message)
    * [ Game > Gamebase > Unreal SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > Push Click Action](../unreal-etc.md#push-click-action)


#### Setting for APNS Sandbox

* SandboxMode를 켜면, APNS Sandbox로 Push를 발송하도록 등록할 수 있습니다.
* 콘솔 발송 방법
    * Push 메뉴의 **대상**에서 **iOS Sandbox**를 선택한 후 발송합니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void SetSandboxMode(bool isSandbox);
```

**Example**

```cpp
void USample::SetSandboxMode(bool bIsSandbox)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetPush()->SetSandboxMode(bIsSandbox);
}
```
