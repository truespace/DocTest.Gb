---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "Unity, v2.7.0, 버그수정, 기능추가, Login"
section: "2.7.0 (2020.01.21)"
order: 93
---

### 2.7.0 (2020.01.21)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.7.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* [SDK] 2.7.0
    * (Unity) NaverCafePLUG 지원

#### 버그 수정
* [SDK] 2.7.0
    * (Android) 서버 응답(response)에서 traceError 필수 파라미터가 없더라도 크래시가 발생하지 않도록 수정
    * (Android) Firebase 설정이 누락되어 있을 때 예외가 발생하지 않도록 수정
    * (Unity) Web Login 시, gamebase://dismiss 스킴 처리 추가
    * (Unity) 릴리스 빌드 시, 간헐적으로 웹뷰가 노출되지 않는 문제 수정
