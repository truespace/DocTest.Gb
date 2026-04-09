---
source: release-notes.md
section: "2020. 06. 09."
order: 26
split: true
created_date_time: 20260408_184906
keyword: Login, Withdraw, Push, Initialize, TemporaryWithdrawal, iOS, Unity, Release Notes, 2.10.1
---

### 2020. 06. 09.

#### 기능 개선/변경
* [Console] 
	* 멤버 > 회원:  **탈퇴 이력 조회** 화면에 탈퇴 유예 상태(탈퇴 유예, 탈퇴 취소, 즉시 탈퇴) 추가 표시
* [SDK] 2.10.1
	* (iOS) 사용자 푸시 설정 초기화 시 언어 코드가 설정되어 있지 않으면 디바이스 언어로 설정되도록 변경

#### 버그 수정
* [Console] 
	* 쿠폰 > 쿠폰 발급: 쿠폰 통계 다운로드 시 SMS로 발송한 내역이 다운로드되지 않는 문제 수정

* [SDK] 2.10.1
	* (Unity) iOS Plugin에서 ViewController가 설정되지 않아 로그인 호출 시 실패하는 문제 수정
	* (JavaScript) 초기화 시 StoreCode를 입력하지 않으면 오류가 발생하는 문제 수정
