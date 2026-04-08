---
source: release-notes-unity.md
section: "2.6.0 (2019.11.12)"
order: 98
split: true
created_date_time: 20260408_191848
keyword: Unity, Login, Purchase, Analytics, Logger, Authentication, Android, iOS, Release Notes, 2.6.0
---

### 2.6.0 (2019.11.12)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.6.0/GamebaseSDK-Unity.zip)

```
Gamebase SDK 2.6.0 미만 버전에서 2.6.0으로 업그레이드 하는 경우
반드시 Upgrade Guide문서에 설명된 변경 사항을 반영해 주시기 바랍니다. 
가이드 위치: Game > Gamebase > Upgrade Guide
```

#### 기능 추가
* Google 구독 결제 기능 추가
    * [SDK] 2.6.0 Android
* [SDK] 2.6.0
    * (공통) 데이터를 Log&Crash 에 전송하여 각종 분석에 이용할 수 있도록 TOAST Logger 추가
    * (iOS) Sign In with Apple 인증 추가
    * (Android) Gamebase Android SDK가 Bintray 를 통해 배포되므로 gradle 설정만으로 Gamebase 를 사용할 수 있음

#### 기능 개선/변경
* [SDK] 2.6.0
    * (Unity) 로그인시 LaunchingStatus를 갱신하는 로직에 오류가 있어 수정
    * (Unity) Debug Log를 전송하는 기능을 Gamebase 콘솔에서 설정할 경우 Client에서 로그 전송을 무한 반복하는 오류 수정
