---
source: release-notes-console.md
section: "2018. 04. 05."
order: 121
split: true
created_date_time: 20260408_184906
keyword: Console, Release Notes, Release
---

### 2018. 04. 05.

#### 기능 추가
* Kick out 기능 추가
	- 현재 게임 중인 전체 사용자의 연결을 끊는 기능(점검 시 게임에서 전체 사용자의 연결을 끊고 싶을 때 사용할 수 있음)
	- [Console] 메뉴 추가
* 점검 웹페이지를 사용자가 Console에서 입력한 HTML 페이지로 사용할 수 있도록 기능을 개선
	- 이전에는 Gamebase에서 제공하는 웹페이지나 외부 웹페이지 연결만 가능했음
	- 웹서버가 없는 경우에도 점검 페이지를 사용자가 원하는 형태로 만들 수 있음


#### 버그 수정
* 국가코드(contry code)가 10자 이상인 경우 동접 데이터가 저장되지 않는 현상 수정
