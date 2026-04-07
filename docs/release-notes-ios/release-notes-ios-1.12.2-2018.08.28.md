---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, XCode, v1.12.2, 기능개선, 변경"
section: "1.12.2 (2018.08.28)"
order: 122
---

### 1.12.2 (2018.08.28) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.12.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* Google Auth Adapter, Naver Auth Adapter의 Callback URL Scheme 설정 개선
    * 콘솔에 "url_scheme_ios_only" 값을 설정하지 않으면 Default URL Scheme을 설정 하도록 개선: Default URL Scheme을 사용하기 위해서는 XCode > Target > Info > URL Types에 tcgb.{Bundle ID}.google 또는 tcgb.{Bundle ID}.naver 등록 필요
* Payco Auth Adapter 개선
    * URL Scheme 미설정으로 인해 의도치 않은 URL Scheme을 호출하던 문제 수정: 설정 방법이 변경되어 업데이트를 위해서는 반드시 URL Scheme 설정 필요 (XCode > Target > Info > URL Types에 tcgb.{Bundle ID}.payco를 등록)
