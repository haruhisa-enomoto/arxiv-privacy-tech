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

更新: 2024-05-07T04:25:06.773812

- - -

### [Fault Detection and Monitoring using an Information-Driven Strategy: Method, Theory, and Application](http://arxiv.org/abs/2405.03667)

**情報駆動型戦略を使用した故障検出と監視: 方法、理論、および応用**

Camilo Ramírez, Jorge F. Silva, Ferhat Tamssaouet, Tomás Rojas, Marcos E. Orchard

- 新しいコンセプトドリフト検出器を基にした情報駆動型故障検出方法を提案
- 提案手法は、事前の故障例が不要で、多くのシステムモデルに対して分布フリーで適用可能
- 理論的特性を証明：強い一貫性、非故障ケースの迅速な検出、テストの重要度レベルとパワーの制御
- 合成データと航空機ターボファンエンジンのベンチマークデータセットN-CMAPSSで理論を検証し、多くの実際の設定での方法の有用性を支持

**Comment:** 28 pages, 11 figures

**トピック:** [合成データ](sd), **カテゴリ:** eess.SP, cs.IT, cs.LG, math.IT, **投稿日時:** 2024-05-06 17:43

- - -

### [Federated Learning Privacy: Attacks, Defenses, Applications, and Policy Landscape - A Survey](http://arxiv.org/abs/2405.03636)

**連合学習プライバシー：攻撃、防衛、応用、及び政策状況の調査**

Joshua C. Zhao, Saurabh Bagchi, Salman Avestimehr, Kevin S. Chan, Somali Chaterji, Dimitris Dimitriadis, Jiacheng Li, Ninghui Li, Arash Nourian, Holger R. Roth

- 連合学習はプライバシーを保護しながら共同で機械学習モデルの訓練を可能にするが、モデル更新がプライベートデータに関する情報を漏らす可能性がある
- この調査では連合学習におけるさまざまなプライバシー攻撃と防衛方法について広範な文献レビューを提供
- 実際の業界アプリケーションを解析し、連合学習の将来の成功の取り組みから教訓を得る
- 連合学習のプライバシー規制の新興風景を調査し、プライバシーを保ちながら正確なモデルを生成する方向での将来的な展望を提案

**Comment:** Submitted to ACM Computing Surveys

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.LG, I.2; H.4; I.5, **投稿日時:** 2024-05-06 16:55

- - -

### [Exploring the Efficacy of Federated-Continual Learning Nodes with Attention-Based Classifier for Robust Web Phishing Detection: An Empirical Investigation](http://arxiv.org/abs/2405.03537)

**フェデレート継続学習ノードと注目に基づく分類器を活用した堅牢なWebフィッシング検出の有効性の探求：実証調査**

Jesher Joshua M, Adhithya R, Sree Dananjay S, M Revathi

- フェデレート学習と連合学習を組み合わせる新たなパラダイムを提案し、分散ネットワーク上で新しいフィッシングデータについてモデルを継続的に更新
- 注目機構を利用したカスタムの注目に基づく分類器モデルを導入し、複雑なフィッシングパターンを検出
- 様々な連合学習戦略とモデルアーキテクチャを用いてハイブリッド学習パラダイムを評価
- 従来の方法を上回る成果を達成し、フィッシング脅威の検出と過去の知識の保持においてLwF戦略で精度0.93、適合率0.90、再現率0.96、F1スコア0.93を記録



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-06 14:55

- - -

### [GI-SMN: Gradient Inversion Attack against Federated Learning without Prior Knowledge](http://arxiv.org/abs/2405.03516)

**連合学習における事前知識不要のグラディエントインバージョン攻撃：GI-SMN**

Jin Qian, Kaimin Wei, Yongdong Wu, Jilian Zhang, Jipeng Chen, Huan Bao

- 連合学習では複数の参加者が元のユーザーデータではなく、勾配情報を共有することでプライバシーを保持
- 従来のグラディエントインバージョン攻撃は、モデル構造やバッチ正規化の統計を変更するなど、強い前提条件を必要としていた
- 新たに提案されたスタイル移行ネットワークを用いたグラディエントインバージョン攻撃(GI-SMN)は、これらの強い前提条件を必要としない
- GI-SMNはより高い類似度でユーザーデータを再構築可能であり、視覚効果と類似度の指標で従来の攻撃手法を上回る

