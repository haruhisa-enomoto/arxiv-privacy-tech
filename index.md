---
layout: single
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

更新: 2024-05-14T04:21:25.829889

- - -

### [A Demographic-Conditioned Variational Autoencoder for fMRI Distribution Sampling and Removal of Confounds](http://arxiv.org/abs/2405.07977)

**人口統計に基づいた条件付き変分オートエンコーダを用いたfMRIデータ分布のサンプリングと交絡因子の除去**

Anton Orlichenko, Gang Qu, Ziyu Zhou, Anqi Liu, Hong-Wen Deng, Zhengming Ding, Julia M. Stephen, Tony W. Wilson, Vince D. Calhoun, Yu-Ping Wang

- DemoVAEは、年齢、性別、人種などの人口統計学的交絡因子をfMRIデータから分離し、高品質な合成fMRIデータを生成する
- フィラデルフィア神経発達コホート(PNC)と双極性及び統合失調症ネットワーク(BSNIP)という大規模データセットを使用してモデルの訓練と検証を行う
- DemoVAEは従来のVAEやGANモデルよりも機能的接続の全分布をより良く再現し、fMRIデータに基づくほとんどの予測が人口統計との相関に依存していることを確認
- 人口統計に基づいて条件付けされた高品質な合成データの生成と、人口統計の交絡効果の除去を可能にする

**Comment:** 12 pages

**トピック:** [合成データ](sd), **カテゴリ:** q-bio.QM, cs.LG, q-bio.NC, **投稿日時:** 2024-05-13 17:49

- - -

### [Efficient and Universal Merkle Tree Inclusion Proofs via OR Aggregation](http://arxiv.org/abs/2405.07941)

**効率的で普遍的なマークル木包含証明のためのOR集約**

Oleksandr Kuznetsov, Alex Rusnak, Anton Yezhov, Dzianis Kanonik, Kateryna Kuznetsova, Oleksandr Domin

- ゼロ知識証明はブロックチェーンアプリケーションのプライバシーとセキュリティ強化に有効だが、証明システムの効率とスケーラビリティが課題である
- 伝統的なANDロジックに基づく証明集約手法は、検証の複雑さとデータ通信の負荷が高い
- この研究では、ORロジックに基づく新しい証明集約アプローチを提案し、マークル木の包含に対してコンパクトで普遍的に検証可能な証明を生成する
- 提案されたOR集約手法は、証明のサイズを木の葉の数とは独立にし、任意の有効な葉のハッシュを使用して検証が可能となり、効率と柔軟性の向上に寄与する



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-13 17:15

- - -

### [Stable Diffusion-based Data Augmentation for Federated Learning with Non-IID Data](http://arxiv.org/abs/2405.07925)

**連合学習における非IIDデータ分布用、安定拡散ベースのデータ拡張技術**

Mahdi Morafah, Matthias Reisser, Bill Lin, Christos Louizos

- 非独立同分布（Non-IID）データが存在する際の連合学習では、モデルトレーニングの性能低下と収束問題が発生する
- 本研究では、Gen-FedSDという新たなアプローチを導入し、テキストから画像への先進的モデルを活用して仮想データを生成
- 各クライアントはクラスラベルごとのテキストプロンプトを構築し、安定拡散モデルで高品質の合成データサンプルを生成
- 生成された合成データはローカルデータのギャップを埋め、最終的に局所データを等分布（IID）化させ、通信コストを削減しつつ高性能を実現

