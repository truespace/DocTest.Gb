## Game > Gamebase > 콘솔 사용 가이드 > 앱

### 고객센터
고객센터 관련 설정을 진행할 수 있습니다.
현재 Gamebase에서는 3가지의 고객센터 형식을 제공하고 있으며 선택되는 고객센터 유형별로 설정할 수 있는 항목이 다릅니다.
각 고객센터 유형별 설정은 아래와 같습니다.

#### 1. 개발사 자체 고객센터
![gamebase_app_06_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_06_ko_240105.png)
개발사에서 자체적으로 고객센터를 사용하고 있을 경우 설정합니다.
설정 항목은 아래와 같습니다.
* **고객센터 URL**: 현재 제공하거나 사용하고 있는 개발사의 자체 고객센터 주소를 입력합니다.
* **연락처**: 고객센터 연락처를 입력합니다. 이 정보는 Gamebase SDK를 통해 전달받을 수 있습니다.

#### 2. Gamebase 제공 고객센터
![gamebase_app_07_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_07_ko_240105.png)
Gamebase에서 제공하는 고객센터 기능을 사용하고자 할 때 설정합니다.
설정 항목은 아래와 같습니다.
* **고객센터 URL**: 고객에게 문의를 인입받을 수 있는 페이지 정보를 제공합니다. 해당 URL은 Gamebase 제공 고객센터를 선택할 경우 자동으로 생성되며 이 URL을 통해 고객의 문의를 별도의 웹페이지를 통해 전달받을 수 있습니다.
* **연락처**: 고객센터 연락처를 입력합니다. 이 정보는 Gamebase SDK를 통해 전달받을 수 있습니다.
* **지원 언어**: 고객센터 사용자에게 지원할 언어를 선택합니다. 프로젝트 자체 언어 설정과는 별도로 설정되며 한국어, 영어, 일본어, 중국어(간체), 중국어(번체), 러시아어를 지원합니다. 원하는 지원 언어가 없을 경우, 고객센터로 문의하시기 바랍니다.
* **기본 언어**: 지원 언어에서 선택한 항목 중 고객센터 내에서 기본으로 제공할 언어를 선택합니다.

#### 3. NHN Cloud 조직 상품(Online Contact)
![gamebase_app_08_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_08_ko_240105.png)
NHN Cloud에서 조직별로 제공되는 Online contact 상품을 사용하는 경우 설정합니다.
설정 항목은 아래와 같습니다.
* **고객센터 URL**: NHN Cloud Online Contact에서 제공되는 주소를 입력합니다. 해당정보는 NHN Cloud Online Contact에 접속하여 확인할 수 있습니다.
* **연락처**: 고객센터 연락처를 입력합니다. 이 정보는 Gamebase SDK를 통해 추가로 정보를 전달받을 수 있습니다.
* **OC 조직 Key**: NHN Cloud Online Contact 고객센터 문의를 확인하기 위한 Key를 입력합니다. 해당정보를 입력하지 않을 경우 고객센터 페이지 내에서 인입된 문의를 확인할 수 없으므로 확인 후 입력해야 합니다. 자세한 연동 방법은 아래 참고내용을 보시고 연동해주시면 됩니다.
> [참고] NHN Cloud Online Contact와 Gamebase간의 연동
> Gamebase내에서 NHN Cloud Online Contact 연동하고자 할 경우 아래 과정에 따라 SSO 로그인 API Key를 발급받아 Gamebase내에 설정해주셔야 고객센터 서비스를 정상적으로 이용할 수 있습니다.
> 고객센터의 안정적인 서비스 제공을 위해 아래 순서대로 참고하시어 진행 해주시기 바랍니다.
>
> 1) NHN Cloud Online Contact에 회원 연동 방식 설정
> 서비스 관리 -> 헬프센터 -> 회원 연동
> ![gamebase_app_09_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_09_ko_240105.png)
> 회원 연동 활성화: 활성화
> 로그인 타입: GET 방식
> Token 검증 URL: https://web-gamebase.nhncloud.com/tcgb-web/v1.0/apps/{appId}/online-contact/login-status
> **{appId}** 부분은 설정하고자 하는 Gamebase의 프로젝트 ID를 확인하신 후 해당 위치에 입력해주시면 됩니다.
>
> 2) OC 조직 Key를 획득하여 OC 조직 Key항목에 입력
> 전체 관리 -> 계약 서비스 현황 -> 조직 정보로 이동한 후 OC 조직 정보의 OC 조직 Key를 복사하여 Gamebase OC 조직 Key 항목에 입력
> ![gamebase_app_10_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_10_ko_240105.png)
>
> 3) NHN Cloud Online contact 고객센터 페이지 주소를 획득하여 고객센터 URL에 입력
> 헬프센터 -> 하위메뉴 선택 -> 우측 위 헬프센터 바로가기 클릭
> ![gamebase_app_11_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_11_ko_240105.png)
> 브라우저 상단에 표시된 주소를 Gamebase 고객센터 URL 항목에 입력
> ![gamebase_app_12_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_12_ko_240105.png)
>
