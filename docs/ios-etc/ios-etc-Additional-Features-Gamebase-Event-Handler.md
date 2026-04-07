---
source: ios-etc.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, Login, Logout, Purchase, Push, Maintenance, EventHandler, Error, Guest, IdP"
section: "Additional Features > Gamebase Event Handler"
order: 5
---

### Gamebase Event Handler

* Gamebase는 각종 이벤트를 **GamebaseEventHandler**라는 하나의 이벤트 시스템에서 모두 처리할 수 있습니다.
* GamebaseEventHandler는 아래 API를 통해 간단하게 Handler를 추가/제거할 수 있습니다.

**API**


```objectivec
+ (void)addEventHandler:(GamebaseEventHandler)handler;
+ (void)removeEventHandler:(GamebaseEventHandler)handler;
+ (void)removeAllEventHandler;
```

**VO**

```objectivec
@interface TCGBGamebaseEventMessage : NSObject <TCGBValueObject>

@property (nonatomic, strong, nonnull)  NSString* category;
@property (nonatomic, strong, nullable) NSString* data;

@end
```

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        if ([message.category isEqualToString:kTCGBIdPRevoked] == YES) {
            TCGBGamebaseEventIdPRevokedData* idPRevokedData = [TCGBGamebaseEventIdPRevokedData gamebaseEventIdPRevokedDataFromJsonString:message.data];
            if (idPRevokedData != nil) {
                //TODO: process idp revoked
            }
        } else if ([message.category isEqualToString:kTCGBLoggedOut] == YES) {
            TCGBGamebaseEventLoggedOutData* loggedOutData = [TCGBGamebaseEventLoggedOutData gamebaseEventLoggedOutDataFromJsonString:message.data];
            if (loggedOutData != nil) {
                //TODO: process loggedOut
            }
        } else if ([message.category isEqualToString:kTCGBServerPushAppKickoutMessageReceived] == YES
            || [message.category isEqualToString:kTCGBServerPushAppKickout] == YES
            || [message.category isEqualToString:kTCGBServerPushTransferKickout] == YES) {
            TCGBGamebaseEventServerPushData* serverPushData = [TCGBGamebaseEventServerPushData gamebaseEventServerPushDataFromJsonString:message.data];
            if (serverPushData != nil) {
                //TODO: process server push
            }
        } else if ([message.category isEqualToString:kTCGBObserverLaunching] == YES
            || [message.category isEqualToString:kTCGBObserverHeartbeat] == YES
            || [message.category isEqualToString:kTCGBObserverNetwork] == YES) {
            TCGBGamebaseEventObserverData* observerData = [TCGBGamebaseEventObserverData gamebaseEventObserverDataFromJsonString:message.data];
            if (observerData != nil) {
                //TODO: process observer
            }
        } else if ([message.category isEqualToString:kTCGBPurchaseUpdated] == YES) {
            
        } else if ([message.category isEqualToString:kTCGBPushReceivedMessage] == YES) {
            
        } else if ([message.category isEqualToString:kTCGBPushClickMessage] == YES) {
            
        } else if ([message.category isEqualToString:kTCGBPushClickAction] == YES) {
            
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
}
```

* Category는 GamebaseEventCategory 클래스에 정의되어 있습니다.
* 이벤트는 크게 IdPRevoked, LoggedOut, ServerPush, Observer, Purchase, Push로 나뉘며, 각 Category에 따라 아래 표와 같은 방법으로 TCGBGamebaseEventMessage.data를 VO로 변환할 수 있습니다.

| <div style="width:150px">Event 종류</div> | GamebaseEventCategory | VO 변환 방법 | 비고 |
| --------- | --------------------- | ----------- | --- |
| IdPRevoked | kTCGBIdPRevoked | [TCGBGamebaseEventIdPRevokedData gamebaseEventIdPRevokedDataFromJsonString:message.data] | \- |
| LoggedOut | kTCGBLoggedOut | [TCGBGamebaseEventLoggedOutData gamebaseEventLoggedOutDataFromJsonString:message.data] | \- |
| ServerPush | kTCGBServerPushAppKickoutMessageReceived<br>kTCGBServerPushAppKickout<br>kTCGBServerPushTransferKickout | [TCGBGamebaseEventServerPushData gamebaseEventServerPushDataFromJsonString:message.data] | \- |
| Observer | kTCGBObserverLaunching<br>kTCGBObserverHeartbeat<br>kTCGBObserverNetwork | [TCGBGamebaseEventObserverData gamebaseEventObserverDataFromJsonString:message.data] | \- |
| Purchase<br>- 프로모션 결제<br>- 지연 결제 | kTCGBPurchaseUpdated | [TCGBPurchasableReceipt purchasableReceiptFromJsonString:message.data] | \- |
| Push<br>- 메시지 수신 | kTCGBPushReceivedMessage | [TCGBPushMessage pushMessageFromJsonString:message.data] | \- |
| Push<br>- 메시지 클릭 | kTCGBPushClickMessage | [TCGBPushMessage pushFromJsonString:message.data] | \- |
| Push<br>- 액션 클릭 | kTCGBPushClickAction | [TCGBPushMessage pushFromJsonString:message.data] | RichMessage 버튼 클릭 시 동작합니다. |

#### IdP Revoked

> [참고]
>
> iOS Appleid 로그인을 사용하는 경우에만 발생할 수 있는 이벤트입니다.

* IdP에서 해당 서비스를 삭제하였을 때 발생하는 이벤트입니다.
* 유저에게 IdP가 사용 중지된 것을 알리고, 로그아웃 후 다시 로그인하도록 구현해야 합니다.

```objectivec
@interface TCGBGamebaseEventIdPRevokedData : NSObject <TCGBValueObject>

