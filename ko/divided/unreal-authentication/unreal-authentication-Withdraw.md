---
source: unreal-authentication.md
section: "Withdraw"
order: 3
created_date: 2026-04-03
---

## Withdraw

로그인 상태에서 탈퇴를 시도합니다.

* 탈퇴 성공 시
  * 로그인했던 IdP의 게임 이용자 데이터는 삭제됩니다.
  * 해당 IdP로 다시 로그인할 수 있으며, 새로운 게임 이용자 데이터를 생성합니다.
  * 연동 중인 모든 IdP가 로그아웃 처리됩니다.
* Gamebase 탈퇴를 의미하며, IdP 계정 탈퇴를 의미하지는 않습니다.

> <font color="red">[주의]</font><br/>
>
> 여러 IdP를 연동 중인 경우, 모든 IdP 연동이 해제되고 Gamebase 유저 데이터가 삭제됩니다.
>

**API**

Supported Platforms

<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void Withdraw(const FGamebaseErrorDelegate& Callback);
```

**Example**

```cpp
void USample::Withdraw()
{
    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Withdraw(FGamebaseErrorDelegate::CreateLambda([](const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("Withdraw succeeded."));
        }
        else
        {
            UE_LOG(LogTemp, Display, TEXT("Withdraw failed. (errorCode: %d, errorMessage: %s)"), Error->Code, *Error->Message);
        }
    }));
}
```
