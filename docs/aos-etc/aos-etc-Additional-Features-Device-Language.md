---
source: aos-etc.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Additional, getDeviceLanguageCode"
section: "Additional Features > Device Language"
order: 1
---

## Game > Gamebase > Android SDK 사용 가이드 > ETC

## Additional Features

Gamebase에서 지원하는 부가 기능을 설명합니다.

### Device Language

* 단말기에 설정된 언어 코드를 반환합니다.
* 여러개의 언어가 등록된 경우, 우선권이 가장 높은 언어만을 반환합니다.

**API**

```java
+ (String)Gamebase.getDeviceLanguageCode();
```
