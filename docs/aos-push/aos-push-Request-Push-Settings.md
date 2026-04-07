---
source: aos-push.md
split: true
created_date_time: 20260406_141859
keyword: "Request Push Settings"
section: "Request Push Settings"
order: 4
---

### Request Push Settings

사용자의 푸시 설정을 조회하기 위해, 다음 API를 이용합니다. <br/>
콜백으로 오는 GamebasePushTokenInfo 값으로 사용자 설정값을 얻을 수 있습니다.

**API**

```java
+ (void)Gamebase.Push.queryTokenInfo(@NonNull Activity activity,
                                     @NonNull GamebaseDataCallback<GamebasePushTokenInfo> callback);

// Legacy API
+ (void)Gamebase.Push.queryPush(@NonNull Activity activity,
                                @NonNull GamebaseDataCallback<PushConfiguration> callback);
```

**Example**

```java
Gamebase.Push.queryTokenInfo(activity, new GamebaseDataCallback<PushConfiguration>() {
    @Override
    public void onCallback(GamebasePushTokenInfo data, GamebaseException exception) {
        if (Gamebase.isSuccess(exception)) {
            // Succeeded.
            boolean enablePush = data.agreement.pushEnabled;
            boolean enableAdPush = data.agreement.adAgreement;
            boolean enableAdNightPush = data.agreement.adAgreementNight;
            String token = data.token;
        } else {
            // Failed.
        }
    }
});
```

#### GamebasePushTokenInfo

| Parameter           | Values                | Description         |
| --------------------| ----------------------| ------------------- |
| pushType            | String                | Push 토큰 타입       |
| token               | String                | 토큰                 |
| userId              | String                | 사용자 아이디         |
| deviceCountryCode   | String                | 국가 코드           |
| timezone            | String                | 표준시간대           |
| registeredDateTime  | String                | 토큰 업데이트 시간    |
| languageCode        | String                | 언어 설정            |
| agreement           | GamebasePushAgreement | 수신 동의 여부        |

#### GamebasePushAgreement

| Parameter        | Values  | Description               |
| -----------------| --------| ------------------------- |
| pushEnabled      | boolean | 알림 표시 동의 여부           |
| adAgreement      | boolean | 광고성 알림 표시 동의 여부      |
| adAgreementNight | boolean | 야간 광고성 알림 표시 동의 여부  |
