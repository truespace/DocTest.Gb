---
source: release-notes-unreal.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, v2.68.1, 버그수정, 기능개선, 변경, WebView, Logger"
section: "2.68.1 (2025. 01. 21.)"
order: 16
---

### 2.68.1 (2025. 01. 21.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.68.1/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경
* 내부 로직을 개선했습니다.
* (Windows) WebView 플러그인을 옵션으로 선택할 수 있도록 변경되었습니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Windows Settings > WebView 플러그인 안내](../../unreal-started.md#windows-settings)
* (Windows) 크래시 로그 전송 시 프로젝트 바이너리 경로에 심벌 파일을 압축한 파일이 생성되도록 추가되었습니다.
    * 자세한 내용은 다음 링크를 참고하세요.
        * [Game > Gamebase > Unreal SDK 사용 가이드 > Logger > Crash Reporter](../../unreal-logger.md#crash-reporter)

#### 버그 수정
* (Windows) 내부 로그 전송 시 크래시가 발생할 수 있는 로직이 수정되었습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.68.0](../../release-notes-android.md#2680-2024-11-26)
* [Gamebase iOS SDK 2.68.1](../../release-notes-ios.md#2681-2024-12-10)
