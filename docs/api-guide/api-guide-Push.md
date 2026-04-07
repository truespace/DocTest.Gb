---
source: api-guide.md
split: true
created_date_time: 20260406_141859
keyword: "Server API, Push, Notification, Contact"
section: Push
order: 11
---

## Push

Gamebase는 NHN Cloud Push 서비스의 서버 API에 대해 **Wrapping** 기능을 제공합니다. Wrapping 기능을 사용하면 사용자 서버에서 일관된 인터페이스로 NHN Cloud 서비스들을 사용할 수 있습니다.

> [참고]
> Gamebase를 활성화 하면 Push Appkey 설정 없이 Gamebase Wrapping API를 호출하여 Push 기능을 사용할 수 있습니다.


<br>

#### Wrapping API
|    | API | Method | Wrapping URI | Push URI |
| --- | --- | --- | --- | --- |
| 메시지 | 발송 | POST | /tcgb-push/v1.3/apps/{appId}/messages | /push/v2.4/appkeys/{appkey}/messages |
|   | 조회 | GET | /tcgb-push/v1.3/apps/{appId}/messages | /push/v2.4/appkeys/{appkey}/messages |
|   | 발송 로그 조회 | GET | /tcgb-push/v1.3/apps/{appId}/logs/message | /push/v2.4/appkeys/{appkey}/logs/message |
| 예약 메시지 | 발송 스케줄 생성 | POST | /tcgb-push/v1.3/apps/{appId}/schedules | /push/v2.4/appkeys/{appkey}/schedules |
|   | 생성 | POST | /tcgb-push/v1.3/apps/{appId}/reservations | /push/v2.4/appkeys/{appkey}/reservations |
|   | 목록 조회 | GET | /tcgb-push/v1.3/apps/{appId}/reservations | /push/v2.4/appkeys/{appkey}/reservations |
|   | 단건 조회 | GET | /tcgb-push/v1.3/apps/{appId}/reservations/{reservation-id} | /push/v2.4/appkeys/{appkey}/reservations/{reservation-id} |
|   | 발송 완료 조회 | GET | /tcgb-push/v1.3/apps/{appId}/reservations/{reservation-id}/messages | /push/v2.4/appkeys/{appkey}/reservations/{reservation-id}/messages |
|   | 수정 | PUT | /tcgb-push/v1.3/apps/{appId}/reservations/{reservationId} | /push/v2.4/appkeys/{appkey}/reservations/{reservationId} |
|   | 삭제 | DELETE | /tcgb-push/v1.3/apps/{appId}/reservations | /push/v2.4/appkeys/{appkey}/reservations |
| 태그 | 생성 | POST | /tcgb-push/v1.3/apps/{appId}/tags | /push/v2.4/appkeys/{appkey}/tags |
|   | 조회 | GET | /tcgb-push/v1.3/apps/{appId}/tags | /push/v2.4/appkeys/{appkey}/tags |
|   | 수정 | PUT | /tcgb-push/v1.3/apps/{appId}/tags/{tagId} | /push/v2.4/appkeys/{appkey}/tags/{tag-id} |
|   | 삭제 | DELETE | /tcgb-push/v1.3/apps/{appId}/tags/{tagId} | /push/v2.4/appkeys/{appkey}/tags/{tag-id} |
| UID | 생성 | POST | /tcgb-push/v1.3/apps/{appId}/uids/{uid}/tag-ids | /push/v2.4/appkeys/{appkey}/uids/{uid}/tag-ids |
|   | 조회 | GET | /tcgb-push/v1.3/apps/{appId}/uids/{uid}/tag-ids | /push/v2.4/appkeys/{appkey}/uids/{uid}/tag-ids |
|   | 수정 | PUT | /tcgb-push/v1.3/apps/{appId}/uids/{uid}/tag-ids | /push/v2.4/appkeys/{appkey}/uids/{uid}/tag-ids |
|   | 태그 삭제 | DELETE | /tcgb-push/v1.3/apps/{appId}/uids/{uid}/tag-ids | /push/v2.4/appkeys/{appkey}/uids/{uid}/tag-ids |

<br/>

**해당 API에 대한 상세 설명은 다음 링크를 참고하시기 바랍니다.**
Gamebase Wrapping API와 매핑된 Push API 스펙은 아래 가이드를 참고하십시오.
Push Appkey 설정 없이 Gamebase AppId 및 SecretKey를 이용하여 Gamebase Wrapping Push API를 호출할 수 있습니다.

> [참고 1]
> Push 가이드에 존재하는 uid 값은 gamebase userId 값을 사용할 수 있습니다. 클라이언트 SDK에서 푸시 토큰 등록 시 유저 식별자는 gamebase userId로 등록되어 있습니다.
> 한 명의 유저가 다수의 단말기에서 모두 푸시 수신을 허용하였다면, 다수의 단말기에서 모두 푸시를 수신하게 됩니다.

> [참고 2]
> API를 통해 푸시 메시지를 발송한 경우 발송 내역은 Gamebase Console의 **푸시 > 발송 이력**에서 확인할 수 없습니다.
> **푸시 > 설정 > 발송 내역 저장** 메뉴에서 **Log & Crash** 설정을 통해 확인할 수 있습니다.

[Push Guide](https://docs.nhncloud.com/ko/Notification/Push/ko/api-guide/)

<br/>

##### API 호출 예시

```
POST https://api-gamebase.nhncloudservice.com/tcgb-push/v1.3/apps/{appId}/messages

Content-Type: application/json
X-TCGB-Transaction-Id: 88a1ae42-6b1d-48c8-894e-54e97aca07fq
X-Secret-Key: IgsaAP

{
    "target" : {
        "type" : "UID",
        "to": ["gamebase userId-1", "gamebase userId-2"]
    },
    "content" : {
        "default" : {
            "title": "title",
            "body": "body"
        }
    },
    "messageType" : "AD",
    "contact": "1588-1588",
    "removeGuide": "메뉴 > 설정",
    "timeToLiveMinute": 1,
    "provisionedResourceId": "id",
    "adWordPosition": "TITLE"
}
```

<br/>
<br/>
