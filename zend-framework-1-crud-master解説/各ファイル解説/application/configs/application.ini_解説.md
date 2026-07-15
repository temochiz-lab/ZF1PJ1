# application.ini 解説

対象ファイル: `application/configs/application.ini`

ソース: [application/configs/application.ini](../../../../zend-framework-1-crud-master/application/configs/application.ini)

## 役割

アプリケーション設定ファイル。

## 主な内容

- PHPエラー表示、Bootstrapクラス、Controllerディレクトリを設定する。
- LayoutとViewリソースを有効にする。
- MySQL接続情報を定義する。

## 関連ファイル

- `public/index.php`
- `application/Bootstrap.php`
- `zf1app_db.sql`

## 注意点

- DBユーザーは `root`、パスワード空文字のローカル開発向け設定。

## 詳細

アプリ全体の環境別設定ファイル。

`production` セクションでは、PHP設定、Bootstrapクラス、Controller配置場所、Layout配置場所、View初期化、DB接続情報を定義している。DBは `PDO_MySQL`、DB名は `zf1app_db`、文字コードは `utf8`。

`staging`、`testing`、`development` は `production` を継承する形になっている。開発環境では例外表示が有効になっており、エラー発生時に詳細を画面で確認しやすい。

このファイルのDB設定と `zf1app_db.sql` の内容が対応しており、`TicketMapper` からのDB操作はこの接続設定を使って実行される。
