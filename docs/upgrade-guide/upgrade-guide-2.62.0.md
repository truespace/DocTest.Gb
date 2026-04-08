---
source: upgrade-guide.md
section: "2.62.0"
order: 20
split: true
created_date_time: 20260408_191848
keyword: Authentication, LoginForLastLoggedInProvider, XCode, Android, iOS, Upgrade Guide, 2.62.0
---

## 2.62.0

### Android

* Gamebase Android SDK 2.62.0은 Android 7.0(API Level 24) 미만 단말기에서 다음 이슈가 발생합니다. 
    * Gamebase.loginForLastLoggedInProvider 호출이 항상 실패합니다.
    * Guest 계정이 유실됩니다.
    * 이슈가 해결된 Gamebase Android SDK 2.62.1을 사용하세요.

### iOS
* Xcode 최소 지원 버전이 14.1에서 15로 변경되었습니다.
* Gamebase iOS 최소 지원 버전이 11.0에서 12.0으로 변경되었습니다.
* Gamebase와 Gamebase Adapter에 Privacy Manifest와 서명을 적용했습니다.
    * 2024년 5월 1일 이후 신규 출시 또는 업데이트를 하는 경우, Apple 정책에 따라 Gamebase iOS SDK 2.62.0 이상을 적용해야 합니다.
* LINE 인증 최소 지원 버전이 11.0에서 13.0으로 변경되었습니다.

### Unity

* Apple 개인정보 보호 정책을 준수하기 위한 대응 조치가 완료되었습니다.
    * Privacy Manifest 파일이 추가되었습니다.
    * Framework에 서명이 적용되었습니다.
    * 2024년 5월 1일 이후에는 새로운 출시나 업데이트를 위해 Apple 정책에 따라 Gamebase SDK for Unity 2.62.0 이상을 적용해야 합니다.
