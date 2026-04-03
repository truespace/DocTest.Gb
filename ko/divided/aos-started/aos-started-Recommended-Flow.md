---
source: aos-started.md
section: "Recommended Flow"
order: 3
created_date: 2026-04-03
---

## Recommended Flow

* Gamebase에서 권장하는 flow는 Sample Project에도 동일하게 구현되어 있습니다.
    * Android Sample Project
        * [https://github.com/nhn/toast.gamebase.android.sample](https://github.com/nhn/toast.gamebase.android.sample)
            * app/src/main/java/com/toast/android/gamebase/sample/gamebase_manager 폴더의 kt 파일들을 참고하시면 됩니다.
    * Unity Sample Project
        * [https://github.com/nhn/toast.gamebase.unity.sample](https://github.com/nhn/toast.gamebase.unity.sample)
* 게임이 시작되었을 때 Gamebase 클라이언트 SDK를 초기화하고 로그인이 성공하면, 결제 재처리를 시작하고 푸시 토큰을 등록하세요.

![overview flow](./image/overview_flow_2.30.1.png)

* 상세 flow 는 다음 링크에서 확인할 수 있습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > ETC > Additional Features > Gamebase Event Handler](../../aos-etc.md#gamebase-event-handler)
    * [Game > Gamebase > Android SDK 사용 가이드 > 초기화 > Initialization Flow](../../aos-initialization.md#initialization-flow)
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Login Flow](../../aos-authentication.md#login-flow)
    * [Game > Gamebase > Android SDK 사용 가이드 > 결제 > Retry Transaction Flow](../../aos-purchase.md#retry-transaction-flow)
    * [Game > Gamebase > Android SDK 사용 가이드 > 푸시 > Register Push](../../aos-push.md#register-push)
