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

更新: 2024-05-05T04:19:01.611705

- - -

### [D2PO: Discriminator-Guided DPO with Response Evaluation Models](http://arxiv.org/abs/2405.01511)

**D2PO: DiscriminatorによるDPOと応答評価モデル**

Prasann Singhal, Nathan Lambert, Scott Niekum, Tanya Goyal, Greg Durrett

- D2POは、学習中に継続的に好みのデータを収集するオンライン設定にて、従来のDPOを拡張した新しいアプローチ
- D2POは、ポリシーだけでなく、合成データをさらにラベル付けするための差別的応答評価モデルの訓練にも好みのデータを使用
- リアルなチャット環境を含む様々なタスクにわたってD2POを検討し、同じデータ予算での出力品質がDPOよりも高く、効率も向上
- 効果的なシルバーラベリングの条件を明らかにし、ポリシーモデルとは別のディスクリミネーターを保持することが効果的

**Comment:** 20 pages, 12 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-05-02 17:44

- - -

### [Navigating Heterogeneity and Privacy in One-Shot Federated Learning with Diffusion Models](http://arxiv.org/abs/2405.01494)

**一発合成学習における異質性とプライバシーの調査：拡散モデルの使用**

Matias Mendieta, Guangyu Sun, Chen Chen

- 一発合成学習は通信ラウンドを削減し、効率を向上させ、盗聴攻撃からのセキュリティを強化するが、データの異質性の問題が残る
- 拡散モデルが一発合成学習においてデータ異質性に対処し、全体のパフォーマンスを向上させるのに有効であることを示す
- FedDiffという拡散モデルアプローチを差分プライバシーの下で他の一発合成学習手法と比較し、その有用性を調査
- 差分プライバシー設定下で生成されたサンプルの品質を改善するために、実際的なフーリエ振幅フィルタリング法を提案し、グローバルモデルトレーニングでの生成データの効果を向上



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CV, cs.CR, cs.LG, **投稿日時:** 2024-05-02 17:26

- - -

### [Uncertainty for Active Learning on Graphs](http://arxiv.org/abs/2405.01462)

**グラフ上のアクティブラーニングにおける不確実性**

Dominik Fuchsgruber, Tom Wollschläger, Bertrand Charpentier, Antonio Oroz, Stephan Günnemann

- アクティブラーニング戦略の一つである不確実性サンプリングは、データ点の不確実性が最も高いもののラベルを反復的に取得することで機械学習モデルのデータ効率を向上させることを目指している
- この戦略は独立データに対して有効であるが、グラフに対する適用可能性は十分に探究されていない
- 論文ではノード分類のための不確実性サンプリングに関する最初の包括的研究を提案し、異なるアクティブラーニング戦略と比べてその性能差を明らかにした
- 実データと合成データにおいて、他の不確実性推定手法よりも優れた結果を示す近似的アプローチを設計し、実証した



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-02 16:50

- - -

### [Privacy-Enhanced Database Synthesis for Benchmark Publishing](http://arxiv.org/abs/2405.01312)

**プライバシー保護付きデータベース合成によるベンチマークパブリッシング**

Yongrui Zhong, Yunqing Ge, Jianbin Qin, Shuyuan Zheng, Bo Tang, Yu-Xuan Qiu, Rui Mao, Ye Yuan, Makoto Onizuka, Chuan Xiao

- 実際のユーザーデータを取り入れたデータベース作成により、ビジネス環境をより正確に反映させる動きが増えている
- プライバシーの問題から直接データの共有は避けられがちであり、プライバシー保護を優先した合成データベースの作成が重要視されている
- PrivBenchという新しい合成フレームワークを導入し、プライバシーを保持しつつ高品質なデータ生成を支援する
- PrivBenchは差分プライバシーを利用し、クエリ性能がオリジナルのデータに近いプライバシー保護データベースを生成することに成功している



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DB, cs.CR, **投稿日時:** 2024-05-02 14:20

- - -

### [Gradient-Congruity Guided Federated Sparse Training](http://arxiv.org/abs/2405.01189)

**連合学習をガイドする勾配合同性によるスパース訓練**

Chris Xing Tian, Yibing Liu, Haoliang Li, Ray C. C. Cheung, Shiqi Wang

- 連合学習(FL)は、データプライバシーを保持しつつエッジデバイス上でAIと機械学習モデルのデプロイを促進するが、計算と通信コストが高い問題がある
- 異種データや分布外データによって一般化性能が低下する問題を指摘
- 勾配合同性に基づく動的なスパース訓練を連合学習フレームワークに統合してこれらの問題に対処する新しい手法、FedSGCを提案
- FedSGCは計算と通信のオーバーヘッドを大幅に削減し、同時に一般化能力を向上させることが示された



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-02 11:29

- - -

