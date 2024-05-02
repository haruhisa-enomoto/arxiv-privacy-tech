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

更新: 2024-05-02T04:20:41.709692

- - -

### [Deep Metric Learning-Based Out-of-Distribution Detection with Synthetic Outlier Exposure](http://arxiv.org/abs/2405.00631)

**深層距離学習と合成データを用いた分布外検出の新手法**

Assefa Seyoum Wahd

- 深層距離学習とデノイジング拡散確率モデル(DDPM)を組み合わせて、合成分布外データを生成
- 分布内データは正確に分類し、分布外データに対するKL分岐を最小化する訓練を実施
- 実験では、距離学習ベースの損失関数がソフトマックスより優れていることを発見
- 合成的に生成された分布外データを使用した訓練により、既存のモデルが大幅に向上し、強力なベースラインを超える性能を示す



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-01 16:58

- - -

### [LEAP: Optimization Hierarchical Federated Learning on Non-IID Data with Coalition Formation Game](http://arxiv.org/abs/2405.00579)

**LEAP: 非IIDデータ上での階層的連合学習の最適化と連合形成ゲームの応用**

Jianfeng Lu, Yue Chen, Shuqin Cao, Longbiao Chen, Wei Wang, Yun Xin

- 階層的連合学習では、エッジサーバを用いて通信負担を軽減するが、非IIDデータと通信資源の制限によってモデルのパフォーマンスが低下する
- LEAPは連合形成ゲームと勾配投影を組み合わせた新しい最適化手法で、クライアントとエッジサーバ間の相関を動的に調整し、最適な相関を保証する
- クライアントの異質性を取り入れ、連合感覚から合理的な帯域幅割り当てを達成し、クライアントレベルで指定された遅延制約内で最適な送信パワーを決定する
- 実データセットに基づく実験結果は、LEAPが従来の基準よりも20.62％モデル精度が向上し、送信エネルギー消費を少なくとも約2.24倍削減することを示している



**トピック:** [連合学習](fl), **カテゴリ:** cs.GT, **投稿日時:** 2024-05-01 15:32

- - -

### [Swarm Learning: A Survey of Concepts, Applications, and Trends](http://arxiv.org/abs/2405.00556)

**スワーム学習：概念、アプリケーション、トレンドの調査**

Elham Shammar, Xiaohui Cui, Mohammed A. A. Al-qaness

- ディープラーニングモデルは、中央サーバーへの大規模データセットの依存により、プライバシーとセキュリティの問題を引き起こしている
- 連合学習(FL)は問題を解決するために分散型でハードウェア非依存の大規模機械学習フレームワークを構築したが、ネットワーク帯域幅の制約とデータ侵害に直面している
- スワーム学習(SL)は、ブロックチェーン技術を利用してセキュリティ、スケーラビリティ、プライバシーの強化された分散型機械学習フレームワークとして提案された
- この調査は、スワーム学習の原則、アーキテクチャ設計、応用分野を初めて紹介し、さらなる研究の必要性を強調している

**Comment:** 31 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, C.2.4, I.2.11, **投稿日時:** 2024-05-01 14:59

- - -

### [FMLFS: A federated multi-label feature selection based on information theory in IoT environment](http://arxiv.org/abs/2405.00524)

**IoT環境における情報理論に基づく連合型マルチラベル特徴選択FMLFS**

Afsaneh Mahanipour, Hana Khamfroush

- IoTデバイスが生成する大規模なマルチラベルデータセットでは、多次元の問題と無関係な特徴が分類器の性能に課題を与える
- FMLFSは初の連合学習を用いたマルチラベル特徴選択方法で、特徴とラベル間の相互情報を利用
- 特徴間の冗長性は相互情報と共同エントロピーから導出される相関距離を使用して評価
- 性能、計算時間、通信コストの3つの指標で評価され、他の5つの方法よりも優れており、実世界のデータセットにおいて良いトレードオフを提供

**Comment:** This paper has been accepted by IEEE SmartComp 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, cs.NI, math.IT, **投稿日時:** 2024-05-01 13:58

- - -

### [PackVFL: Efficient HE Packing for Vertical Federated Learning](http://arxiv.org/abs/2405.00482)

