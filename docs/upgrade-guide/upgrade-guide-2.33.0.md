---
source: upgrade-guide.md
section: "2.33.0"
order: 42
split: true
created_date_time: 20260408_184906
keyword: Mapping, Error, iOS, Unity, Upgrade Guide, 2.33.0
---

## 2.33.0

### iOS

* TCGB_ERROR_UNKNOWN_ERROR 에러에 매핑된 오류 코드가 변경되었습니다.
    * TCGB_ERROR_UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 TCGB_ERROR_SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.

### Unity

* GamebaseErrorCode.UNKNOWN_ERROR 에러에 매핑된 오류 코드가 변경되었습니다.
    * GamebaseErrorCode.UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 GamebaseErrorCode.SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.

### Unreal

* GamebaseErrorCode.UNKNOWN_ERROR 에러에 매핑된 오류 코드가 변경되었습니다.
    * GamebaseErrorCode::UNKNOWN_ERROR 에러에 매핑된 오류 코드를 999에서 9999로 변경하였습니다.
    * 오류 코드 999에 매핑한 GamebaseErrorCode::SOCKET_UNKNOWN_ERROR 에러를 새로 추가하였습니다.
