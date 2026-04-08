---
source: release-notes-android.md
section: "2.55.0 (2023. 09. 12.)"
order: 36
split: true
created_date_time: 20260408_191848
keyword: Android, Login, WebView, Release Notes, 2.55.0
---

### 2.55.0 (2023. 09. 12.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.55.0/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: Naver Login Android SDK(5.7.0), NHN Cloud Android SDK(1.7.1)
* 구버전 Naver Login SDK의 OAuthLoginInAppBrowserActivity에서 발생하던 Cross-app Scripting 취약점이 해결되었습니다.
* Naver IdP 사용 시 Naver IdP에서 지원하지 않는 API 21 미만 단말기에서도 크래시가 발생하지 않도록 방어 로직을 추가했습니다.

#### 버그 수정
* IdP Login 시 로딩 애니메이션 off가 적용되지 않는 현상이 수정되었습니다.
* API Level 28, 29 전체 화면 웹뷰에서 windowFocus가 변경되면 내비게이션 바가 다시 생겨나는 이슈가 수정되었습니다.
* Weibo 로그인에 성공했지만 간헐적으로 Weibo SDK에서 access token이 null로 리턴되는 경우 크래시가 발생하지 않도록 방어 로직을 추가했습니다.