@property (nonatomic, assign) int64_t                 code;
@property (nonatomic, strong) NSString*               idPType;
@property (nonatomic, strong) NSArray<NSString *>*    authMappingList;
@property (nonatomic, strong) NSString*               extras;

@end
```

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        if ([message.category isEqualToString:kTCGBIdPRevoked] == YES) {
            // TODO: process logout, then login again.
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
}
```

#### Logged Out

* Gamebase Access Token이 만료되어 네트워크 세션을 복구하기 위해 로그인 함수 호출이 필요한 경우 발생하는 이벤트입니다.

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        [self printLogAndShowAlertWithData:[message prettyJsonString] error:nil alertTitle:@"addEventHandler Result"];
        if ([message.category isEqualToString:kTCGBLoggedOut] == YES) {
            TCGBGamebaseEventLoggedOutData* loggedOutData = [TCGBGamebaseEventLoggedOutData gamebaseEventLoggedOutDataFromJsonString:message.data];
            if (loggedOutData != nil) {
                //TODO: process loggedOut
            }
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
}
```

#### Server Push

* Gamebase 서버에서 클라이언트 단말기로 보내는 메시지입니다.
* Gamebase에서 지원하는 Server Push Type은 다음과 같습니다.
	* kTCGBServerPushAppKickoutMessageReceived
    	* NHN Cloud Gamebase 콘솔의 **Operation > Kickout**에서 킥아웃 ServerPush 메시지를 등록하면 Gamebase와 연결된 모든 클라이언트에서 킥아웃 메시지를 받게 됩니다.
        * 클라이언트 단말기에서 서버 메시지를 수신한 직후에 발생하는 이벤트입니다.
        * '오토 플레이'와 같이 게임이 동작 중인 경우, 게임을 일시 정지시키는 목적으로 활용할 수 있습니다.
	* kTCGBServerPushAppKickout
    	* NHN Cloud Gamebase 콘솔의 **Operation > Kickout**에서 킥아웃 ServerPush 메시지를 등록하면 Gamebase와 연결된 모든 클라이언트에서 킥아웃 메시지를 받게 됩니다.
        * 클라이언트 단말기에서 서버 메시지를 수신했을 때 팝업 창을 표시하는데, 유저가 이 팝업 창을 닫았을 때 발생하는 이벤트입니다.
    * kTCGBServerPushTransferKickout
    	* Guest 계정을 다른 단말기로 이전을 성공하게 되면 이전 단말기에서 킥아웃 메시지를 받게 됩니다.

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        [self printLogAndShowAlertWithData:[message prettyJsonString] error:nil alertTitle:@"addEventHandler Result"];
        if ([message.category isEqualToString:kTCGBServerPushAppKickoutMessageReceived] == YES) {
            TCGBGamebaseEventServerPushData* serverPushData = [TCGBGamebaseEventServerPushData gamebaseEventServerPushDataFromJsonString:message.data];
            if (serverPushData != nil) {
                //TODO: process server push 
            }
        } else if ([message.category isEqualToString:kTCGBServerPushAppKickout] == YES) {
            TCGBGamebaseEventServerPushData* serverPushData = [TCGBGamebaseEventServerPushData gamebaseEventServerPushDataFromJsonString:message.data];
            if (serverPushData != nil) {
                //TODO: process server push
            }
        } else if ([message.category isEqualToString:kTCGBServerPushTransferKickout] == YES) {
            TCGBGamebaseEventServerPushData* serverPushData = [TCGBGamebaseEventServerPushData gamebaseEventServerPushDataFromJsonString:message.data];
            if (serverPushData != nil) {
                //TODO: process server push
            }
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
}
```