**Comment:** 18 pages, 10 figures, conference

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-06 14:29

- - -

### [Robotic Constrained Imitation Learning for the Peg Transfer Task in Fundamentals of Laparoscopic Surgery](http://arxiv.org/abs/2405.03440)

**ロボットによる「基本的腹腔鏡手術のためのペグ移動タスク」の制約付き模倣学習**

Kento Kawaharazuka, Kei Okada, Masayuki Inaba

- 使用するポートを中心軸として鉗子を操作する必要があるため、腹腔鏡手術ロボットには2つの主要な課題が存在
- 単眼カメラを使用した場合、深度情報の認識が困難
- 熟練したオペレーターの例示的動作から動作制約を抽出し、これに基づいてデータを収集
- 双方のFranka Emika Panda Robot Armsを用いてシステムを構築し、その効果を確認

**Comment:** Accepted at ICRA2024, website -   https://haraduka.github.io/fls-imitation

**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, cs.AI, cs.LG, **投稿日時:** 2024-05-06 13:12

- - -

### [Snake Learning: A Communication- and Computation-Efficient Distributed Learning Framework for 6G](http://arxiv.org/abs/2405.03372)

**6Gにおけるスネークラーニング: 通信・計算効率の高い分散学習フレームワーク**

Xiaoxue Yu, Xingfu Yi, Rongpeng Li, Fei Wang, Chenghui Peng, Zhifeng Zhao, Honggang Zhang

- 既存の分散学習フレームワークはネットワーク環境の多様性で同期要求やコミュニケーションの負担が大きい問題がある
- スネークラーニングはノード間の異なる計算能力とローカルデータ分布を考慮し、モデルのレイヤーを順番にトレーニング
- このレイヤーごとの更新メカニズムにより、ストレージ、メモリ、通信要求を大幅に削減
- コンピュータビジョンのトレーニングと大規模言語モデルの微調整タスクにおいて効率性と適応性が優れている

**Comment:** 7 pages, 6 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.AI, **投稿日時:** 2024-05-06 11:25

- - -

### [Clustering of Disease Trajectories with Explainable Machine Learning: A Case Study on Postoperative Delirium Phenotypes](http://arxiv.org/abs/2405.03327)

**手術後せん妄のフェノタイプに関する説明可能な機械学習を用いた疾病軌跡のクラスタリング：事例研究**

Xiaochen Zheng, Manuel Schürch, Xingyu Chen, Maria Angeliki Komninou, Reto Schüpbach, Ahmed Allam, Jan Bartussek, Michael Krauthammer

- 手術後せん妄（POD）は、臨床的な表出や病態生理において多様性を示す複雑な神経精神医学的条件である
- PODにはいくつかの異なるフェノタイプが存在すると仮定し、これらの特定がPODの病態の理解と疾患対策の向上に寄与する
- 機械学習と非教師ありクラスタリング技術を組み合わせた手法を提案し、合成データを用いて有効性を示す
- 実世界データに適用することで、PODのような複雑な疾病の臨床的に関連するサブタイプを明らかにし、より正確で個別化された治療戦略への道を開く



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-06 10:05

- - -

### [Federated Learning for Drowsiness Detection in Connected Vehicles](http://arxiv.org/abs/2405.03311)

**連合学習による接続車両の眠気検知**

William Lindskog, Valentin Spannagl, Christian Prehofer

- 車両内のドライバー監視システムは、視覚的手がかりからドライバーの状態を識別する
- ドライバーのデータを一元化して処理することはプライバシーの問題やデータサイズの大きさから困難
- 車間連合学習フレームワークを提案し、YawDDデータセットを利用した眠気検出で99.2%の精度を実現
- 提案モデルは異なる数の連合クライアントでのスケールを示しており、従来の深層学習技術と比較可能

**Comment:** 14 pages, 8 figures, 1 table, EAI INTSYS 2023 conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-05-06 09:39

- - -

### [DarkFed: A Data-Free Backdoor Attack in Federated Learning](http://arxiv.org/abs/2405.03299)

**DarkFed: 連合学習におけるデータフリーバックドア攻撃**

Minghui Li, Wei Wan, Yuxuan Ning, Shengshan Hu, Lulu Xue, Leo Yu Zhang, Yichen Wang

