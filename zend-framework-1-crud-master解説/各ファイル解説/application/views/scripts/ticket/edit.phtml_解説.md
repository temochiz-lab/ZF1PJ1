# edit.phtml 解説

対象ファイル: `application/views/scripts/ticket/edit.phtml`

ソース: [application/views/scripts/ticket/edit.phtml](../../../../../../zend-framework-1-crud-master/application/views/scripts/ticket/edit.phtml)

## 役割

チケット編集フォームのView。

## 主な内容

- `blogTopicEditForm` のactionを `/ticket/create` に設定する。
- `Update Ticket` 送信ボタンを追加する。
- フォーム全体をechoしてHTMLを出力する。

## 関連ファイル

- `application/controllers/TicketController.php`
- `application/forms/TopicBootstrapForm.php`

## 注意点

- 更新処理は `/ticket/create` の `saveAction()` で行われる。

## 詳細

チケット編集画面のViewテンプレート。

Controllerから渡された `blogTopicEditForm` を表示する。フォームの送信先は `ticket/create` に設定され、hiddenの `id` を追加することで、保存処理側では新規ではなく更新として扱われる。

つまり編集画面専用の保存Actionはなく、`saveAction()` に登録と更新を集約している。画面の見た目は `TopicBootstrapForm` の定義に強く依存する。
