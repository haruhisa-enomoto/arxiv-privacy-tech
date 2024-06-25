---
layout: single
classes: wide
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

更新: 2024-06-25T04:19:10.411730

- - -

### [From Perfect to Noisy World Simulation: Customizable Embodied Multi-modal Perturbations for SLAM Robustness Benchmarking](http://arxiv.org/abs/2406.16850)

**完璧からノイズの世界シミュレーションへ: SLAMのロバスト性ベンチマークのためのカスタマイズ可能な具現化マルチモーダル摂動**

Xiaohao Xu, Tianyi Zhang, Sibo Wang, Xiang Li, Yongqi Chen, Ye Li, Bhiksha Raj, Matthew Johnson-Roberson, Xiaonan Huang

- SLAMモデルのロバスト性が具現化エージェントの自律性に重要である
- 制御可能なノイズの多い世界の作成が課題である
- 新たなカスタマイズ可能なパイプラインでノイズデータを合成
- 高度なSLAMモデルの耐性を評価するためのNoisy-Replicaベンチマークを提案

シミュレーションを活用して、SLAMモデルがどの程度のノイズや摂動に耐えられるかを評価するのって面白そう！これからのロボティクスの進展に役立ちそうだよね。

**Comment:** 50 pages. arXiv admin note: substantial text overlap with   arXiv:2402.08125

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.RO, **投稿日時:** 2024-06-24 17:57

- - -

### [Exploring Factual Entailment with NLI: A News Media Study](http://arxiv.org/abs/2406.16842)

**ニュースメディア研究における事実含意とNLIの探求**

Guy Mor-Lan, Effi Levi

- FactRelという新たなアノテーションスキームを導入し、事実的含意をモデル化
- データセット分析では、84%がNLIの含意に、63%が矛盾にならない
- 合成データ生成でモデル性能が向上、特にGPT-4の少数ショット学習が優秀
- このタスクは世界知識と高度な推論能力に依存していると仮定

ニュースメディアの文章をこんな風に分析するのっておもしろいよね。少数ショット学習で結果が変わるところが未来が感じられるな。

**Comment:** Presented at *SEM 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-24 17:47

- - -

### [Personalized federated learning based on feature fusion](http://arxiv.org/abs/2406.16583)

**特徴融合に基づくパーソナライズド連合学習**

Wolong Xing, Zhenkui Shi, Hongyan Peng, Xiantao Hu, Xianxian Li

- 連合学習はデータをローカルに保存したまま、分散クライアントが協力してトレーニングできる
- データやデバイスの異質性により、最終的なグローバルモデルの性能が低下する可能性
- 特徴アップロードにより通信コストを削減し、異質なクライアントモデルを許容
- 適切なハイパーパラメータ設定で、複数のデータセットで他のFL手法を上回る性能を実現

データの異質性に着目して新しいアプローチを提案するなんて、めっちゃ面白い！通信コストの削減もできるから、もっと応用されそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-06-24 12:16

- - -

### [Exploring Cross-Domain Few-Shot Classification via Frequency-Aware Prompting](http://arxiv.org/abs/2406.16422)

**周波数認識プロンプトによるクロスドメイン小ショット分類の探求**

Tiange Zhang, Qing Cai, Feng Gao, Lin Qi, Junyu Dong

- クロスドメインの小ショット学習において、メタ学習の進展により大きな進歩を遂げた
- 多くの既存手法は高周波成分に依存する傾向があり、そのためノイズに弱くロバスト性が低下する
- 周波数認識プロンプト法を提案し、新しい認識タスクにおいて人間の視覚をシミュレーション
- 提案手法は既存のCD-FSL手法にも適用可能で、効果的かつ性能向上を実証

新しい手法のロバスト性を向上させるところが面白そう！メタ学習の進展と組み合わせて、どんな新しい応用が見つかるかな？



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-06-24 08:14

- - -

### [On Computing Pairwise Statistics with Local Differential Privacy](http://arxiv.org/abs/2406.16305)

**局所差分プライバシーを用いたペア統計の計算について**

Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Adam Sealfon

