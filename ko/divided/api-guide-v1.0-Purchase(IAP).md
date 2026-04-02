## Game > Gamebase > API v1.0 가이드

## Purchase(IAP)

Gamebase는 NHN Cloud IAP 서비스의 서버 API에 대해 **Wrapping** 기능을 제공합니다. Wrapping 기능을 사용하면 사용자 서버에서 일관된 인터페이스로 NHN Cloud 서비스들을 사용할 수 있습니다.


#### Wrapping API

| API | Method | Wrapping URI | IAP URI |
| --- | --- | --- | --- |
| 아이템 소비 | POST | /tcgb-inapp/v1.0/apps/{appId}/consume/{paymentSeq}/items/{itemSeq} | /inapp/v3/consume/{paymentSeq}/items/{itemSeq} |
| 아이템 조회 | GET | /tcgb-inapp/v1.0/apps/{appId}/item/list/{appSeq} | /standard/item/list/{appSeq} |
| 미소비 결제 내역 조회| POST | /tcgb-inapp/v1.0/apps/{appId}/consumable/list | /standard/inapp/v1/consumable/list |

**해당 API에 대한 상세 설명은 다음 링크를 참고하시기 바랍니다.**

```
해당 API 들은 IAP에서 deprecated 되었습니다.
```

##### API 호출 예시

```
Content-Type: application/json
X-TCGB-Transaction-Id: 88a1ae42-6b1d-48c8-894e-54e97aca07fq
X-Secret-Key: IgsaAP

POST https://api-gamebase.cloud.toast.com/tcgb-inapp/v1.0/apps/{appId}/consume/{paymentSeq}/items/{itemSeq}
```
