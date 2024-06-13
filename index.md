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

更新: 2024-06-13T04:20:08.086900

- - -

### [Real3D: Scaling Up Large Reconstruction Models with Real-World Images](http://arxiv.org/abs/2406.08479)

**Real3D: 実世界の画像を用いた大規模再構築モデルのスケーリング**

Hanwen Jiang, Qixing Huang, Georgios Pavlakos

- 従来の大規模再構築モデル（LRMs）は合成3D資産やマルチビューキャプチャに依存
- Real3Dは実世界のシングルビュー画像を用いた初のLRMシステムを導入
- セルフトレーニングフレームワークと2つの教師なし損失を提案、ピクセルレベルと意味レベルで監督
- 野外画像から高品質な例を収集する自動データキュレーションアプローチを開発

実世界の画像で学習できるってすごい！これでさまざまな形状やデータを取り込める可能性が広がるね。何より、実際の画像が使われてるからより現実に即したモデルが作れそう。

**Comment:** Project page: https://hwjiang1510.github.io/Real3D/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-12 17:59

- - -

### [Nonconvex Federated Learning on Compact Smooth Submanifolds With Heterogeneous Data](http://arxiv.org/abs/2406.08465)

**異種データを扱うコンパクトな滑らかな部分多様体上の非凸分散学習**

Jiaojiao Zhang, Jiang Hu, Anthony Man-Cho So, Mikael Johansson

- 連合学習において非凸最適化問題と多様体最適化を扱う新手法を提案
- 確率的リーマン勾配と多様体射影演算子を用いて計算効率を向上
- 局所的更新を利用し通信効率を改善し、クライアントドリフトを回避
- 提案アルゴリズムは既存の方法より計算および通信オーバーヘッドが小さいことを示す

理論もしっかりしているし、実験でも良い結果が出ているなんて、これからの連合学習の標準になるかもね。異種データを扱うっていう点も現実的にすごく役立ちそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-12 17:53

- - -

### [Causality for Tabular Data Synthesis: A High-Order Structure Causal Benchmark Framework](http://arxiv.org/abs/2406.08311)

**表形式データ合成の因果関係:高次構造因果ベンチマークフレームワーク**

Ruibo Tu, Zineb Senane, Lele Cao, Cheng Zhang, Hedvig Kjellström, Gustav Eje Henter

- 従来のモデルは複雑な依存関係を捉え切れず、合成データの品質が不十分
- 高次構造因果情報を事前知識として導入し、評価のためのベンチマークフレームワークを提供
- 柔軟なデータ生成プロセスでベンチマークデータセットを作成し、モデル評価を実施
- 実験結果は理想と実際の性能間のギャップを明らかにし、ベースライン手法の違いを示した

因果関係をしっかり捉えることで、もっと精度の高いデータ合成が可能になりそう！具体的なベンチマークが公開されているのも楽しみだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-12 15:12

- - -

### [A deep cut into Split Federated Self-supervised Learning](http://arxiv.org/abs/2406.08267)

**分割連合自己教師付き学習の深堀り**

Marcin Przewięźlikowski, Marcin Osial, Bartosz Zieliński, Marek Śmieja

- 最先端手法のMocoSFLは初期層にネットワーク分割を最適化するが、クライアントデータの保護が低下し通信オーバーヘッドが増加
- 分割の深さが分散学習におけるプライバシーと通信効率の維持に重要であることを示す
- MocoSFLは最小限の通信オーバーヘッドでは品質が劇的に劣化することが判明
- オンラインとモメンタムクライアントモデルを揃えるMonAcoSFLを導入し、精度を向上させつつ通信オーバーヘッドを大幅に削減

新しい手法MonAcoSFLで本当に連合学習の実用性が上がるのか注目だね！特に通信効率が改善されると、もっと広い環境で応用できそうでわくわくする。

**Comment:** Accepted to European Conference on Machine Learning (ECML) 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-06-12 14:35

- - -

### [Figuratively Speaking: Authorship Attribution via Multi-Task Figurative Language Modeling](http://arxiv.org/abs/2406.08218)

