---
source: release-notes.md
section: "2019. 11. 20."
order: 41
split: true
created_date_time: 20260408_191848
keyword: Initialize, Error, iOS, Unity, Release Notes, 2.6.1
---

### 2019. 11. 20.

#### 버그 수정
* [SDK] 2.6.1
	* (Unity)iOS Plugin 파일이 Package에 누락되어 iOS 빌드 시 에러가 발생하여 해당 파일을 추가: 'toast_sdk_wrap.m'
	* (Unity)UnityEditor에서 Standalone 이외의 플랫폼으로 실행시 Store Code가 Empty로 입력되어 초기화에 실패하는 오류 수정
	* (Unity)Initialize API 내부 zone type 처리 부분에서의 오류로 NullReferenceException 발생하던 오류 수정
