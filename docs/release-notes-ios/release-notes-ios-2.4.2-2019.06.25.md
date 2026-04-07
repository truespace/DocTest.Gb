---
source: release-notes-ios.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, v2.4.2, 버그수정, 기능개선, 기능추가, 변경, Analytics, Launching"
section: "2.4.2 (2019.06.25)"
order: 111
---

### 2.4.2 (2019.06.25)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.2/GamebaseSDK-iOS.zip)

#### 기능 개선/변경

* LaunchingInfo에 JSON string 형식의 TOAST Launching 정보를 추가
* LINE iOS SDK 업데이트 (5.0.1)
    * LINE Adpater의 최소 지원 OS 버전이 iOS 10으로 변경 
    * LINE 앱을 통한 로그인 기능 추가

#### 버그수정

* Analytics 버그 수정: 로그아웃, 탈퇴, 계정 이전 시 저장된 지표 데이터를 초기화 하도록 수정
* 네트워크 연결 문제로 간헐적으로 크래시가 발생하던 현상 수정
