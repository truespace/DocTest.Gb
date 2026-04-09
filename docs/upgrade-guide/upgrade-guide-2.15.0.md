---
source: upgrade-guide.md
section: "2.15.0"
order: 55
split: true
created_date_time: 20260408_184906
keyword: Purchase, Error, Android, Upgrade Guide, 2.15.0
---

## 2.15.0

### Android

#### Purchase Google

* **gamebase-adapter-purchase-google** 을 사용한다면 Gamebase SDK 2.15.0 미만 버전에서 2.15.0 이상으로 업그레이드 하는 경우 반드시 **이전 버전의 Game Client Version 을 업데이트 필수** 로 설정해야 합니다.
    * Google Billing Client 모듈이 업데이트되어, 여러개의 단말기에서 서로 다른 Billing Client 버전이 적용된 상태에서 아이템을 구매하는 경우 오류가 발생했을때 재처리에 문제가 생길 수 있기 때문입니다.
