---
source: release-notes.md
section: "2019. 02. 26."
order: 62
split: true
created_date_time: 20260408_184906
keyword: Login, Initialize, Android, iOS, Release Notes, 2.1.0
---

### 2019. 02. 26.

#### 기능 개선/변경
* [SDK] 2.1.0
	* (공통)TransferKey API 삭제
		* issueTransferKey : TransferKey 발급
		* requestTransfer : TransferKey 검증
		
#### 버그수정
* [SDK] 2.1.0
	* (Android)Gamebase 초기화 이전, onActivityResult() 가 호출되면서 이상 동작하던 버그 수정
	* (iOS)Gamecenter를 Gamebase가 아닌 다른 로직에의해 로그인 한 후, Gamebase를 통하여 Gamecenter로그인을 시도할 때, 반응이 없는 버그 수정
