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

更新: 2024-04-18T11:26:13.430334

- - -

### [Private federated discovery of out-of-vocabulary words for Gboard](http://arxiv.org/abs/2404.11607)

**Gboardのためのプライベート連合による語彙外単語の発見**

Ziteng Sun, Peter Kairouz, Haicheng Sun, Adria Gascon, Ananda Theertha Suresh

- Gboard言語モデルの語彙強化は、頻繁にタイプされる語彙外の単語をユーザーデバイスで発見することで達成される
- ユーザー入力データの機密性を考慮し、強固なプライバシー保護が必要とされる
- 新たに開発された語彙外単語発見アルゴリズムは、プライベート連合学習の最新技術を活用し、局所差分プライバシー保証を提供
- 匿名集計により、最終的に発表された単語は中央差分プライバシーの基準を満たしており、特に米国英語ではプライバシー保護基準が設定されている



**トピック:** [差分プライバシー](../../dp), **カテゴリ:** cs.DS, **投稿日時:** 2024-04-17 17:55

- - -

### [FedPFT: Federated Proxy Fine-Tuning of Foundation Models](http://arxiv.org/abs/2404.11536)

**FedPFT: Foundation Modelsの連合代理ファインチューニング**

Zhaopeng Peng, Xiaoliang Fan, Yufan Chen, Zheng Wang, Shirui Pan, Chenglu Wen, Ruisheng Zhang, Cheng Wang

- Foundation Modelsを下流タスクに適応させるために、連合学習を用いるアプローチがデータプライバシー保護とFM価値保持に有効である
- 既存のメソッドでは、FMをサブセクションに割り当てることで不十分なチューニングと勾配の誤差蓄積が発生し、最適でないパフォーマンスをもたらす
- 本論文では、FedPFTを提案し、FMの下流タスク適応を向上させるために、レイヤー別圧縮手法を用いたサブ-FM構成モジュールと、2段階の蒸留（レイヤーレベルおよびニューロンレベル）を行うサブ-FM調整モジュールを採用
- 7つの一般的なデータセット（テキスト4つ、ビジョン3つ）での実験結果がFedPFTの優位性を示す

**Comment:** Accepted by IJCAI'24

