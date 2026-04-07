---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "2.63.0, iOS, Unreal"
section: 2.63.0
order: 19
---

## 2.63.0

### iOS

* Facebook SDK가 17.0.0으로 업데이트되면서 Info.plist에 FacebookClientToken과 FacebookDisplayName을 추가해야 합니다.
```
<key>FacebookClientToken</key>
<string>{FACEBOOK_CLIENT_TOKEN}</string>
<key>FacebookDisplayName</key>
<string>{FACEBOOK_DISPLAY_NAME}</string>
```

### Unreal

* Android Firebase Notification 설정 방법이 변경되어 플러그인 내부에 google-services-json.xml 파일이 아닌 설정 툴에서 직접 지정하도록 변경되었습니다.
    * 기존에 제공되었던 Gamebase/Source/Gamebase/ThirdParty/Android/res/values/google-services-json.xml 파일이 제거되었습니다.
    * Firebase 콘솔에서 다운로드한 google-services.json 파일을 [Android 설정 툴](../../unreal-started.md#android-settings)의 Push 항목 내 FCM 하위에 있는 `GoogleServicesFilePath` 값을 설정합니다.
