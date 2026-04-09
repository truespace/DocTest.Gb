---
source: ios-etc.md
section: "Additional Features > IDFA"
order: 1
split: true
created_date_time: 20260408_184906
keyword: iOS, Ios, Etc
---

## Game > Gamebase > iOS SDK 사용 가이드 > ETC

## Additional Features
Gamebase에서 지원하는 부가적인 기능을 설명합니다.

### IDFA

* 단말기의 광고식별자 값을 반환합니다.

**API**

```objectivec
+ (NSString *)idfa;
```

> <font color="red">[주의]</font><br/>
>
> iOS 14 이상부터 IDFA 값 요청 시, 사용자 권한을 받아야합니다.
> 사용자 권한 요청할 때 노출시킬 문구를 info.plist에 설정을 해야 합니다.
> info.plist에 'Privacy - Tracking Usage Description'을 설정하십시오.
