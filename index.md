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

更新: 2024-05-11T04:18:08.493056

- - -

### [Age Aware Scheduling for Differentially-Private Federated Learning](http://arxiv.org/abs/2405.05962)

**年齢認識スケジューリングによる差分プライバシーを持つ連合学習**

Kuan-Yu Lin, Hsuan-Yin Lin, Yu-Pin Hsu, Yu-Chih Huang

- 時間変動データベースを対象に差分プライバシーを備えた連合学習（FL）を探求、年齢、精度、差分プライバシーの三方向トレードオフを詳細に検討
- スケジューリングの利点を強調し、差分プライバシー要件を満たしつつ、集約モデルと非DP制約のモデルとの損失差を最小限に抑える最適化問題を提案
- 年齢依存の損失上限を導入し、年齢認識スケジューリング設計の開発を促進
- 提案スキームは従来のスケジューリングを考慮しない差分プライバシーを用いたFLに比べて優れたパフォーマンスを示すことがシミュレーション結果で強調

**Comment:** "Paper accepted to the 2024 IEEE International Symposium on   Information Theory (ISIT)"

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.IT, cs.LO, math.IT, **投稿日時:** 2024-05-09 17:58

- - -

### [Federated Combinatorial Multi-Agent Multi-Armed Bandits](http://arxiv.org/abs/2405.05950)

**連合学習による組合せ型マルチエージェントマルチアームドバンディット**

Fares Fourati, Mohamed-Slim Alouini, Vaneet Aggarwal

- 連合学習フレームワークをオンラインの組み合わせ最適化に適用し、バンディットフィードバックを用いる
- エージェントは個々のアーム情報にアクセスせず、アームのサブセットからノイズのある報酬を観測し、特定の間隔で情報共有が可能
- オフラインの強固な単一エージェント近似アルゴリズムを、オンラインのマルチエージェントアルゴリズムに変換し、エージェント数が増えると線形に速く学習することを示す
- 提案フレームワークは通信効率が高く、オンライン確率的部分モジュラー最大化にも成功しており、実験を通じてデータ要約問題での有効性を検証



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DM, cs.MA, stat.ML, **投稿日時:** 2024-05-09 17:40

- - -

### [Selecting the Most Conflicting Pair of Candidates](http://arxiv.org/abs/2405.05870)

**選委会選挙における最も対立する候補者ペアの選択**

Théo Delemazure, Łukasz Janeczko, Andrzej Kaczmarczyk, Stanisław Szufa

- 委員会選挙を観点から、最も対立が激しい候補者（投票者の好みに基づく）を特定する
- 主要な多数決ルールが基本的な公理を満たしていないことを示す
- 提案した対立的投票規則に適合する新しい委員会投票ルールを設計
- 実際のデータと合成データの両方において理論的研究を実験で支持

**Comment:** Accepted for publication at IJCAI-24; 27 pages; 11 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.GT, cs.AI, cs.MA, **投稿日時:** 2024-05-09 16:00

- - -

### [Compressed Bayesian Federated Learning for Reliable Passive Radio Sensing in Industrial IoT](http://arxiv.org/abs/2405.05855)

**産業用IoTにおける信頼性の高い受動型無線センサリングのための圧縮ベイジアン連合学習**

Luca Barbieri, Stefano Savazzi, Monica Nicoli

- ベイジアン連合学習は、予測の不確実性を定量化する調整済み機械学習モデルを提供する
- 提案手法は通信効率を向上させるために圧縮ポリシーを統合し、複数の最適化ステップを実行した後に局所後分布を送信
- 工業用IoTでの使用例では、ロボットと共有された職場で人間オペレーターを信頼性高く位置特定する
- 数値結果は、提案手法が通信オーバーヘッドを最大99%削減しながら高精度かつ調整済みのモデルを実現していることを示す

**Comment:** accepted for presentation at IEEE Conference on Artificial   Intelligence 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-09 15:44

- - -

### [Private Online Community Detection for Censored Block Models](http://arxiv.org/abs/2405.05724)

