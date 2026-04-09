---
source: release-notes-android.md
section: "2.34.0 (2022. 02. 22.)"
order: 62
split: true
created_date_time: 20260408_184906
keyword: Android, Push, Alert, Terms, ImageNotice, Console, Release Notes, 2.34.0
---

### 2.34.0 (2022. 02. 22.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.34.0/GamebaseSDK-Android.zip)

#### 기능 추가
* Gamebase 콘솔의 업데이트 필수 설정에서 **팝업 버튼 추가**를 선택하면 클라이언트의 업데이트 필수 팝업 창에 **자세히 보기** 버튼이 추가됩니다.
* 단말기에서 알림을 허용했는지 여부를 알 수 있는 API가 추가되었습니다.
    * **Gamebase.Push.queryNotificationAllowed()**
* 공통 약관 API 호출 후 약관 UI가 표시되었는지 여부를 알 수 있는 VO 클래스가 추가되었습니다.
    * **GamebaseShowTermsViewResult**

#### 기능 개선/변경
* 킥아웃 팝업 창 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 다음 필드가 deprecated되었습니다.
    * **UIPopupConfiguration.enableKickoutPopup**

#### 버그 수정
* 이미지 공지에서 **오늘은 다시 보지 않기**를 선택했을 때, 24시간이 지났는데도 이미지 공지가 표시되지 않는 버그를 수정했습니다.
