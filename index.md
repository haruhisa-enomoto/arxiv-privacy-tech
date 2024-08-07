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

更新: 2024-08-07T04:20:57.377471

- - -

### [Synthesizing Text-to-SQL Data from Weak and Strong LLMs](http://arxiv.org/abs/2408.03256)

**弱および強いLLMからのText-to-SQLデータの合成**

Jiaxi Yang, Binyuan Hui, Min Yang, Jian Yang, Junyang Lin, Chang Zhou

- オープンソースとクローズドソースの大規模言語モデル（LLM）間の能力格差が課題
- 強力なモデルが生成するデータと、弱いモデルのエラー情報データを組み合わせた合成データアプローチを提案
- 合成データアプローチを用いて、オープンソースLLMのインストラクションチューニングを行い、SENSEモデルを作成
- SPIDERおよびBIRDベンチマークで最先端の結果を示し、オープンソースモデルとクローズドソースモデル間の性能差を埋める

強いと弱いモデルを組み合わせて、新しい方法で性能向上を目指すのが面白いよね！結果もすごく良さそうだし、試してみる価値ありそうだなって思ったよ。

**Comment:** 12 pages, 7 figures, ACL 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-08-06 15:40

- - -

### [Masked Random Noise for Communication Efficient Federaetd Learning](http://arxiv.org/abs/2408.03220)

**通信効率の高い連合学習のためのマスク付きランダムノイズ**

Shiwei Li, Yingyi Cheng, Haozhao Wang, Xing Tang, Shijie Xu, Weihong Luo, Yuhua Li, Dugang Liu, Xiuqiang He, and Ruixuan Li

- 連合学習はデータプライバシーを効果的に保護するが、通信コストが高くなる場合がある
- 分散クライアントにモデル更新をグローバルモデル相対で最適化させるためにランダムノイズを利用
- FedMRNというフレームワークを提案し、各モデルパラメータに対して1ビットのマスクを学習
- 実験結果から、FedMRNは他のベースラインと比較して優れた収束速度とテスト精度を示した

新しい視点から通信効率を上げるって面白い発想だよね！実験結果も良好みたいだから、実用化が楽しみだな。

**Comment:** Accepted by MM 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-08-06 14:26

- - -

### [FedBAT: Communication-Efficient Federated Learning via Learnable Binarization](http://arxiv.org/abs/2408.03215)

**FedBAT: 学習可能な二値化による通信効率の高い連合学習**

Shiwei Li, Wenchao Xu, Haozhao Wang, Xing Tang, Yining Qi, Shijie Xu, Weihong Luo, Yuhua Li, Xiuqiang He, Ruixuan Li

- 連合学習は大規模データをプライバシーを守りつつ利用できるが、通信の負荷が高い課題がある
- モデル更新を二値化する従来手法は誤差が大きく、学習精度が低下することが多い
- FedBATは局所学習中に直接二値化を行い、誤差を減少させる新しい枠組みを提案
- 実験結果ではFedBATが収束を大幅に速め、従来手法より最大9%精度向上を達成

通信負荷を減らしつつ精度を高める手法を提案しているのがすごいよね！FedBATの未来が楽しみ！

**Comment:** Accepted by ICML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-08-06 14:19

- - -

### [Personalizing Federated Instrument Segmentation with Visual Trait Priors in Robotic Surgery](http://arxiv.org/abs/2408.03208)

**ロボット手術における視覚特性事前情報を用いた連合学習による手術器具セグメンテーションの個別化**

Jialang Xu, Jiacheng Wang, Lequan Yu, Danail Stoyanov, Yueming Jin, Evangelos B. Mazomenos

- 個別化連合学習（PFL）は、複数の臨床サイトがプライバシーを保ちながら協力してモデルを訓練する手法
- 既存のPFLは多頭型自己注意の個別化や手術シーン特有の外観多様性・器具形状類似性を考慮していない
- 提案手法のPFedSISは、GPD、APE、SGEを取り入れ各サイトのSIS性能を向上
- PFedSISは既存手法よりも性能が向上し、Diceで+1.51%、IoUで+2.11%の改善を達成

新しい手法で手術器具のセグメンテーションがもっと正確になりそうでワクワクする！ロボット手術の未来がもっと進化しそうだね。

**Comment:** 9 pages, 3 figures, under review

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.RO, physics.med-ph, **投稿日時:** 2024-08-06 14:06

- - -

### [Federated Learning Architectures: A Performance Evaluation with Crop Yield Prediction Application](http://arxiv.org/abs/2408.02998)

**連合学習アーキテクチャ: 作物収量予測アプリケーションによるパフォーマンス評価**

Anwesha Mukherjee, Rajkumar Buyya

- IoTアプリ向け連合学習を使用し、LSTMネットワークで作物収量を予測
- 集中型連合学習はクライアントとサーバーでモデル更新を集約
- 分散型連合学習はデバイス間でモデル更新を行い、リングまたはメッシュトポロジーを使用
- 集中型と分散型連合学習は97%と97.5%以上の予測精度を達成し、集中型は応答時間を75%短縮

想像してみて、作物の収量予測を連合学習で実現なんて素晴らしい！未来の農業がもっと効率的になるかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-06 07:05

- - -

### [HARMONIC: Harnessing LLMs for Tabular Data Synthesis and Privacy Protection](http://arxiv.org/abs/2408.02927)

**HARMONIC: LLMを活用した表形式データの生成とプライバシー保護**

