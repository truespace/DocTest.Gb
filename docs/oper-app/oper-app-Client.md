---
source: oper-app.md
section: "Client"
order: 2
split: true
created_date_time: 20260408_191848
keyword: Console, Android, iOS
---

## Client

클라이언트 정보를 운영체제(iOS, Android, Unity WebGL, Unity Standalone), 버전별로 관리할 수 있습니다.

### Client List
![image alt](./image/gamebase_client_01_ko_240105.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: Gamebase 앱 설정 콘솔 Client List 화면 #01
    구성: Gamebase 앱 설정 콘솔의 Client List 기능 설정/조회 화면 스크린샷
    Keyword: 앱 설정, Console, Screenshot, Client List
-->
현재 등록된 클라이언트 목록을 확인할 수 있습니다.
운영체제별로 구분되어 보여지며 아이콘 내 숫자는 클라이언트 등록 시 입력한 버전을 의미합니다.
아이콘 목록은 서비스 상태가 <font color="white" style="background-color:#eed14c">테스트</font>, <font color="white" style="background-color:#eba34b">베타 서비스</font>, <font color="white" style="background-color:#eb7e4b">심사중</font>, <font color="white" style="background-color:#88C637">서비스</font>, <font color="white" style="background-color:#2AB1A6">업데이트 권장(서비스중)</font>인 목록만 표시됩니다. 운영체제별 하단 오른쪽의 화살표를 클릭하면 <font color="white" style="background-color:#A1A1A1">업데이트 필수</font>, <font color="white" style="background-color:#CCCCCC">종료</font> 상태의 클라이언트 목록을 확인할 수 있습니다.
아이콘 색깔을 서비스 상태별로 구분하여 한눈에 서비스 상태를 파악할 수 있습니다.

### Properties

Gamebase Console에서 관리하는 클라이언트 등록 정보를 설명합니다.
**클라이언트** 탭에서 **AOS 등록**, **iOS 등록** 버튼 등을 클릭하면 클라이언트 등록 화면이 나타납니다. 등록된 클라이언트의 입력값을 수정하거나 삭제하고 싶다면 아이콘 목록에서 아이콘을 클릭하거나 클라이언트 전체 목록에서 원하는 클라이언트를 선택하시면 됩니다.
![gamebase_client_02_ko_240105](./image/gamebase_client_02_ko_240105.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: Gamebase 앱 설정 콘솔 Properties 화면 #02
    구성: Gamebase 앱 설정 콘솔의 Properties 기능 설정/조회 화면 스크린샷
    Keyword: 앱 설정, Console, Screenshot, Properties
-->
#### (1) 스토어
(<font color="red">필수</font>) 클라이언트를 배포할 스토어를 선택합니다.
운영체제별로 선택 가능한 스토어가 다릅니다.
#### (2) 게임 버전
(<font color="red">필수</font>) 클라이언트 버전을 입력합니다.
게임에서 정한 규칙에 따라 문자열로 입력하면 됩니다.
#### (3) 서비스 상태
(<font color="red">필수</font>) 클라이언트의 서비스 상태를 선택합니다.
상태는 <font color="white" style="background-color:#eed14c">테스트</font>, <font color="white" style="background-color:#eba34b">베타 서비스</font>, <font color="white" style="background-color:#eb7e4b">심사중</font>, <font color="white" style="background-color:#88C637">서비스</font>, <font color="white" style="background-color:#2AB1A6">업데이트 권장(서비스중)</font>, <font color="white" style="background-color:#A1A1A1">업데이트 필수</font>, <font color="white" style="background-color:#CCCCCC">종료</font> 이렇게 6가지입니다.

- <font color="white" style="background-color:#F8BB28">테스트</font>: 내부 테스트
- <font color="white" style="background-color:#eba34b">베타 서비스</font>: 서비스 서버가 아닌 별도의 베타 서버에 연결이 필요한 경우 선택합니다.
- <font color="white" style="background-color:#FB8F37">심사중</font>: 스토어 심사 중
![gamebase_app_15_201812.png](./image/gamebase_app_15_201812.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: Gamebase SDK 기본 제공 서비스 상태 팝업 예시 3종
    구성: 서비스 상태별로 게임 이용자에게 표시되는 Gamebase SDK 기본 팝업 3개를 보여주는 화면. (1) Update Recommended - "You must update your app to continue playing." 메시지와 LATER/UPDATE NOW 버튼, (2) Update Required - 동일 메시지와 UPDATE NOW 버튼만 표시, (3) Service Closed - "This game has been closed. Thank you for your support." 메시지와 OK 버튼
    Keyword: 앱 설정, SDK 팝업, 서비스 상태, Update Recommended, Update Required, Service Closed
-->

- <font color="white" style="background-color:#88C637">서비스중</font>: 정상 서비스
- <font color="white" style="background-color:#2AB1A6">업데이트 권장(서비스 중)</font>: 정상 서비스. <br/>보다 안정적인 버전을 사용하도록 유도하기 위해 팝업을 표시합니다. <br/>새로운 버전을 다운로드해서 이용하도록 유도하지만 사용자가 원하는 경우 현재 버전으로도 계속 서비스를 이용할 수 있습니다.<br />아래는 '업데이트 권장(서비스 중)' 상태일 때 Gamebase SDK에서 기본적으로 제공하는 팝업입니다.

- <font color="white" style="background-color:#A1A1A1">업데이트 필수</font>: 서비스 불가능. <br/>현재 게임에서 서비스를 지원하지 않는 버전으로, 최신 버전 설치 안내 팝업을 표시합니다.<br />아래는 '업데이트 필수' 상태일 때 Gamebase SDK에서 기본적으로 제공하는 팝업입니다.

![gamebase_client_04_ko_240105.png](./image/gamebase_client_04_ko_240105.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: Gamebase 앱 설정 콘솔 (3) 서비스 상태 화면 #04
    구성: Gamebase 앱 설정 콘솔의 (3) 서비스 상태 기능 설정/조회 화면 스크린샷
    Keyword: 앱 설정, Console, Screenshot, (3) 서비스 상태
-->

>  <font color="red">[주의] </font>
>  **업데이트 필수와 점검이 동시에 설정**되어 있을 경우 서비스 상태는 '업데이트 필수'가 됩니다.
>  점검 진행 도중 사용자에게 업데이트 필수 팝업을 표시하고 싶지 않다면 점검 완료 이후에 서비스 상태를 '업데이트 필수'로 변경해야 합니다.
>  <font color="orange">[참고] </font>
>  업데이트 버튼을 누르면 설치 URL 메뉴에서 설정한 각각의 스토어 주소로 연결됩니다.
>  예를 들면 클라이언트가 App store로 설정되어 있고 설치 URL 메뉴에서 App store 관련 설정이 존재한다면 설정한 주소로 이동되며 만약 설치 URL 메뉴에 설정이 되어 있지 않을 경우 공통(Common) URL로 연결됩니다.

- <font color="white" style="background-color:#CCCCCC">종료</font>: 서비스 불가능. <br/> 서비스가 종료된 버전인 경우 선택합니다.<br />아래는 '종료' 상태일 때 Gamebase SDK에서 기본적으로 제공하는 팝업입니다.

> [참고]
> 서비스 상태별 표시할 메시지 설정
> **업데이트 권장(서비스중)**, **업데이트 필수**, **종료** 상태인 경우 사용자에게 표시할 안내 메시지를 다국어로 설정할 수 있습니다.
> 서비스 상태를 선택하면 앱에 설정되어 있는 언어 설정 정보에 따라 각 상태에 맞는 기본 메시지가 제공되며 원하는 경우 언어를 추가하거나 기본 메시지의 문구를 변경할 수 있습니다.
> 만약 이전에 각 상태로 설정되어 있던 각 언어별 설정들이 있다면 앱의 언어 설정 정보에 관계 없이 이전에 등록했던 내용들을 불러와 보여지게 됩니다.
> 앱의 언어 설정에 설정된 정보가 없을 경우 5개(한국어, 영어, 일본어, 중국어 간체, 중국어 번체)의 언어로 기본 메시지가 제공되며 원하는 경우 언어를 추가하거나 기본 메시지의 문구를 변경할 수 있습니다.
> ![gamebase_client_03_ko_240105](./image/gamebase_client_03_ko_240105.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: Gamebase 앱 설정 콘솔 (3) 서비스 상태 화면 #03
    구성: Gamebase 앱 설정 콘솔의 (3) 서비스 상태 기능 설정/조회 화면 스크린샷
    Keyword: 앱 설정, Console, Screenshot, (3) 서비스 상태
-->

#### (4) 서버 주소
클라이언트에서 이용할 서버 주소(IP, URL)를 입력합니다.
**앱** 탭에서 서버 주소를 입력하면 모든 클라이언트에 적용되므로, 클라이언트마다 다른 서버 주소를 사용하고 싶을 때만 서버 주소를 입력합니다.

#### (5) Debug log
Gamebae SDK의 Debug Log 출력 여부를 콘솔에서 실시간으로 변경할 수 있습니다.
설정되어 있지 않으면 기본적으로 Gamebase SDK 내부에 설정된 값을 우선으로 동작하고 Gamebase 콘솔에서 Debug Log 출력 여부를 설정할 수 있습니다.
Gamebase SDK에 Debug Log가 'OFF' 상태이더라도 콘솔에서 'ON'으로 설정하면 단말기에 Gamebase Debug Log가 출력됩니다.

#### (6) 메모
해당 클라이언트에 대한 간단한 메모를 30자 내로 입력할 수 있습니다.
