# Zend Framework 1について

## ざっくりした歴史

Zend Frameworkは、PHP向けのオープンソースWebアプリケーションフレームワーク。

Zend Technologiesが中心となって開発していたフレームワークで、PHPで本格的なWebアプリを作るための部品群として使われていた。

大まかな流れは次の通り。

| 年 | 出来事 |
| --- | --- |
| 2000年代後半 | Zend Framework 1系が広く使われるようになる。 |
| 2012年 | Zend Framework 2.0系が登場。ZF1とは設計がかなり変わる。 |
| 2016年 | Zend Framework 1.12.20がリリースされ、ZF1系はEOL扱いになる。 |
| 2019年 | Zend FrameworkプロジェクトはLaminas Projectへ移行する流れになる。 |

このプロジェクトのREADMEでは、Zend Frameworkのバージョンは `1.12.20` と書かれている。

つまり、このアプリは **古いが、当時よくあったZF1構成のCRUDサンプル** として読むのがよい。

## EOLについて

ZF1はすでにEOL、つまり公式サポート終了済み。

EOL後は、基本的に次のような扱いになる。

- 新しい機能追加は期待できない
- セキュリティ修正も通常は期待できない
- 新しいPHPバージョンでは動かない可能性がある
- 実運用で使い続ける場合は、移行や隔離運用を検討する必要がある

このアプリを読む目的が「既存システム解析」なら、ZF1を今から積極採用するというより、**古いPHPシステムを理解するための知識** として見るのが自然。

## そもそもZF1とは

ZF1は、PHPでWebアプリを作るためのフレームワーク。

特徴は次の通り。

- MVC構成を使える
- Controller / Model / View を分けて書ける
- DB操作、フォーム、バリデーション、認証、メール、ログなどの部品がある
- クラス名とファイルパスに強い対応関係がある
- `Zend_` で始まるクラスを多く使う
- 名前空間ではなく、アンダースコア区切りのクラス名を使う

例:

```php
Zend_Controller_Action
Zend_Application
Zend_Form
Zend_Db_Table_Abstract
Zend_Paginator
Zend_View_Helper
```

## ZF1の基本構成

今回のアプリでは、だいたい次の構成になっている。

```text
public/index.php
↓
application/configs/application.ini
↓
application/Bootstrap.php
↓
application/configs/routes.php
↓
application/controllers
↓
application/models
↓
application/views
```

### public/index.php

アプリの入口。

ブラウザからのリクエストは、基本的にここへ入る。

このファイルで `Zend_Application` を起動し、設定ファイルやBootstrapを読み込む。

### application.ini

アプリ全体の設定ファイル。

このプロジェクトでは、主に次の設定が書かれている。

- Bootstrapファイル
- Controllerディレクトリ
- Layout設定
- View設定
- DB接続設定

### Bootstrap.php

アプリ起動時の初期化処理を書くファイル。

今回のアプリでは、次のような処理をしている。

- doctype設定
- routes.phpの読み込み
- uploadディレクトリの確認
- `UPLOAD_PATH` 定数の定義

### routes.php

URLとController/Actionの対応を定義するファイル。

今回の例:

```text
/ticket/create
↓
TicketController#saveAction
```

ZF1では、URLがどのControllerのどのActionへ行くかをRouterが決める。

## ZF1のMVC用語

### Controller

リクエストを受け取り、処理の流れを決める場所。

今回の中心はこれ。

```text
application/controllers/TicketController.php
```

Controllerは、画面から来たリクエストを受けて、Modelを呼び、Viewにデータを渡す。

### Action

Controller内の1処理単位。

ZF1では、URLとActionメソッドが対応する。

例:

```php
public function indexAction()
public function saveAction()
public function editAction()
public function deleteAction()
```

`indexAction()` は `index` アクション、`saveAction()` は `save` アクションとして扱われる。

### Model

データや業務ロジックを扱う場所。

今回のアプリでは次の2種類がある。

```text
application/models/Ticket.php
application/models/TicketMapper.php
```

`Ticket.php` はチケット1件分のデータ入れ物。

`TicketMapper.php` はDB操作との橋渡し役。

### View

HTML表示を担当する場所。

ZF1では `.phtml` ファイルがViewテンプレートになる。

今回の例:

```text
application/views/scripts/ticket/index.phtml
application/views/scripts/ticket/save.phtml
application/views/scripts/ticket/edit.phtml
```

### Layout

全画面共通の外枠。

今回のファイル:

```text
application/layouts/scripts/layout.phtml
```

ナビゲーション、CSS読み込み、Flashメッセージ表示など、各画面に共通するHTMLがここにある。

## ZF1固有っぽいファイル・クラス

### Zend_Application

ZF1アプリを起動するためのクラス。