**Comment:** International Workshop on Federated Foundation Models for the Web   2024 (FL@FM-TheWebConf'24)

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-13 16:57

- - -

### [Synthetic Tabular Data Validation: A Divergence-Based Approach](http://arxiv.org/abs/2405.07822)

**合成表データの検証: 発散ベースのアプローチ**

Patricia A. Apellániz, Ana Jiménez, Borja Arroyo Galende, Juan Parras, Santiago Zazo

- タブラー表データを用いる分野での生成モデルの使用増加に対し、実データと合成データの類似性評価のための標準化された検証指標の必要性が高まっている
- 伝統的なアプローチは特徴ごとに発散を独立に計算しており、結合分布のモデリングの複雑さに対応できていない
- 本研究では、実データと合成データの結合分布を考慮した検証指標を構築するために発散推定器を応用している
- 二つの発散、Kullback-Leibler発散とJensen-Shannon発散を計算し、その効果を実データセットとその合成対応物で検証することで示している

**Comment:** 15 pages, 14 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, I.2.0, **投稿日時:** 2024-05-13 15:07

- - -

### [Decoding Geometric Properties in Non-Random Data from First Information-Theoretic Principles](http://arxiv.org/abs/2405.07803)

**情報理論の基本から非ランダムデータの幾何学的特性を解読する**

Hector Zenil, Felipe S. Abrahão

- 情報理論、測度理論、理論計算機科学に基づいて、一変量信号デコンボリューション法を導入
- この方法はゼロ知識一方向通信チャンネルでのコーディング理論に応用可能で、未知の生成源からのメッセージを解読できる
- 技術はエンコード・デコードスキーム、計算モデル、プログラミング言語、形式理論などに依存しない多次元空間再構築方法を提供
- データの非ランダム性を解読するこのユニバーサルな方法は、信号処理や暗号解読、生物・技術シグネチャー検出にも応用可能

**Comment:** arXiv admin note: substantial text overlap with arXiv:2303.16045.   substantial text overlap with arXiv:2303.16045

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.IT, cs.CL, cs.CR, cs.IR, math.IT, math.ST, stat.TH, **投稿日時:** 2024-05-13 14:45

- - -

### [SAR Image Synthesis with Diffusion Models](http://arxiv.org/abs/2405.07776)

**SAR画像合成における拡散モデルの利用**

Denisa Qosja, Simon Wagner, Daniel O'Hagan

- 拡散モデルは高品質な合成データ生成においてGANを上回る
- レーダー分野では訓練データが不足している問題があり、その解決に拡散モデルが利用されていなかった
- デノージング拡散確率モデル（DDPM）をSAR領域に適応し、条件付きおよび無条件のSAR画像生成のためのネットワーク選択と特定の拡散パラメータを検討
- DDPMは、事前訓練を重ねることで更に高品質なSAR画像を生成でき、GANベースの手法を定量的および定性的に上回ることを実験で示す

**Comment:** Published at IEEE Radar Conference 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, eess.IV, eess.SP, **投稿日時:** 2024-05-13 14:21

- - -

### [Federated Hierarchical Tensor Networks: a Collaborative Learning Quantum AI-Driven Framework for Healthcare](http://arxiv.org/abs/2405.07735)

**連合階層テンソルネットワーク: 医療分野における協力的な学習と量子AI駆動フレームワーク**

Amandeep Singh Bhatia, David E. Bernal Neira

- 医療分野での厳格なプライバシー規制下でデータの共有が難しい中、連合学習と量子計算を組み合わせた新フレームワークを提案
- 多体量子物理学の原理を活用し、クラシックなテンソルネットワークを連合環境に初めて実装
- 差分プライバシー分析を実施し、医療機関間での機密データのセキュリティを確保
- 人気の医療画像データセットにおいて、連合量子テンソルネットワークモデルが0.91-0.98のROC-AUCを達成し、高いテスト精度と一般化能力を示す

**Comment:** 12 pages, 8 figures

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** quant-ph, cs.AI, cs.LG, **投稿日時:** 2024-05-13 13:32

- - -

### [Coarse or Fine? Recognising Action End States without Labels](http://arxiv.org/abs/2405.07723)

**ラベルなしで行動の終了状態を認識するための粗さまたは細かさ？**

Davide Moltisanti, Hakan Bilen, Laura Sevilla-Lara, Frank Keller

- 画像内の行動の終了状態を認識することで、行われた行動とその方法の理解が重要
- データセットがないため、訓練データを合成する拡張方法を提案
- 合成データを使用し、粗くまたは細かく切られたオブジェクトを示す実際の画像でモデルをテスト
- モデルはトレーニングとテスト間のドメインギャップにもかかわらず切断動作の終了状態を正確に認識し、未知のオブジェクトにもうまく一般化する

**Comment:** The Eleventh Workshop on Fine-Grained Visual Categorization (CVPR 24)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-13 13:18

- - -

### [Local Mutual-Information Differential Privacy](http://arxiv.org/abs/2405.07596)

**地域相互情報差分プライバシー**

Khac-Hoang Ngo, Johan Östman, Alexandre Graell i Amat

- 地域相互情報差分プライバシー（LMIDP）は、プライバシーを保護するメカニズムの出力が明らかにされた場合の入力データについての不確実性の低減を定量化することを目指している
- LMIDPと地域差分プライバシー（LDP）、状況依存セッティングでの最先端概念である地域情報プライバシー（LIP）との関係性を研究し、明確な変換ルールを確立している
- LMIDPからLDP/LIPへのプライバシーパラメーターに対する制約を確立し、LMIDPが弱いプライバシー概念であることを形式的に検証している
- 入力データとノイズが平均電力制約を受ける場合、無相関ガウスノイズがCI-LMIDPにおける最適ノイズであることを示している

**Comment:** submitted to the IEEE Information Theory Workshop (ITW) 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.IT, math.IT, **投稿日時:** 2024-05-13 09:58

- - -

### [DID Connect: Authentication in TLS with Decentralized Identifiers and Verifiable Credentials](http://arxiv.org/abs/2405.07533)

**DID Connect: TLSにおける分散識別子と検証可能な証明を用いた認証**

Sandro Rodriguez Garzon, Dennis Natusch, Artur Philipp, Axel Küpper, Hans Joachim Einsiedler, Daniela Schneider

- TLSにおける認証は、中心的な認証局（CA）によって発行されるX.509デジタル証明書を使用して行われているが、これには単一障害点やサイバー攻撃のリスクが伴う
- 分散識別子（DID）と分散台帳技術を用いることで、中心的なCAに依存せずに特有の識別子の所有権を証明することが可能になり、セキュリティが強化される
- DID Connectは、自己発行されたX.509証明書と、台帳にアンカーされたDIDを用いてTLS 1.3で認証を行う新しい方式を提案
- 実装の試作は、検証素材がキャッシュされた場合には通常のTLSハンドシェイクと同等の時間で完了し、台帳から取得する場合にはわずかに時間が延長するが、全体の通信の安全性と信頼性を高める潜在性を示す

**Comment:** This work has been submitted to the IEEE for possible publication.   Copyright may be transferred without notice, after which this version may no   longer be accessible

**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.CR, cs.NI, **投稿日時:** 2024-05-13 08:03

- - -

### [Structured Reinforcement Learning for Incentivized Stochastic Covert Optimization](http://arxiv.org/abs/2405.07415)

**構造化された強化学習によるインセンティブ付き確率的秘密最適化**

Adit Jain, Vikram Krishnamurthy

- 分散最適化環境における盗聴者から局所的な定常点の推定値を隠すための確率的勾配アルゴリズムの制御について研究
- 学習者が確率的オラクルにクエリを行い、ノイズが含まれる勾配測定を得るためにオラクルを動機付ける
- 盗聴者への秘匿を目的とした最適化問題を、有限地平線マルコフ決定過程（MDP）として定式化
- 最適ポリシーが単調閾値構造を持つことを示し、確率的近似アルゴリズムと多腕バンディットアプローチを使用して探索提案



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.SY, eess.SY, **投稿日時:** 2024-05-13 01:29

- - -

### [PotatoGANs: Utilizing Generative Adversarial Networks, Instance Segmentation, and Explainable AI for Enhanced Potato Disease Identification and Classification](http://arxiv.org/abs/2405.07332)

**PotatoGANs: ジェネラティブ・アドバーサリアル・ネットワーク、インスタンス分割、説明可能AIを活用したポテト病状の特定と分類の向上**

Mohammad Shafiul Alam, Fatema Tuj Johora Faria, Mukaffi Bin Moin, Ahmed Al Wase, Md. Rabius Sani, Khan Md Hasib

- PotatoGANsは健康なポテト画像から合成データを生成するために2種類のGANを利用
- このアプローチはデータセットを拡張し、モデルの一般化能力を向上させる
- CycleGANはPix2Pix GANよりも高いISスコアを達成し、画像品質が優れている
- 三つの説明可能AIアルゴリズムと三つの異なるCNNアーキテクチャを組み合わせることで、ポテト病状の分類の解釈性が向上



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-12 17:00

- - -

### [Permissioned Blockchain-based Framework for Ranking Synthetic Data Generators](http://arxiv.org/abs/2405.07196)

**許可型ブロックチェーンに基づく合成データジェネレータランキングフレームワーク**

Narasimha Raghavan Veeraragavan, Mohammad Hossein Tabatabaei, Severin Elvatun, Vibeke Binz Vallevik, Siri Larønningen, Jan F Nygård

- 合成データジェネレータの選択を評価するロバストなフレームワークの必要性が高まっている
- 研究では、特定の用途に最適な合成データジェネレータを選出する方法と選択プロセスの透明性を向上させる方法を検討
- 提案されたランキングアルゴリズムは、Sawtoothと呼ばれる許可型ブロックチェーンフレームワーク内のスマートコントラクトとして実装された
- フレームワークは、データ保護原則に準拠しながら特定のニーズに最適な合成データジェネレータを選択するのに有効なツールとして機能



**トピック:** [合成データ](sd), **カテゴリ:** cs.DB, cs.CR, cs.DC, cs.LG, **投稿日時:** 2024-05-12 07:46

- - -

### [On-Demand Model and Client Deployment in Federated Learning with Deep Reinforcement Learning](http://arxiv.org/abs/2405.07175)

**連合学環境におけるオンデマンドモデルとクライアントの展開のための深層強化学習の活用**

Mario Chahoud, Hani Sami, Azzam Mourad, Hadi Otrok, Jamal Bentahar, Mohsen Guizani

- データの限定的なアクセス性とダイナミックな環境による課題に対応するため、Dockerコンテナを用いてオンデマンドで新たなクライアントを展開するソリューションを提案
- 深層強化学習（DRL）を利用し、クライアントの利用可能性と選択、データのシフトおよびコンテナ展開の複雑さを考慮
- モデル展開とクライアント選択を自動的に扱うエンドツーエンドの解決策を実装
- シミュレーションテストにより、提案されたアーキテクチャが環境変動に対応し、クライアントの利用可能性、能力、精度、学習効率を向上させることを確認



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-12 06:08

- - -

### [CRSFL: Cluster-based Resource-aware Split Federated Learning for Continuous Authentication](http://arxiv.org/abs/2405.07174)

**CRSFL: 連合学習とスプリット学習を組み合わせたクラスターベースのリソース意識型学習による連続認証**

Mohamad Wazzeh, Mohamad Arafeh, Hani Sami, Hakima Ould-Slimane, Chamseddine Talhi, Azzam Mourad, Hadi Otrok

- スプリット学習（SL）と連合学習（FL）を組み合わせ、連続認証の課題に対応しつつユーザープライバシーを保護しデバイス資源使用を抑制
- IoTデバイスのリソース差による訓練速度の低下に対処するため、類似能力のデバイスをクラスター化して影響を緩和
- 訓練の効率と堅牢性を向上させるために、クラスタリング後に遺伝的アルゴリズムを用いて最適なクライアント集合を選出
- 実世界データセット（UMDAA-02-FD）を用いた評価で、CRSFLは高い精度を維持しながら連続認証シナリオでのオーバーヘッド負荷を削減



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.DC, **投稿日時:** 2024-05-12 06:08

- - -

### [Digital Twin Aided Compressive Sensing: Enabling Site-Specific MIMO Hybrid Precoding](http://arxiv.org/abs/2405.07115)

**デジタルツインを活用した圧縮センシング：サイト特有のMIMOハイブリッドプリコーディングを可能にする**

Hao Luo, Ahmed Alkhateeb

- MIMOシステムの大規模アンテナアレイとハードウェアの制約に対するチャネル推定で、圧縮センシングが有望な解決策である
- 実世界のチャネルデータを収集することはアンテナの数とハードウェア制約により困難である
- サイト特有のデジタルツインを利用して、実世界のデータと似た合成データを生成し、深層学習モデルの訓練に使用する
- モデルの微調整アプローチを提案し、少量の実世界データでプリトレーニングされたモデルを微調整することで、リアルなデプロイメントでの高性能を実現

**Comment:** 7 pages, 5 figures

**トピック:** [合成データ](sd), **カテゴリ:** eess.SP, cs.IT, math.IT, **投稿日時:** 2024-05-12 00:11

- - -

### [Adaptive Online Bayesian Estimation of Frequency Distributions with Local Differential Privacy](http://arxiv.org/abs/2405.07020)

**局所差分プライバシーの下での頻度分布の適応的オンラインベイズ推定**

Soner Aydin, Sinan Yildirim

- ベイズアプローチを用いて有限カテゴリーの頻度分布を適応的かつオンラインで推定
- 局所差分プライバシー(LDP)に基づいてランダマイズメカニズムを調整し、サンプル後推定を活用
- 有用性を最大限に引き出すために部分集合選択プロセスを計算可能な範囲で実施
- 部分集合の選択が正確な場合、アルゴリズムは高い確率で最適な集合を選択することを理論解析が示す

**Comment:** Code for experiments available at   https://github.com/soneraydin/AdOBEst_LDP

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-05-11 13:59

- - -

### [Robust Model Aggregation for Heterogeneous Federated Learning: Analysis and Optimizations](http://arxiv.org/abs/2405.06993)

**異種連合学習における堅牢なモデル集約: 分析と最適化**

Yumeng Shao, Jun Li, Long Shi, Kang Wei, Ming Ding, Qianmu Li, Zengxiang Li, Wen Chen, Shi Jin

- 均一でないローカルデータサイズと計算能力により、従来の同期連合学習は性能劣化を引き起こす
- 新しい時間駆動型同期連合学習（T-SFL）を提案し、定期的な時間間隔で異なるクライアントからのモデルを集約
- 集約重みの最適化と、反復回数が閾値未満のローカルモデルを排除する判別モデル選択アルゴリズムを開発
- T-SFLと判別モデル選択アルゴリズムは、従来の同期連合学習に比べて50%のレイテンシ低減と3%の学習精度向上を実現



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-11 11:55

- - -

### [MH-pFLID: Model Heterogeneous personalized Federated Learning via Injection and Distillation for Medical Data Analysis](http://arxiv.org/abs/2405.06822)

**MH-pFLID: 医療データ分析のためのモデル非均一性パーソナライズ連合学習フレームワーク**

Luyuan Xie, Manqing Lin, Tianyu Luan, Cong Li, Yuejian Fang, Qingni Shen, Zhonghai Wu

- 医療アプリケーションではグローバルモデルを訓練するために連合学習が広く用いられているが、クライアント間のシステムの異種性が大きな課題となっている
- 非IIDデータからの情報を効果的に集約するために、新たな連合学習パラダイム「MH-pFLID」を提案
- このフレームワークは、情報を集めるために軽量なメッセンジャーモデルを利用し、高効率な情報注入と蒸留を実現するための送受信モジュールを開発
- 知識の蒸留に用いられるパブリックデータセットに依存しないため、プライバシーやデータ収集の問題を解決

**Comment:** This paper is accepted by ICML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-10 21:52

- - -

### [Open Challenges and Opportunities in Federated Foundation Models Towards Biomedical Healthcare](http://arxiv.org/abs/2405.06784)

**連合学習におけるバイオメディカル分野のファンデーションモデルの機会と課題**

Xingyu Li, Lu Peng, Yuping Wang, Weihua Zhang

- ファンデーションモデル(FM)は、ChatGPT、LLaMa、CLIPなど、大規模データセットの訓練を通じて医療診断やパーソナライズされた治療において重要な役割を果たす
- 連合学習(FL)を統合することで、医療データのプライバシー保護を保ちながらFMの分析力を活用する有望な戦略を提供する
- このサーベイは、FLフレームワーク内でのデータ多様性の管理、スケーリング、通信効率の強化などの課題を強調し、今後の研究方向を特定する
- 連合学習とファンデーションモデルの組み合わせの潜在力をさらに研究し、医療革新の土台を築くことが目指される

**Comment:** 42 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-10 19:22

- - -

### [Common Corruptions for Enhancing and Evaluating Robustness in Air-to-Air Visual Object Detection](http://arxiv.org/abs/2405.06765)

**空対空視覚オブジェクト検出のための共通破損に関する研究**

Anastasios Arsenos, Vasileios Karampinis, Evangelos Petrongonas, Christos Skliros, Dimitrios Kollias, Stefanos Kollias, Athanasios Voulodimos

- 実世界の飛行条件を考慮して7種類のカメラ入力破損を設計し、これらを航空物体追跡データセットに適用して、AOT-Cというロバスト性ベンチマークデータセットを構築した
- AOT-Cデータセットには、悪天候やセンサーノイズなど幅広い困難な条件が含まれている
- 8種類の異なるオブジェクト検出器を使用して実験評価を行い、破損が増加するにつれて性能が低下することを確認した
- 合成データのファインチューニングにより、オブジェクト検出器の実世界の飛行実験における一般化能力が向上することを示した



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-10 18:33

- - -

### [Utilizing Large Language Models to Generate Synthetic Data to Increase the Performance of BERT-Based Neural Networks](http://arxiv.org/abs/2405.06695)

**大規模言語モデルを用いた合成データ生成によるBERTベースのニューラルネットワーク性能向上**

Chancellor R. Woolsey, Prakash Bisht, Joshua Rothman, Gondy Leroy

- 医療分野における専門家不足を、機械学習モデルが診断支援で解消する可能性がある
- 大規模言語モデルを使用して、自閉症スペクトラム障害(ASD)に関する合成データ4200件を生成し、既存の医療データを補強
- 合成データを用いた学習が、BERTベースの分類器のリコールは向上したが、精度は低下
- 将来の研究で異なる合成データ特性が機械学習の成果に与える影響を分析する予定

**Comment:** Published in 2024 American Medical Informatics Association (AMIA)   Summit March 18-21

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-05-08 03:18
