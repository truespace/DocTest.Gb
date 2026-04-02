## Game > Gamebase > Unreal SDK 사용 가이드 > ETC

### Gamebase Event Handler

* Gamebase는 각종 이벤트를 **GamebaseEventHandler**라는 하나의 이벤트 시스템에서 모두 처리할 수 있습니다.
* GamebaseEventHandler는 아래 API를 통해 간단하게 Listener를 추가/제거할 수 있습니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
FDelegateHandle AddHandler(const FGamebaseEventDelegate::FDelegate& Callback);
void RemoveHandler(const FDelegateHandle& handle);
void RemoveAllHandler();
```

**VO**

```cpp
struct GAMEBASE_API FGamebaseEventMessage
{
    // Event 종류를 나타냅니다.
    // GamebaseEventCategory 클래스의 값이 할당됩니다.
    FString Category;

    // 각 Category 에 맞는 VO 로 변환할 수 있는 JSON String 데이터입니다.
    FString Data;
};
```

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::IdPRevoked))
        {
            auto IdpRevokedData = FGamebaseEventIdPRevokedData::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::LoggedOut))
        {
            auto LoggedOutData = FGamebaseEventLoggedOutData::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::ServerPushAppKickOut) ||
                 Message.Category.Equals(GamebaseEventCategory::ServerPushAppKickOutMessageReceived) ||
                 Message.Category.Equals(GamebaseEventCategory::ServerPushTransferKickout))
        {
            auto ServerPushData = FGamebaseEventServerPushData::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::ObserverLaunching))
        {
            auto ObserverData = FGamebaseEventObserverData::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::ObserverNetwork))
        {
            auto ObserverData = FGamebaseEventObserverData::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::ObserverHeartbeat))
        {
            auto ObserverData = FGamebaseEventObserverData::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::PurchaseUpdated))
        {
            auto PurchasableReceipt = FGamebaseEventPurchasableReceipt::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::PushReceivedMessage))
        {
            auto PushMessage = FGamebaseEventPushMessage::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::PushClickMessage))
        {
            auto PushMessage = FGamebaseEventPushMessage::From(Message.Data);
        }
        else if (Message.Category.Equals(GamebaseEventCategory::PushClickAction))
        {
            auto PushAction = FGamebaseEventPushAction::From(Message.Data);
        }
    }));
}
```

* Category는 GamebaseEventCategory 클래스에 정의되어 있습니다.
* 이벤트는 크게 LoggedOut, ServerPush, Observer, Purchase, Push로 나뉘며, 각 Category에 따라, 아래 표와 같은 방법으로 GamebaseEventMessage.data를 VO로 변환할 수 있습니다.

| <div style="width:150px">Event 종류</div> | GamebaseEventCategory | VO 변환 방법 | 비고 |
| --------- | --------------------- | ----------- | --- |
| IdPRevoked | GamebaseEventCategory::IdPRevoked | FGamebaseEventIdPRevokedData::From(Message.Data) | \- |
| LoggedOut | GamebaseEventCategory::LoggedOut | FGamebaseEventLoggedOutData::From(Message.Data) | \- |
| ServerPush | GamebaseEventCategory::ServerPushAppKickOut<br>GamebaseEventCategory::ServerPushAppKickOutMessageReceived<br>GamebaseEventCategory::ServerPushTransferKickout | FGamebaseEventServerPushData::From(Message.Data) | \- |
| Observer | GamebaseEventCategory::ObserverLaunching<br>GamebaseEventCategory::ObserverNetwork<br>GamebaseEventCategory::ObserverHeartbeat | FGamebaseEventObserverData::From(Message.Data) | \- |
| Purchase<br>- 프로모션 결제<br>- 지연 결제 | GamebaseEventCategory::PurchaseUpdated | FGamebaseEventPurchasableReceipt::From(Message.Data) | \- |
| Push<br>- 메시지 수신 | GamebaseEventCategory::PushReceivedMessage | FGamebaseEventPushMessage::From(Message.Data) |  |
| Push<br>- 메시지 클릭 | GamebaseEventCategory::PushClickMessage | FGamebaseEventPushMessage::From(Message.Data) |  |
| Push<br>- 액션 클릭 | GamebaseEventCategory::PushClickAction | FGamebaseEventPushAction::From(Message.Data) | RichMessage 버튼 클릭 시 동작합니다. |

