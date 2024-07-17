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

更新: 2024-07-17T04:19:38.474382

- - -

### [Ascend-CC: Confidential Computing on Heterogeneous NPU for Emerging Generative AI Workloads](http://arxiv.org/abs/2407.11888)

**Ascend-CC: 新興の生成AIワークロード向け異種NPU上の機密計算**

Aritra Dhar, Clément Thorens, Lara Magdalena Lazier, Lukas Cavigelli

- 大規模言語モデル（LLM）に基づく生成AIワークロードはクラウド上で中心的
- 専用ハードウェア（GPU、NPU、TPU）は一般的なCPUより優れた性能を持つが、機密性の確保が課題
- Ascend-CCはホストシステムへの信頼を必要とせず、データとモデルの暗号化を実現
- 最先端のLLMを用いた評価で、AIソフトウェアスタックに変更なしに最小のオーバーヘッドを提供

異種NPUでの機密計算って、未来のAI技術をリードしそう！全く新しいプラットフォームがどんな影響を与えるのか気になるんだよね。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-16 16:17

- - -

### [Zero-shot Cross-Lingual Transfer for Synthetic Data Generation in Grammatical Error Detection](http://arxiv.org/abs/2407.11854)

**文法誤り検出における合成データ生成のためのゼロショットクロスリンガル転送**

Gaetan Lopez Latouche, Marc-André Carbonneau, Ben Swanson

- GED（文法誤り検出）は人間が注釈を付けた誤りコーパスに依存している
- ゼロショットクロスリンガル転送を活用し、さまざまな言語のデータを使用して合成誤りを生成
- 合成誤りコーパスを使用してGEDモデルを訓練する二段階の微調整パイプラインを提案
- 提案手法が他の状態最先端の方法を上回り、多様で人間の誤りに似たエラーを生成

ゼロショットって、注釈なしで新しい言語へ転用できるってことだね。リソースが少ない言語でもしっかり対応できるのはすごく未来的だなって思う！

**Comment:** Submitted to EMNLP 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-07-16 15:35

- - -

### [Defining 'Good': Evaluation Framework for Synthetic Smart Meter Data](http://arxiv.org/abs/2407.11785)

**「良いデータ」の定義：合成スマートメーターデータの評価フレームワーク**

Sheng Chai, Gus Chadney, Charlot Avery, Phil Grunewald, Pascal Van Hentenryck, Priya L. Donti

- 詳細な需要データは、正確なプロファイリングと需要管理のために必要
- プライバシー懸念から、データの公表が困難であるが、質の高い合成データが解決策
- 他業界の評価フレームワークを、スマートメーターデータに適用し解析
- 差分プライバシーと特定の指標を用いた評価方法を提案し、従来のプライバシー攻撃の限界を指摘

合成データがプライバシー問題の解決策になるって面白いよね！これが普及したらもっと安心してデータ使えるかも。

**Comment:** This work has been submitted to the IEEE for possible publication.   Copyright may be transferred without notice, after which this version may no   longer be accessible

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-16 14:41

- - -

### [R-SFLLM: Jamming Resilient Framework for Split Federated Learning with Large Language Models](http://arxiv.org/abs/2407.11654)

**大規模言語モデルを用いた分割連合学習におけるジャミング耐性フレームワークR-SFLLM**

Aladin Djuhera, Vlad C. Andrei, Xinyang Li, Ullrich J. Mönich, Holger Boche, Walid Saad

- 分割連合学習（SFL）では、大規模MLモデルの一部がリモートサーバーに委託される
- SFLは特に無線チャネル上で、モデルパラメータが敵対的なジャミングに脆弱である
- フレームワークR-SFLLMは無線センシングデータを利用してジャミング方向を特定し、ビームフォーミングやリソース配分を最適化する
- 実験で、R-SFLLMはBERTやRoBERTaモデルに対して有効性を示し、ノイズ暴露に対して訓練されたLLMの耐性を強化する

新しいアプローチがまだいっぱいでワクワクするね！特に無線センシングでジャミングを防ぐなんて、本当に戦略的で面白そうだと思うよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, eess.SP, **投稿日時:** 2024-07-16 12:21

- - -

### [CCVA-FL: Cross-Client Variations Adaptive Federated Learning for Medical Imaging](http://arxiv.org/abs/2407.11652)

**CCVA-FL: 医療画像のためのクロスクライアント変動適応型連合学習**

Sunny Gupta, Amit Sethi

