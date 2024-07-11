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

更新: 2024-07-11T04:20:46.096740

- - -

### [Stabilized Proximal-Point Methods for Federated Optimization](http://arxiv.org/abs/2407.07084)

**連合最適化のための安定化近傍点法**

Xiaowen Jiang, Anton Rodomanov, Sebastian U. Stich

- 連合学習環境では通信制約が重要な課題
- DANEは最良の通信複雑性を達成する分散近傍点アルゴリズム
- 新しい分散アルゴリズムS-DANEを提案し、局所計算効率を向上
- S-DANEの加速法は既存手法中で最良の通信複雑性を達成

新しいS-DANE、めっちゃ気になる！これで通信量問題が解決されると、連合学習がもっと実用的になっちゃうよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, math.OC, **投稿日時:** 2024-07-09 17:56

- - -

### [Explainable Hyperdimensional Computing for Balancing Privacy and Transparency in Additive Manufacturing Monitoring](http://arxiv.org/abs/2407.07066)

**積層造形モニタリングにおけるプライバシーと透明性のバランスのための説明可能な高次元コンピューティング**

Fardin Jalil Piran, Prathyush P. Poduval, Hamza Errahmouni Barkam, Mohsen Imani, Farhad Imani

- 積層造形プロセスにおけるデータ漏洩やセンサーデータの妥協、モデル逆向き攻撃などのプライバシー問題
- 差分プライバシー（DP）モデルがデータの痕跡を隠すが、ノイズ導入によるモデル精度の影響予測が困難
- この研究は、DP-HDフレームワークを提案し、ノイズの影響を予測しつつ敏感データを保護
- 実験結果では、DP-HDが高い運用効率と予測精度により、現行のMLモデルを上回る

「DP-HDフレームワークはすごく有望だね！これならプライバシーを守りながら精度も高いままで済むから、未来の製造業にはぴったりかも！」

**Comment:** 24 pages, 13 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.CV, **投稿日時:** 2024-07-09 17:42

- - -

### [A Differentially Private Blockchain-Based Approach for Vertical Federated Learning](http://arxiv.org/abs/2407.07054)

**縦型連合学習のための差分プライバシー対応ブロックチェーンアプローチ**

Linh Tran, Sanjay Chari, Md. Saikat Islam Khan, Aaron Zachariah, Stacy Patterson, Oshani Seneviratne

- DP-BBVFLアルゴリズムは、分散型アプリケーションのための検証可能性とプライバシー保証を提供
- スマートコントラクトを用いてクライアントの特徴表現（埋め込み）を透明に集約
- ブロックチェーン上に保存された埋め込みデータに対してローカル差分プライバシーを適用し、元データを保護
- 医療データでの実験は、高い精度を達成しつつ、オンチェーン集約によるトレーニング時間のトレードオフを示す

差分プライバシーとブロックチェーンの組み合わせってすごく新しい発想！これからいろんな分野で応用されそうでワクワクするね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.ET, cs.LG, **投稿日時:** 2024-07-09 17:20

- - -

### [Multimodal Self-Instruct: Synthetic Abstract Image and Visual Reasoning Instruction Using Language Model](http://arxiv.org/abs/2407.07053)

**マルチモーダルセルフインストラクト: 合成抽象画像と視覚推論のための言語モデルによる指示**

Wenqi Zhang, Zhenglin Cheng, Yuanyu He, Mengna Wang, Yongliang Shen, Zeqi Tan, Guiyang Hou, Mingqian He, Yanna Ma, Weiming Lu, Yueting Zhuang

- 現在の大型マルチモーダルモデル（LMMs）は自然なシーンやポートレートの理解はできるが、抽象画像や視覚推論はまだ基本的なレベル
- 時間の読み取り、フローチャートの理解、地図のルート計画などの日常タスクに苦戦
- マルチモーダルセルフインストラクトを設計し、大規模言語モデルとそのコード能力を利用して、8つの視覚シナリオで指示を合成
- 合成データを用いたLMMの微調整結果、チャート理解と地図ナビゲーションのパフォーマンスが向上

視覚推論をもっと進化させるために、こんなデータを駆使するって面白いね！これからはもっと複雑なタスクもどんどんできちゃうかも。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-09 17:18

- - -

