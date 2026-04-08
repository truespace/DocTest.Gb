---
source: api-guide-v1.2.md
section: "Advance Notice"
order: 2
split: true
created_date_time: 20260408_191848
keyword: Server API, Console, Api
---

## Advance Notice

Gamebase Server API는 RESTful 형식으로, 서버 API를 사용하기 위해서는 다음 정보들을 알고 있어야 합니다.

#### Server Address

API를 호출하기 위한 서버 주소는 다음과 같습니다. 해당 주소는 Gamebase Console 화면에서도 확인 가능합니다.
> https://api-gamebase.cloud.toast.com

![image alt](./image/pre_server_address_v1.2.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: 서버 주소 사전 설정 화면
    구성: API 서버 주소 사전 등록/설정 화면
    Keyword: Server, API, Screenshot, Server Address
-->

#### AppId

앱 ID는 NHN Cloud 프로젝트 ID로 앱 메뉴 화면에서 확인할 수 있습니다.
![image alt](./image/pre_appId_v1.2.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: AppId 관련 화면
    구성: AppId 관련 스크린샷
    Keyword: Screenshot, AppId
-->

#### SecretKey

비밀 키(secret key)는 API에 대한 접근 제어 방안으로, Gamebase Console에서 확인할 수 있습니다. 비밀 키는 Server API를 호출할 때 HTTP 헤더에 필수로 설정해야 합니다.
> [참고]
> 비밀 키가 외부에 노출되어 잘못된 호출이 발생한다면 **생성** 버튼을 클릭하여 새로운 비밀 키를 만든 후, 새 비밀 키를 사용하면 됩니다.

![image alt](./image/pre_secret_key_v1.2.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: SecretKey 관련 화면
    구성: SecretKey 관련 스크린샷
    Keyword: Screenshot, SecretKey
-->

#### TransactionId

API를 호출하는 서버에서 내부적으로 API 요청을 관리할 수 있는 방안으로 TransactionId 기능을 제공합니다. 호출하는 서버에서 HTTP 헤더에 트랜잭션 ID를 설정하여 API를 호출하면, Gamebase 서버는 응답 HTTP Header 및 응답 결과의 Response Body Header에 해당 TransactionId를 설정하여 결과를 전달합니다.
