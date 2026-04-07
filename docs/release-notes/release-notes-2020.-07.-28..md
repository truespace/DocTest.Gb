---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2020. 07. 28."
section: "2020. 07. 28."
order: 23
---

### 2020. 07. 28.

#### 기능 추가
* [Console]
    * Analytics: WAU(Weekly Active User), MAU(Monthly Active User) 지표 추가
* [SDK] 2.13.0
    * (Unity) Standalone: 이미지 공지 표시 API 추가    

#### 기능 개선/변경
* [Console]
    * 앱 > 앱: iOS 12 이하에서 Sign In With Apple 인증을 하기 위한 정보를 추가 입력할 수 있도록 수정
* [SDK] 2.13.0
    * (Android) 이미지 공지의 팝업 이미지 비율 계산 로직 수정
    * (iOS) Sign In With Apple 인증: iOS 12 이하 지원

#### 버그 수정
* [Console]
    * 운영 > 이미지 공지: 복사 기능 및 대상 국가 선택 후 전체 국가로 수정 시 반영되지 않는 오류 수정
* [SDK] 2.13.0
    * (Android) 웹뷰 종료 시 종료 콜백에서 ANDROID_ACTIVITY_DESTROYED(31) 오류가 반환되는 문제 수정
    * (Android) 결제 모듈에 ProGuard 선언이 누락된 오류 수정
