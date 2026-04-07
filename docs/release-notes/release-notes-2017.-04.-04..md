---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v1.1.2, 버그수정, 기능개선, 기능추가, 변경, Maintenance, IdP, IAP"
section: "2017. 04. 04."
order: 95
---

### 2017. 04. 04.

#### 기능 개선/변경
* [SDK] 1.1.2 업데이트
    * 게임런칭시 점검, 긴급공지 팝업 개선
    * Unity Plugin 디버그로그 추가 및 익셉션 상세처리
* [API] [IAP](../../api-guide.md#purchaseiap) API 연동 : 아이템 조회, 미소비내역 조회
* [API] checkAccessToken API 응답 결과에, 로그인 시 사용된 IdP 관련 정보 포함하는 스펙 추가
* [Console] 점검, 긴급공지 : 클라이언트 버전 선택 시 게임에서 사용하지 않는 스토어는 노출되지 않도록 변경

#### 버그 수정
* [Console] iOS 클라이언트 등록 시 마켓 비정상 노출 수정
