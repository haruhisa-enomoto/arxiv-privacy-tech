---
layout: single
classes: wide
title: トップページ
permalink: /
author_profile: false
---

プライバシーテック全般に関するarXiv論文まとめです。自動更新（される予定）です。

- [全てのトピック](all/)

- [秘密計算 (Multi-Party Computation)](mpc/)
- [合成データ (Synthetic Data)](sd/)
- [連合学習 (Federated Learning)](fl/)
- [差分プライバシー (Differential Privacy)](dp/)
- [準同型暗号 (Homomorphic Encryption)](he/)
- [ゼロ知識証明 (Zero-Knowledge Proof)](zkp/)
- [PETs (Privacy Enhancing Technologies)](pets/)
- [SSI/DID/VC](ssi/)
- [連合転移学習 (Federated Transfer Learning)](ftl/)


## 方法

[このPythonスクリプト](https://github.com/haruhisa-enomoto/arxiv-privacy-tech/tree/main/scripts)を[GitHub Actions](https://github.com/haruhisa-enomoto/arxiv-privacy-tech/blob/main/.github/workflows/update.yaml)で毎時日本時間13時に動かしています。

## 最新更新分

更新: 2024-10-23T04:22:57.861835

- - -

### [Altogether: Image Captioning via Re-aligning Alt-text](http://arxiv.org/abs/2410.17251)

**Altogether: Altテキストの再整列による画像キャプション**

Hu Xu, Po-Yao Huang, Xiaoqing Ellen Tan, Ching-Feng Yeh, Jacob Kahn, Christine Jou, Gargi Ghosh, Omer Levy, Luke Zettlemoyer, Wen-tau Yih, Shang-Wen Li, Saining Xie, Christoph Feichtenhofer

- 既存の方法は、画像のキャプションを最初から作成し、既存のAltテキストを無視していた
- 本研究では、画像に関連するAltテキストを編集・再整列する方法を提案
- アノテーターがAltテキストを何回も画像に合わせて再整列し、視覚的に豊かなキャプションを作成
- この方法により、テキストから画像への生成やゼロショット画像分類も改善

Altogetherのアイデア、めっちゃ面白いじゃん！画像キャプションの質をこんな風に上げちゃうなんて、未来のテキスト生成とか画像解析とか、もっともっとすごいことになりそうだね！

**Comment:** accepted by EMNLP 2024; MetaCLIPv2

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, **投稿日時:** 2024-10-22 17:59

- - -

### [Feature Homomorphism -- A Cryptographic Scheme For Data Verification Under Ciphertext-Only Conditions](http://arxiv.org/abs/2410.17106)

**特徴ホモモルフィズム -- 暗号文のみの条件下でのデータ検証のための暗号スキーム**

Huang Neng

- プライバシー計算には、暗号化されたデータの検証が重要な課題
- 特徴ホモモルフィズムを提案し、暗号文のみでデータの整合性を確認可能
- 平文と暗号文の固有値を比較して、一貫性を直接検証可能
- 固有値は検索可能暗号で活用され、改ざん耐性や品質追跡を実現

暗号化だけでなく、データの整合性もチェックできるスキームなんてめっちゃ便利！これでプライバシーとデータ利用の両立が実現するかもね。どんな応用例が出てくるか今後が楽しみだね！

**Comment:** 31 pages, 6 figures

**トピック:** [準同型暗号](he), [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-22 15:30

- - -

### [Masked Differential Privacy](http://arxiv.org/abs/2410.17098)

**マスク化差分プライバシー**

David Schneider, Sina Sajadmanesh, Vikash Sehwag, Saquib Sarfraz, Rainer Stiefelhagen, Lingjuan Lyu, Vivek Sharma

- プライバシー保護付きコンピュータビジョンはMLとAIにおいて重要な問題
- 既存手法では差分プライバシーや匿名化技術を使用し、モデルの有用性が犠牲
- 提案するマスク化差分プライバシー(MaskDP)は、データの敏感領域を選択的に制御可能
- 実験で、特に$\epsilon<1$の条件で標準的手法より良い有用性とプライバシーのトレードオフを実現

新しいプライバシー技術で、データの特定部分だけに差分プライバシーを適用するアイデアはおもしろいね！精度を保ちつつプライバシーも守れるなんて、絶妙なバランスが取れそうで期待しちゃう。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CV, 68T45, I.4.m, **投稿日時:** 2024-10-22 15:22

- - -

### [On the Vulnerability of Text Sanitization](http://arxiv.org/abs/2410.17052)

**テキストサニタイズの脆弱性について**

Meng Tong, Kejiang Chen, Xiaojian Yuang, Jiayang Liu, Weiming Zhang, Nenghai Yu, Jie Zhang

- テキストサニタイズは差分プライバシーを用いて敏感なトークンを置換しプライバシーを保護する手法
- 現在の再構成攻撃は経験的に開発されており、効果を正確に評価するのが難しい
- 本論文では、理論的に最適な再構成攻撃を実装し、攻撃成功率の限界を導出した
- 提案する攻撃が、既存の最先端手法に比べて攻撃成功率を46.4%向上させることを示した

テキストの敏感情報を差し替えるテキストサニタイズは、攻撃に対してまだまだ研究の余地があるって感じだね。今後、どんな新しい攻撃や防御手法が出てくるのか、少しワクワクしちゃうな！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-22 14:31

- - -

### [Beyond Yao's Millionaires: Secure Multi-Party Computation of Non-Polynomial Functions](http://arxiv.org/abs/2410.17000)

**ヤオの百万長者問題を超えて：非多項式関数の安全なマルチパーティ計算**

Seyed Reza Hoseini Najarkolaei, Mohammad Mahdi Mojahedian, Mohammad Reza Aref

- シャミア秘密分散を用いて、秘密の入力を明かさずに$N$個のプライベートな数の最大値を決定するスキームを提案
- 提案スキームは、計算複雑性が低く、既存の二つの数を比較する方法より効率的である
- 提案スキームは情報理論的に安全で、最小値、中央値、順位などの非多項式関数の計算も可能
- フェデレーテッドラーニングを含む様々な応用が考えられ、各パーティが結果の一部を保持する

この論文は、連合学習に使えそうな秘密計算の進化を感じる！シャミア秘密分散を駆使するところとか、ちょっとワクワクしない？私たちのデータをしっかり守りながら、みんなで賢く学んでいける未来が楽しみだなぁ。

**Comment:** 11 pages, 4 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.IT, math.IT, **投稿日時:** 2024-10-22 13:22

- - -

### [Learning Mathematical Rules with Large Language Models](http://arxiv.org/abs/2410.16973)

**大規模言語モデルによる数学的規則の学習**

Antoine Gorceix, Bastien Le Chenadec, Ahmad Rammal, Nelson Vadori, Manuela Veloso

- 大規模言語モデルが分配法則や方程式の簡略化などの数学的規則を学習する能力を研究
- 規則を一般化し、単語問題の文脈で再利用する能力を実証的に分析
- 合成データ構築のための厳密な方法論を提供し、モデルのファインチューニングを実施
- 規則の学習や一般化、単語問題での再利用が可能であることを実験で示す

数学的な規則をAIが学習して使いこなせるってすごいね！これからもっと複雑な数学問題もAIが解けるようになるとしたら、勉強の仕方も変わるかも！

**Comment:** 4th MATH-AI Workshop at NeurIPS'24

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-10-22 12:51

- - -

### [SleepCoT: A Lightweight Personalized Sleep Health Model via Chain-of-Thought Distillation](http://arxiv.org/abs/2410.16924)

**SleepCoT: 連鎖思考蒸留を用いた軽量なパーソナライズ睡眠健康モデル**

Huimin Zheng, Xiaofeng Xing, Xiangmin Xu

- 連鎖思考蒸留によって小規模モデルが大規模モデルと同等の性能を発揮
- 問題解決戦略や専門知識を、大規模モデルから小型で効率的なモデルに移植
- 睡眠健康の個別提案や質問対応、専門知識への回答機能を提供
- 100のシミュレートされた睡眠レポートと1000の質問を通じて性能を実証

この研究、すごくユニーク！小さなモデルで大きな成果を出せるなんて、未来の医療がもっと身近に感じられるね。現実世界での応用が進めば、私たちの健康管理もどんどん進化しそうでワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-10-22 11:56

- - -

### [CK4Gen: A Knowledge Distillation Framework for Generating High-Utility Synthetic Survival Datasets in Healthcare](http://arxiv.org/abs/2410.16872)

**CK4Gen: 医療分野での高有用性合成生存データセット生成のための知識蒸留フレームワーク**

Nicholas I-Hsien Kuo, Blanca Gallego, Louisa Jorm

- プライバシー規制が臨床データへのアクセスを制限し、研究と教育が停滞している。
- 現行の生成モデルは表面的なリアリズムを重視し、医療用途の実用性が低い。
- CK4GenはCoxPHモデルの知識蒸留を活用して、臨床的特徴を保つ合成データを生成する。
- CK4Genは異なる臨床条件に対応でき、公開データ生成に適した合成データを提供する。

合成データって面白いよね！CK4Genならプライバシーを守りながら医療研究が進むって最高じゃん！未来の医療研究がもっとスムーズにいくといいなー。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-22 10:20

- - -

### [Federated Causal Inference: Multi-Centric ATE Estimation beyond Meta-Analysis](http://arxiv.org/abs/2410.16870)

**連合因果推論: メタアナリシスを超えた多中心ATE推定**

Rémi Khellaf, Aurélien Bellet, Julie Josse

- 連合因果推論が分散データから治療効果を推定する方法として研究
- ATE推定器を3種比較：メタ分析、単回連合学習、多回連合学習
- 線形モデルにおけるこれらの推定器の漸近分散をRCTに基づいて導出
- シナリオに応じた適切な推定器選択のための実践的ガイダンスを提供

これ、すごいよね！連合学習を使って因果推論を進化させちゃうなんて。RCTの結果を効率的にまとめる方法が増えたら、きっと医療とかでも大活躍だよね。🔍💡✨



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.LG, math.ST, stat.TH, **投稿日時:** 2024-10-22 10:19

- - -

### [Masked Clinical Modelling: A Framework for Synthetic and Augmented Survival Data Generation](http://arxiv.org/abs/2410.16811)

**マスクされた臨床モデリング: 合成および強化生存データ生成のフレームワーク**

Nicholas I-Hsien Kuo, Blanca Gallego, Louisa Jorm

- プライバシー義務で臨床データへのアクセスが制限される問題がある
- 合成データは安全なデータ共有とモデル開発の解決策となる
- 合成データの実用性を重視し、Masked Clinical Modelling (MCM) を提案
- MCMは生存分析で優れた識別と校正を提供し、既存手法を上回る性能を示した

臨床データの合成にMCMを使うって、なんかすごく実用的！データのプライバシーを守りつつも、ちゃんと学べるモデルが作れそうで楽しみだよね。生存分析に強いとか、これからの医療研究に役立ちそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-22 08:38

- - -

### [Forewarned is Forearmed: Leveraging LLMs for Data Synthesis through Failure-Inducing Exploration](http://arxiv.org/abs/2410.16736)

**備えあれば憂いなし: 失敗誘発的探求によるLLMを活用したデータ合成**

Qintong Li, Jiahui Gao, Sheng Wang, Renjie Pi, Xueliang Zhao, Chuan Wu, Xin Jiang, Zhenguo Li, Lingpeng Kong

- LLMは多様で高品質なデータでの訓練により優れた成果を出すが、手動設計の依存で限界がある。
- ReverseGenは自動的に訓練サンプルを生成し、LLMの弱点を暴露するための新たなアプローチ。
- 提案する技術は、失敗を誘発するクエリを作成し、それを用いて効果的な訓練データを構築。
- 3つの重要なアプリケーションで評価し、多様かつ効果的なデータを生み出すとともに、他の手法を上回る性能向上を実証。

このReverseGenって、失敗から学ぶっていう面白いアプローチだよね！しかも、モデルの性能をしっかり改善できるみたいで、未来のAIがもっと賢くなる予感がするよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-22 06:43

- - -

### [Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World](http://arxiv.org/abs/2410.16713)

**崩壊するか繁栄するか？自己生成する世界における合成データの危険と約束**

Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo

- AI生成コンテンツが多い中、モデルが合成データのみで訓練されると劣化するリスクがある
- 実データと合成データを蓄積し続ける方法で崩壊を回避できる可能性を示す
- 固定された計算資源での妥協シナリオでは、テスト損失が蓄積シナリオよりも大きくなるが収束する
- 実データの絶対量が合成データの価値に影響し、モデル崩壊回避には実データの割合が重要

この研究、合成データがどのくらい影響を与えるか一緒に考えてるのめっちゃいいよね。未来のAIモデルがどう発展していくか予想するのにすごく役立ちそう！私たちも自分たちの日常でデータの重要性をもっと感じられるようになるかな？



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-22 05:49

- - -

### [Privacy-hardened and hallucination-resistant synthetic data generation with logic-solvers](http://arxiv.org/abs/2410.16705)

**プライバシー強化と幻影耐性を備えた論理ソルバーによる合成データ生成**

Mark A. Burgess, Brendan Hosking, Roc Reguant, Anubhav Kaphle, Mitchell J. O'Brien, Letitia M. F. Sng, Yatish Jain, Denis C. Bauer

- 合成データの生成はAI訓練やデータ共有に価値があるが、プライバシーと正確性の確保が課題
- Genomatorという論理ソルバー(SAT)を用い、効率的かつプライバシーを守ったデータを生成
- Genomatorは最新技術に比べて正確性が84-93%向上し、プライバシーが95-98%向上
- プライバシーと精度のトレードオフを調整し、医療研究などに貢献する可能性がある

Genomatorって合成データ生成の未来を変えるかもね！プライバシーを守りながら正確なデータを作るなんてすごい。今後の医療研究やデータ共有にも役立ちそう。ワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CR, cs.CY, cs.LG, **投稿日時:** 2024-10-22 05:20

- - -

### [Graph Transformers Dream of Electric Flow](http://arxiv.org/abs/2410.16699)

**グラフ・トランスフォーマーは電気的フローの夢を見る**

Xiang Cheng, Lawrence Carin, Suvrit Sra

- 線形トランスフォーマーをグラフデータに適用し、電気的フローや固有ベクトル分解を解決できることを示す
- トランスフォーマーの入力はグラフのインシデンス行列であり、位置エンコーディング情報は不要
- 各グラフアルゴリズムを実装するための明示的な重み構成を提示し、誤差の境界を検証
- 実験により、ラプラシアン固有ベクトルに基づくエンコーディングより効果的な位置エンコーディングの学習を確認

グラフデータを扱うトランスフォーマーの仕組みを理解する一歩みたい！理論と実験が結びつくのってスゴイね、未来のデータ解析がもっと楽しくなりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-22 05:11

- - -

### [No more hard prompts: SoftSRV prompting for synthetic data generation](http://arxiv.org/abs/2410.16534)

**もうハードプロンプトはいらない: 合成データ生成のためのSoftSRVプロンプト法**

Giulia DeSalvo, Giulia DeSalvo, Jean-Fracois Kagy, Lazaros Karydas, Afshin Rostamizadeh, Sanjiv Kumar

- SoftSRVは事前学習済み大規模言語モデルを用いてターゲットに近い合成テキストを生成する。
- データ駆動型の損失最小化手法を用いて、文脈に応じたソフトプロンプトを訓練する。
- SoftSRVは手間のかかるハードプロンプトより実用的で、多様なドメインに対応可能である。
- 評価結果では、SoftSRVが合成データ生成における性能向上を示し、ターゲットに近づけた。

合成データ生成におけるソフトプロンプトの使い方がすごく賢いなって思う！いろいろなドメインで試行錯誤しなくてもいいなんて、未来の技術が待ちきれないよね。きっとこれからもっと簡単にデータ作りができそうだね！😊



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-21 21:48

- - -

### [To the Globe (TTG): Towards Language-Driven Guaranteed Travel Planning](http://arxiv.org/abs/2410.16456)

**グローブへ: 言語駆動型の保証付き旅行計画に向けて**

Da JU, Song Jiang, Andrew Cohen, Aaron Foss, Sasha Mitts, Arman Zharmagambetov, Brandon Amos, Xian Li, Justine T Kao, Maryam Fazel-Zarandi, Yuandong Tian

- 旅行計画は、フライトや宿泊、観光などの制約を満たす旅程を探す困難なタスク。
- TTGは自然言語要求を受け、LLMで翻訳し、最適な旅程を生成するシステム。
- 合成データパイプラインを開発し、人手によらずシンボル形式のトレーニングデータを生成。
- ユーザー評価で高いNPSを達成し、迅速で正確な旅行計画を提供。

このシステム、リアルタイムで旅行計画ができちゃうとか未来感がすごいよね！忙しい人や旅行初心者には超嬉しいサービスになりそう。きちんとニーズを捉えてくれるなら、ぜひ試してみたい！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-21 19:30

- - -

### [Secure Computation and Trustless Data Intermediaries in Data Spaces](http://arxiv.org/abs/2410.16442)

**データ空間における安全な計算とインターミディアリーに頼らないデータ仲介者**

Christoph Fabianek, Stephan Krenn, Thomas Loruenser, Veronika Siska

- 進化するデータ経済における安全で信頼できるデータ共有を実現するための、暗号技術を組み込んだ安全な計算の利用
- EUデータガバナンス法に従ったデータ仲介者の役割を分析し、利用者データにアクセスしない仲介者の概念を導入
- セキュアマルチパーティ計算と完全準同型暗号を活用し、セキュリティの利点を強調
- 身元管理、政策実施、ノード選択、アクセス制御といった統合の課題を現実のケースを通して解決

この研究では、難しい暗号技術を使っているみたいだけど、それを使ってデータを安全に使う方法を考えているところが面白い！データ仲介者がデータを覗けないって、未来のプライバシーはこうやって守られるのかなぁってわくわくしたなぁ。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-21 19:10

- - -

### [Position: Challenges and Opportunities for Differential Privacy in the U.S. Federal Government](http://arxiv.org/abs/2410.16423)

**位置: 米国連邦政府における差分プライバシーの課題と機会**

Amol Khanna, Adam McCormick, Andre Nguyen, Chris Aguirre, Edward Raff

- 差分プライバシーの導入には現時点で3つの重要な課題がある
- 定量的な特徴を活かし、異なるプライバシーレベルの分析を提供可能
- 新しい発見として、差分プライバシーが機密分野での人員効率を向上させる可能性
- 技術者や規制者、法制定者への理解促進を目指す非技術的リソースとしての役割を果たす

差分プライバシーがいろんな場面で役立ちそうで面白い！特に機密分野での人員効率向上は新鮮な発見だね。未来にどんな影響を与えるのか、期待しちゃう！

**Comment:** 2nd Workshop on Regulatable ML at NeurIPS 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-10-21 18:46

- - -

### [Subword Embedding from Bytes Gains Privacy without Sacrificing Accuracy and Complexity](http://arxiv.org/abs/2410.16410)

**バイトからのサブワード埋め込みは精度と複雑性を犠牲にせずプライバシーを向上させる**

Mengjiao Zhang, Jia Xu

- NLPモデルのプライバシー侵害が懸念され、特に埋め込み攻撃の防護が課題である
- 提案手法であるSEBは、サブワードをバイト列にエンコードし、テキスト回復を困難にする
- SEBは小さなメモリで効率を維持し、埋め込み攻撃からの保護を強化する
- 機械翻訳や言語モデリングで標準手法よりも優れた精度と効率を証明

攻撃からのプライバシー保護をしつつ、効率もアップするなんて夢みたい！データを守りつつ進化する技術の可能性がいっぱいで、未来の私たちの生活を考えるとワクワクしちゃうね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, **投稿日時:** 2024-10-21 18:25

- - -

### [Synthetic Data Generation in Cybersecurity: A Comparative Analysis](http://arxiv.org/abs/2410.16326)

**サイバーセキュリティにおける合成データ生成の比較分析**

Dure Adan Ammara, Jianguo Ding, Kurt Tutschku

- 合成データ生成は、特に表形式データで実データを正確に再現するための課題がある
- ネットワークトラフィックの合成データ生成で最も効果的な手法はまだ未解明
- GANモデル（CTGAN、CopulaGANなど）が非AIや従来のAI手法よりも高い忠実度と有用性を示す
- サイバーセキュリティデータにおいて特徴選択に相互情報量を使用しデータ品質を向上

GANを用いた合成データ生成がかなり効果的みたい！特にCTGANとCopulaGANが優れてるって驚き。サイバーセキュリティの分野で新しい可能性が見えそうでワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-18 14:19
