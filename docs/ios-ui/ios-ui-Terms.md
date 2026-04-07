---
source: ios-ui.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, Login, TermsView, Error, isShowingTermsView, showTermsView, queryTermsResult, showTermsViewResult, isTermsUIOpened, registerPushWithConfiguration"
section: Terms
order: 3
---

## Terms

Gamebase 콘솔에 설정한 약관을 표시합니다.

![TermsView Example](./image/termsView-guide-ui-001_2.20.0.png)
<!-- LLM_Image_DESC_20260406
    유형: UI
    내용: 약관 동의 화면 예시
    구성: 모바일 앱 화면에 약관 동의 팝업이 표시됨. 이용약관 및 개인정보 관련 동의, 게임 이용약관, 게임 정보 수집/이용, 광고성 알림 수신(선택), 광고성 야간 알림 수신(선택) 항목이 체크박스와 보기 링크로 나열되며, 하단에 빨간 확인 버튼이 위치
    Keyword: 약관, Terms, 동의, UI, 개인정보, 광고
-->

showTermsView API 는 웹뷰로 약관 창을 표시해줍니다.
Game 의 UI 에 맞는 약관 창을 직접 제작하고자 하는 경우에는 queryTerms API를 호출하여, Gamebase 콘솔에 설정한 약관 항목을 불러올 수 있습니다.
유저가 약관에 동의했다면 각 항목별 동의 여부를 updateTerms API를 통해 Gamebase 서버로 전송하시기 바랍니다.

### showTermsView

약관 창을 화면에 띄워 줍니다.
유저가 약관에 동의를 했을 경우, 동의 여부를 서버에 등록합니다.
약관에 동의했다면 showTermsView API를 다시 호출해도 약관 창이 표시되지 않고 바로 성공 콜백이 반환됩니다.
단, Gamebase 콘솔에서 약관 재동의 항목을 **필요** 로 변경했다면 유저가 다시 약관에 동의할 때까지는 약관 창이 표시됩니다.

> <font color="red">[주의]</font><br/>
>
> * 약관에 푸시 수신 동의 여부를 추가했다면, TCGBDataContainer 로부터 TCGBPushConfiguration 을 생성할 수 있습니다.
> * PushConfiguration 은 약관 창이 표시되지 않은 경우에는 nil입니다.(약관 창이 표시되었다면 항상 유효한 객체가 반환됩니다.) 
> * PushConfiguration.pushEnabled 값은 항상 true입니다. 
> * TCGBPushConfiguration 이 nil 이 아니라면 **로그인 후에** [TCGBPush registerPushWithConfiguration:completion:] API를 호출하세요.
>

#### Required 파라미터
* viewController: 약관 창이 노출되는 ViewController입니다.
 
#### Optional 파라미터
* configuration: TCGBTermsConfiguration으로 약관 창 강제 표시 여부 등 설정을 변경할 수 있습니다.
* completion: 약관 동의 후 약관 창이 종료될 때 사용자에게 콜백으로 알려줍니다. 콜백으로 오는 TCGBDataContainer 객체는 TCGBPushConfiguration으로 변환해서 로그인 후 registerPush API 에 사용할 수 있습니다.


**API**

