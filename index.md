---
layout: single
title: トップページ
permalink: /
author_profile: true
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

To be written.

## 最新更新分

更新: 2024-05-08T04:20:03.995223

- - -

### [Comparing Ways of Obtaining Candidate Orderings from Approval Ballots](http://arxiv.org/abs/2405.04525)

**承認投票から候補者の順序付けを得る方法の比較**

Théo Delemazure, Chris Dong, Dominik Peters, Magdaléna Tydrichová

- 承認投票を用いた政治選挙では、候補者が隣接して承認されるような左右のイデオロギー軸を設定することが有効
- 理想的な軸の設定は通常不可能であり、最も理想に近い軸を選択する必要がある
- 本論文では、社会選択のアプローチを取り、5つの異なる軸選択規則を公理的に比較し、それらが満たす特性を研究
- フランスの選挙調査データ、米国最高裁判所の裁判官の投票データ、合成データを用いて各規則の振る舞いを分析

**Comment:** 43 pages including appendix, accepted to IJCAI 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.GT, **投稿日時:** 2024-05-07 17:57

- - -

### [Large-Scale MPC: Scaling Private Iris Code Uniqueness Checks to Millions of Users](http://arxiv.org/abs/2405.04463)

**大規模秘密計算: 数百万ユーザーへのプライベート虹彩コード一意性チェックのスケーリング**

Remco Bloemen, Daniel Kales, Philipp Sippl, Roman Walch

- 秘密計算(MPC)を用いて虹彩コードがデータベース内のものと一致するかを確認しながらプライバシーを保護
- 世界IDや赤十字会の援助分配などの実用システムの高いパフォーマンス要求に対応する新プロトコルを提案
- 最新のプロトコルでは、1秒間に100万以上の虹彩コード比較が可能であり、プライバシーを保護しつつも高速に処理
- GPU加速を利用することで、従来のマルチスレッドCPU実装よりも38倍以上の高速化を実現



**トピック:** [秘密計算](mpc), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-07 16:29

- - -

### [Enhancing Scalability of Metric Differential Privacy via Secret Dataset Partitioning and Benders Decomposition](http://arxiv.org/abs/2405.04344)

**指標差分プライバシーのスケーラビリティ向上に向けた秘密データセットのパーティショニングとベンダーズ分解の活用**

Chenxi Qiu

- 指標差分プライバシー（mDP）は、一般的なメトリック空間で表現される秘密データ（テキストデータやジオロケーションデータなど）の保護を目的として拡張された
- 非効率な線形プログラミング問題を解決するため、オリジナルの秘密データセットを複数のサブセットに分割
- ベンダーズ分解を用いて、マスタープログラムとサブプロブレムを組み合わせることでパーティション問題を再構成し解決
- 実験結果は、道路ネットワーク上のジオロケーションデータやテキストデータ、合成データを用いて、提案メカニズムの優れたスケーラビリティと効率性を示した

**Comment:** To be published in IJCAI 2024

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.AI, cs.CR, **投稿日時:** 2024-05-07 14:19

- - -

### [Federated Learning for Cooperative Inference Systems: The Case of Early Exit Networks](http://arxiv.org/abs/2405.04249)

**連合学習を用いた協調推論システム: 早期終了ネットワークの事例**

Caelin Kaplan, Tareq Si Salem, Angelo Rodio, Chuan Xu, Giovanni Neglia

- IoT技術の進展により、センサーやスマートフォンなどの端末がAIモデルをローカルに装備し始めており、通信コストやレイテンシを削減
- より小さなモデルは、通常、エッジサーバーやクラウド内の洗練されたモデルに比べて性能が劣るため、協調推論システム（CIS）がこの問題に対処
- 連合学習（FL）は、クライアント間での異なる応答速度を考慮しながらCIS内のモデルを共同でトレーニングするために利用される
- 提案する新たなFLアプローチは理論的保証を提供し、特にクライアント間での推論リクエスト率やデータ利用可能性が不均等な状況で既存の最先端アルゴリズムを超越



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-07 12:07

- - -

### [FedStale: leveraging stale client updates in federated learning](http://arxiv.org/abs/2405.04171)

**FedStale: 連合学習における遅延クライアント更新の活用**

Angelo Rodio, Giovanni Neglia

