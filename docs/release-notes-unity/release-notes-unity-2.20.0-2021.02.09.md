---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v2.20.0, 버그수정, 기능개선, 기능추가, 변경, 제거, TermsView, Contact"
section: "2.20.0 (2021.02.09)"
order: 74
---

### 2.20.0 (2021.02.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.20.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* 공통 약관 기능 추가
    * 약관 웹뷰를 여는 API 추가
    * 약관 리스트 및 유저별 동의 여부를 조회하는 API 추가
    * 유저별 약관 동의 여부를 Gamebase 서버에 저장하는 API 추가

#### 기능 개선/변경
* 고객 센터 타입이 TOAST 조직 상품(Online Contact)인 경우 로그인을 하지 않아도 고객 센터가 표시되도록 변경
* Warning 로그 제거
* Standalone 웹뷰에 CEF 2.1.2 업데이트
    * URL의 길이가 2,048보다 길 경우 크래시가 발생하는 이슈 수정
    * Unity 2019에서 빌드 시 라이브러리 경로가 변경되어 PostProcessBuild 개선
    * string 초기화를 하지 않아 간헐적으로 발생하는 오류 수정
    * Gamebase 웹뷰 사용 중 웹뷰가 신(scene)을 이동한 이후에는 다시 열리지 않는 버그 수정
