---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "2017. 11. 23."
section: "2017. 11. 23."
order: 88
---

### 2017. 11. 23.

#### 기능 추가

* [SDK] 1.4.0 업데이트
	* (Unity)Gamebase Facebook Adapter가 추가 : Android, iOS, WebGL, Standalone Platform 및 UnityEditor 지원

#### 기능 개선/변경
* [SDK] 1.4.0 업데이트
	* (iOS)close/back 버튼 리소스가 없을 때, "x", "<" 등의 텍스트로 노출되던 이슈를 디폴트 값으로 대체

#### 버그 수정
* [SDK] 1.4.0 업데이트
	* (Android)Gamebase 제공 팝업을 사용하지 않는 경우 이용정지 정보가 null로 리턴되는 오류 수정
	* (iOS)WebView 런치 후, 기기 회전시 NavigationBar Title 이 reset이 되는 오류 수정
	* (iOS)WebView의 NavigationBar Height을 커스터마이징 할 때, NavigationBar 배경 부분이 겹쳐서 노출되는 오류 수정
