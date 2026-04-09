---
source: upgrade-guide.md
section: "2.56.0"
order: 24
split: true
created_date_time: 20260408_184906
keyword: Unreal, Upgrade Guide, 2.56.0
---

## 2.56.0

### Unreal
 
* 제공되는 타입이 USTRUCT에서 일반 구조체로 변경되었습니다.
    * 결과로 받는 타입은 기본적으로 제공되지 않는 값인 경우 TOptional 형태로 제공됩니다. 기존에 사용하던 값인 경우 Value.IsSet()를 이용해 설정된 값인지 확인한 뒤 Value.GetValue()를 통해 값을 사용할 수 있습니다.
