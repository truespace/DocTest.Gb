---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "2.41.0, Android, Unity"
section: 2.41.0
order: 37
---

## 2.41.0

### Android

* 이제 웹뷰에 등록한 커스텀 스킴 이벤트가 동작할 때 자동으로 웹뷰가 종료됩니다.
    * 이전과 같이 커스텀 스킴 이벤트가 동작하더라도 웹뷰를 유지하려면 **GamebaseWebViewConfiguration.Builder.enableAutoCloseByCustomScheme(false)** API를 호출하세요.
* Gamebase Android SDK 2.41.0에는 약관 창의 '보기' 버튼이 동작하지 않는 버그가 존재합니다.
    * Gamebase 약관 창을 사용하려면 문제가 해결된 Gamebase Android SDK 2.41.1을 사용하세요.

### Unity

* Gamebase SettingTool 필수 업데이트가 추가되었습니다. (v2.4.0)
    * 기존 SettingTool은 Unity 프로젝트에서 완전히 제거한 뒤 최신 버전으로 다시 설치해야 합니다.
    * SettingTool v1은 더 이상 지원하지 않습니다.
