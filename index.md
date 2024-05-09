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

更新: 2024-05-09T04:23:24.696619

- - -

### [SPIDER: Improved Succinct Rank and Select Performance](http://arxiv.org/abs/2405.05214)

**SPIDER: 簡潔なランクおよびセレクトパフォーマンスの向上**

Matthew D. Laws, Jocelyn Bliven, Kit Conklin, Elyes Laalai, Samuel McCauley, Zach S. Sturdevant

- SPIDERは簡潔なデータ構造で、オリジナルのビットベクトルよりも大幅に小さな空間（3.82%の追加スペース）を使用する
- ランククエリにおいて、従来の少ないスペースを使うデータ構造よりも高速で、8億ビット以上のデータセットで最高の性能を示す
- セレクトクエリでは、線形スキャンのコストをほぼ排除する予測使用により、4%未満のスペースを使用する他のデータ構造よりも性能が優れる
- 実データと合成データの両方で効果的であることが示されており、キャッシュ効率を改善するためにメタデータをビットベクトルと交互に配置する技術を導入している



**トピック:** [合成データ](sd), **カテゴリ:** cs.DS, **投稿日時:** 2024-05-08 17:06

- - -

### [SCALA: Split Federated Learning with Concatenated Activations and Logit Adjustments](http://arxiv.org/abs/2405.04875)

**SCALA: 連合学習における分割学習方式に基づく連結活性化とロジット調整**

Jiarong Yang, Yuan Liu

- 分割連合学習(SFL)は、学習プロセスをサーバーとクライアント間で分割し、ローカルモデルを集約して共有モデルを訓練する分散機械学習フレームワーク
- データの不均一性と部分的なクライアント参加により、ラベル配分の偏りが生じ、学習性能が低下
- 提案されたSCALAは、クライアント側モデルの活性化を連結し、サーバー側モデルの入力として利用することで、異なるクライアント間のラベル配分を中央で調整
- SCALAによるロジット調整は、参加するクライアントのサブセット間でのラベル配分の変動を扱うために、サーバー側とクライアント側の両方のモデルで損失関数を調整



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-08 08:12

- - -

### [Federated Adaptation for Foundation Model-based Recommendations](http://arxiv.org/abs/2405.04840)

**連合適応によるファンデーションモデルベースの推薦システム**

Chunxu Zhang, Guodong Long, Hongkuan Guo, Xiao Fang, Yang Song, Zhaojie Liu, Guorui Zhou, Zijian Zhang, Yang Liu, Bo Yang

- ファンデーションモデルを推薦システムに適用することで、ユーザーの嗜好の変化をタイムリーかつプライバシーを保ちながら捉える新たな課題に対応
- 新たな連合適応メカニズムを提案し、プライバシーを保ちつつファンデーションモデルベースの推薦システムを強化
- 各クライアントがプライベートデータを使用して軽量の個人化アダプタを学習し、事前訓練されたファンデーションモデルと共同で効率的な推薦サービスを提供
- ベンチマークデータセット4つで実験を行った結果、提案方法の優れた性能が確認され、再現性を容易にする実装コードも提供

**Comment:** Accepted as a regular paper of IJCAI'24

**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, **投稿日時:** 2024-05-08 06:27

- - -

### [Teacher-Student Network for Real-World Face Super-Resolution with Progressive Embedding of Edge Information](http://arxiv.org/abs/2405.04778)

**実世界の顔画像超解像のためのエッジ情報進行埋込みを持つティーチャースチューデントネットワーク**

Zhilei Liu, Chenggong Zhang

- 従来の顔画像超解像（FSR）手法は、合成データセットでの訓練が実世界の顔画像への一般化能力を低下させている
- ティーチャースチューデントモデルが提案され、合成データと実データのドメインギャップを考慮
- 再帰ネットワークの中間出力を使用して、段階的に異なるエッジ情報を導入
- 提案手法は、広範な実験を通じて実世界のFSRにおいて高品質な顔画像を得るための最先端の手法を上回ることが示された

**Comment:** Accepted by ICIP 2023

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-05-08 02:48

- - -

### [When Foresight Pruning Meets Zeroth-Order Optimization: Efficient Federated Learning for Low-Memory Devices](http://arxiv.org/abs/2405.04765)

**連合学習における予視プルーニング法とゼロ次最適化の融合**

Pengyu Zhang, Yingjie Liu, Yingbo Zhou, Xiao Du, Xian Wei, Ting Wang, Mingsong Chen

- 連合学習はAIoT設計において協力的な学習を可能にするが、低メモリデバイスでは通常のメモリ使用量が多すぎる
- ニューラルタンジェントカーネル(NTK)に基づく予視プルーニング法を提案し、バックプロパゲーションフリーの連合学習フレームワークと統合
- この方法は、特にデータの不均一性が激しい状況で推測エラーを大幅に削減する
- 実際のテストとシミュレーションによる試験結果から、提案手法は最大9倍のメモリ削減を達成し、計算負荷も大幅に減少させることが確認された



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-08 02:24

