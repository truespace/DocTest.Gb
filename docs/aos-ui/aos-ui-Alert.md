---
source: aos-ui.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Alert, showAlertDialog"
section: Alert
order: 6
---

## Alert

시스템 알림을 표시할 수 있습니다.<br/>

### Simple Alert Dialog

제목과 메시지만 입력하여 간단하게 알림 대화 상자를 표시할 수 있습니다.

**API**

```java
+ (void)Gamebase.Util.showAlertDialog(Activity activity, String title, String message);
```

![Alert Dialog Example](./image/aos-developers-guide-ui-002_1.0.0.png)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Android Alert Dialog 예시를 보여주는 모바일 앱 스크린샷
    구성: MainActivity 화면에서 Toast Message, Dialog 옵션(Dialog, Selector Dialog, ChoiceItem Dialog) 등의 UI 요소가 나열되어 있고, 중앙에 "Title"과 "Message" 텍스트가 있는 Alert Dialog가 CANCEL, OK 버튼과 함께 팝업으로 표시된 Android 스크린샷
    Keyword: AlertDialog, 다이얼로그, Android, UI, 스크린샷, Toast, CANCEL, OK
-->


### Alert Dialog with Listener

알림 대화 상자를 표시한 후 처리 결과를 콜백받고 싶다면 다음 API를 사용합니다.

**API**

```java
+ (void)Gamebase.Util.showAlertDialog(Activity activity,
                            String title,
                            String messsage,
                            String okButtonText,
                            DialogInterface.OnClickListener clickListener);
```
