---
source: unity-etc.md
section: "Gamebase Event Handler"
order: 4
created_date: 2026-04-03
---

### Gamebase Event Handler

* Gamebase는 각종 이벤트를 **GamebaseEventHandler**라는 하나의 이벤트 시스템에서 모두 처리할 수 있습니다.
* GamebaseEventHandler는 아래 API를 통해 간단하게 Listener를 추가/제거할 수 있습니다.

**API**

<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#5319E7; font-size: 10pt">■</span> UNITY_WEBGL
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
public static void Gamebase.AddEventHandler(GamebaseCallback.DataDelegate<GamebaseResponse.Event.GamebaseEventMessage> eventHandler);
public static void Gamebase.RemoveEventHandler(GamebaseCallback.DataDelegate<GamebaseResponse.Event.GamebaseEventMessage> eventHandler);
public static void Gamebase.RemoveAllEventHandler();
```

**VO**

```cs
public class GamebaseEventMessage 
{
	// Event 종류를 나타냅니다.
    // GamebaseEventCategory 클래스의 값이 할당됩니다.
    public string category;

    // 각 category 에 맞는 VO 로 변환할 수 있는 JSON String 데이터입니다.
     public string data;
}
```

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {
        case GamebaseEventCategory.IDP_REVOKED:
            {
                GamebaseResponse.Event.GamebaseEventIdPRevokedData idPRevokedData = GamebaseResponse.Event.GamebaseEventIdPRevokedData.From(message.data);
                if (idPRevokedData != null)
                {
                    ProcessIdPRevoked(idPRevokedData);
                }
                break;
            }
        case GamebaseEventCategory.LOGGED_OUT:
            {
                GamebaseResponse.Event.GamebaseEventLoggedOutData loggedData = GamebaseResponse.Event.GamebaseEventLoggedOutData.From(message.data);
                if (loggedData != null)
                {
                    // There was a problem with the access token.
                    // Call login again.
                }
                break;
            }
        case GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED:
        case GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT:
        case GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT:
            {
                GamebaseResponse.Event.GamebaseEventServerPushData serverPushData = GamebaseResponse.Event.GamebaseEventServerPushData.From(message.data);
                if (serverPushData != null)
                {
                    CheckServerPush(message.category, serverPushData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_LAUNCHING:
            {
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                if(observerData != null)
                {
                    CheckLaunchingStatus(observerData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_NETWORK:
            {
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                if (observerData != null)
                {
                    CheckNetwork(observerData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_HEARTBEAT:
            {
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                if (observerData != null)
                {
                    CheckHeartbeat(observerData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_WEBVIEW:
            {
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                if (observerData != null)
                {
                    CheckWebView(observerData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_INTROSPECT:
            {
                // Introspect error
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                int errorCode = observerData.code;
                string errorMessage = observerData.message;
                break;
            }
        case GamebaseEventCategory.PURCHASE_UPDATED:
            {
                GamebaseResponse.Event.PurchasableReceipt purchasableReceipt = GamebaseResponse.Event.PurchasableReceipt.From(message.data);
                if (purchasableReceipt != null)
                {
                    // If the user got item by 'Promotion Code',
                    // this event will be occurred.
                }
                break;
            }
        case GamebaseEventCategory.PUSH_RECEIVED_MESSAGE:
            {
                GamebaseResponse.Event.PushMessage pushMessage = GamebaseResponse.Event.PushMessage.From(message.data);
                if (pushMessage != null)
                {
                    // When you received push message.
                    
                    // By converting the extras field of the push message to JSON,
                    // you can get the custom information added by the user when sending the push.
                    // (For Android, an 'isForeground' field is included so that you can check if received in the foreground state.)
                }
                break;
            }
        case GamebaseEventCategory.PUSH_CLICK_MESSAGE:
            {
                GamebaseResponse.Event.PushMessage pushMessage = GamebaseResponse.Event.PushMessage.From(message.data);
                if (pushMessage != null)
                {
                    // When you clicked push message.
                }
                break;
            }
        case GamebaseEventCategory.PUSH_CLICK_ACTION:
            {
                GamebaseResponse.Event.PushAction pushAction = GamebaseResponse.Event.PushAction.From(message.data);
                if (pushAction != null)
                {
                    // When you clicked action button by 'Rich Message'.
                }
                break;
            }
    }
}
```

