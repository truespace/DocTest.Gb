---
source: Overview.md
section: "Console Role"
order: 7
split: true
created_date_time: 20260408_191848
keyword: Purchase, Push, Contact, Coupon, Console, Overview
---

## Console Role

NHN Cloud의 기본적인 멤버 정책과 권한에 대해서는 다음 가이드를 참고하시기 바랍니다.
* [NHN Cloud > 콘솔 사용 가이드 > 멤버 관리](https://docs.nhncloud.com/ko/nhncloud/ko/console-guide/#_14)

### Manage Role

**Console > 프로젝트 설정 > 멤버 관리**
프로젝트 설정 화면에서 토스트 회원을 추가하거나 등록된 회원에게 개별적인 권한 부여가 가능합니다. 한 명의 회원에게 여러개의 권한을 중복하여 지급할 수 있습니다.
![프로젝트권한](./image/gamebase_overview_01_ko_240105.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: NHN Cloud 회원 등록 및 권한 부여 화면
    구성: NHN Cloud 콘솔의 회원 등록 팝업으로, Gamebase 서비스를 검색하여 ADMIN, ANALYTICS VIEWER - ALL, ANALYTICS VIEWER - EXCLUDING SALES, ANALYTICS VIEWER - ONLY REAL-TIME, APP ADMIN, APP VIEWER 등 개별 권한 목록을 표시하고 선택할 수 있는 UI
    Keyword: Screenshot, Console, Manage Role
-->

**Console > 프로젝트 설정 > 권한 그룹 관리**
운영상의 편의를 위해서 자주 사용하는 권한은 *권한 그룹*으로 등록하여 토스트 회원에게 권한 그룹 단위로 권한을 줄 수 있습니다.
![프로젝트권한그룹](./image/gamebase_overview_02_ko_240105.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: 프로젝트 권한 그룹 관리 화면
    구성: NHN Cloud 콘솔의 권한 그룹 관리 테이블로, 역할 그룹 이름(Gamebase 운영자), 설명(운영자 권한), 유형(프로젝트 정의 그룹), 멤버 수, 역할 수(25개), 역할 그룹 추가일 등의 컬럼이 표시되며 역할 그룹 추가/삭제 버튼 포함
    Keyword: Screenshot, Console, Manage Role
-->

**Console > 조직 설정 > 프로젝트 공통 권한 그룹 설정**
조직 관리 화면에서 조직내의 프로젝트에서 공통으로 사용하는 권한 그룹을 관리할 수 있습니다.
![조직권한그룹](./image/gamebase_overview_03_ko_240105.png)
<!-- LLM_Image_DESC_20260408_191856
    유형: Screenshot
    내용: 조직 프로젝트 공통 권한 그룹 설정 화면
    구성: NHN Cloud 콘솔의 조직 설정 내 프로젝트 공통 권한 그룹 관리 화면으로, Gamebase 운영자 역할 그룹의 상세 권한 목록(Gamebase ADMIN, ANALYTICS VIEWER 등)을 표시하고 프로젝트 공통 역할 그룹 설정 탭을 포함
    Keyword: Screenshot, Console, Manage Role
-->

### Gamebase에서 제공하는 권한 목록

| 서비스 | 권한 | 설명 |
| --- | --- | --- |
| Gamebase | ADMIN | **전체 화면의 접근 및 제어**<br>Gamebase 서비스 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | ANALYTICS VIEWER - ALL | 모든 지표 Read(읽기)<br>지표 결과의 엑셀 파일 다운로드 가능 |
| Gamebase | ANALYTICS VIEWER - EXCLUDING SALES | 매출을 제외한 모든 지표 Read(읽기) |
| Gamebase | ANALYTICS VIEWER - ONLY REAL-TIME | 실시간 지표 Read(읽기) |
| Gamebase | APP ADMIN | APP 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | APP VIEWER | APP 메뉴 Read(읽기) |
| Gamebase | BAN ADMIN | 이용 정지 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | BAN VIEWER | 이용 정지 메뉴 Read(읽기) |
| Gamebase | COUPON ADMIN | 쿠폰 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | COUPON VIEWER | 쿠폰 메뉴 Read(읽기) |
| Gamebase | CS ADMIN | 고객센터 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | CS INQUIRY SUPPORT | 고객센터 문의 메뉴 Read(읽기), Update(갱신) 및 멤버 메뉴 Read(읽기) |
| Gamebase | IAP ADMIN | 구매 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | IAP VIEWER | 구매 메뉴 Read(읽기) |
| Gamebase | LEADERBOARD ADMIN | 리더보드 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | LEADERBOARD VIEWER | 리더보드 메뉴 Read(읽기) |
| Gamebase | MANAGEMENT ADMIN | 관리 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | MEMBER ADMIN | 멤버 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | MEMBER VIEWER | 멤버 메뉴 Read(읽기) |
| Gamebase | MEMBER FILE DOWNLOAD | 멤버 메뉴 Read(읽기) 및 멤버 파일 다운로드 |
| Gamebase | OPERATION ADMIN | 운영 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | OPERATION VIEWER | 운영 메뉴 Read(읽기) |
| Gamebase | PUSH ADMIN | 푸시 메뉴 Create(생성), Read(읽기), Update(갱신), Delete(삭제) |
| Gamebase | PUSH VIEWER | 푸시 메뉴 Read(읽기) |

* 프로젝트에서 자주 사용하는 권한 그룹을 생성하여 권한을 관리하는 예시입니다. 게임에서 필요에 따라 적절한 권한 그룹을 생성하여 관리할 수 있습니다.

| 서비스 | 권한 | 관리자/사업 | 개발 | CS |
| --- | --- | --- | --- | --- | 
| Gamebase | ADMIN | ● | | |
| Gamebase | ANALYTICS VIEWER - ALL |  |  | |
| Gamebase | ANALYTICS VIEWER - EXCLUDING SALES |   |  | |
| Gamebase | ANALYTICS VIEWER - ONLY REAL-TIME |  | ● | |
| Gamebase | APP ADMIN | |  ● | |
| Gamebase | APP VIEWER | |  | |
| Gamebase | BAN ADMIN | |  ● | ●|
| Gamebase | BAN VIEWER | |  | |
| Gamebase | COUPON ADMIN | | ● | |
| Gamebase | COUPON VIEWER | |  |● |
| Gamebase | CS ADMIN | |  | |
| Gamebase | CS INQUIRY SUPPORT | |  | ● |
| Gamebase | IAP ADMIN | | ● | |
| Gamebase | IAP VIEWER | |  |● |
| Gamebase | LEADERBOARD ADMIN || ● | | 
| Gamebase | LEADERBOARD VIEWER | |  | |
| Gamebase | MANAGEMENT ADMIN | | ● | |
| Gamebase | MEMBER ADMIN | | ● | ● |
| Gamebase | MEMBER VIEWER | |  |  |
| Gamebase | MEMBER FILE DOWNLOAD | |  | |
| Gamebase | OPERATION ADMIN | | ● | |
| Gamebase | OPERATION VIEWER | |  |● |
| Gamebase | PUSH ADMIN | | ● | |
| Gamebase | PUSH VIEWER | |  | ● |
