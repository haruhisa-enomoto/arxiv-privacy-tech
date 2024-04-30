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

更新: 2024-04-30T04:24:30.933884

- - -

### [FeDeRA:Efficient Fine-tuning of Language Models in Federated Learning Leveraging Weight Decomposition](http://arxiv.org/abs/2404.18848)

**FeDeRA: 重み分解を活用した連合学習における言語モデルの効率的なファインチューニング**

Yuxuan Yan, Shunpu Tang, Zhiguo Shi, Qianqian Yang

- FeDeRAはLoRAメソッドを改良したもので、パラメータ効率的なファインチューニングを連合学習に適用している
- 事前訓練された行列に特異値分解を行い、主成分を選択することを特徴とするアダプターモジュールを初期化する
- FeDeRAはFTメソッドと比較してパフォーマンスが良好であり、他のPEFTメソッドよりも優れている
- RoBERTaとDeBERTaV3を用いて三つのタスクでのトレーニング時間を95%以上削減し、効率性を保ちながらも高いパフォーマンスを実現している



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-29 16:42

- - -

### [Interpolating between Optimal Transport and KL regularized Optimal Transport using Rényi Divergences](http://arxiv.org/abs/2404.18834)

**$(\alpha, 1)$間でのKL正則化最適輸送問題と最適輸送問題の補間**

Jonas Bresch, Viktor Stein

- $\alpha$-Renyi分岐を用いて最適輸送問題を正則化する新たな手法を提案
- $\alpha$が0に近づくと未正則化の最適輸送問題へと収束し、$\alpha$が1に近づくとKL分岐に一致
- Renyi分岐によるペナルティを用いた手法は、未正則化とKL正則化最適輸送問題の間を補間するプリメトリックを導入
- 真実の輸送計画に近く、推論タスクでの性能が向上していることが、実データ及び合成データセットで示された

**Comment:** 40 pages, 9 figures, 3 tables, comments welcome

**トピック:** [合成データ](sd), **カテゴリ:** math.OC, cs.NA, math.FA, math.NA, 49Q22, 46N10, 94A15, **投稿日時:** 2024-04-29 16:21

- - -

### [Belt and Brace: When Federated Learning Meets Differential Privacy](http://arxiv.org/abs/2404.18814)

**連合学習と差分プライバシーが融合する時**

Xuebin Ren, Shusen Yang, Cong Zhao, Julie McCann, Zongben Xu

- 連合学習（FL）は、生データを露呈せずに大規模な機械学習を可能にする
- 差分プライバシー（DP）は、証明可能な保護を提供するプライバシー保護の事実上の標準である
- 連合学習に差分プライバシーを統合することで、プライバシーの全面的な保持が可能になるが、実用的な連合学習システムの開発は依然として困難
- この論文では、プライバシー保護とモデルの有用性間の適切なバランスを求める最適化原理についても議論している

**Comment:** 10 pages, 4 figures, accepted by and to appear in Communications of   the ACM (CACM)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-04-29 15:51

- - -

### [A Universal Metric of Dataset Similarity for Cross-silo Federated Learning](http://arxiv.org/abs/2404.18773)

**クロスサイロ連合学習のためのデータセット類似度を測るユニバーサルメトリック**

Ahmed Elhussein, Gamze Gursoy

- 連合学習でモデル性能の劣化を引き起こす異なるサイト間のデータセット分布の非同一性問題を解決
- データセットまたはタスク特有でなく、プライバシーを保護しながら計算できる新たな類似度メトリックを提案
- モデルの性能との関連が解釈可能で頑強な関係を示し、データを交換することなくプライバシーを保持しながら計算可能
- 各種データセット（合成データ、ベンチマークデータ、医用画像データセット）で広範囲に評価し、効率的な計算能力を実証



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-04-29 15:08

- - -

### [Private graph colouring with limited defectiveness](http://arxiv.org/abs/2404.18692)

**プライベートグラフ彩色における限定的な欠陥性**

Aleksander B. G. Christiansen, Eva Rotenberg, Teresa Anna Steiner, Juliette Vlieghe

- 差分プライバシーは、幅広い分野で重要なプライバシー保護データ分析の問題でゴールドスタンダードである
- 本研究では、差分プライバシー設定下での頂点色付け問題を検討している
- エッジ差分プライベート化を実現するための色分けアルゴリズムは欠陥が必要で、d-欠陥性色分けとは頂点が最大d個の隣接点と色を共有できる状況を指す
- 提案されたε-差分プライベート色分けアルゴリズムは、グラフをΘ({Δ} / log n + 1 / {ε})色で最大Θ(log n)の欠陥性で色分け可能



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, **投稿日時:** 2024-04-29 13:41