* Category 는 GamebaseEventCategory 클래스에 정의되어 있습니다.
* 이벤트는 크게 IdPRevoked, LoggedOut, ServerPush, Observer, Purchase, Push로 나뉘며, 각 Category에 따라 아래 표와 같은 방법으로 GamebaseEventMessage.data를 VO로 변환할 수 있습니다.

| <div style="width:150px">Event 종류</div> | GamebaseEventCategory | VO 변환 방법 | 비고 |
| --------- | --------------------- | ----------- | --- |
| IdPRevoked | GamebaseEventCategory.IDP_REVOKED | GamebaseResponse.Event.GamebaseEventIdPRevokedData.from(message.data) | \- |
| LoggedOut | GamebaseEventCategory.LOGGED_OUT | GamebaseResponse.Event.GamebaseEventLoggedOutData.from(message.data) | \- |
| ServerPush | GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED<br>GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT<br>GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT | GamebaseResponse.Event.GamebaseEventServerPushData.from(message.data) | \- |
| Observer | GamebaseEventCategory.OBSERVER_LAUNCHING<br>GamebaseEventCategory.OBSERVER_NETWORK<br>GamebaseEventCategory.OBSERVER_HEARTBEAT | GamebaseResponse.Event.GamebaseEventObserverData.from(message.data) | \- |
| Purchase - 프로모션 결제 | GamebaseEventCategory.PURCHASE_UPDATED | GamebaseResponse.Event.PurchasableReceipt.from(message.data) | \- |
| Push - 메시지 수신 | GamebaseEventCategory.PUSH_RECEIVED_MESSAGE | GamebaseResponse.Event.PushMessage.from(message.data) | |
| Push - 메시지 클릭 | GamebaseEventCategory.PUSH_CLICK_MESSAGE | GamebaseResponse.Event.PushMessage.from(message.data) | |
| Push - 액션 클릭 | GamebaseEventCategory.PUSH_CLICK_ACTION | GamebaseResponse.Event.PushAction.from(message.data) | RichMessage 버튼 클릭 시 동작합니다. |

#### IdP Revoked

> [참고]
>
> iOS Appleid 로그인을 사용하는 경우에만 발생할 수 있는 이벤트입니다.

* IdP에서 해당 서비스를 삭제하였을 때 발생하는 이벤트입니다.
* 유저에게 IdP가 사용 중지된 것을 알리고, 로그아웃 후 다시 로그인하도록 구현해야 합니다.
 
* GamebaseEventIdPRevokedData.idpType: 사용 중지된 IdP 타입을 의미합니다.
* GamebaseEventIdPRevokedData.authMappingList: 현재 계정에 매핑되어 있는 IdP 목록을 의미합니다.

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {
        case GamebaseEventCategory.IDP_REVOKED:
            {
                GamebaseResponse.Event.GamebaseEventIdPRevokedData idPRevokedData = GamebaseResponse.Event.GamebaseEventIdPRevokedData.From(message.data);
                if (idPRevokedData != null)
                {
                    // Call logout, then login again.
                }
                break;
            }
        default:
            {
                break;
            }
    }
}
```

#### Logged Out

* Gamebase Access Token이 만료되어 네트워크 세션을 복구하기 위해 로그인 함수 호출이 필요한 경우 발생하는 이벤트입니다.

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {
        case GamebaseEventCategory.LOGGED_OUT:
            {
                GamebaseResponse.Event.GamebaseEventLoggedOutData loggedData = GamebaseResponse.Event.GamebaseEventLoggedOutData.From(message.data);
                if (loggedData != null)
                {
                    // There was a problem with the access token.
                    // Call login again.
                }
                break;
            }
    }
}
```

