---
source: unreal-ui.md
section: "ImageNotice"
order: 2
split: true
created_date_time: 20260408_184906
keyword: Unreal, ImageNotice, Console
---

## ImageNotice

콘솔에 이미지를 등록한 후 사용자에게 공지를 띄울 수 있습니다.

![ImageNotice Example](./image/imageNotice-guide-landscape-ko_v3.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: ImageNotice 관련 화면
    구성: ImageNotice 관련 스크린샷
    Keyword: Unreal, Screenshot, ImageNotice
-->

### Show ImageNotices

이미지 공지를 화면에 띄워 줍니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void ShowImageNotices(FGamebaseImageNoticeConfiguration& Configuration, const FGamebaseErrorDelegate& CloseCallback, const FGamebaseImageNoticeEventDelegate& EventCallback = {});
```

**Example**

```cpp
void USample::ShowImageNotices(int32 ColorR, int32 ColorG, int32 ColorB, int32 ColorA, int64 TimeOut)
{
    FGamebaseImageNoticeConfiguration Configuration;
    Configuration.BackgroundColor = FColor(ColorR, ColorG, colorB, colorA);
    Configuration.TimeOut = TimeOut;

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetImageNotice()->ShowImageNotices(Configuration,
        FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error) {
            // Called when the entire imageNotice is closed.
            ...
        }),
        FGamebaseSchemeEventDelegate::CreateLambda([](const FString& Scheme, const FGamebaseError* Error) {
            // Called when custom event occurred.
            ...
        })
    );
}
```

#### FGamebaseImageNoticeConfiguration

| Parameter                              | Values                                   | Description        |
| -------------------------------------- | ---------------------------------------- | ------------------ |
| BackgroundColor          | FColor       | 백그라운드 색상           |
| TimeOut                  | int64        | 이미지 공지 최대 로딩 시간(단위: millisecond)<br/>**default**: 5000 |


### Close ImageNotices

CloseImageNotices API를 호출하여 현재 표시 중인 이미지 공지를 모두 종료할 수 있습니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void CloseImageNotices();
```
