---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2020. 12. 29."
section: "2020. 12. 29."
order: 11
---

### 2020. 12. 29.

#### 기능 추가
* [SDK] 2.19.0
	* (공통) Weibo 인증 추가
	* (Android) Sign In with Apple 인증 추가
	
#### 기능 개선/변경
* [Console]
	* 앱 > 앱: 서버 주소 관리에 베타 서비스 서버 추가 
	* 앱 > 클라이언트: 클라이언트 상태에 베타 서비스 추가, 클라이언트 추가 정보 등록할 수 있도록 메모 기능 추가 
	* 구매(IAP) > 상품: 검색 조건 추가 - 사용여부
	* 구매(IAP) > 결제 정보: 결제 내역에 스토어 테스트 결제건 표시
	* 구매(IAP) > 판매 현황 메뉴 종료: Analytics > 매출 지표와 기능이 통합되었습니다.
	* Analytics > 이용 환경 > 설치 URL 메뉴 종료
* [SDK] 2.19.0
	* (공통) 론칭 상태 코드 추가: 베타 서비스(205)

#### 버그 수정
* [SDK] 2.19.0
    * (Unity) WebSocket에서 재시도 시 OutOfMemoryException이 발생하는 문제 수정
* [SDK] 2.19.1
	* (Android) Weibo 로그인 시도 후 다른 IdP로 로그인 시 크래시가 발생하는 문제 수정
