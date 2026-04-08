---
source: release-notes-unity.md
section: "2.15.0 (2020.08.25)"
order: 81
split: true
created_date_time: 20260408_191848
keyword: Unity, Purchase, Push, Alert, Android, iOS, Release Notes, 2.15.0
---

### 2.15.0 (2020.08.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.15.0/GamebaseSDK-Unity.zip)

```
Gamebase SDK 2.15.0 버전에서 Google Billing Client 모듈이 업데이트 되었습니다.

'gamebase-adapter-purchase-google'을 사용한다면 Gamebase SDK 2.15.0 미만 버전에서 2.15.0 이상으로 업그레이드하는 경우 
반드시 이전 버전의 'Game Client Version'을 '업데이트 필수'로 설정해야 합니다.

아이템을 구매하다 오류가 발생하면 재처리를 수행하게 되는데 
여러 개의 단말기에서 서로 다른 Billing Client 버전이 적용된 상태에서는 재처리 수행 중에 문제가 생길 수 있기 때문입니다.
```

#### 기능 추가
* [SDK] 2.15.0
    * (공통) 푸시 토큰 등록시 NotificationOption 설정으로 앱이 포그라운드(foreground) 상태에서도 푸시 알림을 받을 수 있도록 기능 추가
    * (공통) 푸시 API 추가: Push 토큰 정보 확인(Gamebase.Push.queryTokenInfo API)

#### 기능 개선/변경
* [SDK] 2.15.0
    * (공통) TOAST SDK 업데이트: Android(0.23.0), iOS(0.26.0), Unity(0.21.0)
    * (iOS) 결제 payload의 null check 로직 추가
