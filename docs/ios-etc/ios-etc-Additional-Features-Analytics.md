---
source: ios-etc.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, Analytics, setGameUserData, requestPurchase, setGameUserDataWithLevel, setChannelId, setCharacterId"
section: "Additional Features > Analytics"
order: 6
---

### Analytics

Game지표를 Gamebase Server로 전송할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> Gamebase Analytics에서 지원하는 모든 API는 로그인 후에 호출할 수 있습니다.

> [TIP]
>
> TCGBPurchase의 requestPurchase API의 호출을 통한 결제를 완료하면 자동으로 지표를 전송합니다.

Analytics Console 사용법은 아래 가이드를 참고하십시오.

- [Analytics Console](../oper-analytics.md)

#### Game User Data Settings

게임 로그인 이후 게임 유저 레벨 정보를 지표로 전송할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> 게임 로그인 이후 SetGameUserData API를 호출하지 않으면 다른 지표에서 Level 정보가 누락될 수 있습니다.
>

API 호출에 필요한 파라미터는 아래와 같습니다.

**GameUserData**

| Name | Mandatory(M) / Optional(O) | type | Desc |
| -------------------------- | -------------------------- | ---- | ---- |
| userLevel | M | int | 게임 유저 레벨을 나타내는 필드입니다. |
| channelId | O | String | 채널을 나타내는 필드입니다. |
| characterId | O | String | 캐릭터 이름을 나타내는 필드입니다. |
| classId | O | String | 직업을 나타내는 필드입니다. |


**API**

```objectivec
+ (void)setGameUserData:(nonnull TCGBAnalyticsGameUserData *)gameUserData;
```

**Example**

```objectivec
- (void)setGameUserDataWithLevel:(int)level channelId:(NSString *)channelId characterId:(NSString *)characterId {
    TCGBAnalyticsGameUserData* gameUserData = [TCGBAnalyticsGameUserData gameUserDataWithUserLevel:level];
    [gameUserData setChannelId:channelId];
    [gameUserData setCharacterId:characterId];
    [TCGBAnalytics setGameUserData:gameUserData];
}
```

#### Level Up Trace

레벨업이 되었을 경우 게임 유저 레벨 정보를 지표로 전송할 수 있습니다.

API 호출에 필요한 파라미터는 아래와 같습니다.

**LevelUpData**

| Name | Mandatory (M) / Optional (O) | type | Desc |
| -------------------------- | -------------------------- | ---- | ---- |
| userLevel | M | int | 게임 유저 레벨을 나타내는 필드입니다. |
| levelUpTime | M | long | Epoch time으로 입력합니다.</br>밀리초(ms) 단위로 입력합니다. |

**API**

```objectivec
+ (void)traceLevelUpWithLevelUpData:(nonnull TCGBAnalyticsLevelUpData *)levelUpData;
```

**Example**

```objectivec
- (void)traceLevelUpWith:(int)level levelUpTime:(long long)levelUpTime channelId:(NSString *)channelId characterId:(NSString *)characterId {
  TCGBAnalyticsLevelUpData* levelUpData = [TCGBAnalyticsLevelUpData levelUpDataWithUserLevel:level levelUpTime:levelUpTime];
  [TCGBAnalytics traceLevelUpWithLevelUpData:levelUpData];
}
```
