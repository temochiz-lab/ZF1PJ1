# Multiples.php 解説

対象ファイル: `application/helpers/Multiples.php`

ソース: [application/helpers/Multiples.php](../../../../zend-framework-1-crud-master/application/helpers/Multiples.php)

## 役割

Action Helperのサンプルまたはテスト用クラス。

## 主な内容

- `direct($a)` は4倍、`thrice($a)` は2倍を返す。
- TicketController内にコメントアウトされた呼び出し例がある。

## 関連ファイル

- `application/controllers/TicketController.php`

## 注意点

- 現在の主要処理では使われていない。

## 詳細

Action Helperのサンプル的なクラス。

`direct($a)` は `$a * 4`、`thrice($a)` は `$a * 2` を返す。名前と処理内容が一致していない部分もあり、業務処理というよりHelper呼び出しの動作確認用に近い。

`TicketController` 内にはコメントアウトされた呼び出し例があるが、現在のチケットCRUD処理では使われていない。
