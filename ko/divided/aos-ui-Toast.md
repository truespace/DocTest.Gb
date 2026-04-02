## Game > Gamebase > Android SDK 사용 가이드 > UI

## Toast

다음 API를 사용하여 쉽게 [Android 토스트(toast)](https://developer.android.com/guide/topics/ui/notifiers/toasts.html) 메시지를 표시할 수 있습니다.<br/>
메시지를 표시하는 시간 종류 파라미터는 int 형식이며, Android SDK NotificationManagerService 클래스의 정의에 따라 아래 표에 정리한 시간 동안 표시됩니다.

| 시간 종류(int)         | 노출 시간                     |
| ------------------ | ------------------------- |
| Toast.LENGTH_SHORT | 2초                        |
| Toast.LENGTH_LONG  | 3.5초                      |
| 0                  | Toast.LENGTH_SHORT => 2초  |
| 1                  | Toast.LENGTH_LONG => 3.5초 |
| 나머지 모든 값           | Toast.LENGTH_SHORT => 2초  |

**API**

```java
+ (void)Gamebase.Util.showToast(Activity activity,
                        String message,
                        int duration);    // 메시지를 표시하는 시간 종류 (Toast.LENGTH_SHORT or Toast.LENGTH_LONG)
```
