## Game > Gamebase > iOS SDK 사용 가이드 > UI

## GameNotice

콘솔에 이미지와 함께 등록한 공지 사항을 표시하는 기능입니다.

![GameNotice Example](https://static.toastoven.net/prod_gamebase/DevelopersGuide/gameNotice_guide_001.png) 
![GameNotice Example](https://static.toastoven.net/prod_gamebase/DevelopersGuide/gameNotice_guide_002.png)

### Open GameNotice

게임 공지를 화면에 표시합니다.

#### Required 파라미터
* viewController: 게임 공지가 노출되는 ViewController입니다.
 
#### Optional 파라미터
* completion: 게임 공지가 종료될 때 사용자에게 콜백으로 알려 줍니다.

**API**

```objectivec
+ (void)openGameNoticeWithViewController:(nullable UIViewController *)viewController
                              completion:(nullable void(^)(TCGBError * _Nullable))completion;
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| TCGB\_ERROR\_NOT\_INITIALIZED | 1 | Gamebase가 초기화되어 있지 않습니다. |
| TCGB\_ERROR\_UI\_GAME\_NOTICE\_FAIL\_INVALID\_URL | 6941 | 게임 공지 URL 생성에 실패했습니다. |
| TCGB\_ERROR\_WEBVIEW\_TIMEOUT | 7002 | 약관 웹뷰 표시 중 타임아웃이 발생했습니다. |
| TCGB\_ERROR\_WEBVIEW\_HTTP\_ERROR | 7003 | 약관 웹뷰 오픈 중 HTTP 에러가 발생하였습니다. |

**Example**

```objectivec
- (void)openGameNotice {
    void(^completion)(TCGBError *) = ^(TCGBError *error) {
        // Called when the entire gameNotice is closed.
        NSLog(@"GameNotice closed");
    };

    [TCGBGameNotice openGameNoticeWithViewController:self completion:completion];
}
```
