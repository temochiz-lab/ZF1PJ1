# URL一覧

対象アプリ: `zend-framework-1-crud-master`

## 主要URL

| URL                  | Controller#Action                  | HTTPメソッド   | 内容                                       | Controllerリンク | 画面再現 |
| -------------------- | ---------------------------------- | ---------- | ---------------------------------------- | --- | --- |
| `/`                  | `TicketController#indexAction`     | GET        | チケット一覧画面。ページング付きでチケットを表示する。              | 解説: [TicketController.php_解説.md](各ファイル解説/application/controllers/TicketController.php_解説.md)<br>ソース: [TicketController.php](../zend-framework-1-crud-master/application/controllers/TicketController.php) | [01_チケット一覧.png](画面再現/01_チケット一覧.png) |
| `/ticket/create`     | `TicketController#saveAction`      | GET / POST | チケット作成画面。POST時は新規登録を行う。                  | 解説: [TicketController.php_解説.md](各ファイル解説/application/controllers/TicketController.php_解説.md)<br>ソース: [TicketController.php](../zend-framework-1-crud-master/application/controllers/TicketController.php) | [02_チケット新規登録.png](画面再現/02_チケット新規登録.png) |
| `/ticket/edit/:id`   | `TicketController#editAction`      | GET        | チケット編集画面。`:id` は数字のみ。                    | 解説: [TicketController.php_解説.md](各ファイル解説/application/controllers/TicketController.php_解説.md)<br>ソース: [TicketController.php](../zend-framework-1-crud-master/application/controllers/TicketController.php) | [03_チケット編集.png](画面再現/03_チケット編集.png) |
| `/ticket/delete/:id` | `TicketController#deleteAction`    | GET        | チケット削除処理。`:id` は数字のみ。処理後は `/` にリダイレクトする。 | 解説: [TicketController.php_解説.md](各ファイル解説/application/controllers/TicketController.php_解説.md)<br>ソース: [TicketController.php](../zend-framework-1-crud-master/application/controllers/TicketController.php) | 専用画面なし。処理後に `/` へ戻る。 |
| `/ticket/cvsexport`  | `TicketController#cvsexportAction` | GET        | チケット一覧をCSV出力する。画面描画は行わない。                | 解説: [TicketController.php_解説.md](各ファイル解説/application/controllers/TicketController.php_解説.md)<br>ソース: [TicketController.php](../zend-framework-1-crud-master/application/controllers/TicketController.php) | 画面なし。CSVを直接出力する。 |

## ページングURL

| URL | Controller#Action | 内容 |
| --- | --- | --- |
| `/?page=1` | `TicketController#indexAction` | 一覧の1ページ目を表示する。 |
| `/?page=2` | `TicketController#indexAction` | 一覧の2ページ目を表示する。 |
| `/?page={page}` | `TicketController#indexAction` | 指定ページを表示する。`controls.phtml` のページングリンクで使用される。 |

## 画面からリンクされているURL

| 表示箇所 | URL | 内容 |
| --- | --- | --- |
| ナビゲーションのブランドリンク | `/` | 一覧画面へ戻る。 |
| ナビゲーションの `Add Ticket` | `/ticket/create` | チケット作成画面へ移動する。 |
| ナビゲーションの `CVS export` | `/ticket/cvsexport` | CSV出力を実行する。 |
| 一覧画面の `Edit` | `/ticket/edit/{id}` | 対象チケットの編集画面へ移動する。 |
| 一覧画面の `Delete` | `/ticket/delete/{id}` | 対象チケットを削除する。 |

## フォーム送信先

| 画面 | action属性 | 内容 |
| --- | --- | --- |
| 作成画面 | 現在のURL | `/ticket/create` にPOSTして新規登録する。 |
| 編集画面 | `/ticket/create` | hidden項目の `id` を含めてPOSTし、`saveAction` 側で更新として処理する。 |

## ルート定義上の注意

- `application/configs/routes.php` では、ルート名に `labs/create` などの名前が使われているが、実際のURLパターンは `ticket/create`、`ticket/edit/:id`、`ticket/delete/:id`、`ticket/cvsexport`。
- `/` は `index` コントローラではなく `ticket/index` に割り当てられている。
- `IndexController#indexAction` も存在するが、通常のトップページ `/` からは使われない。
- `deleteAction` はGETで削除を実行しているため、実運用ではPOSTや確認画面を挟む設計が望ましい。
