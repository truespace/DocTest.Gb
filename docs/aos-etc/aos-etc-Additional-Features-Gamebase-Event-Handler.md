---
source: aos-etc.md
split: true
created_date_time: 20260406_141859
keyword: "Gamebase Event Handler"
section: "Additional Features > Gamebase Event Handler"
order: 4
---

### Gamebase Event Handler

* Gamebase는 각종 이벤트를 **GamebaseEventHandler**라는 하나의 이벤트 시스템에서 모두 처리할 수 있습니다.
* GamebaseEventHandler는 아래 API를 통해 간단하게 Listener를 추가/제거할 수 있습니다.

**API**

```java
+ (void)Gamebase.addEventHandler(GamebaseEventHandler handler);
+ (void)Gamebase.removeEventHandler(GamebaseEventHandler handler);
+ (void)Gamebase.removeAllEventHandler();
```

**VO**

```java
class GamebaseEventMessage {
	// Event 종류를 나타냅니다.
    // GamebaseEventCategory 클래스의 값이 할당됩니다.
    @NonNull
    final public String category;

    // 각 category 에 맞는 VO 로 변환할 수 있는 JSON String 데이터입니다.
    @Nullable
    final public String data;
}
```

**Example**

```java
void eventHandlerSample(Activity activity) {
    Gamebase.addEventHandler(new GamebaseEventHandler() {
        @Override
        public void onReceive(@NonNull GamebaseEventMessage message) {
            switch (message.category) {
                case GamebaseEventCategory.LOGGED_OUT:
                    GamebaseEventLoggedOutData loggedOutData = GamebaseEventLoggedOutData.from(message.data);
                    if (loggedOutData != null) {
                        processLoggedOut(activity, message.category, loggedOutData);
                    }
                    break;
                case GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED:
                case GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT:
                case GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT:
                    GamebaseEventServerPushData serverPushData = GamebaseEventServerPushData.from(message.data);
                    if (serverPushData != null) {
                        processServerPush(activity, message.category, serverPushData);
                    }
                    break;
                case GamebaseEventCategory.OBSERVER_LAUNCHING:
                case GamebaseEventCategory.OBSERVER_HEARTBEAT:
                case GamebaseEventCategory.OBSERVER_NETWORK:
                    GamebaseEventObserverData observerData = GamebaseEventObserverData.from(message.data);
                    if (observerData != null) {
                        processObserver(activity, message.category, observerData);
                    }
                    break;
                case GamebaseEventCategory.PURCHASE_UPDATED:
                    ...
                case GamebaseEventCategory.PUSH_RECEIVED_MESSAGE:
                    ...
                case GamebaseEventCategory.PUSH_CLICK_MESSAGE:
                    ...
                case GamebaseEventCategory.PUSH_CLICK_ACTION:
                    ...
                default:
                    ...
            }
        }
    });
}
```

* Category는 GamebaseEventCategory 클래스에 정의되어 있습니다.
* 이벤트는 크게 LoggedOut, ServerPush, Observer, Purchase, Push로 나뉘며, 각 Category에 따라, 아래 표와 같은 방법으로 GamebaseEventMessage.data를 VO로 변환할 수 있습니다.

| <div style="width:150px">Event 종류</div> | GamebaseEventCategory | VO 변환 방법 | 비고 |
| --------- | --------------------- | ----------- | --- |
| LoggedOut | GamebaseEventCategory.LOGGED_OUT | GamebaseEventLoggedOutData.from(message.data) | \- |
| ServerPush | GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED<br>GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT<br>GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT | GamebaseEventServerPushData.from(message.data) | \- |
| Observer | GamebaseEventCategory.OBSERVER_LAUNCHING<br>GamebaseEventCategory.OBSERVER_NETWORK<br>GamebaseEventCategory.OBSERVER_HEARTBEAT | GamebaseEventObserverData.from(message.data) | \- |
| Purchase<br>- 프로모션 결제<br>- 지연 결제 | GamebaseEventCategory.PURCHASE_UPDATED | PurchasableReceipt.from(message.data) | \- |
| Push<br>- 메시지 수신 | GamebaseEventCategory.PUSH_RECEIVED_MESSAGE | PushMessage.from(message.data) | **isForeground** 값을 통해 Foreground에서 메시지를 수신했는지 여부를 확인할 수 있습니다. |
| Push<br>- 메시지 클릭 | GamebaseEventCategory.PUSH_CLICK_MESSAGE | PushMessage.from(message.data) | **isForeground** 값이 없습니다. |
| Push<br>- 액션 클릭 | GamebaseEventCategory.PUSH_CLICK_ACTION | PushAction.from(message.data) | RichMessage 버튼 클릭 시 동작합니다. |

