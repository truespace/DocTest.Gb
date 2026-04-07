---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.52.0 (2023. 06. 27.)"
section: "2.52.0 (2023. 06. 27.)"
order: 39
---

### 2.52.0 (2023. 06. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.52.0/GamebaseSDK-Android.zip)

#### 기능 추가
* ONE store v21 Adapter가 추가되었습니다.
* 특정 메시지가 포함된 알림을 표시하지 않는 커스텀 푸시 리시버가 추가되었습니다.
    * 이 기능을 사용하려면 빌드 의존성에 **gamebase-adapter-push-notification** 모듈 선언을 추가해야 합니다.

            dependencies {
                ...
                implementation "com.toast.android.gamebase:gamebase-adapter-push-notification:$GAMEBASE_SDK_VERSION"
            }

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK 업데이트 1.6.0

#### 버그 수정
* Render outside safe area 가로 모드에서 내비게이션 바와 X 버튼이 겹쳐 보이는 오류를 수정했습니다.
* 약관 팝업에서 '더보기'를 클릭했을 때 약관 전문이 완전히 로딩되기 전에는 백그라운드를 클릭할 수 없도록 수정했습니다.
