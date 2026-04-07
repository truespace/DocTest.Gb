---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "Contact, IdP, 2.53.0"
section: 2.53.0
order: 27
---

## 2.53.0

### Android

#### Contact

* '고객 센터' 기능을 사용하는 경우 첨부 파일 선택 시 권한 요청이 정상적으로 작동하도록 아래 가이드에 따라 AndroidManifest.xml에 권한 설정을 추가해야 합니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > AndroidManifest.xml > Contact](../../aos-started.md#contact)

#### Line IdP

* 기존 ['시작하기' 문서](../../aos-started.md)에서 Line IdP 사용 시 AndroidManifest.xml에 선언하도록 안내한 아래 내용은 Line SDK 업데이트로 인해 불필요해졌으므로 삭제하시기 바랍니다.

```xml
<manifest>
    <!-- [Android11] settings start -->
    <queries>
        <!-- [LINE] Configurations begin -->
        <package android:name="jp.naver.line.android" />
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
            <data android:scheme="https" />
        </intent>
        <!-- [LINE] Configurations end -->
    </queries>
    <!-- [Android11] settings end -->
        
    <application
          tools:replace="android:allowBackup"
          ... >
</manifest>
```
