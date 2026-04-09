---
source: aos-etc.md
section: "Additional Features > Country Code"
order: 3
split: true
created_date_time: 20260408_184906
keyword: Android, Aos, Etc
---

### Country Code

* Gamebase는 System의 Country Code를 다음과 같은 API로 제공하고 있습니다.
* 각 API 마다 특징이 있으니 쓰임새에 맞는 API를 선택하시기 바랍니다.

#### USIM Country Code

* USIM에 기록된 국가코드를 반환합니다.
* USIM에 잘못된 국가코드가 기록되어 있다 하더라도 추가적인 체크 없이 그대로 반환합니다.
* 값이 비어있는 경우 'ZZ'를 반환합니다.

**API**

```java
+ (String)Gamebase.getCountryCodeOfUSIM()
```

#### Device Country Code

* OS로부터 전달받은 단말기 국가코드를 추가적인 체크 없이 그대로 반환합니다.
* 단말기 국가코드는 '언어' 설정에 따라 OS가 자동으로 결정합니다.
* 여러개의 언어가 등록된 경우, 우선권이 가장 높은 언어로 국가코드를 결정합니다.
* 값이 비어있는 경우 'ZZ'를 반환합니다.

**API**

```java
+ (String)Gamebase.getCountryCodeOfDevice()
```

#### Intergrated Country Code

* USIM, 단말기 언어 설정의 순서로 국가 코드를 확인하여 반환합니다.
* getCountryCode API는 다음 순서로 동작합니다.
	1. USIM에 기록된 국가 코드를 확인해 보고 값이 존재한다면 추가적인 체크 없이 그대로 반환합니다.
	2. USIM 국가 코드가 빈 값이라면 단말기 국가 코드를 확인해 보고 값이 존재한다면 추가적인 체크 없이 그대로 반환합니다.
	3. USIM, 단말기 국가 코드가 모두 빈 값이라면 'ZZ'를 반환합니다.

![observer](./image/get_country_code_001_1.14.0.png)
<!-- LLM_Image_DESC_20260408_185735
    유형: Screenshot
    내용: Intergrated Country Code 관련 화면
    구성: Intergrated Country Code 관련 스크린샷
    Keyword: Android, Screenshot, Intergrated Country Code
-->

**API**

```java
+ (String)Gamebase.getCountryCode()
```
