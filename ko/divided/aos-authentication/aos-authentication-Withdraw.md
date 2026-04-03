---
source: aos-authentication.md
section: "Withdraw"
order: 3
created_date: 2026-04-03
---

## Withdraw

로그인 상태에서 탈퇴를 시도합니다.

* 탈퇴 성공 시
  * 로그인했던 IdP의 게임 이용자 데이터는 삭제됩니다.
  * 해당 IdP로 다시 로그인할 수 있으며, 새로운 게임 이용자 데이터를 생성합니다.
  * 연동 중인 모든 IdP가 로그아웃 처리됩니다.
* Gamebase 탈퇴를 의미하며, IdP 계정 탈퇴를 의미하지는 않습니다.

> <font color="red">[주의]</font><br/>
>
> 여러 IdP를 연동 중인 경우, 모든 IdP 연동이 해제되고 Gamebase 유저 데이터가 삭제됩니다.
>

**API**

```java
+ (void)Gamebase.withdraw(Activity activity, GamebaseCallback callback);
```

**Example**

```java
private static void onWithdraw(final Activity activity) {
    Gamebase.withdraw(activity, new GamebaseCallback() {
        @Override
        public void onCallback(GamebaseException exception) {
            if (Gamebase.isSuccess(exception)) {
                // 탈퇴 성공
                Log.d(TAG, "Withdraw successful");
            } else {
                if (exception.getCode() == GamebaseError.SOCKET_ERROR ||
                        exception.getCode() == GamebaseError.SOCKET_RESPONSE_TIMEOUT) {
                    // Socket error 로 일시적인 네트워크 접속 불가 상태임을 의미합니다.
                    // 네트워크 상태를 확인하거나 잠시 대기 후 재시도 하세요.
                    new Thread(new Runnable() {
                        @Override
                        public void run() {
                            try {
                                Thread.sleep(2000);
                                onWithdraw(activity);
                            } catch (InterruptedException e) {}
                        }
                    }).start();
                } else {
                    // 탈퇴 실패
                    Log.e(TAG, "Withdraw failed- "
                            + "errorCode: " + exception.getCode()
                            + "errorMessage: " + exception.getMessage());
                }
            }
        }
    });
}
```
