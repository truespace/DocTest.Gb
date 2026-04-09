---
source: aos-started.md
section: "Environments"
order: 1
split: true
created_date_time: 20260408_184906
keyword: Android, Login, Purchase, Push, Gradle
---

## Game > Gamebase > Android SDK 사용 가이드 > 시작하기

## Environments

Android에서 Gamebase를 사용하기 위한 시스템 환경은 다음과 같습니다.

> [최소 사양]
>
> * 사용자 실행 환경: Android API 22(Lollipop MR1, OS 5.1) 이상
> * 빌드 환경: Android Gradle Plugin 7.4.2 이상
> * 개발 환경: Android Studio

### Dependencies

| Gamebase SDK | Gamebase Adapter | External SDK | 용도 | minSdkVersion |
| --- | --- | --- | --- | --- |
| Gamebase | gamebase-sdk | nhncloud-core-1.12.0<br>nhncloud-common<br>nhncloud-crash-reporter-ndk<br>nhncloud-logger<br>gson-2.8.9<br>okhttp-3.12.13<br>kotlin-stdlib-1.8.0<br>kotlin-stdlib-jdk8<br>kotlinx-coroutines-core-1.6.4<br>kotlinx-coroutines-android<br>age-signals-0.0.2 | Gamebase의 인터페이스 및 핵심 로직을 포함 | API 22(Lollipop MR1, OS 5.1) |
| Gamebase Auth Adapters | gamebase-adapter-auth-appleid | - | Sign In With Apple 로그인을 지원 | - |
|  | gamebase-adapter-auth-facebook | facebook-login-18.0.0 | Facebook 로그인을 지원 | - |
|  | gamebase-adapter-auth-google | credentials-play-services-auth-1.3.0<br>play-services-auth-20.3.0 | Google 로그인을 지원 | - |
|  | gamebase-adapter-auth-gpgs-v2 | play-services-games-v2-20.1.2 | GPGS(Google Play Games Services) V2 로그인을 지원<br>Player ID 기반 | - |
|  | gamebase-adapter-auth-gpgs-autologin | play-services-games-v2-20.1.2 | GPGS(Google Play Games Services) 자동 로그인을 지원 | - |
|  | gamebase-adapter-auth-hangame | hangame-id-1.17.3 | Hangame 로그인을 지원 | - |
|  | gamebase-adapter-auth-line | linesdk-5.8.1 | LINE 로그인을 지원 | - |
|  | gamebase-adapter-auth-naver | naveridlogin-android-sdk-5.8.0 | NAVER 로그인을 지원 | - |
|  | gamebase-adapter-auth-payco | payco-login-1.5.17 | PAYCO 로그인을 지원 | - |
|  | gamebase-adapter-auth-twitter | - | Twitter 로그인을 지원 | API 25(Nougat, OS 7.1.1) |
|  | gamebase-adapter-auth-weibo | sinaweibosdk.core-13.10.5 | Weibo 로그인을 지원 | - |
|  | gamebase-adapter-auth-kakaogame | kakaogame.idp_kakao-3.19.3<br>kakaogame.gamesdk-3.19.3<br>kakaogame.common-3.19.3<br>kakao.sdk.v2-auth-2.17.0<br>kakao.sdk.v2-partner-auth-2.17.0<br>kakao.sdk.v2-common-2.17.0<br>play-services-ads-identifier-17.0.0 | Kakao 로그인을 지원 | API 23(Marshmallow, OS 6.0) |
|  | gamebase-adapter-auth-steam | - | Steam 로그인을 지원 | API 25(Nougat, OS 7.1.1) |
| Gamebase IAP Adapters | gamebase-adapter-toastiap | nhncloud-iap-core | 게임 내 결제 지원 | - |
|  | gamebase-adapter-purchase-galaxy | nhncloud-iap-galaxy | Samsung Galaxy Store를 지원 | - |
|  | gamebase-adapter-purchase-google | billing-7.1.1<br>nhncloud-iap-google | Google Play를 지원 | API 24(Nougat, OS 7.0)<br>API 23 이하 지원을 위해서는 [desugaring 선언](https://developer.android.com/studio/write/java8-support#library-desugaring) 필요 |
|  | gamebase-adapter-purchase-huawei | nhncloud-iap-huawei | Huawei AppGallery를 지원 | - |
|  | gamebase-adapter-purchase-onestore | nhncloud-iap-onestore | ONE store v17을 지원 | - |
|  | gamebase-adapter-purchase-onestore-v19 | nhncloud-iap-onestore-v19 | ONE store v19를 지원 | - |
|  | gamebase-adapter-purchase-onestore-v21 | nhncloud-iap-onestore-v21 | ONE store v21을 지원 | API 23(Marshmallow, OS 6.0) |
|  | gamebase-adapter-purchase-onestore-external | nhncloud-iap-onestore-external | ONE store 외부 결제 기능을 지원 | - |
|  | gamebase-adapter-purchase-mycard | nhncloud-iap-mycard | MyCard 결제 기능을 지원 | - |
| Gamebase Push Adapters | gamebase-adapter-toastpush | nhncloud-push-analytics<br>nhncloud-push-core<br>nhncloud-push-notification | Push를 지원 | - |
|  | gamebase-adapter-push-fcm | firebase-messaging-17.6.0<br>nhncloud-push-fcm | Firebase Cloud Messaging을 지원 | - |