- 連合学習（FL）は、分散データ上でモデルを訓練しながらプライバシーを保護するアプローチ
- 医療分野でのFLの可能性は大きいが、医療画像データのクロスクライアント変動と限定された注釈で課題が生じる
- CCVA-FLは、画像を共通の特徴空間に変換し、クロスクライアント変動を最小化するために専門家による一部画像の注釈を利用
- スケーラブル・ディフュージョン・モデルとトランスフォーマーを用いた合成医療画像を作成し、各クライアントのローカル画像をターゲット画像空間に変換してサーバーモデルを開発

医療分野でのクロスクライアント変動をうまく解決できるなら、連合学習の醍醐味がもっと活かされるかもね！新しい技術で医療の可能性が広がりそうですごくワクワクしちゃう！

**Comment:** 10 pages, 6 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, I.2.10; I.4.0; I.4.1; I.4.2; I.4.6; I.4.7; I.4.8; I.4.9; I.4.10;
  I.2.10; I.5.1; I.5.2; I.5.4; J.2, **投稿日時:** 2024-07-16 12:18

- - -

### [Probing the Efficacy of Federated Parameter-Efficient Fine-Tuning of Vision Transformers for Medical Image Classification](http://arxiv.org/abs/2407.11573)

**医療画像分類におけるビジョン・トランスフォーマーの連合パラメータ効率的なファインチューニングの有効性を探る**

Naif Alkhunaizi, Faris Almalik, Rouqaiah Al-Refai, Muzammal Naseer, Karthik Nandakumar

- 事前学習済みトランスフォーマーモデルのファインチューニングは、データ不足やプライバシー制約により困難
- 連合学習の通信負担を減らすため、パラメータ効率的ファインチューニング（PEFT）が必須
- 視覚プロンプトチューニングや低ランク分解、ハイブリッドPEFTなど新たな連合PEFT手法を提案
- OODや非IIDデータで精度と効率のトレードオフがあり、元のモデル選択が重要。医療領域のモデルが望ましい

新しいPEFT手法を使うことで、医療画像分類の精度がどう変わるのか気になる！こんな研究が進むと、医療の未来も変わりそうでワクワクするね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-07-16 10:28

- - -

### [Federated Learning Forecasting for Strengthening Grid Reliability and Enabling Markets for Resilience](http://arxiv.org/abs/2407.11571)

**グリッドの信頼性強化と市場の復元力を実現する連合学習予測**

Lucas Pereira, Vineet Jagadeesan Nair, Bruno Dias, Hugo Morais, Anuradha Annaswamy

- 分散エネルギー資源が豊富な将来の電力網の信頼性と復元力を向上させるための包括的アプローチを提案
- 連合学習ベースの攻撃検出と、ローカル電力市場ベースの攻撃緩和方法を組み合わせた分散スキーム
- 現実の太陽光発電が豊富な配電網に適用し、スキームを検証
- シミュレーション結果により、このアプローチが実現可能で、サイバー物理攻撃の影響を効果的に緩和できると示された

未来の電力網に使う連合学習ってなんだかSFみたいでワクワクするよね！リアルな配電網で実証されてるって、なんだか未来がもうすぐそこに来てる感じがする。

**Comment:** Submitted to CIRED 2024 USA: Workshop on Resilience of Electric   Distribution Systems

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.SY, eess.SY, math.OC, **投稿日時:** 2024-07-16 10:23

- - -

### [Detection of Global Anomalies on Distributed IoT Edges with Device-to-Device Communication](http://arxiv.org/abs/2407.11308)

**デバイス間通信による分散IoTエッジ上のグローバル異常検出**

Hideya Ochiai, Riku Nishihata, Eisuke Tomiyama, Yuwei Sun, Hiroshi Esaki

- 異常検出は高頻度データサンプリングを伴うことが多く、エッジデバイスで実行する必要がある
- 複数のIoTデバイスが協調して異常を検出するために、"WAFL-Autoencoder"という全分散協調スキームを提案
- グローバル異常の概念を導入し、ターゲット領域内の全デバイスで稀なサンプルも含める
- 分散しきい値検出アルゴリズムで、低い誤検知率と高い真陽性率を達成した

"ターゲット領域内で稀なサンプル"なんて、デバイス同士が協力して異常を検出するのがすごいよね！未来の監視システムとして期待できそう！

**Comment:** 6 pages, 3 figures, ACM MobiHoc AIoT 2023 (accepted)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-07-16 01:50

- - -

### [Empirical Mean and Frequency Estimation Under Heterogeneous Privacy: A Worst-Case Analysis](http://arxiv.org/abs/2407.11274)

**不均一なプライバシー下での経験平均と頻度推定：最悪ケースの分析**

