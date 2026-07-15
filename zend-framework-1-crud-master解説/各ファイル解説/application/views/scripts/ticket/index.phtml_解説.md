# index.phtml 解説

対象ファイル: `application/views/scripts/ticket/index.phtml`

ソース: [application/views/scripts/ticket/index.phtml](../../../../../../zend-framework-1-crud-master/application/views/scripts/ticket/index.phtml)

## 役割

チケット一覧画面のView。

## 主な内容

- `blogTopics` をループしてチケット一覧テーブルを表示する。
- Title、Notes、Date、Action列を表示する。
- 各行にEdit/Deleteボタンを出す。
- `paginationControl()` でページング部品を表示する。

## 関連ファイル

- `application/controllers/TicketController.php`
- `application/views/scripts/controls.phtml`

## 注意点

- 日付表示に `displayDate()` View Helperを使う。

## 詳細

チケット一覧画面のViewテンプレート。

`blogTopics` に入ったチケット一覧をテーブルで表示し、各行にタイトル、本文、作成日、編集リンク、削除リンクを出す。作成日の表示には `displayDate()` View Helperを使う。

編集リンクは `ticket/edit/{id}`、削除リンクは `ticket/delete/{id}` に向く。削除リンクはGETで削除処理へ進むため、実運用では確認やPOST化が望ましい。

一覧下部では `paginationControl()` により `controls.phtml` を呼び出し、ページングリンクを表示する。1ページあたりの件数はController側で5件に設定されている。
