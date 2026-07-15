# zf1app_db.sql 解説

対象ファイル: `zf1app_db.sql`

ソース: [zf1app_db.sql](../../zend-framework-1-crud-master/zf1app_db.sql)

## 役割

MySQL用のDB定義とサンプルデータ。

## 主な内容

- `tickets` テーブルを作成し、サンプルチケットを投入する。
- `users` テーブルも作成するが、現在のチケットCRUD処理では使われていない。
- データベース名はコメント上 `zf1app_db`。

## 関連ファイル

- `application/configs/application.ini`
- `application/models/DbTable/TicketDbTable.php`

## 注意点

- 外部キー定義はない。
- `users.password` には平文らしき値が入っている。

## 詳細

MySQL向けの初期データベース定義ファイル。

中心になるテーブルは `tickets` で、チケットCRUD画面の一覧・登録・編集・削除・CSV出力はこのテーブルを対象にしている。主なカラムは `id`、`title`、`notes`、`files`、`priority`、`created_at`、`updated_at`。

`users` テーブルも定義されているが、このプロジェクト内にはログイン処理やユーザー管理処理が揃っていないため、現在の主要CRUDとは直接つながっていない。`LoggedInUser` View Helperなど、別アプリから持ち込まれた名残と見るのが自然。

サンプルデータには `avatar92.jpg` などのアップロードファイル名が含まれており、`application/uploads` 配下の画像と対応している。
