---
source: api-guide.md
split: true
created_date_time: 20260406_141859
keyword: Leaderboard
section: Leaderboard
order: 10
---

## Leaderboard

Gamebase는 NHN Cloud Leaderboard 서비스의 서버 API에 대해 **Wrapping** 기능을 제공합니다. Wrapping 기능을 사용하면 사용자 서버에서 일관된 인터페이스로 NHN Cloud 서비스들을 사용할 수 있습니다.

> [참고]
> Gamebase를 활성화 하면 Leaderboard Appkey 설정 없이 Gamebase Wrapping API를 호출하여 Leaderboard 기능을 사용할 수 있습니다.

<br>

#### Wrapping API
| API | Method | Wrapping URI | Leaderboard URI |
| --- | --- | --- | --- |
| Factor에 등록된 유저 수 조회<br>- Get user count in factor | GET | /tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/user-count | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/user-count |
| Factor 전체 수 검색<br>- Get total factor count | GET | /tcgb-leaderboard/v1.3/apps/{appId}/factor-count | /leaderboard/v2.0/appkeys/{appKey}/factor-count |
| Factor 정보 조회<br>- Get factor info<br>- Get multiple factor info | GET | /tcgb-leaderboard/v1.3/apps/{appId}/factors | /leaderboard/v2.0/appkeys/{appKey}/factors |
| 단일 유저 점수/순위 조회<br>- Get single user info | GET | /tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/users?userId={userId} | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users?userId={userId} |
| 다수 유저 점수/순위 조회<br>- Get multiple user info | POST | /tcgb-leaderboard/v1.3/apps/{appId}/get-users | /leaderboard/v2.0/appkeys/{appKey}/get-users |
| 일정 범위의 전체 점수/순위 조회<br>- Get multiple user info by range | GET | /tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/users?start={start}&size={size} | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users?start={start}&size={size} |
| 특정 순위의 유저들을 검색<br>- Get selected rank user info | POST | /tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/users | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users |
| 특정 유저의 순위 및 상위, 하위 유저들의 순위 검색<br>- Get multiple user info by pivot user | GET | /tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/users?userId={userId}&prevSize={prevSize}&nextSize={nextSize} | /leaderboard/v2.0/appkeys/{appkey}/factors/{factor}/users?userId={userId}&prevSize={prevSize}&nextSize={nextSize} |
| 단일 유저 점수 등록<br>- Set single user score | POST | /tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/users/{userId}/score | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users/{userId}/score |
| 단일 유저 점수/ExtraData 등록<br>- Set single user score with extra data | POST | /tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/users/{userId}/score-with-extra | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users/{userId}/score-with-extra |
| 다수 유저 점수 등록<br>- Set multiple user score | POST | /tcgb-leaderboard/v1.3/apps/{appId}/scores | /leaderboard/v2.0/appkeys/{appKey}/scores |
| 다수 유저 점수/ExtraData 등록<br>- Set multiple user score with extra data | POST | /tcgb-leaderboard/v1.3/apps/{appId}/scores-with-extra | /leaderboard/v2.0/appkeys/{appKey}/score-with-extra |
| 유저 Leaderboard 정보 삭제<br>- Delete single user info<br>- Delete multiple user info | DELETE | /tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/users | /leaderboard/v2.0/appkeys/{appKey}/factors/{factor}/users |

<br/>

**해당 API에 대한 상세 설명은 다음 링크를 참고하시기 바랍니다.**
Gamebase Wrapping API와 매핑된 Leaderboard API 스펙은 아래 가이드를 참고하십시오.
Leaderboard Appkey 설정 없이 Gamebase AppId 및 SecretKey를 이용해서 Gamebase Wrapping Leaderboard API를 호출할 수 있습니다.


[Leaderboard Guide](https://docs.nhncloud.com/ko/Game/Leaderboard/ko/api-guide/)

<br/>

##### API 호출 예시

```
GET https://api-gamebase.nhncloudservice.com/tcgb-leaderboard/v1.3/apps/{appId}/factors/{factor}/user-count

Content-Type: application/json
X-TCGB-Transaction-Id: 88a1ae42-6b1d-48c8-894e-54e97aca07fq
X-Secret-Key: IgsaAP
```

<br/>
<br/>
