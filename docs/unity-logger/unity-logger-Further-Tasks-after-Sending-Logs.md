---
source: unity-logger.md
section: "Further Tasks after Sending Logs"
order: 4
split: true
created_date_time: 20260408_184906
keyword: Unity, Logger, Further
---

### Further Tasks after Sending Logs
리스너를 등록하면 로그 전송 후 추가 작업을 진행할 수 있습니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_WEBGL

```cs
static void SetLoggerListener(GamebaseCallback.Logger.ILoggerListener listener)
```

**Example**
```cs
public class LoggerListener : GamebaseCallback.Logger.ILoggerListener
{
    public void OnError(GamebaseResponse.Logger.LogEntry log, string errorMessage)
    {
        // Sending logs failed
    }

    public void OnFilter(GamebaseResponse.Logger.LogEntry log, GamebaseResponse.Logger.LogFilter filter)
    {
        // The logs were filtered out and not sent.(Refer to AddClashFilter API Guide)
    }

    public void OnSave(GamebaseResponse.Logger.LogEntry log)
    {
        // If log transmission fails due to network disconnection, the log is saved in a file for log retransmission.(The saved file cannot be checked.)
    }

    public void OnSuccess(GamebaseResponse.Logger.LogEntry log)
    {
        // Sending logs succeeded
    }
}                    

public void SetLoggerListenerSample()
{
    LoggerListener listener = new LoggerListener();
    Gamebase.Logger.SetLoggerListener(listener);
}
```