#### How to handle events when the application is not running

* 커스텀 Application 클래스에서 GamebaseEventHandler를 등록하면 애플리케이션이 실행되지 않았을 때에도 이벤트를 처리할 수 있습니다.

```java
public class MyApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();

        Gamebase.addEventHandler(new GamebaseEventHandler() {
            @Override
            public void onReceive(@NonNull GamebaseEventMessage message) {
                // ...
            }
        });

        // ...
    }
}
```

#### Logged Out

* Gamebase Access Token이 만료되어 네트워크 세션을 복구하기 위해 로그인 함수 호출이 필요한 경우 발생하는 이벤트입니다.

**Example**

```java
void eventHandlerSample(Activity activity) {
    Gamebase.addEventHandler(new GamebaseEventHandler() {
        @Override
        public void onReceive(@NonNull GamebaseEventMessage message) {
            switch (message.category) {
                case GamebaseEventCategory.LOGGED_OUT:
                    GamebaseEventLoggedOutData loggedOutData = GamebaseEventLoggedOutData.from(message.data);
                    if (loggedOutData != null) {
                        processLoggedOut(activity, message.category, loggedOutData);
                    }
                    break;
                default:
                    ...
            }
        }
    });
}

void processLoggedOut(String category, GamebaseEventLoggedOutData data) {
    if (category.equals(GamebaseEventCategory.LOGGED_OUT)) {
        // There was a problem with the access token.
        // Call login again.
        Gamebase.login(activity, Gamebase.getLastLoggedInProvider(), (authToken, exception) -> {});
    }
}
```

#### Server Push

* Gamebase 서버에서 클라이언트 단말기로 보내는 메시지입니다.
* Gamebase에서 지원하는 Server Push Type은 다음과 같습니다.
	* GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED
    	* NHN Cloud Gamebase 콘솔의 **Operation > Kickout**에서 킥아웃 ServerPush 메시지를 등록하면 Gamebase와 연결된 모든 클라이언트에서 킥아웃 메시지를 받게 됩니다.
        * 클라이언트 단말기에서 서버 메시지를 수신한 직후에 발생하는 이벤트입니다.
        * '오토 플레이'와 같이 게임이 동작 중인 경우, 게임을 일시 정지시키는 목적으로 활용할 수 있습니다.
	* GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT
    	* NHN Cloud Gamebase 콘솔의 **Operation > Kickout**에서 킥아웃 ServerPush 메시지를 등록하면 Gamebase와 연결된 모든 클라이언트에서 킥아웃 메시지를 받게 됩니다.
        * 클라이언트 단말기에서 서버 메시지를 수신했을 때 팝업 창을 표시하는데, 유저가 이 팝업 창을 닫았을 때 발생하는 이벤트입니다.
    * GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT
    	* Guest 계정을 다른 단말기로 이전을 성공하게 되면 이전 단말기에서 킥아웃 메시지를 받게 됩니다.

**Example**

```java
void eventHandlerSample(Activity activity) {
    Gamebase.addEventHandler(new GamebaseEventHandler() {
        @Override
        public void onReceive(@NonNull GamebaseEventMessage message) {
            switch (message.category) {
                case GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED:
                case GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT:
                case GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT:
                    GamebaseEventServerPushData serverPushData = GamebaseEventServerPushData.from(message.data);
                    if (serverPushData != null) {
                        processServerPush(activity, message.category, serverPushData);
                    }
                    break;
                default:
                    ...
            }
        }
    });
}

void processServerPush(String category, GamebaseEventServerPushData data) {
    if (category.equals(GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT_MESSAGE_RECEIVED)) {
        // Currently, the kickout pop-up is displayed.
        // If your game is running, stop it.
    } else if (category.equals(GamebaseEventCategory.SERVER_PUSH_APP_KICKOUT)) {
        // Kicked out from Gamebase server.(Maintenance, banned or etc..)
        // And the game user closes the kickout pop-up.
        // Return to title and initialize Gamebase again.
    } else if (category.equals(GamebaseEventCategory.SERVER_PUSH_TRANSFER_KICKOUT)) {
        // If the user wants to move the guest account to another device,
        // if the account transfer is successful,
        // the login of the previous device is released,
        // so go back to the title and try to log in again.
    }
}
```