**トピック:** [連合学習](../../fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-17 16:30

- - -

### [A Federated Learning Approach to Privacy Preserving Offensive Language Identification](http://arxiv.org/abs/2404.11470)

**連合学習を用いたプライバシー保護型攻撃的言語識別のアプローチ**

Marcos Zampieri, Damith Premasiri, Tharindu Ranasinghe

- オンラインでの攻撃的言語の拡散はソーシャルメディアにとって重要な問題である
- 攻撃的言語を識別するための従来のモデルは、大量のデータを中央サーバーに保存しているが、プライバシーの問題が大きく残っている
- 連合学習（FL）を用いた分散型アーキテクチャーを提案し、ユーザーのプライバシーを保護しながら攻撃的言語を識別
- 提案されたモデル融合アプローチは、英語の4つの公開ベンチマークデータセット（AHSD, HASOC, HateXplain, OLID）で従来の基準を上回るパフォーマンスを示す同时，进行了英语与西班牙语的跨语言实验

**Comment:** Accepted to TRAC 2024 (Fourth Workshop on Threat, Aggression and   Cyberbullying) at LREC-COLING 2024 (The 2024 Joint International Conference   on Computational Linguistics, Language Resources and Evaluation)

**トピック:** [連合学習](../../fl), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-04-17 15:23

- - -

### [Real-Time Trajectory Synthesis with Local Differential Privacy](http://arxiv.org/abs/2404.11450)

**リアルタイム軌道合成と局所差分プライバシー**

Yujia Hu, Yuntao Du, Zhikun Zhang, Ziquan Fang, Lu Chen, Kai Zheng, Yunjun Gao

- ユーザーのトラジェクトリデータに局所差分プライバシーを適用し、プライバシーを保護しながらデータを共有
- 既存の方法は軌道ストリームの空間的-時間的コンテキスト情報を無視してしまう問題点が存在
- RetraSynフレームワークを提案し、リアルタイムでのトラジェクトリ合成を実現し、移動パターンに基づいた合成データの利用性を向上
- 実世界および合成データセットを用いたテストで、提案フレームワークの優越性と多才性を実証

**Comment:** Accepted by ICDE 2024. Code is available at:   https://github.com/ZJU-DAILY/RetraSyn

**トピック:** [差分プライバシー](../../dp), **カテゴリ:** cs.DB, cs.CR, **投稿日時:** 2024-04-17 14:55

- - -

### [What-if Analysis Framework for Digital Twins in 6G Wireless Network Management](http://arxiv.org/abs/2404.11394)

**6Gワイヤレスネットワーク管理のためのデジタルツインによるWhat-if分析フレームワーク**

Elif Ak, Berk Canberk, Vishal Sharma, Octavia A. Dobre, Trung Q. Duong

- デジタルツインネットワーク（DTN）をNS-3で実装した物理ツイン層と、機械学習及び強化学習を利用したサービス層で構成
- キャリア感度閾値と無線ネットワークの送信電力制御を最適化
- 条件付き表型GAN（CTGAN）を用いた合成データ生成により、様々なネットワークシナリオを模倣
- 通信のスループット、遅延、パケットロス、カバレッジの4つのネットワークパフォーマンス指標の評価を含む

**Comment:** 6 pages, 3 figures, 1 table conference

**トピック:** [合成データ](../../sd), **カテゴリ:** cs.NI, **投稿日時:** 2024-04-17 13:55

- - -

### [Enhancing Data Privacy In Wireless Sensor Networks: Investigating Techniques And Protocols To Protect Privacy Of Data Transmitted Over Wireless Sensor Networks In Critical Applications Of Healthcare And National Security](http://arxiv.org/abs/2404.11388)

**ワイヤレスセンサーネットワークにおけるデータプライバシーの強化：保健医療と国家安全保障の重要アプリケーションにおけるデータ送信のプライバシー保護のための技術とプロトコルの調査**

Akinsola Ahmed, Ejiofor Oluomachi, Akinde Abdullah, Njoku Tochukwu

- ワイヤレスセンサーネットワーク(WSN)は、健康管理、国家安全、緊急対応、インフラ監視など多岐にわたるアプリケーションに利用されている
- データプライバシーを守るために、暗号化技術、認証メカニズム、匿名化技術、アクセス制御メカニズムが重視されている
- ヘルスケアと国家安全の文脈でのデータプライバシーに関連する脆弱性や課題が指摘され、規制遵守や倫理的考慮、社会経済的要因が強調された
- プライバシー保護技術の採用を理解するために「イノベーションの普及理論」が紹介され、有効なセキュリティソリューションの事例が検討された



**トピック:** [PETs](../../pets), **カテゴリ:** cs.CR, cs.NI, **投稿日時:** 2024-04-17 13:48

- - -

### [S3PHER: Secure and Searchable System for Patient-driven HEalth data shaRing](http://arxiv.org/abs/2404.11372)

**S3PHER: 患者主導の健康データ共有のためのセキュアで検索可能なシステム**

Ivan Costa, Ivone Amorim, Eva Maia, Pedro Barbosa, Isabel Praca

- 健康データ共有のための既存のシステムは、プライバシー、機密保持、同意管理といったセキュリティ要件を完全に満たしていない
- S3PHERは、どのデータが誰に、いつアクセスされるかを患者自身がコントロールできる新しい健康データ共有アプローチを提案
- このシステムは、準同型暗号を利用して、医療従事者が患者の文書にプライベートに検索アクセスできるようにし、エンドツーエンドのプライバシーを保証
- 実際のデータセットにおけるテストは、実行時間が有望であることを示し、エンドツーエンドのデプロイメントと使用例分析を通じてS3PHERの実用性と利点が確認された

**Comment:** 20 pages, 1 figure, 2 tables in the appendix

**トピック:** [準同型暗号](../../he), **カテゴリ:** cs.CR, E.3; H.3.1; H.3.2; H.3.3, **投稿日時:** 2024-04-17 13:31

- - -

### [CAGE: Causality-Aware Shapley Value for Global Explanations](http://arxiv.org/abs/2404.11208)

**CAGE: 因果関係を考慮したShapley値によるグローバル説明**

Nils Ole Breuer, Andreas Sauter, Majid Mohammadi, Erman Acar

- AIの決定が透明で説明可能であることが重要とされる中、XAI（説明可能なAI）分野が人気を博している
- 従来のShapley値に基づく方法は特徴の独立性を仮定しており、特徴間の因果関係を見落としていた
- CAGEは特徴の因果関係を尊重する新しいサンプリング手法を提案し、グローバルな説明に因果知識を組み込む
- 合成データと実世界のデータによる評価で、従来の方法より直感的で忠実な説明が可能とされた



**トピック:** [合成データ](../../sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-04-17 09:43

- - -

### [Synthesizing Realistic Data for Table Recognition](http://arxiv.org/abs/2404.11100)

**表認識のための現実的なデータの合成**

Qiyu Hou, Jun Wang, Meixuan Qiao, Lujun Tian

- 既存の自動表データアノテーション方法やランダムな表データ合成手法の限界を克服するために、表認識専用のアノテーションデータの合成方法を提案
- 複雑な表の構造と内容を利用して、対象ドメインの本物のスタイルを密接に再現する表を効率的に作成
- 中国の金融告示から得られた表の実際の構造と内容を活用し、この分野で初の広範囲な表アノテーションデータセットを開発し、ディープラーニングベースの表認識モデルを訓練
- 合成手法を用いて、英語の金融告示から抽出されたFinTabNetデータセットに複雑性を加え、複数のセルが交差する表の割合を増加させた結果、特に複数のセルが交差する表の認識性能が向上することを実証

**Comment:** ICDAR 2024

**トピック:** [合成データ](../../sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-04-17 06:36

- - -

### [Lightweight Unsupervised Federated Learning with Pretrained Vision Language Model](http://arxiv.org/abs/2404.11046)

**軽量かつ教師なし連合学習の新手法: 事前学習された視覚言語モデルの活用**

Hao Yan, Yuhong Guo

- 連合学習は、個々のクライアントが孤立したデータからプライバシーを保護しつつ共同モデルを学習することを目指す
- 提案手法は、事前に学習された視覚言語モデル（例: CLIP）を使用して、ラベルがないデータに対して軽量なモデル訓練と通信を行う
- ゼロショット予測能力を利用して、固定された画像エンコーダー上で線形分類器のみを訓練することにより、擬似ラベルを洗練
- 各クライアント内のデータ不均衡に対処するため、クラスバランスの取れたテキスト特徴サンプリング戦略により合成データを生成し、ローカルトレーニングをサポートする



**トピック:** [連合学習](../../fl), **カテゴリ:** cs.AI, cs.CV, cs.LG, **投稿日時:** 2024-04-17 03:42

- - -

### [Approximate Wireless Communication for Lossy Gradient Updates in IoT Federated Learning](http://arxiv.org/abs/2404.11035)

**IoT環境における連合学習のための効率的な近似無線通信手法**

Xiang Ma, Haijian Sun, Rose Qingyang Hu, Yi Qian

- IoTデバイス向けに特化した連合学習のパラメータ伝送のための無線通信手法を提案
- 従来のエラー訂正コードや再送信を避けながら、機械学習の勾配の近似値を効率的に伝送
- 受信側の勾配値を特定の範囲内に制限する新しい受信ビットマスキング方法を導入
- シミュレーションにより、提案手法がFL性能のランダムビットエラーを有効に軽減し、従来の方法に比べて通信時間を50%削減することを実証

**Comment:** submitted to IEEE journals for publication

**トピック:** [連合学習](../../fl), **カテゴリ:** cs.IT, cs.DC, cs.NI, math.IT, **投稿日時:** 2024-04-17 03:23

- - -

### [FedFa: A Fully Asynchronous Training Paradigm for Federated Learning](http://arxiv.org/abs/2404.11015)

**FedFa: 連合学習のための完全非同期訓練パラダイム**

Haotian Xu, Zhaorui Zhang, Sheng Di, Benben Liu, Alharthi Khalid, Jiannong Cao

- 連合学習ではFedAvgが基本的なパラメータ更新戦略として使用され、異なるクライアント間のデータの非均質性の影響を排除して収束を保証
- トレーニング中の各通信ラウンドの同期化による待ち時間が、トレーニングの速度を遅らせる問題がある
- 提案された完全非同期トレーニングパラダイム「FedFa」は、サーバー上のバッファされた結果を使用することで完全に待ち時間を排除し、モデルの収束を保証
- 実験結果によると、FedFaは最新の同期および半同期戦略よりも6倍までトレーニング性能を改善し、IIDおよびNon-IIDシナリオの両方で高精度を維持



**トピック:** [連合学習](../../fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-04-17 02:46

- - -

### [Personalized Federated Learning via Stacking](http://arxiv.org/abs/2404.10957)

**パーソナライズド連合学習のためのスタッキング手法**

Emilio Cantu-Cervini

- 既存の連合学習は単一のグローバルモデルを共同で訓練するのに対し、パーソナライズド連合学習は個々のクライアントデータに合わせた複数のモデルを作成する
- 新たなパーソナライズ手法として、スタッキングされた一般化を用いたモデルが提案され、各クライアントがプライバシーを保護されたモデルを他のクライアントと直接共有する
- この手法は様々なプライバシー保護技術やモデルタイプへの対応が可能であり、横断的、ハイブリッド、垂直的に分割された連合に適用可能
- 評価を通じて、我々の方法が異なるデータの不均一性シナリオにおいて有効であることを示す



**トピック:** [連合学習](../../fl), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-04-16 23:47

- - -

### [Cognitive-Motor Integration in Assessing Bimanual Motor Skills](http://arxiv.org/abs/2404.10889)

**認知運動統合による両手運動技能の評価**

Erim Yanik, Xavier Intes, Suvranu De

- 従来の両手運動技能評価は主観的判断や運動行動のみに焦点を当て、認知プロセスを見落としていた
- この研究では、認知的意思決定と運動実行の両方を分析・統合するために深層ニューラルネットワーク(DNN)を活用
- 腹腔鏡手術スキルの評価において、動画キャプチャと非侵襲的近赤外線分光法(fNIRS)を用いて神経活動を測定
- 従来の単一方法よりも精度高く専門家レベルを分類し、FLS行動パフォーマンススコアを予測

**Comment:** 12 pages, 3 figures, 2 tables

**トピック:** [連合学習](../../fl), **カテゴリ:** cs.AI, **投稿日時:** 2024-04-16 20:20

- - -

### [Unsupervised Speaker Diarization in Distributed IoT Networks Using Federated Learning](http://arxiv.org/abs/2404.10842)

**分散IoTネットワークにおける教師なし話者識別のための連合学習の利用**

Amit Kumar Bhuyan, Hrishikesh Dutta, Subir Biswas

- 連合学習を用いて、大規模な音声データベースを必要とせずに会話参加者を識別する効率的なフレームワークを提案
- 話者の埋め込みのコサイン類似性に依存した、教師なしオンライン更新メカニズムを導入
- ホテリングのt二乗統計とベイズ情報基準を使用した非監督セグメント技術により、話者変更検出を改善
- 非IID音声データでも高い効果を示し、セグメンテーション段階での誤検出と見逃し検出の削減に成功

**Comment:** 11 pages, 7 figures, 1 table

**トピック:** [連合学習](../../fl), **カテゴリ:** cs.SD, cs.LG, eess.AS, **投稿日時:** 2024-04-16 18:40
