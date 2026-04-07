---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v1.11.1, 버그수정, 기능개선, 기능추가, 변경, Login, Purchase, Push, Maintenance"
section: "1.11.1 (2018.07.05)"
order: 125
---

### 1.11.1 (2018.07.05) 
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v1.11.1/GamebaseSDK-iOS.zip)

#### 기능 추가

* LINE IdP 추가

#### 기능 개선/변경

* Guest로그인 후 AddMapping 성공 시, loginForLastLoggedInPrivder를 하게되면, AddMapping 성공한 IdP계정을 사용하여 로그인하도록 변경
    
#### 버그수정

* 점검 해제 후 후속 API 진행(login/push/purchase 등)이 되지 않던 버그 수정