### [Why Tabular Foundation Models Should Be a Research Priority](http://arxiv.org/abs/2405.01147)

**タブラーファンデーションモデルを研究の優先事項にすべき理由**

Boris van Breugel, Mihaela van der Schaar

- 近年のテキストや画像のファンデーションモデルは非常に印象的であり、研究リソースの増大を引き寄せている
- 本論文では、ML研究コミュニティの優先順位をタブラーデータへ僅かにシフトすることを目指している
- 多くの分野で主要なモダリティであるタブラーデータは、研究においてほとんど注意を払われず、規模とパワーで大きく遅れをとっている
- 大規模タブラーモデル(LTM)の開発を開始する時が来ており、これが科学とMLのタブラーデータの使用方法を革命的に変える可能性がある

**Comment:** Accepted at International Conference on Machine Learning (ICML 2024)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-02 10:05

- - -

### [Boosting Communication Efficiency of Federated Learning's Secure Aggregation](http://arxiv.org/abs/2405.01144)

**連合学習におけるセキュア集約の通信効率の向上**

Niousha Nazemi, Omid Tavallaie, Shuaijun Chen, Albert Y. Zomaya, Ralph Holz

- 連合学習（FL）は、クライアントデバイスがローカルでモデルを訓練し、サーバーがこれを集約してグローバルモデルを生成する分散型機械学習アプローチである
- FLは、サーバーが訓練されたモデルから機密クライアントデータを推測可能なモデル反転攻撃に対して脆弱
- グーグルの安全集約プロトコル（SecAgg）は通信と計算に多大なオーバーヘッドを要するものの、プライバシーを保護するためにクライアント毎に共有秘密と個別要素を用いて訓練モデルをマスキングする
- 新たに提案された通信効率の良い安全集約プロトコル（CESA）は、クライアントごとに2つの共有秘密を使用することでオーバーヘッドを大幅に削減し、SecAggと比較して通信コストを大幅に低下させる

**Comment:** 2 pages, 4 figures, The 54th Annual IEEE/IFIP International   Conference on Dependable Systems and Networks

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-02 10:00

- - -

### [Sharp Bounds for Sequential Federated Learning on Heterogeneous Data](http://arxiv.org/abs/2405.01142)

**異質データにおける逐次連合学習の鋭敏な境界**

Yipeng Li, Xinchen Lyu

- 異質データに対する逐次連合学習 (SFL) の収束理論が未整備であることに対処するため、上限と下限を含む厳密な収束保証を確立
- 強凸、一般凸、非凸目的関数に対して上限境界を導出し、強凸および一般凸目的関数については対応する下限も構築
- 異質度が比較的高い状況では、逐次連合学習が並列連合学習 (PFL) よりも優れていることを示す
- 二次関数と実データセットに関する実験結果が、直感に反する比較結果を検証

**Comment:** arXiv admin note: text overlap with arXiv:2311.03154

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-02 09:58

- - -

### [Federated Learning with Heterogeneous Data Handling for Robust Vehicular Object Detection](http://arxiv.org/abs/2405.01108)

**連合学習を用いた異種データ処理による堅牢な車両物体検出**

Ahmad Khalil, Tizian Dege, Pegah Golchin, Rostyslav Olshevskyi, Antonio Fernandez Anta, Tobias Meuser

- 連合学習（FL）は車両ネットワーク内でモデル訓練を効率的に行いながら生データの完全性を保持
- 新たな連合学習手法FedProx+LAは、FedProxとFedLAを基に車両向けのデータ異質性に対応
- 連続的なオンライン物体検出モデル訓練を通じて、FedProx+LAは従来手法に比べ優れた収束率を示す
- ラベル分布が非常に異質な場合にFedProx+LAは検出性能を大幅に向上させ、FedLAの性能も上回る



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-05-02 09:14

- - -

### [Poisoning Attacks on Federated Learning for Autonomous Driving](http://arxiv.org/abs/2405.01073)

**連合学習における自動運転用の毒入れ攻撃**

Sonakshi Garg, Hugo Jönsson, Gustav Kalander, Axel Nilsson, Bhhaanu Pirange, Viktor Valadi, Johan Östman

- 連合学習（FL）は自動運転内でモデルを共同で訓練しながらデータの秘密を保持する分散学習パラダイムである
- 本研究では自動運転に特化した2つの新規毒入れ攻撃、FLStealthとOff-Track Attack（OTA）を導入
- FLStealthはグローバルモデルの性能を低下させる目的の非対象攻撃で、OTAは特定のトリガーに反応してモデルの振る舞いを変える目的の対象攻撃
- 車両の軌道予測タスクに関する実験で攻撃の有効性を示し、OTAに対する一般的な防御戦略が不十分であることを強調

**Comment:** Accepted to SCAI2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, cs.CV, **投稿日時:** 2024-05-02 08:06

