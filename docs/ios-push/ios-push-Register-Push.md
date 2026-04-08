---
source: ios-push.md
section: "Register Push"
order: 2
split: true
created_date_time: 20260408_191848
keyword: iOS, Login, Push, Alert, RegisterPush
---

### Register Push

다음 API를 호출하여 NHN Cloud Push에 해당 사용자를 등록합니다.

푸시 수신 동의 여부(TCGBPushConfiguration)를 사용자로부터 받아 다음의 API 호출을 통해 등록을 완료합니다.

> <font color="red">[주의]</font><br/>
>
> 푸시 토큰이 언제 만료될지 모르기 때문에, 로그인 이후에는 항상 registerPush API를 호출하는 것을 권장합니다.
>

#### API

```objectivec
+ (void)registerPushWithPushConfiguration:(TCGBPushConfiguration *)configuration
                               completion:(nullable void(^)(TCGBError * _Nullable error))completion;
```

#### TCGBPushConfiguration

| Parameter     | Mandatory(M) /<br/>Optional(O) | Values            | Description        |
| ------------- | ------------- | ---------------------------------- | ------------------ |
| pushEnabled                   | M             | BOOL         | 푸시 동의 여부 |
| ADAgreement                   | M             | BOOL         | 광고성 푸시 동의 여부 |
| ADAgreementNight              | M             | BOOL         | 야간 광고성 푸시 동의 여부 |
| alwaysAllowTokenRegistration  | O             | BOOL         | 사용자가 푸시 권한을 거부해도 토큰을 등록할지 여부<br>YES로 설정할 경우 푸시 권한을 획득하지 못하더라도 토큰을 등록합니다.<br>**default**: NO    |

#### Example

```objectivec
- (void)didLoginSucceeded {
    BOOL enablePush;
    BOOL enableAdPush;
    BOOL enableAdNightPush;
    BOOL alwaysAllowTokenRegistration;
    
    // You should receive the above values to the logged-in user.

    TCGBPushConfiguration* pushConfig = [TCGBPushConfiguration pushConfigurationWithPushEnable:enablePush
                                                                                   ADAgreement:enableAdPush
                                                                              ADAgreementNight:enableAdNightPush
                                                                  alwaysAllowTokenRegistration:alwaysAllowTokenRegistration];

    [TCGBPush registerPushWithPushConfiguration:pushConfig completion:^(TCGBError* error) {
        if (error != nil) {
            // To Register Push Failed.
        }
    }];
}
```

<br/>

NHN Cloud Push에 사용자를 등록할 때 TCGBNotificationOptions 객체로 알림 옵션 설정이 가능합니다.

포그라운드 푸시 여부(foregroundEnabled), 배지 사용 여부(badgeEnabled), 알림음 사용 여부(soundEnabled) 값을 사용자로부터 받아, 다음의 API 호출을 통해 알림 옵션 설정이 가능합니다.

#### API

```objectivec
+ (void)registerPushWithPushConfiguration:(TCGBPushConfiguration *)configuration
                      notificationOptions:(nullable TCGBNotificationOptions *)notificationOptions
                               completion:(nullable void(^)(TCGBError * _Nullable error))completion;
```

#### TCGBNotificationOptions

| Parameter     | Mandatory(M) /<br/>Optional(O) | Values            | Description        |
| ------------- | ------------- | ---------------------------------- | ------------------ |
| foregroundEnabled   | M     | BOOL         | 앱이 포그라운드 상태일 때의 알림 노출 여부<br/>**default**: NO           |
| badgeEnabled        | M     | BOOL         | 배지 아이콘 사용 여부<br/>**default**: YES           |
| soundEnabled        | M     | BOOL         | 알림음 사용 여부<br/>**default**: YES           |

#### Example

```objectivec
- (void)didLoginSucceeded {
    BOOL enablePush;
    BOOL enableAdPush;
    BOOL enableAdNightPush;
    BOOL alwaysAllowTokenRegistration;

    BOOL foregroundEnabled;
    BOOL badgeEnabled;
    BOOL soundEnabled;

    // You should receive the above values to the logged-in user.

    TCGBPushConfiguration *pushConfig = [TCGBPushConfiguration pushConfigurationWithPushEnable:enablePush
                                                                                   ADAgreement:enableAdPush
                                                                              ADAgreementNight:enableAdNightPush
                                                                  alwaysAllowTokenRegistration:alwaysAllowTokenRegistration];
    
    TCGBNotificationOptions *options = [TCGBNotificationOptions notificationOptionsWithForegroundEnabled:foregroundEnabled 
                                                                                            badgeEnabled:badgeEnabled 
                                                                                            soundEnabled:soundEnabled];

    [TCGBPush registerPushWithPushConfiguration:pushConfig notificationOptions:options completion:^(TCGBError* error) {
        if (error != nil) {
            // To Register Push Failed.
        }
    }];
    // You should receive the above values to the logged-in user.
}
```
