---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Gradle, v2.31.0, 기능개선, 기능추가, 변경"
section: "2.31.0 (2021.12.14)"
order: 65
---

### 2.31.0 (2021.12.14)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.31.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Amazon 스토어가 추가되었습니다.
    * **STORE_CODE**는 **AMAZON**입니다.
    * 스토어 설정 방법은 다음 가이드를 확인하시기 바랍니다.
        * [Game > Gamebase > 스토어 콘솔 가이드 > Amazon 콘솔 가이드](../../console-amazon-guide.md)
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Define Adapters](../../aos-started.md#define-adapters)
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Android 11](../../aos-started.md#android-11)
* Huawei 스토어가 추가되었습니다.
    * **STORE_CODE**는 **HUAWEI**입니다.
    * 스토어 설정 방법은 다음 가이드를 확인하시기 바랍니다.
        * [Game > Gamebase > 스토어 콘솔 가이드 > Huawei 콘솔 가이드](../../console-huawei-guide.md)
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Define Adapters](../../aos-started.md#define-adapters)
        * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Resources > Huawei Store](../../aos-started.md#resources)

#### 기능 개선/변경
* 외부 SDK 업데이트: TOAST Android SDK(0.29.0)
* 이용 정지 웹뷰 내의 고객 센터 링크에서 이용 정지 유저 정보로 문의를 등록할 수 없는 문제를 해결하였습니다.
* 앱이 켜지자마자 Gamebase 초기화를 호출하는 경우, 론칭 팝업 창이 간헐적으로 영어로 표시되는 문제를 수정하였습니다.
* 앱이 백그라운드에서 포그라운드로 전환될 때는 항상 론칭 정보가 변경되지 않았는지 바로 체크하도록 스케줄러를 개선하였습니다.
