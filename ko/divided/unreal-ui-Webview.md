## Game > Gamebase > Unreal SDK 사용 가이드 > UI

## Webview

### Show WebView

웹뷰를 표시합니다.<br/>

##### Required 파라미터
* Url: 파라미터로 전송되는 url은 유효한 값이어야 합니다.

##### Optional 파라미터(현재는 Required 파라미터지만, 이후 버전에서 Optional로 변경 예정)
* Configuration: GamebaseWebViewConfiguration으로 웹뷰의 레이아웃을 변경할 수 있습니다.
* closeCallback: 웹뷰가 종료될 때 사용자에게 콜백으로 알려 줍니다.
* SchemeList: 사용자가 받고 싶은 커스텀 스킴 목록을 지정합니다.
* schemeEvent: schemeList로 지정한 커스텀 스킴을 포함하는 url을 콜백으로 알려 줍니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void ShowWebView(const FString& Url, const FGamebaseWebViewConfiguration& Configuration, FGamebaseErrorDelegate& CloseCallback, const TArray<FString>& SchemeList, const FGamebaseSchemeEventDelegate& onSchemeEvent);
```

**Example**
```cpp
void USample::ShowWebView(const FString& Url)
{
    FGamebaseWebViewConfiguration Configuration;
    Configuration.Title = TEXT("Title");

    TArray<FString> SchemeList{ TEXT("customScheme://openBrowser") };

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetWebView()->ShowWebView(Url, Configuration,
        FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error) {
            Result(ANSI_TO_TCHAR(__FUNCTION__), TEXT("Close webview"));
        }),
        SchemeList,
        FGamebaseSchemeEventDelegate::CreateLambda([](const FString& Scheme, const FGamebaseError* Error) {
        if (Gamebase::IsSuccess(Error))
        {
            Result(ANSI_TO_TCHAR(__FUNCTION__), true, *FString::Printf(TEXT("Scheme= %s"), *Scheme));
        }
        else
        {
            Result(ANSI_TO_TCHAR(__FUNCTION__), false, GamebaseJsonUtil::UStructToJsonObjectString(*Error));
        }
    }));
}
```


#### FGamebaseWebViewConfiguration

| Parameter                | Values                                           | Description |
| ------------------------ | ------------------------------------------------ | --- |
| Title                    | FString                                          | 웹뷰의 제목 |
| Orientation              | GamebaseScreenOrientation::Unspecified           | 미지정(**default**) |
|                          | GamebaseScreenOrientation::Portrait              | 세로 모드 |
|                          | GamebaseScreenOrientation::Landscape             | 가로 모드 |
|                          | GamebaseScreenOrientation::LandscapeReverse      | 가로 모드를 180도 회전 |
| ContentMode              | GamebaseWebViewContentMode::Recommended          | 현재 플랫폼 추천 브라우저(**default**) |
|                          | GamebaseWebViewContentMode::Mobile               | 모바일 브라우저 |
|                          | GamebaseWebViewContentMode::Desktop              | 데스크톱 브라우저 |
| NavigationColor          | FColor                                           | 내비게이션 바 색상<br>**default**: FColor(18, 93, 230, 255) |
| NavigationTitleColor     | FColor                                           | 내비게이션 바 제목 색상<br>**default**: FColor::White |
| NavigationIconTintColor  | TOptional&lt;FColor&gt;                          | 내비게이션 바 아이콘 틴트 색상 |
| NavigationBarHeight      | int32                                            | 내비게이션 바 높이 |
| bIsNavigationBarVisible  | bool                                             | 내비게이션 바 활성 또는 비활성<br>**default**: true |
| bIsBackButtonVisible     | bool                                             | 뒤로 가기 버튼 활성 또는 비활성<br>**default**: true |
| BackButtonImageResource  | FString                                          | 뒤로 가기 버튼 이미지 |
| CloseButtonImageResource | FString                                          | 닫기 버튼 이미지 |
| bEnableFixedFontSize     | bool                                             | 약관 창의 글자 크기 고정 여부 결정<br>**default**: false<br>**Android에 한함** |
| bRenderOutSideSafeArea   | bool                                             | SafeArea를 무시하고 Cutout 영역에도 렌더링<br>**default**: false<br>**Android에 한함** |
| CutoutColor              | TOptional&lt;FColor&gt;                          | SafeArea 밖의 Cutout 영역 바탕 색상<br>**Android에 한함** |

> [TIP]
>
> iPadOS 13 이상에서 웹뷰는 기본적으로 데스크톱 모드입니다.
> contentMode =`GamebaseWebViewContentMode::MOBILE` 설정으로 모바일 모드로 변경할 수 있습니다.

#### Predefined Custom Scheme

Gamebase에서 지정해 놓은 스킴입니다.

| Scheme | 용도 |
| ----------------------------- | ------------------------------ |
| gamebase://dismiss | 웹뷰 닫기 |
| gamebase://getMaintenanceInfo | 점검 내용을 WebPage에 표시 |
| gamebase://getUserId          | 현재 로그인된 게임 유저의 사용자 ID를 표시 |
| gamebase://goBack | 웹뷰 뒤로 가기 |


### Close WebView

다음 API를 이용해 보이는 웹뷰를 닫을 수 있습니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void CloseWebView();
```

**Example**CloseWebview
```cpp
void USample::CloseWebView()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetWebView()->CloseWebView();
}
```
