---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2019. 01. 29."
section: "2019. 01. 29."
order: 63
---

### 2019. 01. 29.

```
Gamebase 2.0의 개선된 전체 지표를 활용하기 위해서는 SDK 업데이트가 필요합니다.
```

#### 기능 추가
* Console
	* Analytics : Gamebase 2.0 지표 신규 오픈
	* 앱 : 클라이언트의 디버그 로그를 실시간으로 변경할 수 있는 기능 추가
* [SDK] 2.0.0
	* (공통)Custom 지표를 위한 API 추가 (구매 성공의 경우 SDK내부에서 자동 전송)
		* setGameUserData : 게임 로그인 이후 유저 레벨 정보 전송
		* traceLevelUpData : 레벨업 추적을 위하여 게임 유저의 레벨업이 되었을 때 호출
    * (JavaScript)SDK 신규 배포

#### 기능 개선/변경
* [SDK] 2.0.0
	* (Android)Push SDK 업데이트(android:1.7.0)
	* (Android)Adapter API 변경
		* Launching 정보 전달
		* logout, withdraw API에 Callback 추가
	* (iOS)IAP SDK 업데이트
		* 결제 실패 시 간헐적으로 크래시가 발생하던 현상 수정

#### 버그수정
* [SDK] 2.0.0
	* (iOS)iOS 12 이상의 시뮬레이터에서 debugMode On 상태로 Gamebase 초기화 시 크래시가 발생하던 현상 수정
