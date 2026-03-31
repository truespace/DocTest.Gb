## Game > Gamebase > 콘솔 사용 가이드 > 앱

### Test Device

![gamebase_app_13_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_13_ko_240105.png)
테스트 단말기로 등록되면 Gamebase를 사용하는 앱이 점검 중이어도 정상적으로 게임에 접근할 수 있습니다.
테스트 단말기를 등록하려면 **Device Key** 또는 **IP** 정보를 등록해야 합니다. 직접 입력하거나 **게임유저 ID**를 조회하여 등록할 수 있습니다.
점검시 게임플레이가 가능할 수 있도록 하거나 단말기별 Debug Log 출력 여부를 설정하여 테스트 단말기를 관리할 수 있습니다.
더 이상 사용하지 않는 테스트 단말기를 삭제할 수도 있습니다.
접속 이력 확인버튼을 누르면 해당 기기를 통한 **점검이 진행되는 동안의 접속 시간 및 상세 접속 로그**를 확인할 수 있습니다.
![gamebase_app_14_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_14_ko_240105.png)

> [참고]
> 테스트 단말기는 최대 100개까지만 등록할 수 있습니다.

#### (1) 조회

앱에 등록된 전체 테스트 단말기를 확인 할 수 있습니다. 검색어를 **Search**에 입력하여 검색 조건에 맞는 테스트 단말기를 찾아 볼 수 있습니다.

#### (2) 등록

조회 화면에서 **등록** 버튼을 클릭하면 테스트 단말기를 등록할 수 있는 화면이 나타납니다. **Device Key**를 직접 입력하거나 **게임유저 ID**를 검색해 테스트 단말기를 등록할 수 있습니다.

![gamebase_app_15_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_15_ko_240105.png)
![gamebase_app_16_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_16_ko_240105.png)

**(1) 게임유저 ID를 통한 등록**

타입을 유저 ID로 선택하고 게임유저 ID를 입력하여 **검색** 버튼을 클릭하면 화면 하단에 사용자의 로그인 로그 내역이 조회됩니다. 조회된 내역에서 테스트 단말기로 등록하고자 하는 Device Key를 선택하여 **추가 정보**를 입력하여 **등록** 버튼을 클릭하면 해당 Device key가 테스트 단말기 정보로 등록됩니다.



**(2)Device Key 또는 IP를 통한 등록**

등록하고자 하는 Device key 또는 IP 정보를 알고 있을 경우 타입을 원하는 입력방식으로 선택하여 직접 테스트 단말기를 등록할 수 있습니다.
등록하고자 하는 단말기의 **단말기 이름** 및 디버그 로그, 점검 무시 여부를 입력 후 등록 버튼을 누르면 테스트 단말기로 등록됩니다.

> [참고]
> 단말기 이름에는 사용자가 알아보기 편한 별칭을 입력하시면 됩니다. 예시) iPhone 6 테스트, 토스트님 아이패드

#### (3) 삭제

![gamebase_app_17_ko_240105](https://kr1-api-object-storage.nhncloudservice.com/v1/AUTH_2acdfabf4efe4efc8a04c00b348110c9/cdn_origin/prod_gamebase/ConsoleGuide/App/ko/gamebase_app_17_ko_240105.png)

테스트 단말기 조회 화면에서 삭제하고자 하는 테스트 단말기를 체크한 후 왼쪽 위의 삭제 버튼을 클릭하면 테스트 단말기 정보가 삭제됩니다. 삭제된 정보는 복구할 수 없으므로 삭제 전에 다시 한번 확인한 후 삭제하시기 바랍니다.