### [Bayesian Federated Learning with Hamiltonian Monte Carlo: Algorithm and Theory](http://arxiv.org/abs/2407.06935)

**ハミルトニアンモンテカルロを用いたベイジアン連合学習：アルゴリズムと理論**

Jiajun Liang, Qian Zhang, Wei Deng, Qifan Song, Guang Lin

- FA-HMCアルゴリズムを提案し、パラメータ推定と不確実性の定量化を実現
- 非独立同分布データセット上での収束保証を確立
- パラメータ空間の次元、勾配のノイズ、通信頻度の影響を解析
- FA-LDアルゴリズムよりも優れた性能を実証

ハミルトニアンモンテカルロ使ってるのが面白そう！これで連合学習の精度もっと上がりそうだね、未来のアプリとかに期待しちゃう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.CO, stat.ML, **投稿日時:** 2024-07-09 15:10

- - -

### [A Simple, Nearly-Optimal Algorithm for Differentially Private All-Pairs Shortest Distances](http://arxiv.org/abs/2407.06913)

**差分プライバシー全点間最短距離のためのシンプルでほぼ最適なアルゴリズム**

Jesse Campbell, Chunjiang Zhu

- 無向重み付きグラフの全点間最短距離を差分プライバシーで推定する問題を取り扱う
- 提案するアルゴリズムは従来のエラー率を大幅に改善し、ほぼ最適な精度を実現する
- 乗法近似を許容する場合、追加エラーを減少させる二つの構築法を提案
- アルゴリズムは単純であり、グラフをスパニングツリーに分解し、ツリー内の距離をプライベートに公開する手法を利用する

このアルゴリズム、プライバシーを保ちながら距離を計算できるとかすごくない？テクノロジーってどんどん進化しててびっくりしちゃうね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, **投稿日時:** 2024-07-09 14:48

- - -

### [Differentially Private Multiway and -Cut](http://arxiv.org/abs/2407.06911)

**差分プライバシーによる多方面および$k$カット**

Rishi Chandra, Michael Dinitz, Chenglin Fan, Zongrui Zou

- グラフのカット問題に対する差分プライバシーの課題に取り組んでいる
- 多方面カット問題に対し、非プライベートアルゴリズムに匹敵する性能のプライベートアルゴリズムを提案
- 重み付きグラフにおいて定数$k$に対して最適に近いアルゴリズムを実現
- 最小$k$カット問題では、既知の近似カット数を活用し、固定プライバシーパラメータで最適な加法誤差を達成

最適化ってほんっとうに面白いね。これを使ってプライバシー保護しながらいろんな問題解決できるのがすごいって思うの！

**Comment:** 38 pages

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, **投稿日時:** 2024-07-09 14:46

- - -

### [Trust and Resilience in Federated Learning Through Smart Contracts Enabled Decentralized Systems](http://arxiv.org/abs/2407.06862)

**スマートコントラクトを活用した分散システムによる連合学習の信頼性とレジリエンス**

Lorenzo Cassano, Jacopo D'Abramo, Siraj Munir, Stefano Ferretti

- 分散型アーキテクチャを使用して、連合学習(FL)システムの信頼性と信頼性を向上
- FLのコラボレーターが暗号化されたモデルパラメータをIPFSにアップロードし、スマートコントラクトで行動を追跡
- パラメータ更新フェーズをスマートコントラクトで効率的に管理し、データセキュリティを強化
- クラシックな平均化方式と連合プロキシマル集約の2つの方法を使った重み付け集約の実験で提案の実現可能性を確認

スマートコントラクトを実際にFLに活用して、システム全体のセキュリティを強化するのってすごいね！学べば学ぶほど面白くなりそう♪

**Comment:** TRUSTCHAIN workshop

**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, cs.LG, **投稿日時:** 2024-07-09 13:50

- - -

### [Threats and Defenses in Federated Learning Life Cycle: A Comprehensive Survey and Challenges](http://arxiv.org/abs/2407.06754)

**連合学習ライフサイクルにおける脅威と防御: 包括的調査と課題**

Yanli Li, Jifei Hu, Zhongliang Guo, Nan Yang, Huaming Chen, Dong Yuan, Weiping Ding

- 連合学習（FL）は、分散性が理由で多様な攻撃に脆弱
- 脅威はモデルの有用性や参加者のプライバシーに直接/間接的な影響を与える
- 防御フレームワークは特定の状況で効果を発揮し、脅威と防御の関係を分析
- 現在の研究ボトルネックと今後の研究方向をまとめ、FLコミュニティに貢献

