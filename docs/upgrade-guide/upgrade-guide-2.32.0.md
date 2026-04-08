---
source: upgrade-guide.md
section: "2.32.0"
order: 43
split: true
created_date_time: 20260408_191848
keyword: Login, Android, Upgrade Guide, 2.32.0
---

## 2.32.0

### Android

* Gamebase Access Token이 만료되어 복구되지 않을 때 발생하는 GamebaseEventHandler 이벤트 category가 **GamebaseEventCategory.OBSERVER_HEARTBEAT**에서 **GamebaseEventCategory.LOGGED_OUT**으로 변경되었습니다.
    * **GamebaseEventCategory.OBSERVER_HEARTBEAT** 이벤트에서 GamebaseEventObserverData.code 값이 **GamebaseError.AUTH_TOKEN_LOGIN_INVALID_TOKEN_INFO(3102)**일 때 로그인 하도록 구현했다면 **GamebaseEventCategory.LOGGED_OUT** 이벤트에서 로그인을 하도록 변경하시기 바랍니다.
