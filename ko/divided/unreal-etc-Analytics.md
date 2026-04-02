## Game > Gamebase > Unreal SDK 사용 가이드 > ETC

### Analytics

Game지표를 Gamebase Server로 전송할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> Gamebase Analytics에서 지원하는 모든 API는 로그인 후에 호출할 수 있습니다.
>
>
> [TIP]
>
> RequestPurchase API를 호출하여 결제를 완료하면, 자동으로 지표를 전송합니다.
>

Analytics Console 사용법은 아래 가이드를 참고하십시오.

* [Analytics Console](./oper-analytics)

#### Game User Data Settings

게임 로그인 이후 게임 유저 레벨 정보를 지표로 전송할 수 있습니다.

> <font color="red">[주의]</font><br/>
>
> 게임 로그인 이후 SetGameUserData API를 호출하지 않으면 다른 지표에서 Level 정보가 누락될 수 있습니다.
>

API 호출에 필요한 파라미터는 아래와 같습니다.

**FGamebaseAnalyticsUserData**

| Name                       | Mandatory(M) / Optional(O) | type | Desc |
| -------------------------- | -------------------------- | ---- | ---- |
| UserLevel | M | int32 | 게임 유저 레벨을 나타내는 필드입니다. |
| ChannelId | O | FString | 채널을 나타내는 필드입니다. |
| CharacterId | O | FString | 캐릭터 이름을 나타내는 필드입니다. |
| CharacterClassId | O | FString | 직업을 나타내는 필드입니다. |

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void SetGameUserData(const FGamebaseAnalyticsUserData& GameUserData);
```

**Example**

```cpp
void USample::SetGameUserData(int32 UserLevel, const FString& ChannelId, const FString& CharacterId, const FString& CharacterClassId)
{
    FGamebaseAnalyticsUserData GameUserData;
    GameUserData.UserLevel = UserLevel;
    GameUserData.ChannelId = ChannelId;
    GameUserData.CharacterId = CharacterId;
    GameUserData.CharacterClassId = CharacterClassId;
    
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetAnalytics()->SetGameUserData(GameUserData);
}

```

#### Level Up Trace

레벨업이 되었을 경우 게임 유저 레벨 정보를 지표로 전송할 수 있습니다.

API 호출에 필요한 파라미터는 아래와 같습니다.

**LevelUpData**

| Name                       | Mandatory(M) / Optional(O) | type | Desc    |
| -------------------------- | -------------------------- | ---- | ---- |
| UserLevel | M | int32 | 게임 유저 레벨을 나타내는 필드입니다. |
| LevelUpTime | M | long | Epoch Time으로 입력합니다.</br>Millisecond 단위로 입력합니다. |

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void TraceLevelUp(const FGamebaseAnalyticesLevelUpData& levelUpData);
```

**Example**

```cpp
void USample::TraceLevelUpNow(int32 UserLevel)
{
    FGamebaseAnalyticesLevelUpData levelUpData{ UserLevel, FDateTime::Now().ToUnixTimestamp() };
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetAnalytics()->TraceLevelUp(levelUpData);
}
```
