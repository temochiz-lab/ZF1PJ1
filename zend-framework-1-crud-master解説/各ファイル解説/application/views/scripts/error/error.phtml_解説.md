# error.phtml 解説

対象ファイル: `application/views/scripts/error/error.phtml`

ソース: [application/views/scripts/error/error.phtml](../../../../../../zend-framework-1-crud-master/application/views/scripts/error/error.phtml)

## 役割

エラー画面のView。

## 主な内容

- `message` を表示する。
- `exception` が渡された場合、例外メッセージ、スタックトレース、リクエストパラメータを表示する。

## 関連ファイル

- `application/controllers/ErrorController.php`

## 注意点

- 開発時には便利だが、本番で例外詳細を表示するのは避けるべき。

## 詳細

エラー発生時の表示テンプレート。

`ErrorController` から渡された `message` を見出しとして表示する。開発環境などで `exception` が渡されている場合は、例外メッセージ、スタックトレース、リクエストパラメータも表示する。

本番環境では詳細例外を出さない設定にすることで、利用者には簡潔なエラー表示だけを見せる設計になる。
