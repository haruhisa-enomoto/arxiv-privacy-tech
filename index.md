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

更新: 2024-05-06T04:21:04.856697

- - -

### [Secure and Efficient General Matrix Multiplication On Cloud Using Homomorphic Encryption](http://arxiv.org/abs/2405.02238)

**クラウド上での安全かつ効率的な一般行列積計算に関する準同型暗号の利用**

Yang Gao, Gang Quan, Soamar Homsi, Wujie Wen, Liqiang Wang

- クラウドコンピューティングにおけるセキュリティとプライバシーの懸念が高い
- 準同型暗号（HE）は暗号化されたデータ上で計算を可能にすることでプライバシーとセキュリティを保証
- HEベースの計算は高コストであるため、シングルインストラクションマルチプルデータ（SIMD）操作を利用して一般行列積の計算コストを削減
- 提案された新しいアルゴリズムは、既存のHEベースの行列積計算手法よりも大幅に性能が向上

**Comment:** 10 pages, 7 figures. 4 tables

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-03 16:50

- - -

### [An Information Theoretic Perspective on Conformal Prediction](http://arxiv.org/abs/2405.02140)

**情報理論の観点から見たコンフォーマル予測**

Alvaro H. C. Correia, Fabio Valerio Massoli, Christos Louizos, Arash Behboodi

- コンフォーマル予測（CP）は、ユーザー指定の確率で真の解を含む予測セットを構築する分布フリーの不確かさ推定フレームワークである
- 予測セットの大きさは不確かさの度合いを表し、セットが大きいほど不確かさが高い
- 情報理論を活用して、コンフォーマル予測と他の不確かさの概念を結び付け、条件付きエントロピーによって示される内在的不確かさを上限で評価する方法を三つ証明
- コンフォーマル予測と情報理論の接続による二つの直接的かつ有用な応用例を示し、集中学習および連合学習設定での実証実験を通じて結果の有効性を確認



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, math.IT, stat.ML, **投稿日時:** 2024-05-03 14:43

- - -

### [A Federated Learning Benchmark on Tabular Data: Comparing Tree-Based Models and Neural Networks](http://arxiv.org/abs/2405.02074)

**連合学習における表形式データのベンチマーク：木ベースモデルとニューラルネットワークの比較**

William Lindskog, Christian Prehofer

- 連合学習（FL）は、分散データセット上での機械学習モデルの訓練方法を扱っており、画像やテキストタスクにおいて有望とされている
- 表形式データに適用されるFLは少なくとも注目されているが、木ベースモデル（TBM）が表形式データにはより適していると考えられている
- 本研究では、10の主要な表形式データセットへの連合木ベースモデルとDNNのベンチマークを行い、連合TBMがDNNよりも優れていると示された
- 特に、連合XGBoostモデルが他のモデルを上回っており、クライアント数が増加しても連合TBMのパフォーマンスは向上している

**Comment:** 8 pages, 6 figures, 6 tables, FMEC 2023 (best paper)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-03 13:08

- - -

### [Histogram-Based Federated XGBoost using Minimal Variance Sampling for Federated Tabular Data](http://arxiv.org/abs/2405.02067)

**ヒストグラムベースの連合XGBoostにおける最小分散サンプリングを用いた連合表データの評価**

William Lindskog, Christian Prehofer, Sarandeep Singh

- 連合学習では表データに対する注目が少ないなか、XGBoostのような木ベースのモデルが効果的であることが示されている
- 訓練データのサブサンプリングがモデルのパフォーマンス向上に寄与するか未解決問題であったが、最小分散サンプリングを用いた連合XGBoostが有効であることを示す
- 最小分散サンプリングを用いることで、ランダムサンプリングや無サンプリングよりも精度と回帰エラーが改善される
- 提案モデルは連合データセットでのローカルおよびグローバルなパフォーマンスが優れ、一部のケースでは中央集権型XGBoostを上回る

**Comment:** 6 figures, 5 tables, 8 pages, FLTA 2023 (together with FMEC 2023)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-03 12:58

