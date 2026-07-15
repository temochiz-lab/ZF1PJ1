# ActionErrors.php 解説

対象ファイル: `application/views/helpers/ActionErrors.php`

ソース: [application/views/helpers/ActionErrors.php](../../../../../zend-framework-1-crud-master/application/views/helpers/ActionErrors.php)

## 役割

Viewに渡されたActionエラー一覧をHTML化するView Helper。

## 主な内容

- `actionErrors` が存在する場合、`ul` と `li` でエラー一覧を出力する。

## 注意点

- 現在のチケットCRUDの主要画面では直接使われていない。

## 詳細

Viewに渡された `actionErrors` をHTMLのエラー一覧として表示するView Helper。

`setView()` でViewオブジェクトを保持し、`actionErrors()` 呼び出し時に `$this->_view->actionErrors` があれば `ul/li` を組み立てる。

現在のチケットCRUD画面では目立って使われていないが、フォーム処理や認証処理などでエラー一覧を共通表示するための補助部品として作られている。
