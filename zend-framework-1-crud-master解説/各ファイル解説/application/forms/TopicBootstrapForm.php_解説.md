# TopicBootstrapForm.php 解説

対象ファイル: `application/forms/TopicBootstrapForm.php`

ソース: [application/forms/TopicBootstrapForm.php](../../../../zend-framework-1-crud-master/application/forms/TopicBootstrapForm.php)

## 役割

チケット登録/編集用のZend_Form。

## 主な内容

- POSTメソッド、Bootstrap向けclass、multipart/form-dataを設定する。
- `id` hidden、`title`、`notes`、`priority`、`files`、`csrf` を定義する。
- ファイルはjpg/png/gifのみ許可する。

## 関連ファイル

- `application/controllers/TicketController.php`
- `application/views/scripts/ticket/save.phtml`
- `application/views/scripts/ticket/edit.phtml`

## 注意点

- `files` が必須なので、編集時もファイル選択を求める挙動になりやすい。

## 詳細

チケット登録・編集画面で使うフォーム定義。

`init()` 内でhiddenの `id`、必須の `title`、必須の `notes`、選択式の `priority`、アップロード用の `files`、CSRF用の `csrf` を追加している。

`title` と `notes` にはBootstrap系のCSSクラスやplaceholderを設定し、表示時にフォームらしい見た目になるようにしている。`priority` は Low / Normal / High / Emergency の選択肢を持つ。

`files` は `UPLOAD_PATH` を保存先にし、拡張子を jpg/png/gif に制限している。フォーム全体には `multipart/form-data` が設定されるため、ファイルアップロード可能なHTMLフォームになる。

`getBootstrapDecorator()` は各フォーム要素のHTML構造を調整するための共通デコレータ定義。