- - -

### [Federated Learning for Tabular Data using TabNet: A Vehicular Use-Case](http://arxiv.org/abs/2405.02060)

**連合学習を用いた車両ケーススタディのための表形式データ用TabNet**

William Lindskog, Christian Prehofer

- 道路上の障害物、不規則性、舗装の種類を分類する車両用途に連合学習(FL)を適用する方法を示す
- 提案フレームワークでは、表形式データのための最先端ニューラルネットワークであるTabNetと連合学習を組み合わせて使用
- TabNetを連合学習と統合する手法を初めて実演し、最大93.6%のテスト精度を達成
- データセットにとって連合学習が適切なコンセプトである理由を説明する

**Comment:** 7 pages, 9 figures, 1 table, ICCP Conference 2022

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-03 12:42

- - -

### [Quantifying Distribution Shifts and Uncertainties for Enhanced Model Robustness in Machine Learning Applications](http://arxiv.org/abs/2405.01978)

**機械学習アプリケーションにおけるモデル堅牢性を強化するための分布シフトと不確実性の定量化**

Vegard Flovik

- トレーニングとテストデータセット間での統計的特性の違い（分布シフト）は、モデルの一般化と堅牢性に直接影響を与える
- 合成データを用いて、異なるデータ分布にわたるモデル適応をシステマティックに評価
- Kullback-Leibler発散、Jensen-Shannon距離、マハラノビス距離を使用してデータの類似度を評価し、モデルの精度と予測の不確実性を定量化
- マハラノビス距離を活用して、モデル予測が低誤差の「内挿領域」か高誤差の「外挿領域」に属するかを判断する方法がモデルの不確実性と分布シフトを評価する補完的方法として提案された

**Comment:** Working paper

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-05-03 10:05

- - -

### [Real Risks of Fake Data: Synthetic Data, Diversity-Washing and Consent Circumvention](http://arxiv.org/abs/2405.01820)

**合成データのリアルなリスク：多様性の偽装と同意の回避**

Cedric Deslandes Whitney, Justin Norman

- 合成データを使用することで、データセットの多様性と表現を拡大しようとする際に高いリスクの偽信頼が生じる
- 顔認識技術の評価のために生成された合成データセットの事例を基にした詳細な分析を提供
- 合成データの使用がデータ利用における同意を回避するリスクを持つと示す
- 合成データは既存のガバナンスや倫理的実践を複雑にし、アルゴリズムによる影響を受ける人々から力を集約する傾向がある



**トピック:** [合成データ](sd), **カテゴリ:** cs.CY, cs.AI, cs.CV, **投稿日時:** 2024-05-03 02:47

- - -

### [Bike network planning in limited urban space](http://arxiv.org/abs/2405.01770)

**都市内限られた空間での自転車ネットワーク計画**

Nina Wiedemann, Christian Nöbel, Henry Martin, Lukas Ballo, Martin Raubal

- 都市環境で自転車インフラが不足すると、サステナブルで効率的かつ健康的な移動手段としての自転車通勤の採用が阻害される
- 自転車ネットワーク計画は繁雑であり、新規自転車インフラ導入時の車線再配置の重要性をしばしば見過ごす
- 新たな線形プログラミング方式を用いて最適な自転車ネットワーク配置を目指し、実世界及び合成データを用いた実験が効果を実証
- 提案フレームワークは自転車利用性と車のアクセシビリティ評価基準に適応可能で、都市計画における柔軟でスケーラブルなリソースを提供



**トピック:** [合成データ](sd), **カテゴリ:** math.OC, cs.CE, **投稿日時:** 2024-05-02 22:55

- - -

### [ATTAXONOMY: Unpacking Differential Privacy Guarantees Against Practical Adversaries](http://arxiv.org/abs/2405.01716)

**差分プライバシー保証の実際的な敵に対する解析: ATTAXONOMY**

Rachel Cummings, Shlomi Hod, Jayshree Sarathy, Marika Swanberg

