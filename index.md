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

更新: 2024-04-25T04:19:14.472927

- - -

### [PoisonedFL: Model Poisoning Attacks to Federated Learning via Multi-Round Consistency](http://arxiv.org/abs/2404.15611)

**連合学習における多ラウンド一貫性を利用したモデル毒攻撃: PoisonedFL**

Yueqi Xie, Minghong Fang, Neil Zhenqiang Gong

- 既存のモデル毒攻撃は、防御策が施された場合の効果が限定的であり、モデル更新やクライアントの訓練データの知識が必要であった
- PoisonedFLは、悪意のあるクライアント間で複数ラウンドに渡る一貫したモデル更新を行い、正規クライアントに関する知識は不要
- PoisonedFLは、最先端の8つの防御策を突破し、他の7つのモデル毒攻撃よりも優れた性能を示した
- この研究は、連合学習システムのロバスト性が従来考えられていたよりも低いことを示し、新たな防御機構の開発の必要性を強調している



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-04-24 03:02

- - -

### [Federated Learning with Only Positive Labels by Exploring Label Correlations](http://arxiv.org/abs/2404.15598)

**連合学習におけるポジティブラベルのみを用いたラベル相関の探索**

Xuming An, Dui Wang, Li Shen, Yong Luo, Han Hu, Bo Du, Yonggang Wen, Dacheng Tao

- 連合学習は複数ユーザーのデータをプライバシーを保持しながら共同でモデル学習を行うものである
- クライアントが単一クラスラベルに対してのみポジティブなデータを提供する場合には、通常のアプローチでは性能が落ちる
- 本研究では、クラスの埋め込み学習においてラベル間の相関を推定し、モデル訓練を改善する新しい方法（FedALC）を提案
- 通信の負担を減らし、安全性を向上させるため、サーバーとクライアント間でのクラス埋め込みの交換を一度きりに制限するバリアントを導入

**Comment:** To be published in IEEE Transactions on Neural Networks and Learning   Systems

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-04-24 02:22

- - -

### [Brain Storm Optimization Based Swarm Learning for Diabetic Retinopathy Image Classification](http://arxiv.org/abs/2404.15585)

**脳嵐最適化とスワーム学習を活用した糖尿病網膜症画像分類**

Liang Qu, Cunze Wang, Yuhui Shi

- 医療分野のデータプライバシーを保持しつつ、モデルの有用性を維持するために連合学習が用いられる
- スワーム学習はブロックチェーン技術を用いてサーバーなしでクライアント間のパラメータを直接交換
- 従来のスワーム学習の課題である計算負荷を解決するために脳嵐最適化アルゴリズムを統合
- 提案手法は糖尿病網膜症の画像分類データセットでの実験を通じて有効性が検証された



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, eess.IV, **投稿日時:** 2024-04-24 01:37

- - -

### [FedGreen: Carbon-aware Federated Learning with Model Size Adaptation](http://arxiv.org/abs/2404.15503)

**FedGreen: モデルサイズ適応によるカーボン意識型連合学習**

Ali Abbasi, Fan Dong, Xin Wang, Henry Leung, Jiayu Zhou, Steve Drew

- FL（連合学習）は、クライアントが分散している状態でもモデルを構築できる協力的なフレームワークとして提供されており、本研究ではFLプロセスのカーボン排出量を調査
- 地理的な位置や使用する電力源の違いによって、異なるカーボンフットプリントを示す可能性があり、適応的な計算と通信によってローカルモデルを訓練することでカーボン排出量を削減する機会が提供される
- FedGreenというカーボン意識型のFLアプローチを提案し、Ordered Dropoutというモデル圧縮技術を用いて、クライアントのカーボンプロファイルと位置に基づいて適応的なモデルサイズを共有することで効率的なモデル訓練を行う
- 実践的な研究により、FedGreenは最新の技術と比較してFLのカーボンフットプリントを大幅に削減できることが示され、同時に競争力のあるモデル精度を維持している



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-04-23 20:37

- - -

### [FL-TAC: Enhanced Fine-Tuning in Federated Learning via Low-Rank, Task-Specific Adapter Clustering](http://arxiv.org/abs/2404.15384)

**FL-TAC: 連合学習による低ランク・タスク特有アダプタクラスタリングを用いたファインチューニングの拡張**

Siqi Ping, Yuzhu Mao, Yang Liu, Xiao-Ping Zhang, Wenbo Ding

- ファインチューニングにおける高品質なタスク特有データの収集が困難であるため、大規模事前学習モデルの性能が限定されている
- 連合学習は、大規模クライアント間でのファインチューニングを可能にするが、事前学習モデルの大きさにより通信コストが問題となっている
- 本研究では、クライアント側で各タスクに対して低ランクアダプタを学習し、類似のアダプタ群をサーバー側でクラスタリングすることでタスク特有アグリゲーションを達成
- GLUEやCIFAR-10/100など、様々な言語・視覚タスクにおいて広範な実験を実施し、FLトレーニングプロセスを通じたタスク特有アダプタの進化を明らかにし、低ランクのタスク特有アダプタクラスタリング方法の有効性を確認



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-23 10:50

- - -

### [Advances and Open Challenges in Federated Learning with Foundation Models](http://arxiv.org/abs/2404.15381)

**連合学習と基盤モデルの進展と課題**

Chao Ren, Han Yu, Hongyi Peng, Xiaoli Tang, Anran Li, Yulan Gao, Alysa Ziying Tan, Bo Zhao, Xiaoxiao Li, Zengxiang Li, Qiang Yang

- 連合学習（FL）と基盤モデル（FMs）を組み合わせることで、AIのプライバシー保護、データの分散化、計算効率が向上
- 連合基盤モデル（FedFM）の新たな方法論、課題、未来の方向性について詳述し、多段階の分類法を提案
- 計算の複雑性、プライバシー、貢献評価、通信効率という主要な課題を深掘り
- 量子コンピューティングが訓練、推論、最適化、データ暗号化プロセスの革新に寄与する可能性を強調

**Comment:** Survey of Federated Foundation Models (FedFM)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-23 09:44
