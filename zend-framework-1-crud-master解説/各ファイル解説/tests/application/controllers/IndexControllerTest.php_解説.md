# IndexControllerTest.php 解説

対象ファイル: `tests/application/controllers/IndexControllerTest.php`

ソース: [tests/application/controllers/IndexControllerTest.php](../../../../../zend-framework-1-crud-master/tests/application/controllers/IndexControllerTest.php)

## 役割

IndexController用のテストクラス雛形。

## 主な内容

- `Zend_Test_PHPUnit_ControllerTestCase` を継承する。
- `setUp()` で `Zend_Application` を作成する。

## 関連ファイル

- `application/controllers/IndexController.php`
- `tests/bootstrap.php`

## 注意点

- 具体的なテストメソッドはまだ書かれていない。

## 詳細

`IndexController` 用のControllerテスト雛形。

ZF1のControllerTestCase系の構成で、リクエストを投げてレスポンスやController/Actionの到達を確認するためのファイル。ただし現在のトップページは `routes.php` により `TicketController#indexAction()` に向いているため、このテストは主要導線とずれている可能性がある。

実用的なテストにするなら、`/` が `ticket/index` に到達すること、`/ticket/create` がフォームを表示することなどを追加するとよい。
