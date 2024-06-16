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

更新: 2024-06-16T04:18:09.805723

- - -

### [SimGen: Simulator-conditioned Driving Scene Generation](http://arxiv.org/abs/2406.09386)

**SimGen: シミュレータ調整型運転シーン生成**

Yunsong Zhou, Michael Simon, Zhenghao Peng, Sicheng Mo, Hongzi Zhu, Minyi Guo, Bolei Zhou

- 合成データ生成により自動運転研究のアノテーションコストが大幅に削減可能
- 既存の手法は3Dオブジェクト配置に基づいて運転画像を生成するがデータセットが小規模
- SimGenフレームワークはシミュレータと実世界のデータをミックスし多様な運転シーンを生成
- DIVAデータセットを活用し、多条件のギャップを解消しつつ生成品質と多様性を向上

おもしろそう！SimGenがリアルな運転場面をミックスして生成するなんて、もっと安全な自動運転が実現しそう♡ これからの自動運転技術、楽しみだよね〜



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-13 17:58

- - -

### [Understanding Hallucinations in Diffusion Models through Mode Interpolation](http://arxiv.org/abs/2406.09358)

**拡散モデルにおけるモード補間を通じた幻覚の理解**

Sumukh K Aithal, Pratyush Maini, Zachary C. Lipton, J. Zico Kolter

- 拡散プロセスに基づく画像生成モデルは、訓練データに存在しない「幻覚」を生成する
- この研究はモード補間という特定の失敗モードを調査し、元の訓練分布の外にあるサンプルを生成
- 1Dおよび2D ガウスモデルでの実験により、不連続な損失ランドスケープが幻覚を引き起こす原因を解明
- 簡単なメトリックを用いて、生成時に95%以上の幻覚を除去しつつ96%のサンプルを保持することが可能

拡散モデルが自己修正する方法があるのは面白いね！訓練データ外のサンプルを簡単に判別できるなんて、未来の画像生成技術がもっと進化しそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-13 17:43

- - -

### [Deep Transformer Network for Monocular Pose Estimation of Ship-Based UAV](http://arxiv.org/abs/2406.09260)

**船上UAVの単眼姿勢推定のためのディープトランスフォーマーネットワーク**

Maneesha Wickramasuriya, Taeyoung Lee, Murray Snyder

- 単眼画像を用いて無人航空機（UAV）の相対的な6次元ポーズを推定するディープトランスフォーマーネットワークを紹介
- 多数の船のパーツを2次元のキーポイントでアノテートした合成データセットを作成
- トランスフォーマーネットワークはこれらのキーポイントを検出し、各パーツの6次元ポーズを推定
- ベイジアン融合を用いて推定値を統合し、様々な照明条件下での頑健性と精度を実証

船上のUAV着陸の自動化とかもできちゃうんだって！いろんな気象条件でも使えるのはすごく将来性ありそう！

**Comment:** 23 pages, 25 figures, 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.RO, eess.IV, **投稿日時:** 2024-06-13 16:01

- - -

### [EncCluster: Scalable Functional Encryption in Federated Learning through Weight Clustering and Probabilistic Filters](http://arxiv.org/abs/2406.09152)

**EncCluster: 重みクラスタリングと確率フィルタによる連合学習のスケーラブルな機能暗号化**

Vasileios Tsouvalas, Samaneh Mohammadi, Ali Balador, Tanir Ozcelebi, Francesco Flammini, Nirvana Meratnia

- 連合学習は地方分散型デバイス間でモデルを訓練し、ローカルモデル更新のみを集約サーバに送信
- 通常の連合学習は推論攻撃のリスクがある
- EncClusterは重みクラスタリングと確率フィルタを統合し、性能に影響なく強力なプライバシー保証を提供
- EncClusterは通信コストを従来の方法よりも大幅に削減し、暗号化速度を4倍超に向上させる

具体的な手法は難しそうだけど、プライバシーを守りながら効率も良くなるなんてすごいね！未来の連合学習の標準になりそう♡

