# TicketMapper.php 解説

対象ファイル: `application/models/TicketMapper.php`

ソース: [application/models/TicketMapper.php](../../../../zend-framework-1-crud-master/application/models/TicketMapper.php)

## 役割

ControllerとDBテーブルの橋渡しをするMapper。

## 主な内容

- `getDbTable()` で `TicketDbTable` を取得する。
- `saveTopic()` でINSERT/UPDATEを分岐する。
- `findTopic()` で1件取得する。
- `fetchAllTopics()` で一覧表示用データを取得する。
- `fetchAllCvs()` でCSV用配列を作る。
- `deleteTopic()` で指定IDを削除する。

## 関連ファイル

- `application/models/DbTable/TicketDbTable.php`
- `application/models/Ticket.php`

## 注意点

- `deleteTopic()` は文字列連結のSQL条件なので、プレースホルダ利用が望ましい。

## 詳細

ControllerとDBアクセスを分離するためのMapper。

`getDbTable()` は `Application_Model_DbTable_TicketDbTable` を遅延生成し、以後のDB操作で使う。ControllerはSQLやDbTableを直接扱わず、このMapperのメソッドを呼ぶ。

`saveTopic()` は `Application_Model_Ticket` から配列を作り、`id` の有無でINSERTとUPDATEを分岐する。新規時は `created_at`、更新時は `updated_at` を設定する。

`findTopic()` は指定IDの1件を取得し、取得結果を `Application_Model_Ticket` に詰め直す。`fetchAllTopics()` は一覧表示用に全件をモデル配列へ変換する。

`fetchAllCvs()` はCSV出力用に、モデルではなく配列データを返す。`Csv` Helperに渡しやすい形にするため。

`deleteTopic()` は指定IDを削除する。条件が文字列連結なので、実運用ではプレースホルダやquote処理を使う方が安全。
