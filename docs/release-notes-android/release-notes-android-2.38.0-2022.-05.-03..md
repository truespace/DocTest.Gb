---
source: release-notes-android.md
section: "2.38.0 (2022. 05. 03.)"
order: 58
split: true
created_date_time: 20260408_184906
keyword: Android, Push, Release Notes, 2.38.0
---

### 2.38.0 (2022. 05. 03.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.38.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Amazon(ADM) Push Adapter가 추가되었습니다.
    * 빌드 의존성에 **gamebase-adapter-push-adm** 모듈을 추가하시면 사용 가능합니다.
            
            dependencies {
                ...
                implementation "com.toast.android.gamebase:gamebase-adapter-push-adm:$GAMEBASE_SDK_VERSION"
            }
            
    * Proguard를 적용하는 경우, 다음 가이드를 확인하여 적용하셔야 합니다.
        * [NHN Cloud > SDK 사용 가이드 > TOAST Push > Android > Amazon Device Messaging 설정 > ADM SDK 다운로드](https://docs.toast.com/ko/TOAST/ko/toast-sdk/push-android/#adm-sdk)
        * [NHN Cloud > SDK 사용 가이드 > TOAST Push > Android > Amazon Device Messaging 설정 > Proguard 설정](https://docs.toast.com/ko/TOAST/ko/toast-sdk/push-android/#proguard)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.30.0)
* Display Language의 중국어 번체(zh-TW) 언어셋에서 어색한 문장을 수정했습니다.
