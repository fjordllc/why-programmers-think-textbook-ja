# プログラマーはなぜそう考えるのか

FBC Press シリーズの一冊。原稿リポジトリ。

> **引き継ぎ・初見の方へ:** まず [HANDOFF.md](HANDOFF.md) を読むと、現状・資料の地図・進め方・未解決の論点・ハマりどころが一枚でわかります。

> ソフトウェア開発の「当たり前」は、どう生まれたのか
> ── プログラマーが、不自由と戦いながら自由を勝ち取ってきた記録

## この本について

「シンプルに書こう」「テストを書こう」「コードは人に見せよう」――こうした開発の「当たり前」は、最初から当たり前だったわけではない。誰かが不自由に気づき、本気で間違え、議論し、少しずつ文化にしてきた。本書は、その営みを **九つの不自由と、九つの自由の物語** として描く、ソフトウェア文化への入門書。

正しい手法のカタログではなく、プログラマーが「なぜそう考えるのか」を、判断できる形で読者に渡すことを目指す。

## 構成

- はじめに ──「常識」は、最初から常識ではなかった
- 第1部 複雑さと読めなさに抗う（第1〜2章）
- 第2部 変化との戦い（第3〜4章）
- 第3部 一人では作れない（第5〜6章／第6章は本書の心臓）
- 第4部 正解はない（第7〜9章）
- 終章 AI は「当たり前」を作れるのか
- 付録 年表

詳しい企画は [OUTLINE.md](OUTLINE.md)、執筆規約は [STYLEGUIDE.md](STYLEGUIDE.md)、進捗は [PROGRESS.md](PROGRESS.md)、判断を委ねる点とレビュー観点は [docs/REVIEW_POINTS.md](docs/REVIEW_POINTS.md) を参照。各章の自己点検は `docs/notes/`、ファクト確認は [docs/notes/fact-check.md](docs/notes/fact-check.md)。

## リポジトリ構成

```
why-programmers-think-textbook-ja/
├── OUTLINE.md          改訂企画 v3（不自由の地図／6拍子／崩し A〜E）
├── STYLEGUIDE.md       本書固有の執筆規約
├── TERMS.md            用語・表記統一
├── PROGRESS.md         進捗管理（作業のたびに更新）
├── book.toml           mdBook 設定
├── manuscript/         原稿本体（mdBook ソース）
│   ├── SUMMARY.md
│   ├── preface.md / epilogue.md
│   ├── part1〜4/       各部 index.md＋章
│   └── appendix/       年表
├── docs/notes/         各章の構造チェック（本に載らない編集メモ）
├── theme/              シリーズ共通テーマ（mdbook-book-jp）＋本書固有 CSS
└── scripts/            ビルド補助
```

## ローカルでビルドする

[mdBook](https://github.com/rust-lang/mdBook) が必要。

```sh
mdbook serve --open   # 編集しながらブラウザで確認
mdbook build          # book/ に静的サイトを生成
```

## リンクチェック

[`mdbook-linkcheck`](https://github.com/Michael-F-Bryan/mdbook-linkcheck) を使う。

```sh
scripts/check-links.sh          # 書籍内リンクを厳格に確認
scripts/check-links.sh web      # 外部リンクも確認（警告扱い）
```

- `internal` は日常の確認用。書籍内リンクや相対リンクの崩れを失敗として扱う。
- `web` は公開前の確認用。外部サイトの一時的な不調で止まりすぎないよう、警告を出しつつ全体を見る。
- 初回だけ `cargo install mdbook-linkcheck` が必要。

## ライセンス

本文・コードともに MIT License（[LICENSE](LICENSE)）。