**比喩的表現による著者識別: マルチタスク比喩言語モデル**

Gregorios A Katsios, Ning Sa, Tomek Strzalkowski

- 比喩言語（FL）の特徴の識別は、著者の意図する意味とそのニュアンスを理解するために重要
- 複数のFL形式を組み合わせた使用が、単一の構成よりも作家のスタイルを正確に反映
- FL特徴が著者識別（AA）に重要な役割を果たすと仮定し、AAに基づくFL使用の最初の計算研究を実施
- マルチタスク比喩言語モデル（MFLM）を提案し、いくつかのデータセットでAAのパフォーマンスを改善

比喩言語で著者が特定できるなんて面白そう！たくさんのスタイルがモデルで検出されるなんて、スゴイね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-12 13:49

- - -

### [Semi-Supervised Spoken Language Glossification](http://arxiv.org/abs/2406.08173)

**半教師ありの音声言語グロッシフィケーション**

Huijie Yao, Wengang Zhou, Hao Zhou, Houqiang Li

- 音声言語グロッシフィケーション（SLG）は音声言語テキストを手話グロスに翻訳することを目指す
- $S^3$LG フレームワークは、限られた並列データのボトルネックを解決するために大規模な音声言語テキストを取り入れる
- ルールに基づくヒューリスティックとモデルに基づくアプローチを採用して自己トレーニングを行う
- データの品質に一貫性を持たせるため、合成データのノイズの影響を軽減するためのレギュラリゼーションを用いる

音声言語を手話に変換する技術は、コミュニケーションの壁をもっと取り除けるかもね。これからの発展が楽しみ！

**Comment:** Accepted to ACL2024 main

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-12 13:05

- - -

### [MWIRSTD: A MWIR Small Target Detection Dataset](http://arxiv.org/abs/2406.08063)

**MWIRSTD: MWIR小目標検出データセット**

Nikhil Kumar, Avinash Upadhyay, Shreya Sharma, Manoj Sharma, Pravendra Singh

- MWIRSTDは14のビデオシーケンスと約1053の画像から構成され、3種類の小目標が注釈付きで含まれる
- 冷却MWIRイメージャを使用して取得されたこのデータセットは、現実的なMWIRシーンでの小物体検出のための研究に寄与
- 既存のデータセットとは異なり、MWIRSTDは非冷却の熱画像や背景に合成されたデータではなく、本物のMWIRデータを提供
- 伝統的な方法や深層学習ベースの技術による小目標検出の実験が行われ、その有効性に関する貴重な洞察が得られている

実験での深層学習技術の効果がとっても楽しみ！現実的なシーンでのデータって本当に貴重だよね、これは研究の進展に大きく貢献しそう。

**Comment:** Accepted in ICIP2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-12 10:26

- - -

### [Beyond the Mean: Differentially Private Prototypes for Private Transfer Learning](http://arxiv.org/abs/2406.08039)

**平均を超えて: プライバシー転送学習のための差分プライベートプロトタイプ**

Dariush Wahdany, Matthew Jagielski, Adam Dziedzic, Franziska Boenisch

- 機械学習モデルはトレーニングデータセットからプライベート情報を漏洩することがある
- 差分プライバシー（DP-SGD）は情報漏洩を制限する標準的な解決策だが課題が残る
- 新しい差分プライベートプロトタイプ学習（DPPL）を提案し、転送学習に応用
- DPPLは少数のプライベートデータから高いユーティリティと強いプライバシー保証を提供

このアプローチ、すごく革新的だよね。少ないデータでも高パフォーマンスを維持できるなんて、実用化が楽しみ！

**Comment:** Submitted to NeurIPS 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, 68T01, **投稿日時:** 2024-06-12 09:41

- - -

### [A Federated Online Restless Bandit Framework for Cooperative Resource Allocation](http://arxiv.org/abs/2406.07992)

**連合オンラインレストレスバンディットフレームワークによる協調リソース配分**

Jingwen Tong, Xinran Li, Liqun Fu, Jun Zhang, Khaled B. Letaief

