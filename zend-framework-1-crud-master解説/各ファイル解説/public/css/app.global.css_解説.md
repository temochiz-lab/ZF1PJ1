# app.global.css 解説

対象ファイル: `public/css/app.global.css`

ソース: [public/css/app.global.css](../../../../zend-framework-1-crud-master/public/css/app.global.css)

## 役割

画面全体のCSS。

## 主な内容

- normalize.cssとBootstrap系のスタイルが含まれている。
- 最後に独自CSSとしてリストやエラー表示の調整がある。
- `layout.phtml` から読み込まれる。

## 関連ファイル

- `application/layouts/scripts/layout.phtml`

## 注意点

- 非常に大きいCSSで、アプリ固有の記述は末尾の `Custom CSS` 付近が中心。

## 詳細

画面全体で使う独自CSS。

Bootstrapだけでは足りない余白、テーブル、フォーム、ページングなどの見た目を調整するためのファイル。`layout.phtml` から読み込まれるため、チケット一覧・登録・編集など全画面に影響する。

画面再現や見た目調整を行う場合は、ViewテンプレートだけでなくこのCSSも確認する。