#### Server Push

* Gamebase 서버에서 클라이언트 단말기로 보내는 메시지입니다.
* Gamebase 에서 지원하는 Server Push Type 은 다음과 같습니다.
    * GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED
    	* NHN Cloud Gamebase 콘솔의 **Operation > Kickout** 에서 킥아웃 ServerPush 메시지를 등록하면 Gamebase와 연결된 모든 클라이언트에서 킥아웃 메시지를 받게 됩니다.
        * 클라이언트 단말기에서 서버 메시지를 수신했을 때 바로 동작하는 이벤트입니다.
        * '오토 플레이'와 같이 게임이 동작 중인 경우, 게임을 일시 정지시키는 목적으로 활용할 수 있습니다.
    * GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT
    	* NHN Cloud Gamebase 콘솔의 **Operation > Kickout** 에서 킥아웃 ServerPush 메시지를 등록하면 Gamebase와 연결된 모든 클라이언트에서 킥아웃 메시지를 받게 됩니다.
        * 클라이언트 단말기에서 서버 메시지를 수신했을 때 팝업 창을 표시하는데, 유저가 이 팝업 창을 닫았을 때 발생하는 이벤트입니다.
    * GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT
    	* Guest 계정을 다른 단말기로 이전을 성공하게 되면 이전 단말기에서 킥아웃 메시지를 받게 됩니다.

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {
        case GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED:
        case GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT:
        case GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT:
            {
                GamebaseResponse.Event.GamebaseEventServerPushData serverPushData = GamebaseResponse.Event.GamebaseEventServerPushData.From(message.data);
                if (serverPushData != null)
                {
                    CheckServerPush(message.category, serverPushData);
                }
                break;
            }
        default:
            {
                break;
            }
    }
}

private void CheckServerPush(string category, GamebaseResponse.Event.GamebaseEventServerPushData data)
{
    if (category.Equals(GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT) == true)
    {
        // Kicked out from Gamebase server.(Maintenance, banned or etc.)
        // And the game user closes the kickout pop-up.
        // Return to title and initialize Gamebase again.
    }
    else if (category.Equals(GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED) == true)
    {
        // Currently, the kickout pop-up is displayed.
        // If your game is running, stop it.
    }
    else if (category.Equals(GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT) == true)
    {
        // If the user wants to move the guest account to another device,
        // if the account transfer is successful,
        // the login of the previous device is released,
        // so go back to the title and try to log in again.
    }
}
```

#### Observer

* Gamebase Gamebase의 각종 상태 변동 이벤트를 처리하는 시스템입니다.
* Gamebase 에서 지원하는 Observer Type 은 다음과 같습니다.
    * GamebaseEventCategory.OBSERVER_LAUNCHING
    	* 점검이 걸리거나 풀린 경우, 새로운 버전이 배포되어 업데이트가 필요한 경우와 같이, Launching 상태가 변경되었을 때 동작합니다.
    	* GamebaseEventObserverData.code: LaunchingStatus 값을 의미합니다.
            * LaunchingStatus.IN_SERVICE: 200
            * LaunchingStatus.RECOMMEND_UPDATE: 201
            * LaunchingStatus.IN_SERVICE_BY_QA_WHITE_LIST: 202
            * LaunchingStatus.REQUIRE_UPDATE: 300
            * LaunchingStatus.BLOCKED_USER: 301
            * LaunchingStatus.TERMINATED_SERVICE: 302
            * LaunchingStatus.INSPECTING_SERVICE: 303
            * LaunchingStatus.INSPECTING_ALL_SERVICES: 304
            * LaunchingStatus.INTERNAL_SERVER_ERROR: 500
    * GamebaseEventCategory.OBSERVER_HEARTBEAT
    	* 탈퇴 처리 되거나 이용 정지로 인하여 사용자 계정 상태가 변했을 때 동작합니다.
    	* GamebaseEventObserverData.code: GamebaseError 값을 의미합니다.
            * GamebaseError.INVALID_MEMBER: 6
            * GamebaseError.BANNED_MEMBER: 7
    * GamebaseEventCategory.OBSERVER_NETWORK
        *Android, iOS에 한합니다.
    	* 네트워크 변동 사항 정보를 받을 수 있습니다.
    	* 네트워크가 끊기거나 연결되었을 때, 혹은 Wifi에서 셀룰러 네트워크로 변경되었을 때 동작합니다.
    	* GamebaseEventObserverData.code: NetworkManager 값을 의미합니다.
            * NetworkManager.TYPE_NOT: -1
            * NetworkManager.TYPE_MOBILE: 0
            * NetworkManager.TYPE_WIFI: 1
            * NetworkManager.TYPE_ANY: 2
    * GamebaseEventCategory.OBSERVER_WEBVIEW
        * Standalone에 한합니다.
        * Standalone에서 웹뷰를 열고 닫을 때 동작합니다.
            * GamebaseWebViewEventType.OPENED: 1
            * GamebaseWebViewEventType.CLOSED: 2
    * GamebaseEventCategory.OBSERVER_INTROSPECT
        * Standalone, WebGL에 한합니다.
        * 로그인 후 세션 연장에 실패할 때 동작합니다.

**VO**

```cs
public class GamebaseEventObserverData 
{
	// 상태값을 나타내는 정보입니다.
    public int code;

