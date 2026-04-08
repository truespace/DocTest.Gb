---
source: release-notes-unity.md
section: "2.41.0 (2022. 07. 05.)"
order: 50
split: true
created_date_time: 20260408_191848
keyword: Unity, Purchase, Android, iOS, Release Notes, 2.41.0
---

### 2.41.0 (2022. 07. 05.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.41.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 외부 SDK 업데이트: TOAST Unity SDK(0.25.6)
* GamebaseEventHandler의 GamebaseEventCategory에 **IDP_REVOKED** 타입이 추가되었습니다.
    * [Game > Gamebase > Unity SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler > IdP Revoked](../unity-etc.md#idp-revoked)

#### 기능 개선/변경
* Unity의 Burst 패키지를 사용할 때 메모리 누수가 발생하는 이슈를 수정했습니다.
* Setting Tool (v2.4.0)
    * 내부 안정화 지표가 추가되었습니다.
    * 기존 SettingTool은 Unity 프로젝트에서 완전히 제거한 뒤 최신 버전으로 다시 설치해야 합니다.
    * SettingTool v1은 더 이상 지원하지 않습니다.

#### 버그 수정
* (iOS) 특정 환경에서 결제 후 크래시가 발생하는 문제를 수정했습니다.

#### 플랫폼별 변경 사항
* [Gamebase Android SDK 2.41.0](../release-notes-android.md#2410-2022-07-05)
* [Gamebase iOS SDK 2.41.0](../release-notes-ios.md#2410-2022-07-05)
