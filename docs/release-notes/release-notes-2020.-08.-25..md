---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v2.15.0, 버그수정, 기능개선, 기능추가, 변경, Purchase, Push"
section: "2020. 08. 25."
order: 20
---

### 2020. 08. 25.

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
* [SDK] 2.9.1
    * (Unreal) Unreal 4.22 ~ 4.25 지원
    * (Unreal) PLCrashReporter 이슈 지원: [가이드](http://docs.toast.com/ko/Game/Gamebase/ko/unreal-started/#ios-settings)

#### 기능 개선/변경
* [Console]
    * 푸시 > 푸시: 홍보성 푸시 알림 발송 시 발신자 연락처, 수신 철회 동의 방법을 입력하지 않아도 발송이 가능하도록 수정
* [SDK] 2.15.0
    * (공통) TOAST SDK 업데이트: Android(0.23.0), iOS(0.26.0), Unity(0.21.0)
    * (iOS) 결제 payload의 null check 로직 추가
* [SDK] 2.9.1
    * (Unreal) iOS Plugin 내부 Gamebase SDK for iOS 버전 업데이트(2.9.1)
    * (Unreal) UObject 레퍼런싱 처리가 누락된 부분을 수정

#### 버그 수정
* [Console]
    * 푸시 > 푸시: 푸시 알림 반복 발송 시 시간 정보가 입력된 타임존과 상관없이 무조건 UTC+9로 계산되어 전송되던 문제 수정
