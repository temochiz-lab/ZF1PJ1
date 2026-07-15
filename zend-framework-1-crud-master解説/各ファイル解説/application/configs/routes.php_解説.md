# routes.php 解説

対象ファイル: `application/configs/routes.php`

ソース: [application/configs/routes.php](../../../../zend-framework-1-crud-master/application/configs/routes.php)

## 役割

URLとController/Actionの対応表。

## 主な内容

- `/` を `ticket/index` に割り当てる。
- `ticket/create` を `ticket/save` に割り当てる。
- `ticket/edit/:id`、`ticket/delete/:id`、`ticket/cvsexport` を定義する。

## 関連ファイル

- `application/controllers/TicketController.php`

## 注意点

- ルート名に `labs/create` などが残っており、URLの `ticket/...` とは命名がずれている。

## 詳細

URLパターンとController/Actionの対応を明示的に登録するファイル。

`/` は `ticket/index` に割り当てられているため、トップページでチケット一覧が表示される。`ticket/create`、`ticket/edit/:id`、`ticket/delete/:id`、`ticket/cvsexport` もここで登録されている。

`edit` と `delete` の `:id` には `\d+` の制約があり、数字だけを受け付ける。URLとしては `ticket/...` だが、ルート名には `labs/create` のような名前が使われており、名前と実URLが一致していない点は読み間違えやすい。

このファイルは `Bootstrap::_initRoutes()` から読み込まれる。