- 連合学習はバックドア攻撃に対して脆弱であるが、実際の利用シナリオでは単純な防御で最新の攻撃を防げることが示されている
- DarkFedは、実際の訓練データがなくてもバックドア攻撃が可能な「データフリー」アプローチを提案している
- 影のデータセットを利用してバックドアを注入し、意味情報を欠く合成データを使用しても効果的な攻撃が可能であることを示している
- 悪意のある更新を良性のものと見間違うように最適化し、防御機構を回避する技術を開発している

**Comment:** This paper has been accepted by IJCAI 2024

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-05-06 09:21

- - -

### [Communication-Efficient Federated Learning with Adaptive Compression under Dynamic Bandwidth](http://arxiv.org/abs/2405.03248)

**動的帯域下で適応圧縮を用いた効果的な連合学習**

Ying Zhuansun, Dandan Li, Xiaohong Huang, Caijun Sun

- 連合学習は、ローカルモデルの頻繁な更新による大きな通信負担が問題となっている
- 提案されたAdapComFLアルゴリズムでは、各クライアントが帯域幅を認識し予測し、モデルを動的に圧縮
- サーバーは異なるサイズの圧縮モデルを集約する
- 実験結果はAdapComFLが通信効率と競合する精度で優れていることを示している



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-06 08:00

- - -

### [Mind the Gap Between Synthetic and Real: Utilizing Transfer Learning to Probe the Boundaries of Stable Diffusion Generated Data](http://arxiv.org/abs/2405.03243)

**安定拡散生成データの境界を探るための転移学習の活用**

Leonhard Hennicke, Christian Medeiros Adriano, Holger Giese, Jan Mathias Koehler, Lukas Schott

- 安定拡散のような生成基盤モデルは、ラベル付き実世界データ収集の必要性を回避する形で学習データの生成に利用可能
- 合成データで学習したモデルは、実データで訓練したモデルと比較して精度が著しく低下することが認められる
- 精度低下の主要因はモデルの最終層にあり、合成データと実データの間のデータ正規化の違いやデータ拡張による影響なども考慮されるが、実データとの差を埋めるには不十分
- 最終層のみ実データで微調整することにより、使用する実データの量とモデルの精度の間で改善されたトレードオフが示唆される



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-06 07:51

- - -

### [Compression-based Privacy Preservation for Distributed Nash Equilibrium Seeking in Aggregative Games](http://arxiv.org/abs/2405.03106)

**圧縮を基にしたプライバシー保護に関する分散ナッシュ均衡求解**

Wei Huo, Xiaomeng Chen, Kemi Ding, Subhrakanti Dey, Ling Shi

- 分散型アグレガティブゲームでの現行のナッシュ均衡求解法は、プライバシー問題と通信の負担を引き起こす
- 提案アルゴリズムは、ス トカスティック圧縮を用いて通信資源を節約し、圧縮により生じるランダムエラーで情報を隠蔽
- 圧縮エラーを使用しても収束精度を保証することを理論分析で示し、差分プライバシーも達成
- エネルギー消費ゲームでのシミュレーション結果がアプローチの有効性を支持



**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.SY, cs.GT, cs.SY, **投稿日時:** 2024-05-06 01:42

- - -

### [Powering the Future of IoT: Federated Learning for Optimized Power Consumption and Enhanced Privacy](http://arxiv.org/abs/2405.03065)

**IoTの未来を動かす：最適化された消費電力と向上したプライバシーのための連合学習**

Ghazaleh Shirvani, Saeid Ghasemshirazi

- IoT環境における消費電力の削減とプライバシー強化に連合学習が有望である
- IoTデバイスの寿命を延ばすため、連合学習の要素とIoTエコシステム内での応用を詳述
- IoTにおいて機械学習ソリューションが必要であると強調、消費電力とデータプライバシーが主な課題
- 連合学習の限界と可能性を探ることで、よりセキュアでプライバシー重視のIoT環境を開発するための研究が必要



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-05 22:18

- - -

### [Convolutional Learning on Directed Acyclic Graphs](http://arxiv.org/abs/2405.03056)

**有向非巡回グラフにおける畳み込み学習**

Samuel Rey, Hamed Ajorlou, Gonzalo Mateos

