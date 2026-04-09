---
source: unity-push.md
section: "Request Push Settings"
order: 4
split: true
created_date_time: 20260408_184906
keyword: Unity, Push, Alert
---

### Request Push Settings

사용자의 푸시 설정을 조회하기 위해, 다음 API를 이용합니다. <br/>
콜백으로 오는 GamebaseResponse.Push.TokenInfo 값으로 사용자 설정값을 얻을 수 있습니다.

**API**

Supported Platforms

<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

```cs
public static void QueryTokenInfo(GamebaseCallback.GamebaseDelegate<GamebaseResponse.Push.TokenInfo> callback);

// Legacy API
public static void QueryPush(GamebaseCallback.GamebaseDelegate<GamebaseResponse.Push.PushConfiguration> callback);
```

**Example**

```cs
public void QueryTokenInfoSample(bool isSandbox)
{
    Gamebase.Push.QueryTokenInfo((data, error)=> 
    {
        if (Gamebase.IsSuccess(error)) 
        {
            // Succeeded.
            bool enablePush = data.agreement.pushEnabled;
            bool enableAdPush = data.agreement.adAgreement;
            bool enableAdNightPush = data.agreement.adAgreementNight;
            string token = data.token;
        } 
        else 
        {
        // Failed.
        }
    });
}
```

#### GamebaseResponse.Push.TokenInfo

| Parameter           | Values                | Description         |
| --------------------| ----------------------| ------------------- |
| pushType            | string                | Push 토큰 타입       |
| token               | string                | 토큰                 |
| userId              | string                | 사용자 아이디         |
| deviceCountryCode   | string                | 국가 코드           |
| timezone            | string                | 표준시간대           |
| registeredDateTime  | string                | 토큰 업데이트 시간    |
| languageCode        | string                | 언어 설정            |
| agreement           | GamebaseResponse.Push.Agreement | 수신 동의 여부        |
| sandbox             | bool                  | sandbox 여부(iOS에 한함)        |

#### GamebaseResponse.Push.Agreement

| Parameter        | Values  | Description               |
| -----------------| --------| ------------------------- |
| pushEnabled      | bool | 알림 표시 동의 여부           |
| adAgreement      | bool | 광고성 알림 표시 동의 여부      |
| adAgreementNight | bool | 야간 광고성 알림 표시 동의 여부  |