- - -

### [4D-DRESS: A 4D Dataset of Real-world Human Clothing with Semantic Annotations](http://arxiv.org/abs/2404.18630)

**4D-DRESS: 実世界の人間の服装に関する4Dデータセットおよびセマンティックアノテーション**

Wenbo Wang, Hsuan-I Ho, Chen Guo, Boxiang Rong, Artur Grigorev, Jie Song, Juan Jose Zarate, Otmar Hilliges

- 既存のデジタルアバターの服装研究は合成データに依存しており、現実感が欠ける場合がある
- 4D-DRESSは、リアルな4Dテクスチャスキャンと衣服メッシュを備えた初の実世界4Dデータセット
- 全体で64の衣装と520の人間動作シーケンスを含む78,000のテクスチャスキャンをキャプチャ
- 半自動の4D人間パーシングパイプラインを開発し、効率的な人間介入プロセスと自動化を組み合わせて正確にラベル付け

**Comment:** CVPR 2024 paper, 21 figures, 9 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-29 12:06

- - -

### [Assessing Quality Metrics for Neural Reality Gap Input Mitigation in Autonomous Driving Testing](http://arxiv.org/abs/2404.18577)

**自動運転テストにおけるニューラル実環境ギャップ入力緩和の品質指標評価**

Stefano Carlo Lambertenghi, Andrea Stocco

- 仮想シミュレーションは現実の条件を正確に再現できないことがあり、シミュレーションと実世界との間で自動運転システム（ADS）の挙動に重要な違いが発生する
- イメージ・トゥ・イメージ（I2I）ニューラル変換を用いて、シミュレート環境のリアリズムを向上し、sim2realギャップを緩和する手法が研究されている
- Pix2pixとCycleGANの二つのI2Iアーキテクチャを評価し、それぞれが車両検出とエンドツーエンドのレーンキーピングのタスクで異なる効果を示した
- タスク固有の調整を経た知覚指標を用いることで、より強い相関関係を示し、適切なI2I技術の選択を助けることが可能であることが確認された

