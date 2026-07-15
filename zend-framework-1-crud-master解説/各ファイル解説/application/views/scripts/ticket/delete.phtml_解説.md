# delete.phtml 解説

対象ファイル: `application/views/scripts/ticket/delete.phtml`

ソース: [application/views/scripts/ticket/delete.phtml](../../../../../../zend-framework-1-crud-master/application/views/scripts/ticket/delete.phtml)

## 役割

削除Action用のView。

## 主な内容

- Blog/delete用の雛形文言が残っている。
- 実際の `deleteAction()` は削除後すぐ `/` にリダイレクトするため通常表示されない。

## 関連ファイル

- `application/controllers/TicketController.php`

## 注意点

- 実処理と文言が一致していないため、古い雛形の残骸と思われる。

## 詳細

削除用Viewテンプレートだが、現在の削除処理ではほぼ使われない。

`TicketController#deleteAction()` は削除処理後すぐに一覧へリダイレクトするため、削除確認画面や完了画面をこのテンプレートで表示する流れになっていない。

実運用向けにするなら、GETアクセス時にこのテンプレートで確認画面を表示し、POSTで削除確定する構成に変えると安全。
