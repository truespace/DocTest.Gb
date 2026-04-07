---
source: release-notes-unreal.md
split: true
created_date_time: 20260406_141859
keyword: "2.73.0 (2025. 07. 15.)"
section: "2.73.0 (2025. 07. 15.)"
order: 9
---

### 2.73.0 (2025. 07. 15.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.73.0/GamebaseSDK-Unreal.zip)

#### 기능 개선/변경

* (Windows) SDK를 사용하지 않는 IdP의 경우 외부 브라우저 로그인으로 진행되도록 변경되었습니다.
    * 외부 브라우저 로그인 진행 중 로그인을 취소할 수 있는 API가 추가되었습니다.
        * CancelLoginWithExternalBrowser
        * API 호출 방법은 다음 가이드 문서를 참고하시기 바랍니다.
            * [Game > Gamebase > Unreal SDK 사용 가이드 > 인증 > Login > Login with IdP > Cancel Login with External Browser](../../unreal-authentication.md#cancel-login-with-external-browser)
* (Windows) Steam 로그인 시 Steamworks 초기화 실패 여부 메시지를 추가하여 원인을 파악하기 쉽도록 변경했습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정

* Epic Games 관련 기능을 사용하지 않을 때는 EOSSDK 모듈이 포함되지 않도록 수정되었습니다.
* (Windows) 콘솔에서 설정되지 않은 스토어를 사용할 때 크래시가 발생하지 않도록 수정되었습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.73.0](../../release-notes-android.md#2730-2025-07-15)
* [Gamebase iOS SDK 2.73.0](../../release-notes-ios.md#2730-2025-07-15)
