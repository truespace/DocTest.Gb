---
source: release-notes.md
section: "2020. 10. 13."
order: 16
split: true
created_date_time: 20260408_184906
keyword: Login, Logout, WebView, Authentication, ImageNotice, Android, iOS, Release Notes, 2.17.0
---

### 2020. 10. 13.

```
한게임 인증 사용을 원하는 경우 고객센터로 미리 연락주세요.
```

#### 기능 추가
* Hangame IdP 인증 추가: SDK 2.17.0

#### 기능 개선/변경
* [SDK] 2.17.0
    * (공통) 고객 센터 첨부 이미지 클릭 시 다운로드 지원
    * (공통) TOAST SDK 업데이트: Android(0.23.2), Unity(0.21.2)
    * (iOS) TCGBMember.regDate, TCGBMember.lastLoginDate의 타입을 long long으로 변경
    * (iOS) 웹뷰에서 URL 및 타이틀 변경 시 타이틀을 재출력할 수 있도록 로직 변경

#### 버그 수정
* [SDK] 2.17.0
    * (iOS) PAYCO 인증: lastLoggedInProvider 로그인 후 로그아웃 호출 시 로그아웃 콜백이 오지 않는 문제 수정
* [SDK] 2.17.1
    * (Android) 2.17.0에서 ImageNotice API 호출 시 kotlinx-coroutine 모듈에서 크래시가 발생하는 문제 수정
