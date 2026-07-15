# Bootstrap.php 解説

対象ファイル: `application/Bootstrap.php`

ソース: [application/Bootstrap.php](../../../zend-framework-1-crud-master/application/Bootstrap.php)

## 役割

Zend Frameworkアプリの初期化処理。

## 主な内容

- `_initDoctype()` でViewのdoctypeを `XHTML1_STRICT` に設定する。
- `_initRoutes()` でRouterを取得し、`configs/routes.php` を読み込む。
- `_initUploadDirAndConstant()` で `application/uploads` を用意し、`UPLOAD_PATH` を定義する。

## 関連ファイル

- `application/configs/routes.php`
- `application/configs/application.ini`

## 注意点

- アップロード先ディレクトリがない場合は作成する。

## 詳細

ZF1アプリ起動時の初期化クラス。

`_initDoctype()` ではViewを初期化し、DOCTYPEを `XHTML1_STRICT` に設定する。これによりレイアウトやView側で `$this->doctype()` を出力できる。

`_initRoutes()` ではAction Helperの探索パスを追加し、Front ControllerからRouterを取得して `application/configs/routes.php` を読み込む。URLとController/Actionの対応はここから登録される。

`_initUploadDirAndConstant()` ではアップロード先パスを定数として使えるようにする役割を持つ。`TopicBootstrapForm` のファイル要素や `TicketController` のアップロード処理がこの定数に依存する。
