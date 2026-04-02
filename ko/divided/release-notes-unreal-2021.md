## Game > Gamebase > 릴리스 노트 > Unreal

### 2.26.1 (2021.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.26.1/GamebaseSDK-Unreal.zip)

#### 버그 수정
* GamebaseDisplayLanguageCode 핀란드어 오타 수정
    * Finish → Finnish

### 2.26.0 (2021.09.28)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.26.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
* 공통 약관 기능 추가
    * 약관 웹뷰를 여는 API 추가
    * 약관 리스트 및 유저별 동의 여부를 조회하는 API 추가
    * 유저별 약관 동의 여부를 Gamebase 서버에 저장하는 API 추가

#### 기능 개선/변경
* 고객 센터 타입이 TOAST 조직 상품(Online Contact)인 경우 로그인을 하지 않아도 고객 센터가 표시되도록 변경
* 내부 론칭 URL 변경
* Gamebase에서 Android multidex 적용 제거

### 2.19.2 (2021.06.29)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.19.2/GamebaseSDK-Unreal.zip)

#### 버그 수정
* 이미지 공지 ShowImageNotices API 호출 시 onEventCallback을 등록하지 않는 경우 닫기 버튼을 눌렀을 때 크래시가 발생하는 문제 수정
* Android 설정 툴 - Enable Hangame, Enable Weibo가 정상 동작하지 않는 문제 수정

### 2.19.1 (2021.02.09)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.19.1/GamebaseSDK-Unreal.zip)

#### 버그 수정
* Unity 빌드 중 제외되는 파일이 생길 때 발생하는 컴파일 오류 수정

### 2.19.0 (2021.01.26)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.19.0/GamebaseSDK-Unreal.zip)

#### 기능 추가
* SDK 배포: 2.16.0 ~ 2.19.0 누적된 내역 반영
    * [Android 설정 툴](./unreal-started/#android-settings) 제공: Gamebase_Android_UPL.xml 파일을 수정하는 대신 설정 툴을 사용바랍니다.
    * 고객 센터 기능 추가    
    * 인증 추가: Hangame, Weibo
    * Galaxy 스토어 추가
    * 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription
    * Android 설정 툴 제공
    * Unreal 4.26 지원
