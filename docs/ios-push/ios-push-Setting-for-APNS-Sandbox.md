---
source: ios-push.md
split: true
created_date_time: 20260406_141859
keyword: "Setting for APNS Sandbox"
section: "Setting for APNS Sandbox"
order: 3
---

### Setting for APNS Sandbox

SandboxMode를 켜면, APNS Sandbox로 Push를 발송하도록 등록할 수 있습니다.

* 클라이언트 설정 방법

```objectivec
- (void)didLoginSucceeded {
	[TCGBPush setSandboxMode:YES];
    [TCGBPush registerPushWithPushConfiguration:pushConfig completion:^(TCGBError *error) {
    	...
    }];
}
```

* 콘솔 발송 방법

Push 메뉴의 **대상**에서 **iOS Sandbox**를 선택한 후 발송합니다.
