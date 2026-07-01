# デプロイ（Cloudflare Pages・Git 連携）

GitHub リポジトリを Cloudflare Pages に接続し、`main` への push で自動ビルド・自動公開する。

## 初回セットアップ（ダッシュボード）

Git 連携プロジェクトの作成は Cloudflare ダッシュボードで行う（wrangler CLI では Git 連携プロジェクトを作れない）。

1. Cloudflare ダッシュボード → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. GitHub 連携を許可し、リポジトリ `fjordllc/why-programmers-think-textbook-ja` を選択
3. ビルド設定を次のとおり入力する:

   | 項目 | 値 |
   |---|---|
   | Production branch | `main` |
   | Framework preset | `None` |
   | Build command | `bash scripts/cf-build.sh` |
   | Build output directory | `book` |

4. **Save and Deploy** で初回ビルドが走る。完了すると `https://<project>.pages.dev` で公開される。

## 仕組み

- Cloudflare のビルド環境には mdBook が無いので、`scripts/cf-build.sh` がバージョン固定の公式リリースバイナリを取得してから `mdbook build` する。
- 出力は `book/`（`.gitignore` 済み。リポジトリには含めない。ビルドのたびに生成する）。
- mdBook のバージョンを上げるときは、ローカルと `scripts/cf-build.sh` の `MDBOOK_VERSION` を合わせて更新する。

## 以降の更新

`main` に push すれば自動でビルド・公開される。手動操作は不要。

## 状態確認（任意・wrangler CLI）

認証すれば CLI からデプロイ状況を確認できる。

```sh
npx wrangler login                      # ブラウザで承認
npx wrangler pages deployment list --project-name <project>
```
