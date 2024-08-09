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

更新: 2024-08-09T04:20:11.642543

- - -

### [Better Alignment with Instruction Back-and-Forth Translation](http://arxiv.org/abs/2408.04614)

**命令の前後翻訳によるより良い整合性**

Thao Nguyen, Jeffrey Li, Sewoong Oh, Ludwig Schmidt, Jason Weston, Luke Zettlemoyer, Xian Li

- 命令の前後翻訳を用いて高品質な合成データを生成し、LLMを整合させる
- Webコーパスの文書から合成命令を生成し、さらに文書を基に応答を改良
- (前後翻訳命令、改良応答)ペアでファインチューニングし、他の命令データセットより高い勝率を達成
- 前後翻訳命令は他の合成命令よりも高品質で、応答も蒸留法より多様かつ複雑

前後翻訳って面白そう！今後、AIの応答がもっと人間らしく、賢くなるかも。どんな応答が返ってくるのか試してみたいね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-08-08 17:42

- - -

### [Img-Diff: Contrastive Data Synthesis for Multimodal Large Language Models](http://arxiv.org/abs/2408.04594)

**Img-Diff: マルチモーダル大規模言語モデルのための対比データ合成**

Qirui Jiao, Daoyuan Chen, Yilun Huang, Yaliang Li, Ying Shen

- 対比学習と画像差分キャプションを活用し、細かな画像認識を向上させる新たなデータセットを提案
- Stable-Diffusion-XLモデルと高度な画像編集技術を用いて「オブジェクト置換」を強調した類似画像のペアを作成
- 提案データセットでMLLMsを微調整し、画像差分および視覚的質問応答タスクで性能スコアが飛躍的に向上
- 「オブジェクト削除」などの代替生成方法を調査し、データセットの多様性、品質、堅牢性を確認

マルチモーダルな画像理解の向上ってすごいよね。実際のデータも公開されてるみたいだし、今後の研究が楽しみだな！

**Comment:** 14 pages, 9 figures, 7 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-08-08 17:10

- - -

### [NFDI4Health workflow and service for synthetic data generation, assessment and risk management](http://arxiv.org/abs/2408.04478)

**合成データ生成、評価、およびリスク管理のためのNFDI4Healthワークフローとサービス**

Sobhan Moazemi, Tim Adams, Hwei Geok NG, Lisa Kühnel, Julian Schneider, Anatol-Fiete Näher, Juliane Fluck, Holger Fröhlich

- 個人の健康データは科学の進歩に不可欠だが、プライバシーの懸念から共有が制限されることが多い
- 合成データ生成は、実際のデータの統計的特性を模倣しながら機密情報を保護する技術である
- NFDI4Healthプロジェクトにおいて、VAMBNとMultiNODEという2つのAIツールが最先端の合成データ生成ツールとして活用されている
- SYNDATは公開されたウェブベースのツールであり、生成モデルによる合成データの品質とリスクを視覚化・評価することができる

実際の患者データを使わずにAIを開発できるようになるって未来感がすごい！SYNDATみたいなツールが普及したら、もっと安心してデータ使えちゃうね。

**Comment:** 9 pages, 4 figures, accepted for publication in the proceedings of   the 69th Annual Conference of the Society for Medical Informatics, Biometry   and Epidemiology (GMDS)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-08 14:08

- - -

### [FedAD-Bench: A Unified Benchmark for Federated Unsupervised Anomaly Detection in Tabular Data](http://arxiv.org/abs/2408.04442)

**FedAD-Bench: 表形式データにおける連合型教師なし異常検知のための統一ベンチマーク**

Ahmed Anwar, Brian Moser, Dayananda Herurkar, Federico Raue, Vinit Hegiste, Tatjana Legler, Andreas Dengel

- 連合学習（FL）は、分散データをプライバシーを保ちながら活用する有望なアプローチ
- FLと異常検知の組み合わせにより、サイバーセキュリティや医療などの重要かつ希少な異常を検出可能
- FedAD-Benchは、FL環境下での教師なし異常検知アルゴリズムを評価するための統一ベンチマーク
- 実験でモデルの統合効率の低さや指標の信頼性の問題を特定、FLの正則化効果で過学習を軽減

面白そう！異常検知がFLでどう強化されるのか気になるよね。医療分野とかで安全にデータ使えるようになったら、すごいって思う！

**Comment:** 8 pages, 1 figure

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-08 13:14

- - -

### [Federated Cubic Regularized Newton Learning with Sparsification-amplified Differential Privacy](http://arxiv.org/abs/2408.04315)

**連合学習におけるスパース化を強化した差分プライバシーによるキュービック正則化ニュートン法**

Wei Huo, Changxin Liu, Kemi Ding, Karl Henrik Johansson, Ling Shi

- トピックは連合学習とプライバシー漏洩や通信ボトルネックの問題
- キュービック正則化ニュートン法を導入し、従来の一階手法より繰り返し複雑度を低減
- ノイズ付加によるプライバシー確保と、アップリンクのスパース化で通信コストを削減
- アルゴリズムの収束特性とプライバシー保証を分析し、ベンチマークデータセットで有効性を実証