**Comment:** In Proceedings of 17th IEEE International Conference on Software   Testing, Verification and Validation 2024 (ICST '24)

**トピック:** [合成データ](sd), **カテゴリ:** cs.SE, **投稿日時:** 2024-04-29 10:37

- - -

### [Bridging Data Barriers among Participants: Assessing the Potential of Geoenergy through Federated Learning](http://arxiv.org/abs/2404.18527)

**参加者間のデータ障壁を橋渡しする：連合学習を通じてジオエネルギーの潜在能力を評価する**

Weike Peng, Jiaxin Gao, Yuntian Chen, Shengwei Wang

- ジオエネルギー分野で、高いデータ収集コストとプライバシー懸念からデータ障壁が発生している
- 新しい連合学習フレームワークを導入し、XGBoostモデルを用いて複数の参加者の安全な共同モデリングを実現
- 提案されたFL-XGBoost手法はプライバシーと精度の最適なバランスを提供し、特にデータが限られている参加者において優れた精度と一般化能力を示す
- ベイズ最適化によりモデルのハイパーパラメータチューニングが効果的に達成され、新たな非典型的貯蔵層の評価への道を開く



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, stat.AP, **投稿日時:** 2024-04-29 09:12

- - -

### [On the Impact of Data Heterogeneity in Federated Learning Environments with Application to Healthcare Networks](http://arxiv.org/abs/2404.18519)

**データ異質性が連合学環境に与える影響に関する研究、特に医療ネットワークへの適用**

Usevalad Milasheuski. Luca Barbieri, Bernardo Camajori Tedeschini, Monica Nicoli, Stefano Savazzi

- 医療分野において、異なる集団が連合学習を用いて精度と汎化性能が向上されたグローバルモデルの構築を試みている
- 医療データの高い異質性が大きな課題であり、量ベースや特徴およびラベルの分布ベースの異質性への対処が必要
- 7つの主要な連合学習アルゴリズムを医療データケースの固有の課題に対して評価し、ベンチマークを行っている
- 心筋梗塞再発率のリスク予測を目的として、異なる加盟病院の集めた表形式の臨床報告データを用いる場合のデータ異質性の影響と連合学習の性能を検討



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-29 09:05

- - -

### [Fostering Trust in Smart Inverters: A Framework for Firmware Update Management and Tracking in VPP Context](http://arxiv.org/abs/2404.18453)

**スマートインバーターの信頼性向上: VPP環境におけるファームウェア更新管理と追跡のフレームワーク**

Thusitha Dayaratne, Carsten Rudolph, Tom Shirley, Sol Levi, David Shirley

- 分散エネルギー資源と電力グリッド間のインターフェースを提供するスマートインバーターの信頼性と安全性の確保が重要
- 既存のファームウェア更新による信頼性確立方法は、効果的な履歴追跡と検証が欠けている
- 新しいフレームワークを導入し、検証可能な証明書を利用してファームウェア更新履歴を管理・追跡する
- 更新履歴の追跡とこれら検証可能な更新に基づいた信頼サイクルの実装を通じて、グリッドのレジリエンス強化、サイバーセキュリティ向上、利害関係者への透明性増大を目指す



**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.CR, cs.SY, eess.SY, **投稿日時:** 2024-04-29 06:23

- - -

### [SPECIAL: Synopsis Assisted Secure Collaborative Analytics](http://arxiv.org/abs/2404.18388)

**SPECIAL: シノプシス支援型安全協調分析**

Chenghong Wang, Lina Qiu, Johes Bater, Yukui Luo

- 従来の安全協調分析(SCA)はデータの秘匿性が高いが、データ忘却プリミティブの大きなオーバーヘッドが実用的な採用を妨げている
- SPECIALは、制御された情報漏洩を許容することでプライバシーと効率のバランスが取れた初のSCAシステムである
- 特定のプライバシーコストで個人データからプライベートシノプシス(テーブル統計)を取得し、プライバシーを損なうことなくデータを安全に処理する
- 複雑なクエリに対して80倍高速なクエリ時間と900倍以上小さなメモリ使用量を実現し、連続処理におけるプライバシー損失も大幅に削減



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-04-29 02:55

- - -

### [Joint Energy and Latency Optimization in Federated Learning over Cell-Free Massive MIMO Networks](http://arxiv.org/abs/2404.18287)

**セルフリー・マッシブMIMOネットワークにおける連合学習のエネルギーと遅延の同時最適化**

Afsaneh Mahmoudi, Mahmoud Zaher, Emil Björnson

- 連合学習では生データセットの代わりにFLモデルをサーバーと交換し、データのプライバシーを保護しつつ通信オーバーヘッドを削減
- セルフリー・マッシブMIMO（CFmMIMO）は、空間多重化と協調ビームフォーミングを通じてエネルギー効率を高める
- 本研究では、各ユーザーの上り送信電力が他のユーザーのエネルギー効率と遅延に与える影響を考慮した電力割り当て方式を提案
- 数値結果によると、提案方式は既存の最大合計レートを27％、ディンケルバッハ法の最大最小エネルギー効率を21％上回るテスト精度でのパフォーマンス向上を実現



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-04-28 19:24

- - -

### [TabVFL: Improving Latent Representation in Vertical Federated Learning](http://arxiv.org/abs/2404.17990)

**TabVFL: 垂直連合学習における潜在表現の向上**

Mohamed Rashad, Zilong Zhao, Jeremie Decouchant, Lydia Y. Chen

- 垂直連合学習（VFL）において、既存のオートエンコーダ訓練方法では、各参加者が別々にオートエンコーダを訓練し潜在表現を後で集約するが、これにより参加者間の特徴データの重要な相関が失われる問題がある
- TabVFLは、参加者の共同特徴を用いて潜在表現の学習を改善するために設計された分散フレームワークを提案し、プライバシー保護と特徴相関の保持、訓練中のクライアント障害に対するロバスト性向上を目的とする
- 提案されたフレームワークは、全連結層の追加によって潜在的なデータ漏洩を抑制し、一つの潜在表現ベクトルを学習することで特徴の相関を維持する
- 実験結果では、TabVFLは既存の設計よりも優れた性能を示し、F1スコアで26.12％の改善を果たした



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-04-27 19:40

- - -

### [Privacy-Preserving Aggregation for Decentralized Learning with Byzantine-Robustness](http://arxiv.org/abs/2404.17970)

**分散学習のためのプライバシー保護集約とビザンチン堅牢性**

Ali Reza Ghavamipour, Benjamin Zi Hao Zhao, Oguzhan Ersoy, Fatih Turkmen

- 分散学習は、単一障害点を排除するために注目を集めているが、ビザンチンクライアントによって脅かされている
- ビザンチンクライアントは、グローバルモデルの性能を低下させようと意図的に任意のモデル更新を他のクライアントに送信する
- 本論文では、SecureDLという新規のプロトコルを導入し、ビザンチンの脅威に対するセキュリティとプライバシーを強化する
- SecureDLは、効率的な類似性計算と更新の正規化を使用して、モデルの収束に悪影響を与える更新を検出し排除する



**トピック:** [連合学習](fl), [秘密計算](mpc), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-04-27 18:17

- - -

### [FedCRL: Personalized Federated Learning with Contrastive Shared Representations for Label Heterogeneity in Non-IID Data](http://arxiv.org/abs/2404.17916)

**FedCRL: ラベル不均一性と非IIDデータにおけるコントラスティブ共有表現を用いた個別化連合学習**

Chenghao Huang, Xiaolu Chen, Yanru Zhang, Hao Wang

- ラベル分布の偏りやデータ不足に対処するために、コントラスティブ表現学習（CRL）を用いた新しい個別化連合学習アルゴリズム「FedCRL」を提案
- クライアント間での知識獲得を促進するために、ローカルモデルパラメータとローカル表現の平均値をサーバーに共有可能情報として導入
- ローカル表現とグローバル表現間でCRLを適用し、類似表現を近づけ分散表現を分けることで、ラベル分布の偏りによる影響を軽減
- データ不足対策として、各ローカルモデルとグローバルモデル間でのローカル集約を採用し、ローカル集約を調整する損失重み付けメカニズムを導入



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-27 14:05

- - -

### [Uncertainty quantification for iterative algorithms in linear models with application to early stopping](http://arxiv.org/abs/2404.17856)

**線形モデルにおける反復アルゴリズムの不確実性定量化と早期停止への応用**

Pierre C. Bellec, Kai Tan

- 高次元線形回帰問題において反復アルゴリズムから得られる反復子を分析し、特徴量の次元とサンプルサイズが近い場合に適用
- 新たな推定器を提案しており、Gradient Descent（GD）、proximal GD、Fast Iterative Soft-Thresholding（FISTA）などに対応
- 反復子の一般化誤差を推定し、$\sqrt n$-一致性を持っていることをガウスデザインの下で証明
- 一般化誤差が反復数に応じてU字型になる場合、データから最小の一般化誤差を達成する反復数$\hat t$を選択する方法を提供



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, math.ST, stat.CO, stat.ME, stat.TH, **投稿日時:** 2024-04-27 10:20

- - -

### [pFedAFM: Adaptive Feature Mixture for Batch-Level Personalization in Heterogeneous Federated Learning](http://arxiv.org/abs/2404.17847)

**pFedAFM: 異種連合学習におけるバッチレベル個人化のための適応型特徴混合**

Liping Yi, Han Yu, Chao Ren, Heng Zhang, Gang Wang, Xiaoguang Liu, Xiaoxiao Li

- 異種モデル個人化連合学習（MHPFL）を実現し、非独立同分布（non-IID）のローカルデータ上で構造的に異なる個人化モデルを訓練する
- 新たな手法pFedAFMを提案し、クライアント間での知識融合を支援するため全てのクライアントに共通の小型特徴抽出器を割り当てる
- グローバル共通の小型特徴抽出器とローカルの大型モデルを交互に訓練する反復学習戦略を導入し、効果的なグローバル・ローカル知識交換を行う
- バッチレベルのデータ多様性に適応するために、双方の特徴抽出器から抽出された特徴を動的に混合する訓練可能な重みベクトルを設計する



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-04-27 09:52

- - -

### [T-CLAP: Temporal-Enhanced Contrastive Language-Audio Pretraining](http://arxiv.org/abs/2404.17806)

**T-CLAP: 時間強化型コントラスティブ言語音声事前学習**

Yi Yuan, Zhuo Chen, Xubo Liu, Haohe Liu, Xuenan Xu, Dongya Jia, Yuanzhe Chen, Mark D. Plumbley, Wenwu Wang

- T-CLAPは、音声と言語のデータ表現を同期させることで、検索や分類タスクにおいて高い性能を発揮する
- 既存のCLAPモデルは音声とテキスト特徴内の時間情報を捉えるのに苦労していた
- T-CLAPは、音声クリップに対して時間対比的なキャプションを生成し、新たな時間焦点のコントラスティブ損失を用いてモデルを微調整する
- 実験結果からT-CLAPは音のイベントの時間的関係を捉える能力が向上し、最先端モデルを大幅に上回るパフォーマンスを示した

**Comment:** Preprint submitted to IEEE MLSP 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.LG, eess.AS, **投稿日時:** 2024-04-27 07:05

- - -

### [From Optimization to Generalization: Fair Federated Learning against Quality Shift via Inter-Client Sharpness Matching](http://arxiv.org/abs/2404.17805)

**最適化から一般化へ：クライアント間の鋭さのマッチングを通じた品質シフトに対する公平な連合学習**

Nannan Wu, Zhuo Kuang, Zengqiang Yan, Li Yu

- 医療データの分散訓練において連合学習がプライバシー保護の重要な手法として認識されている
- 画像の品質の不均一性が連合モデルで高品質画像への偏見を生じさせ、公平性に重大な問題を引き起こしている
- 新たに「連合学習におけるクライアント間の鋭さのマッチング（FedISM）」というソリューションを提案し、公平な一般化のためにクライアント間の鋭さレベルを調和させる
- FedISMは広く使用されているICHとISIC 2019データセットでの実験評価により、公平性を促進する既存の連合学習方法を上回ることが確認された

**Comment:** This paper is accepted at IJCAI'24 (Main Track)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-04-27 07:05

- - -

### [Personalized Federated Learning via Sequential Layer Expansion in Representation Learning](http://arxiv.org/abs/2404.17799)

**連合学習におけるパーソナライズのための表現学習に基づく新手法**

Jaewon Jang, Bonjun Choi

- 連合学習は、モデルの重みのみを中央サーバーで共有することでクライアントのプライバシーを保護
- データの異質性に対処するため、深層学習モデルを「基底」部と「ヘッド」部に分離する表現学習を利用
- 新しい手法では、モデルをさらに細かい部分に分離し、スケジューリング手法を適用してクラス異質性にも対応
- 提案アルゴリズムは既存の手法と比較して精度が向上し、計算コストの削減も実現している

**Comment:** 12 pages, 7 figure

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-27 06:37

- - -

### [Stocking and Harvesting Effects in Advection-Reaction-Diffusion Model: Exploring Decoupled Algorithms and Analysis](http://arxiv.org/abs/2404.17702)

**N種競合モデルを通じて個体群動態における補充と収穫（SH）効果を調査**

Mayesha Sharmim Tisha, Md. Kamrujjaman, Muhammad Mohebujjaman, Taufiquar Khan

- ARD（移流反応拡散）$N$-種競合モデルを提案し、補充と収穫が個体群動態に与える影響を探究
- 無フラックス境界条件下で２種の競争種の結果を分析し、解の存在、一意性、及び正値性を確立
- 非線形に結びついたARD $N$-種競合モデルに対して、新たな完全離散化された線形化アルゴリズム2つを提案、分析、検証
- 数値実験と合成データを用いてアルゴリズムの有効性や解析の収束率を検証し、最適な補充または収穫による種の共存シナリオを観察

**Comment:** 24 pages, 11 figures

**トピック:** [合成データ](sd), **カテゴリ:** math.NA, cs.NA, math.AP, math.DS, 92-10, 92C42, 92C60, 92D30, 92D45, 65M12, 65M22, **投稿日時:** 2024-04-26 21:20

- - -

### [Federated Learning for Blind Image Super-Resolution](http://arxiv.org/abs/2404.17670)

**連合学習による盲目的画像超解像**

Brian B. Moser, Ahmed Anwar, Federico Raue, Stanislav Frolov, Andreas Dengel

- 従来の盲目的画像SR手法は、現実の劣化を正確にモデル化する必要があるが、これが応用の限界を生む
- 提案手法では、連合学習を画像SRに融合させ、プライバシーを侵害することなくユーザーから直接劣化を学ぶ
- 新たに設計されたベンチマークは、分散ユーザーベース間での劣化の多様性を模倣し、実世界の劣化を正確にモデリングする必要を回避
- このベンチマークを用いて検証すれば、実際のアプリケーションでの性能が向上すると考えられる



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.AI, cs.CV, cs.ET, cs.LG, **投稿日時:** 2024-04-26 19:27

- - -

### [Beyond Traditional Threats: A Persistent Backdoor Attack on Federated Learning](http://arxiv.org/abs/2404.17617)

**伝統的な脅威を超えて: 連合学習における持続的バックドア攻撃**

Tao Liu, Yuhang Zhang, Zhu Feng, Zhiqin Yang, Chen Xu, Dapeng Man, Wu Yang

- 連合学習では、有害なバックドアが後続の良性の更新によって希釈され、攻撃成功率が著しく低下して失敗することが一般的
- 攻撃の持続性を定量化する新しい指標「attack persistence」を使用し、この弱まったバックドア効果を測定
- 全結合バックドア攻撃（FCBA）法を提案、グローバルモデルにより完全なバックドアパターンを形成するためのトリガー情報が集約され、攻撃が高い成功率を保持
- 三つのデータセットでテストし、FCBAは持続性が他の状態最先端の連合学習バックドア攻撃より優れていることが確認された



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.CV, cs.LG, **投稿日時:** 2024-04-26 11:47
