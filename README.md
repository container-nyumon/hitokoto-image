# hitokoto-image（題材のイメージのもと）

Kubernetes 入門のハンズオンで使うイメージ `ghcr.io/container-nyumon/hitokoto` を作るリポジトリです。
**受講者はこのリポジトリを使いません**（テンプレート `hitokoto-k8s-template` のマニフェストから、公開済みのイメージを取ってきます）。

- 公開の手順: Actions → publish → Run workflow → 版（`1.0`・`1.1`）を入れて実行。amd64 と arm64 の両方を作る。
- 初めて公開した後、パッケージの設定で **Public** にする（GitHub の画面で行う）。
- 版の違いは画面の右下の表示（`hitokoto 1.0` ／ `hitokoto 1.1`）だけ。

## 環境変数

| 名前 | 意味 | 既定 |
|---|---|---|
| `DB_HOST` | データベースの名前（Service の名前）。`none` で DB を使わない | （必須） |
| `DB_PASSWORD` | データベースのパスワード（ユーザーは postgres・DB は postgres） | 空 |
| `APP_TITLE` | 見出しのタイトル | ひとこと掲示板 |
| `APP_VERSION` | 画面に出す版（イメージを作るときに入る） | dev |

- ポート 8000、確認用のパス `/health`（`{"status":"ok"}`。DB は確かめない）。
- 一般のユーザー（UID 10001）で動く。
