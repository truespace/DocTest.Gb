---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, XCode, v2.26.0, 버그수정, 기능개선, 변경, Push, TermsView"
section: "2.26.0 (2021.08.10)"
order: 72
---

### 2.26.0 (2021.08.10)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.26.0/GamebaseSDK-iOS.zip)

#### 기능 개선/변경
* Display Language 기능이 개선되었습니다.
    * 지금까지는 언어셋을 추가하기 위해 Gamebase.bundle 안에 있는 파일을 직접 수정해야 했습니다.
        * 이제 Xcode 프로젝트의 Copy Bundle Resources에 localizedstring.json 파일을 추가하면 되도록 개선하였습니다.
    * Display Language 언어셋에 중국어 간체(zh-CN), 중국어 번체(zh-TW), 태국어(th)가 추가되었습니다.
    * 기본 언어코드가 **en** 이었으나, Gamebase 콘솔에서 설정한 기본언어가 반영되도록 개선하였습니다.
        * [Game > Gamebase > 콘솔 사용 가이드 > 앱 > App > 언어 설정](../../oper-app.md#language-settings)
* showTermsView API 호출 후 생성할 수 있는 PushConfiguration 객체의 생성 기준이 다음과 같이 변경되었습니다.
    * 변경 전
        * 약관 항목 중에 **Push 수신** 항목이 존재하는 경우에만 nil이 아닌 유효한 PushConfiguration이 반환되었습니다.
        * 유저가 주간, 야간 홍보성 Push 수신에 모두 거부한 경우 PushConfiguration.pushEnabled는 false로 생성되었습니다.
    * 변경 후
        * 약관 UI가 표시되었다면 항상 nil이 아닌 유효한 PushConfiguration이 반환됩니다.
        * showTermsView가 반환하는 PushConfiguration 객체의 pushEnabled 값은 항상 true입니다.
    * 변경되지 않고 동일한 점
        * 이미 약관에 동의하여 약관 UI가 표시되지 않았다면 PushConfiguration은 nil로 반환됩니다.

#### 버그 수정
* Push 언어 설정은 별다른 보조 처리가 없이 단말기의 언어코드를 그대로 적용되어, Push 콘솔에서 전송한 메시지의 언어코드가 일치하지 않는 문제를 수정하였습니다.
