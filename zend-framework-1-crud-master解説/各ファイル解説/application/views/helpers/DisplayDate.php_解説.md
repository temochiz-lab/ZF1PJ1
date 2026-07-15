# DisplayDate.php 解説

対象ファイル: `application/views/helpers/DisplayDate.php`

ソース: [application/views/helpers/DisplayDate.php](../../../../../zend-framework-1-crud-master/application/views/helpers/DisplayDate.php)

## 役割

日付表示用View Helper。

## 主な内容

- タイムスタンプを `Zend_Date` に変換し、指定フォーマットで返す。
- デフォルトは `Zend_Date::DATE_LONG`。

## 関連ファイル

- `application/views/scripts/ticket/index.phtml`

## 注意点

- 一覧画面の日付表示で使用される。

## 詳細

日付表示を整えるView Helper。

`displayDate($timestamp, $format = Zend_Date::DATE_LONG)` でタイムスタンプを受け取り、`Zend_Date` を使って指定フォーマットの文字列に変換する。

一覧画面 `ticket/index.phtml` では、チケットの `created_at` を表示するために `$this->displayDate($value->getCreatedat())` の形で呼び出される。DB上の日付文字列を画面向けに整形する役割。