- 連合学習ではデータの偏りと部分的なクライアント参加が問題となる
- 新アルゴリズムFedStaleは、参加クライアントの「新しい」更新と非参加クライアントの「古い」更新の凸結合を用いてグローバルモデルを更新
- FedStaleは、参加の偏りが大きいクライアントほど収束エラーに影響することを示し、古い更新の効用について実用的なガイドラインを提供
- 実験により、FedStaleはFedAvgやFedVARPよりも多くの設定で性能が向上することが確認された

**Comment:** 33 pages, 5 figures, preprint

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-07 10:11

- - -

### [Bridging the Synthetic-to-Authentic Gap: Distortion-Guided Unsupervised Domain Adaptation for Blind Image Quality Assessment](http://arxiv.org/abs/2405.04167)

**合成データから本物の画像へのギャップを埋める：歪みガイドによる盲目画質評価のための教師なしドメイン適応**

Aobo Li, Jinjian Wu, Yongxu Liu, Leida Li

- 盲目的画質評価の注釈付けは労力がかかり時間も消費する
- 合成データでのトレーニングは有用だが、ドメイン間のギャップにより一般化能力が低下することが問題
- 新たに提案された教師なしドメイン適応フレームワーク「DGQA」は、歪み知識を用いた適応多道選択を活用してソースとターゲット間のデータ分布の一致を図る
- DGQAは既存のモデルベースBIQA手法と組み合わせ可能で、少ない訓練データでの性能向上に寄与する

**Comment:** Accepted by CVPR2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, eess.IV, **投稿日時:** 2024-05-07 10:07

- - -

### [pFedLVM: A Large Vision Model (LVM)-Driven and Latent Feature-Based Personalized Federated Learning Framework in Autonomous Driving](http://arxiv.org/abs/2405.04146)

**pFedLVM: 自動運転における大規模視覚モデルと潜在特徴ベースのパーソナライズド連合学習フレームワーク**

Wei-Bin Kou, Qingfeng Lin, Ming Tang, Sheng Xu, Rongguang Ye, Yang Leng, Shuai Wang, Zhenyu Chen, Guangxu Zhu, Yik-Chung Wu

- 自動運転の深層学習モデルは分散データと常に変化する環境により、一般化が難しい問題を示している
- pFedLVMは大規模視覚モデル（LVM）を中央サーバーでのみ実装し、個々の車両への計算負担を軽減
- 車両とサーバー間のやり取りはLVMのパラメータではなく、学習した特徴を交換することで通信オーバーヘッドを大幅に削減
- 共通特徴と個々の車両の特性を利用するパーソナライズド学習メカニズムにより、一般的なグローバルモデルよりも優れた性能を実現

**Comment:** This paper was submitted to IEEE Transactions on Mobile Computing   (TMC) on Apr. 6th, 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, **投稿日時:** 2024-05-07 09:25

- - -

### [Ranking-based Client Selection with Imitation Learning for Efficient Federated Learning](http://arxiv.org/abs/2405.04122)

**連合学習におけるランキングベースクライアント選択と模倣学習による効率的なクライアント選択**

Chunlin Tian, Zhan Shi, Xinpeng Qin, Li Li, Chengzhong Xu

- 連合学習において、複数のデバイスがデータのプライバシーを保持しながら共有モデルを共同で訓練する
- 新しいデバイス選択ソリューション「FedRank」は、模倣学習を用いて事前訓練され、ランキングベースのアプローチを採用している
- FedRankはデータとシステムの異質性を考慮し、適切なクライアントを適応的かつ効率的に選択する
- 実験結果によれば、FedRankはモデルの精度を5.2%から56.9%向上させ、訓練の収束速度を最大2.01倍速め、エネルギー消費を最大40.1%削減する

**Comment:** Accepted by ICML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-07 08:44

- - -

### [A2-DIDM: Privacy-preserving Accumulator-enabled Auditing for Distributed Identity of DNN Model](http://arxiv.org/abs/2405.04108)

**A2-DIDM: 分散DNNモデルのためのプライバシー保護型積算器搭載監査技術**

Tianxiu Xie, Keke Gai, Jing Yu, Liehuang Zhu, Kim-Kwang Raymond Choo

- DNNモデルの取引における不正利用や複製問題への対策として、DNNモデルの分散アイデンティティの監査システムA2-DIDMを提案
- ブロックチェーンとゼロ知識証明技術を利用し、データのプライバシー保護と軽量な所有権検証を実現
- モデル重みのチェックポイントと対応するゼロ知識証明を配置してアイデンティティレコードを生成し、モデルの状態変化も捉える
- 重みチェックポイントの一意性を保持し、監査の正確性やDNN訓練プロセスの計算整合性を保証



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-05-07 08:24

