---
source: unreal-initialization.md
section: "Initialize"
order: 4
split: true
created_date_time: 20260408_184906
keyword: Unreal, Initialize, Error
---

### Initialize

SDK를 초기화합니다.

**API**

Supported Platforms
<span style="color:#0E8A16; font-size: 10pt">■</span> UNREAL_ANDROID
<span style="color:#1D76DB; font-size: 10pt">■</span> UNREAL_IOS
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNREAL_WINDOWS

```cpp
void Initialize(const FGamebaseConfiguration& Configuration, const FGamebaseLaunchingInfoDelegate& Callback);
```

**Example**

```cpp
void USample::Initialize(const FString& AppID, const FString& AppVersion)
{
    FGamebaseConfiguration Configuration;
    Configuration.AppID = AppID;
    Configuration.AppVersion = AppVersion;
    Configuration.StoreCode = GamebaseStoreCode::Google;
    Configuration.bEnablePopup = true;
    Configuration.bEnableLaunchingStatusPopup = true;
    Configuration.bEnableBanPopup = true;

    UGamebaseSubsystem* Subsystem = UGameInstance::GetSubsystem<UGamebaseSubsystem>(GetGameInstance());
    Subsystem->Initialize(Configuration, FGamebaseLaunchingInfoDelegate::CreateLambda([](const FGamebaseLaunchingInfo* LaunchingInfo, const FGamebaseError* Error)
    {
        if (Gamebase::IsSuccess(Error))
        {
            UE_LOG(LogTemp, Display, TEXT("Initialize succeeded."));
        
            // Following notices are registered in the Gamebase Console
            auto Notice = LaunchingInfo->Launching.Notice;
            if (Notice != null)
            {
                if (string.IsNullOrEmpty(Notice.message) == false)
                {
                    UE_LOG(LogTemp, Display, TEXT("title: %s"), Notice.title);
                    UE_LOG(LogTemp, Display, TEXT("message: %s"), Notice.message);
                    UE_LOG(LogTemp, Display, TEXT("url: %s"), Notice.url);
                }
            }
            
            // Status information of game app version set in the Gamebase Unreal SDK initialization.
            auto Status = LaunchingInfo->Launching.Status;
    
            // Game status code (e.g. Under maintenance, Update is required, Service has been terminated)
            // refer to GamebaseLaunchingStatus
            if (Status.Code == GamebaseLaunchingStatus::IN_SERVICE)
            {
                // Service is now normally provided.
            }
            else
            {
                switch (Status.Code)
                {
                    case GamebaseLaunchingStatus::RECOMMEND_UPDATE:
                    {
                        // Update is recommended.
                        break;
                    }
                    // ... 
                    case GamebaseLaunchingStatus::INTERNAL_SERVER_ERROR:
                    {
                        // Error in internal server.
                        break;
                    }
                }
            }
        }
        else
        {
            // Check the Error code and handle the Error appropriately.
            UE_LOG(LogTemp, Display, TEXT("Initialize failed."));
        }
    }));
}
```
