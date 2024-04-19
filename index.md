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

更新: 2024-04-19T16:17:39.455681

- - -

### [KDk: A Defense Mechanism Against Label Inference Attacks in Vertical Federated Learning](http://arxiv.org/abs/2404.12369)

**垂直連合学習におけるラベル推論攻撃防御機構 KDk**

Marco Arazzi, Serena Nicolazzo, Antonino Nocera

- 垂直連合学習（VFL）では、標本のラベルが集約サーバーを除く全参加者から秘匿される
- サーバーから返される勾配情報を利用して、敵は限られた補助ラベルのみで秘密のラベルを推測可能である
- KDkフレームワークは知識蒸留とk-匿名性を組み合わせてVFLのラベル推論攻撃に対する防御機制を提供
- 提案手法ではラベル推論攻撃の効果を60%以上削減しつつ、VFL全体の正確性はほぼ変わらないことが示された



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-04-18 17:51

- - -

### [Inverse Neural Rendering for Explainable Multi-Object Tracking](http://arxiv.org/abs/2404.12359)

**逆ニューラルレンダリングによる説明可能なマルチオブジェクト追跡**

Julian Ost, Tanushree Banerjee, Mario Bijelic, Felix Heide

- 既存のネットワークは異なるデータセット間での一般化に苦労するが、本研究ではRGBカメラからの3Dマルチオブジェクト追跡を逆レンダリング問題として再構成する
- 事前訓練された3Dオブジェクト表現の潜在空間を最適化し、入力画像内のオブジェクトインスタンスを最もよく表す潜在変数を回収する
- 本手法では形状と外観の特性を自然に切り離す生成的潜在空間の画像損失を最適化する
- 合成データからのみ生成的事前学習を行い、nuScenesおよびWaymoデータセットを使用してカメラに基づく3D追跡の一般化とスケーリング能力を検証する



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.GR, cs.RO, **投稿日時:** 2024-04-18 17:37

- - -

### [FedEval-LLM: Federated Evaluation of Large Language Models on Downstream Tasks with Collective Wisdom](http://arxiv.org/abs/2404.12273)

**FedEval-LLM: 大規模言語モデルのダウンストリームタスクでの連合評価における集合知**

Yuanqin He, Yan Kang, Lixin Fan, Qiang Yang

- 大規模言語モデル（LLM）を連合学習（FL）に統合するには、評価方法に関する新たな課題が存在する
- 従来の評価方法は限られた適切な答えのみをカバーし、LLMの生成タスクでの性能を正確に反映できない
- FedEval-LLMは、ラベル付きテストセットや外部ツールに依存せずに、LLMのダウンストリームタスクでの性能を信頼性高く測定するためのフレームワークを提案する
- 実験結果は、この評価モデルがダウンストリームタスクにおける評価能力を大幅に改善し、人間の好みとRougeLスコアとの強い一致を示す

**Comment:** In Progress

**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, cs.CL, cs.LG, **投稿日時:** 2024-04-18 15:46

- - -

### [Aligning Actions and Walking to LLM-Generated Textual Descriptions](http://arxiv.org/abs/2404.12192)

**LLMを用いて行動とウォーキングパターンのテキスト記述を調整する**

Radu Chivereanu, Adrian Cosma, Andy Catruna, Razvan Rughinis, Emilian Radoi

- 大規模言語モデル（LLM）を使用して、行動認識と歩行シーケンスの検索のために、動作シーケンスに富んだテキスト記述を生成
- BABEL-60データセットの行動をテキストで記述し、動作シーケンスと言語表現を整合させる
- DenseGaitデータセットを用い、衣服選択や履物による歩行スタイルの変動を捉えたテキスト記述を生成
- LLMの能力を活用し、構造化された動きの属性を増大させ、マルチモーダル表現を整合する方法を示す

**Comment:** Accepted at 2nd Workshop on Learning with Few or without Annotated   Face, Body and Gesture Data

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-18 13:56

- - -

### [Privacy-Preserving UCB Decision Process Verification via zk-SNARKs](http://arxiv.org/abs/2404.12186)

