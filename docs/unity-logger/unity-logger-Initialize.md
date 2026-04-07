---
source: unity-logger.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, Logger, Initialize, InitializeSample"
section: Initialize
order: 1
---

## Game > Gamebase > Unity SDK 사용 가이드 > Logger

여기에서는 Log & Crash Search 전송 API를 사용하는 방법을 알아보겠습니다.

### Initialize
Log & Crash Search에서 발급 받은 앱키로 NHN Cloud Logger SDK를 초기화합니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_WEBGL

```cs
static void Initialize(GamebaseRequest.Logger.Configuration configuration)
```

**Example**
```cs
public static void InitializeSample()
{
    var configuration = new GamebaseRequest.Logger.Configuration("USER_LOGGER_APP_KEY");
    // configuration.enableCrashReporter = true;    // Whether to send crash logs.
    // configuration.enableCrashErrorLog =  true;   // Errro log is excluded by default. Use it if you want to collect error logs.
    Gamebase.Logger.Initialize(configuration);
}
```