連合学習でこんなに色々なリスクがあるなんて驚き！防御方法の比較が面白そうだし、未来の課題を解決するヒントにもなりそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.AI, **投稿日時:** 2024-07-09 11:05

- - -

### [Enhanced Model Robustness to Input Corruptions by Per-corruption Adaptation of Normalization Statistics](http://arxiv.org/abs/2407.06450)

**入力破損に対するモデルのロバスト性を向上させるための個別適応型正規化統計**

Elena Camuffo, Umberto Michieli, Simone Milani, Jijoong Moon, Mete Ozay

- ロボット技術における信頼性の高いビジョンシステムの開発が課題
- 現在のモデルロバスト性向上策は一般的なデータ拡張や高コストなテスト時適応が主
- 提案したPANは、破損タイプの特定、正規化層の動的調整、リアルタイムでの統計更新を実現
- PANは、複数のロボットビジョンタスクでモデル精度を向上し、20-30%の性能向上を達成

この論文、ロボットビジョンの未来を切り拓きそうでワクワクするね！特に悪条件下での性能がこれだけ上がるのは、本当に実用的で感激！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-08 23:20

- - -

### [When in Doubt, Cascade: Towards Building Efficient and Capable Guardrails](http://arxiv.org/abs/2407.06323)

**迷ったときはカスケード：効率的かつ有能なガードレールの構築に向けて**

Manish Nagireddy, Inkit Padhi, Soumya Ghosh, Prasanna Sattigeri

- 大規模言語モデル（LLM）は下流タスクで高い性能を発揮するが、有害やバイアスのかかったテキスト生成の問題がある
- ソーシャルバイアス検出器の開発から得た知見に基づき、使用と言及の区別が主な性能低下要因であることを発見
- タクソノミー駆動の指示を利用して合成データ生成パイプラインを構築し、標的データとラベル付きデータを作成
- 30万以上のユニークな対照サンプルを生成し、公開データセットを使って競争力のある性能を低コストで実現

自分たちの方法が低コストで効率的に性能向上するのってスゴイ！自動的にデータを作成してテストするアイデア、マジで最先端ぽいなと思った。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-07-08 18:39

- - -

### [FairDiff: Fair Segmentation with Point-Image Diffusion](http://arxiv.org/abs/2407.06250)

**FairDiff: Point-Image拡散による公正なセグメンテーション**

Wenyi Li, Haoran Xu, Guiyu Zhang, Huan-ang Gao, Mingju Gao, Mengyu Wang, Hao Zhao

- 医用画像解析における公平性のため、合成画像を用いてデータバランスを強化
- 従来の方法はペアラベルが欠如または境界の精度管理が困難
- 3つのネットワークを共同で最適化し、経験的リスク最小化と公平性最大化を目指す
- 3Dポイントクラウドを活用し、最新技術を上回るSLO眼底画像の合成に成功

実際にどんな風に合成が行われるのか気になるね！公平性って今後重要になってくるし、目の病気の診断がもっと公平になるなんて素敵すぎ！

**Comment:** Accepted to MICCAI 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-08 17:59

- - -

### [Synthetic data: How could it be used for infectious disease research?](http://arxiv.org/abs/2407.06211)

**合成データ: それは感染症研究にどのように利用できるか?**

Styliani-Christina Fragkouli, Dhwani Solanki, Leyla J Castro, Fotis E Psomopoulos, Núria Queralt-Rosinach, Davide Cirillo, Lisa C Crossman

- 合成データはヘルスケア関連の用途で機械学習に利用可能
- 深層偽造やフェイクニュースなど、生成AIの潜在的な悪用が懸念される
- 合成データはデータプライバシー、研究、バイアス軽減で大きな利点を提供
- 最新の生成AI技術により、感染症研究の進展に重要な役割を果たせると提案

感染症研究に合成データを活用するなんて、今後どんな新発見があるかワクワクするよね！AIが病気の予測や治療法の開発に役立つなんて、未来がすごく楽しみ。



**トピック:** [合成データ](sd), **カテゴリ:** q-bio.OT, cs.CY, cs.LG, **投稿日時:** 2024-07-03 17:13
