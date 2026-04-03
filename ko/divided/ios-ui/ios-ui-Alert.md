---
source: ios-ui.md
section: "Alert"
order: 6
created_date: 2026-04-03
---

## Alert

시스템 알림을 표시할 수 있습니다.<br/>

#### Types of Alert
1. '확인' 버튼을 1개만 제공하며, 확인 버튼을 클릭하면 completion이 호출됩니다.
2. '확인' 버튼을 1개만 제공하며, completion을 제공하지 않습니다.

```objectivec
// 1. Alert has completion
- (void)showAlertWithCompletion:(id)sender {
    [TCGBUtil showAlertWithTitle:@"TITLE" message:@"MESSAGE" completion:^{
        NSLog(@"Tapped OK Button.");
    }];
}

// 2. Alert without completion
- (void)showAlertWitoutCompletion:(id)sender {
    [TCGBUtil showAlertWithTitle:@"TITLE" message:@"MESSAGE"];
}
```

#### Types of ActionSheet
1. 기본적으로 'Cancel' 버튼이 있는 ActionSheet을 제공합니다.
2. 'blocks'에 사용자의 AlertAction을 등록할 수 있습니다.


```objectivec
// Create ActionSheet [OK, Detail, Cancel]
- (void)showActionSheet {
    NSMutableDictionary<NSString *, void(^)(UIAlertAction *)> *blocks = [NSMutableDictionary dictionary];
    
    void(^okActionHandler)(UIAlertAction *) = ^(UIAlertAction *action){
        NSLog(@"OK");
    };
    void(^detailActionHandler)(UIAlertAction *) = ^(UIAlertAction *action){
        NSLog(@"Detail");
    };

    // Add AlertAction(Title: "OK", Handler: okActionHandler)
    [blocks setValue:okActionHandler forKey:@"OK"];

    // Add AlertAction(Title: "Detail", Handler: detailActionHandler)
    [blocks setValue:detailActionHandler forKey:@"Detail"];
    
    [TCGBUtil showActionSheetWithTitle:@"TITLE" message:@"MESSAGE" blocks:blocks];
}
```
