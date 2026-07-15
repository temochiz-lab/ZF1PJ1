# DisplayAddress.php 解説

対象ファイル: `application/views/helpers/DisplayAddress.php`

ソース: [application/views/helpers/DisplayAddress.php](../../../../../zend-framework-1-crud-master/application/views/helpers/DisplayAddress.php)

## 役割

住所文字列生成用View Helper。

## 主な内容

- address1/address2/town/county/postcode/countryを改行区切りで組み立てる。

## 注意点

- チケット機能のモデルには住所項目がないため、流用元コードの名残と思われる。

## 詳細

住所情報を表示用文字列に整形するView Helper。

複数の住所系フィールドを見て、値があるものを組み合わせる想定の処理になっている。しかし現在の `tickets` テーブルには住所項目がなく、チケットCRUD画面からも呼ばれていない。

このファイルは、別サンプルや流用元から残った補助Helperと見るのが自然。