- 有向非巡回グラフ（DAG）上のデータから学ぶために特化した新しい畳み込みアーキテクチャを開発
- DAGの因果関係をモデリングする能力を生かしつつ、グラフのトポロジーによる部分順序を考慮する学習可能なDAGフィルターを組み込んだ新しい畳み込みグラフニューラルネットワークを提案
- 提案されたDAG畳み込みネットワーク（DCN）の主要な利点と潜在的な制約について議論
- 合成データを使用した二つの学習タスク（ネットワーク拡散推定と情報源識別）でDCNの性能を評価し、いくつかのベースラインと比較して有望な結果を示す



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-05 21:30

- - -

### [Confidential and Protected Disease Classifier using Fully Homomorphic Encryption](http://arxiv.org/abs/2405.02790)

**完全同型暗号を用いた機密性と保護された病気分類器**

Aditya Malik, Nalini Ratha, Bharat Yalavarthi, Tilak Sharma, Arjun Kaushik, Charanjit Jutla

- 大規模言語モデル（LLMs）の普及に伴い、多くの人々が病気診断などの健康関連の問い合わせで会話型AIを利用し始めている
- 個人の医療データをオンラインで共有するリスクに対応するため、完全同型暗号（FHE）とディープラーニングを組み合わせた新しいフレームワークを提案
- 提案システムは、医療従事者とのやり取りに似た質問応答モデルを採用し、入力データを暗号化して処理する
- 実験を通じて、安全性とプライバシーを維持しつつ性能の低下を最小限に抑える効果を実証



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-05-05 02:10

- - -

### [Understanding Server-Assisted Federated Learning in the Presence of Incomplete Client Participation](http://arxiv.org/abs/2405.02745)

**不完全なクライアント参加下でのサーバー支援連合学習についての理解**

Haibo Yang, Peiwen Qiu, Prashant Khanduri, Minghong Fang, Jia Liu

- 従来の連合学習では、クライアントの全参加または均一的な参加が仮定されていたが、実際には参加しないクライアントが存在する
- 不完全なクライアント参加問題に対処するためにサーバー支援連合学習（SA-FL）が用いられているが、その理論的理解はまだ不足している
- 不完全なクライアント参加のリスクを評価した結果、SA-FLを使用することで連合学習の学習可能性が復活することを初めて理論的に示した
- 実用的な指針として、SA-FLトレーニングのための$\mathsf{SAFARI}$（サーバー支援連合平均化）アルゴリズムを提案し、理想的なクライアント参加の仮定と同じ線形収束スピードアップを保証する

**Comment:** Accepted in ICML2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-04 19:56

- - -

### [A Mathematical Model of the Hidden Feedback Loop Effect in Machine Learning Systems](http://arxiv.org/abs/2405.02726)

**機械学習システムにおける隠れたフィードバックループ効果の数学モデル**

Andrey Veprikov, Alexander Afanasiev, Anton Khritankov

- 社会規模の機械学習システムの広範な展開により生じる長期的な影響を詳細に理解することが必要
- 繰り返し学習プロセスを導入し、エラー増幅、コンセプトのドリフト誘発、エコーチャンバーなどの現象を記述
- 環境の状態が時間とともに学習者自身に因果的に依存するようになり、通常のデータ分布の仮定が破られる
- 理論的な予測に基づいて合成データセットを使用した計算実験を行い、繰り返し学習プロセスを研究するアプローチの実現可能性を示す

**Comment:** 21 pages, 15 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.SY, eess.SY, **投稿日時:** 2024-05-04 17:57

- - -

### [Stable Diffusion Dataset Generation for Downstream Classification Tasks](http://arxiv.org/abs/2405.02698)

**安定拡散モデルによる下流分類タスク用合成データセットの生成**

Eugenio Lomurno, Matteo D'Oria, Matteo Matteucci

- 高品質の合成データを生成できるようになった最近の進歩を活用
- 安定拡散2.0モデルを用いた合成データセットの生成に、転移学習、ファインチューニング、生成パラメータの最適化技術を適用
- クラス条件付きモデルを導入し、クラスエンコーダと生成パラメータの最適化を行う
- 提案方法によって生成した合成データセットは、実データセットに比べて三分の一の場合において性能が向上したモデルを生んだ



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2024-05-04 15:37

