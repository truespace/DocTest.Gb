## Game > Gamebase > Unreal SDK 사용 가이드 > ETC

### Device Language

* 단말기에 설정된 언어 코드를 반환합니다.
* 여러 개의 언어가 등록된 경우, 우선권이 가장 높은 언어만을 반환합니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
FString GetDeviceLanguageCode() const;
```
