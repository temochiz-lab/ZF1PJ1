# LoggedInUser.php 解説

対象ファイル: `application/views/helpers/LoggedInUser.php`

ソース: [application/views/helpers/LoggedInUser.php](../../../../../zend-framework-1-crud-master/application/views/helpers/LoggedInUser.php)

## 役割

ログイン状態表示用View Helper。

## 主な内容

- `Zend_Auth` のidentityを確認し、ログイン中ならユーザー名とログアウトリンクを表示する。
- 未ログインならログインリンクを表示する。

## 関連ファイル

- `zf1app_db.sql` の [users](../../../../08_データベース.md#users) テーブル

## 関連テーブル

- [users](../../../../08_データベース.md#users): SQLには定義されているが、対応する認証ControllerやUserモデルは見当たらない。

## 注意点

- `AuthController` や `Users` モデルが見当たらないため、未完成または流用元の名残と思われる。

## 詳細

ログイン中ユーザーの表示を行うView Helper。

`Zend_Auth` に認証情報があればログアウトリンクとユーザー名を表示し、なければログインリンクを表示する作りになっている。

ただし、このプロジェクトには `AuthController` や `Users` モデルなど認証に必要なファイルが揃っていないため、[users](../../../../08_データベース.md#users) テーブルは現状のチケットCRUDでは実用状態ではない。認証付きアプリから流用された残りと考えられる。
