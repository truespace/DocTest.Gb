---
source: unity-etc.md
split: true
created_date_time: 20260406_141859
keyword: Contact
section: "Additional Features > Contact"
order: 6
---

### Contact

Gamebase 는 고객 문의 대응을 위한 기능을 제공합니다.

> [TIP]
>
> NHN Cloud Contact 서비스와 연동해서 사용하면 보다 쉽고 편리하게 고객 문의에 대응할 수 있습니다.
> 자세한 NHN Cloud Contact 서비스 이용법은 아래 가이드를 참고하시기 바랍니다.
> [NHN Cloud Online Contact Guide](https://docs.nhncloud.com/ko/Contact%20Center/ko/online-contact-overview/)

#### 권한 설정

* [Game > Gamebase > Android SDK 사용 가이드 > ETC > Contact](aos-etc/#contact)
* [Game > Gamebase > iOS SDK 사용 가이드 > ETC > Contact](ios-etc/#contact)


#### Customer Service Type

**Gamebase 콘솔 > App > Customer service**에서 아래와 같이 3가지 유형의 고객 센터를 선택할 수 있습니다.
![](./image/etc_customer_center_001_2.16.0.png)
<!-- LLM_Image_DESC_20260406
    유형: UI
    내용: Gamebase 콘솔의 Customer Service 유형 선택 화면
    구성: Customer service 설정 화면에서 Type 드롭다운 메뉴가 열려 있으며, Developer customer center, Gamebase customer center(선택됨), NHN Cloud Online Contact 3가지 옵션이 표시됨. 하단에 Customer service URL 입력 필드가 있음
    Keyword: Customer Service, 고객센터, Gamebase 콘솔, 유형 선택, Online Contact
-->

| Customer Service Type     | Required Login |
| ------------------------- | -------------- |
| Developer customer center | X              |
| Gamebase customer center  | △             |
| NHN Cloud Online Contact      | △              |

각 유형에 따라 Gamebase SDK 의 고객 센터 API 는 다음 URL 을 사용합니다.

* 개발사 자체 고객 센터(Developer customer center)
    * **고객 센터 URL** 에 입력한 URL.
* Gamebase 제공 고객 센터(Gamebase customer center)
    * 로그인 전 : 유저 정보가 **없는** 고객 센터 URL.
    * 로그인 후 : 유저 정보가 포함된 고객 센터 URL.
* NHN Cloud 조직 상품(Online Contact)
    * 로그인 전 : 유저 정보가 **없는** 고객 센터 URL.
    * 로그인 후 : 유저 정보가 포함된 고객 센터 URL.

#### Open Contact WebView

고객 센터 웹뷰를 표시합니다.
URL은 고객 센터 유형에 따라 결정됩니다.
ContactConfiguration으로 URL에 추가 정보를 전달할 수 있습니다.

**GamebaseRequest.Contact.Configuration**

| Parameter     | Mandatory(M) /<br/>Optional(O) | Values            | Description        |
| ------------- | ------------- | ---------------------------------- | ------------------ |
| userName      | O             | string                             | 사용자 이름(닉네임)<br>**default**: null    |
| additionalURL | O             | string                             | 개발사 자체 고객 센터 URL 뒤에 붙는 추가적인 URL<br>**default**: null    |
| additionalParameters | O      | Dictionary<string, string>         | 고객 센터 URL 뒤에 붙는 추가적인 파라미터<br>**default**: null    |
| extraData     | O             | Dictionary<string, string>         | 개발사가 원하는 extra data를 고객 센터 오픈 시에 전달<br>**default**: null    |

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE

```cs
static void OpenContact(GamebaseCallback.ErrorDelegate callback);
static void OpenContact(GamebaseRequest.Contact.Configuration configuration, GamebaseCallback.ErrorDelegate callback);
```

**ErrorCode**

| Error Code | Description |
| --- | --- |
| NOT\_INITIALIZED(1)                                 | Gamebase.initialize가 호출되지 않았습니다. |
| UI\_CONTACT\_FAIL\_INVALID\_URL(6911)               | 고객 센터 URL 이 존재하지 않습니다.<br>Gamebase 콘솔의 **고객 센터 URL** 을 확인하세요. |
| UI\_CONTACT\_FAIL\_ISSUE\_SHORT\_TERM\_TICKET(6912) | 사용자 식별을 위한 임시 티켓 발급에 실패하였습니다. |
| UI\_CONTACT\_FAIL\_ANDROID\_DUPLICATED\_VIEW(6913)  | 고객 센터 웹뷰가 이미 표시중입니다. |

**Example**

``` cs
public void SampleOpenContact()
{
    Gamebase.Contact.OpenContact((error) =>
    {
        if (Gamebase.IsSuccess(error) == true)
        {
            // A user close the contact web view.
        }
        else if (error.code == GamebaseErrorCode.UI_CONTACT_FAIL_INVALID_URL)  // 6911
        {
            // TODO: Gamebase Console Service Center URL is invalid.
            // Please check the url field in the TOAST Gamebase Console.
        } 
        else if (error.code == GamebaseErrorCode.UI_CONTACT_FAIL_ANDROID_DUPLICATED_VIEW) // 6913
        { 
            // The customer center web view is already opened.
        } 
        else 
        {
            // An error occur when opening the contact web view.
        }
    });
}
```

#### Request Contact URL

고객 센터 웹뷰를 표시하는 데 사용되는 URL을 반환합니다.

**API**

```cs
static void RequestContactURL(GamebaseCallback.GamebaseDelegate<string> callback);
static void RequestContactURL(GamebaseRequest.Contact.Configuration configuration, GamebaseCallback.GamebaseDelegate<string> callback);
```

**ErrorCode**

| Error Code | Description |
| --- | --- |
| NOT\_INITIALIZED(1)                                 | Gamebase.initialize가 호출되지 않았습니다. |
| UI\_CONTACT\_FAIL\_INVALID\_URL(6911)               | 고객 센터 URL 이 존재하지 않습니다.<br>Gamebase 콘솔의 **고객 센터 URL** 을 확인하세요. |
| UI\_CONTACT\_FAIL\_ISSUE\_SHORT\_TERM\_TICKET(6912) | 사용자를 식별을 위한 임시 티켓 발급에 실패하였습니다. |

**Example**

``` cs
public void SampleRequestContactURL()
{
    var configuration = new GamebaseRequest.Contact.Configuration()
                            {
                                userName = "User Name"
                            };

    Gamebase.Contact.RequestContactURL(configuration, (url, error) => 
    {
        if (Gamebase.IsSuccess(error) == true) 
        {
            // Open webview with 'contactUrl'
        } 
        else if (error.code == GamebaseErrorCode.UI_CONTACT_FAIL_INVALID_URL) // 6911
        { 
            // TODO: Gamebase Console Service Center URL is invalid.
            // Please check the url field in the TOAST Gamebase Console.
        } 
        else 
        {
            // An error occur when requesting the contact web view url.
        }
    });
}
```
