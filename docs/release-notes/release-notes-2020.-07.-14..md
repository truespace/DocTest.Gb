---
source: release-notes.md
section: "2020. 07. 14."
order: 24
split: true
created_date_time: 20260408_184906
keyword: Login, Withdraw, Purchase, WebView, Initialize, iOS, Unity, Release Notes, 2.12.0
---

### 2020. 07. 14.

#### 기능 추가
* 이미지 공지: 표시 기간과 우선순위에 따라 게임 내 이미지 팝업 표시
    * [Console] 운영 > 이미지 공지: 메뉴 추가
    * [SDK] 2.12.0: 이미지 공지 표시 API 추가

#### 기능 개선/변경
* [Console] 
    * 구매(IAP) > 상품: 아이템 번호로 상품 조회 가능하도록 추가
    * 멤버 > 회원: 탈퇴 유예 상태의 유저를 정상 상태로 변경할 수 있도록 개선
    * 멤버 > 다운로드: 로그인 로그 이력에 deveiceKey, IdP 코드 항목 추가
* [SDK] 2.12.0
    * (iOS) Facebook SDK 업데이트(7.1.1)
    * (iOS) configuartion에 설정된 storeCode(default=AS)로 Gamebase 초기화 시도
    * (iOS) 콘텐츠를 로딩할 수 없는 웹뷰 출력 시 **닫기** 버튼이 없어 닫을 수 없는 문제 수정
    * (Unity) TOAST Unity SDK 업데이트(0.20.1.1)
