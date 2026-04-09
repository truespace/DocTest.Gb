---
source: upgrade-guide.md
section: "2.40.0"
order: 38
split: true
created_date_time: 20260408_184906
keyword: iOS, Unreal, Upgrade Guide, 2.40.0
---

## 2.40.0

### Unreal

* 일부 API의 이름이 변경되었습니다.
    * FGamebaseAnalyticesLevelUpData → FGamebaseAnalyticsLevelUpData
    * FGambaseBanInfoPtr → FGamebaseBanInfoPtr
* (iOS) iOS 설정 툴을 제공하면서 빌드 시 필요한 프레임워크만 포함되도록 수정되었습니다.
* (iOS) PLCrashReporter가 업데이트되어 엔진 내부에 PLCrashReporter도 업데이트가 필요합니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Installation > iOS Settings > PLCrashReporter](../unreal-started.md#ios-settings)
* (iOS) Facebook iOS SDK가 9.2.0버전으로 업데이트되어 swift 사용을 위해 엔진 코드 수정이 필요합니다.
    * [Game > Gamebase > Unreal SDK 사용 가이드 > 시작하기 > Installation > iOS Settings > Facebook SDK](../unreal-started.md#ios-settings)
