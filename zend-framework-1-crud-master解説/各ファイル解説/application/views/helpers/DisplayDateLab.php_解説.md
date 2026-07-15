# DisplayDateLab.php 解説

対象ファイル: `application/views/helpers/DisplayDateLab.php`

ソース: [application/views/helpers/DisplayDateLab.php](../../../../../zend-framework-1-crud-master/application/views/helpers/DisplayDateLab.php)

## 役割

日付表示用View Helperの別名/派生版。

## 主な内容

- `DisplayDate` とほぼ同じ処理を行う。

## 関連ファイル

- `application/views/helpers/DisplayDate.php`

## 注意点

- 現在の主要画面では使われていない可能性が高い。

## 詳細

`DisplayDate` とほぼ同じ構造の日付表示Helper。

メソッド名は `displayDateLab()` で、受け取った日時を `Zend_Date` でフォーマットして返す。現在の主要画面では `displayDate()` 側が使われており、このHelperは未使用の可能性が高い。

名前に `Lab` が付いているため、試作用または別画面用の名残として見る。
