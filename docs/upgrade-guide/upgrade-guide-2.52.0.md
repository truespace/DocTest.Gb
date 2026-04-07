---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "IdP, 2.52.0, Android"
section: 2.52.0
order: 28
---

## 2.52.0

### Android

* Android 4.4(OS 19 Kitkat) 단말기에서 크래시가 발생합니다.
    * 이슈가 수정된 Gamebase Android SDK 2.52.1을 사용하시기 바랍니다.

### Unity

* '**IapOnestore**'로 표시되던 **ONE Store v17** 결제 어댑터가 Gamebase Setting Tool (v2.7.0)부터 '**IapOnestoreV17**'로 표시됩니다.

### iOS

#### Weibo IdP

* WeiboSDK가 3.3.3로 업데이트되면서 info.plist에 weibosdk3.3을 추가해야 합니다.
```
<key>LSApplicationQueriesSchemes</key>
<array>
    ...
    <string>weibosdk</string>
    <string>weibosdk2.5</string>
    <string>weibosdk3.3</string>
    ...
</array>
```

#### Changed/Deprecated APIs

* iOS 16.4부터 Apple이 CTCarrier class가 deprecated됨에 따라 아래 API들이 deprecated되었습니다.
    * **+[TCGBGamebase countryCode]**
    * **+[TCGBGamebase countryCodeOfUSIM]**
    * **+[TCGBGamebase carrierCode]**
    * **+[TCGBGamebase carrierName]**
    * **+[TCGBUtil countryCode]**
    * **+[TCGBUtil usimCountryCode]**
    * **+[TCGBUtil carrierCode]**
    * **+[TCGBUtil carrierName]**