```objectivec
+ (void)showTermsViewWithViewController:(UIViewController *)viewController
                             completion:(nullable void (^)(TCGBDataContainer * _Nullable dataContainer, TCGBError * _Nullable error))completion;
                             
+ (void)showTermsViewWithConfiguration:(TCGBTermsConfiguration *)configuration
                        viewController:(nullable UIViewController *)viewController
                            completion:(nullable void (^)(TCGBDataContainer * _Nullable dataContainer, TCGBError * _Nullable error))completion;
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| TCGB\_ERROR\_NOT\_INITIALIZED | 1 | Gamebase가 초기화되어 있지 않습니다. |
| TCGB\_ERROR\_LAUNCHING\_SERVER\_ERROR | 2001 | 론칭 서버에서 전달받은 항목에 약관 관련 내용이 없는 경우에 발생하는 에러입니다.<br/>정상적인 상황이 아니므로 Gamebase 담당자에게 문의해주시기 바랍니다. |
| TCGB\_ERROR\_UI\_TERMS\_ALREADY\_IN\_PROGRESS\_ERROR | 6924 | Terms API 호출이 아직 완료되지 않았습니다.<br/>잠시 후 다시 시도하세요. |
| TCGB\_ERROR\_WEBVIEW\_TIMEOUT | 7002 | 약관 웹뷰 표시 중 타임아웃이 발생했습니다. |
| TCGB\_ERROR\_WEBVIEW\_HTTP\_ERROR | 7003 | 약관 웹뷰 오픈 중 HTTP 에러가 발생하였습니다. |

**Example**

```objectivec
- (void)showTermsView {
    void(^completion)(TCGBDataContainer *, TCGBError *) = ^(TCGBDataContainer *dataContainer, TCGBError *error) {
        // Called when the entire termsView is closed.
        NSLog(@"TermsView closed");

        TCGBShowTermsViewResult *showTermsViewResult = [TCGBShowTermsViewResult fromDataContainer:dataContainer];

        // If the TCGBPushConfiguration is not null, 
        // save TCGBPushConfiguration and use it for registerPush after login.
        TCGBPushConfiguration *savedPushConfiguration = showTermsViewResult.pushConfiguration;

        // Wheter the TermsUI was displayed.
        BOOL isTermsUIOpened = showTermsViewResult.isTermsUIOpened;
    };

    [TCGBTerms showTermsViewWithViewController:self completion:completion];
}

- (void)afterLogin {
    // Call registerPush with saved TCGBPushConfiguration.
    if (savedPushConfiguration != nil) {
        [TCGBPush registerPushWithPushConfiguration:savedPushConfiguration completion:^(TCGBError* error) {
            ...
        }];
    }
}
```

**TCGBTermsConfiguration**

| Parameter            | Values                          | Description         |
| -------------------- | --------------------------------| ------------------- |
| forceShow            | BOOL                            | 약관에 동의한 이후에도 약관 창을 강제로 표시합니다.<br/>**default**: NO          |

**TCGBShowTermsViewResult**

| Parameter            | Values                          | Description         |
| -------------------- | --------------------------------| ------------------- |
| isTermsUIOpened            | BOOL                            | 약관 창이 화면에 표시되었는지 여부를 나타냅니다.          |
| TCGBPushConfiguration      | TCGBPushConfiguration           | 약관에 푸시 수신 동의 여부를 추가한 경우, 푸시 수신 동의 여부에 대한 정보를 가지고 있습니다.    |

### queryTerms

Gamebase는 단순한 형태의 웹뷰로 약관을 표시합니다.
게임UI에 맞는 약관을 직접 제작하고자 하신다면, queryTerms API를 호출하여 Gamebase 콘솔에 설정한 약관 정보를 내려받아 활용하실 수 있습니다.

'선택' 약관 항목은 로그인 후에 호출하면 동의 여부도 함께 알 수 있습니다. 단, '필수' 항목의 동의 여부는 항상 false로 반환됩니다.

> <font color="red">[주의]</font><br/>
>
> * TCGBTermsContentDetail.required가 true인 필수 항목은 동의 여부를 Gamebase 서버에 저장하지 않으므로 agreed 값은 항상 false로 반환됩니다.
>     * 약관 필수 항목에 동의하지 않은 경우 게임 진행 또는 게임 로그인이 불가능하므로 약관 팝업이 닫혀 있고 로그인되어 있는 상태라면 자연스럽게 약관 필수 항목에 동의한 것과 같습니다. 그래서 로그인한 유저는 이미 필수 항목에 모두 동의한 상태이므로 굳이 동의 여부를 저장할 필요가 없습니다.
> * 푸시 수신 동의 여부도 Gamebase 서버에 저장되지 않으므로 agreed 값은 항상 false로 반환됩니다.
>     * 유저의 푸시 수신 동의 여부는 [TCGBPush queryTokenInfoWithCompletion:] API를 통해 확인하시기 바랍니다.
> * 콘솔에서 '기본 약관 설정'을 하지 않는 경우 약관 언어와 다른 국가 코드로 설정된 단말기에서 queryTerms API를 호출하면 **TCGB_ERROR_UI_TERMS_NOT_EXIST_FOR_DEVICE_COUNTRY(6922)** 오류가 발생합니다.
>     * 콘솔에서 '기본 약관 설정' 을 하거나, **TCGB_ERROR_UI_TERMS_NOT_EXIST_FOR_DEVICE_COUNTRY(6922)** 에러가 발생했을때는 약관을 표시하지 않도록 처리하시기 바랍니다.

#### Required 파라미터
* viewController: 최상위 ViewController입니다.
* completion: API 호출 결과를 사용자에게 콜백으로 알려줍니다. 콜백으로 오는 TCGBQueryTermsResult으로 콘솔에 설정된 약관 정보를 얻을 수 있습니다.
 

**API**

```objectivec
+ (void)queryTermsWithViewController:(UIViewController *)viewController
                          completion:(void (^)(TCGBQueryTermsResult * _Nullable queryTermsResult, TCGBError * _Nullable error))completion;
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| TCGB\_ERROR\_NOT\_INITIALIZED | 1 | Gamebase가 초기화되어 있지 않습니다. |
| TCGB\_ERROR\_UI\_TERMS\_NOT\_EXIST\_IN\_CONSOLE | 6921 | 약관 정보가 콘솔에 등록되어 있지 않습니다. |
| TCGB\_ERROR\_UI\_TERMS\_NOT\_EXIST\_FOR\_DEVICE\_COUNTRY | 6922 | 단말기 국가코드에 맞는 약관 정보가 콘솔에 등록되어 있지 않습니다. |

