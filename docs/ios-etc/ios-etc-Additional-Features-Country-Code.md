---
source: ios-etc.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, Country Code"
section: "Additional Features > Country Code"
order: 4
---

### Country Code

* Gamebase는 System의 Country Code를 다음 API로 제공하고 있습니다.

#### Device Country Code

* OS로부터 전달받은 단말기 지역 설정을 추가적인 체크 없이 그대로 반환합니다.
* 단말기 국가코드는 '설정 > 일반 > 언어 및 지역 > 지역' 설정에 따라 OS가 결정합니다.
* iOS에서 제공하는 NSLocaleCountryCode를 사용하여 획득한 값을 반환합니다.

**API**

```objectivec
+ (NSString *)deviceCountryCode;
```
