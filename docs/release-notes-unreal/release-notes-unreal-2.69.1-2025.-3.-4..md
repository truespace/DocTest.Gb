---
source: release-notes-unreal.md
section: "2.69.1 (2025. 3. 4.)"
order: 14
split: true
created_date_time: 20260408_191848
keyword: Unreal, Login, Terms, Error, Android, iOS, Release Notes, 2.69.1
---

### 2.69.1 (2025. 3. 4.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.1/GamebaseSDK-Unreal.zip)

#### 기능 추가

* 론칭 정보에서 약관 정보를 확인할 수 있도록 추가했습니다.
    * FGamebaseLaunchingInfo::FApp::FTermsService

#### 기능 개선/변경

* API 호출 시 매개변수로 전달 받는 `UGamebaseJsonObject`를 `FGamebaseVariantMap(TMap<FName, FVariant>)`으로 변경했습니다.
* 내부 로직을 개선했습니다.

#### 버그 수정

* (Windows) 게스트 로그인 시 UUID 발급 과정 오류로 인해 모두 동일한 값이 생성되는 문제를 수정했습니다.
* (Windows) Line IDP 로그인 시 region 설정이 동작하지 않는 문제를 수정했습니다.
* (Windows) 킥아웃 시 ServerPushAppKickOut 이벤트 발생과 팝업이 노출되지 않는 문제를 수정했습니다.
* (Windows) 심볼 생성 시 엔진의 Build Configuration이 Development가 아닌 경우 오류가 발생하는 문제를 수정했습니다.
* (Android) 환경에 따라 RegisterPush가 동작하지 않는 문제를 수정했습니다.

#### 플랫폼별 변경 사항

* [Gamebase Android SDK 2.69.0](../release-notes-android.md#2690-2025-01-21)
* [Gamebase iOS SDK 2.69.0](../release-notes-ios.md#2690-2025-01-21)
