---
source: release-notes.md
section: "2020. 01. 14."
order: 37
split: true
created_date_time: 20260408_191848
keyword: Login, Withdraw, Error, Unity, Release Notes, 2.6.3
---

### 2020. 01. 14.

#### 기능 추가
* [서버 API] 사용자 탈퇴 API 추가

#### 기능 개선/변경
* [SDK] 2.6.3
	* (Unity) Standalone Webview 개선: CefWebview 업데이트	
	* (Unity) 로그인 이후 오류가 발생하여 누락된 .dll 파일 추가
		* ToastCommon.dll, vcruntime140.dll

#### 버그 수정
* [SDK] 2.6.3
	* (Unity) Login(CredentialInfo) API 호출 시 오류가 발생하여 수정
