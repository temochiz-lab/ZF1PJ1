# layout.phtml 解説

対象ファイル: `application/layouts/scripts/layout.phtml`

ソース: [application/layouts/scripts/layout.phtml](../../../../../zend-framework-1-crud-master/application/layouts/scripts/layout.phtml)

## 役割

全画面共通レイアウト。

## 主な内容

- doctype、head、CSS読み込み、Google Fonts、Bootstrap JS読み込みを定義する。
- ナビゲーションにブランドリンク、Add Ticket、CVS exportを表示する。
- FlashMessengerのメッセージをBootstrap alertとして表示する。
- `layout()->content` で各ActionのViewを埋め込む。

## 関連ファイル

- `public/css/app.global.css`
- `application/views/scripts/ticket/*.phtml`

## 注意点

- 外部CDNのjQuery/Bootstrapを読み込む想定。

## 詳細

全画面共通のHTMLレイアウト。

DOCTYPE、head、CSS読み込み、ナビゲーションバー、本文表示位置を定義する。各ActionのViewテンプレートで出力された内容は `$this->layout()->content` の位置に差し込まれる。

ナビゲーションには一覧へ戻るリンク、`Add Ticket`、`CVS export` があり、主要URLへの導線はここに集約されている。Bootstrap系CSSと独自CSS `app.global.css` もこのレイアウトから読み込まれる。

各画面の見た目を変える場合、個別Viewだけでなくこのレイアウトの影響も確認する必要がある。
