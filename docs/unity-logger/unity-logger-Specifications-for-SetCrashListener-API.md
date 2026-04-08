---
source: unity-logger.md
section: "Specifications for SetCrashListener API"
order: 5
split: true
created_date_time: 20260408_191848
keyword: Unity, Logger, Specifications
---

### Specifications for SetCrashListener API
유니티를 이용하다보면 수집을 원하지 않는 예외 로그 혹은 크래시 로그들이 수집될 수 있습니다.
NHN Cloud Logger SDK는 수집을 원하지 않는 크래시 로그를 필터링 하는 기능을 지원합니다.
crashFilter의 return값이 true이면 로그는 필터링 됩니다.

> <font color="red">[주의]</font><br/>
>
> 해당 기능은 유니티 예외에 한정된 기능입니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_WEBGL

```cs
static void AddCrashFilter(GamebaseCallback.Logger.CrashFilter filter)
static void RemoveCrashFilter(GamebaseCallback.Logger.CrashFilter filter)
```

**Example**
```cs
public GamebaseCallback.Logger.CrashFilter crashFilter = (crashLogData) =>
{
    // If the return value is true, no log is sent.
    // The properties of CrashLogData are the same as the parameters of Application.LogCallback on Unity.
    // https://docs.unity3d.com/ScriptReference/Application.LogCallback.html
    return crashLogData.Condition.Contains("UnityEngine.Debug.Log");
};

public void AddCrashFilterSample()
{
    Gamebase.Logger.AddCrashFilter(crashFilter);
}

public void RemoveCrashFilterSample()
{
    Gamebase.Logger.RemoveCrashFilter(crashFilter);
}
```