    // 상태에 관련된 메시지 정보입니다.
    public string message;

    // 추가 정보용 예비 필드입니다.
    public string extras;
}
```

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {
        case GamebaseEventCategory.OBSERVER_LAUNCHING:
            {
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                if(observerData != null)
                {
                    CheckLaunchingStatus(observerData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_NETWORK:
            {
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                if (observerData != null)
                {
                    CheckNetwork(observerData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_HEARTBEAT:
            {
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                if (observerData != null)
                {
                    CheckHeartbeat(observerData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_WEBVIEW:
            {
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                if (observerData != null)
                {
                    CheckWebView(observerData);
                }
                break;
            }
        case GamebaseEventCategory.OBSERVER_INTROSPECT:
            {
                // Introspect error
                GamebaseResponse.Event.GamebaseEventObserverData observerData = GamebaseResponse.Event.GamebaseEventObserverData.From(message.data);
                int errorCode = observerData.code;
                string errorMessage = observerData.message;
                break;
            }
        default:
            {
                break;
            }
    }
}

private void CheckLaunchingStatus(GamebaseResponse.Event.GamebaseEventObserverData observerData)
{
    switch (observerData.code)
    {
        case GamebaseLaunchingStatus.IN_SERVICE:
            {
                // Service is now normally provided.
                break;
            }
        // ... 
        case GamebaseLaunchingStatus.INTERNAL_SERVER_ERROR:
            {
                // Error in internal server.
                break;
            }
    }
}

private void CheckNetwork(GamebaseResponse.Event.GamebaseEventObserverData observerData)
{
    switch ((GamebaseNetworkType)observerData.code)
    {
        case GamebaseNetworkType.TYPE_NOT:
            {
                // Network disconnected.
                break;
            }
        case GamebaseNetworkType.TYPE_MOBILE:
        case GamebaseNetworkType.TYPE_WIFI:
        case GamebaseNetworkType.TYPE_ANY:
            {
                // Network connected.
                break;
            }
    }
}

private void CheckHeartbeat(GamebaseResponse.Event.GamebaseEventObserverData observerData)
{
    switch (observerData.code)
    {
        case GamebaseErrorCode.INVALID_MEMBER:
            {
                // You can check the invalid user session in here.
                // ex) After transferred account to another device.
                break;
            }
        case GamebaseErrorCode.BANNED_MEMBER:
            {
                // You can check the banned user session in here.
                break;
            }
    }
}

private void CheckWebView(GamebaseResponse.Event.GamebaseEventObserverData observerData)
{
    switch (observerData.code)
    {
        case GamebaseWebViewEventType.OPENED:
            {
                // WebView opened.
                break;
            }
        case GamebaseWebViewEventType.CLOSED:
            {
                // WebView closed.
                break;
            }
    }
}
```


