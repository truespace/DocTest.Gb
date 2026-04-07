---
source: unreal-ui.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal SDK 사용 가이드, UI, GameNotice, Open GameNotice"
section: GameNotice
order: 1
---

## Game > Gamebase > Unreal SDK 사용 가이드 > UI

## GameNotice

콘솔에 이미지와 함께 등록한 공지 사항을 표시하는 기능입니다.

![GameNotice Example](./image/gameNotice_guide_001.png)
<!-- LLM_Image_DESC_20260406
    유형: UI
    내용: 게임 내 공지사항 화면 예시
    구성: 모바일 화면에 Notice 제목의 공지사항 목록이 표시됨. Gamebase 로고와 설명 배너, 글로벌 진출 안내 배너, NHN GamePlatform 홍보 배너 등 여러 공지 항목이 카드 형태로 세로 나열됨
    Keyword: 게임공지, GameNotice, 공지사항, UI, Gamebase
-->

### Open GameNotice

게임 공지를 화면에 표시합니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS


```cpp
void OpenGameNotice(const FGamebaseErrorDelegate& Callback);
```

**ErrorCode**

| Error                                | Error Code | Description |
|--------------------------------------| --- | --- |
| NOT\_INITIALIZED                     | 1 | Gamebase가 초기화되어 있지 않습니다. |
| UI\_GAME\_NOTICE\_FAIL\_INVALID\_URL            | 6941 | 게임 공지 URL 생성에 실패했습니다. |
| UI\_GAME\_NOTICE\_FAIL\_ANDROID\_DUPLICATED\_VIEW | 6942 | 게임 공지 팝업을 종료하기 전에 다시 게임 공지를 호출했습니다. |
| WEBVIEW\_TIMEOUT                | 7002 | 웹뷰 표시 시간이 초과되었습니다.(10초) |
| WEBVIEW\_HTTP\_ERROR                 | 7003 |  웹뷰 내부에서 HTTP 에러가 발생했습니다. |
| WEBVIEW\_UNKNOWN\_ERROR           | 7999 | 알 수 없는 웹뷰 에러가 발생했습니다. |

**Example**

```cpp
void USample::OpenGameNotice()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->GetGameNotice()->OpenGameNotice(
        FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error) {
            // Called when the entire imageNotice is closed.
            ...
        })
    );
}
```
