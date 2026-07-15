# ----TopicForm.php 解説

対象ファイル: `application/forms/----TopicForm.php`

ソース: [application/forms/----TopicForm.php](../../../../zend-framework-1-crud-master/application/forms/----TopicForm.php)

## 役割

旧版または未使用と思われるフォームクラス。

## 主な内容

- `Application_Form_TopicForm` を定義する。
- `dataname`、`explanation`、`important` など、現在のticketsカラムとは名前が合わない項目を持つ。
- チケットCRUDの主要処理では `TopicBootstrapForm.php` が使われている。

## 関連ファイル

- `application/forms/TopicBootstrapForm.php`

## 注意点

- ファイル名先頭に `----` があり、退避・旧版ファイルの可能性が高い。

## 詳細

旧版または未使用と思われるフォームクラス。

項目名が `dataname`、`explanation`、`important` などになっており、現在の `tickets` テーブルの `title`、`notes`、`priority` とは対応していない。

現在の `TicketController` では `TopicBootstrapForm` が使われているため、このファイルは実行経路に入らない。サンプルや流用元コードの残りとして見る。
