---
source: upgrade-guide.md
section: "2.81.4"
order: 1
split: true
created_date_time: 20260714_114945
keyword: Unity, Upgrade Guide, 2.81.4
---

## Game > Gamebase > Upgrade Guide

## 2.81.4

### Unity

* Gamebase Unity SDK 소스에 Assembly Definition(.asmdef)이 적용되어, SDK가 기본 어셈블리(Assembly-CSharp)에서 분리된 별도의 **Gamebase** 어셈블리로 컴파일됩니다.
    * Gamebase 어셈블리는 autoReferenced가 활성화되어 있으므로, 별도의 Assembly Definition을 사용하지 않는 프로젝트는 추가 설정 없이 기존과 동일하게 Gamebase API를 사용할 수 있습니다.
    * 게임 코드에서 자체 Assembly Definition(.asmdef)을 사용하는 경우, Gamebase API를 호출하는 어셈블리의 **Assembly Definition References**에 **Gamebase** 어셈블리를 추가해야 합니다.
