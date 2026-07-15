# save.phtml 解説

対象ファイル: `application/views/scripts/ticket/save.phtml`

ソース: [application/views/scripts/ticket/save.phtml](../../../../../../zend-framework-1-crud-master/application/views/scripts/ticket/save.phtml)

## 役割

チケット新規登録フォームのView。

## 主な内容

- `blogTopicForm` のactionを現在URLに設定する。
- `Post Topic` 送信ボタンを追加する。
- フォーム全体をechoしてHTMLを出力する。

## 関連ファイル

- `application/forms/TopicBootstrapForm.php`
- `application/controllers/TicketController.php`

## 注意点

- フォームHTMLの大部分はZend_Formが生成する。

## 詳細

チケット新規登録画面のViewテンプレート。

Controllerから渡された `blogTopicForm` を表示する。フォームの送信先は現在のURLに設定されるため、`/ticket/create` をGETで開くとフォーム表示、POSTすると同じActionで登録処理になる。

フォーム自体の項目やバリデーションは `TopicBootstrapForm` に定義されている。このViewは主にフォームの配置と送信先設定を担当する薄いテンプレート。
