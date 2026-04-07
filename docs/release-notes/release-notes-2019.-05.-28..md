---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v2.4.0, 버그수정, 기능개선, 기능추가, 변경, 제거"
section: "2019. 05. 28."
order: 56
---

### 2019. 05. 28.

#### 기능 추가
* HANGAME mix 일본결제 추가
    * [SDK] 2.4.0
    	* (Unity)Standalone 일본 외부결제 추가
    	* (Unity)Standalone 일본 HANGAME 인증 추가
    * [Console] 
    	* 구매 > 스토어: 'HANGAME mix(JAPAN)' Store 추가
    	* 앱 > 클라이언트: Windows 클라이언트 등록 시 스토어 설정 항목 추가
    	* 앱 > 설치URL: Windo 설치 URL 추가 시 스토어 설정 항목 추가

#### 기능 개선/변경
* [SDK] 2.4.0
	* (공통) 지표관련 Class 변경
        * LevelUpData Class: userLevel, levelUpTime 파라미터가 필수로 변경 / 그 외 필드 삭제 [자세히보기 [Android](http://docs.toast.com/ko/Game/Gamebase/ko/aos-etc/#game-user-data-settings) / [iOS](http://docs.toast.com/ko/Game/Gamebase/ko/ios-etc/#game-user-data-settings) / [Unity](http://docs.toast.com/ko/Game/Gamebase/ko/unity-etc/#game-user-data-settings) / [JavaScript](http://docs.toast.com/ko/Game/Gamebase/ko/js-etc/#game-user-data-settings)]
        * GameUserData Class: classId(게임유저의 직업) 필드 추가 [자세히보기 [Android](http://docs.toast.com/ko/Game/Gamebase/ko/aos-etc/#level-up-trace) / [iOS](http://docs.toast.com/ko/Game/Gamebase/ko/ios-etc/#level-up-trace) / [Unity](http://docs.toast.com/ko/Game/Gamebase/ko/unity-etc/#level-up-trace) / [JavaScript](http://docs.toast.com/ko/Game/Gamebase/ko/js-etc/#level-up-trace)]
    * (Android)Naver SDK 버전 업데이트(v4.2.5): Naver SDK 버그 수정(Naver 로그인 도중에 앱 아이콘을 통해 앱을 재시작할 경우, Activity가 강제종료 되는 이슈로 인해 인증 프로세스가 중단되는 이슈가 해결)
    * (Unity)StandaloneWebview가 32bit 빌드를 지원 (SDK 용량 53.6MB에서 99.2MB로 증가)
* [Server]
    * LTV 쿼리 수정 및 failover 로직 수정
* [Console]
    * LTV Grid ComplexColumns 지원 및 엑셀 다운로드 지원
