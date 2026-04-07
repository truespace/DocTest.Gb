---
source: unity-logger.md
split: true
created_date_time: 20260406_141859
keyword: "Send Handled Exceptions"
section: "Send Handled Exceptions"
order: 6
---

### Send Handled Exceptions

일반/크래시 로그뿐만 아니라, try/catch 구문에서 예외와 관련된 내용을 Report API를 사용하여 전송할 수 있습니다.
이렇게 전송한 예외 로그는 **Log & Crash Search** 콘솔 > **App Crash Search** 탭의 **오류 유형**에서 'Handled'로 필터링하여 조회할 수 있습니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_WEBGL

```cs
static void Report(GamebaseLoggerConst.LogLevel logLevel, string message, string logString, string stackTrace)
```

**Example**
```cs
public void ReportSample(Exception e)
{
    Gamebase.Logger.Report(GamebaseLoggerConst.LogLevel.ERROR, "message", e.Message, e.StackTrace);
}
```
