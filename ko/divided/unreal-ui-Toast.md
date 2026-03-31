## Game > Gamebase > Unreal SDK 사용 가이드 > UI

## Toast

다음 API를 사용하여 쉽게 메시지를 표시할 수 있습니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void ShowToast(const FString& Message, EGamebaseToastExposureTime ExposureTimeType);
```

**Example**
```cpp
void USample::ShowToast(const FString& Message, EGamebaseToastExposureTime ExposureTimeType)
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetUtil()->ShowToast(Message, ExposureTimeType);
}
```