- ペア統計の計算問題研究、局所モデルでの差分プライバシー利用
- 重要なメトリクス（ケンドールのτ係数、AUC、ジニ係数など）を計算
- 差分プライバシーアルゴリズムの技術を活用し、斬新で汎用的なアルゴリズムを提案
- 線形クエリのDPアルゴリズム技術を利用してペア統計を計算

ペア統計を局所差分プライバシーで計算する方法がすごく気になった！この技術が広まれば更にプライバシー守りつつデータ解析できそうだよね。

**Comment:** Published in NeurIPS 2023

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, **投稿日時:** 2024-06-24 04:06

- - -

### [Semi-Variance Reduction for Fair Federated Learning](http://arxiv.org/abs/2406.16193)

**フェアな連合学習のためのセミバリアンス削減**

Saber Malekmohammadi

- フェアネスを追求する連合学習（FL）は、異なるクライアントの公平な性能を確保する点で重要
- 既存のFLアルゴリズムは、最悪の性能を持つクライアントの損失関数を重視し、全体の平均性能を犠牲にすることが多い
- 提案手法のSemiVRedは、平均損失からの最悪のクライアントの損失関数の差異を減らす
- 実験で、異質なデータ分布下でフェアネスと全体平均性能を改善することを示した

いろんなデータセットで試してバランスを取るなんて、すごい興味が湧くよね！連合学習がどんどん進化していて、未来が楽しみだなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CY, **投稿日時:** 2024-06-23 19:14

- - -

### [Meta-FL: A Novel Meta-Learning Framework for Optimizing Heterogeneous Model Aggregation in Federated Learning](http://arxiv.org/abs/2406.16035)

**Meta-FL: 連合学習における異種モデル統合を最適化する新しいメタ学習フレームワーク**

Zahir Alsulaimawi

- 連合学習（FL）は、データプライバシーを保護しつつ協調的なモデル訓練を可能にする
- データの異質性とモデルの多様性はFLの主要な課題
- Meta-FLは最適化ベースのMeta-Aggregatorを使用して異種モデル更新の複雑さを解決
- 実証評価では、Meta-FLが従来のFL手法を上回る適応性、効率性、拡張性、および堅牢性を示した

新しいフレームワークがFLの課題をどう解決するかって興味深いよね！特に少ない通信回数で高精度を実現できるって、実用化につながりそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-23 06:57

- - -

### [Privacy Preserving Machine Learning for Electronic Health Records using Federated Learning and Differential Privacy](http://arxiv.org/abs/2406.15962)

**連合学習と差分プライバシーを用いた電子カルテのプライバシー保護機械学習**

Naif A. Ganadily, Han J. Xia

- 電子カルテは診断、治療、費用などの個人情報を含む
- 機械学習は患者データを分析し、ケアの改善に役立つ
- 社会保障番号や住所などの機密情報が含まれているため、プライバシー保護技術が必要
- 連合学習と差分プライバシーを用いて、これらの機械学習モデルのプライバシーを保護することが重要

プライバシー保護しながら医療データを活用できるってすごいよね。未来の医療がもっと効率的になる予感。

**Comment:** 5 pages, 12 figures

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.ET, **投稿日時:** 2024-06-23 00:01

- - -

### [Federated Adversarial Learning for Robust Autonomous Landing Runway Detection](http://arxiv.org/abs/2406.15925)

**ロバストな自律着陸滑走路検出のための連合敵対学習**

Yi Li, Plamen Angelov, Zhengxin Yu, Alvaro Lopez Pellicer, Neeraj Suri

- 自律着陸システムの深層学習技術発展のなかで、信頼性とセキュリティが主要な課題
- 連合敵対学習を用いたフレームワークを提案、クリーンなデータと敵対的データを組み合わせ
- 大規模な車線検出データセットで事前学習を行い、SSFによる効率的なパラメータ調整の手法を使用
- 著者の知る限り、連合学習で敵対サンプル問題に対処する初の試みであり、実験評価で高い性能を示す