**PackVFL: 垂直連合学習のための効率的なHEパッキング**

Liu Yang, Shuowei Cai, Di Chai, Junxue Zhang, Han Tian, Yilun Jin, Kun Guo, Kai Chen, Qiang Yang

- 垂直連合学習(VFL)は、準同型暗号(HE)に基づいており、データ増大と時間を要する操作により効率の問題がある
- PackVFLは、複数のクリアテキストを1つの暗号テキストにパッキングし、SIMDスタイルの並列処理を支援する効率的なVFLフレームワーク
- 独自のマトリックス乗算(MatMult)方式を提案し、HEベースのVFLの計算コストと通信コストを効果的に削減
- PackVFLは、モデルサイズや特徴次元が大規模になるとも高い性能を保ち、既存のVFLアルゴリズムを最大51.52倍高速化することが実証された

**Comment:** 12 pages excluding references

**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-05-01 12:46

- - -

### [Detection of ransomware attacks using federated learning based on the CNN model](http://arxiv.org/abs/2405.00418)

**連合学習ベースのCNNモデルを使用したランサムウェア攻撃の検出**

Hong-Nhung Nguyen, Ha-Thanh Nguyen, Damien Lescos

- スマートグリッドやデジタル変電所に影響を与えるランサムウェアの脅威に対処するための研究
- AIを使用したランサムウェア検出方法とデジタル変電所の運用を対象とした攻撃モデルを提案
- バイナリデータを画像データに変換し、連合学習によって畳み込みニューラルネットワークモデルに供給
- 実験結果は、提案された技術が高い精度でランサムウェアを検出することを示す



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-05-01 09:57

- - -

### [Trust Driven On-Demand Scheme for Client Deployment in Federated Learning](http://arxiv.org/abs/2405.00395)

**信頼を基にしたオンデマンド方式によるクライアント配置の提案**

Mario Chahoud, Azzam Mourad, Hadi Otrok, Jamal Bentahar, Mohsen Guizani

- 連合学習(FL)において、コンテナ技術を使用したクライアントの参加拡大と学習の各イテレーションに特定のクライアント群の可用性の確保が重要
- クライアントの信頼性に関する問題に対処するために、"Trusted-On-Demand-FL"という信頼メカニズムを導入し、サーバーと適格なクライアント間の信頼関係を構築
- Dockerを使用してクライアントの行動を効果的に監視・検証し、データアクセスや改ざんから防御を強化
- 個々のクライアントに信頼値を割り当て、動的に調整することで、悪意のあるクライアントを特定し除外し、システムの安定性とセキュリティを向上



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-05-01 08:50

- - -

### [Enhancing Mutual Trustworthiness in Federated Learning for Data-Rich Smart Cities](http://arxiv.org/abs/2405.00394)

**データ豊かなスマートシティにおける連合学習の相互信頼性向上**

Osama Wehbi, Sarhad Arisdakessian, Mohsen Guizani, Omar Abdel Wahab, Azzam Mourad, Hadi Otrok, Hoda Al khzaimi, Bassem Ouni

- 都市環境の異質性が信頼できるクライアントの選定に課題を提起している
- クライアントとサーバー双方の信頼ニーズを考慮した新しいフレームワークを提案
- 信頼スコアに基づいて相手をランク付けするための嗜好関数を作成し、信頼性評価システムを構築
- 提案手法は、信頼レベルと全体的なモデル精度の向上、信頼できないクライアントの減少において従来方法を上回る



**トピック:** [連合学習](fl), **カテゴリ:** cs.GT, cs.LG, **投稿日時:** 2024-05-01 08:49

- - -

### [Employing Federated Learning for Training Autonomous HVAC Systems](http://arxiv.org/abs/2405.00389)

**連合学習を用いた自律型HVACシステムの訓練**

Fredrik Hagström, Vikas Garg, Fabricio Oliveira

