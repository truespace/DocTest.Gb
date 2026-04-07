---
source: release-notes-unity.md
split: true
created_date_time: 20260406_141859
keyword: "2.4.0 (2019.05.28)"
section: "2.4.0 (2019.05.28)"
order: 106
---

### 2.4.0 (2019.05.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.4.0/GamebaseSDK-Unity.zip)

#### 기능 추가
* HANGAME mix 일본결제 추가
    * [SDK] 2.4.0
        * (Unity)Standalone 일본 외부결제 추가
        * (Unity)Standalone 일본 HANGAME 인증 추가

#### 기능 개선/변경
* [SDK] 2.4.0
    * (공통) 지표관련 Class 변경
        * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히보기 [Android](../../aos-etc.md#game-user-data-settings) / [iOS](../../ios-etc.md#game-user-data-settings) / [Unity](../../unity-etc.md#game-user-data-settings) / JavaScript]
        * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히보기 [Android](../../aos-etc.md#level-up-trace) / [iOS](../../ios-etc.md#level-up-trace) / [Unity](../../unity-etc.md#level-up-trace) / JavaScript]
    * (Android)NAVER SDK 버전 업데이트(v4.2.5): NAVER SDK 버그 수정(NAVER 로그인 도중에 앱 아이콘을 통해 앱을 재시작할 경우, Activity가 강제종료 되는 이슈로 인해 인증 프로세스가 중단되는 이슈가 해결)
    * (Unity)StandaloneWebview가 32bit 빌드를 지원 (SDK 용량 53.6MB에서 99.2MB로 증가)
