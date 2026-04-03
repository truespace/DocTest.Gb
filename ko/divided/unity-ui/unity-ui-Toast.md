---
source: unity-ui.md
section: "Toast"
order: 7
created_date: 2026-04-03
---

## Toast

다음 API를 사용하여 쉽게 메시지를 표시할 수 있습니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID

```cs
static void ShowToast(string message, int duration)
static void ShowToast(string message, GamebaseUIToastType type)
```

**Example**
```cs
public void ShowToast(string message, int duration)
{
    Gamebase.Util.ShowToast(
        message,
        duration
        );
}
public void ShowToast(string message, GamebaseUIToastType type)
{
    Gamebase.Util.ShowToast(
        message,
        type
        );
}
```
