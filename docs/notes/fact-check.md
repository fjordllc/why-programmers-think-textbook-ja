# ファクト確認ログ

出版前ファクト確認の記録。`◎`＝ウェブで一次寄り情報を確認し本文と整合／`○`＝広く確立した事実で確信あり（未個別検証）／`△`＝要・一次資料確認。

最終更新：2026-06-30

## 検証済み（◎ ウェブ確認・本文と整合）

| 事項 | 確認内容 | 関連章 |
|------|---------|--------|
| アリアン5・501 | 1996-06-04 初号機。発射 37 秒後に喪失・自爆。アリアン4 の慣性基準系コードを再利用。水平速度が大きく、64bit 浮動小数点→16bit 符号付き整数の変換であふれ、例外が処理されず航法系が停止。負荷目標 80% のため 7 変数中 4 つしか保護せず | 4 |
| アポロ11・1202 | 1969-07-20 着陸降下中。ランデブーレーダ由来の過負荷でエグゼクティブ・オーバーフロー。ハミルトンらの優先度スケジューラが低優先度ジョブを捨て、着陸に必須の処理を生かして継続。故障でなく設計どおりの自己防衛 | 4 |
| 第五世代コンピュータ | 1982 開始、ICOT（MITI 傘下）、論理プログラミング（Prolog）基盤、並列推論マシン。10 年・約 540 億円・1992 まで。技術成果はあったが当初描いた変革的な商業的成果には届かず | 1 |
| ストールマンとプリンタ | 1980 ごろ、MIT AI Lab に Xerox 9700 レーザープリンタ。前のプリンタではドライバを改造し紙詰まりを利用者へ通知していたが、新機のソースは入手不可。Xerox は企業秘密として拒否。これが GNU（1983 発表）・自由ソフトウェア運動の契機 | 6 |

## 高確信・未個別検証（○ 広く確立）

刊行前に一次資料へ一度通すが、内容の確信は高い。

- ブルックス「銀の弾丸はない（No Silver Bullet, 1986）」と本質的／偶有的複雑さ（『人月の神話』系） — 1
- マキルロイとパイプ・UNIX 哲学「一つのことをうまくやる」 — 1
- KISS・DRY・YAGNI の出どころ（KISS＝航空・軍／DRY＝Hunt & Thomas／YAGNI＝XP） — 1
- クヌース「文芸的プログラミング（1984）」／SICP 冒頭「プログラムは人が読むために書かれ、機械の実行は副次的」（Abelson & Sussman, 1985） — 2
- ファウラー「Any fool can write code that a computer can understand…」（『リファクタリング』1999） — 2
- ダイクストラ「テストはバグの存在は示せるが不在は示せない」 — 4・7
- ダイクストラ「Go To Statement Considered Harmful（1968, CACM、表題は編集者）」 — 7
- ケント・ベック『Extreme Programming Explained: Embrace Change（1999）』 — 3
- カニンガム「技術的負債」メタファ（1992 OOPSLA） — 3
- ファウラーのリファクタリング定義（外部の振る舞いを変えず内部構造を改善） — 3
- アジャイル開発宣言（2001・Snowbird・17 名）「計画に従うことより変化への対応を」 — 3
- Fagan Inspection（IBM・1976） — 5
- プルリクエストを一般化した GitHub（2008） — 5
- GNU 宣言（1985）・FSF（1985）・四つの自由・"free as in freedom, not beer" — 6
- トーバルズと Linux（1991）・Git（2005）／Wikipedia（2001） — 6
- 松本行弘と Ruby（1995）、「プログラマーの幸福／楽しさ」を設計の中心に — 8
- CORBA（OMG・1991〜）の重厚さと失速／REST（Fielding・2000）の軽さ — 9
- Web の起源（バーナーズ＝リー・CERN・1989〜1991） — 9

## 残・要判断（△）

- 本文に固有名（製品名・規格名・人名）をどこまで出すか。初稿は多くを伏せ「機能」で描いている。各章 structure-check の「要・編集判断」を参照。
- 「静的型／動的型」を開いた問い、「集中／分散（実質 Git）」を閉じた問いとする扱いは本書の主張。妥当性は編集合意で確定する。

## 出典（検証に使用）

- Ariane: [ESA Inquiry Board report](https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report), [Wikipedia: Ariane flight V88](https://en.wikipedia.org/wiki/Ariane_flight_V88)
- Apollo 1202: [Apollo 11 Technical Mission Analysis – Lunar Landing Alarms](https://oboe.com/learn/apollo-11-technical-mission-analysis-1k75j47/lunar-landing-alarms-2)
- 第五世代: [Wikipedia: Fifth Generation Computer Systems](https://en.wikipedia.org/wiki/Fifth_Generation_Computer_Systems), [IPSJ Computer Museum](http://museum.ipsj.or.jp/en/computer/other/0002.html)
- Stallman/printer: [Free as in Freedom, Ch.1 (O'Reilly)](https://www.oreilly.com/openbook/freedom/ch01.html), [Wikipedia: Richard Stallman](https://en.wikipedia.org/wiki/Richard_Stallman)