- - -

### [Scalable Vertical Federated Learning via Data Augmentation and Amortized Inference](http://arxiv.org/abs/2405.04043)

**スケーラブルな縦型連合学習のためのデータ拡張とコスト分散推測**

Conor Hassan, Matthew Sutton, Antonietta Mira, Kerrie Mengersen

- 縦型連合学習（VFL）のために、バイエスモデルを適用する初の包括的フレームワークを提案
- データ拡張技術を利用してVFL問題を既存のバイエシアン連合学習アルゴリズムに適合させる新しい手法を提案
- 観測数とクライアント数に依存しないスケーラビリティを実現するために、分割されたアモルタイズド変分近似を開発
- ロジスティック回帰、多層回帰、階層的ベイジアン分割ニューラルネットモデルに数値実験を通じてフレームワークの有効性を示す

**Comment:** 30 pages, 5 figures, 3 tables

**トピック:** [連合学習](fl), **カテゴリ:** stat.CO, cs.LG, stat.ME, stat.ML, **投稿日時:** 2024-05-07 06:29

- - -

### [Enabling Privacy-Preserving and Publicly Auditable Federated Learning](http://arxiv.org/abs/2405.04029)

**プライバシー保護と公開監査が可能な連合学習を実現**

Huang Zeng, Anjia Yang, Jian Weng, Min-Rong Chen, Fengjun Xiao, Yi Liu, Ye Yao

- 連合学習での三つの主要課題を同時に解決する手法を提案：第三者による監査の公開性、悪意のある参加者の影響回避、プライベート勾配とモデルの漏洩防止
- 悪意のある参加者が誤った方向の勾配をアップロードするのを防ぐための頑強な集約アルゴリズムを設計
- ゼロ共有とブロックチェーン技術と組み合わせ、訓練プロセスを公開して任意の第三者が正確性を検証可能にするランダムベクトル生成アルゴリズムを設計
- 実験結果として、提案プロトコルのモデルは元の連合学習アプローチと同等の精度を持ちつつ、セキュリティの利点を保持していることを確認

**Comment:** ICC 2024 - 2024 IEEE International Conference on Communications   Conference Program

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, C.2.2; C.2.4; E.3, **投稿日時:** 2024-05-07 06:03

- - -

### [Research on financial fraud algorithm based on federal learning and big data technology](http://arxiv.org/abs/2405.03992)

**連合学習と大データ技術を基にした金融詐欺アルゴリズムに関する研究**

Xinye Sha

- 金融業務のデジタル化が進むにつれ、金融詐欺はより複雑で隠蔽されがちな特性を呈している
- 連合学習は、データプライバシーを守りつつ、複数の参加者が協力してモデルを学習させることが可能
- 設計された連合学習アーキテクチャは、ローカルでモデルを訓練し、生データではなくモデルパラメータのみを交換することでプライバシーを保護
- 実験結果は、連合学習を用いた金融詐欺検出アルゴリズムが、データのプライバシー違反の可能性を大幅に削減しつつ、高い検出精度を損なわないことを示している



**トピック:** [連合学習](fl), **カテゴリ:** cs.CE, **投稿日時:** 2024-05-07 04:11

- - -

### [IPFed: Identity protected federated learning for user authentication](http://arxiv.org/abs/2405.03955)

**IPFed: ユーザ認証のための身元保護連合学習**

Yosuke Kaga, Yusei Suzuki, Kenta Takahashi

- 既存の方法ではプライバシー保護と高精度の達成が困難であることを示している
- クラス埋め込みのためのランダム射影を使用したプライバシー保護連合学習であるIPFedを提案
- IPFedが最先端の方法と同等の学習を実現できることを証明
- 顔画像データセットにおける実験で、IPFedは最先端の精度を保ちつつ個人データのプライバシー保護が可能であることを示している



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-05-07 02:29

- - -

### [FedSC: Provable Federated Self-supervised Learning with Spectral Contrastive Objective over Non-i.i.d. Data](http://arxiv.org/abs/2405.03949)

**FedSC: 非独立同分布データ上でのスペクトルコントラスティブ目的を用いた証明可能な連合自己教師あり学習**

Shusen Jing, Anlan Yu, Shuai Zhang, Songyang Zhang

