---
source: unity-etc.md
section: "IDFA"
order: 8
created_date: 2026-04-03
---

### IDFA

* 단말기의 광고 식별자 값을 반환합니다.

iOS에서 IDFA 기능을 설정하는 방법은 다음 문서를 참고하시기 바랍니다.<br/>
* [iOS IDFA](../../ios-etc.md#idfa)<br/>

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS

```cs
static void GetIdfa();
```

**Example**

``` cs
public void SampleGetIdfa()
{
#if UNITY_IOS
    string idfa = Gamebase.Util.GetIdfa(); iOS only
#endif
}
```
