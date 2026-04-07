---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "2.29.0, iOS, Unity"
section: 2.29.0
order: 44
---

## 2.29.0

### iOS

* Xcode 최소 지원 버전이 12에서 13으로 변경되었습니다.
    * Xcode 12에서 아카이브 빌드를 하면 에러가 발생합니다. Xcode 13으로 업데이트하시기 바랍니다.

### Unity
 
* Setting Tool 2.0.0이 배포되었습니다.
    * 폴더 구조가 변경되어, 이전 버전의 Setting Tool을 완전히 삭제한 후 재설치해야 합니다. 
    * Setting Tool 1.5.0 이하 사용자는 아래 디렉터리 있는 Gamebase 관련 라이브러리들을 모두 제거해야 합니다. 
        * **Assets/Plugins/Android**  
        * **Assets/Plugins/iOS** 
    * 변경된 내용 및 사용 방법은 아래 가이드를 확인하십시오. 
        * [Game > Gamebase > Unity SDK 사용 가이드 > 시작하기 > Specification of Setting Tool](../../unity-started.md#specification-of-setting-tool)
