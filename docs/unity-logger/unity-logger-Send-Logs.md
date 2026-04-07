---
source: unity-logger.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, Logger, Send Logs"
section: "Send Logs"
order: 2
---

### Send Logs
Log & Crash Server로 로그를 전송합니다
NHN Cloud Logger SDK는 아래 다섯 가지 레벨의 로그를 전송할 수 있습니다. 
* DEBUG
* INFO
* WARN
* ERROR
* FATAL

로그 레벨은 다음과 같습니다.
* DEBUG > INFO > WARN > ERROR > FATAL

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_WEBGL

```cs
static void Debug(string message, Dictionary<string, string> userFields = null)
static void Info(string message, Dictionary<string, string> userFields = null)
static void Warn(string message, Dictionary<string, string> userFields = null)
static void Error(string message, Dictionary<string, string> userFields = null)
static void Fatal(string message, Dictionary<string, string> userFields = null)
```

**Example**
```cs
public void DebugSample()
{
    Dictionary<string, string> userFields = new Dictionary&lt;string, string>()
    {
        { "KEY_1", "VALUE_1" },
        { "KEY_2", "VALUE_2" },
    };
        
    Gamebase.Logger.Debug(
        "MESSAGE", 
        userFields);
}

public void InfoSample()
{
    Dictionary<string, string> userFields = new Dictionary&lt;string, string>()
    {
        { "KEY_1", "VALUE_1" },
        { "KEY_2", "VALUE_2" },
    };
        
    Gamebase.Logger.Info(
        "MESSAGE", 
        userFields);
}

public void WarnSample()
{
    Dictionary<string, string> userFields = new Dictionary&lt;string, string>()
    {
        { "KEY_1", "VALUE_1" },
        { "KEY_2", "VALUE_2" },
    };
        
    Gamebase.Logger.Warn(
        "MESSAGE", 
        userFields);
}

public void ErrorSample()
{
    Dictionary<string, string> userFields = new Dictionary&lt;string, string>()
    {
        { "KEY_1", "VALUE_1" },
        { "KEY_2", "VALUE_2" },
    };
        
    Gamebase.Logger.Error(
        "MESSAGE", 
        userFields);
}

public void FatalSample()
{
    Dictionary<string, string> userFields = new Dictionary&lt;string, string>()
    {
        { "KEY_1", "VALUE_1" },
        { "KEY_2", "VALUE_2" },
    };
        
    Gamebase.Logger.Fatal(
        "MESSAGE", 
        userFields);
}
```
