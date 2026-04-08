---
source: upgrade-guide.md
section: "2.2.2"
order: 58
split: true
created_date_time: 20260408_191848
keyword: Unity, Upgrade Guide, 2.2.2
---

## 2.2.2

### Unity

* GamebaseUnitySDKSettings 클래스의 **storeCodeAOS** 변수명이 **storeCodeAndroid**로 변경되었습니다.
    * **storeCodeAOS**를 참조하여 Store Code를 정의하는 코드나 Prefab이 있다면 변수 참조에 실패하므로 **storeCodeAndroid** 변수로 변경하시기 바랍니다.
