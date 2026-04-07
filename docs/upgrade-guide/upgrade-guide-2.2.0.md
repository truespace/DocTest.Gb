---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "2.2.0, Unity"
section: 2.2.0
order: 59
---

## 2.2.0

### Unity

* GamebaseMainActivity의 Package Name이 변경되었습니다.
    * AndroidManifest.xml의 MainActivity 선언을 아래와 같이 변경하지 않으면 크래시가 발생합니다.
    * **com.toast.gamebase.activity.GamebaseMainActivity** -> **com.toast.android.gamebase.activity.GamebaseMainActivity**

```xml
<manifest>
    ...
    <application>
    ...
        <activity android:name="com.toast.android.gamebase.activity.GamebaseMainActivity"
            android:launchMode="singleTask"
            android:configChanges="keyboard|keyboardHidden|screenLayout|screenSize|orientation"
            android:label="@string/app_name">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    ...
    </application>
    ...
</manifest>
```
