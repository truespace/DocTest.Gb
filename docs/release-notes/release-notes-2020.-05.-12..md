---
source: release-notes.md
section: "2020. 05. 12."
order: 28
split: true
created_date_time: 20260408_191848
keyword: Mapping, Withdraw, Purchase, TemporaryWithdrawal, Error, iOS, Unreal, Release Notes, 2.9.0
---

### 2020. 05. 12.

#### 기능 추가
* [SDK] 2.9.0
	* (Unreal) SDK 신규 배포
	
#### 기능 개선/변경
* [Console] 
	* 앱 > 앱: 탈퇴 유예 기간을 변경한 사용자의 토스트 계정을 저장하도록 개선
	* 멤버 > 회원: 매핑 이력 조회 시 정보가 제대로 보이지 않는 문제 수정
	* 구매(IAP) > 스토어: 테스트, 구) 원스토어는 신규 등록이 되지 않도록 수정

#### 버그 수정
* [SDK] 2.9.1
	* (Andoird) 매핑 이후 지표 레벨이 null이 되어 결제 지표에 정상적으로 반영되지 않는 오류 수정
	* (iOS) unreal 엔진에서 빌드 하면, warning을 빌드 오류로 판정해서 빌드가 안되는 부분을 수정