- - -

### [The Privacy Power of Correlated Noise in Decentralized Learning](http://arxiv.org/abs/2405.01031)

**分散学習における相関ノイズのプライバシー保護効果**

Youssef Allouah, Anastasia Koloskova, Aymane El Firdoussi, Martin Jaggi, Rachid Guerraoui

- 分散学習を用いることで中央集権を避けつつ、大量の分散データとリソースをスケーラブルに利用可能
- 分散SGDに差分プライバシーを統合した新型手法「Decor」を提案し、局所モデルの保護に相関ガウスノイズを注入
- Decorは任意の接続グラフに対して中心差分プライバシーの最適なプライバシーと効用のトレードオフに匹敵
- 通信対の秘密共有を前提とした新しいローカル差分プライバシーの緩和版（SecLDP）と、それに対応するプライバシー計算ツールを提案

**Comment:** Accepted as conference paper at ICML 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DC, math.OC, stat.ML, **投稿日時:** 2024-05-02 06:14

- - -

### [Robust Decentralized Learning with Local Updates and Gradient Tracking](http://arxiv.org/abs/2405.00965)

**ロバストな分散学習：ローカルアップデートと勾配追跡を利用**

Sajjad Ghiasvand, Amirhossein Reisizadeh, Mahnoosh Alizadeh, Ramtin Pedarsani

- 分散学習におけるデータの異質性と敵対的堅牢性の問題を取り扱う
- ローカルアップデートと勾配追跡の二つの重要なモジュールを使用する分散最小最適化法を提案
- 提案されたアルゴリズム「Dec-FedTrack」は非凸-強凹の最小最適化問題でも収束することを証明
- 理論的な結果を裏付ける数値実験も行われた



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-02 03:03

- - -

### [Recovering Labels from Local Updates in Federated Learning](http://arxiv.org/abs/2405.00955)

**連合学習におけるローカル更新からのラベル回復**

Huancheng Chen, Haris Vikalo

- 連合学習において、勾配反転攻撃がクライアントのデータ復元を試みる中で、モデル更新情報からラベル回復が鍵とされる
- RLU（Recovering Labels from Local Updates）方式は未訓練モデルに対して高い正確さを示し、現実的な環境でも効果を発揮
- RLUは、トレーニングデータのラベルと結果としての出力層の更新との間の相関関係分析を基に最小二乗問題を解いてラベルを推定する
- 複数のデータセットとアーキテクチャでの実験結果から、RLUは既存の方法よりも一貫して優れた性能を示し、勾配反転攻撃における画像再構成の質を向上させた



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-02 02:33

- - -

### [Quantum Federated Learning Experiments in the Cloud with Data Encoding](http://arxiv.org/abs/2405.00909)

**量子連合学習をクラウドで実験したデータエンコーディング**

Shiva Raj Pokhrel, Naman Yash, Jonathan Kua, Gang Li, Lei Pan

- 量子連合学習は、量子ネットワーク上で連合学習を実行し、ローカルデータのプライバシーを保つために開発されている
- クラウドプラットフォーム上でのQFLの展開における課題が探求されている
- 提案されたデータエンコーディングを使用したQFLは、ゲノムデータセットを用いた量子シミュレータ上での実証実験を通じて、有望な結果を示している
- 実験と成果はGitHubでオープンソースとして公開されている

**Comment:** SIGCOMM 2024, Quantum Computing, Federated Learning, Qiskit

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.ET, quant-ph, **投稿日時:** 2024-05-01 23:41

- - -

### [WHALE-FL: Wireless and Heterogeneity Aware Latency Efficient Federated Learning over Mobile Devices via Adaptive Subnetwork Scheduling](http://arxiv.org/abs/2405.00885)

**モバイルデバイス上での適応的サブネットワークスケジューリングを利用した連合学習の遅延効率向上手法、WHALE-FL**

Huai-an Su, Jiaxiang Geng, Liang Li, Xiaoqi Qin, Yanzhao Hou, Xin Fu, Miao Pan

- 連合学習はモバイルデバイス間での異種性による計算能力と通信能力の違いにより展開が困難
- 従来の固定サイズのサブネットワーク割り当てはデバイスの動的な変化や学習進行状況への対応が不十分
- WHALE-FLはデバイスの計算・通信能力と連合学習の進行状態に応じたサブネットワークサイズの動的選択を可能にする新しいユーティリティ機能を導入
- WHALE-FLは学習精度を犠牲にすることなく、連合学習の遅延を効果的に短縮



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.NI, eess.IV, **投稿日時:** 2024-05-01 22:01

- - -

### [Coherent 3D Portrait Video Reconstruction via Triplane Fusion](http://arxiv.org/abs/2405.00794)

**3Dポートレート動画再構築のためのTriplane Fusionによる新手法**

