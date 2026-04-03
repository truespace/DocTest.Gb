---
source: aos-etc.md
section: "Analytics"
order: 5
created_date: 2026-04-03
---

### Analytics

Game지표를 Gamebase Server로 전송할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> Gamebase Analytics에서 지원하는 모든 API는 로그인 후에 호출이 가능합니다.
>

> [TIP]
>
> Gamebase.Purchase.requestPurchase() API를 호출하여 결제를 진행한 경우, 결제가 완료되면 자동으로 서버로 지표가 전송됩니다.
>

#### Game User Data Settings

로그인 이후 유저 레벨 정보를 설정할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> 게임 로그인 이후 setGameUserData API를 호출하지 않으면 다른 지표에서 Level 정보가 누락될 수 있습니다.
>

API 호출에 필요한 파라미터는 아래와 같습니다.

**GameUserData**

| Name                       | Mandatory(M) / Optional(O) | type | Desc |
| -------------------------- | -------------------------- | ---- | ---- |
| userLevel | M | int | 유저 레벨을 나타내는 필드입니다. |
| channelId | O | String | 채널을 나타내는 필드입니다. |
| characterId | O | String | 캐릭터 이름을 나타내는 필드입니다. |
| classId | O | String | 직업을 나타내는 필드입니다. |

**API**

```java
Gamebase.Analytics.setGameUserData(GameUserData gameUserData);
```

**Example**

``` java
public void onLoginSuccess() {
    int userLevel = 10;
    String channelId, characterId, classId;

    GameUserData gameUserData = new GameUserData(userLevel);
    gameUserData.channelId = channelId; // Optional
    gameUserData.characterId = characterId; // Optional
    gameUserData.classId = classId; // Optional

    Gamebase.Analytics.setGameUserData(gameUserData);
}
```

#### Level Up Trace

레벨업이 되었을 경우 유저 레벨 정보를 변경할 수 있습니다.

API 호출에 필요한 파라미터는 아래와 같습니다.

**LevelUpData**

| Name                       | Mandatory(M) / Optional(O) | type | Desc	|
| -------------------------- | -------------------------- | ---- | ---- |
| userLevel | M | int | 유저 레벨을 나타내는 필드입니다. |
| levelUpTime | M | long | Epoch Time으로 입력합니다.</br>Millisecond 단위로 입력 합니다. |



**API**

```java
Gamebase.Analytics.traceLevelUp(LevelUpData levelUpData);
```

**Example**

``` java
public void onLevelUp(int userLevel, long levelUpTime) {
    LevelUpData levelUpData = new LevelUpData(userLevel, levelUpTime);

    Gamebase.Analytics.traceLevelUp(levelUpData);
}
```