- - -

### [FedProK: Trustworthy Federated Class-Incremental Learning via Prototypical Feature Knowledge Transfer](http://arxiv.org/abs/2405.02685)

**FedProK: 連合型クラス増分学習における信頼性を持つプロトタイプ特徴知識伝達**

Xin Gao, Xin Yang, Hao Yu, Yan Kang, Tianrui Li

- 連合クラス増分学習（FCIL）は知識の連続的な転送を通じて新しいクラスを学習する
- 従来のFCIL手法は、信頼性（連続的な効用、プライバシー、効率性の同時向上）を考慮していない
- FedProKは、プロトタイプ特徴を用いて空間的および時間的な知識伝達を実行
- FedProKは実験により他の最先端手法より信頼性の面で優れていることが証明された



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.NE, **投稿日時:** 2024-05-04 14:57

- - -

### [Metric Differential Privacy at the User-Level](http://arxiv.org/abs/2405.02665)

**ユーザーレベルのメトリック差分プライバシー**

Jacob Imola, Amrita Roy Chowdhury, Kamalika Chaudhuri

- メトリック差分プライバシーは入力ペア間の距離に基づいた異質なプライバシー保証を提供し、位置データなど多くのアプリケーションで自然なプライバシー意味論を捉える
- 従来の研究はアイテムレベル設定に焦点を当てていたが、本研究では各ユーザーが複数のアイテムを提供するユーザーレベル設定でのメトリックDPを初めて探求
- 地球移動距離を指標として使用し、ユーザーデータの変更の大きさと空間的側面を捉えるプライバシー概念を得るための2つの新規なメカニズムを設計
- 提案したメカニズムは、特定のタイプの線形クエリと頻度推定においてユーザーレベルDPよりも改善されたユーティリティを数学的に提供することが示された



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-04 13:29

- - -

### [Maximal Guesswork Leakage](http://arxiv.org/abs/2405.02585)

**最大推測リーク**

Gowtham R. Kurri, Malhar Managoli, Vinod M. Prabhakaran

- 「推測作業」とは、ランダム変数を推測するために必要な最小予想推測回数を指す
- 「最大推測リーク」とは、ランダム化された関数$X$の推測作業が、$Y$を観察することでどれだけ減少するか、すべてのランダム化関数に対して最大化された値
- ある特定の$Y$の実現のリリースによるリークを捉える、点形式のリークも研究
- 二元消失源については最大推測リークの閉形式表現を得るが、任意の源については表現を導出することが困難

**Comment:** 6 pages. Extended version of a paper accepted to ISIT 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.IT, math.IT, **投稿日時:** 2024-05-04 06:52

- - -

### [SSI4IoT: Unlocking the Potential of IoT Tailored Self-Sovereign Identity](http://arxiv.org/abs/2405.02476)

**SSI4IoT: IoT向け自己主権型アイデンティティの可能性を解き放つ**

Thusitha Dayaratne, Xinxin Fan, Yuhong Liu, Carsten Rudolph

- 既存の自己主権型アイデンティティ(SSI)の応用は主に人対人や人対サービスの関係に焦点を当てており、人対デバイスやデバイス対デバイスの相互作用は大きく見過ごされている
- この論文では、IoTにおけるSSIの適用に関していくつかの主要な課題を特定し、有効期間、信頼性、相互運用性レベル、使用範囲に関してIoTコンテキスト内での検証可能クレデンシャル(VC)の包括的な分類と使用法を提供する
- VCのライフサイクル管理やIoT環境でSSIを実現するためのさまざまな最適化技術についても詳細に取り扱う
- この研究はSSIを用いて既存および将来のIoTアプリケーションを安全にするための実践的な大規模採用に向けた注目すべき一歩である



**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.ET, cs.CR, cs.DC, **投稿日時:** 2024-05-03 20:31

- - -

### [No One-Size-Fits-All Neurons: Task-based Neurons for Artificial Neural Networks](http://arxiv.org/abs/2405.02369)

**人工ニューラルネットワークのためのタスクベースのニューロン**

Feng-Lei Fan, Meng Wang, Hang-Cheng Dong, Jianwei Ma, Tieyong Zeng