Shengze Wang, Xueting Li, Chao Liu, Matthew Chan, Michael Stengel, Josef Spjut, Henry Fuchs, Shalini De Mello, Koki Nagano

- 一枚の画像からの3Dポートレート再構築はあるが、フレームごとの再構築は時間的な一貫性が欠け、ユーザーの外観が失われる問題が存在
- 自己再現手法は3Dポートレートの一貫性を維持できるが、フレームごとの細かい表情や照明を正確に再現することは困難
- この研究では、個々の3Dモデルを補足するフレーム情報と融合し、時間的に安定で正確な3D動画を生成する新しい融合ベースの手法を提案
- 提案手法は、表情条件付き3D GANで生成された合成データを使用して訓練され、スタジオ内及び野外データセットにおいて3D再構築の精度と時間的一貫性で最先端の成果を実現



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-01 18:08

- - -

### [Federated Graph Learning for EV Charging Demand Forecasting with Personalization Against Cyberattacks](http://arxiv.org/abs/2405.00742)

**連合グラフ学習を用いたEV充電需要予測の個人化とサイバー攻撃対策**

Yi Li, Renyou Xie, Chaojie Li, Yi Wang, Zhaoyang Dong

- 電気自動車の充電需要予測におけるサイバーセキュリティリスクの軽減は、複数の充電施設の安全な運用、電力網の安定、インフラ拡張のコスト削減に重要
- 新たに提案された連合グラフ学習手法は、複数の充電ステーションの空間的相関を捉えつつ、予測モデルのトレーニングを協調することで汎用性と耐攻撃性を向上
- グラフニューラルネットワークを用いて、異なる充電ステーション間の地理的相関を連合形式で特徴付けることで、モデルのパフォーマンスを高める
- 各クライアントの個別のモデルを集約するグローバルアテンションメカニズムを活用したメッセージパッシングとクレジットベースの機能が導入され、データの異質性とサイバー攻撃のリスクに対処

**Comment:** 11 pages,4 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.LG, stat.ML, **投稿日時:** 2024-04-30 05:17

- - -

### [Federated Learning and Differential Privacy Techniques on Multi-hospital Population-scale Electrocardiogram Data](http://arxiv.org/abs/2405.00725)

**連合学習と差分プライバシー技術を用いた複数病院の大規模心電図データに関する研究**

Vikhyat Agrawal, Sunil Vasu Kalmady, Venkataseetharam Manoj Malipeddi, Manisimha Varma Manthena, Weijie Sun, Saiful Islam, Abram Hindle, Padma Kaul, Russell Greiner

- カナダ・アルバータの7つの病院からの1,565,849件の心電図データを使用し、連合学習と差分プライバシーを適用して多ラベル心電図分類モデルを学習
- 連合学習を用いることで、病院間で生データを共有せずにモデル訓練を共同で行い、様々な心臓病の診断に有効な心電図分類モデルを構築
- 実装された連合学習モデルは、全ての病院のデータを集約して訓練したモデルと比較して同等の性能を示す
- 差分プライバシーを使用することで、モデルの性能とデータプライバシーのトレードオフを示し、訓練データが限られている病院にとってもメリットがあることを示唆

**Comment:** Accepted for ICMHI 2024

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** eess.SP, cs.CR, cs.LG, **投稿日時:** 2024-04-26 19:29

- - -

### [EEG-Deformer: A Dense Convolutional Transformer for Brain-computer Interfaces](http://arxiv.org/abs/2405.00719)

**EEG-Deformer: 脳コンピュータインターフェースのための密な畳み込みトランスフォーマー**

Yi Ding, Yong Li, Hao Sun, Rui Liu, Chengxuan Tong, Cuntai Guan

- EEG信号の時間的ダイナミクスを学習することが課題だが、脳活動のデコードには不可欠である
- EEG-Deformerは、粗大な時間的ダイナミクスを効果的に識別する階層的粗大細密トランスフォーマー(Hierarchical Coarse-to-Fine Transformer, HCT)と、多レベルの純化された時間情報を利用する密情報浄化モジュール(Dense Information Purification, DIP)を組み込んだ
- 3つの認知タスクに関する広範な実験を通じて、提案されたEEG-Deformerの一般化能力が確認され、既存の最先端手法を上回るか、それに匹敵するパフォーマンスを示した
- EEG-Deformerは、対応する認知タスクに対し神経生理学的に意味のある脳領域から学習していることが視覚化結果から示された

**Comment:** 10 pages, 9 figures. This work has been submitted to the IEEE for   possible publication. Copyright may be transferred without notice, after   which this version may no longer be accessible

**トピック:** [連合転移学習](ftl), **カテゴリ:** eess.SP, cs.LG, q-bio.NC, **投稿日時:** 2024-04-25 18:00
