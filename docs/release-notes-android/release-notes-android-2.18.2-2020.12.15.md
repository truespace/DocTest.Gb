---
source: release-notes-android.md
section: "2.18.2 (2020.12.15)"
order: 82
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Purchase, Push, WebView, iOS, Unity, Release Notes, 2.18.2
---

### 2.18.2 (2020.12.15)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.18.2/GamebaseSDK-Android.zip)

#### 기능 추가
* Gamebase 고객 센터 페이지 오픈 시 게임에서 정의한 extra data 전달: SDK 2.18.2
    * [Console] 고객 센터 > 고객 문의: 고객 문의 상세 조회 화면에서 추가로 등록한 extra data 확인 가능
* [SDK] 2.18.2
    * (공통) 개발사 자체 고객 센터 오픈 시 additionalURL 필드 추가
    * (공통) 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription

#### 기능 개선/변경
* [SDK] 2.18.2
    * (공통) TOAST SDK 업데이트: Android(0.24.2), iOS(0.27.1), Unity(0.21.3)
    * (Android) 암호화 로직 보안 경고 해결을 위한 외부 SDK 업데이트: PAYCO Login SDK(1.5.3), Hangame ID SDK(1.3.2)
    * (Android) Tencent Push 모듈 제거
    * (Android) Gamebase Android SDK 2.6.0에서 deprecated된 함수 제거
        * GamebaseConfiguration.Builder.setFCMSenderId()
        * GamebaseConfiguration.Builder.setTencentAccessKey()
        * GamebaseConfiguration.Builder.setTencentAccessId()

#### 버그 수정
* [SDK] 2.18.2
    * (Android) 5.0~6.0 OS 단말기에서 웹뷰 커스텀 스킴이 동작하지 않는 문제 수정
