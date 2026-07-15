# .htaccess 解説

対象ファイル: `public/.htaccess`

ソース: [public/.htaccess](../../../zend-framework-1-crud-master/public/.htaccess)

## 役割

Apache用のURLリライト設定ファイル。

ブラウザから来たリクエストを、必要に応じて `public/index.php` へ流すための設定。

## 主な内容

- `RewriteEngine On` でApacheのmod_rewriteを有効にする。
- リクエストされたファイル、シンボリックリンク、ディレクトリが実在する場合は、そのまま返す。
- 実在しないURLの場合は、最終的に `index.php` へリライトする。
- これにより、`/ticket/create` のような物理ファイルではないURLも、Zend FrameworkのFront Controllerで処理できる。

## このアプリでの流れ

```text
ブラウザから /ticket/create にアクセス
↓
public/.htaccess
↓
実ファイルではないので public/index.php へリライト
↓
Zend_Application 起動
↓
routes.php
↓
TicketController#saveAction
```

## 関連ファイル

- `public/index.php`
- `application/configs/routes.php`
- `application/controllers/TicketController.php`

## 注意点

- Apacheで動かす場合に重要なファイル。
- PHP組み込みサーバーやNginxで動かす場合は、別途同等のルーティング設定が必要になる。
- 実ファイルが存在する場合は `index.php` へ流さず、そのまま配信する設定になっている。

## 詳細

Apacheでフロントコントローラ方式を動かすためのURLリライト設定。

静的ファイルなど実在するファイルへのアクセスはそのまま返し、それ以外のリクエストを `public/index.php` に集約する。これにより `/ticket/create` のようなURLでも、実際には `index.php` からZF1のルーティングへ渡される。

この設定がない環境では、きれいなURLが動かず `index.php` 経由のURLが必要になる場合がある。