#### Observer

* Gamebase의 각종 상태 변동 이벤트를 처리하는 시스템입니다.
* Gamebase에서 지원하는 Observer Type은 다음과 같습니다.
    * kTCGBObserverLaunching
    	* 점검이 걸리거나 풀린 경우, 새로운 버전이 배포되어 업데이트가 필요한 경우와 같이, Launching 상태가 변경되었을 때 동작합니다.
    	* TCGBGamebaseEventObserverData.code: TCGBLaunchingStatus 값을 의미합니다.
            * IN_SERVICE: 200
            * RECOMMEND_UPDATE: 201
            * IN_SERVICE_BY_QA_WHITE_LIST: 202
            * REQUIRE_UPDATE: 300
            * BLOCKED_USER: 301
            * TERMINATED_SERVICE: 302
            * INSPECTING_SERVICE: 303
            * INSPECTING_ALL_SERVICES: 304
            * INTERNAL_SERVER_ERROR: 500
    * kTCGBObserverHeartbeat
    	* 탈퇴 처리 되거나 이용 정지로 인하여 사용자 계정 상태가 변했을 때 동작합니다.
    	* TCGBGamebaseEventObserverData.code: TCGBError 값을 의미합니다.
            * TCGB_ERROR_INVALID_MEMBER: 6
            * TCGB_ERROR_BANNED_MEMBER: 7
    * kTCGBObserverNetwork
    	* 네트워크 변동 사항 정보를 받을 수 있습니다.
    	* 네트워크가 끊기거나 연결되었을 때, 혹은 Wifi에서 셀룰러 네트워크로 변경되었을 때 동작합니다.
    	* TCGBGamebaseEventObserverData.code: NetworkManager 값을 의미합니다.
            * ReachabilityIsNotDefined = -100
            * NotReachable = -1
            * ReachableViaWWAN = 0
            * ReachableViaWifi = 1

**VO**

