# index.php 解説

対象ファイル: `public/index.php`

ソース: [public/index.php](../../../zend-framework-1-crud-master/public/index.php)

## 役割

アプリケーションのフロントコントローラ入口。

## 主な内容

- `APPLICATION_PATH` を `application` ディレクトリに設定する。
- `APPLICATION_ENV` を環境変数または `production` として設定する。
- `library` を include_path に追加し、`Zend/Application.php` を読み込む。
- `Zend_Application` を作成し、bootstrap後に実行する。

## 関連ファイル

- `application/configs/application.ini`
- `application/Bootstrap.php`

## 注意点

- 全リクエストは基本的にこのファイルを通ってZend Frameworkへ渡る。

## 詳細

Webアプリの入口になるフロントコントローラ。

`APPLICATION_PATH` と `APPLICATION_ENV` を定義し、`library` を `include_path` に追加してから `Zend_Application` を生成する。設定ファイルは `application/configs/application.ini`。

最後に `$application->bootstrap()->run()` を実行することで、Bootstrap初期化、ルーティング、Controller実行、View描画までのZF1の処理が始まる。

通常のURLアクセスは、Apacheの `.htaccess` によってこのファイルへ集約される。
