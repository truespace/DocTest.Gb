---
source: release-notes.md
section: "2019. 04. 23."
order: 58
split: true
created_date_time: 20260408_191848
keyword: Login, Purchase, Authentication, Android, Unity, Release Notes, 2.3.0
---

### 2019. 04. 23.

```
Gamebase를 사용하면 50여개의 중국스토어 연동이 가능합니다.
중국출시에 관심 있으신 경우에는 고객센터로 연락주세요.
```

#### 기능 추가
* [SDK] 2.3.0
	* (Android/Unity)중국스토어 인증/결제 추가

#### 기능 개선/변경
* [SDK] 2.3.0
	* (공통)Launching Status Code 추가: "심사중(204)", "테스트중(203)"
	* (Android)최근 로그인한 Provider로 로그인 및 웹소켓 응답 실패를 받았을 경우(Timeout, network disable 등) AuthToken을 삭제 처리하지 않도록 수정
	* (Android)IdP로그인 시 AuthAdapter 내부에서 발생하는 MemoryLeak을 수정
