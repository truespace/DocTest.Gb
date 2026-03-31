## Game > Gamebase > Unity SDK 사용 가이드 > 초기화

### Handling Unregistered Version
 	 
Gamebase 콘솔에 등록되지 않은 GameClientVersion 을 초기화를 하면 **LAUNCHING_UNREGISTERED_CLIENT(2004)** 에러가 발생합니다.
enablePopup(true), enableLaunchingStatusPopup(true) 상태라면 강제 업데이트 팝업 창이 표시되고, 마켓으로 이동할 수 있습니다.
Gamebase 팝업을 사용하지 않을 경우에는 마켓 URL과 같은 Udpate정보를 GamebaseError 객체로부터 얻을 수 있습니다.

**VO**

```cs
public class UpdateInfo {
	// 최신 버전을 다운로드 할 수 있는 스토어 설치 URL.
	string installUrl;
    // 사용자에게 노출할 수 있는 메시지로 사용자의 단말기 언어에 맞게 전달됩니다.
    // 만일 언어가 'ko'인 경우 메시지는 아래와 같습니다.
    // '지원하지 않는 버전입니다. 최신 버전으로 업데이트해 주세요.'
    string message;
}
```

**API**

Supported Platforms
<span style="color:#1D76DB; font-size: 10pt">■</span> UNITY_IOS
<span style="color:#0E8A16; font-size: 10pt">■</span> UNITY_ANDROID
<span style="color:#F9D0C4; font-size: 10pt">■</span> UNITY_STANDALONE
<span style="color:#5319E7; font-size: 10pt">■</span> UNITY_WEBGL
<span style="color:#B60205; font-size: 10pt">■</span> UNITY_EDITOR

```cs
GamebaseResponse.Launching.UpdateInfo GamebaseResponse.Launching.UpdateInfo.From(GamebaseError error);
```

**Example**

```cs
public class SampleInitialization
{
    public void Initialize()
    {
        var configuration = new GamebaseRequest.GamebaseConfiguration();
        configuration.appID = "appID";
        configuration.appVersion = "appVersion;"
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

        Gamebase.Initialize(configuration, (launchingInfo, error) =>
        {
            if (Gamebase.IsSuccess(error) == true)
            {
                // Gamebase initialization succeeded.
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
                        // Unregistered game client version.
                        // Open market url to update application.
                        string installUrl = updateInfo.installUrl; // Market URL.
                        string message updateInfo.message; // Message from launching server.
                    }
                }
            }
        });
    }
}
```
