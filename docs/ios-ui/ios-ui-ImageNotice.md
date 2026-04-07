---
source: ios-ui.md
split: true
created_date_time: 20260406_141859
keyword: "ImageNotice, Show ImageNotices, Custom ImageNotices, Close ImageNotices"
section: ImageNotice
order: 2
---

## ImageNotice

콘솔에 이미지를 등록한 후 사용자에게 공지를 띄울 수 있습니다.

![ImageNotice Example](./image/imageNotice-guide-landscape-ko_v3.png)
<!-- LLM_Image_DESC_20260406
    유형: UI
    내용: 이미지 공지 팝업 예시 (가로 모드)
    구성: 게임 성공을 위한 맞춤 패키지 NHN GamePlatform 홍보 이미지가 팝업으로 표시됨. 좌우 화살표로 이미지 넘기기 가능, 하단에 '오늘은 그만 보기' 체크박스와 '닫기' 버튼이 위치
    Keyword: 이미지공지, ImageNotice, 팝업, 가로모드, GamePlatform
-->

### Show ImageNotices

이미지 공지를 화면에 띄워 줍니다.

#### Required 파라미터
* viewController: 이미지 공지가 노출되는 ViewController입니다.
 
#### Optional 파라미터
* configuration: TCGBImageNoticeConfiguration으로 배경색 등 이미지 공지 설정을 변경할 수 있습니다.
* closeCompletion: 이미지 공지가 전체 종료될 때 사용자에게 콜백으로 알려 줍니다.
* schemeEvent: 이미지를 클릭했을 때, 콘솔에 등록한 payload를 콜백으로 알려 줍니다.

**API**

```objectivec
+ (void)showImageNoticesWithViewController:(nullable UIViewController *)viewController
                            closeCompletion:(void(^ _Nullable)(TCGBError * _Nullable error))closeCompletion;

+ (void)showImageNoticesWithViewController:(nullable UIViewController *)viewController
                             configuration:(nullable TCGBImageNoticeConfiguration *)configuration
                           closeCompletion:(void(^ _Nullable)(TCGBError * _Nullable error))closeCompletion
                               schemeEvent:(void(^ _Nullable)(NSString * _Nullable payload, TCGBError * _Nullable error))schemeEvent;
```

**ErrorCode**

| Error | Error Code | Description |
| --- | --- | --- |
| TCGB\_ERROR\_NOT\_INITIALIZED | 1 | Gamebase가 초기화되어 있지 않습니다. |
| TCGB\_ERROR\_UI\_IMAGE\_NOTICE\_TIMEOUT | 6901 | 이미지 공지 팝업 창 표시 중 시간이 초과되어 모든 팝업 창을 강제 종료합니다. |
| TCGB\_ERROR\_SERVER\_INVALID\_RESPONSE | 8003 | 서버가 유효하지 않은 응답을 반환했습니다. | 

**Example**

```objectivec
- (void)showImageNotices {
    void(^closeCompletion)(TCGBError *) = ^(TCGBError *error) {
        // Called when the entire imageNotice is closed.
        NSLog(@"ImageNotices closed");
    };

    void(^schemeEvent)(NSString *, TCGBError *) = ^(NSString *payload , TCGBError *error) {
        // Called when image click event occurred.
        NSLog(@"Image click event occurred: %@", payload);
    };

    [TCGBImageNotice showImageNoticesWithViewController:self configuration:nil closeCompletion:closeCompletion schemeEvent:schemeEvent];
}
```

### Custom ImageNotices

사용자 설정 이미지 공지를 화면에 띄워 줍니다.
TCGBImageNoticeConfiguration으로 사용자 설정 이미지 공지를 만들 수 있습니다.

**Example**

```objectivec
- (void)showImageNotices {
    void(^closeCompletion)(TCGBError *) = ^(TCGBError *error) {
        // Called when the entire imageNotice is closed.
        NSLog(@"ImageNotices closed");
    };

    void(^schemeEvent)(NSString *, TCGBError *) = ^(NSString *payload , TCGBError *error) {
        // Called when image click event occurred.
        NSLog(@"Image click event occurred: %@", payload);
    };

    TCGBImageNoticeConfiguration *configuration = [[TCGBImageNoticeConfiguration] alloc] init];
    configuartion.backgroundColor = [UIColor colorWithRed:0 green:0 blue:0 alpha:0.5];
    configuartion.timeoutInterval = 5000;
    configuartion.enableAutoCloseByCustomScheme = YES;

    [TCGBImageNotice showImageNoticesWithViewController:self configuration:configuration closeCompletion:closeCompletion schemeEvent:schemeEvent];
}
```


#### TCGBImageNoticeConfiguration

| Parameter                              | Values                                   | Description        |
| -------------------------------------- | ---------------------------------------- | ------------------ |
| backgroundColor                  | UIColor     | 이미지 공지 뒷 배경색<br/>**default**: [UIColor colorWithRed:0 green:0 blue:0 alpha:0.5]         |
| timeoutMS                  | long        | 이미지 공지 최대 로딩 시간(단위: millisecond)<br/>**default**: 5000                     |
| enableAutoCloseByCustomScheme    | YES or NO   | 커스텀 스킴 이벤트 발생 시 공지 전체 닫기 또는 다음 공지 표시<br/>**default**: YES         |


### Close ImageNotices

closeImageNotices API를 호출하여 현재 표시 중인 이미지 공지를 모두 종료할 수 있습니다.

**API**

```objecgivec
+ (void)closeImageNoticesWithViewController:(nullable UIViewController *)viewController;
```

**Example**

```objectivec
- (void)closeImageNotices {
    [TCGBImageNotice closeImageNoticesWithViewController:self];
}
```
