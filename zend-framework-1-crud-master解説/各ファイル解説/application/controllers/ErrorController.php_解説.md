# ErrorController.php 解説

対象ファイル: `application/controllers/ErrorController.php`

ソース: [application/controllers/ErrorController.php](../../../../zend-framework-1-crud-master/application/controllers/ErrorController.php)

## 役割

エラー表示用Controller。

## 主な内容

- ルートなし、Controllerなし、Actionなしを404として処理する。
- その他の例外を500相当のアプリケーションエラーとして処理する。
- 設定により例外情報やリクエストパラメータをViewへ渡す。

## 関連ファイル

- `application/views/scripts/error/error.phtml`

## 注意点

- ログリソースがある場合はエラー内容をログ出力する構成。

## 詳細

アプリ内で例外や存在しないURLが発生したときに呼び出されるController。

`errorAction()` は `error_handler` パラメータから例外情報を受け取り、エラー種別に応じて404または500を設定する。404系は「ルートなし」「Controllerなし」「Actionなし」の場合、その他はアプリケーションエラーとして扱う。

ログリソースがBootstrapに登録されていれば、エラーメッセージとリクエストパラメータをログへ出す。開発環境で `displayExceptions` が有効な場合は、Viewへ例外オブジェクトも渡す。

表示は `application/views/scripts/error/error.phtml` が担当する。
