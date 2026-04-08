---
source: release-notes-android.md
section: "1.13.0 (2018.09.13)"
order: 114
split: true
created_date_time: 20260408_191848
keyword: Android, Login, Push, Initialize, Error, iOS, Release Notes, 1.13.0
---

### 1.13.0 (2018.09.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.13.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* [SDK] 1.13.0
    * (공통)IAP SDK 최신버전 적용 (android:1.5.1, iOS:1.6.0)
    * (Android)Push API 호출 시, Gamebase 초기화/로그인 상태에 따라 호출 실패에 대한 에러 메시지를 보다 명확하게 개선
        * 초기화 전 호출 : NOT_INITIALIZED(1)
        * 초기화 이후 호출 시 Push 모듈이 없음 : NOT_SUPPORTED(10)
        * 초기화 성공 및 로그인 이전 호출 : NOT_LOGGED_IN(2)        
    
#### 버그수정
* [SDK] 1.13.0
    * (Android)NaverCafe SDK와의 충돌로 NAVER 로그인시 발생하던 오류 해결
