---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2018. 06. 07."
section: "2018. 06. 07."
order: 76
---

### 2018. 06. 07.

#### 기능 추가
* [SDK] 1.10.0
	* (Unity)StandaloneWebviewAdapter: html source rendering 지원	

#### 기능 개선/변경
* [SDK] 1.10.0
	* (Unity)Unity Adapter의 interface가 수정
		* v1.10.0 이상 사용 시에는 UnityAdapter 버전 업그레이드가 필요(GamebaseUnitySDK_FacebookAdapter_v1.5.0, GamebaseUnitySDK_StandaloneWebviewAdapter_v1.7.0)
	* (Unity)Login API 호출 시 Unity Adapter가 없는 경우 네이티브(Android/iOS)의 로그인 API를 호출하도록 로직 변경 : facebook, Google
	* (Unity)각 Adapter 폴더 구조 및 이름 오타 수정
		* 경로: Assets/Gamebase/Scripts/Adapter => Assets/Gamebase/Adapter
		* 오타: Adapater => Adapter
