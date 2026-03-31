## Game > Gamebase > Unreal SDK 사용 가이드 > ETC

### IDFA

* 단말기의 광고 식별자 값을 반환합니다.
* iOS에서 IDFA 기능을 설정하는 방법은 다음 문서를 참고하세요.
    * [iOS IDFA](./ios-etc/#idfa)

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
FString GetIdfa();
```

**Example**

```cpp
void USample::GetIdfa()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    FString Idfa = Subsystem->GetUtil()->GetIdfa();
}
```
