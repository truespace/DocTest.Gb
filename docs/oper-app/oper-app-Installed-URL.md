---
source: oper-app.md
split: true
created_date_time: 20260406_141859
keyword: "Installed URL, Properties"
section: "Installed URL"
order: 5
---

## Installed URL

게임을 설치하기 위한 스토어 URL 정보를 관리합니다.

![gamebase_installed_url_01_ko_240105](./image/gamebase_installed_url_01_ko_240105.jpg)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: 설치 URL 관리 화면 (조회 모드)
    구성: 설치 URL 정보와 수정 버튼, 공통(COMMON) URL 설정, Android 스토어별(Google Play, ONE store, Galaxy Store) 대표 스토어 및 코드/PC/Mobile URL 설정, iOS(App Store) URL 설정이 테이블 형태로 표시됨.
    Keyword: 설치 URL, 스토어별 URL, Google Play, ONE store, Galaxy Store, App Store
-->

클라이언트 상태가  <font color="white" style="background-color:#2AB1A6">업데이트 권장(서비스 중)</font> 또는 <font color="white" style="background-color:#A1A1A1">업데이트 필수</font>일 때 스토어별로 제공할 주소의 값을 설정합니다.
사용자가 PC나 모바일에서 단축 URL을 클릭하면, 사용자 단말기 정보(디바이스, 운영체제, 스토어 등)를 이용하여 입력된 사이트로 리디렉션합니다.
스토어 정보가 없거나 스토어 이동에 실패하면 'COMMON'에 설정된 URL로 이동합니다.

_[예시1] Android 휴대폰에서 문자로 받은 설치 URL을 클릭하는 경우
**(Device:mobile,OS:Android,Store:없음)** Android 중에 대표 스토어로 지정된 모바일 URL로 이동. 대표 스토어가 'Google Play'인 경우 'Google Play' 모바일에 설정된 URL로 이동.
_[예시2] 'One Store'에서 다운로드한 앱으로 게임 중이던 사용자가 '업데이트 필수' 팝업 창에서 '지금 업데이트' 버튼을 클릭한 경우_
**(Device:mobile,OS:Android,Store:One Store)** 'One Store' 모바일에 설정된 URL로 이동(One Store 모바일 설치 페이지)<br/>
_[예시3] PC에서 설치 URL을 입력한 경우_
**(Device:PC,OS:Windows,Store:없음)** COMMON PC에 설정된 URL로 이동


### Properties

입력된 설치 URL 정보를 변경하려면 **수정** 버튼을 클릭합니다.

![gamebase_installed_url_02_ko_240105](./image/gamebase_installed_url_02_ko_240105.jpg)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: 설치 URL 수정 화면
    구성: 공통(COMMON), Android(Google Play, ONE store, Galaxy Store), iOS(App Store) 섹션별로 PC/Mobile URL 입력 필드가 편집 가능한 상태로 표시됨. 대표 스토어 선택 라디오 버튼과 하단에 취소/저장 버튼 존재.
    Keyword: 설치 URL 수정, 스토어별 URL, PC, Mobile, 대표 스토어
-->

- 각 항목은 PC, 모바일별로 따로 설정할 수 있습니다. PC와 모바일을 구분할 필요가 없다면 동일한 값을 각각 입력하면 됩니다.
- 원하는 스토어가 목록에 표시되지 않을 경우, [고객 센터](https://toast.com/support/inquiry)로 연락 주시면 해당 스토어에 대한 추가가 가능합니다.

#### (1) Common
스토어 정보가 없거나 스토어 이동에 실패했을 때 연결될 주소를 설정합니다.

#### (2) Android
Android 사용자가 설치 URL을 실행할 때 연결될 주소를 설정합니다.

#### (3) iOS
iOS 사용자가 설치 URL을 실행할 때 연결될 주소를 설정합니다.

#### (4) Standalone
Standalone으로 서비스 되는 앱에서 연결될 주소를 설정합니다. Standalone은 PC에서만 동작하므로 PC설정만 하면 됩니다.
