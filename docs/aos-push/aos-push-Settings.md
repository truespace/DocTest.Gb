---
source: aos-push.md
section: "Settings"
order: 1
split: true
created_date_time: 20260408_191848
keyword: Android, Push, Alert, RegisterPush
---

## Game > Gamebase > Android SDK 사용 가이드 > 푸시

### Settings

#### Android Notification Icon

푸시 알림이 도착했을때 표시되는 아이콘의 경우, 기본 상태에서는 앱 아이콘이 사용됩니다.

하지만 Android의 푸시 아이콘은 알파 영역을 적용한 단색 이미지를 사용해야 올바르게 표시됩니다.
[머티리얼 디자인 가이드 - Android Notification \[LINK\]](https://material.io/design/platform-guidance/android-notifications.html#anatomy-of-a-notification)

단말기 해상도별로 아이콘 사이즈도 정해져 있으므로 다음을 참고하여 푸시 아이콘을 준비하시기 바랍니다.

* MDPI - 24 x 24  (drawable-mdpi)
* HDPI - 36 x 36  (drawable-hdpi)
* XHDPI - 48 x 48  (drawable-xhdpi)
* XXHDPI - 72 x 72  (drawable-xxhdpi)
* XXXHDPI - 96 x 96  (drawable-xxxhdpi)

푸시 아이콘 파일 이름에 공백, 영어 대문자, 특수문자는 사용할 수 없습니다.

그리고 다음 Notification Options 가이드를 참고하여 **default_small_icon**(AndroidManifest.xml) 또는 **setSmallIconName**(API)을 설정해야 합니다.
[Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > Notification Options](../aos-started.md#notification-options)
[Game > Gamebase > Android SDK 사용 가이드 > 푸시 > Notification Options > Set Notification Options with RegisterPush in Runtime](./aos-push-Notification-Options.md#set-notification-options-with-registerpush-in-runtime)
