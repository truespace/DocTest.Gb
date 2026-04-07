---
source: aos-ui.md
split: true
created_date_time: 20260406_141859
keyword: "Android, Notice, TermsView, Error"
section: "Error Handling"
order: 9
---

## Error Handling

| Error                                             | Error Code | Description                                                                                 |
|---------------------------------------------------|------------|---------------------------------------------------------------------------------------------|
| NOT\_INITIALIZED                                  | 1          | Gamebase.initialize가 호출되지 않았습니다.                                                            |
| LAUNCHING\_SERVER\_ERROR                          | 2001       | 론칭 서버에서 전달 받은 항목에 약관 관련 내용이 없는 경우에 발생하는 에러입니다.<br/>정상적인 상황이 아니므로 Gamebase 담당자에게 문의하세요. |
| UI\_IMAGE\_NOTICE\_TIMEOUT                        | 6901       | 이미지 공지 팝업 창 표시 중 시간이 초과되어 모든 팝업 창을 강제 종료합니다. |
| UI\_IMAGE\_NOTICE\_NOT\_SUPPORTED\_OS             | 6902       | 롤링 타입의 경우 API 19 이하의 단말기에서는 이미지 공지를 지원하지 않습니다. |
| UI\_TERMS\_NOT\_EXIST\_IN\_CONSOLE                | 6921       | 약관 정보가 콘솔에 등록되어 있지 않습니다. |
| UI\_TERMS\_NOT\_EXIST\_FOR\_DEVICE\_COUNTRY       | 6922       | 단말기 국가코드에 맞는 약관 정보가 콘솔에 등록되어 있지 않습니다. |
| UI\_TERMS\_UNREGISTERED\_SEQ                      | 6923       | 등록되지 않은 약관 Seq 값을 설정하였습니다. |
| UI\_TERMS\_ALREADY\_IN\_PROGRESS\_ERROR           | 6924       | Terms API 호출이 아직 완료되지 않았습니다.<br/>잠시 후 다시 시도하세요. |
| UI\_TERMS\_ANDROID\_DUPLICATED\_VIEW              | 6925       | 약관 웹뷰가 아직 종료되지 않은 상태에서 다시 호출되었습니다 |
| UI\_GAME\_NOTICE\_FAIL\_INVALID\_URL              | 6941       | 게임 공지 URL 생성에 실패했습니다. |
| UI\_GAME\_NOTICE\_FAIL\_ANDROID\_DUPLICATED\_VIEW | 6942       | 게임 공지 팝업을 종료하기 전에 다시 게임 공지를 호출했습니다. |
| UI\_UNKNOWN\_ERROR                                | 6999       | 알 수 없는 오류입니다(정의되지 않은 오류입니다). |
| WEBVIEW\_TIMEOUT                                  | 7002       | 웹뷰 표시 시간이 초과되었습니다.(10초) |
| WEBVIEW\_HTTP\_ERROR                              | 7003       | 웹뷰 내부에서 HTTP 에러가 발생했습니다. |
| WEBVIEW\_UNKNOWN\_ERROR                           | 7999       | 알 수 없는 웹뷰 에러가 발생했습니다. |
| SERVER\_INVALID\_RESPONSE                         | 8003       | 서버가 유효하지 않은 응답을 반환했습니다. |

* 전체 오류 코드는 다음 문서를 참고하시기 바랍니다.
    * [오류 코드](../error-code.md#client-sdk)
