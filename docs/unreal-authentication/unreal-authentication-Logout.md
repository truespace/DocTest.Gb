---
source: unreal-authentication.md
split: true
created_date_time: 20260406_141859
keyword: "Unreal, Logout, Error, GetSubsystem, GetGameInstance, IsSuccess"
section: Logout
order: 2
---

## Logout
로그인된 IdP에서 로그아웃을 시도합니다. 주로 게임의 설정 화면에 로그아웃 버튼을 두고, 버튼을 클릭하면 실행되도록 구현하는 경우가 많습니다.
로그아웃이 성공하더라도, 게임 유저 데이터는 유지됩니다.
로그아웃에 성공하면 해당 IdP로 인증했던 기록을 제거하므로 다음에 로그인할 때 ID, 비밀번호 입력 창이 나타납니다.<br/><br/>

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void Logout(const FGamebaseErrorDelegate& Callback);
```

**Example**

```cpp
void USample::Logout()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Logout(FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("Logout succeeded."));
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("Logout failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```