#### Observer

* Gamebase의 각종 상태 변동 이벤트를 처리하는 시스템입니다.
* Gamebase에서 지원하는 Observer Type은 다음과 같습니다.
    * GamebaseEventCategory.OBSERVER_LAUNCHING
    	* 점검이 걸리거나 풀린 경우, 새로운 버전이 배포되어 업데이트가 필요한 경우와 같이, Launching 상태가 변경되었을 때 동작합니다.
    	* GamebaseEventObserverData.code: LaunchingStatus 값을 의미합니다.
            * LaunchingStatus.IN_SERVICE: 200
            * LaunchingStatus.RECOMMEND_UPDATE: 201
            * LaunchingStatus.IN_SERVICE_BY_QA_WHITE_LIST: 202
            * LaunchingStatus.IN_TEST: 203
            * LaunchingStatus.IN_REVIEW: 204
            * LaunchingStatus.IN_BETA: 205
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
    	* 네트워크 변동 사항 정보를 받을 수 있습니다.
    	* 네트워크가 끊기거나 연결되었을 때, 혹은 Wifi에서 셀룰러 네트워크로 변경되었을 때 동작합니다.
    	* GamebaseEventObserverData.code: NetworkManager 값을 의미합니다.
            * NetworkManager.TYPE_NOT: -1
            * NetworkManager.TYPE_MOBILE: 0
            * NetworkManager.TYPE_WIFI: 1
            * NetworkManager.TYPE_ANY: 2

**VO**

```java
class GamebaseEventObserverData {
	// 상태값을 나타내는 정보입니다.
    public int code;

    // 상태에 관련된 메시지 정보입니다.
    @Nullable
    public String message;

    // 추가 정보용 예비 필드입니다.
    @Nullable
    public String extras;
}
```

**Example**

```java
void eventHandlerSample(Activity activity) {
    Gamebase.addEventHandler(new GamebaseEventHandler() {
        @Override
        public void onReceive(@NonNull GamebaseEventMessage message) {
            switch (message.category) {
                case GamebaseEventCategory.OBSERVER_LAUNCHING:
                case GamebaseEventCategory.OBSERVER_HEARTBEAT:
                case GamebaseEventCategory.OBSERVER_NETWORK:
                    GamebaseEventObserverData observerData = GamebaseEventObserverData.from(message.data);
                    if (observerData != null) {
                        processObserver(activity, message.category, observerData);
                    }
                    break;
                default:
                    ...
            }
        }
    });
}

void processObserver(String category, GamebaseEventObserverData data) {
    if (category.equals(GamebaseEventCategory.OBSERVER_LAUNCHING)) {
        int launchingStatusCode = data.code;
        String launchingMessage = data.message;
        switch (launchingStatusCode) {
            case LaunchingStatus.IN_SERVICE:
                // Finished maintenance.
                break;
            case LaunchingStatus.INSPECTING_SERVICE:
            case LaunchingStatus.INSPECTING_ALL_SERVICES:
                // Under maintenance.
                break;
            ...
        }
    } else if (category.equals(GamebaseEventCategory.OBSERVER_HEARTBEAT)) {
        int errorCode = data.code;
        switch (errorCode) {
            case GamebaseError.INVALID_MEMBER:
                // You can check the invalid user session in here.
                // ex) After transferred account to another device.
                break;
            case GamebaseError.BANNED_MEMBER:
                // You can check the banned user session in here.
                break;
            case GamebaseError.AUTH_TOKEN_LOGIN_INVALID_TOKEN_INFO:
                // There was a problem with the access token.
                // Call login again.
                Gamebase.login(activity, Gamebase.getLastLoggedInProvider(), (authToken, exception) -> {});
                break;
        }
    } else if (category.equals(GamebaseEventCategory.OBSERVER_NETWORK)) {
        int networkTypeCode = data.code;
        // You can check the changed network status in here.
        if (networkTypeCode == NetworkManager.TYPE_NOT) {
            // Network disconnected.
        } else {
            // Network connected.
        }
    }
}
```

#### Purchase Updated

