# index.phtml 解説

対象ファイル: `application/views/scripts/index/index.phtml`

ソース: [application/views/scripts/index/index.phtml](../../../../../../zend-framework-1-crud-master/application/views/scripts/index/index.phtml)

## 役割

Zend Framework標準のWelcome画面View。

## 主な内容

- Zend Frameworkサイトやマニュアルへのリンクを持つ。
- 背景画像など標準生成に近いHTML/CSSが含まれる。

## 関連ファイル

- `application/controllers/IndexController.php`

## 注意点

- トップページ `/` はTicketControllerへ割り当てられているため、通常の導線では使われない。

## 詳細

`IndexController#indexAction()` に対応するViewテンプレート。

ただし、ルート設定ではトップページ `/` が `TicketController#indexAction()` に向いているため、通常のアクセスではこのテンプレートは表示されない。

ZF1プロジェクト作成時に生成された初期ページに近く、現在のチケットCRUDの説明では補助的な存在として扱う。
