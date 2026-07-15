# readme.md 解説

対象ファイル: `readme.md`

ソース: [readme.md](../../zend-framework-1-crud-master/readme.md)

## 役割

プロジェクトのREADME。

## 主な内容

- Zend Framework 1 のCRUDサンプルアプリであることを説明している。
- アップロード、ページング、CSV出力を含むチケットアプリとして紹介している。
- `zf1app_db.sql` をインポートして使う想定が書かれている。

## 関連ファイル

- `zf1app_db.sql`
- `other_example/crud_picture.jpg`

## 注意点

- README内では `cvs export` と書かれているが、文脈上は `csv export` の意味と思われる。

## 詳細

プロジェクト概要や導入手順を簡単に示すための説明ファイル。

このアプリ自体の処理は `application` と `public` 以下にあるため、READMEは実行時には読み込まれない。解析時には、プロジェクトの由来、必要な環境、サンプルアプリとしての位置づけを確認する入口になる。

コードの流れを追う場合は、READMEよりも `public/index.php`、`application/Bootstrap.php`、`application/configs/routes.php` の順に見る方が実処理に近い。
