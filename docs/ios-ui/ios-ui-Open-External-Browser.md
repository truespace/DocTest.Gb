---
source: ios-ui.md
section: "Open External Browser"
order: 5
split: true
created_date_time: 20260408_184906
keyword: iOS, Ios, Ui
---

## Open External Browser

다음 API를 사용해 외부 브라우저를 열 수 있습니다. 파라미터로 전송되는 URL은 유효한 값이어야 합니다.

```objectivec
// Open the url with Browser
- (void)openWebBrowser:(id)sender {
    NSString* urlString = @"https://www.toast.com/";
    [TCGBWebView openWebBrowserWithURL:urlString];
}
```