- - -

### [Fast Decentralized Gradient Tracking for Federated Minimax Optimization with Local Updates](http://arxiv.org/abs/2405.04566)

**連合学習における高速分散逆行追跡**

Chris Junchi Li

- 連合学習でのミニマックス最適化に、新たな分散最適化アルゴリズムであるK-GT-Minimaxを提案
- ローカルアップデートと勾配追跡技術を組み合わせることで通信効率と収束率を向上
- 従来の方法に比べて優れた収束速度を実証
- データの異質性に対応し、モデルの堅牢性を保証することで連合学習の進展に貢献



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, stat.ML, **投稿日時:** 2024-05-07 17:25

- - -

### [Differentially Private Synthetic Data with Private Density Estimation](http://arxiv.org/abs/2405.04554)

**差分プライバシーを用いた合成データとプライベート密度推定**

Nikolija Bojkovic, Po-Ling Loh

- 個人情報が敏感なデータ（医療記録や金融データなど）の分析には、差分プライバシーの枠組みを採用している
- Boedihardjoらの研究を基に、プライバシーを保持した合成データを生成する新たな最適化ベースのアルゴリズムを開発
- 均一サンプリングステップをプライベート分布推定器に置き換えることにより、離散分布に対してより良い計算保証を得ている
- 連続分布に適した新しいアルゴリズムを開発し、いくつかの統計的タスクへの応用を探求している

**Comment:** Accepted to ISIT 2024

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.IT, cs.LG, math.IT, math.ST, stat.ML, stat.TH, 62G07, **投稿日時:** 2024-05-06 14:06

- - -

### [Differentially Private Federated Learning without Noise Addition: When is it Possible?](http://arxiv.org/abs/2405.04551)

**連合学習における差分プライバシーの達成方法に関する研究**

Jiang Zhang, Yahya H Ezzeldin, Ahmed Roushdy Elkordy, Konstantinos Psounis, Salman Avestimehr

- 連合学習とセキュア集約を用いた際、個々の暗号化されたモデル更新からユーザーデータに関する情報の漏洩を防ぐことに注目が集まっている
- 既存の研究は平均的なプライバシー漏洩を測るが、最悪のケースのプライバシー保証が提供されていない
- セキュア集約が追加のノイズなしで差分プライバシーを提供するための必要条件を特定し、それが成立するときは内部の乱数がガウス分布と非特異共分散行列を持つ場合であることを証明
- 実際にはこれらの条件が成立しにくいため、モデル更新に追加ノイズが必要であるが、集約モデル更新内の固有のランダムネスを利用して必要な追加ノイズ量を減少させる可能性についても議論



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-05-06 03:19

- - -

### [Enhancing Deep Knowledge Tracing via Diffusion Models for Personalized Adaptive Learning](http://arxiv.org/abs/2405.05134)

**個別適応型学習のための深層知識追跡の強化に関する研究**

Ming Kuo, Shouvon Sarker, Lijun Qian, Yujian Fu, Xiangfang Li, Xishuang Dong

- 個別適応型学習（PAL）は、生徒の進捗を密に監視し、それぞれの知識とニーズに合わせた学習経路を設計する
- 知識追跡は生徒の知識の進化をモデル化し、将来のパフォーマンスを予測することが重要
- この研究では、データ不足の問題を解決するために、TabDDPMという拡散モデルを用いて教育記録の合成データを生成してDKTのパフォーマンスを向上
- 実験結果は、特に訓練データが少なくテストデータが多いシナリオにおいて、TabDDPMによる合成データがDKTのパフォーマンスを大幅に改善することを示した



**トピック:** [合成データ](sd), **カテゴリ:** cs.CY, cs.AI, cs.LG, **投稿日時:** 2024-04-25 00:23

- - -

### [Distributed Learning for Wi-Fi AP Load Prediction](http://arxiv.org/abs/2405.05140)

**Wi-Fi AP負荷予測のための分散学習**

Dariush Salami, Francesc Wilhelmi, Lorenzo Galati-Giordano, Mika Kasslin

- 多数の独立した展開間の相互作用を支えるために、分散マシンラーニング（ML）が利用された
- 分散学習の主要な形態である連合学習（FL）と知識蒸留（KD）をWi-Fiアクセスポイント（AP）負荷予測に応用
- 大規模Wi-Fiキャンパスネットワークの実測データセットを使用して、異なる戦略に基づいてMLモデルを学習
- 分散学習により、予測精度を最大93％向上させつつ、通信コストとエネルギー消費を約80％削減可能であることが示された



**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.AI, cs.LG, **投稿日時:** 2024-04-22 16:37
