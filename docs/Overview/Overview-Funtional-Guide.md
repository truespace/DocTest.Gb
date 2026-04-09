---
source: Overview.md
section: "Funtional Guide"
order: 6
split: true
created_date_time: 20260408_184906
keyword: Login, Logout, Mapping, Withdraw, Purchase, Android, iOS, Overview
---

## Funtional Guide

| Feature               | Description                              | Client                                   | Server                                   | Console                                  |
| --------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Analytics                  | 실시간, 매출, 이용자, 밸런싱 지표 제공<br>레벨별, 서버별 지표 제공 | [[Android](../aos-etc.md#analytics)] [[iOS](../ios-etc.md#analytics)] [[Unity](../unity-etc.md#analytics)] |                                          | [[Analytics]](../oper-analytics.md)  ||
| Login                 | 게스트, 3rd Party 인증 지원  <br> - [지원되는 IdP](./Overview-Key-Features.md#authentication) |  [[Android](../aos-authentication.md#login)] [[iOS](../ios-authentication.md#login)] [[Unity](../unity-authentication.md#login)] | [[토큰 검증](../api-guide.md#token-authentication)] <br> [[회원 조회](../api-guide.md#get-member)] | [[App] > 인증 정보 설정](../oper-app.md#authentication-information) <br> [[Member] > 회원 조회](../oper-member.md#member) <br> - 기본 정보, 로그인 이력, 플레이 시간, 결제 이력 등 |
| Logout                | 로그아웃                                     | [[Android](../aos-authentication.md#logout)]  [[iOS](../ios-authentication.md#logout)] [[Unity](../unity-authentication.md#logout)] |                                          |                                          |
| Withdraw              | 게임 탈퇴 <br> -  게임 이용자의 사용자 ID, 매핑 정보 등 모든 정보 삭제 | [[Android](../aos-authentication.md#withdraw)] [[iOS](../ios-authentication.md#withdraw)] [[Unity](../unity-authentication.md#withdraw)] |                                          |                                          |
| Mapping               | 하나의 사용자 ID에 여러 개의 IdP를 연동하는 기능           | [[Android](../aos-authentication.md#mapping)] [[iOS](../ios-authentication.md#mapping)] [[Unity](../unity-authentication.md#mapping)] |                                          |
| Purchase(IAP)         | 인앱 결제  | [[Android](../aos-purchase.md#purchase)] [[iOS](../ios-purchase.md#purchase)] [[Unity](../unity-purchase.md#purchase)] | [[API](../api-guide.md#purchaseiap)] | [[Purchase]](../oper-purchase.md#app)<br> [- 아이템 등록](../oper-purchase.md#item) <br> [- 결제 정보 조회](../oper-purchase.md#transactions) |
| Push                  | (NHN Cloud 서비스 연동) <br> 푸시 메시지 전송 및 결과 확인 | [[Android](../aos-push.md#push)] [[iOS](../ios-push.md#push)] [[Unity](../unity-push.md#push)] |                                          | [[Push]](../oper-push.md#push) <br/>- 실시간, 예약 푸시 발송 |
| Leaderboard           | 실시간 대용량 랭킹 조회 및 등록 |                                          | [[API](../api-guide.md#leaderboard)] |                                          |
| Webview               | SDK에서 기본적인 웹뷰 UI를 제공<br/>시스템 팝업, 토스트(toast) UI 제공 | [[Android](../aos-ui.md#webview)] [[iOS](../ios-ui.md#webview)] [[Unity](../unity-ui.md#webview)] |                                          |                                          |
| [Operator] Maintenance | (운영) 점검 기능                               |                                          | [[점검 여부 확인](../api-guide.md#maintenance)] | [[Maintenance]](../oper-operation.md#maintenance)<br>- 점검 등록, 점검 해제 |
| [Operator] Notice      | (운영) 긴급 공지 기능 <br> -  게임 이용자가 앱을 실행할 때 팝업 형태로 공지 확인 가능 |                                          |                                          | [[Notice]](../oper-operation.md#notice) <br/>- 공지 등록 |
| [Operator] Image Notice         | (운영) 이미지 공지 기능 <br> -  게임내 팝업 형태의 이미지 공지 노출 | [[Android](../aos-ui.md#imagenotice)] [[iOS](../ios-ui.md#imagenotice)] [[Unity](../unity-ui.md#imagenotice)] <br/> - 이미지 공지 노출 |                             | [[Image Notice]](../oper-operation.md#image-notice) <br/>- 이미지 공지 관리 |
| [Operator] Ban         | (운영) 게임 이용자의 이용 정지 등록 및 해제 <br> -  게임 이용자의 이용 정지 등록 및 해제 | [[Android](../aos-authentication.md#get-banned-user-information)] [[iOS](../ios-authentication.md#get-banned-user-information)] [[Unity](../unity-authentication.md#get-banned-user-infomation)] <br/> - 이용 정지 게임 이용자 정보 확인 |    [[게임 이용자의 이용정지 이력조회](../api-guide.md#ban-histories)]                                      | [[Ban]](../oper-ban.md#ban) <br/>- 이용 정지 등록 및 해제 |
| [Operator] Coupon         | (운영) 쿠폰 관리<br>- 발급, 이력 조회 |  |                                      [[쿠폰 유효성 검증 및 쿠폰 상태 변경](../api-guide.md#coupon)  | [[Coupon]](../oper-coupon.md) <br/>- 쿠폰 발급 |
| [Operator] Customer Service         | (운영) 1:1 문의 접수 및 처리 <br> -  FAQ, 공지사항 관리 | [[Android](../aos-etc.md#contact)] [[iOS](../ios-etc.md#contact)] [[Unity](../unity-etc.md#contact)] <br/> - 고객 센터 웹페이지를 웹뷰로 표시 |                                        | [[Customer Service]](../oper-customer-service.md) <br/>- 고객 센터 문의 처리<br>- FAQ/공지 관리 |
