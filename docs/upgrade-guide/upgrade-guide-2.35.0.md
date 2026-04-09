---
source: upgrade-guide.md
section: "2.35.0"
order: 40
split: true
created_date_time: 20260408_184906
keyword: Login, Logout, Android, Upgrade Guide, 2.35.0
---

## 2.35.0

### Android

#### NAVER IdP

* 이제 NAVER 로그아웃 시 토큰을 삭제하지 않습니다.
    * 재로그인할 때 정보 제공 동의 창이 나타나지 않습니다.
    * 웹 로그인 시에는 계정이 변경되지 않습니다.
    * 이전 동작을 유지하려면 Gamebase Console의 AdditionalInfo에 다음과 같이 설정하세요.

```
{"logout_and_delete_token":true}
```
