# controls.phtml 解説

対象ファイル: `application/views/scripts/controls.phtml`

ソース: [application/views/scripts/controls.phtml](../../../../../zend-framework-1-crud-master/application/views/scripts/controls.phtml)

## 役割

Zend_Paginator用のページングView部品。

## 主な内容

- First / Previous / 数字 / Next / Last のリンクを表示する。
- リンク先は `?page=番号`。
- ページング用のCSSもこのファイル内に直接書かれている。

## 関連ファイル

- `application/views/scripts/ticket/index.phtml`
- `application/controllers/TicketController.php`

## 注意点

- CSSがView部品内にあるため、見通しを良くするならCSSファイルへ移す余地がある。

## 詳細

ページングリンクを描画する部分View。

`Zend_Paginator` から渡される `pageCount`、`current`、`first`、`previous`、`next`、`last`、`pagesInRange` などを使い、First / Previous / ページ番号 / Next / Last のリンクを作る。

`ticket/index.phtml` から `paginationControl($this->blogTopics, 'Sliding', 'controls.phtml')` の形で呼び出される。URLは `?page=番号` 形式で、一覧画面のページ切り替えに使われる。

ページ数がない場合は何も表示しない。