#### IdP Revoked

> [참고]
>
> iOS Appleid 로그인을 사용하는 경우에만 발생할 수 있는 이벤트입니다.

* IdP에서 해당 서비스를 삭제하였을 때 발생하는 이벤트입니다.
* 유저에게 IdP가 사용 중지된 것을 알리고, 로그아웃 후 다시 로그인하도록 구현해야 합니다.

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::IdPRevoked))
        {
            // TODO: process logout, then login again.
        }
    }));
}
```

#### Logged Out

* Gamebase Access Token이 만료되어 네트워크 세션을 복구하기 위해 로그인 함수 호출이 필요한 경우 발생하는 이벤트입니다.

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::LoggedOut))
        {
            auto LoggedOutData = FGamebaseEventLoggedOutData::From(Message.Data);
            if (loggedData.IsValid() == true)
            {
                // There was a problem with the access token.
                // Call login again.
            }
        }
    }));
}
```

#### Server Push

* Gamebase 서버에서 클라이언트 단말기로 보내는 메시지입니다.
* Gamebase 에서 지원하는 Server Push Type 은 다음과 같습니다.
    * GamebaseEventCategory::ServerPushAppKickOutMessageReceived
    	* NHN Cloud Gamebase 콘솔의 **Operation > Kickout** 에서 킥아웃 ServerPush 메시지를 등록하면 Gamebase와 연결된 모든 클라이언트에서 킥아웃 메시지를 받게 됩니다.
        * 클라이언트 단말기에서 서버 메시지를 수신했을 때 바로 동작하는 이벤트 입니다.
        * '오토 플레이'와 같이 게임이 동작 중인 경우, 게임을 일시 정지 시키는 목적으로 활용할 수 있습니다.
    * GamebaseEventCategory::ServerPushAppKickOut
        * NHN Cloud  Gamebase 콘솔의 **Operation > Kickout** 에서 킥아웃 ServerPush 메시지를 등록하면 Gamebase와 연결된 모든 클라이언트에서 킥아웃 메시지를 받게 됩니다.
        * 클라이언트 단말기에서 서버 메시지를 수신했을 때 팝업을 표시하는데, 유저가 팝업을 닫았을 때 동작하는 이벤트 입니다.
    * GamebaseEventCategory::ServerPushTransferKickout
        * Guest 계정을 다른 단말기로 이전을 성공하게 되면 이전 단말기에서 킥아웃 메시지를 받게 됩니다.

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::ServerPushAppKickOut) ||
            Message.Category.Equals(GamebaseEventCategory::ServerPushAppKickOutMessageReceived) ||
            Message.Category.Equals(GamebaseEventCategory::ServerPushTransferKickout))
        {
            auto serverPushData = FGamebaseEventServerPushData::From(Message.Data);
            if (serverPushData.IsVaild())
            {
                CheckServerPush(Message.Category, *serverPushData);
            }
        }
    }));
}

