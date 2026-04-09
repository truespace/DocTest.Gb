---
source: release-notes.md
section: "2019. 11. 12."
order: 43
split: true
created_date_time: 20260408_184906
keyword: Login, Purchase, Consume, Analytics, Logger, Android, iOS, Release Notes, 2.6.0
---

### 2019. 11. 12.

```
Gamebase SDK 2.6.0 미만 버전에서 2.6.0으로 업그레이드 하는 경우
반드시 Upgrade Guide문서에 설명된 변경 사항을 반영해 주시기 바랍니다. 
가이드 위치: Game > Gamebase > Upgrade Guide
```

#### 기능 추가
* 쿠폰 서비스 신규 오픈: 쿠폰을 대량으로 생성하고 관리하는 기능
	* [Console] Coupon 메뉴 신규 오픈
	* [Server API] 쿠폰 확인 및 소비 API 추가
* 자동 결제 어뷰징 기능 추가
	* [Console] 구매(IAP) > 결제 어뷰징 모니터링 메뉴 신규 오픈
		* 결제 어뷰징 자동 제재 설정 기능
		* 결제 어뷰징 조건 검색 후 수동 이용 정지 가능
* Google 구독 결제 기능 추가
	* [SDK] 2.6.0 Android
* [SDK] 2.6.0
	* (공통) 데이터를 Log&Crash 에 전송하여 각종 분석에 이용할 수 있도록 TOAST Logger 추가
	* (iOS) Sign In with Apple 인증 추가
	* (Android) Gamebase Android SDK 가 Bintray 를 통해 배포되므로 gradle 설정만으로 Gamebase 를 사용할 수 있음

#### 기능 개선/변경
* [SDK] 2.6.0
	* (Unity) 로그인시 LaunchingStatus를 갱신하는 로직에 오류가 있어 수정
	* (Unity) Debug Log를 전송하는 기능을 Gamebase 콘솔에서 설정할 경우 Client에서 로그 전송을 무한 반복하는 오류 수정
* [Console]
	* 앱 > 앱: 서버 주소를 서비스 상태별(테스트, 심사중, 서비스)로 입력 받을 수 있도록 변경
	* 구매(IAP) > 결제 정보: 검색 조건 선택하여 검색할 수 있도록 UI 변경
