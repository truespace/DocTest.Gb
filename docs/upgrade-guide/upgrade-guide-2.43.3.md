---
source: upgrade-guide.md
section: "2.43.3"
order: 35
split: true
created_date_time: 20260408_184906
keyword: Error, Android, Unreal, Upgrade Guide, 2.43.3
---

## 2.43.3

### Unreal

* Google Billing Client 5.0.0 버전으로 변경되었습니다. Unreal에서 제공하는 Online SubSystem GooglePlay 플러그인 사용 시 /Config/Android/AndroidEngine.ini 파일에 해당 값을 추가해야 빌드 시 오류가 발생하지 않습니다.

            [OnlineSubsystemGooglePlay.Store]
            bUseGooglePlayBillingApiV2=False