**Example**

```objectivec
- (void)queryTerms {
    void(^completion)(TCGBQueryTermsResult *, TCGBError *) = ^(TCGBQueryTermsResult *queryTermsResult, TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == YES) {
            int termsSeq = queryTermsResult.termsSeq;
            NSString *termsVersion = queryTermsResult.termsVersion;
            ...    
        } else if (error.code == TCGB_ERROR_UI_TERMS_NOT_EXIST_FOR_DEVICE_COUNTRY) {
            // Another country device.
            // Pass the 'terms and contidions' step
        } else {
            // QueryTerms API Failed.
        }
    };

    [TCGBTerms queryTermsWithViewController:self completion:completion];
}
```

#### TCGBQueryTermsResult

| Parameter            | Values                          | Description         |
| -------------------- | --------------------------------| ------------------- |
| termsSeq             | int                             | 약관 전체 KEY.<br/>updateTerms API 호출 시 필요한 값입니다.          |
| termsVersion         | String                          | 약관 버전.<br/>updateTerms API 호출 시 필요한 값입니다.              |
| termsCountryType     | String                          | 약관 타입.<br/> - KOREAN: 한국 약관 <br/> - GDPR: 유럽 약관 <br/> - ETC: 기타 약관         |
| contents             | Array< TCGBTermsContentDetail > | 약관 항목 정보          |


#### TCGBTermsContentDetail

| Parameter            | Values                | Description         |
| -------------------- | ----------------------| ------------------- |
| termsContentSeq      | int                   | 약관 항목 KEY         | 
| name                 | String                | 약관 항목 이름         |
| required             | BOOL                  | 필수 동의 여부         |
| agreePush            | String                | 광고성 푸시 동의 여부.<br/> - NONE: 동의 안함 <br/> - ALL: 전체 동의 <br/> - DAY: 주간 푸시 동의<br/> - NIGHT: 야간 푸시 동의          |
| agreed               | BOOL                  | 해당 약관 항목에 대한 유저 동의 여부           |
| node1DepthPosition   | int                   | 1단계 항목 노출 순서           |
| node2DepthPosition   | int                   | 2단계 항목 노출 순서<br/> 없을 경우 -1           |
| detailPageUrl        | String                | 약관 자세히 보기 URL<br/> 설정되어 있지 않으면 필드 없음           |


