---
source: release-notes-android.md
section: "2.30.0 (2021.11.23)"
order: 66
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Mapping, WebView, Initialize, Authentication, Release Notes, 2.30.0
---

### 2.30.0 (2021.11.23)
[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.30.0/GamebaseSDK-Android.zip)

#### 기능 추가
* 강제 매핑 시 IdP 로그인을 한 번 더 시도해야 하는 불편함을 개선한 새로운 강제 매핑 API가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Mapping > Add Mapping Forcibly](../aos-authentication.md#add-mapping-forcibly)
* Gamebase.addMapping() 호출 후 AUTH_ADD_MAPPING_ALREADY_MAPPED_TO_OTHER_MEMBER(3302) 에러가 발생했을 때, 해당 계정으로 로그인을 할 수 있는 API가 추가되었습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 인증 > Mapping > Change Login with ForcingMappingTicket](../aos-authentication.md#change-login-with-forcingmappingticket)

#### 기능 개선/변경
* 외부 SDK 업데이트: Hangame Android SDK(1.4.2)
* Gamebase가 기본으로 제공하는 점검 상세보기 웹뷰 html을 사용자가 수정해서 사용할 수 있도록 개선하였습니다.
    * [Game > Gamebase > Android SDK 사용 가이드 > 초기화 > Launching Information > 1. Launching > 1.3 Maintenance > Change Default Maintenance HTML](../aos-initialization.md#change-default-maintenance-html)
* DisplayLanguageCode를 설정했음에도 기본 점검 웹뷰의 시간이 단말기 언어로 표시되는 오류를 수정하였습니다.
* 통신 오류 발생 시, 끊긴 커넥션으로 통신을 시도함으로 인해 반복적으로 발생하던 네트워크 오류를 개선하였습니다.
