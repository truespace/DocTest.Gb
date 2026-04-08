---
source: release-notes-ios.md
section: "2.69.0 (2025. 01. 21.)"
order: 11
split: true
created_date_time: 20260408_191848
keyword: iOS, Login, Console, Release Notes, 2.69.0
---

### 2.69.0 (2025. 01. 21.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트
    * PAYCO iOS SDK (1.5.13)
        * iOS 18에서 정상적인 PAYCO 간편로그인 이용을 위한 openURL 관련 함수 수정
    * Hangame iOS SDK (1.17.1)
        * 내부 로직 개선
    * Weibo iOS SDK (3.4.0)
        * iOS 18 최적화
* completion block이 main thread에서 실행되도록 수정하였습니다.

#### 버그 수정
* SceneDelegate를 사용하는 앱에서 NAVER 로그인 취소 시 callback이 오지 않는 버그를 수정하였습니다.
* Gamebase 콘솔에 LINE old clientId를 설정하지 않았을 때 LINE 로그인에 실패하는 버그를 수정하였습니다.
