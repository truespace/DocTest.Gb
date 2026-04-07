---
source: ios-push.md
split: true
created_date_time: 20260406_141859
keyword: "Get NotificationOptions"
section: "Get NotificationOptions"
order: 4
---

### Get NotificationOptions

푸시를 등록할 때 설정한 알림 옵션값을 가져옵니다.

```objectivec
- (void)didLoginSucceeded {
    TCGBNotificationOptions *options = [TCGBPush notificationOptions];

    if (options == nil) {
        // You need to login and call the registerPush API first.
    }
}
```

> [참고]
>
> foregroundEnabled 옵션은 런타임 때 변경이 가능합니다.
> badgeEnabled, soundEnabled 옵션은 registerPush API 최초 호출 시에만 반영이 되고 런타임 때의 변경은 보장되지 않습니다.
>