自律着陸技術に連合学習を取り入れるなんてすごく面白そう！これでより安全に飛行機が降りられるようになるかもね。

**Comment:** ICANN2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-22 19:31

- - -

### [Credit Attribution and Stable Compression](http://arxiv.org/abs/2406.15916)

**クレジットの付与と安定した圧縮**

Roi Livni, Shay Moran, Kobbi Nissim, Chirag Pabbaraju

- クレジットの付与はさまざまな分野で重要で、生成モデルにも必要
- 差分プライバシーの緩和版を提案、特定のデータポイントに対する安定性保証を弱める
- 新しいフレームワークは既存の安定性概念を拡張、PAC学習の枠内でその表現力を検討
- アルゴリズムの学習可能性を包括的に特徴付け、今後の研究方向を提案

クレジットの付与を学習アルゴリズムで真剣に考えるなんて、面白い発想だよね。今後の応用が楽しみだな！

**Comment:** 15 pages, 1 figure

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-06-22 18:40

- - -

### [Automatic AI Model Selection for Wireless Systems: Online Learning via Digital Twinning](http://arxiv.org/abs/2406.15819)

**ワイヤレスシステムのための自動AIモデル選択: デジタルツインによるオンライン学習**

Qiushuo Hou, Matteo Zecchin, Sangwoo Park, Yunlong Cai, Guanding Yu, Kaushik Chowdhury, Osvaldo Simeone

- ワイヤレスネットワークでのAIアプリは、ネットワーク条件やトポロジーなどの文脈情報に基づき選択される
- 自動モデル選択（AMS）は文脈情報だけでゼロショットで行うことが理想
- AMSのオンライン最適化は、多くの異なる文脈から収集するデータが必要で難航
- デジタルツインのシミュレーションデータを用い、少量の実データでバイアスを補正する新手法を提案

AIがワイヤレスネットワークのパフォーマンスを自動で最適化するなんて、未来のネットワーク進化って感じでワクワクするよね！実システムでうまくいくかどうかのチャレンジが面白そう！

**Comment:** submitted for a journal publication

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.IT, cs.NI, eess.SP, math.IT, **投稿日時:** 2024-06-22 11:17

- - -

### [Intrinsic Dimension Correlation: uncovering nonlinear connections in multimodal representations](http://arxiv.org/abs/2406.15812)

**内在次元相関：多モーダル表現における非線形接続の解明**

Lorenzo Basile, Santiago Acevedo, Luca Bortolussi, Fabio Anselmi, Alex Rodriguez

- 機械学習のメカニズム理解にはデータ特徴間の接続が重要
- 標準的手法では捉えにくい高次元かつ非線形の相関を計測する指標を提案
- 合成データで方法を検証し、現存技術と比較した利点と欠点を明らかに
- 大規模なニューラルネットの多モーダルデータ表現に適用し、視覚とテキスト埋め込み間の相関を発見

高次元の中でも特に非線形な相関を見つける新方法って面白いよね！これでマルチモーダルの世界がさらに広がりそう⤴️



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CL, cs.CV, **投稿日時:** 2024-06-22 10:36

- - -

### [Split Federated Learning Empowered Vehicular Edge Intelligence: Adaptive Parellel Design and Future Directions](http://arxiv.org/abs/2406.15804)

**スプリット連合学習を活用した車載エッジインテリジェンス：適応型並列設計と将来の方向性**

Xianke Qiang, Zheng Chang, Chaoxiong Ye, Timo Hamalainen

- 車載ネットワークの知識をAIで掘り起こし、AI駆動サービスの品質を向上させる重要性
- 車載エッジインテリジェンス（VEI）は車両の計算、保存、通信資源を活用してAIモデルを訓練
- 伝統的な集中型学習はデータを中央サーバーへアップロードし、通信過負荷とプライバシーリスクが発生
- 分散機械学習方式であるスプリット連合学習（SFL）を提案し、その適応型並列設計と性能分析を実施

車とAIの融合って何か未来感がすごいよね！プライバシーも守られて安心だし、早くこの技術が普及してほしいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-06-22 10:15