* Promotion 코드 입력을 통해 상품을 획득한 경우 또는 Pending 결제(느린 결제, 부모 동의 등)가 완료되었을 때 발생하는 이벤트입니다.
* 결제 영수증 정보를 획득할 수 있습니다.

**Example**

```java
void eventHandlerSample(Activity activity) {
    Gamebase.addEventHandler(new GamebaseEventHandler() {
        @Override
        public void onReceive(@NonNull GamebaseEventMessage message) {
            switch (message.category) {
                case GamebaseEventCategory.PURCHASE_UPDATED:
                    PurchasableReceipt receipt = PurchasableReceipt.from(message.data);
                    if (receipt != null) {
                        // If the user got item by 'Promotion Code' or
                        // 'Lazy purchase', or 'Parents permission',...,
                        // this event will be occurred.
                    }
                    break;
                default:
                    ...
            }
        }
    });
}
```

#### Push Received Message

* Push 메시지가 도착했을때 발생하는 이벤트입니다.
* **isForeground** 필드를 통해 포그라운드에서 메시지를 수신했는지, 백그라운드에서 메시지를 수신했는지 구분할 수 있습니다.
* extras 필드를 JSON으로 변환하여, Push 발송 시 전송했던 커스텀 정보를 얻을 수도 있습니다.

**VO**

```java
class PushMessage {
	// 메시지 고유의 id입니다.
    @NonNull
    public String id;

    // Push 메시지 제목입니다.
    @Nullable
    public String title;

    // Push 메시지 본문 내용입니다.
    @Nullable
    public String body;

    // JSONObject 로 변환하여 모든 정보를 확인할 수 있습니다.
    @NonNull
    public String extras;
}
```

**Example**

```java
void eventHandlerSample(Activity activity) {
    Gamebase.addEventHandler(new GamebaseEventHandler() {
        @Override
        public void onReceive(@NonNull GamebaseEventMessage message) {
            switch (message.category) {
                case GamebaseEventCategory.PUSH_RECEIVED_MESSAGE:
                    PushMessage pushMessage = PushMessage.from(message.data);
                    if (pushMessage != null) {
                        // When you received push message.
                        try {
                            JSONObject json = new JSONObject(pushMessage.extras);
                            // There is 'isForeground' information.
                            boolean isForeground = json.getBoolean("isForeground");
                            Object customValue = json.get("YourCustomKey");
                        } catch (Exception e) {}
                    }
                    break;
                default:
                    ...
            }
        }
    });
}
```

#### Push Click Message

* 수신한 Push 메시지를 클릭했을 때 발생하는 이벤트입니다.
* 'GamebaseEventCategory.PUSH_RECEIVED_MESSAGE'와는 다르게 **isForeground** 필드가 존재하지 않습니다.

**Example**

```java
void eventHandlerSample(Activity activity) {
    Gamebase.addEventHandler(new GamebaseEventHandler() {
        @Override
        public void onReceive(@NonNull GamebaseEventMessage message) {
            switch (message.category) {
                case GamebaseEventCategory.PUSH_CLICK_MESSAGE:
                    PushMessage clickedMessage = PushMessage.from(message.data);
                    if (clickedMessage != null) {
                        // When you clicked push message.
                    }
                    break;
                default:
                    ...
            }
        }
    });
}
```

#### Push Click Action

* Rich Message 기능을 통해 생성한 버튼을 클릭했을 때 발생하는 이벤트입니다.
* actionType은 다음 항목이 제공됩니다.
	* "OPEN_APP"
	* "OPEN_URL"
	* "REPLY"
	* "DISMISS"

**VO**

```java
class PushAction {
	// 버튼 액션 종류입니다.
    @NonNull
    public String actionType;

	// PushMessage 데이터입니다.
    @NonNull
    public PushMessage message;

	// Push 콘솔에서 입력한 사용자 텍스트입니다.
    @Nullable
    public String userText;
}
```

**Example**

```java
void eventHandlerSample(Activity activity) {
    Gamebase.addEventHandler(new GamebaseEventHandler() {
        @Override
        public void onReceive(@NonNull GamebaseEventMessage message) {
            switch (message.category) {
                case GamebaseEventCategory.PUSH_CLICK_ACTION:
                    PushAction pushAction = PushAction.from(message.data);
                    if (pushAction != null) {
                        // When you clicked action button by 'Rich Message'.
                    }
                    break;
                default:
                    ...
            }
        }
    });
}
```
