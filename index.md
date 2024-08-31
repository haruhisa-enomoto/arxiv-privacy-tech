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

更新: 2024-08-31T04:20:50.727299

- - -

### [Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal Sampling](http://arxiv.org/abs/2408.16737)

**小さく、弱く、それでも優れている：計算最適なサンプリングを用いたLLM推論者の訓練**

Hritik Bansal, Arian Hosseini, Rishabh Agarwal, Vinh Q. Tran, Mehran Kazemi

- 強力な言語モデル（LM）から高品質な合成データを使用するのが一般的な戦略
- 合成データ生成における強力で高価なモデル（SE）と弱く安価なモデル（WC）のトレードオフを調査
- WCモデルのデータはカバレッジと多様性が高いが、誤検知率も高い
- WC生成データで学習したモデルが複数のベンチマークでSE生成データを上回る

めっちゃおもしろそう！弱いモデルの方が強いモデルより結果が良い場合もあるって、逆転の発想だね。次世代のAI訓練法がこれで変わるかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-08-29 17:32

- - -

### [Spurfies: Sparse Surface Reconstruction using Local Geometry Priors](http://arxiv.org/abs/2408.16544)

**Spurfies: 局所的な幾何プリエアを用いた希薄な表面再構成**

Kevin Raj, Christopher Wewer, Raza Yunus, Eddy Ilg, Jan Eric Lenssen

- Spurfiesは、外観と幾何情報を分離し、合成データを用いた局所幾何プリエアを利用
- 一般的な3D再構成方法は多数の画像を必要とし、少数ビューの場面では困難
- 新しい手法は、内接幾何プリエアを用い希薄な入力ビューから表面・外観を再構成
- DTUデータセットで検証し、以前の最先端技術より35%優れた表面品質を達成

この新しい手法、面白そうだね！合成データを利用することで、少数の画像でも精度が上がるなんてすごいよね。いろんな応用が考えられそうだから、これからもっと発展しそう！

**Comment:** https://geometric-rl.mpi-inf.mpg.de/spurfies/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-29 14:02

- - -

### [MICDrop: Masking Image and Depth Features via Complementary Dropout for Domain-Adaptive Semantic Segmentation](http://arxiv.org/abs/2408.16478)

**MICDrop: 補完ドロップアウトによるドメイン適応型セマンティックセグメンテーションのための画像および深度特徴のマスキング**

Linyan Yang, Lukas Hoyer, Mark Weber, Tobias Fischer, Dengxin Dai, Laura Leal-Taixé, Marc Pollefeys, Daniel Cremers, Luc Van Gool

- 現在のUDA方法は細かい構造で劣る結果を示し、曖昧な外観のオブジェクトを過剰にセグメント化する傾向がある
- 幾何情報（すなわち、深度予測）を活用する提案。深度の不連続性がセグメンテーション境界と一致することが多い
- 提案手法MICDropは画像エンコーダー特徴をマスキングしつつ、逆に深度エンコーダー特徴をマスキングすることで、共同特徴表現を学習
- 特徴融合モジュールを提案し、グローバルとローカル情報共有を改善し、深度予測の誤差にも強靭

新しいセグメンテーション手法として深度情報をうまく使うのが面白いね。色んなUDA手法にも対応できるのがすごいと思った！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-29 12:15

- - -

### [Self-Improving Diffusion Models with Synthetic Data](http://arxiv.org/abs/2408.16333)

**合成データを用いた自己改善型拡散モデル**

Sina Alemohammad, Ahmed Imtiaz Humayun, Shruti Agarwal, John Collomosse, Richard Baraniuk

- 現在のAIは大規模生成モデルの訓練用の実データが不足している
- 合成データを使った訓練はモデルオートファジー障害(MAD)とモデル崩壊の原因となる
- SIMSは自己合成データを使い、生成過程を理想的な実データ分布へ誘導する手法を提案
- CIFAR-10やImageNet-64の生成で新記録を打ち立て、自己生成データを使ってもMADを避けられる

自己生成データでモデルがどんどん良くなってくなんてめっちゃ可能性ありそう！偏りもなくせるって超未来的だよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-29 08:12

- - -

### [OpenFGL: A Comprehensive Benchmarks for Federated Graph Learning](http://arxiv.org/abs/2408.16288)

**OpenFGL: 連合グラフ学習の包括的ベンチマーク**

Xunkai Li, Yinlin Zhu, Boyang Pang, Guochen Yan, Yeyu Yan, Zening Li, Zhengyu Wu, Wentao Zhang, Rong-Hua Li, Guoren Wang

