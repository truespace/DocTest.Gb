---
source: oper-customer-service.md
split: true
created_date_time: 20260406_141859
keyword: "Console, Contact, Email Config"
section: "Email Config"
order: 6
---

## Email Config
문의 처리가 완료되었을 경우 유저에게 발송할 이메일 형식을 설정할 수 있습니다.
최초에 활성화 시켰을 경우 기본 템플릿이 제공되며 이후 Text editor를 통해 원하는 형태로 얼마든지 수정하실 수 있습니다.

테스트 발송 기능이 제공되며 해당 기능을 통해 현재 입력한 템플릿을 이용하여 실제 유저에게 어떤 형태로 전송되는지 미리 확인할 수 있습니다.

![gamebase_ban_01_201812](./image/gamebase_template_03_ko_240105.jpg)
<!-- LLM_Image_DESC_20260406
    유형: Screenshot
    내용: Gamebase 고객센터 - 이메일 설정 화면
    구성: 상단에 '이메일 설정' 제목과 테스트 발송 버튼이 있음. 발신자 이름, 발신 주소 입력란이 있고, 내용 영역에 텍스트 에디터가 배치되어 이메일 템플릿을 편집할 수 있음. 하단에 SPF 설정 안내 문구와 취소/저장 버튼이 배치됨
    Keyword: 이메일 설정, 발신 주소, 템플릿, 텍스트 에디터, SPF
-->

> [참고]
> 발신 주소에 설정된 이메일이 SPF 레코드가 설정되지 않았을 경우에는 해당 메일이 스팸 처리 될 수 있습니다. 
> 그러므로 반드시 아래의 값을 DNS의 TXT레코드에 먼저 등록 후 발신주소에 설정해 주셔야 합니다.
> 추가 값 : v=spf1 include:_spfblocka.toast.com ~all