- - -

### [Privacy Implications of Explainable AI in Data-Driven Systems](http://arxiv.org/abs/2406.15789)

**データ駆動システムにおける説明可能なAIのプライバシーへの影響**

Fatima Ezzeddine

- 機械学習モデルは強力だが、透明性の欠如が信頼を損なう
- 説明可能なAI（XAI）技術が内部決定プロセスを説明するフレームワークを提供
- データには敏感な情報が含まれ、差分プライバシーなどの技術が重要
- XAIとプライバシー保護技術は対立し、プライバシー侵害攻撃のリスクがある

データの透明性とプライバシーのバランスをどうとるかが超重要！未来のAIシステムがどう進化するか楽しみ～。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-06-22 08:51

- - -

### [Breaking Secure Aggregation: Label Leakage from Aggregated Gradients in Federated Learning](http://arxiv.org/abs/2406.15731)

**連合学習におけるラベル漏洩：集約された勾配からのプライバシー侵害**

Zhibo Wang, Zhiwei Chang, Jiahui Hu, Xiaoyi Pang, Jiacheng Du, Yongle Chen, Kui Ren

- 連合学習（FL）は勾配逆転攻撃（GIA）に対してプライバシー脆弱性を持つ
- セキュアアグリゲーション（SA）は、サーバーが個々の勾配を取得できないようにし、GIAに効果的に対抗する
- 本研究では、SAを無効化し個々のクライアントのラベルを回復するための攻撃手法（ラベル推論攻撃）を提案
- 実験により、この攻撃が様々なデータセットやモデルアーキテクチャで100%の精度でラベルを回復可能であることを示した

ラベルをこんなに簡単に抜き取るとはビックリ！連合学習の未来がちょっと心配になっちゃうけど、対策の進展も楽しみね。

**Comment:** 10 pages, conference to IEEE INFOCOM 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-06-22 04:42

- - -

### [GenSQL: A Probabilistic Programming System for Querying Generative Models of Database Tables](http://arxiv.org/abs/2406.15652)

**GenSQL: データベーステーブル生成モデルの問い合わせを可能にする確率的プログラムシステム**

Mathieu Huot, Matin Ghavami, Alexander K. Lew, Ulrich Schaechtle, Cameron E. Freer, Zane Shelby, Martin C. Rinard, Feras A. Saad, Vikash K. Mansinghka

- GenSQLは、SQLに少数のキー原語を追加し、確率モデルの問い合わせを可能にする
- 新しい型システムと意味論を用いて、GenSQLの健全性保証を証明
- 臨床試験の異常検出と仮想ウェットラボの条件付き合成データ生成において有効性を評価
- 主要な競合他社に比べて1.7～6.8倍の速度向上を実現し、手書きコードと同等の時間で実行

GenSQLは、確率モデルを用いたデータベースの問い合わせを簡潔にし、速度も向上させる点がすごく興味深いね。リアルなデータセットでの評価もされてるし、これからもっと注目されそう！

**Comment:** 54 pages, 30 figures, 1 table, published at PLDI 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.PL, **投稿日時:** 2024-06-21 21:09

- - -

### [Supersonic OT: Fast Unconditionally Secure Oblivious Transfer](http://arxiv.org/abs/2406.15529)

**Supersonic OT: 高速無条件安全なオブリビアストランスファー**

Aydin Abadi, Yvo Desmedt

- OTは安全なマルチパーティ計算、連合学習、プライベートセットインターセクションにおいて重要
- ポスト量子時代に向けて無条件安全なOTの開発が必要
- 既存のOTは計算仮定に依存しているが、「Supersonic OT」はこれを回避
- 単一インスタンスが0.35ミリ秒で完了し、最新技術の2000倍高速

量子コンピュータに耐えられる無条件安全な技術なんてすごくない？しかも2000倍も速いとか、とても未来が楽しみ！

**Comment:** arXiv admin note: text overlap with arXiv:2406.15063

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DB, cs.LG, **投稿日時:** 2024-06-21 11:50