**センサード・ブロックモデルを用いたプライベートオンラインコミュニティ検出**

Mohamed Seif, Liyan Xie, Andrea J. Goldsmith, H. Vincent Poor

- 動的なコミュニティのためのプライベートオンライン変更検出問題に焦点を当て、エッジ差分プライバシーを使用しています
- プライバシー予算、検出遅延、コミュニティラベルの正確な回復との間の基本的なトレードオフを理解することを目指しています
- プライベートな変更検出の遅延に関する理論的な下限を確立し、ユーザープライバシーを維持しながらコミュニティ構造の変化を識別できるアルゴリズムを提案します
- エッジ差分プライバシーの下での変更検出と正確な回復に必要十分条件を示し、提案方法の効果について理論的保証を提供します



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.SI, cs.CR, cs.IT, math.IT, **投稿日時:** 2024-05-09 12:35

- - -

### [Privacy-Preserving Edge Federated Learning for Intelligent Mobile-Health Systems](http://arxiv.org/abs/2405.05611)

**プライバシーを保護するエッジ連合学習による知能型モバイルヘルスシステム**

Amin Aminifar, Matin Shokri, Amir Aminifar

- 連合学習は、ローカルに保持されたデータサンプルを共有せずに、複数の参加者間でMLモデルをトレーニングする手法である
- プライバシーを保護しながら、エッジIoTシステム（例えば、モバイルヘルスやウェアラブル技術）上での学習を実現することは、リソースの制約が非常に厳しいため、主要な課題となっている
- 提案されたフレームワークは、計算能力、通信帯域、メモリストレージ、バッテリー寿命が限られたモバイルヘルスおよびウェアラブル技術に対応している
- 実装はAmazonのAWSクラウドプラットフォームを用いて行われ、ウェアラブル技術を使用したてんかんモニタリングの発作検出アプリケーションでの評価が提供されている



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-09 08:15

- - -

### [Intelligent EC Rearview Mirror: Enhancing Driver Safety with Dynamic Glare Mitigation via Cloud Edge Collaboration](http://arxiv.org/abs/2405.05579)

**クラウドエッジコラボレーションを活用したインテリジェントECバックミラー：ダイナミックなグレア軽減によるドライバーの安全性向上**

Junyi Yang, Zefei Xu, Huayi Lai, Hongjian Chen, Sifan Kong, Yutong Wu, Huan Yang

- 従来のアンチグレア技術の問題点を克服するため、新しい全液体電気泳色技術を用いたインテリジェントなバックミラーシステムを導入
- IoTと連合学習を組み合わせ、クラウドエッジ協力フレームワーク内で電圧を動的に制御し、グレアを効果的に除去する
- アンサンブル学習モデルを利用し、光の強度に基づいてミラーの透過率を自動調整し、テストセットで低いRMSE 0.109を達成
- フェデレート学習を活用してデバイス間でデータの分散訓練を行い、プライバシーを向上させながらクラウドモデルを継続的に更新



**トピック:** [連合学習](fl), **カテゴリ:** cs.HC, cs.SY, eess.SY, **投稿日時:** 2024-05-09 07:10

- - -

### [Inference With Combining Rules From Multiple Differentially Private Synthetic Datasets](http://arxiv.org/abs/2405.04769)

**複数の差分プライバシー合成データセットからの推定における統合ルール**

Leila Nombo, Anne-Sophie Charest

- 差分プライバシー（DP）は、機密データから統計データや合成データセットを取得するために使用されるランダムなメカニズムによるプライバシー保護を測定する厳格な基準として認められている
- 差分プライバシー合成（DIPS）データセットからの統計的推論を適切に実行する方法はまだ十分に調査されていない
- 合成データ生成の変動性と通常のサンプリング変動性を考慮することが分析上の課題
- 統合ルールを基にした手法は、一部の文脈で正確な推論を提供する可能性があるが、全てのケースで有効とは限らない



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** stat.ME, cs.CR, cs.LG, stat.AP, **投稿日時:** 2024-05-08 02:33
