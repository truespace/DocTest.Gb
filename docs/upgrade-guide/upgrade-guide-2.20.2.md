---
source: upgrade-guide.md
section: "2.20.2"
order: 49
split: true
created_date_time: 20260408_184906
keyword: iOS, Upgrade Guide, 2.20.2
---

## 2.20.2

### iOS

#### Facebook IdP

* Gamebase iOS SDK 2.20.2 에서 Facebook SDK가 9.1.0으로 업데이트 되었습니다. 
    * Facebook SDK에 추가 설정이 필요하게 되어 info.plist에 아래의 값을 추가해 주시기 바랍니다. 설정하지 않을 경우 크래시가 발생할 수 있습니다.
        * FacebookAutoLogAppEventsEnabled
        * FacebookAdvertiserIDCollectionEnabled
* 자세한 내용은 [Facebook iOS SDK 가이드](https://developers.facebook.com/docs/app-events/getting-started-app-events-ios) 를 참고하시기 바랍니다.
