---
source: ios-ui.md
split: true
created_date_time: 20260406_141859
keyword: "iOS, showToastWithMessage, showToastMessage"
section: Toast
order: 7
---

## Toast

다음 API를 사용하여 쉽게 [Android 토스트(toast)](https://developer.android.com/guide/topics/ui/notifiers/toasts.html) 메시지를 표시할 수 있습니다.<br/>
간단한 메시지와 표시되는 시간을 설정할 수 있습니다.

```objectivec
- (void)showToastMessage:(id)sender {
    // 3초 동안 메시지 나타내기 (deprecated API)
    [TCGBUtil showToastWithMessage:@"TOAST MESSAGE" duration:3];
    
    // 길게(3.5초) 메시지 나타내기
    [TCGBUtil showToastWithMessage:@"TOAST MESSAGE with enum long" length:GamebaseToastLengthLong]; 
    
    // 짧게(2초) 메시지 나타내기
    [TCGBUtil showToastWithMessage:@"TOAST MESSAGE with enum short" length:GamebaseToastLengthShort];
}
```