**Comment:** 21 pages, 4 figures

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DC, cs.LG, **投稿日時:** 2024-06-13 14:16

- - -

### [HDNet: Physics-Inspired Neural Network for Flow Estimation based on Helmholtz Decomposition](http://arxiv.org/abs/2406.08570)

**HDNet: ヘルムホルツ分解に基づく物理インスパイアニューラルネットワークによるフロー推定**

Miao Qi, Ramzi Idoughi, Wolfgang Heidrich

- フロー推定問題は科学的イメージングで広く見られる
- 物理的制約（発散なし、回転なし）を利用した推定が重要
- HDNetは入力フローを発散と回転成分に分解するニューラルネットワーク
- 専ら合成データで訓練され、様々なフロー推定問題に適用可能

物理の知識を使ったニューラルネットってすごい！どんなフローでも使えそうで今後の研究が楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-12 18:11

- - -

### [Noise-Aware Differentially Private Regression via Meta-Learning](http://arxiv.org/abs/2406.08569)

**ノイズに対応した差分プライバシー回帰：メタ学習を通じて**

Ossi Räisä, Stratis Markou, Matthew Ashman, Wessel P. Bruinsma, Marlon Tobaben, Antti Honkela, Richard E. Turner

- 差分プライバシー（DP）はユーザープライバシー保護のゴールドスタンダードだが、通常のDPメカニズムは性能を大幅に低下させる
- シミュレーションデータを用いて事前学習を行い、プライベートデータでのDP学習前にモデルをプレトレーニングするアプローチを提案
- コンボリューショナル適条件ニューラルプロセス（ConvCNP）と改良されたDPメカニズムを組み合わせたメタ学習モデル（DPConvCNP）を開発
- DPConvCNPは特に非ガウスデータにおいて、DPガウス過程(GP)ベースラインを上回り、テスト時に高速かつ調整が少なく済む

メタ学習を取り入れた差分プライバシー回帰モデルって面白そう！特に非ガウスデータでの性能向上は期待できるねー。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-06-12 18:11

- - -

### [IMFL-AIGC: Incentive Mechanism Design for Federated Learning Empowered by Artificial Intelligence Generated Content](http://arxiv.org/abs/2406.08526)

**IMFL-AIGC: 連合学習を強化する人工知能生成コンテンツのためのインセンティブ機構設計**

Guangjing Huang, Qiong Wu, Jingyi Li, Xu Chen

- 連合学習は、クライアントがデータを共有せずに協力してモデルを訓練できる画期的な枠組み
- データ品質の異質性を軽減するため、人工知能生成コンテンツ（AIGC）が新たなデータ合成技術として利用可能
- AIGCを取り入れた連合学習の費用（計算やデータ合成のコスト）が参加の阻害要因となる
- 提案されたデータ品質評価法とインセンティブ機構により、トレーニングの精度向上とコスト削減が実現

連合学習とAI生成データを組み合わせた新しいアプローチだね！これが実現すれば、もっと効率的にモデルを訓練できる未来が楽しみだな～。

**Comment:** The paper has been accepted by IEEE Transactions on Mobile Computing

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.DC, cs.GT, **投稿日時:** 2024-06-12 07:47

- - -

### [Automated Question Generation for Science Tests in Arabic Language Using NLP Techniques](http://arxiv.org/abs/2406.08520)

**自然言語処理技術を用いたアラビア語理科試験の自動問題生成**

Mohammad Tami, Huthaifa I. Ashqar, Mohammed Elhenawy

- 教育評価のための自動質問生成は教育技術分野で重要
- 最近の研究はアラビア語での評価質問生成に挑戦も、文解析の誤りや名前認識の問題などが影響
- 3つの段階（キーワード抽出、質問生成、ランキング）で構築されたシステムを提案
- 提案された方法は精度83.50%、再現率78.68%、F1スコア80.95%を達成し、人間評価で84%の平均評価

実際にアラビア語での質問生成って本当に難しいんだね。でも、この研究が後々もっと広がって、他の言語にも活きそうで超ワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.CY, **投稿日時:** 2024-06-11 20:27
