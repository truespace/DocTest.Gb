---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.28.0 (2021.09.28)"
section: "2.28.0 (2021.09.28)"
order: 68
---

### 2.28.0 (2021.09.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.28.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Kakaogame 인증 추가
* '결제 어뷰징 자동 해제' 기능이 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > GraceBan](../../aos-authentication.md#graceban)
    * 결제 어뷰징 자동 해제 기능은 결제 어뷰징 자동 제재로 이용 정지가 되어야 할 사용자가 '이용 정지 유예 상태' 후 이용 정지가 되도록 합니다.
    * '이용 정지 유예 상태'일 경우, 설정한 기간 내에 이용 정지 해제 조건을 모두 만족하면 정상적으로 플레이할 수 있습니다.
    * 기간 내에 조건을 충족하지 못하면 이용 정지가 됩니다.
* 결제 어뷰징 자동 해제 기능을 사용하는 게임은 로그인 후 항상 AuthToken.getGraceBanInfo() API 값을 확인하고, null이 아닌 유효한 GraceBanInfo 객체를 반환한다면 해당 유저에게 이용 정지 해제 조건, 기간 등을 안내해야 합니다.
    * 이용 정지 유예 상태인 유저의 게임 내 접근 제어는 게임에서 처리해야 합니다.
* 로그인 응답 대기중에 대기 아이콘이 표시됩니다.

#### 기능 개선/변경
* 외부 SDK 업데이트: PAYCO Android SDK(1.5.6)
