# TicketController.php 解説

対象ファイル: `application/controllers/TicketController.php`

ソース: [application/controllers/TicketController.php](../../../../zend-framework-1-crud-master/application/controllers/TicketController.php)

## 役割

チケットCRUDの中心Controller。

## 主な内容

- `indexAction()` でチケット一覧を取得し、ページングしてViewへ渡す。
- `saveAction()` で新規登録と更新を処理する。
- `editAction()` で編集フォームに既存データを入れる。
- `deleteAction()` で指定IDのチケットを削除する。
- `cvsexportAction()` でCSV出力を行う。

## 関連ファイル

- `application/models/TicketMapper.php`
- `application/forms/TopicBootstrapForm.php`
- `application/views/scripts/ticket/*.phtml`

## 関連テーブル

- [tickets](../../../08_データベース.md#tickets): 一覧取得、登録、編集、削除、CSV出力の対象テーブル。

## 注意点

- 削除がGETで実行されるため、実運用ではPOST化や確認画面が望ましい。

## 詳細

チケット機能のControllerで、一覧、登録、編集、削除、CSV出力をまとめて担当する。

`init()` ではFlashMessengerのメッセージをViewへ渡す。登録・更新・削除後の通知を画面に出すための準備になる。

`indexAction()` は `Application_Model_TicketMapper` から [tickets](../../../08_データベース.md#tickets) の全チケットを取得し、`Zend_Paginator` で1ページ5件に分割して `blogTopics` としてViewに渡す。表示側は `ticket/index.phtml` と `controls.phtml`。

`saveAction()` はGET時に新規登録フォームを表示し、POST時にバリデーション、ファイルアップロード、`Application_Model_Ticket` への詰め替え、`TicketMapper::saveTopic()` の呼び出しを行う。hiddenの `id` がある場合は更新、ない場合は新規登録として処理される。

`editAction()` はURLの `id` から既存データを取得し、フォームに値を入れて編集画面へ渡す。実際の保存先は `ticket/create` で、保存処理は `saveAction()` に集約されている。

`deleteAction()` は指定IDを `TicketMapper::deleteTopic()` に渡して削除し、一覧へリダイレクトする。GETで削除できるため、実運用ではPOST化や確認画面追加が必要。

`cvsexportAction()` は画面描画を止め、[tickets](../../../08_データベース.md#tickets) から作ったCSV用データを `Csv` Action Helperに渡してダウンロードレスポンスを直接作る。
