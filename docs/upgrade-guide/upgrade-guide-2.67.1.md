---
source: upgrade-guide.md
split: true
created_date_time: 20260406_141859
keyword: "Purchase, 2.67.1, Unreal"
section: 2.67.1
order: 12
---

## 2.67.1

### Unreal

* (Windows) Purchase 설정 시 스토어를 하나만 선택할 수 있도록 변경되었습니다.
    * 스토어 재설정이 필요합니다.
* (Windows) Epic Games Store 사용 시 EOS SDK의 핸들을 등록하는 과정이 변경되었습니다.
    * Online Subsystem EOS를 사용하는 경우 Gamebase 초기화 시 StoreCode가 Epic Games Store의 해당하는 값이면 자동으로 핸들을 등록합니다.
    * Online Subsystem EOS를 사용하지 않는 경우 [Windows Settings](../unreal-started.md#windows-settings) 가이드를 참고하여 EOS의 핸들을 등록하는 과정이 필요합니다.
* (Windows) Steamworks SDK 지원 버전이 1.59로 변경되었습니다.
    * [Steamworks 업그레이드 가이드](../unreal-started.md#windows-settings)를 확인하여 업데이트가 필요합니다.
