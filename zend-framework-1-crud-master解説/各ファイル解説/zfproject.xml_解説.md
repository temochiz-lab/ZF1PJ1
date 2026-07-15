# .zfproject.xml 解説

対象ファイル: `.zfproject.xml`

ソース: [.zfproject.xml](../../zend-framework-1-crud-master/.zfproject.xml)

## 役割

Zend Toolが管理するプロジェクト構成メタデータ。

ZF1の `zf` コマンドやZend Toolが、プロジェクト内にどのController、Model、View、テスト設定などがあるかを把握するためのXMLファイル。

## 主な内容

- `projectProfile` の `version` は `1.12.19`。
- `applicationDirectory` に `Application_` というクラス名プレフィックスが設定されている。
- `configsDirectory`、`controllersDirectory`、`layoutsDirectory`、`modelsDirectory`、`viewsDirectory` など、ZF1アプリの標準的な構成が記録されている。
- `IndexController` と `ErrorController` の存在が記録されている。
- `public/index.php` と `public/.htaccess` が公開ディレクトリ内の入口ファイルとして記録されている。
- `tests/phpunit.xml` と `tests/bootstrap.php` など、テスト関連ファイルも記録されている。

## このアプリでの位置づけ

このファイルは、実行時のリクエスト処理では直接使われない。

実際のアプリ起動は `public/index.php`、設定読み込みは `application/configs/application.ini`、ルーティングは `application/configs/routes.php` が担当する。

`.zfproject.xml` は、実行処理というより **開発ツール用のプロジェクト情報** と見るのがよい。

## 関連ファイル

- `public/index.php`
- `public/.htaccess`
- `application/Bootstrap.php`
- `application/configs/application.ini`
- `tests/phpunit.xml`

## 注意点

- XML内には `BlogDbTable`、`LabsDbTable`、`LabDbTable`、`BlogMapper`、`LabMapper` など、現在のチケットCRUDとは一致しない名前が残っている。
- このため、過去のサンプルや別名のアプリから変更された名残が含まれている可能性がある。
- 現在の主要処理を追う場合は、このファイルより実ソース側を優先して読む。

## 詳細

Zend Toolがプロジェクト構造を管理するためのメタ情報ファイル。

アプリ実行時のリクエスト処理には直接関与しない。Controller、Action、ViewなどをZend Toolで生成・管理した履歴や構成情報を記録するためのもの。

解析では、実際の動作よりも「このプロジェクトがZend Framework 1の標準プロジェクト構成で作られている」ことを示す補助情報として扱う。
