# menuList.php 解説

対象ファイル: `application/views/helpers/menuList.php`

ソース: [application/views/helpers/menuList.php](../../../../../zend-framework-1-crud-master/application/views/helpers/menuList.php)

## 役割

メニュー用HTMLリスト生成View Helper。

## 主な内容

- 配列を受け取り、`ul/li` とリンクまたは見出しに変換する。

## 注意点

- 現在の主要画面では使われていない。クラス名が小文字混じり。

## 詳細

配列からメニュー用のHTMLリストを作るView Helper。

`menuList($list, $id='')` に配列を渡すと、`ul` と `li` を組み立てる想定の処理。ナビゲーションやサイドメニューを共通生成する目的の部品。

現在の `layout.phtml` ではBootstrapのナビゲーションHTMLを直接書いているため、このHelperは主要画面では使われていない。
