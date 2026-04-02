## Game > Gamebase > 콘솔 사용 가이드 > 앱

### GPGS Automatic Login Settings

* [GPGS(Google Play Games Services)를 이용한 자동 로그인(Automatic sign-in)](https://developer.android.com/games/pgs/signin#automatic-sign-in) 기능을 지원합니다.
    * 이 기능을 사용하기 위해서는 Android 빌드 의존성에 **gamebase-adapter-auth-gpgs-autologin** 모듈 선언 및 [추가 설정](./aos-started/#gpgs-idp)이 필요합니다.
    * 또한 *GPGS 자동 로그인 설정* 항목에 *서비스 계정 json* 정보를 입력해야 합니다.
        * ![](https://static.toastoven.net/prod_gamebase/Console_App_Auth_GPGS_AutoLogin_001_2.68.0.png)
* Google 서비스 계정 생성 방법을 소개합니다.
    1. `Google Cloud Console > IAM & Admin > IAM > VIEW BY PRINCIPALS` 메뉴에서 '서비스 계정 사용자' 권한을 가진 유저가 있는지 찾습니다.
        * ![](https://static.toastoven.net/prod_gamebase/Console_App_Auth_GPGS_AutoLogin_002_2.68.0.png)
    2. '서비스 계정 사용자' 권한을 가진 유저가 없다면 `Google Cloud Console > IAM & Admin > Service Accounts > + CREATE SERVICE ACCOUNT`를 선택해서 서비스 계정을 생성합니다.
        * ![](https://static.toastoven.net/prod_gamebase/Console_App_Auth_GPGS_AutoLogin_003_2.68.0.png)
    3. 역할로 '서비스 계정 사용자'를 찾아 부여합니다.
        * ![](https://static.toastoven.net/prod_gamebase/Console_App_Auth_GPGS_AutoLogin_004_2.68.0.png)
    4. 생성한 서비스 계정으로 이동하여 Key를 생성합니다.
        * ![](https://static.toastoven.net/prod_gamebase/Console_App_Auth_GPGS_AutoLogin_005_2.68.0.png)
        * ![](https://static.toastoven.net/prod_gamebase/Console_App_Auth_GPGS_AutoLogin_006_2.68.0.png)
    5. JSON 형식을 선택하면 키 생성과 함께 json 파일이 자동으로 다운로드 완료됩니다.
        * ![](https://static.toastoven.net/prod_gamebase/Console_App_Auth_GPGS_AutoLogin_007_2.68.0.png)
        * ![](https://static.toastoven.net/prod_gamebase/Console_App_Auth_GPGS_AutoLogin_008_2.68.0.png)