void USample::CheckServerPush(const FString& Category, const FGamebaseEventServerPushData& Data)
{
    if (Message.Category.Equals(GamebaseEventCategory::ServerPushAppKickOut))
    {
        // Kicked out from Gamebase server.(Maintenance, banned or etc.)
        // And the game user closes the kickout pop-up.
        // Return to title and initialize Gamebase again.
    }
    else if (Message.Category.Equals(GamebaseEventCategory::ServerPushAppKickOutMessageReceived))
    {
        // Currently, the kickout pop-up is displayed.
        // If your game is running, stop it.
    }
    else if (Message.Category.Equals(GamebaseEventCategory::ServerPushTransferKickout))
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
    * GamebaseEventCategory::ObserverLaunching
        * 점검이 걸리거나 풀린 경우, 새로운 버전이 배포되어 업데이트가 필요한 경우와 같이, Launching 상태가 변경되었을 때 동작합니다.
        * GamebaseEventObserverData.code: LaunchingStatus 값을 의미합니다.
            * GamebaseLaunchingStatus::IN_SERVICE: 200
            * GamebaseLaunchingStatus::RECOMMEND_UPDATE: 201
            * GamebaseLaunchingStatus::IN_SERVICE_BY_QA_WHITE_LIST: 202
            * GamebaseLaunchingStatus::REQUIRE_UPDATE: 300
            * GamebaseLaunchingStatus::BLOCKED_USER: 301
            * GamebaseLaunchingStatus::TERMINATED_SERVICE: 302
            * GamebaseLaunchingStatus::INSPECTING_SERVICE: 303
            * GamebaseLaunchingStatus::INSPECTING_ALL_SERVICES: 304
            * GamebaseLaunchingStatus::INTERNAL_SERVER_ERROR: 500
    * GamebaseEventCategory::ObserverHeartbeat
        * 탈퇴 처리 되거나 이용 정지로 인하여 사용자 계정 상태가 변했을 때 동작합니다.
        * GamebaseEventObserverData.code: GamebaseError 값을 의미합니다.
            * GamebaseErrorCode::INVALID_MEMBER: 6
            * GamebaseErrorCode::BANNED_MEMBER: 7
    * GamebaseEventCategory::ObserverNetwork
        *Android, iOS에 한합니다.
        * 네트워크 변동 사항 정보를 받을 수 있습니다.
        * 네트워크가 끊기거나 연결되었을 때, 혹은 Wifi에서 셀룰러 네트워크로 변경되었을 때 동작합니다.
        * GamebaseEventObserverData.code: NetworkManager 값을 의미합니다.
            * EGamebaseNetworkType::Not: 255
            * EGamebaseNetworkType::Mobile: 0
            * EGamebaseNetworkType::Wifi: 1
            * EGamebaseNetworkType::Any: 2
**VO**

```cpp
struct GAMEBASE_API FGamebaseEventObserverData
{
    // 상태값을 나타내는 정보입니다.
    int32 Code;

    // 추가 정보용 예비 필드입니다.
    FString Message;

    // 상태에 관련된 메시지 정보입니다.
    FString Extras;
}
```

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::ObserverLaunching))
        {
            auto observerData = FGamebaseEventObserverData::From(Message.Data);
            if (observerData.IsVaild())
            {
                CheckLaunchingStatus(*observerData);
            }
        }
        else if (Message.Category.Equals(GamebaseEventCategory::ObserverNetwork))
        {
            auto observerData = FGamebaseEventObserverData::From(Message.Data);
            if (observerData.IsVaild())
            {
                CheckNetwork(*observerData);
            }
        }
        else if (Message.Category.Equals(GamebaseEventCategory::ObserverHeartbeat))
        {
            auto observerData = FGamebaseEventObserverData::From(Message.Data);
            if (observerData.IsVaild())
            {
                CheckHeartbeat(*observerData);
            }
        }
    }));
}

void USample::CheckLaunchingStatus(const FGamebaseEventObserverData& Data)
{
    switch (Data.code)
    {
        case GamebaseLaunchingStatus::IN_SERVICE:
            {
                // Service is now normally provided.
                break;
            }
        // ... 
        case GamebaseLaunchingStatus::INTERNAL_SERVER_ERROR:
            {
                // Error in internal server.
                break;
            }
    }
}

void USample::CheckNetwork(const FGamebaseEventObserverData& Data)
{
    switch ((GamebaseNetworkType)Data.code)
    {
        case EGamebaseNetworkType::Not:
            {
                // Network disconnected.
                break;
            }
        case EGamebaseNetworkType::Mobile:
        case EGamebaseNetworkType::Wifi:
        case EGamebaseNetworkType::Any:
            {
                // Network connected.
                break;
            }
    }
}