- 連合自己教師あり学習(FedSSL)では、局所的自己教師あり学習の目標と全体目標が一致しない問題が存在
- 通常の連合学習手法であるFedAvgはFedSSLの全体目標を効率的に最小化できず、特に非独立同分布データでは性能が劣る
- 提案されたFedSCアルゴリズムは、クライアント間でのデータ表現の相関行列とモデルの重みを共有することでデータサンプルの比較を実現し、データ表現の質を向上
- 差分プライバシー(DP)を適用し、相関行列の共有による追加的なプライバシーリークを制御



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-05-07 02:12

- - -

### [Unified Locational Differential Privacy Framework](http://arxiv.org/abs/2405.03903)

**統一的位置情報差分プライバシーフレームワーク**

Aman Priyanshu, Yash Maurya, Suriya Ganesh, Vy Tran

- 地理的領域における統計データの集約は、収入分析、選挙結果、疾病拡散など多くのアプリケーションにとって重要
- 機密性が高いデータのため、個人を保護するための強力なプライバシー保護が必要
- 当研究では、様々なデータタイプ（1ビットエンコーディング、ブーリアン、浮動小数点数、整数配列）のプライベート集計を可能にする位置情報差分プライバシーフレームワークを提案
- ランダム応答、指数メカニズム、ガウスメカニズムなどのローカルDPメカニズムを採用し、地理的データ分析を可能にする正式なDP保証を提供することを示す

**Comment:** 10 pages, 7 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.AI, cs.CY, **投稿日時:** 2024-05-06 23:33

- - -

### [Thoughtful Things: Building Human-Centric Smart Devices with Small Language Models](http://arxiv.org/abs/2405.03821)

**スマートデバイスを人間中心で設計する: 小型言語モデルを用いた開発**

Evan King, Haoxiang Yu, Sahil Vartak, Jenna Jacob, Sangsu Lee, Christine Julien

- スマートデバイスの操作が複雑化する中で、自然言語を介した簡易操作を可能とする新たな方法を提案
- 命令を自然言語で受け付け、デバイスの動作を理解・説明する能力を持つ小型の言語モデルをデバイスに組み込む
- 提案されたフレームワークは、形式的モデリング、自動トレーニングデータ合成、生成言語モデルを利用し、ラベル付きデータを必要とせず、クラウド非依存のオンデバイス展開を実現
- 実際のハードウェア上でランプとサーモスタットの二つのデバイスを実装し、それらの実用的なパフォーマンスを評価

**Comment:** 24 pages (3 pages of references)

**トピック:** [合成データ](sd), **カテゴリ:** cs.HC, cs.AI, cs.SE, **投稿日時:** 2024-05-06 20:04

- - -

### [Interpretable Data Fusion for Distributed Learning: A Representative Approach via Gradient Matching](http://arxiv.org/abs/2405.03782)

**分散学習における解釈可能なデータ統合：勾配マッチングを用いた代表的アプローチ**

Mengchen Fan, Baocheng Geng, Keren Li, Xueqian Wang, Pramod K. Varshney

- 複数の生データ点から仮想表現へと変換する新しい代表ベースの分散学習手法を紹介
- 伝統的な連合学習と比べて、機械学習プロセスをアクセスしやすく、理解しやすくする
- プライバシー保護と通信効率を維持しつつ、生データを使用するモデルと同等の訓練性能を達成
- 複雑なモデルや多数のクライアントを持つシナリオにおいて、伝統的な連合学習よりも精度と収束速度で優れることをシミュレーション結果が示している



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.HC, **投稿日時:** 2024-05-06 18:21

- - -

### [Secure Inference for Vertically Partitioned Data Using Multiparty Homomorphic Encryption](http://arxiv.org/abs/2405.03775)

**垂直分割データに対する多方準同型暗号を使用した安全推論**

Shuangyi Chen, Yue Ju, Zhongwen Zhu, Ashish Khisti

- 複数のクライアントノードと単一のサーバーノードを含む分散環境での安全な推論プロトコルを提案
- クライアントノードはデータベクトルの一部を暗号化し、その暗号文をサーバーノードに送信
- サーバーノードは、受け取った暗号文を集めて暗号化された領域で推論を実施
- 提案プロトコルは多方準同型暗号（MPHE）を使用し、サーバーによる完全なデータの暗号文の形成を可能にするパッキングスキームを採用



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-06 18:17