タイトルからして新しい手法だよね。効果的なプライバシー保護が連合学習でどれだけ進んでるか気になる！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.SY, eess.SY, **投稿日時:** 2024-08-08 08:48

- - -

### [Constructing Adversarial Examples for Vertical Federated Learning: Optimal Client Corruption through Multi-Armed Bandit](http://arxiv.org/abs/2408.04310)

**縦型連合学習（VFL）のための敵対的サンプル構築：バンディットアルゴリズムによる最適クライアント破損**

Duanyi Yao, Songze Li, Ye Xue, Jin Liu

- VFLは金融、医療、IoTシステムなどで多くの応用がある
- 敵対例の注入による攻撃がVFLモデルのセキュリティに重大な挑戦をもたらす
- 問題をオンライン最適化問題として定式化し、AE生成と破損パターン選択に分解
- 最適な破損パターンを効率的に特定するE-TSアルゴリズムを提案し、その有効性を実証

VFLのセキュリティに関する研究、ちょっとスリリングだね。どんなふうに敵対例が効率よく見つかるか、実際に見てみたいな！

**Comment:** Published on ICLR2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-08-08 08:42

- - -

### [Tackling Noisy Clients in Federated Learning with End-to-end Label Correction](http://arxiv.org/abs/2408.04301)

**連合学習におけるノイズの多いクライアントへの対処とエンドツーエンドのラベル補正**

Xuefeng Jiang, Sheng Sun, Jia Li, Jingjing Xue, Runhan Li, Zhiyuan Wu, Gang Xu, Yuwei Wang, Min Liu

- 連合学習はプライバシー保護をしつつ多様なアプリケーションで成功しているが、クライアントデータのラベルノイズが問題
- ラベルノイズの多いクライアントが多くの誤情報を含むため、パフォーマンス低下の主因となる
- 提案するFedELCは2段階のフレームワークで、第一段階でノイズの多いクライアントを検出し、第二段階でラベルを補正する
- 16の関連手法を実装し、5つのデータセットで評価を行った結果、提案手法が優れたパフォーマンスを示した

ノイズの多いデータが問題なんて、想像してなかった！FedELCのおかげでデータの質がグッと上がってすごい。未来の連合学習がもっと進化しそうで楽しみ！

**Comment:** To appear in ACM CIKM'24 full research paper track

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-08 08:35

- - -

### [DC Algorithm for Estimation of Sparse Gaussian Graphical Models](http://arxiv.org/abs/2408.04206)

**スパースガウシアン・グラフィカルモデルの推定のためのDCアルゴリズム**

Tomokaze Shiratori, Yuichi Takano

- ガウシアン・グラフィカルモデルのスパース推定は、多数の観測変数関係を解釈しやすくする技術
- 既存手法の多くは$\ell_0$ノルムを凸関数で近似し、直接扱うことに課題
- 本研究では$\ell_0$ノルムを直接用いて、DCアルゴリズム(DCA)で解決する手法を提案
- 合成データでの実験結果から、既存手法と同等またはそれ以上の性能を示し、特に真のエッジ選択に有利

DCAを使って直接的なアプローチを取るところがすごく革新的だね！モデルのエッジ選択が正確になるなら実用性も高そう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-08 04:05

- - -

### [Trustworthy Semantic-Enabled 6G Communication: A Task-oriented and Privacy-preserving Perspective](http://arxiv.org/abs/2408.04188)

**信頼できるセマンティック対応6G通信：タスク指向およびプライバシー保護の視点**

Shuaishuai Guo, Anbang Zhang, Yanhu Wang, Chenyuan Feng, Tony Q. S. Quek

- 信頼できるタスク指向セマンティック通信（ToSC）は、6Gで重要な情報のみを伝達する新しいアプローチ
- ToSCは効率的だが、送信されたデータから元データが再構成されるプライバシーの懸念がある
- DeepJSCCに基づくプライバシー保護策を解析、差分プライバシーや暗号化などの特徴摂動方法を比較
- 説明可能な学習アルゴリズムの統合が、新たな6G時代のプライバシー基準を設定することを強調

6G時代の通信がどんどん進化していくなんてワクワクするね！プライバシーもちゃんと守られるようになったら安心だな。



**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.SP, cs.SY, eess.SY, **投稿日時:** 2024-08-08 03:16

- - -

### [Active Inference in Contextual Multi-Armed Bandits for Autonomous Robotic Exploration](http://arxiv.org/abs/2408.04119)

**文脈付き多腕バンディットにおける能動的推論による自律ロボット探査**

Shohei Wakayama, Alberto Candela, Paul Hayne, Nisar Ahmed

- 不確実な環境で複数の選択肢から最適なデータ収集オプションの自律的選択は難しい
- 能動的推論は探索と利用のバランスを取るための期待自由エネルギー目的関数を使用
- 現実的なシナリオで能動的推論を適用し、鉱物学的調査サイト選定問題をシミュレーション
- 能動的推論は、標準バンディット手法よりも少ない反復回数で成果を上げ、専門家の好みの変動に対応可能

能動的推論ってすごいよね！未来のロボットがどんどん賢くなって、自分で考えて行動するんだね。今後の技術の進展が楽しみだなって思う。

**Comment:** 10 pages, 12 figures, submitted to IEEE Transactions on Robotics

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-08-07 23:00
