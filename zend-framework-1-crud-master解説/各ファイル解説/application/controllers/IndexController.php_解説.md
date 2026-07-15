# IndexController.php 解説

対象ファイル: `application/controllers/IndexController.php`

ソース: [application/controllers/IndexController.php](../../../../zend-framework-1-crud-master/application/controllers/IndexController.php)

## 役割

Zend Frameworkの標準生成に近いIndexController。

## 主な内容

- `indexAction()` は空のまま。
- 通常のトップページ `/` はroutes.phpでTicketControllerへ割り当てられている。

## 関連ファイル

- `application/views/scripts/index/index.phtml`
- `application/configs/routes.php`

## 注意点

- このアプリの主要導線では使われていない。

## 詳細

ZF1標準構成で作られたトップ用Controllerだが、このアプリでは主要導線では使われていない。

`routes.php` で `/` が `ticket/index` に割り当てられているため、通常アクセス時のトップ画面は `TicketController#indexAction()` が担当する。

`indexAction()` 自体は空に近く、対応する `application/views/scripts/index/index.phtml` も初期テンプレートに近い。残っているが、チケットCRUDの本流ではないファイルとして扱う。