**プライバシー保護を目的としたUCB意思決定プロセスのzk-SNARKsを用いた検証**

Xikun Jiang, He Lyu, Chenhao Ying, Yibin Xu, Boris Düdder, Yuan Luo

- 機械学習のプライバシー保護と検証可能性のバランスを取るために、ゼロ知識証明(zk-SNARKs)を活用した新しいアルゴリズムzkUCBを導入
- zkUCBは訓練データとアルゴリズムパラメータの機密性を保護しながら、透明なUCB意思決定プロセスを実現
- 実験により、zkUCBは情報量の減少に貢献する量子化ビットの適切な使用により性能が向上することが示された
- zkUCBの証明サイズと検証時間は、実行ステップに比例してスケールし、データセキュリティと運用効率のバランスを効果的に取る



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-04-18 13:49

- - -

### [One-Shot Sequential Federated Learning for Non-IID Data by Enhancing Local Model Diversity](http://arxiv.org/abs/2404.12130)

**非IIDデータに対するワンショット連続連合学習の向上のためのローカルモデル多様性強化**

Naibo Wang, Yuchen Deng, Wenjie Feng, Shichen Fan, Jianwei Yin, See-Kiong Ng

- 伝統的な連合学習は、高い通信と計算コストに悩まされるが、ワンショットおよびシーケンシャル連合学習はこれを軽減する新しいパラダイムとして登場
- ローカルモデルの多様性を利用するため、各クライアントに多様なモデルを持つローカルモデルプールを導入し、モデル多様性をさらに強化するための二つの距離測定法を提案
- 提案するフレームワークは通信コストを抑えつつ世界的なモデルの性能を向上させる
- 広範な実験により、提案方法は従来のワンショット並列連合学習方法より優れた性能を示し、特にCIFAR-10データセットでラベルスキューとドメインシフトのタスクで6％以上の精度向上を実現



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, cs.DC, **投稿日時:** 2024-04-18 12:31

- - -

### [FedMID: A Data-Free Method for Using Intermediate Outputs as a Defense Mechanism Against Poisoning Attacks in Federated Learning](http://arxiv.org/abs/2404.11905)

**FedMID: 連合学習における中間出力を使用したデータフリーな防御メカニズム**

Sungwon Han, Hyeonho Song, Sungwon Park, Meeyoung Cha

- 連合学習では、参加者のローカルなアップデートを組合せることでグローバルモデルを作成するが、これが毒物攻撃の影響を受けやすい
- 従来の防御戦略はユークリッド空間上の投影によるベクトルに依存していたが、これはローカルモデルの機能性や構造を正確に表現できず、パフォーマンスに不整合が生じていた
- 新たに提案されたFedMIDは、中間出力に基づいたローカルモデルの機能マッピングを使用して毒物攻撃に対抗
- この防御メカニズムは様々な計算条件と高度な攻撃シナリオ下での堅牢性を示し、データに敏感な参加者間の安全な協力を可能にする



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-04-18 05:10

- - -

### [FCNCP: A Coupled Nonnegative CANDECOMP/PARAFAC Decomposition Based on Federated Learning](http://arxiv.org/abs/2404.11890)

**FCNCP: 脳科学データのための連合学習に基づく非負結合テンソル分解**

Yukai Cai, Hang Liu, Xiulin Wang, Hongjin Li, Ziyi Wang, Chuanshuai Yang, Fengyu Cong

- 脳科学において、プライバシーの問題や行政手続きの規制などにより、サーバー間でのデータ共有が困難になっている
- 新たに提案されたFCNCPアルゴリズムは、連合学習を用いて異なるサーバー上のデータ間での結合制約を確立し、高次元データの分析と処理を可能にする
- シミュレーション実験により、FCNCPアルゴリズムが安定かつ一貫した分解結果をもたらすことが確認された
- FCNCPを用いて収集されたERPテンソルデータの分析結果は、認知神経科学の関連研究と一致し、重要な隠れた情報の保存が可能であることが示された



