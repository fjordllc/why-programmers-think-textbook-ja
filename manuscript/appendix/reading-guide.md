# 付録 読書ガイド

本書は、プログラマーが「なぜそう考えるのか」をつかむための入口として書いた。ここから先は、ぜひ元になった本や論文そのものを読んでほしい。

全部を順番に読む必要はない。まずは、自分がいちばん引っかかった章から入るのがいい。そのうえで、「最初の一冊」と「次の一冊」を示す。

## まず最初に読むなら

### 1. [『人月の神話』](https://ja.wikipedia.org/wiki/%E4%BA%BA%E6%9C%88%E3%81%AE%E7%A5%9E%E8%A9%B1) フレデリック・P・ブルックス Jr.

複雑さ、見積もり、銀の弾丸探し。ソフトウェア開発がなぜ難しいのかを、流行語ではなく地に足のついた言葉で考えたいなら、まずここから入るのがよい。

向いている章:
- [第1章](../part1/chapter1.md)
- [第3章](../part2/chapter3.md)
- [第7章](../part4/chapter7.md)

### 2. [『リファクタリング』](https://martinfowler.com/books/refactoring.html) マーティン・ファウラー

本書では思想や歴史の流れを中心に書いたが、実際にコードをどう整えるのかへ降りていくなら、この本が橋になる。読みやすさ、変更しやすさ、設計の手入れが、同じ実践の中に並んでいるとわかる。

向いている章:
- [第2章](../part1/chapter2.md)
- [第3章](../part2/chapter3.md)
- [第4章](../part2/chapter4.md)

### 3. [『XP エクストリーム・プログラミング』](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780321278654) ケント・ベック

変化を前提に作るとはどういうことかを、単なる精神論でなく実践の束として読むのに向いている。本書の[第3章](../part2/chapter3.md)と[第4章](../part2/chapter4.md)を、実際の開発の作法として読み直しやすくしてくれる。

向いている章:
- [第3章](../part2/chapter3.md)
- [第4章](../part2/chapter4.md)
- [第5章](../part3/chapter5.md)

### 4. [*Free Software, Free Society*](https://www.gnu.org/philosophy/fsfs/rms-essays.pdf) リチャード・ストールマン

[第6章](../part3/chapter6.md)を読んで「自由」の意味をもう少し正面から受け止めたくなったら、やはり原典に近いところへ行くべきだと思う。賛成するにせよ距離を取るにせよ、一度は自分で読んでおく価値がある。

向いている章:
- [第6章](../part3/chapter6.md)
- [第9章](../part4/chapter9.md)

### 5. [*Weaving the Web*](https://www.harpercollins.com/products/weaving-the-web-tim-berners-lee) ティム・バーナーズ＝リー

Web が単なる技術の積み重ねではなく、どういう思想で作られたのかを知るにはよい入口になる。[第9章](../part4/chapter9.md)の「誰のものでもない」という感覚に、作った本人の言葉で触れられる。

向いている章:
- [第9章](../part4/chapter9.md)

## テーマ別に読むなら

### 複雑さと設計

1. [『人月の神話』](https://ja.wikipedia.org/wiki/%E4%BA%BA%E6%9C%88%E3%81%AE%E7%A5%9E%E8%A9%B1)
2. [Frederick P. Brooks Jr., "No Silver Bullet"](https://worrydream.com/refs/Brooks-NoSilverBullet.pdf)
3. [『リファクタリング』](https://martinfowler.com/books/refactoring.html)
4. [『XP エクストリーム・プログラミング』](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780321278654)

### 読みやすいコード

1. [*Structure and Interpretation of Computer Programs*](https://mitpress.mit.edu/9780262510875/structure-and-interpretation-of-computer-programs/)
2. [Donald E. Knuth, "Literate Programming"](https://cs.stanford.edu/~knuth/lp.html)
3. [『リファクタリング』](https://martinfowler.com/books/refactoring.html)

### テストと変更

1. [*The Art of Software Testing*](https://www.wiley.com/en-us/The+Art+of+Software+Testing%2C+3rd+Edition-p-9781118031964)
2. [『XP エクストリーム・プログラミング』](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780321278654)
3. [『リファクタリング』](https://martinfowler.com/books/refactoring.html)

### オープンソースと自由

1. [*Free Software, Free Society*](https://www.gnu.org/philosophy/fsfs/rms-essays.pdf)
2. [*Free as in Freedom*](https://www.oreilly.com/openbook/freedom/)
3. [*The Cathedral and the Bazaar*](http://www.catb.org/~esr/writings/cathedral-bazaar/)

### 言語と道具の思想

1. [まつもとゆきひろ『まつもとゆきひろ 言語のしくみ』](https://www.oreilly.co.jp/books/9784873117966/)
2. [*Hackers & Painters*](https://www.paulgraham.com/hp.html)
3. [Alan Kay, "The Early History of Smalltalk"](https://worrydream.com/EarlyHistoryOfSmalltalk/)

### Web と公開性

1. [*Weaving the Web*](https://www.harpercollins.com/products/weaving-the-web-tim-berners-lee)
2. [Roy T. Fielding の学位論文](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm)
3. [*Designing Data-Intensive Applications*](https://dataintensive.net/)

## 読み方の勧め

- 一冊を全部理解してから次へ進まなくていい
- 難しい本ほど、まず目次と序文と結論だけ読むやり方でいい
- 本書の対応する章を読み返しながら往復すると、名著の言葉が急に自分の問題として読める

名著は、要約で知った気になるより、どこかで一度、原文や原典に当たるほうがいい。本書が、そのための助走になれば十分だと思っている。