`public/index.php` で使われている。

```php
$application = new Zend_Application(
    APPLICATION_ENV,
    APPLICATION_PATH . '/configs/application.ini'
);
$application->bootstrap()
            ->run();
```

### Zend_Controller_Action

Controllerの親クラス。

今回の `TicketController`、`IndexController`、`ErrorController` はこれを継承している。

```php
class TicketController extends Zend_Controller_Action
```

### Zend_Controller_Router_Route

URLルートを定義するクラス。

`routes.php` で使われている。

```php
$route = new Zend_Controller_Router_Route(
    'ticket/create',
    array(
        'controller' => 'ticket',
        'action' => 'save'
    )
);
```

### Zend_Form

フォームをPHPクラスとして定義するための仕組み。

今回のファイル:

```text
application/forms/TopicBootstrapForm.php
```

フォーム項目、必須チェック、ファイルアップロード、CSRF対策などをまとめて書ける。

### Zend_Db_Table_Abstract

DBテーブルに対応するクラスの親。

今回のファイル:

```text
application/models/DbTable/TicketDbTable.php
```

```php
class Application_Model_DbTable_TicketDbTable extends Zend_Db_Table_Abstract
{
    protected $_name = 'tickets';
}
```

`$_name` にDBテーブル名を書く。

### Zend_Paginator

ページング用のクラス。

今回の一覧画面で、チケットを5件ずつ表示するために使っている。

```php
$paginator = Zend_Paginator::factory($data);
$paginator->setCurrentPageNumber($page);
$paginator->setItemCountPerPage(5);
```

### Zend_File_Transfer_Adapter_Http

ファイルアップロードを扱うクラス。

今回の `saveAction()` で使われている。

```php
$upload = new Zend_File_Transfer_Adapter_Http();
$upload->receive();
```

### FlashMessenger

リダイレクト後にメッセージを表示するための仕組み。

登録・更新・削除後の成功/失敗メッセージに使われている。

```php
$this->_helper->FlashMessenger->addMessage(...)
```

表示側は `layout.phtml` で処理している。

### View Helper

Viewから呼び出せる補助関数のようなもの。

今回の例:

```text
application/views/helpers/DisplayDate.php
```

一覧画面では次のように使っている。

```php
echo $this->displayDate($value->getCreatedat());
```

### Action Helper

Controllerから呼び出せる補助処理。

今回の例:

```text
application/helpers/Csv.php
```

CSV出力で使われている。

```php
$this->_helper->Csv($blogTopic->fetchAllCvs(), "tickets");
```

## ZF1の命名ルール

ZF1では、クラス名とフォルダ構成がかなり強く対応する。

例:

```php
Application_Model_TicketMapper
```

これはだいたい次のファイルに対応する。

```text
application/models/TicketMapper.php
```

また、DBテーブルクラスは次のようになっている。

```php
Application_Model_DbTable_TicketDbTable
```

対応ファイル:

```text
application/models/DbTable/TicketDbTable.php
```

現代のPHPでよく見る `namespace` ではなく、`_` 区切りのクラス名で階層を表現しているのがZF1らしい点。

## 今回のアプリを読む時のポイント

このアプリは、ZF1の基本要素がかなりコンパクトに入っている。

読む順番としては、次が分かりやすい。

```text
public/index.php
↓
application/configs/application.ini
↓
application/Bootstrap.php
↓
application/configs/routes.php
↓
application/controllers/TicketController.php
↓
application/models/TicketMapper.php
↓
application/models/DbTable/TicketDbTable.php
↓
application/views/scripts/ticket/*.phtml
↓
application/layouts/scripts/layout.phtml
```

特に重要なのは次の3つ。

| ファイル | 見るポイント |
| --- | --- |
| `routes.php` | URLがどのActionへ行くか |
| `TicketController.php` | 画面ごとの処理の入口 |
| `TicketMapper.php` | DB操作の実体 |

## 今の感覚で見ると古いところ

ZF1は古いフレームワークなので、今のPHPアプリと比べると次の点が古く見える。

- 名前空間ではなく `Zend_...` のクラス名
- Composer前提ではない構成
- `require_once` や include_path 前提の読み込み
- Controllerが太くなりやすい
- ViewにPHPを直接書く
- GETで削除しているような古い実装が残りやすい

ただし、古い業務システムではこの形がまだ残っていることがある。

そのため、ZF1を読む時は「新しく作るための技術」ではなく、**既存PHPシステムを読み解くための技術** として見るのが現実的。

## 参考

- [Zend Framework - Wikipedia](https://de.wikipedia.org/wiki/Zend_Framework)
- [Laminas - Wikipedia](https://en.wikipedia.org/wiki/Laminas)