Syomantak Chaudhuri, Thomas A. Courtade

- 差分プライバシー（DP）は現時点でのプライバシー基準である
- DPの枠組みにおいて、ユーザーごとに異なるプライバシー要求を許可
- 経験平均推定と頻度推定の問題を、相関あり・なし二つの設定で分析
- 提案アルゴリズムは、PACエラーや平均2乗誤差の点で最適性を持ち、従来手法より優れている

ユーザーごとにプライバシー要求が異なる設定を考慮するなんて最新の研究だね！色んな状況に対応できる解析方法って、本当に現場でも役立ちそう。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-07-15 22:46

- - -

### [TLRN: Temporal Latent Residual Networks For Large Deformation Image Registration](http://arxiv.org/abs/2407.11219)

**TLRN: 大変形画像登録のための時系列潜在残差ネットワーク**

Nian Wu, Jiarui Xing, Miaomiao Zhang

- 時系列画像登録における大きな動きの登録を目指す新しいアプローチの提案
- 動きの連続性と連続画像フレームの時間的滑らかさを利用
- 潜在変形空間で設計された残差ブロックを用いた時系列の残差ネットワーク
- 合成データと実世界の心臓MRI画像ビデオでの有効性を検証し、登録精度が向上

時系列画像を使って動きの大きい画像の登録をするなんて、なんか未来感あるよね！これ、医療とかで本当に役立ちそうだと思わない？

**Comment:** 10 pages. Accepted by MICCAI 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, eess.IV, **投稿日時:** 2024-07-15 20:07

- - -

### [SSSD-ECG-nle: New Label Embeddings with Structured State-Space Models for ECG generation](http://arxiv.org/abs/2407.11108)

**SSSD-ECG-nle: 構造化状態空間モデルと新しいラベル埋め込みを用いたECG生成**

Sergey Skorik, Aram Avetisyan

- 心電図（ECG）は心臓病の診断のために重要だが、プライバシーの懸念あり
- 拡散モデルを用いて、実データに匹敵する合成データの生成が可能
- SSSD-ECGの改良版を提案し、下流タスクでの有効性を実証
- 定量／定性評価や専門医による評価を実施し、結果を共有

心電図のデータ生成って未来の医療に欠かせないよね！専門家の評価も取り入れて、実験結果が再現可能なのがすごいなって思った。



**トピック:** [合成データ](sd), **カテゴリ:** eess.SP, cs.LG, **投稿日時:** 2024-07-15 16:31

- - -

### [Overcoming Catastrophic Forgetting in Federated Class-Incremental Learning via Federated Global Twin Generator](http://arxiv.org/abs/2407.11078)

**連合グローバルツインジェネレーターによる連合階調学習における壊滅的忘却の克服**

Thinh Nguyen, Khoa D Doan, Binh T. Nguyen, Danh Le-Phuoc, Kok-Seng Wong

- FCILは連合学習で複数の参加者がプライベートデータを共有せずにグローバルモデルを訓練できる
- 従来の連合学習アルゴリズムは壊滅的忘却に苦しみ、生成モデルによる対策も限定的
- FedGTGはプライバシー保護の生成モデルを利用し、クライアントのデータにアクセスせずに合成データを生成
- 実験ではCIFAR-10、CIFAR-100、tiny-ImageNetで精度と忘却の改善を実証

これは興味津々だね！特にプライバシーを守りながらも壊滅的忘却を克服できる点が注目だよね。未来の連合学習がどこまで進化するか楽しみだな～。



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CV, 68T07 (Primary), 68T45 (Secondary), **投稿日時:** 2024-07-13 08:23

- - -

### [Combining Federated Learning and Control: A Survey](http://arxiv.org/abs/2407.11069)

**連合学習と制御の統合：サーベイ**

Jakob Weber, Markus Gurtner, Amadeus Lobe, Adrian Trachte, Andreas Kugi

- 連合学習と制御を組み合わせて適応性、スケーラビリティ、一般化、およびプライバシーを向上
- 従来の制御方法はオンラインモデルの調整や学習が必要な場合が多い
- 連合学習はデータをローカルに保持しながら、分散デバイス間で協調的に学習を行う
- ダイナミックシステムのモデリングから多エージェント決定システムでの知識移転まで、応用の期待が高まる

これからの連合学習と制御の融合が、どんな新しい世界を開くかすごく楽しみだよね！プライバシーを守りながら賢く制御する技術なんて、夢のよう！

**Comment:** Submitted to IEEE Communications Survey and Tutorials

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.SY, eess.SY, stat.ML, **投稿日時:** 2024-07-12 14:29