Yuxin Wang, Duanyu Feng, Yongfu Dai, Zhengyu Chen, Jimin Huang, Sophia Ananiadou, Qianqian Xie, Hao Wang

- LLMの活用によるリアルなプライバシー保護型の合成データ生成が急務
- kNNアルゴリズムの概念で指示微調整データセットを構築
- 微調整によりデータ自体ではなくフォーマットと接続を記憶させる手法
- 評価部分では特定のプライバシーリスク指標DLTと性能評価指標LLEを開発

大規模なLLMで繊細なデータをさわるのってすごく興味深いことだよね！新しいプライバシー保護の方法とか、未来が明るく感じられる！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, cs.CR, **投稿日時:** 2024-08-06 03:21

- - -

### [Mitigating Malicious Attacks in Federated Learning via Confidence-aware Defense](http://arxiv.org/abs/2408.02813)

**信頼度を活用した防衛による連合学習における悪意ある攻撃の緩和**

Qilei Li, Ahmed M. Abdelmoniem

- 連合学習はプライベートなデータを共有せずにグローバルモデルを協力して訓練する。
- 従来の防衛法は単一の攻撃タイプに焦点を当て、多様なデータ中毒攻撃に対応できない。
- モデル信頼度スコアに基づいてクライアント更新の不確実性を評価し、悪意ある更新を検出・防衛。
- 提案手法は攻撃に対するロバスト性を向上させ、様々なシナリオでモデル精度と安定性を向上。

攻撃への対応がまるでゲームのバフとデバフみたいじゃない？これ、実社会でも多用途に使われそうでワクワクするね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.CV, cs.DC, **投稿日時:** 2024-08-05 20:27

- - -

### [ConDL: Detector-Free Dense Image Matching](http://arxiv.org/abs/2408.02766)

**ConDL: ディテクターフリーの密画像マッチング**

Monika Kwiatkowski, Simon Matern, Olaf Hellwich

- 深層学習フレームワークを導入し、密な画像対応関係を推定
- 解像度の高い特徴マップを生成し、各ピクセルにマッチ可能な記述子を付与
- 合成データに基づき、透視変化や照明変化、影、反射を含む大きな歪みに対する不変性を実現
- キーポイントディテクターを不要にし、既存の技術とは異なる方法で画像をマッチング

画像をより正確にマッチングできるってすごくない？これ、写真の加工とかにも活用できそうで楽しみだよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-08-05 18:34

- - -

### [Privacy-Safe Iris Presentation Attack Detection](http://arxiv.org/abs/2408.02750)

**プライバシー安全な虹彩プレゼンテーション攻撃検出**

Mahsa Mitcheff, Patrick Tinsley, Adam Czajka

- 身元漏洩のない合成虹彩画像を使用してプライバシー安全な虹彩プレゼンテーション攻撃検出方法を提案
- ISO/IEC 19794-6に準拠する虹彩画像生成の2つの生成モデルを設計
- 合成データのみで訓練したモデルは人間から収集した虹彩画像で訓練した場合より性能が低め
- 生成モデルの精度が向上すればプライバシー安全な虹彩プレゼンテーション攻撃検出の可能性が示唆される

合成データだけで虹彩攻撃を検出するなんて新しい取り組みだね！実際のデータでなくても効果があるなら、プライバシー保護が強化できそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, eess.IV, **投稿日時:** 2024-08-05 18:09

- - -

### [Automatic Voice Identification after Speech Resynthesis using PPG](http://arxiv.org/abs/2408.02712)

**PPGを用いた再合成音声による自動音声識別**

Thibault Gaudier, Marie Tahon, Anthony Larcher, Yannick Estève

- 音声再合成は、入力音声を基に別の音声を生成するタスクで、メディアモニタやジャーナリストに応用可能
- 音声変換では話者のアイデンティティを変え、言語情報を保持し、音声編集では話者のアイデンティティを保持するが一部の言葉を変更
- どちらの場合も中間表現で話者と音素の内容を分離する必要がある
- PPGに基づく音声再合成システムが正しい音声品質を生成し、再合成後の音声から元の話者を自動話者認証モデルが特定できないことを示す

PPGって中立なのがすごいよね。話者が変わったことを特定できないなんて、これが未来のメディア技術だよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.AI, cs.NE, eess.AS, eess.SP, **投稿日時:** 2024-08-05 13:59

- - -

### [Optimizing Disease Prediction with Artificial Intelligence Driven Feature Selection and Attention Networks](http://arxiv.org/abs/2408.03151)

**人工知能を用いた特徴選択とアテンションネットワークによる病気予測の最適化**

D. Dhinakaran, S. Edwin Raja, M. Thiyagarajan, J. Jeno Jasmine, P. Raghavan

- 機械学習は医療分野で革新的な病気予測戦略を生み出している
- SEV-EBアルゴリズムを用い、統計的・深層的特徴を結合し最適な特徴選択を実現
- 提案された合成モデルは、短期的パターンと長期的依存性を捉えるHSC-AttentionNetを採用
- 精度95%、F1スコア94%を達成し、従来の方法を超える性能を示した

技術と医療の融合がどんどん進んでいくこの時代、こういった研究がどれだけ人の命を救うのか楽しみすぎる！また、今後はもっと多くの病気にも応用されていくといいなぁ。

**Comment:** 16 Pages, 4 Figures

**トピック:** [TEE](tee), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-31 14:12