### updateTerms

queryTerms API 로 내려받은 약관 정보로 UI 를 직접 제작했다면,
게임유저가 약관에 동의한 내역을 updateTerms API를 통해 Gamebase 서버로 전송하시기 바랍니다.

선택 약관 동의를 취소하는 것과 같이, 약관에 동의했던 내역을 변경하는 목적으로도 활용하실 수 있습니다.


> <font color="red">[주의]</font><br/>
>
> 푸시 수신 동의 여부는 Gamebase 서버에 저장되지 않습니다.
> 푸시 수신 동의 여부는 **로그인 후에** [TCGBPush registerPushWithConfiguration:completion:] API를 호출해서 저장하세요.
>

#### Required 파라미터
* viewController: 최상위 ViewController입니다.
* configuration: 서버에 등록할 유저의 선택 약관 정보입니다.
 
#### Optional 파라미터

* completion: 선택 약관 정보를 서버에 등록 후 사용자에게 콜백으로 알려줍니다.


**API**

```objectivec
+ (void)updateTermsWithViewController:(UIViewController *)viewController
                        configuration:(TCGBUpdateTermsConfiguration *)configuration
                           completion:(nullable void (^)(TCGBError * _Nullable error))completion;
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| TCGB\_ERROR\_NOT\_INITIALIZED | 1 |Gamebase가 초기화되어 있지 않습니다. |
| TCGB\_ERROR\_UI\_TERMS\_UNREGISTERED\_SEQ | 6923 | 등록되지 않은 약관 Seq 값을 설정하였습니다. |
| TCGB\_ERROR\_UI\_TERMS\_ALREADY\_IN\_PROGRESS\_ERROR | 6924 | Terms API 호출이 아직 완료되지 않았습니다.<br/>잠시 후 다시 시도하세요. |


**Example**

```objectivec
- (void)updateTerms {
    void(^completion)(TCGBError *) = ^(TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == NO) {
            // UpdateTerms API Failed.
        }
    };

    TCGBTermsContent *termsContent = [TCGBTermsContent termsContentWithTermsContentSeq:12 agreed:YES];

    NSMutableArray *contents = [NSMutableArray array];
    [contents addObject:termsContent];

    TCGBUpdateTermsConfiguration *configuration = [TCGBUpdateTermsConfiguration configurationWithTermsVersion:@"1.2.3" termsSeq:1 contents:contents];

    [TCGBTerms updateTermsWithViewController:self configuration:configuration completion:completion];
}
```


#### TCGBUpdateTermsConfiguration

| Parameter            | Mandatory(M) / Optional(O) | Values                    | Description         |
| -------------------- | -------------------------- | ------------------------- | ------------------- |
| termsVersion         | **M**                      | String                    | 약관 버전.<br/>queryTerms API를 호출해 내려받은 값을 전달해야 합니다.   |
| termsSeq             | **M**                      | int                       | 약관 전체 KEY.<br/>queryTerms API를 호출해 내려받은 값을 전달해야 합니다.             |
| contents             | **M**                      | Array< TCGBTermsContent > | 선택 약관 유저 동의 정보  |

#### TCGBTermsContent

| Parameter            | Mandatory(M) / Optional(O) | Values             | Description         |
| -------------------- | -------------------------- | ------------------ | ------------------- |
| termsContentSeq      | **M**                      | int                | 선택 약관 항목 KEY      |
| agreed               | **M**                      | BOOL               | 선택 약관 항목 동의 여부  |

### isShowingTermsView

현재 약관 창이 화면에 표시되고 있는지를 알 수 있습니다.

**API**

```objectivec
+ (void)isShowingTermsView;
```
**Example**

```objectivec
- (void)isShowingTermsView {
    BOOL isShowingTermsView = [TCGBTerms isShowingTermsView];   // YES or NO
}
```
