---
source: release-notes-unity.md
section: "1.14.2 (2018.11.15)"
order: 113
split: true
created_date_time: 20260408_184906
keyword: Unity, Error, ShowWebView, Android, iOS, Release Notes, 1.14.2
---

### 1.14.2 (2018.11.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.14.2/GamebaseSDK-Unity.zip)
#### 기능 개선/변경
* [SDK] 1.14.2
    * (Android)점검시, 데이터구조에서 점검 시작/종료 시간을 의미하는 epoch time의 타입을 기존 String에서 long으로 타입 변경 : 기존 Gamebase Unity와 연동 후 점검 호출 시 타입불일치로 콜백이 내려오지 않는 현상으로 인한 수정
    * (iOS)Provider Profile 획득 메서드 호출 시, 반환하는 TCGBAuthProviderProfile 객체의 description 메서드의 JSON 문자열 구조 변경으로 인하여 Gamebase iOS SDK 1.14.0와 Unity Plugin 1.14.0 적용시 크래시가 발생될 수 있는 구조 수정

#### 버그수정
* [SDK] 1.14.2
    * (Unity)ShowWebView API 호출 시 파라메타에 Callback을 넣지 않으면 크래시가 발생되는 부분 수정
    * (Unity)iOS SDK의 Deleted API를 호출하는 코드가 있어 컴파일시 오류가 발생 되는 버그 수정
