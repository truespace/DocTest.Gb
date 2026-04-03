---
source: unreal-started.md
section: "3rd-Party Provider SDK Settings"
order: 3
created_date: 2026-04-03
---

## 3rd-Party Provider SDK Settings

### Epic Games

* Epic Games의 기능을 사용하려면 Epic Online Services(EOS) SDK를 사용하여 로그인해야 합니다.
* Online Subsystem EOS 플러그인이 활성화되고, Engine.ini의 OnlineSubsystemEOS 섹션 내 bEnabled이 활성화된 경우 Online Subsystem EOS를 사용하는 것으로 간주합니다.

        [OnlineSubsystemEOS]
		bEnabled=True

* EOS SDK는 엔진 경로 내 `Engine/Source/ThirdParty/EOSSDK` 모듈을 사용합니다.
    * EOS SDK 업데이트 시 해당 모듈 내에서 필요한 플랫폼에 맞게 업데이트 바랍니다.
        * Windows: 최소 버전은 1.15.5으로 1.16.3 버전까지 확인되었습니다.
        * Android, iOS: 1.17.0-CL39599718 버전까지 확인되었습니다.
    * Online Subsystem EOS에서 [로그인 인증 타입](https://dev.epicgames.com/docs/api-ref/enums/eos-e-login-credential-type) 중 `PersistentAuth` 타입을 지원하려면 UE 4.27에서는 코드 수정이 필요합니다.
        * OnlineSubsystemEOS 모듈 내 UserManagerEOS.cpp 파일을 열어 `FUserManagerEOS::Login` 메서드 내에 AccountCredentials.Type의 스트링을 비교하는 조건문을 찾아 PersistentAuth 로그인을 위한 코드 추가가 필요합니다.

                else if (AccountCredentials.Type == TEXT("persistentauth"))
                {
                    // Use locally stored token managed by EOSSDK keyring to attempt login.
                    Credentials.Type = EOS_ELoginCredentialType::EOS_LCT_PersistentAuth;
                    Credentials.Id = nullptr;
                    Credentials.Token = nullptr;
                }

    * UE 4.27에서 Online Subsystem EOS를 사용 시 빌드 오류가 발생하므로 수정이 필요합니다.

        > EOS SDK의 핸들을 가져오기 위해 `OnlineSubsystemEOS.h` 헤더를 포함하게 되어 빌드 오류가 발생하므로 OnlineSubsystemEOS 플러그인의 Private 폴더 내 헤더 파일을 Public 폴더로 이동해 주는 과정이 필요합니다. (참고: [EOS 오류 관련 문의](https://eoshelp.epicgames.com/s/question/0D54z00007QIJjhCAH/cant-call-get-voice-chat-user-interface-from-game-instance-using-the-eos-plugin-and-eos-voice-plugins-on-unreal-engine4?language=en_US))
        > - SocketSubsystemEOS.h 
        > - EOSSettings.h
        > - EOSHelpers.h
        > - [Platform]/[Platform]EOSHelpers.h

    * Online Subsystem EOS를 사용하지 않을 시 EOSSDK 모듈을 이용해 따로 EOS 초기화를 진행하여 EOS SDK의 플랫폼 핸들을 설정해야 합니다.
        * Gamebase에서는 Epic Games 인증 및 스토어 설정에 따라 필요한 기능만 호출하며 EOS SDK의 필수 라이프 사이클은 게임에서 직접 호출해야 합니다. 
        * 플랫폼 핸들 설정을 위한 모듈 추가

                PrivateDependencyModuleNames.AddRange(
                    new[]
                    {
                        "GamebaseSharedEOS"
                    }
                );

        * 플랫폼 핸들 설정

                #include "GamebaseSharedEOS.h"

                void USample::SetEosPlatformHandle(UGameInstance* GameInstance, EOS_HPlatform PlatformHandle)
                {
                    if (const auto GamebaseSharedEOS = UGameInstance::GetSubsystem<UGamebaseSharedEOS>(GameInstance))
                    {
                        // EOS SDK 초기화 후 플랫폼 핸들을 가져와 Gamebase SDK로 전달
                        GamebaseSharedEOS->SetPlatformHandle(PlatformHandle);
                    }
                }
    
    * Android 지원 시, 로그인 응답을 받기 위해 [EOS SDK 가이드](https://dev.epicgames.com/docs/epic-online-services/platforms/android#7-how-to-receive-login-callback)를 참고하여 엔진 내 EOSSDK 모듈 내 `EOSSDK_strings.xml` 파일에 해당하는 값을 등록해야 합니다.

            <?xml version="1.0" encoding="utf-8"?>
            <resources>
                <!-- EOS SDK requires the Client ID to be in lowercase. -->
                <string name="eos_login_protocol_scheme">eos.yourclientidhere</string>
            </resources>