**トピック:** [連合学習](fl), **カテゴリ:** math.NA, cs.LG, cs.NA, **投稿日時:** 2024-04-18 04:30

- - -

### [The Dog Walking Theory: Rethinking Convergence in Federated Learning](http://arxiv.org/abs/2404.11888)

**連合学環境における収束に関する新理論：ドッグウォーキング理論**

Kun Zhai, Yifeng Gao, Xingjun Ma, Difan Zou, Guangnan Ye, Yu-Gang Jiang

- 連合学習は多様なクライアントがプライベートデータを共有せずにグローバルモデルを訓練する手法であるが、非独立同分布（non-IID）データにおいて収束問題を抱えている
- ドッグウォーキング理論は、公園を横切りながら複数の犬を散歩させるドッグウォーカーのプロセスを連合学習にたとえ、クライアントの探索を導く「リーシュ（リード）」の概念を提案
- 新しい連合学習アルゴリズム「FedWalk」が提案され、サーバー側で簡単に収束するタスクを用いてクライアントのローカルトレーニングをガイドする
- 実験結果から、FedWalkは独立同分布（IID）および非独立同分布（non-IID）データにおいて最先端の連合学習手法よりも優れていることが示された



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-18 04:25

- - -

### [Cross-model Mutual Learning for Exemplar-based Medical Image Segmentation](http://arxiv.org/abs/2404.11812)

**医用画像のセグメンテーションのためのクロスモデル相互学習**

Qing En, Yuhong Guo

- 医用画像セグメンテーションには通常、密度の高いアノテーションが必要だが、この作業は時間がかかり専門技術が必要
- CMEMSフレームワークは、異なる粒度でのモデル間の一貫性を強化することで、補完情報の学習を促進
- 弱い摂動と強い摂動が加えられた画像を用いて、高信頼度の擬似ラベルを生成し、モデル間で予測を監督
- 実験結果から、限定的な教師ありデータを用いても、CMEMSは最先端のセグメンテーション手法より優れた性能を示した

**Comment:** AISTATS 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-04-18 00:18

- - -

### [Improved Generalization Bounds for Communication Efficient Federated Learning](http://arxiv.org/abs/2404.11754)

**通信効率の良い連合学習のための一般化境界の改善**

Peyman Gholami, Hulya Seferoglu

- ローカルクライアントの一般化とデータ分布の異質性を考慮して、ワンラウンド連合学習のためのより厳密な一般化境界を示した
- Rラウンド連合学習での一般化境界とローカル更新（ローカルSGDs）の数との関係を特定
- 一般化境界と表現学習解析を基に、特に非iidシナリオで、より一般化可能なモデルの構築に向けて、集約の頻度を減らすことが効果的であることを示した
- 一般化境界と表現学習解析に基づく新しいアルゴリズム「FedALS（連合学習と適応的ローカルステップ）」を設計し、モデルの異なる部分に異なる集約頻度を適用して通信コストを削減



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-17 21:17

- - -

### [A Secure and Trustworthy Network Architecture for Federated Learning Healthcare Applications](http://arxiv.org/abs/2404.11698)

**連合学習（FL）を用いた医療用アプリケーションのための安全で信頼性のあるネットワークアーキテクチャ**

Antonio Boiano, Marco Di Gennaro, Luca Barbieri, Michele Carminati, Monica Nicoli, Alessandro Redondi, Stefano Savazzi, Albert Sund Aillet, Diogo Reis Santos, Luigi Serio

- 連合学習は、医療などのプライバシーが重視される分野で有望な手法として登場
- TRUSTrokeプロジェクトは、脳梗塞の予測を支援するためにFLを使用
- 提案されたアーキテクチャは、中央パラメータサーバーを持つクライアント-サーバーモデルを採用し、臨床環境でのFLプロセスの実装に柔軟なソリューションを提供するDockerベースのデザインを導入
- 通信プロトコル（HTTPまたはMQTT）の違いがFLネットワークの運用に与える影響を分析し、FLシナリオに適しているためMQTTが選ばれた



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, cs.DC, **投稿日時:** 2024-04-17 18:55
