# Ticket.php 解説

対象ファイル: `application/models/Ticket.php`

ソース: [application/models/Ticket.php](../../../../zend-framework-1-crud-master/application/models/Ticket.php)

## 役割

チケット1件分のデータモデル。

## 主な内容

- `id`、`title`、`notes`、`created_at`、`updated_at`、`files`、`priority` を保持する。
- setter/getterで値を出し入れする。
- コンストラクタで配列を受け取り、対応するsetterへ流す。

## 関連ファイル

- `application/models/TicketMapper.php`

## 注意点

- DB行そのものではなく、アプリ側で扱うデータ入れ物。

## 詳細

チケット1件分の値を持つドメインモデル。

内部プロパティとして `id`、`title`、`notes`、`created_at`、`updated_at`、`files`、`priority` を持ち、それぞれにsetter/getterが用意されている。

コンストラクタに配列を渡すと `setOptions()` が呼ばれ、キー名に対応するsetterが存在する場合だけ値をセットする。フォーム値やDB行データをまとめてモデルに変換するための仕組み。

`__set()` と `__get()` もsetter/getterへ委譲する作りになっているため、直接プロパティ風に扱っても各setter/getterを通る。ただし存在しない項目を渡すと例外になる。