void USample::CheckHeartbeat(const FGamebaseEventObserverData& Data)
{
    switch (Data.code)
    {
        case EGGamebaseErrorCode::INVALID_MEMBER:
            {
                // You can check the invalid user session in here.
                // ex) After transferred account to another device.
                break;
            }
        case EGGamebaseErrorCode::BANNED_MEMBER:
            {
                // You can check the banned user session in here.
                break;
            }
    }
}
```

#### Purchase Updated

* Promotion 코드 입력을 통해 상품을 획득한 경우 또는 Pending 결제(느린 결제, 부모 동의 등)가 완료되었을 때 발생하는 이벤트입니다.
* 결제 영수증 정보를 획득할 수 있습니다.

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::PurchaseUpdated))
        {
            auto purchasableReceipt = FGamebaseEventPurchasableReceipt::From(Message.Data);
            if (purchasableReceipt.IsVaild())
            {
                // If the user got item by 'Promotion Code' or
                // 'Lazy purchase', or 'Parents permission',...,
                // this event will be occurred.
            }
        }
    }));
}
```


#### Push Received Message

* Push 메시지가 도착했을때 발생하는 이벤트입니다.
* extras 필드를 JSON으로 변환하여, Push 발송 시 전송했던 커스텀 정보를 얻을 수도 있습니다.
    * **Android**에서는 **isForeground** 필드를 통해 포그라운드에서 메시지를 수신했는지, 백그라운드에서 메시지를 수신했는지 구분할 수 있습니다.

**VO**

```cpp
struct FGamebaseEventPushMessage
{
    // 메시지 고유의 id입니다.
    FString Id;

    // Push 메시지 제목입니다.
    FString Title;

    // Push 메시지 본문 내용입니다.
    FString Body;

    // JSON 형식으로 Push 발송 시 전송했던 커스텀 정보를 확인할 수 있습니다.
    FString Extras;
};
```

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::PushReceivedMessage))
        {
            auto PushMessage = FGamebaseEventPushMessage::From(Message.Data);
            if (PushMessage.IsVaild())
            {
                // When you clicked push Message.

                // By converting the extras field of the push Message to JSON,
                // you can get the custom information added by the user when sending the push.
                // (For Android, an 'isForeground' field is included so that you can check if received in the foreground state.)
            }
        }
    }));
}
```

#### Push Click Message

* 수신한 Push 메시지를 클릭했을 때 발생하는 이벤트입니다.
* 'GamebaseEventCategory::PushReceivedMessage'와는 다르게 Android에서 extras 필드에 **isForeground** 정보가 존재하지 않습니다.

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::PushClickMessage))
        {
            auto PushMessage = FGamebaseEventPushMessage::From(Message.Data);
            if (PushMessage.IsVaild())
            {
                // When you clicked push Message.
            }
        }
    }));
}
```


#### Push Click Action

* Rich Message 기능을 통해 생성한 버튼을 클릭했을 때 발생하는 이벤트입니다.
* ActionType은 다음 항목이 제공됩니다.
    * "OPEN_APP"
    * "OPEN_URL"
    * "REPLY"
    * "DISMISS"


**VO**

```cpp
struct FGamebaseEventPushAction
{
    // 버튼 액션 종류입니다.
    FString ActionType;

    // PushMessage 데이터입니다.
    FGamebaseEventPushMessage Message;

    // Push 콘솔에서 입력한 사용자 텍스트입니다.
    FString UserText;
};
```

**Example**

```cpp
void USample::AddEventHandler()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->AddEventHandler(FGamebaseEventDelegate::FDelegate::CreateLambda([](const FGamebaseEventMessage& Message)
    {
        if (Message.Category.Equals(GamebaseEventCategory::PushClickAction))
        {
            auto PushAction = FGamebaseEventPushAction::From(Message.Data);
            if (PushAction.IsVaild())
            {
                // When you clicked action button by 'Rich Message'.
            }
        }
    }));
}
```