- 既存の研究はMarkov報酬プロセス(MRP)の既知の指数の前提によるものが多い
- MRPsの未知のシステムダイナミクス問題を解決するための学習ベースの効率的な解決策は未解決
- フェデレーテッドThompsonサンプリング有効Whittle指数(FedTSWI)アルゴリズムを提案
- 提案アルゴリズムは速い収束率と高性能を達成し、エージェント数が多いほどサンプル複雑性が低下

協調的な学習でシステムダイナミクスを効率よく学ぶって未来っぽくてワクワクしちゃうね。リソース配分って難しいけど、この方法ならうまくいきそうな予感！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-06-12 08:34

- - -

### [Interpetable Target-Feature Aggregation for Multi-Task Learning based on Bias-Variance Analysis](http://arxiv.org/abs/2406.07991)

**バイアス-バリアンス分析に基づく多タスク学習の解釈可能なターゲット・特徴の集約**

Paolo Bonetti, Alberto Maria Metelli, Marcello Restelli

- 多タスク学習（MTL）はタスク間の共有知識を活用して一般化と性能を向上させる強力な機械学習手法である
- 提案手法はタスククラスターリングと特徴変換の間に位置し、ターゲットと特徴を二相で反復的に集約
- 最初のフェーズでは、加法ガウスノイズを伴う回帰モデルのバイアスとバリアンス分析を行い、タスクの漸近的バイアスとバリアンスを導出
- 提案手法は合成データと実データで検証され、地球科学への応用も示唆

新しい技術で、多タスク学習の性能がどれだけ向上するかすごく興味あるよね。特に地球科学への応用がどんなものか、ちょっとワクワクしちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-06-12 08:30

- - -

### [DPSW-Sketch: A Differentially Private Sketch Framework for Frequency Estimation over Sliding Windows (Technical Report)](http://arxiv.org/abs/2406.07953)

**DPSW-Sketch: スライディングウィンドウ上の頻度推定における差分プライバシーを備えたスケッチフレームワーク (テクニカルレポート)**

Yiping Wang, Yanhao Wang, Cen Chen

- スライディングウィンドウモデルでは最新の$w$個のデータのみを使用し、計算スペースを最小化しつつ統計を追跡
- データストリームに個人の敏感情報が含まれるため、プライバシー保証が必要
- カウントミンスケッチに基づく\textsc{DPSW-Sketch}を提案し、差分プライバシーを満たしつつサブリニア時間と空間で周波数とヘビーヒッタークエリの結果を近似
- 実世界と合成データセットを用いた実験で、最先端の方法よりも優れたユーティリティとプライバシーのトレードオフを提供

この研究って未来のデータ解析に革命が起きそうな予感！個人のプライバシーを守りつつ、重要な情報を効率的に見つけるなんて最高だね。

**Comment:** Accepted for publication at KDD 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, cs.LG, **投稿日時:** 2024-06-12 07:24

- - -

### [FDLoRA: Personalized Federated Learning of Large Language Model via Dual LoRA Tuning](http://arxiv.org/abs/2406.07925)

**FDLoRA: デュアルLoRAチューニングによる大規模言語モデルの個別連合学習**

Jiaxing QI, Zhongzhi Luan, Shaohan Huang, Carol Fung, Hailong Yang, Depei Qian

- 大規模言語モデル（LLM）の訓練は多大な計算リソースと豊富なラベル付きデータを必要とし、個別ユーザー向けのLLM訓練が困難。
- 連合学習（FL）を導入して分散プライベートデータ上で協調訓練を行うことが提案されているが、データやシステムの異質性、モデルサイズの課題により低効率。
- 新たな個別連合学習（PFL）フレームワーク「FDLoRA」は、クライアント単位でパーソナライズとグローバル知識をキャプチャするデュアルLoRAモジュールをセット。
- 自適応融合アプローチを採用し、計算コストと通信コストを抑えつつ、クライアントのパフォーマンス向上を実現。

この論文は、個別のデータで効率的に連合学習を実行し、大規模言語モデルの訓練を最適化する新戦略を提案しているところが面白いと思う。このアプローチで、将来的にいろいろなアプリがさらに賢くなりそうでワクワクするよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-06-12 06:44

