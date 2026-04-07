---
source: api-guide-v1.2.md
split: true
created_date_time: 20260406_141859
keyword: "Gamebase, API v1.2 가이드, 변경 사항"
section: "변경 사항"
order: 1
---

## Game > Gamebase > API v1.2 가이드

## 변경 사항
- IAP(in app purchase) API가 변경되었습니다.
- Get Simple Launching API 호출 시 필수 파라미터로 storeCode가 추가되었습니다.
- Check Maintenance API 응답 결과에 점검 대상에 대한 storeCode 정보가 추가되었습니다.
- GUEST 계정의 단말기 이전에 사용되는 TransferAccount에 대해, 사전에 발급된 TransferAccount를 검증할 수 있는 Validate TransferAccount API가 추가되었습니다.
- API 응답 결과의 date 타입이 Epoch time에서 ISO 8601 형식(yyyy-MM-dd'T'HH:mm:ssXXX)으로 변경되었습니다. Token Authentication, Get Member, Get Members API 응답 결과의 regDate, lastLoginDate 항목
- 쿠폰 소진 API가 추가되었습니다.
- 사용자 탈퇴 API가 추가 되었습니다.
- Purchase(IAP)의 구매 가격(price) 데이터 타입이 가이드상에서 Long 으로 잘못 표기된 것을 Float 타입으로 변경하였습니다.
- 탈퇴 유예 기능 추가에 따라 Token Authentication, Get Member API 응답 결과에 탈퇴 유예 상태인 사용자에 대한 정보가 추가 되었습니다.