- 連合グラフ学習は、直接のデータ共有なしで複数のローカルシステム間でグラフニューラルネットワークの分散トレーニングを可能にする
- OpenFGLはGraph-FLとSubgraph-FLの主要シナリオに対して設計された統一ベンチマーク
- 16のアプリケーションドメインからの38のグラフデータセット、8つの連邦データシミュレーション戦略、および5つのグラフベースの下流タスクを含む
- 最近提案された18のSOTA FGLアルゴリズムをユーザーフレンドリーなAPIを通じて提供し、その効果、堅牢性、効率性を徹底的に比較評価可能

連合グラフ学習やばい！どこまで進化するのかワクワクするよね。未来のデータ共有ってこうなっていくのかなって期待が膨らむ！

**Comment:** Under Review

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DB, cs.SI, **投稿日時:** 2024-08-29 06:40

- - -

### [SAU: A Dual-Branch Network to Enhance Long-Tailed Recognition via Generative Models](http://arxiv.org/abs/2408.16273)

**SAU: 生成モデルを用いた長尾認識の向上を目指す二重分岐ネットワーク**

Guangxi Li, Yinsheng Song, Mingkai Zheng

- 画像認識において長尾分布は、少数の支配的なクラスと多くのマイノリティクラスの不均衡が課題
- 生成モデルを使って合成データを作成し、不均衡を解消する提案
- 現実のデータと合成データを混在させるSynthetic-AwareとUnawareの二枝モデルを設計
- 提案手法はCIFAR-10-LTとCIFAR-100-LTでのTop-1精度で最先端を達成

生成モデルを使ってデータの不均衡を解消するなんて面白そう！先行研究を超える精度を達成したのもすごいよね。これからもっと実用化が進むのかも。

**Comment:** 15 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-29 05:33

- - -

### [Monadring: A lightweight consensus protocol to offer Validation-as-a-Service to AVS nodes](http://arxiv.org/abs/2408.16094)

**Monadring: 検証をサービスとして提供するための軽量コンセンサスプロトコル**

Yu Zhang, Xiao Yan, Gang Tang, Helena Wang

- 既存のブロックチェーンネットワークは大規模で、全体の同期が必要だが、計算コストが高い
- Monadringという新たなプロトコルを提案、より速く費用対効果の高い計算を実現
- Verifiable Random Function (VRF)と準同型暗号を用いてセキュリティ強化
- シミュレーション実験により、性能と実現可能性を評価

ネーミングの「Monadring」がカッコイイし、軽量っていうところが使いやすそうでいいよね。これが普及すれば、ブロックチェーンのハードルもぐっと下がる気がするなぁ。

**Comment:** 23 pages, 3 figures

**トピック:** [準同型暗号](he), **カテゴリ:** cs.DC, **投稿日時:** 2024-08-28 18:55

- - -

### [Analysis of Diagnostics (Part II): Prevalence, Linear Independence, and Unsupervised Learning](http://arxiv.org/abs/2408.16035)

**診断分析 (第2部): 有病率、線形独立、無監督学習**

Paul N. Patrone, Raquel A. Binder, Catherine S. Forconi, Ann M. Moormann, Anthony J. Kearsley

- 診断テストを用いて有病率、不確実性定量化、分類理論の関係を明らかにする研究
- 無監督学習タスクへ結果を拡張するための線形代数の概念を考察
- 未知のクラスを持つサンプルの分布を有病率でパラメータ化し線形独立の概念を導入
- 合成データとSARS-CoV-2 ELISAの文脈で手法の有効性を立証

無監督学習が監督学習の一般化になるなんて超知的！診断テストをこんな形で応用する発想が面白い。



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, math.PR, **投稿日時:** 2024-08-28 13:39

- - -

### [Differentially Private Publication of Electricity Time Series Data in Smart Grids](http://arxiv.org/abs/2408.16017)

**スマートグリッドにおける電力時系列データの差分プライバシー出版**

Sina Shaham, Gabriel Ghinita, Bhaskar Krishnamachari, Cyrus Shahabi

- スマートグリッドのデータは消費者行動の研究とエネルギー政策決定に重要
- 差分プライバシーは個々のデータの保護に適しているが、時系列データの有用性を損なう
- 新手法STPTはRNNを活用し、時空間属性を分析して微小から大規模パターンを捉える
- 実世界と合成データセット両方で実験し、STPTが既存ベンチマークを上回る結果を示す

プライバシーを守りながらデータの有用性も保つ新しい手法が登場だね！RNNを使ってるのも面白いから、今後技術がもっと進化しそう。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-08-24 23:30
