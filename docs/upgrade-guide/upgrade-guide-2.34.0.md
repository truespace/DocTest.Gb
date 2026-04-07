---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "isEnableKickoutPopup, 2.34.0, Android"
section: 2.34.0
order: 41
---

## 2.34.0

### Android

#### Changed/Deprecated APIs

* 킥아웃 팝업 표시 여부는 Gamebase 콘솔에서 킥아웃 등록시 설정할 수 있으므로 다음 필드가 deprecated 되었습니다.
    * **UIPopupConfiguration.enableKickoutPopup**

### iOS

#### Changed/Deprecated APIs

* 킥아웃 팝업 표시 여부는 Gamebase 콘솔에서 킥아웃 등록 시 설정할 수 있으므로 아래 API들이 deprecated되었습니다.
    * **-[TCGBConfiguration enableKickoutPopup:]**
    * **-[TCGBConfiguration isEnableKickoutPopup]**

### Unity

* GamebaseConfiguration의 enableKickoutPopup 속성을 더 이상 지원하지 않습니다.
