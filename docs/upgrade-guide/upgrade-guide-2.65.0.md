---
source: upgrade-guide.md
section: "2.65.0"
order: 17
split: true
created_date_time: 20260408_184906
keyword: Purchase, ImageNotice, Error, Gradle, XCode, Android, iOS, Upgrade Guide, 2.65.0
---

## 2.65.0

### Common

* Gamebase SDK 2.65.0에서 이미지 공지 기능 사용 시 발생하는 문제를 수정하였습니다.
    * 표시할 이미지 공지가 없는 경우 오류 대신 성공 콜백이 호출되도록 변경하였습니다.
    * 등록된 이미지 공지가 없는 경우 빈 공지 화면이 노출되고, 이때 Android에서는 '오늘은 그만 보기'를 체크한 뒤 화면을 닫으면 크래시가 발생하는 문제를 수정하였습니다.
    * 이슈가 해결된 Gamebase SDK 2.65.1 이상을 사용하세요.

### Android

* Google billing client version 6.2.1이 적용되어 Android OS 4.4(API Level 19) 단말기에서 결제하려면 추가 설정이 필요합니다.
    * 자세한 내용은 [Game > Gamebase > Android SDK 사용 가이드 > 시작하기 > Setting > Gradle > Root level build.gradle](../aos-started.md#root-level-buildgradle) 가이드를 참고하시기 바랍니다.

### iOS

* Facebook SDK가 17.0.1로 업데이트되면서 Dynamic Framework로 변경되었습니다.
    * Gamebase SDK를 다운로드하여 Xcode에 직접 설정하는 경우, Facebook SDK를 Embeded Frameworks에 추가해야 합니다.
    * 자세한 내용은 [Game > Gamebase > iOS SDK 사용 가이드 > 시작하기 > Setting > Xcode Settings](../ios-started.md#xcode-settings) 가이드를 참고하시기 바랍니다.
