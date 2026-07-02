# 引き継ぎガイド ──『プログラマーはなぜそう考えるのか』

別の担当者（人／AI）がこのリポジトリの作業を引き継ぐための入口。**まずこの1枚を読み、必要に応じて各ドキュメントへ飛ぶ。**

最終更新：2026-07-02

---

## 1. これは何か

FBC Press シリーズの技術書『プログラマーはなぜそう考えるのか』の**原稿リポジトリ**。ソフトウェア開発の「当たり前」がどう生まれたかを、**九つの不自由と九つの自由の物語**として描く、ソフトウェア文化への入門書。手法カタログではなく「なぜそう考えるのか」を読者に渡すのが狙い。

- 体裁：[mdBook](https://github.com/rust-lang/mdBook)（Rust 製の静的サイトジェネレータ）
- 公開：Cloudflare Pages（`main` への push で自動デプロイ）
- ライセンス：MIT
- GitHub：`https://github.com/fjordllc/why-programmers-think-textbook-ja`

## 2. 現在の状態（2026-07-02 時点）

- **本文は全11本＋巻末年表そろって通読可能**（はじめに・全9章・終章・おわりに・年表）。初稿→推敲→多視点レビュー一巡→二巡目まで完了。
- **図版24枚**を自作 SVG で用意・全章に挿入済み（`<figure>`/`<figcaption>` 構造）。再生成は `scripts/figures/build_all.py` 一本。
- **体裁の実 HTML 監査を一巡済み**：場面転換は `<hr>`、図版は figure/figcaption、生 Markdown 漏れ・setext 誤変換なしを確認。
- **FBC 宣伝導線**（はじめに・おわりに・共通フッター）挿入済み。
- **Cloudflare Pages 用のビルド設定**（`scripts/cloudflare-build.sh`＋`docs/DEPLOY.md`）あり。ダッシュボードでの Git 連携接続だけは手作業（未確認なら DEPLOY.md 参照）。

いまの主な残タスクは **著者判断待ちの論点**（下記 5）と、刊行前の **一次資料での事実確認**。文章の骨格自体は完成度が高い。

## 3. ドキュメントの地図（どこに何があるか）

| ファイル | 役割 |
|---|---|
| `HANDOFF.md`（この文書） | 引き継ぎの入口 |
| `README.md` | リポジトリ概要・構成・ビルド方法 |
| `OUTLINE.md` | 改訂企画 v3。**本の設計思想**（不自由の地図／6拍子の背骨／崩し A〜E）。執筆判断の一次典拠 |
| `STYLEGUIDE.md` | 本書固有の執筆規約 |
| `TERMS.md` | 用語・表記統一 |
| `PROGRESS.md` | **作業ログ（時系列）**。何をなぜ変えたかの経緯はここ。作業のたびに追記する |
| `docs/REVIEW_POINTS.md` | **判断を委ねる点（第1部）＋レビュー観点（第2部）**。著者に振るべき論点が一覧化されている |
| `docs/notes/chapterN-structure-check.md` | 各章の自己点検メモ（本に載らない編集メモ） |
| `docs/notes/multi-perspective-review.md` | 多視点レビューの記録（編集者／メンター／ベテラン／受講生＋面白さ） |
| `docs/notes/figure-plan.md` | 図版24枚の計画（各図の主張・種類・配置・alt） |
| `docs/notes/fact-check.md` | ファクト確認の記録と未確認項目 |
| `docs/DEPLOY.md` | Cloudflare Pages デプロイ手順 |

共有の編集規約は**別リポジトリ** `/Users/machida/dev/FBC_Press`（GitHub: `fjordllc/FBC_Press`）にある。STYLE_GUIDE / FIGURE_GUIDE / ASSET_RULES / REVIEW_CHECKLIST / BUILD_AND_PUBLISH / PROMOTION_POLICY など。**本書で得た一般的な学びは FBC_Press 側に還元する**運用。

## 4. 作業の進め方（このプロジェクトの流儀）

1. **多視点レビュー・ループ**が基本方針（ユーザーの標準ゴール）：
   「技術書編集者／FBCメンター／エンジニア歴30年のベテラン／FBC受講生＋**読み物としての面白さ**」の5つの目でレビュー → 結果を `docs/notes/` に記録 → 文章を修正 → 再レビュー → 次へ、を繰り返す。
2. **章を仕上げたら、必ず `mdbook build` 後の実 HTML を読者の見た目で確認する**（原稿=Markdown だけで判断しない）。過去に区切り記号の浮き・強調の生漏れを、この工程で初めて捕捉した。共通チェックは FBC_Press `REVIEW_CHECKLIST.md`「ビルド後の実ページ確認」節。
3. **変更したら `PROGRESS.md` に一行残す**（日付・何を・なぜ）。
4. 図版を増減したら `docs/notes/figure-plan.md` を更新し、`build_all.py` で再生成する。

## 5. 未解決・引き継ぎたい論点

**著者（町田さん）の判断が要る**もの。詳細と初稿での暫定方針は `docs/REVIEW_POINTS.md` 第1部の表に一覧。要点だけ：

- 固有名（製品名・規格名 CORBA/Git/GitHub/Rails/Ruby 等）を本文にどこまで出すか（現状は機能描写で匿名化）
- 「自由」を本文に出す章の線引き（現状は第6章・終章のみ）
- 終章の AI 論のメタ性（本書自体を AI が書いている事実に触れるか）
- 第7・8章の「静的/動的型＝開いた問い」「集中/分散＝閉じた問い」の断定を確定してよいか
- 第6章「静かな回収」の一文の塩梅（**本全体の心臓部**）
- 刊行前の一次資料確認（`docs/notes/fact-check.md` の `○` 項目）

これらは「正解を一つに潰さない」ため初稿であえて固定していない。編集判断で確定する。

## 6. ハマりどころ（学び）

- **CJK と `**強調**`**：全角括弧や句読点に隣接した `**…**` は、CommonMark のフランキング規則で強調にならず `**` が生漏れすることがある（例：`…」**だ` は閉じと見なされない）。その箇所だけ `<strong>…</strong>` を直書きする。
- **場面転換は `<hr>`**：単独行に記号（`──` 等）を置くと `<p>──</p>` として浮く。Markdown の `---` を使う。ただし直前行との間に**空行が要る**（詰めると setext 見出し化する）。
- **図版は `<figure>`/`<figcaption>`**：画像とキャプションの並置ではなく、セマンティック構造で書く。見た目は共有テーマの CSS に委ねる（独自 CSS を足さない）。
- **和欧間スペース**：`HTML は`／`1996 年`／`0 円`。ただし `第10章` の序数は詰める、全角約物とは空けない。詳細は FBC_Press STYLE_GUIDE §1.1。
- **シェルの `grep` は `ugrep` エイリアス**：ファイルリスト渡しで挙動が違い、警告や誤集計が出る。HTML の一括監査は Python で書くのが確実。
- **`book/` は `.gitignore` 済み**：ビルド成果物。コミットしない。
- **`theme/` はファイル実体で同梱**（submodule ではない）。CI で追加取得が要らない。

## 7. ビルド・デプロイ・環境

```sh
mdbook serve --open   # 編集しながらブラウザで確認
mdbook build          # book/ に静的サイトを生成
```

- ローカル環境（macOS）に mdBook v0.4.52 導入済み。SVG→PNG 目視確認は `rsvg-convert`（`/opt/homebrew/bin/rsvg-convert`）。
- Cloudflare Pages：ビルドコマンド `bash scripts/cloudflare-build.sh`／出力ディレクトリ `book`。詳細は `docs/DEPLOY.md`。
- リポジトリのパス（ローカル）：`/Users/machida/dev/why-programmers-think-textbook-ja`

## 8. 重要な運用ルール

- **コミット／プッシュは、ユーザーに言われたときだけ行う。** 勝手にコミットしない。`main` への push は Cloudflare の本番デプロイを走らせる点にも注意。
- 本書固有でない一般的な学び・ルールは、共有リポジトリ **FBC_Press** に還元して push する（FBC_Press は main へ直接ルールコミットする運用）。