- - -

### [Aggregation Design for Personalized Federated Multi-Modal Learning over Wireless Networks](http://arxiv.org/abs/2406.07915)

**ワイヤレスネットワークにおけるパーソナライズド連合マルチモーダル学習のための集約設計**

Benshun Yin, Zhiyong Chen, Meixia Tao

- パーソナライズド連合マルチモーダル学習（FMML）で異なるモダリティの情報が統合され、学習性能が向上する
- パラメータスケジューリングスキームを開発し、非独立・非同分布（non-IID）データとモダリティヘテロジニティを考慮
- 学習ベースのアプローチを用いて、異なるデバイスのモダリティごとのパラメータの集約係数を得る
- 提案アルゴリズムがFMMLのパーソナライズド性能を効果的に向上させることを実験結果で示す

ネットワーク環境が違っても個別に最適化できる学習法ってすごく面白そう！どんなデバイスでも効果が出るなんて未来感あるよね。

**Comment:** accepted by IEEE Communications Letters

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, eess.SP, math.IT, **投稿日時:** 2024-06-12 06:35

- - -

### [SynthForge: Synthesizing High-Quality Face Dataset with Controllable 3D Generative Models](http://arxiv.org/abs/2406.07840)

**SynthForge: 管理可能な3D生成モデルを用いた高品質な顔データセットの合成**

Abhay Rawat, Shubham Dokania, Astitva Srivastava, Shuaib Ahmed, Haiwen Feng, Rahul Tallamraju

- 生成モデルの進歩によりリアルなデータを制御可能にレンダリングする能力が向上
- 従来のグラフィックスレンダリングと比較して、最小限のドメインギャップでリアルなサンプルを生成可能
- 既存の制御可能な生成モデルから3D一貫したアノテーションを抽出し、下流タスクに利用可能にする
- 合成データだけを使用しても、最先端モデルと競合する性能を示し、下流タスクの解決に可能性を示す

3D一貫性のアノテーションって面白そう！これからの顔認識技術にどう影響するのか楽しみだね。

**Comment:** 11 pages, 4 figures, 3 tables. Under Review

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-12 03:15

- - -

### [Regularizing and Aggregating Clients with Class Distribution for Personalized Federated Learning](http://arxiv.org/abs/2406.07800)

**クラス分布によるクライアントの正則化と集約を用いた個別化連合学習**

Gyuejeong Lee, Daeyoung Choi

- 個別化連合学習(PFL)は異なるデータ分布を持つクライアントに対してカスタマイズされたモデルを提供
- 高い計算コストや通信コストが既存のPFL方法の実用性を制限している
- 提案手法cwFedAVGは、クラスごとに連合平均化（FedAVG）を行い、サーバーでクラスごとのグローバルモデルを作成
- WDRにより推定精度を向上させ、cwFedAVGは他のPFL手法と比較して性能が優れ、計算効率も高い

新しいPFL手法で計算コストがグッと下がるのはマジ嬉しい！クラスごとにモデルを特化させるなんて新鮮で面白そうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-12 01:32

- - -

### [Label Smoothing Improves Machine Unlearning](http://arxiv.org/abs/2406.07698)

**ラベルスムージングによる機械アンラーニングの改善**

Zonglin Di, Zhaowei Zhu, Jinghan Jia, Jiancheng Liu, Zafar Takhirov, Bo Jiang, Yuanshun Yao, Sijia Liu, Yang Liu

- 機械アンラーニング（MU）はモデルから学習データを消去するが、計算コストと性能の均衡が困難
- ラベルスムージングのモデル信頼性と差分プライバシーに着想を得た逆プロセスを提案
- 新手法UGradSLはラベルスムージングを用いてMU性能を向上させるシンプルなアプローチ
- 6つの異なるデータセットの実験で、有効性と頑健性を実証し、性能が向上するが計算コストは僅か

データ消去の効率と精度を高めるなんて、すごく便利そう！これでプライバシー問題ももっと解決できるかもね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-11 20:26
