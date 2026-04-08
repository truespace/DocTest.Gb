---
source: api-guide.md
section: "Others"
order: 12
split: true
created_date_time: 20260408_191848
keyword: Server API, Withdraw, Purchase, Authentication, GraceBan, TemporaryWithdrawal, Android, iOS
---

## Others

### OS Code

유저 단말기의 OS에 대해 Gamebase 내부적으로 정의한 코드입니다.

| Code | 설명 |
| --- | --- |
| AOS | Android |
| IOS | iOS |
| WEB | Web |
| WINDOWS | Windows |
| MACOS | macOS |
<br/>

### Store Code

앱을 설치한 스토어에 대해 Gamebase 내부적으로 정의한 코드입니다.

| Code | 설명 |
| --- | --- |
| GG | Google Play Store |
| AS | App Store |
| ONESTORE | ONE store |
| GALAXY | Galaxy Store |
| AMAZON | Amazon Appstore |
| HUAWEI | Huawei AppGallery |
| MYCARD | Global MyCard |
| EPIC | Epic Games Store |
| STEAM | STEAM Store |
<br/>

### Identity Provider Code

유저 인증에 사용된 Identity Provider들에 대해 Gamebase 내부적으로 정의한 코드입니다.

- guest
- google
- facebook
- appleid
- iosgamecenter
- payco
- hangame
- twitter
- naver
- line
- kakaogame
- weibo
<br/>

### Member Valid Code

유저의 현재 상태에 대해 Gamebase 내부적으로 정의한 코드입니다.

| Code | 설명 |
| --- | --- |
| Y | 정상 유저 |
| D | 탈퇴된 유저 |
| B | 이용 정지된 유저 |
| T | 탈퇴 유예 상태인 유저 |
| P | 이용 정지 유예 상태인 유저 |
| M | 유실된 계정 |
<br/>


### Store Reference Status

결제 시스템(스토어의 인앱 결제, 외부 결제)이 제공하는 결제 참조 상태

| 결제 시스템 | Code | 설명 |
| --- | --- | --- |
| 구글 인앱 | PURCHASED | 구매 완료 |
| | REPURCHASED | 재구매 완료 |
| | RESTARTED | 구독 재시작 |
| | PENDING | 결제 지연 중 |
| | RENEWED | 구독 갱신 |
| | RECOVERED | 구독 복구 |
| | PAUSE_SCHEDULED | 구독 중지 예정 |
| | PAUSED | 중지 |
| | REVOKED | 환불 |
| | CANCELED_PRODUCT | 단품 결제 취소 |
| | CANCELED_SUBSCRIPTION | 구독 취소(갱신 중지)<br>- 현 회차 구독은 제공해야 함 |
| | ON_HOLD | 보류 중 |
| | IN_GRACE | 유예 중 |
| | EXPIRED | 만료 |
| | NOT_APPOINTED | 알맞은 특정 상태 없음 |
<br/>

### Withdrawal Event Type

유저 탈퇴가 어디서 발생했는지를 나타내는 이벤트 발생 경로입니다.

| Type | 설명 |
| --- | --- |
| WAA | 앱(클라이언트) 요청에 의해 계정 탈퇴 |
| WACS | 콘솔/관리자 요청에 의해 계정 탈퇴 |
| WAES | 외부 서버(게임 서버)에 의해 탈퇴<br>- 서버 탈퇴 API 호출 |
| WAAI | Apple ID 연동 삭제에 의해 탈퇴 |
| WAHI | 한게임 계정 삭제로 인한 탈퇴 |
| WAHD | 한게임 장기 미사용 계정 탈퇴 |
| WAGE | 유예 기간 만료에 따른 시스템 자동 탈퇴 |
| WAT | 탈퇴 유예 상태<br>- 최종 탈퇴 상태가 아님 |
| WAC | 탈퇴 유예 취소 |
<br/>

### Support

API 호출 실패 원인에 대한 문의 사항이 있을 경우, **API 호출 URL(HTTP body가 있는 경우는 body와 함께)과 그에 대한 응답 결과**를 [고객 센터](https://toast.com/support/inquiry)에 올려 주시면 가능한 한 빠르게 답변 드리겠습니다.

##### API 호출 예시

```
GET https://api-gamebase.nhncloudservice.com/tcgb-launching/v1.3/apps/C3JmSctU/maintenances/under-maintenance
```

##### API 실패 응답 결과

```json
{
    "header": {
        "transactionId": "18a1ae42-6b1d-54c8-894e-54e97bca07fq",
        "resultCode": -4010002,
        "resultMessage": "Gamebase product appKey is invalid, appId:C3JmSctU",
        "traceError": {
            "trackingTime": 1489726350287,
            "throwPoint": "gateway",
            "uri": "/tcgb-launching/v1.3/apps/C3JmSctU/maintenances/under-maintenance"
        },
        "isSuccessful": false
    }
}
```