- 建物のエネルギー消費は全体の40％を占め、その大部分は暖房、換気、空調(HVAC)から生じる
- モデルフリー強化学習アルゴリズムを用いてHVACシステムを訓練し、エネルギーコストと消費を削減し熱快適性を向上
- 連合学習アプローチを採用し、異なる気候区分のデータセンターで訓練されたローカルポリシーを集約してグローバルコントロールポリシーを学習
- 実験評価により、連合ポリシーは個別に訓練されたポリシーに比べて学習速度が速く、一般化能力も高いことが示された



**トピック:** [連合学習](fl), **カテゴリ:** math.OC, cs.LG, cs.SY, eess.SY, **投稿日時:** 2024-05-01 08:42

- - -

### [Metric geometry of the privacy-utility tradeoff](http://arxiv.org/abs/2405.00329)

**メトリック幾何学とプライバシー・ユーティリティトレードオフ**

March Boedihardjo, Thomas Strohmer, Roman Vershynin

- 合成データはデータ共有におけるプライバシーを確保する魅力的な概念である
- メトリックプライバシーを使用し、離散的な設定を超えた差分プライバシーの一般化を効果的に実施
- データの基盤となる空間のメトリック幾何学によって、最適なプライバシー精度トレードオフを特徴づける問題を提起
- 「エントロピックスケール」という量を用いて、この問題の部分的な解決策を提供し、メトリック空間の多スケール幾何学を捉える



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, math.PR, **投稿日時:** 2024-05-01 05:31

- - -

### [Proof of Sampling: A Nash Equilibrium-Secured Verification Protocol for Decentralized Systems](http://arxiv.org/abs/2405.00295)

**サンプリングの証明: 分散システム用ネイシュ均衡保証検証プロトコル**

Yue Zhang, Shouqiao Wang, Xiaoyuan Liu, Sijun Tan, Raluca Ada Popa, Ciamac C. Moallemi

- 分散アプリケーション用のサンプリングベース検証プロトコル「Proof of Sampling（PoSP）」を提案
- PoSPプロトコルは純粋戦略ネイシュ均衡を有し、参加者は正直に行動する動機付けがなされ、ネットワークの完全性が強化される
- PoSPをAIアプリケーションの分散推論に応用し、楽観的不正証明とゼロ知識証明ベースのアプローチを組み合わせた新しい方法「spML」を設計
- さらに、PoSPプロトコルはEigenLayer内のアクティブに検証されるサービス（AVS）の検証機構の設計に有効



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.GT, **投稿日時:** 2024-05-01 03:27

- - -

### [Differentially Private Release of Israel's National Registry of Live Births](http://arxiv.org/abs/2405.00267)

**差分プライバシーを用いたイスラエル国立出生登録簿の公開**

Shlomi Hod, Ran Canetti

- イスラエルの保健省は2014年の生誕データを差分プライバシー技術を用いて処理し、科学研究や政策立案に利用可能なデータセットをリリース
- プライバシー保護の基準として差分プライバシーを採用し、プライバシー喪失予算（\(\epsilon = 9.98\)）が設定された
- データ変換やモデル生成アルゴリズム選択等、複数のステップでプライベート選択アルゴリズムを活用
- プロジェクトの評価は差分プライバシー保証を提供するため、受入基準もおおよそのみ開示された



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.CY, cs.DS, **投稿日時:** 2024-05-01 01:20

- - -

### [Synthetic Face Datasets Generation via Latent Space Exploration from Brownian Identity Diffusion](http://arxiv.org/abs/2405.00228)

**合成顔データセットの生成: ブラウニアン・アイデンティティ拡散による潜在空間の探索**

David Geissbühler, Hatef Otroshi Shahreza, Sébastien Marcel

- 顔認識（FR）モデルの訓練は、プライバシーや倫理的な懸念を伴う大規模データセットを使用
- 合成データを利用して本物のデータを補完または置換する手法が提案されているが、データの多様性が十分かは不明
- 物理現象であるソフト粒子のブラウニアン運動に触発された新メソッドを導入し、潜在空間におけるアイデンティティ分布をサンプリング
- この方法で生成されたデータセットは、既存のGANベースのデータセットを上回り、最先端の拡散ベースの合成データセットと競合するパフォーマンスを実現

**Comment:** 17 pages, 7 figures, 10 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-30 22:32
