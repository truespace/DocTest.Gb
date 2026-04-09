---
source: release-notes.md
section: "2021. 01. 26."
order: 9
split: true
created_date_time: 20260408_184906
keyword: Purchase, Authentication, Contact, Android, iOS, Release Notes, 2.19.0
---

### 2021. 01. 26.

```
푸시 > 푸시(구) 콘솔 메뉴 기능이 제외되었습니다.
```

#### 기능 추가
* [Console] 
	* 이용 정지 > 앱가드: 조건 차단 기능 추가
	* 구매(IAP) > 결제 어뷰징 모니터링: Apple App Store 추가 
* [SDK] 2.19.0
	* (Unreal) SDK 배포: 2.16.0 ~ 2.19.0 누적된 내역 반영
		* [Android 설정 툴](https://docs.toast.com/ko/Game/Gamebase/ko/unreal-started/#android-settings) 제공: Gamebase_Android_UPL.xml 파일을 수정하는 대신 설정 툴을 사용바랍니다.
		* 고객센터 기능 추가	
		* 인증 추가: Hangame, Weibo
		* Galaxy 스토어 추가
		* 결제 아이템 정보에 지역화된 상품 정보 추가: localizedTitle, localizedDescription
		* Android 설정 툴 제공
		* Unreal 4.26 지원

#### 기능 개선/변경
* [Console]
	* 관리 > 권한: 매출 접근 권한 제거 [관련 공지 바로 가기](https://www.toast.com/kr/support/notice/detail/2101)
* [SDK] 2.19.1
	* (iOS) Weibo IdPAdapter 구조 변경
