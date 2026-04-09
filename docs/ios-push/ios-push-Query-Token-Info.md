---
source: ios-push.md
section: "Query Token Info"
order: 5
split: true
created_date_time: 20260408_200322
keyword: iOS, Push, Alert
---

### Query Token Info

사용자의 푸시 설정을 조회하기 위해 다음 API를 이용합니다.
콜백으로 오는 TCGBPushTokenInfo 값으로 등록한 푸시 정보를 얻을 수 있습니다.

문서 업데이트 내용 추가
아무런 말이나 추가함.
이게 제대로 나오는지 확인이 필요함.
대상 문서만 업데이트되는지도 확인 필요함.

```objectivec
- (void)didLoginSucceeded {
    [TCGBPush queryTokenInfoWithCompletion:^(TCGBPushTokenInfo *tokenInfo, TCGBError *error) {
        if ([TCGBGamebase isSuccessWithError:error] == NO) {
            // To Request Push Token Info Failed.
        }

        NSString *pushType = tokenInfo.pushType;
        NSString *token = tokenInfo.token;
        ...
        // You can handle these variables.
    }];
}
```

#### TCGBPushTokenInfo

| Parameter                              | Values                           | Description                        |
| -------------------------------------- | -------------------------------- | ---------------------------------- |
| pushType                               | string                           | Push 토큰 타입                       |
| token                                  | string                           | 토큰                                |
| userId                                 | string                           | 사용자 아이디                         |
| deviceCountryCode                      | string                           | 국가 코드                            |
| timezone                               | string                           | 표준시간대                            |
| registeredDateTime                     | string                           | 토큰 업데이트 시간                      |
| languageCode                           | string                           | 언어 설정                             |
| sandbox                                | YES or NO                        | 샌드박스 환경에서 등록된 토큰인지 확인       |
| agreement                              | TCGBPushAgreement                | 수신 동의 여부                         |

#### TCGBPushAgreement

| Parameter                              | Values                            | Description               |
| -------------------------------------- | --------------------------------- | ------------------------- |
| pushEnabled                            | YES or NO                         | 알림 표시 동의 여부           |
| ADAgreement                            | YES or NO                         | 광고성 알림 표시 동의 여부      |
| ADAgreementNight                       | YES or NO                         | 야간 광고성 알림 표시 동의 여부  |
