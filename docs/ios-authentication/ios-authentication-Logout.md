---
source: ios-authentication.md
split: true
created_date_time: 20260406_141859
keyword: Logout
section: Logout
order: 2
---

## Logout

#### Import Header File

로그아웃을 구현하고자 하는 ViewController에 다음의 헤더 파일을 가져옵니다.

```objectivec
#import <Gamebase/Gamebase.h>
```

#### Logout API

로그인된 IdP에서 로그아웃을 시도합니다. 주로 게임의 설정 화면에 로그아웃 버튼을 두고, 버튼을 클릭하면 실행되도록 구현하는 경우가 많습니다.
로그아웃이 성공하더라도, 게임 유저 데이터는 유지됩니다.
로그아웃에 성공하면 해당 IdP로 인증했던 기록을 제거하므로 다음에 로그인할 때 ID, 비밀번호 입력 창이 표시됩니다.<br/><br/>

다음은 로그아웃 버튼을 클릭하면 로그아웃이 되는 예시 코드입니다.

```objectivec
- (void)authLogout {
    [TCGBGamebase logoutWithViewController:topViewController completion:^(TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == YES) {
            // To Logout Succeeded
        } else {
            // To Logout Failed
        }
    }];
}
```
