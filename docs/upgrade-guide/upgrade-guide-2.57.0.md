---
source: upgrade-guide.md
section: "2.57.0"
order: 23
split: true
created_date_time: 20260408_184906
keyword: iOS, Unreal, Upgrade Guide, 2.57.0
---

## 2.57.0

### iOS

* Privacy manifest 파일을 추가했습니다.
    * Privacy manifest 파일에서 Gamebase iOS SDK가 수집하는 데이터와 허용된 사유를 명시해야 하는 API 목록들을 볼 수 있습니다.
    * Apple 정책에 따라 2024년 봄까지 Gamebase iOS SDK 2.57.0 이상으로 업데이트해 주시기 바랍니다.

### Unreal
 
* Gamebase 모듈이 분리되었습니다. Gamebase 코드를 사용하려면 모듈의 Build.cs 파일 내 **GamebaseInterface** 모듈을 의존 모듈로 추가해야 합니다.

        PrivateDependencyModuleNames.AddRange(
            new[]
            {
                "Gamebase",
                "GamebaseInterface"
            }
        );
