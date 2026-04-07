---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.17.0, 버그수정, 기능개선, 기능추가, 변경, IdP"
section: "2.17.0 (2020.10.13)"
order: 89
---

### 2.17.0 (2020.10.13)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.17.0/GamebaseSDK-iOS.zip)

```
한게임 인증 사용을 원하는 경우 고객 센터로 미리 연락주세요.
```

#### 기능 추가

* Hangame IdP 인증 추가

#### 기능 개선/변경

* 고객 센터 첨부 이미지 클릭 시 다운로드 지원
* TCGBMember.regDate, TCGBMember.lastLoginDate의 타입을 long long으로 변경
* 웹뷰에서 URL 및 타이틀 변경 시 타이틀을 재출력할 수 있도록 로직 변경

#### 버그 수정

* PAYCO 인증: lastLoggedInProvider 로그인 후 로그아웃 호출 시 로그아웃 콜백이 오지 않는 문제 수정
