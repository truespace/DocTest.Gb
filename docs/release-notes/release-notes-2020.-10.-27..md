---
source: release-notes.md
split: true
created_date_time: 20260406_141859
keyword: "v2.15.0, 버그수정, 기능개선, 기능추가, 변경, Push, Analytics, Notice, Coupon"
section: "2020. 10. 27."
order: 15
---

### 2020. 10. 27.

#### 기능 추가
* Unreal SDK 기능 추가: SDK 2.15.0
    * 기존의 모든 이벤트 시스템을 통합하는 GamebaseEventHandler 추가
        * ServerPush, Observer 기능을 포함하고 있고, 프로모션 결제 이벤트 및 푸시 이벤트 확인 가능
    * API 추가
    	* 상품 ID로 결제 요청하고 추가 정보(UserPayload)를 입력해 결제 완료 시 확인 가능한 결제 API 추가
    	* 이미지 공지 표시: showImageNotices
    	* Push 토큰 정보 확인: queryTokenInfo
    * 푸시 토큰 등록 시 NotificationOption 설정으로 앱이 포그라운드(foreground) 상태에서도 푸시 알림을 받을 수 있도록 기능 추가
    * WebViewConfiguration contentMode 설정 추가
    
#### 기능 개선/변경
* [SDK] 2.17.1
    * (iOS) 특정 지표 전송 시 오류 메시지를 추가하여 전송: 푸시 등록에 실패 시, 게임 지표 전송 시
    * (Unity) Unity 2017.2.5 지원
* [SDK] 2.15.0
    * (Unreal) TOAST SDK 업데이트: Android(0.23.0), iOS(0.26.0), Unity(0.21.0)    

#### 버그 수정
* [Console]
    * Analytics > 이용자 지표: 주간, 월간 평균 CCU 계산 로직 수정하여 비정상적으로 노출되는 문제 수정
    * Push > 푸시: 제목을 입력하지 않고 제목 글자색을 검은색이 아닌 색으로 설정하면 제목에 'null'이 표시되는 문제 수정
	* 쿠폰 > 쿠폰 발급: 발급된 쿠폰이 5만 개 이상인 경우 파일이 다운로드되지 않는 문제 수정
* [SDK] 2.17.1
    * (Unity) 이미지 공지와 웹뷰를 차례로 호출하면 뒤에 호출한 API가 동작하지 않는 오류 수정	
* [SDK] 2.15.0    
    * (Unreal) 결제 모듈에 ProGuard 선언이 누락된 오류 수정
