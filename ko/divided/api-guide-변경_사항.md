## Game > Gamebase > API v1.3 가이드

## 변경 사항
- IAP(in app purchase) API의 요청 파라미터 및 응답 결과 항목 추가 및 삭제
- `Push Wrapping` API 추가
- Gamebase Access Token으로 로그인 시 사용된 IdP의 프로필 및 토큰 정보를 획득할 수 있는 `Get IdP Token and Profiles` API 추가
- IdP Id로 매핑된 Gamebase userId를 획득하는 `Get UserId Information with IdP Id` API 추가
- 특정 기간 동안 탈퇴한 유저의 Gamebase userId를 획득하는 `Withdraw Histories` API 추가
- 이용 정지 및 이용 정지 해제를 수행하는 `Ban`, `Ban Release` API 추가
- 결제 트랜잭션을 조회하는 `Get Payment Transaction` API 추가
- 미소비 결제 내역을 조회하는 `List Consumables` API에 한 번에 N개의 스토어를 대상으로 조회할 수 있도록 `marketIds` 추가
- 서버 주소가 https://api-gamebase.nhncloudservice.com으로 변경. 기존 주소도 별도의 공지 전까지 유지
- `List Active Subscriptions` API 응답 결과에 구독 상품 취소/재구매 시 원거래 구독의 마켓 결제 번호를 나타내는 `linkedPaymentId` 추가
- 구독 중인 상품을 취소하는 `Cancel Subscriptions`, `Revoke Subscriptions` API 추가
- `List Active Subscriptions` API request body에 구글 구독 비활성 상태를 요청할 수 있는 `includeInactiveGoogleStatuses` 추가
- `List Active Subscriptions` API 응답 결과에 RENEWED/RECOVERED 발생 시간을 나타내는 `renewTime` 추가
- `List Active Subscriptions` API request에 한 번에 N개의 스토어를 대상으로 조회할 수 있도록 `marketIds` 추가
- 이용 정지 상태의 유저를 조회하는 `Get Ban Members` API 추가
- 구독의 현재 상태를 조회하는 `Get Subscriptions Status` API 추가
- `Get Payment Transaction` API request body에 ONEStore의 purchaseId 혹은 purchaseToken 값을 나타내는 `paymentToken` 추가
- `Withdraw Histories` API의 요청 파라미터에 eventLogType/includePending 추가
- `SIWA Account Webhook` API 추가
- `Get Coupon Information by Coupon Code` API 추가
