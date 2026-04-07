---
source: release-notes-android.md
split: true
created_date_time: 20260406_141859
keyword: "2.69.0 (2025. 01. 21.)"
section: "2.69.0 (2025. 01. 21.)"
order: 16
---

### 2.69.0 (2025. 01. 21.)

[SDK Download](https://static.toastoven.net/toastcloud/sdk_download/gamebase/v2.69.0/GamebaseSDK-Android.zip)

#### 기능 추가

* **Gamebase.requestLastLoggedInProvider(GamebaseDataCallback&lt;String&gt;) 비동기 API**를 추가했습니다.
    * **Gamebase.getLastLoggedInProvider() 동기 API**가 타이밍상 정상적인 값을 반환하지 못할 때가 있습니다.
    * **gamebase-adapter-auth-gpgs-autologin** 모듈을 빌드에 포함하는 경우 GPGS 서버에서 데이터를 획득하는 시간이 필요하므로 Gamebase 초기화 직후 getLastLoggedInProvider() 동기 API를 호출하면 정상적인 값을 획득할 수 없습니다.
    * 이때 requestLastLoggedInProvider(GamebaseDataCallback&lt;String&gt;) 비동기 API는 정확한 값을 보장합니다.
    * gamebase-adapter-auth-gpgs-autologin 모듈이 빌드에 포함되지 않은 경우에는 계속해서 getLastLoggedInProvider() 동기 API를 사용해도 무방합니다.
* **GamebaseWebViewConfiguration.Builder.setCutoutAreaColor() API**를 추가했습니다.
    * GamebaseWebView의 **GamebaseWebViewConfiguration.Builder.renderOutsideSafeArea() API**를 **false**로 설정한 경우, cutout 영역에 자동으로 padding 여백을 추가합니다.
    * setCutoutAreaColor()는 이렇게 추가된 padding 영역의 색을 설정할 수 있습니다.
    * renderOutsideSafeArea()를 false로 설정했지만 setCutoutAreaColor()는 설정하지 않는 경우에는 웹 페이지 'body'의 'background-color' 값으로 자동으로 padding 영역의 색상을 결정합니다.

#### 기능 개선/변경

* **gamebase-adapter-auth-gpgs-autologin** 모듈을 빌드에 포함하는 경우 Gamebase 초기화와 동시에 **Gamebase.getLastLoggedInProvider() 동기 API**를 호출하면 내부 데이터가 초기화가 완료되지 않아 null이 반환되었으나, 이 경우 **'NOT\_INITIALIZED\_YET'**이라는 문자열을 반환하도록 내부 로직을 변경했습니다.
* **GamebaseWebViewConfiguration.Builder.renderOutsideSafeArea() API**를 **false**로 설정한 경우에도 cutout 영역까지 웹뷰를 모두 표시하도록(**edge-to-edge**) 내부 로직을 변경했습니다.
    * 그 대신 자동으로 padding 여백을 추가하여 콘텐츠가 가려지지 않도록 했습니다.

#### 버그 수정
 
* 로그인 전에 Gamebase.Push.getNotificationOptions() API를 호출하는 경우 크래시가 발생하지 않도록 수정했습니다.
* Loading Progress가 간헐적으로 사라지지 않거나 크래시가 발생하는 이슈에 대한 방어 코드를 추가했습니다.
* WebSocket에서 간헐적으로 내부 콜백 함수가 중복으로 호출되어 발생하는 크래시에 대한 방어 코드를 추가했습니다.
