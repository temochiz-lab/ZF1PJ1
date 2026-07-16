# Csv.php 解説

対象ファイル: `application/helpers/Csv.php`

ソース: [application/helpers/Csv.php](../../../../zend-framework-1-crud-master/application/helpers/Csv.php)

## 役割

CSVダウンロード用Action Helper。

## 主な内容

- `direct()` から `printExcel()` を呼び出す。
- CSV用HTTPヘッダを設定する。
- 配列データを `fputcsv()` で出力する。
- Excel向けに区切り文字 `;` を使う。

## 関連ファイル

- `application/controllers/TicketController.php`

## 関連テーブル

- [tickets](../../../08_データベース.md#tickets): `TicketMapper#fetchAllCvs()` で取得されたデータがCSV出力される。

## 注意点

- 出力後に `exit()` するため、通常のView描画は行われない。

## 詳細

Controllerから `$this->_helper->Csv(...)` の形で呼び出されるCSV出力用Action Helper。

`direct()` は呼び出し口で、実処理は `printExcel()` に渡している。`TicketController#cvsexportAction()` では、[tickets](../../../08_データベース.md#tickets) を元にした `TicketMapper::fetchAllCvs()` の結果とファイル名 `tickets` を渡す。

`printExcel()` はCSV用のHTTPヘッダを設定し、必要に応じて先頭行へカラム名を追加し、CSV本文を作る。最後に `Content-Disposition` を使って `tickets-export.csv` のようなファイル名でダウンロードさせる。

CSVの先頭が `ID` の場合にExcelがSYLK形式と誤認する問題を避けるため、先頭文字列を調整している。画面表示ではなくレスポンスを直接作るため、通常のViewテンプレートは使わない。