- 人間の脳がタスクベースのニューロンを使用しているため、人工ネットワークもタスクベースのニューロン設計に移行することを探求
- タスクベースのニューロンは、同じ構造を持つ既存のユニバーサルニューロンよりも特徴表現能力を向上させる
- 提案された二段階のフレームワークでは、最初にシンボリック回帰を使用して最適な式を特定し、次に獲得した基本式をパラメータ化して学習可能にする
- 実験結果が示す通り、提案されたタスクベースのニューロン設計は実現可能であり、他の最先端モデルと比較して競争力のある性能を提供する

**Comment:** 12 pages, 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.NE, cs.AI, cs.LG, **投稿日時:** 2024-05-03 09:12

- - -

### [A Survey on Contribution Evaluation in Vertical Federated Learning](http://arxiv.org/abs/2405.02364)

**垂直連合学習における寄与評価に関する調査**

Yue Cui, Chung-ju Huang, Yuzhu Zhang, Leye Wang, Lixin Fan, Xiaofang Zhou, Qiang Yang

- 垂直連合学習（VFL）はデータのプライバシー保護を目的とし、中央集中型のデータストレージや処理に対する重要なアプローチである
- VFLでは、異なる特徴セットを持つ複数のエンティティが協力して、直接的なデータ共有なしに予測モデルの共同トレーニングを実現
- 各エンティティの学習プロセスへの貢献を公正かつ正確に評価することが、信頼維持、資源の公平な共有、持続可能な協力体制の促進に必要
- この論文は寄与評価に関する広範なレビューやVFL生涯サイクルの段階ごとの特性分析も行っており、将来的な課題に対する展望も提示



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-03 06:32

- - -

### [Holistic Evaluation Metrics: Use Case Sensitive Evaluation Metrics for Federated Learning](http://arxiv.org/abs/2405.02360)

**連合学習のためのホリスティック評価指標: ユースケース感度を持つ評価指標**

Yanli Li, Jehad Ibrahim, Huaming Chen, Dong Yuan, Kim-Kwang Raymond Choo

- 連合学習の評価において、単一指標（例：正確性）に依存することが多いが、これは多種多様なユースケースの特異性を逃している
- 異なるユースケースごとに異なる重要性のベクトルを割り当て、それぞれの性能要件と優先順位を反映
- ホリスティック評価指標（HEM）は、正確性、収束性、計算効率、公平性、パーソナライゼーションといった複数の側面を包括
- 実験結果はHEMが特定のシナリオに最適な連合学習アルゴリズムを効果的に評価し特定できることを示す



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-03 03:39

- - -

### [Improved Communication-Privacy Trade-offs in  Mean Estimation under Streaming Differential Privacy](http://arxiv.org/abs/2405.02341)

**$L_2$平均推定を通信とプライバシーの要件の下で改善する方法について研究**

Wei-Ning Chen, Berivan Isik, Peter Kairouz, Albert No, Sewoong Oh, Zheng Xu

- 既存の平均推定スキームは$L_\infty$幾何に基づき、$L_2$幾何へ適応するためには非最適な定数で結果が出る
- 通信とプライバシーのトレードオフを改善する新しいプライバシー会計方法を導入
- 提案するアルゴリズムは、圧縮されていないガウスメカニズムの平均二乗誤差（MSE）に迅速に収束する
- 行列分解とDP-FTRL型オプティマイザーに特化したプライバシーアカウンタントをストリーミング差分プライバシー設定に拡張



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-05-02 03:48

- - -

### [A SER-based Device Selection Mechanism in Multi-bits Quantization Federated Learning](http://arxiv.org/abs/2405.02320)

**多ビット量子化連合学習におけるSERベースのデバイス選択メカニズム**

Pengcheng Sun, Erwu Liu, Rui Wang

- 無線通信の品質が連合学習のパフォーマンスに直接影響するため、シンボルエラーレート（SER）を用いてその影響を分析
- 通信の混雑と干渉を減少させるため、非直交多重アクセス（NOMA）を基本通信フレームワークとして使用
- 勾配パラメータを多ビットに量子化し、伝送誤差の耐性を高める
- SERに基づくデバイス選択メカニズム（SER-DSM）を設計し、通信状態が悪いユーザーの影響を避けつつ、より多くのユーザーが学習プロセスに参加できるようにする



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, cs.AI, math.IT, **投稿日時:** 2024-04-20 06:27
