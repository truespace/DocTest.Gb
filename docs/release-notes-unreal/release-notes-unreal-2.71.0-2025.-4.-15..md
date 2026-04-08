---
source: release-notes-unreal.md
section: "2.71.0 (2025. 4. 15.)"
order: 12
split: true
created_date_time: 20260408_191848
keyword: Unreal, Purchase, Authentication, Android, iOS, Release Notes, 2.71.0
---

### 2.71.0 (2025. 4. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.71.0/GamebaseSDK-Unreal.zip)

#### 기능 추가

* '게임 공지' 신규 기능이 추가되었습니다.
    * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > UI > GameNotice](../unreal-ui.md#gamenotice)
* (Windows) Google Play Games 지원을 위한 Google 결제 기능이 추가되었습니다.
    * [Windows 설정 툴](../unreal-started.md#windows-settings) 내 Windows Store 설정에 `Google Play Store`가 추가되었습니다.

#### 기능 개선/변경

* (Windows) 시스템 설정에서 '지역 > 국가 또는 지역'을 바탕으로 CountryCode를 생성하도록 수정했습니다.
    * 변경 전에는 엔진에서 제공하는 `FInternationalization::Get().GetDefaultCulture()`를 통해 '지역 > 사용지역 언어' 정보를 가져왔습니다.

#### 버그 수정

* (Windows) WebView를 열고 프로그램 종료 시 크래시가 발생하지 않도록 수정했습니다.
* (Windows) 엔진에 포함된 Steamworks 모듈을 에디터에서 사용할 수 없으므로 Steam 인증 및 결제 기능을 에디터에서 사용할 수 없도록 수정했습니다.
* (Windows) 로그 전송 필터링이 정상적으로 동작하지 않는 문제가 수정되었습니다.
* 내부 로직을 개선했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.71.0](../release-notes-android.md#2710-2025-04-15)
* [Gamebase iOS SDK 2.71.0](../release-notes-ios.md#2710-2025-04-15)
