---
source: unreal-ui.md
section: "Terms"
order: 3
split: true
created_date_time: 20260408_191848
keyword: Unreal, Login, Push, WebView, Initialize, Terms, ShowTermsView, RegisterPush, Console
---

## Terms

Gamebase 콘솔에 설정한 약관을 표시합니다.

![TermsView Example](./image/termsView-guide-ui-001_2.20.0.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: 약관 동의 화면
    구성: Gamebase 약관 동의 UI 화면
    Keyword: Screenshot, Terms
-->

ShowTermsView API는 웹뷰로 약관 창을 표시해줍니다.
Game 의 UI 에 맞는 약관 창을 직접 제작하고자 하는 경우에는 QueryTerms API를 호출하여, Gamebase 콘솔에 설정한 약관 항목을 불러올 수 있습니다.
유저가 약관에 동의했다면 각 항목별 동의 여부를 UpdateTerms API를 통해 Gamebase 서버로 전송하시기 바랍니다.

### ShowTermsView

약관 창을 화면에 띄워 줍니다.
유저가 약관에 동의를 했을 경우, 동의 여부를 서버에 등록합니다.
약관에 동의했다면 ShowTermsView API를 다시 호출해도 약관 창이 표시되지 않고 바로 성공 콜백이 반환됩니다.
단, Gamebase 콘솔에서 약관 재동의 항목을 **필요** 로 변경했다면 유저가 다시 약관에 동의할 때까지는 약관 창이 표시됩니다.

> <font color="red">[주의]</font><br/>
>
> * FGamebasePushConfiguration은 약관 창이 표시되지 않은 경우에는 null입니다(약관 창이 표시되었다면 항상 유효한 객체가 반환됩니다.).
> * FGamebasePushConfiguration.bPushEnabled 값은 항상 true입니다.
> * FGamebasePushConfiguration이 null이 아니라면 **로그인 후에** Subsystem->GetPush()->RegisterPush()를 호출하세요.

#### Optional 파라미터

* GamebaseTermsConfiguration : GamebaseTermsConfiguration 객체를 통해 강제 약관 동의 창 표시 여부와 같은 설정을 변경할 수 있습니다.
* Callback: 약관 동의 후 약관 창이 종료될 때 사용자에게 콜백으로 알려줍니다. 콜백으로 오는 GamebaseResponse.DataContainer 객체는 GamebaseResponse.Push.PushConfiguration 변환해서 로그인 후 Gamebase.Push.RegisterPush API에 사용할 수 있습니다.

**FGamebaseTermsConfiguration** 
 
| API | Mandatory(M) / Optional(O) | Description | 
| --- | --- | --- | 
| bForceShow | O | 약관에 동의했다면 ShowTermsView API를 다시 호출해도 약관 창이 표시되지 않지만, 이를 무시하고 강제로 약관 창을 표시합니다.<br>**default**: false | 
| bEnableFixedFontSize | O | 약관 창의 폰트 사이즈를 고정할지 결정합니다.<br>**default** : false<br/>**Android에 한함** |
 
**FGamebaseShowTermsViewResult**

| Parameter              | Values                          | Description         |
| ---------------------- | --------------------------------| ------------------- |
| bIsTermsUIOpened        | bool                            | **true** : 유저가 약관에 동의하여 약관 창이 종료되었습니다.<br>**false** : 이미 약관에 동의하여 약관 창이 표시되지 않고 종료되었습니다.        |

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS

```cpp
void ShowTermsView(const FGamebaseDataContainerDelegate& Callback);
void ShowTermsView(const FGamebaseTermsConfiguration& Configuration, const FGamebaseDataContainerDelegate& Callback);
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| NOT\_INITIALIZED | 1 | Gamebase가 초기화되어 있지 않습니다. |
| LAUNCHING\_SERVER\_ERROR | 2001 | 론칭 서버에서 전달받은 항목에 약관 관련 내용이 없는 경우에 발생하는 에러입니다.<br/>정상적인 상황이 아니므로 Gamebase 담당자에게 문의해주시기 바랍니다. |
| UI\_TERMS\_ALREADY\_IN\_PROGRESS\_ERROR | 6924 | Terms API 호출이 아직 완료되지 않았습니다.<br/>잠시 후 다시 시도하세요. |
| UI\_TERMS\_ANDROID\_DUPLICATED\_VIEW | 6925 | 약관 웹뷰가 아직 종료되지 않았는데 다시 호출되었습니다. |
| WEBVIEW\_TIMEOUT | 7002 | 약관 웹뷰 표시 중 타임아웃이 발생했습니다. |
| WEBVIEW\_HTTP\_ERROR | 7003 | 약관 웹뷰 오픈 중 HTTP 에러가 발생하였습니다. |

**Example**

```cpp
void USample::ShowTermsView()
{
    FGamebaseTermsConfiguration Configuration { true };

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetTerms()->ShowTermsView(Configuration,
        FGamebaseDataContainerDelegate::CreateLambda([](const FGamebaseDataContainer* DataContainer, const FGamebaseError* Error) {
            if (Gamebase::IsSuccess(Error))
            {
                UE_LOG(LogTemp, Display, TEXT("ShowTermsView succeeded."));
                
                const auto result = FGamebaseShowTermsResult::From(DataContainer);
                if (result.IsValid())
                {
                    // Save the 'PushConfiguration' and use it for RegisterPush() after Login().
                    SavedPushConfiguration = FGamebasePushConfiguration::From(DataContainer);
                }
            }
            else
            {
                UE_LOG(LogTemp, Display, TEXT("ShowTermsView failed. (Error: %d)"), Error->Code);
            }
        })
    );
}

void USample::AfterLogin()
{
    // Call RegisterPush with saved PushConfiguration.
    if (SavedPushConfiguration != null)
    {
        Gamebase.Push.RegisterPush(SavedPushConfiguration, (Error) =>
        {
            ...
        });
    }
}
```


### QueryTerms

Gamebase는 단순한 형태의 웹뷰로 약관을 표시합니다.
게임UI에 맞는 약관을 직접 제작하고자 하신다면, QueryTerms API를 호출하여 Gamebase 콘솔에 설정한 약관 정보를 내려받아 활용하실 수 있습니다.

'선택' 약관 항목은 로그인 후에 호출하면 동의 여부도 함께 알 수 있습니다. 단, '필수' 항목의 동의 여부는 항상 false로 반환됩니다.

> <font color="red">[주의]</font><br/>
>
> * GamebaseResponse.Terms.ContentDetail.required가 true인 필수 항목은 동의 여부를 Gamebase 서버에 저장하지 않으므로 bAgreed 값은 항상 false로 반환됩니다.
>     * 약관 필수 항목에 동의하지 않은 경우 게임 진행 또는 게임 로그인이 불가능하므로 약관 팝업이 닫혀 있고 로그인되어 있는 상태라면 자연스럽게 약관 필수 항목에 동의한 것과 같습니다. 그래서 로그인한 유저는 이미 필수 항목에 모두 동의한 상태이므로 굳이 동의 여부를 저장할 필요가 없습니다.
> * 푸시 수신 동의 여부도 Gamebase 서버에 저장되지 않으므로 bAgreed 값은 항상 false로 반환됩니다.
>     * 유저의 푸시 수신 동의 여부는 Gamebase.Push.QueryPush API를 통해 확인하시기 바랍니다.
> * 콘솔에서 '기본 약관 설정'을 하지 않는 경우 약관 언어와 다른 국가 코드로 설정된 단말기에서 queryTerms API를 호출하면 `UI_TERMS_NOT_EXIST_FOR_DEVICE_COUNTRY(6922)` 오류가 발생합니다.
>     * 콘솔에서 '기본 약관 설정'을 하거나, `UI_TERMS_NOT_EXIST_FOR_DEVICE_COUNTRY(6922)` 오류가 발생했을 때는 약관을 표시하지 않도록 처리하시기 바랍니다.

#### Required 파라미터
* Callback: API 호출 결과를 사용자에게 콜백으로 알려줍니다. 콜백으로 오는 GamebaseResponse.Terms.QueryTermsResult로 콘솔에 설정된 약관 정보를 얻을 수 있습니다.
 

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void QueryTerms(const FGamebaseQueryTermsResultDelegate& Callback);
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| NOT\_INITIALIZED | 1 | Gamebase가 초기화되어 있지 않습니다. |
| UI\_TERMS\_NOT\_EXIST\_IN\_CONSOLE | 6921 | 약관 정보가 콘솔에 등록되어 있지 않습니다. |
| UI\_TERMS\_NOT\_EXIST\_FOR\_DEVICE\_COUNTRY | 6922 | 단말기 국가코드에 맞는 약관 정보가 콘솔에 등록되어 있지 않습니다. |

**Example**

```cpp
void USample::QueryTerms()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetTerms()->QueryTerms(
        FGamebaseQueryTermsResultDelegate::CreateLambda([](const FGamebaseQueryTermsResult* Data, const FGamebaseError* Error) {
            if (Gamebase::IsSuccess(Error))
            {
                UE_LOG(LogTemp, Display, TEXT("QueryTerms succeeded."));
            }
            else
            {
                UE_LOG(LogTemp, Display, TEXT("QueryTerms failed. (Error: %d)"), Error->Code);
            }
        })
    );
}
```

#### GamebaseResponse.Terms.QueryTermsResult

| Parameter            | Values                          | Description         |
| -------------------- | --------------------------------| ------------------- |
| TermsSeq             | int32                           | 약관 전체 KEY.<br/>updateTerms API 호출 시 필요한 값입니다.          |
| TermsVersion         | FString                         | 약관 버전.<br/>updateTerms API 호출 시 필요한 값입니다.              |
| termsCountryType     | FString                         | 약관 타입.<br/> - KOREAN: 한국 약관 <br/> - GDPR: 유럽 약관 <br/> - ETC: 기타 약관         |
| Contents             | TArray<FGamebaseTermsContent>   | 약관 항목 정보          |


#### GamebaseResponse.Terms.ContentDetail

| Parameter            | Values                | Description         |
| -------------------- | ----------------------| ------------------- |
| TermsContentSeq      | int32                 | 약관 항목 KEY         | 
| Name                 | FString               | 약관 항목 이름         |
| Required             | bool                  | 필수 동의 여부         |
| AgreePush            | FString               | 광고성 푸시 동의 여부<br/> - NONE: 동의 안 함 <br/> - ALL: 전체 동의 <br/> - DAY: 주간 푸시 동의<br/> - NIGHT: 야간 푸시 동의          |
| bAgreed              | bool                  | 해당 약관 항목에 대한 유저 동의 여부           |
| Node1DepthPosition   | int32                 | 1단계 항목 노출 순서           |
| Node2DepthPosition   | int32                 | 2단계 항목 노출 순서<br/> 없을 경우 -1           |
| DetailPageUrl        | FString               | 약관 자세히 보기 URL<br/> 없을 경우 null. |


### UpdateTerms

QueryTerms API로 내려받은 약관 정보로 UI를 직접 제작했다면,
게임유저가 약관에 동의한 내역을 UpdateTerms API를 통해 Gamebase 서버로 전송하시기 바랍니다.

선택 약관 동의를 취소하는 것과 같이, 약관에 동의했던 내역을 변경하는 목적으로도 활용하실 수 있습니다.


> <font color="red">[주의]</font><br/>
>
> 푸시 수신 동의 여부는 Gamebase 서버에 저장되지 않습니다.
> 푸시 수신 동의 여부는 **로그인 후에** Gamebase.Push.RegisterPush API를 호출해서 저장하세요.
>

#### Required 파라미터
* Configuration: 서버에 등록할 유저의 선택 약관 정보입니다.
 
#### Optional 파라미터

* callback : 선택 약관 정보를 서버에 등록 후 사용자에게 콜백으로 알려줍니다.


**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void UpdateTerms(const FGamebaseUpdateTermsConfiguration& Configuration, const FGamebaseErrorDelegate Callback);
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| NOT\_INITIALIZED | 1 | Gamebase가 초기화되어 있지 않습니다. |
| UI\_TERMS\_UNREGISTERED\_SEQ | 6923 | 등록되지 않은 약관 Seq 값을 설정하였습니다. |
| UI\_TERMS\_ALREADY\_IN\_PROGRESS\_ERROR | 6924 | Terms API 호출이 아직 완료되지 않았습니다.<br/>잠시 후 다시 시도하세요. |


**Example**

```cpp
void USample::UpdateTerms(int32 TermsSeq, const FString& TermsVersion, int32 TermsContentSeq, bool bAgreed)
{
    TArray<FGamebaseTermsContent> Contents;
    Contents.Add(FGamebaseTermsContent { TermsContentSeq, bAgreed });
    
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetTerms()->UpdateTerms(
        FGamebaseUpdateTermsConfiguration { TermsSeq, TermsVersion, Contents },
        FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error) {
            if (Gamebase::IsSuccess(Error))
            {
                UE_LOG(LogTemp, Display, TEXT("UpdateTerms succeeded."));
            }
            else
            {
                UE_LOG(LogTemp, Display, TEXT("UpdateTerms failed. (Error: %d)"), Error->Code);
            }
        })
    );
}
```

#### GamebaseRequest.Terms.UpdateTermsConfiguration

| Parameter            | Mandatory(M) / Optional(O) | Values                    | Description         |
| -------------------- | -------------------------- | ------------------------- | ------------------- |
| TermsVersion         | **M**                      | FString                    | 약관 버전.<br/>queryTerms API를 호출해 내려받은 값을 전달해야 합니다.   |
| TermsSeq             | **M**                      | int32                       | 약관 전체 KEY.<br/>queryTerms API를 호출해 내려받은 값을 전달해야 합니다.             |
| Contents             | **M**                      | List< Content > | 선택 약관 유저 동의 정보  |

#### GamebaseRequest.Terms.Content

| Parameter            | Mandatory(M) / Optional(O) | Values             | Description         |
| -------------------- | -------------------------- | ------------------ | ------------------- |
| TermsContentSeq      | **M**                      | int32                | 선택 약관 항목 KEY      |
| bAgreed               | **M**                      | bool               | 선택 약관 항목 동의 여부  |

### IsShowingTermsView

현재 약관 창이 화면에 표시되고 있는지 여부를 알 수 있습니다.

**API**

```cpp
bool IsShowingTermsView();
```

**Example**

```cpp
void USample::IsShowingTermsView()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    bool isShowingTermsView = Subsystem->GetTerms()->IsShowingTermsView();
    UE_LOG(LogTemp, Display, TEXT("IsShowingTermsView : %s"), isShowingTermsView ? TEXT("true") : TEXT("false"));
}
```
