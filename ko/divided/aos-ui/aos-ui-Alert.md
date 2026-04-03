---
source: aos-ui.md
section: "Alert"
order: 6
created_date: 2026-04-03
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
