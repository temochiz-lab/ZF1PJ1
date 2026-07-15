# phpunit.xml 解説

対象ファイル: `tests/phpunit.xml`

ソース: [tests/phpunit.xml](../../../zend-framework-1-crud-master/tests/phpunit.xml)

## 役割

PHPUnit設定ファイル。

## 主な内容

- `bootstrap.php` をテスト起動時に読み込む。
- `tests/application` と `tests/library` をテストスイートとして定義する。

## 関連ファイル

- `tests/bootstrap.php`

## 注意点

- `tests/library` ディレクトリは現状ファイル一覧には見当たらない。

## 詳細

PHPUnitの設定ファイル。

テスト実行時のbootstrapとして `tests/bootstrap.php` を指定し、テストスイートの対象ディレクトリやコードカバレッジ用の設定候補を持つ。

現状のテストは最小限で、チケットCRUD全体の自動テストが揃っているわけではない。テストを拡充する場合は、Controller、Mapper、Formの動作を追加していくことになる。
