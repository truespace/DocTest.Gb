---
source: unity-initialization.md
section: "Initialize"
order: 3
created_date: 2026-04-03
---

### Initialize

SDK를 초기화 합니다.

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#5319E7; font-size: 10pt">■</span> UNITY_WEBGL
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
static void Initialize(GamebaseRequest.GamebaseConfiguration configuration, GamebaseCallback.GamebaseDelegate<GamebaseResponse.Launching.LaunchingInfo> callback)
```

**Example**

```cs
public class SampleInitialization
{
    public void Initialize()
    {
        /**
         * Show gamebase debug message.
         * set 'false' when build RELEASE.
         */
        Gamebase.SetDebugMode(true);

        /**
         * Gamebase Configuration.
         */
        var configuration = new GamebaseRequest.GamebaseConfiguration();
        configuration.appID = "appID";
        configuration.appVersion = "appVersion";
        configuration.displayLanguageCode = GamebaseDisplayLanguageCode.English;
    #if UNITY_ANDROID
        configuration.storeCode = GamebaseStoreCode.GOOGLE;
    #elif UNITY_IOS
        configuration.storeCode = GamebaseStoreCode.APPSTORE;
    #elif UNITY_WEBGL
        configuration.storeCode = GamebaseStoreCode.WEBGL;
    #elif UNITY_EDITOR_OSX || UNITY_STANDALONE_OSX
        configuration.storeCode = GamebaseStoreCode.MACOS;
    #else
        configuration.storeCode = GamebaseStoreCode.WINDOWS;
    #endif

        /**
         * Gamebase Initialize.
         */
        Gamebase.Initialize(configuration, (launchingInfo, error) =>
        {
            if (Gamebase.IsSuccess(error) == true)
            {
                Debug.Log("Initialization succeeded.");

                //Following notices are registered in the Gamebase Console
                var notice = launchingInfo.launching.notice;
                if (notice != null)
                {
                    if (string.IsNullOrEmpty(notice.message) == false)
                    {
                        Debug.Log(string.Format("title:{0}", notice.title));
                        Debug.Log(string.Format("message:{0}", notice.message));
                        Debug.Log(string.Format("url:{0}", notice.url));
                    }
                }
        
                //Status information of game app version set in the Gamebase Unity SDK initialization.
                var status = launchingInfo.launching.status;
        
                // Game status code (e.g. Under maintenance, Update is required, Service has been terminated)
                // refer to GamebaseLaunchingStatus
                if (status.code == GamebaseLaunchingStatus.IN_SERVICE)
                {
                    // Service is now normally provided.
                }
                else
                {
                    switch (status.code)
                    {
                        case GamebaseLaunchingStatus.RECOMMEND_UPDATE:
                        {
                            // Update is recommended.
                            break;
                        }
                        // ... 
                        case GamebaseLaunchingStatus.INTERNAL_SERVER_ERROR:
                        {
                            // Error in internal server.
                            break;
                        }
                    }
                }
            }
            else
            {
                // Check the error code and handle the error appropriately.
                Debug.Log(string.Format("Initialization failed. error is {0}", error));

                if (error.code == GamebaseErrorCode.LAUNCHING_UNREGISTERED_CLIENT)
                {
                    GamebaseResponse.Launching.UpdateInfo updateInfo = GamebaseResponse.Launching.UpdateInfo.From(error);
                    if (updateInfo != null)
                    {
                        // Update is require.
                    }
                }
            }
        });
    }
}
```