#### Purchase Updated

* App Store 프로모션 상품 구매 완료 또는 Ask to Buy 등으로 지연된 결제가 완료되었을 때 발생하는 이벤트입니다.
* 결제 영수증 정보를 획득할 수 있습니다.

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {
        case GamebaseEventCategory.PURCHASE_UPDATED:
            {
                GamebaseResponse.Event.PurchasableReceipt purchasableReceipt = GamebaseResponse.Event.PurchasableReceipt.From(message.data);
                if (purchasableReceipt != null)
                {
                    // If a promotion or pending purchase is completed, this event will be occurred.
                }
                break;
            }
        default:
            {
                break;
            }
    }
}
```

#### Push Received Message

* Push 메시지가 도착했을때 발생하는 이벤트입니다.
* extras 필드를 JSON으로 변환하여, Push 발송 시 전송했던 커스텀 정보를 얻을 수도 있습니다.
    * **Android**에서는 **isForeground** 필드를 통해 포그라운드에서 메시지를 수신했는지, 백그라운드에서 메시지를 수신했는지 구분할 수 있습니다.

**VO**

```cs
public class PushMessage 
{
	// 메시지 고유의 id입니다.
    public string id;

    // Push 메시지 제목입니다.
    public string title;

    // Push 메시지 본문 내용입니다.
    public string body;

    // JSON 형식으로 Push 발송 시 전송했던 커스텀 정보를 확인할 수 있습니다.
    public string extras;
}
```

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {
        case GamebaseEventCategory.PUSH_RECEIVED_MESSAGE:
            {
                GamebaseResponse.Event.PushMessage pushMessage = GamebaseResponse.Event.PushMessage.From(message.data);
                if (pushMessage != null)
                {
                    // When you received push message.

                    // By converting the extras field of the push message to JSON,
                    // you can get the custom information added by the user when sending the push.
                    // (For Android, an 'isForeground' field is included so that you can check if received in the foreground state.
                }
                break;
            }
        default:
            {
                break;
            }
    }
}
```

#### Push Click Message

* 수신한 Push 메시지를 클릭했을 때 발생하는 이벤트입니다.
* 'GamebaseEventCategory.PUSH_RECEIVED_MESSAGE'와는 다르게 Android에서 extras 필드에 **isForeground** 정보가 존재하지 않습니다.

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {
        case GamebaseEventCategory.PUSH_CLICK_MESSAGE:
            {
                GamebaseResponse.Event.PushMessage pushMessage = GamebaseResponse.Event.PushMessage.From(message.data);
                if (pushMessage != null)
                {
                    // When you clicked push message.
                }
                break;
            }
        default:
            {
                break;
            }
    }
}
```

#### Push Click Action

* Rich Message 기능을 통해 생성한 버튼을 클릭했을 때 발생하는 이벤트입니다.
* actionType 은 다음 항목이 제공됩니다.
	* "OPEN_APP"
	* "OPEN_URL"
	* "REPLY"
	* "DISMISS"

**VO**

```cs
class PushAction 
{
	// 버튼 액션 종류입니다.
    public string actionType;

	// PushMessage 데이터입니다.
    public PushMessage message;

	// Push 콘솔에서 입력한 사용자 텍스트입니다.
    public string userText;
}
```

**Example**

```cs
public void AddEventHandlerSample()
{
    Gamebase.AddEventHandler(GamebaseEventHandler);
}

private void GamebaseEventHandler(GamebaseResponse.Event.GamebaseEventMessage message)
{
    switch (message.category)
    {    
        case GamebaseEventCategory.PUSH_CLICK_ACTION:
            {
                GamebaseResponse.Event.PushAction pushAction = GamebaseResponse.Event.PushAction.From(message.data);
                if (pushAction != null)
                {
                    // When you clicked action button by 'Rich Message'.
                }
                break;
            }
        default:
            {
                break;
            }
    }
}
```
