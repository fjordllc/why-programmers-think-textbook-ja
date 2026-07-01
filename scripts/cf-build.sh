#!/usr/bin/env bash
#
# Cloudflare Pages 用ビルドスクリプト。
# Cloudflare のビルド環境には mdBook が無いので、バージョンを固定した
# 公式リリースバイナリを取得してから `mdbook build` を実行する。
#
# ダッシュボードの設定:
#   Build command   : bash scripts/cf-build.sh
#   Build output dir : book
#
# ローカルの mdBook を上げたら MDBOOK_VERSION も合わせて更新すること。
set -euo pipefail

MDBOOK_VERSION="0.4.52"
TARBALL="mdbook-v${MDBOOK_VERSION}-x86_64-unknown-linux-gnu.tar.gz"
URL="https://github.com/rust-lang/mdBook/releases/download/v${MDBOOK_VERSION}/${TARBALL}"

echo "==> Downloading mdBook v${MDBOOK_VERSION}"
curl -sSL "$URL" | tar -xz

echo "==> Building book"
./mdbook build

echo "==> Done. Output in ./book"
