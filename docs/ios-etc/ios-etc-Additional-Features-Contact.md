---
source: ios-etc.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, Login, WebView, Contact, Error, isSuccessWithError, requestContactURLWithCompletion, additionalURL, additionalParameters, requestContactURLWithConfiguration"
section: "Additional Features > Contact"
order: 7
---

### Contact

Gamebase에서는 고객 문의 대응을 위한 기능을 제공합니다.

> [TIP]
>
> NHN Cloud Contact 서비스와 연동해서 사용하면 보다 쉽고 편리하게 고객 문의에 대응할 수 있습니다.
> 자세한 NHN Cloud Contact 서비스 이용법은 아래 가이드를 참고하시기 바랍니다.
> [NHN Cloud Online Contact Guide](https://docs.nhncloud.com/ko/Contact%20Center/ko/online-contact-overview/)
>

> <font color="red">[주의]</font><br/>
>
> 고객 센터 문의 시 파일 첨부를 위해 카메라 또는 앨범 접근이 필요할 수 있습니다.
> info.plist에 'Privacy - Camera Usage Description', 'Privacy — Microphone Usage Description'을 설정하십시오.

#### Customer Service Type

**Gamebase 콘솔 > App > Customer service**에서는 아래와 같이 3가지 유형의 고객 센터를 선택할 수 있습니다.
![](./image/etc_customer_center_001_2.16.0.png)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Gamebase 콘솔의 고객 센터(Customer service) 유형 선택 화면
    구성: Customer service 설정 화면에서 Type 드롭다운 메뉴를 통해 Developer customer center, Gamebase customer center, NHN Cloud Online Contact 중 하나를 선택할 수 있는 UI와 Customer service URL 입력 필드가 표시됨
    Keyword: 고객센터, Customer service, 콘솔, 설정, Gamebase
-->

| Customer Service Type     | Required Login |
| ------------------------- | -------------- |
| Developer customer center | X              |
| Gamebase customer center  | △              |
| NHN Cloud Online Contact      | △              |

각 유형에 따라 Gamebase SDK의 고객 센터 API는 다음 URL을 사용합니다.

* 개발사 자체 고객 센터(Developer customer center)
    * **고객 센터 URL**에 입력한 URL.
* Gamebase 제공 고객 센터(Gamebase customer center)
    * 로그인 전: 유저 정보가 **없는** 고객 센터 URL.
    * 로그인 후: 유저 정보가 포함된 고객 센터 URL.
* NHN Cloud 조직 상품(Online Contact)
    * 로그인 전: 유저 정보가 **없는** 고객 센터 URL.
    * 로그인 후: 유저 정보가 포함된 고객 센터 URL.

#### Open Contact WebView

Gamebase 콘솔에 입력한 **고객 센터 URL** 웹뷰를 나타낼 수 있는 기능입니다.
TCGBContactConfiguration으로 URL에 추가 정보를 전달할 수 있습니다.


**TCGBContactConfiguration**

| Parameter     | Mandatory(M) /<br/>Optional(O) | Values            | Description        |
| ------------- | ------------- | ---------------------------------- | ------------------ |
| userName      | O             | string                             | 사용자 이름(닉네임)<br>**default**: nil    |
| additionalURL | O             | string                             | 개발사 자체 고객 센터 URL 뒤에 붙는 추가적인 URL<br>고객 센터 타입이 `CUSTOM` 인 경우에만 사용<br>**default**: nil    |
| additionalParameters | O      | dictionary&lt;string, string&gt;         | 고객 센터 URL 뒤에 붙는 추가적인 파라미터<br>**default**: nil    |
| extraData     | O             | dictionary&lt;string, string&gt;         | 개발사가 원하는 extra data를 고객 센터 오픈 시에 전달<br>**default**: nil    |


**API**

```objectivec
+ (void)openContactWithViewController:(UIViewController *)viewController 
                           completion:(void(^)(TCGBError *error))completion;

+ (void)openContactWithViewController:(UIViewController *)viewController
                        configuration:(TCGBContactConfiguration *)configuration
                           completion:(void(^)(TCGBError *error))completion;
```

**Error Code**

| Error                           | Error Code | Description                 |
| ------------------------------- | ---------- | --------------------------- |
| TCGB\_ERROR\_NOT\_INITIALIZED | 1       | Gamebase가 초기화되어 있지 않습니다. |
| TCGB\_ERROR\_UI\_CONTACT\_FAIL\_INVALID\_URL | 6911       | 고객 센터 URL이 존재하지 않습니다.<br>Gamebase 콘솔의 **고객 센터 URL**을 확인하세요. |
| TCGB\_ERROR\_UI\_CONTACT\_FAIL\_ISSUE\_SHORT\_TERM\_TICKET | 6912       | 사용자 식별을 위한 임시 티켓 발급에 실패하였습니다. |

**Example**

```objectivec
[TCGBContact openContactWithViewController:self completion:^(TCGBError *error) {
    if ([TCGBGamebase isSuccessWithError:error] == YES) {
        // A user close the contact web view.
    } else if (error.code == TCGB_ERROR_UI_CONTACT_FAIL_INVALID_URL) {
        // TODO: Gamebase Console Service Center URL is invalid.
        // Please check the url field in the TOAST Gamebase Console.
    } else {
        // TODO: Error occur when opening the contact web view.
    }
}];
```

#### Request Contact URL

고객 센터 웹뷰를 표시하는 데 사용되는 URL을 얻을 수 있습니다.

**API**

```objectivec
+ (void)requestContactURLWithCompletion:(void(^)(NSString *contactUrl, TCGBError *error))completion;

+ (void)requestContactURLWithConfiguration:(TCGBContactConfiguration *)configuration
                                completion:(void(^)(NSString *contactUrl, TCGBError *error))completion;
```

**Error Code**

| Error                           | Error Code | Description                 |
| ------------------------------- | ---------- | --------------------------- |
| TCGB\_ERROR\_NOT\_INITIALIZED | 1       | Gamebase가 초기화되어 있지 않습니다. |
| TCGB\_ERROR\_UI\_CONTACT\_FAIL\_INVALID\_URL | 6911       | 고객 센터 URL이 존재하지 않습니다.<br>Gamebase 콘솔의 **고객 센터 URL**을 확인하세요. |
| TCGB\_ERROR\_UI\_CONTACT\_FAIL\_ISSUE\_SHORT\_TERM\_TICKET | 6912       | 사용자 식별을 위한 임시 티켓 발급에 실패하였습니다. |

**Example**

```objectivec
[TCGBContact requestContactURLWithCompletion^(NSString *contactUrl, TCGBError *error){
    if ([TCGBGamebase isSuccessWithError:error] == YES) {
        NSLog(@"ContactURL: %@", contactUrl);
    } else if (error.code == TCGB_ERROR_UI_CONTACT_FAIL_INVALID_URL) {
        // TODO: Gamebase Console Service Center URL is invalid.
        // Please check the url field in the TOAST Gamebase Console.
    } else {
        // TODO: Error occur when request contact url.
    }
}];
```
