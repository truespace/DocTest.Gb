---
source: unity-etc.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, Additional, GetDeviceLanguageCode"
section: "Additional Features > Device Language"
order: 1
---

## Game > Gamebase > Unity SDK 사용 가이드 > ETC

## Additional Features

Gamebase에서 지원하는 부가 기능을 설명합니다.

### Device Language

* 단말기에 설정된 언어 코드를 반환합니다.
* 여러개의 언어가 등록된 경우, 우선권이 가장 높은 언어만을 반환합니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#5319E7; font-size: 10pt">■</span> UNITY_WEBGL
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static string GetDeviceLanguageCode()
```

> [참고]
>
> Editor on Windows, Standalone on Windows인 경우에는 [CultureInfo](https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo?view=netframework-4.7.2)를 참고하여 언어 코드를 반환합니다.
>
> Editor on Mac, WebGL은 [Application.systemLanguage](https://docs.unity3d.com/ScriptReference/SystemLanguage.html) 값을 참고하여 언어 코드를 반환합니다.<br/>예를 들어, Application.systemLanguage == SystemLanguage.Korean인 경우에는 'ko'를 반환합니다.
