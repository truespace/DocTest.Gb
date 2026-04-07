---
source: aos-ui.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Maintenance, Custom Maintenance Page"
section: "Custom Maintenance Page"
order: 8
---

## Custom Maintenance Page

점검 상태에서 '자세히 보기'를 클릭하면 표시되는 점검 페이지를 변경할 수 있습니다.

* 사용자 지정 웹 페이지를 점검 페이지로 등록
    * AndroidManifest.xml에 com.gamebase.maintenance.detail.url를 키 값으로 하는 meta-data를 설정합니다.
    * android:value 값으로 .html 파일 또는 URL을 입력할 수 있습니다.

```xml
<meta-data
	android:name="com.gamebase.maintenance.detail.url"
	android:value="file:///android_asset/html/gamebase-maintenance.html"/>
```
