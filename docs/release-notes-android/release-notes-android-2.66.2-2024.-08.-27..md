---
source: release-notes-android.md
section: "2.66.2 (2024. 08. 27.)"
order: 20
split: true
created_date_time: 20260408_191848
keyword: Android, Login, Purchase, WebView, ImageNotice, Error, Release Notes, 2.66.2
---

### 2.66.2 (2024. 08. 27.)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.66.2/GamebaseSDK-Android.zip)

#### 기능 개선/변경
* 외부 SDK 업데이트: NHN Cloud SDK(1.9.1), Kakaogame SDK(3.19.3), PAYCO SDK(1.5.15)
* Amazon Appstore 결제 시 문제가 생겨 재처리가 동작할 때 처음 결제를 시도했던 User ID로 아이템을 지급하도록 하는 보완 로직이 추가되었습니다.
* Twitter 로그인 타이틀 바 색상과 이름이 변경되었습니다.
* 롤링 이미지 공지의 웹뷰 내부에서 오류가 발생한 경우 기존의 성공 콜백 호출 대신 실패 콜백이 호출되도록 수정했습니다.

#### 버그 수정
* Activity가 파괴되면 해당 Activity 위에 떠 있는 WebView가 닫히며 이 때 `close event callback`이 누락되는 오류가 수정되었습니다.
* Hangame 로그인 어댑터에서 외부 IdP 로그인 시 callback이 중복으로 오는 경우 `already resumed` 오류가 발생하지 않도록 방어 로직을 추가했습니다.