```objectivec
@interface TCGBGamebaseEventObserverData : NSObject <TCGBValueObject>

@property (nonatomic, assign)           int64_t     code;
@property (nonatomic, strong, nullable) NSString*   message;
@property (nonatomic, strong, nullable) NSString*   extras;

@end
```

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        if ([message.category isEqualToString:kTCGBObserverLaunching] == YES) {
            TCGBGamebaseEventObserverData* observerData = [TCGBGamebaseEventObserverData gamebaseEventObserverDataFromJsonString:message.data];
            if (observerData != nil) {
                int launchingStatusCode = observerData.code;
                NSString* launchingMessage = observerData.message;
                switch (launchingStatusCode) {
                    case IN_SERVICE:
                    // Finished maintenance.
                    break;
                case INSPECTING_SERVICE:
                case INSPECTING_ALL_SERVICES:
                    // Under maintenance.
                    break;
                ...
                }
            }
        }
        else if ([message.category isEqualToString:kTCGBObserverHeartbeat] == YES) {
            TCGBGamebaseEventObserverData* observerData = [TCGBGamebaseEventObserverData gamebaseEventObserverDataFromJsonString:message.data];
            int errorCode = observerData.code;
            switch (errorCode) {
            case TCGB_ERROR_INVALID_MEMBER:
                // You can check the invalid user session in here.
                // ex) After transferred account to another device.
                break;
            case TCGB_ERROR_BANNED_MEMBER:
                // You can check the banned user session in here.
                break;
            }
        }
        else if ([message.category isEqualToString:kTCGBObserverNetwork] == YES) {
            TCGBGamebaseEventObserverData* observerData = [TCGBGamebaseEventObserverData gamebaseEventObserverDataFromJsonString:message.data];
            NetworkStatus networkTypeCode = observerData.code;
            // You can check the changed network status in here.
            if (networkTypeCode == NotReachable || networkTypeCode == ReachabilityIsNotDefined) {
                // Network disconnected.
            } else {
                // Network connected.
            }
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
}
```


#### Purchase Updated

* App Store 프로모션 상품 구매 완료 또는 Ask to Buy 등으로 지연된 결제가 완료되었을 때 발생하는 이벤트입니다.
* 결제 영수증 정보를 획득할 수 있습니다.

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        TCGBPurchasableReceipt* receipt = [TCGBPurchasableReceipt purchasableReceiptFromJsonString:message.data];
        if (receipt != nil) {
            // If a promotion or pending purchase is completed, this event will be occurred.
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
}
```

#### Push Received Message


* Push 메시지가 도착했을때 발생하는 이벤트입니다.
* extras 필드를 JSON으로 변환하여, Push 발송 시 전송했던 커스텀 정보를 얻을 수도 있습니다.

**VO**

```objectivec
@interface TCGBPushMessage : NSObject <TCGBValueObject>

@property (nonatomic, strong, nonnull) NSString* identifier;
@property (nonatomic, strong, nullable) NSString* title;
@property (nonatomic, strong, nullable) NSString* body;
@property (nonatomic, strong, nonnull) NSString* extras;

@end
```

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        if ([message.category isEqualToString:kTCGBPushReceivedMessage] == YES) {
            TCGBPushMessage* pushMessage = [TCGBPushMessage pushMessageFromJsonString:message.data];
            if (pusMessage != nil) {
                //TODO: process 
            }
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
}
```

#### Push Click Message

* 수신한 Push 메시지를 클릭했을 때 발생하는 이벤트입니다.

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        if ([message.category isEqualToString:kTCGBPushClickMessage] == YES) {
            TCGBPushMessage* pushMessage = [TCGBPushMessage pushMessageFromJsonString:message.data];
            if (pusMessage != nil) {
                //TODO: process 
            }
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
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

```objectivec
@interface TCGBPushAction : NSObject <TCGBValueObject>

@property (nonatomic, strong, nonnull) NSString* actionType;
@property (nonatomic, strong, nullable) TCGBPushMessage* message;
@property (nonatomic, strong, nullable) NSString* userText;

@end
```

**Example**

```objectivec
- (void)eventHandler_addEventHandler {
    void(^eventHandler)(TCGBGamebaseEventMessage *) = ^(TCGBGamebaseEventMessage * _Nonnull message) {
        if ([message.category isEqualToString:kTCGBPushClickAction] == YES) {
            TCGBPushAction* pushMessage = [TCGBPushAction pushActionFromJsonString:message.data];
            if (pushAction != nil) {
                //TODO: process 
            }
        }
    };
    
    [TCGBGamebase addEventHandler:eventHandler];
}
```
