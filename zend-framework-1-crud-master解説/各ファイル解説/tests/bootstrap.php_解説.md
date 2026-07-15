# bootstrap.php 解説

対象ファイル: `tests/bootstrap.php`

ソース: [tests/bootstrap.php](../../../zend-framework-1-crud-master/tests/bootstrap.php)

## 役割

PHPUnitテスト用Bootstrap。

## 主な内容

- `APPLICATION_PATH` を定義する。
- `APPLICATION_ENV` を `testing` に設定する。
- `library` を include_path に追加し、ZendのAutoloaderを有効にする。

## 関連ファイル

- `tests/phpunit.xml`

## 注意点

- テスト実行時の初期化専用。

## 詳細

PHPUnit実行時の初期化ファイル。

テスト用に `APPLICATION_PATH`、`APPLICATION_ENV`、include_pathを設定し、Zend FrameworkのAutoloaderを初期化する。アプリ本体の `public/index.php` に近い準備をテスト環境向けに行う役割。

このファイル自体はWebアクセス時には読み込まれない。
