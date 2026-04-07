---
source: unreal-logger.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, Logger, Unreal SDK 사용 가이드"
section: Settings
order: 1
---

## Game > Gamebase > Unreal SDK 사용 가이드 > Logger

여기에서는 Log & Crash Search 전송 API를 사용하는 방법을 알아보겠습니다.

### Settings

* Windows
    * Log & Crash Search에서 ProjectVersion의 값을 설정하려면 DefaultGame.ini에서 GeneralProjectSettings의 ProjectVersion에 알맞은 버전을 입력해야 합니다.
            
            [/Script/EngineSettings.GeneralProjectSettings]
            ProjectVersion=1.0.0