- 差分プライバシー（DP）はプライバシー保護のために機械学習や統計分析でますます使用されているが、その技術的なパラメータは実世界のプライバシーリスクを直感的に説明するのに適していない
- 現実のデプロイメントを解析し、より有益なプライバシー攻撃の理論的限界を開発するための道筋として、攻撃の詳細な分類（タクソノミー）を提供
- イスラエル保健省の出生データセットのリリース事例を用いて、このタクソノミーを実用化し、詳細な脅威モデリングを可能にし、プライバシーパラメータの選択に向けての洞察を提供
- 従来の文獻で検討されていたものよりも現実的な攻撃手法を定義し、分布的不確実性を有する情報が少ない敵を想定し、DPの最悪の場合の保証を平均的ケースに拡張



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.CY, **投稿日時:** 2024-05-02 20:23

- - -

### [A deep causal inference model for fully-interpretable travel behaviour analysis](http://arxiv.org/abs/2405.01708)

**深層因果推論モデルによる完全に解釈可能な交通行動分析**

Kimia Kamal, Bilal Farooq

- 伝統的な交通行動モデルの因果推論能力に限界があるため、CAROLINAフレームワークが開発され、交通行動の因果関係を明示的にモデリング
- 因果推論、深層学習、伝統的な離散選択モデリングを統合して予測精度を向上し、解釈可能性を維持
- 仮想現実を使用した歩行者の横断行動やロンドンの実際の旅行データ、合成データを用いたケーススタディで、因果関係の明らか化、予測精度、政策介入の評価におけるモデルの有効性を実証
- 政策介入によって歩行者のストレスレベルが低下し待ち時間が短縮される個人が38.5%増加、ロンドンでの移動距離削減が持続可能な旅行モードの利用を47%増加させることを発見



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-02 20:06

- - -

### [Privacy-aware Berrut Approximated Coded Computing for Federated Learning](http://arxiv.org/abs/2405.01704)

**連合学習におけるプライバシー重視のBerrut近似符号化計算**

Xavier Martínez Luaña, Rebeca P. Díaz Redondo, Manuel Fernández Veiga

- 連合学習では、データ所有者間でAIモデルを共同で訓練しつつ、私的データセットを公開せずに行うことが可能
- 既存のプライバシー保護技術（差分プライバシー、準同型暗号、秘密計算）には非線形関数の取り扱いや大規模行列演算での問題点が存在
- Berrut近似符号化計算を秘密分散設定に適応させ、スケーラブルな入力プライバシーを連合学習で提供
- 提案手法は非線形関数計算や分散行列乗算（多くの自動学習タスクの核心）に対応可能で、様々な連合学習シナリオで利用可能



**トピック:** [連合学習](fl), [差分プライバシー](dp), [準同型暗号](he), **カテゴリ:** cs.LG, cs.CC, cs.DC, cs.IT, math.IT, **投稿日時:** 2024-05-02 20:03

- - -

### [1-Diffractor: Efficient and Utility-Preserving Text Obfuscation Leveraging Word-Level Metric Differential Privacy](http://arxiv.org/abs/2405.01678)

**1-Diffractor: 効率的で有用性を保持するテキスト難読化を実現する単語レベルのメトリック差分プライバシーの活用**

Stephen Meisenbacher, Maulik Chevli, Florian Matthes

- 自然言語処理(NLP)において、差分プライバシーの統合により革新的な方法が導入されている
- 従来の局所差分プライバシーに基づく単語ごとの摂動は、ノイズ追加による有用性の損失と計算コストの高さが問題であった
- 新メカニズム「1-Diffractor」は、以前のメカニズムと比較して高速化を実現しつつ、有用性とプライバシーの保持を維持
- 1-Diffractorは複数のNLPタスクでの有用性、プライバシーと効率性を評価し、既存のMLDPメカニズムに対して優れた成績を示している

**Comment:** 12 pages, 7 figures, 7 tables, 10th ACM International Workshop on   Security and Privacy Analytics (IWSPA 2024)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, **投稿日時:** 2024-05-02 19:07
