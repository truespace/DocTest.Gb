## Game > Gamebase > iOS SDK 사용 가이드 > UI

## Open External Browser

다음 API를 사용해 외부 브라우저를 열 수 있습니다. 파라미터로 전송되는 URL은 유효한 값이어야 합니다.

```objectivec
// Open the url with Browser
- (void)openWebBrowser:(id)sender {
    NSString* urlString = @"https://www.toast.com/";
    [TCGBWebView openWebBrowserWithURL:urlString];
}
```
