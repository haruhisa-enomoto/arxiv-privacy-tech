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

更新: 2024-05-22T07:26:28.608214

- - -

### [Establishing Trust in the Beyond-5G Core Network using Trusted Execution Environments](http://arxiv.org/abs/2405.12177)

**信頼できる実行環境を用いたBeyond-5Gコアネットワークにおける信頼構築**

Marinos Vomvas, Norbert Ludant, Guevara Noubir

- 5Gは従来のモノリシック設計からサービスベースアーキテクチャへのパラダイムシフトを開始
- 新アーキテクチャはネットワーク機能を地理的、物理的に分散可能な小さな論理単位に分割する
- クラウドなどの技術採用で攻撃面が広がり、厳格なセキュリティ分析が必要
- 提案するモデルは5G標準に変更を加えず、信頼を強化し、実験により性能影響が最小限であることを示す

5Gってこれからますます重要になるから、その安全性確立のための研究はめっちゃ面白そう！今回は、信頼できる実行環境を使ってゼロトラストを強化しているのがポイントだね。

**Comment:** 18 pages, 8 figures

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-20 17:02

- - -

### [Embracing Radiance Field Rendering in 6G: Over-the-Air Training and Inference with 3D Contents](http://arxiv.org/abs/2405.12155)

**6Gにおけるレイディアンスフィールドレンダリングの採用: 3Dコンテンツを用いたOTAトレーニングと推論**

Guanlin Wu, Zhonghao Lyu, Juyong Zhang, Jie Xu

- 3Dコンテンツの効率的な表現、伝送、再構築は、6Gネットワークで重要である
- NeRFと3D-GSは、複雑なシーンにおいてフォトリアリスティックなレンダリング結果を提供する技術である
- 連合学習と階層的なデバイスエッジクラウドアーキテクチャを利用して、NeRFと3D-GSモデルのOTAトレーニングを提案
- モデル圧縮やレンダリング加速、通信オーバーヘッド削減のための新しいセマンティック通信設計を示す

3Dの表現技術の進化ってすごくワクワクするよね！6Gがもっと身近になったらどんな体験ができるんだろう～。

**Comment:** 15 pages,7 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, math.IT, **投稿日時:** 2024-05-20 16:32

- - -

### [Sheet Music Transformer ++: End-to-End Full-Page Optical Music Recognition for Pianoform Sheet Music](http://arxiv.org/abs/2405.12105)

**シートミュージックトランスフォーマー++: ピアノ形式の楽譜に対するエンドツーエンドの全ページ光学音楽認識**

Antonio Ríos-Vila, Jorge Calvo-Zaragoza, David Rizo, Thierry Paquet

- 現行のOMRは多段階パイプラインに依存し、全ページの転写に課題がある
- 提案されたモデルはレイアウト解析を省略し、全ページのポリフォニック楽譜を転写可能
- シンセティックデータ生成によるカリキュラム学習ベースの事前訓練が鍵
- 公開ポリフォニック転写データセットでの実験によりモデルの有効性を確認

楽譜認識がここまで進歩するなんてすごいね！ピアノのさまざまな楽譜を手軽にデジタル化できる未来が楽しみ♡



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-20 15:21

- - -

### [Energy-Efficient Federated Edge Learning with Streaming Data: A Lyapunov Optimization Approach](http://arxiv.org/abs/2405.12046)

**ストリーミングデータを用いたエネルギー効率の良い連合エッジ学習：ライアプノフ最適化アプローチ**

Chung-Hsuan Hu, Zheng Chen, Erik G. Larsson

- 連合学習（FL）により、分散するクライアント間でユーザーの機密データを開示せずに効率的な学習が可能
- FEELシステムでは無線チャンネルの変動により通信の遅延とエネルギー消費が発生
- ストリーミングデータシナリオで、ランダムに生成されるデータの到着とリソースの可用性に対応する動的スケジューリングとリソース配分アルゴリズムを提案
- 提案アルゴリズムはデバイスのスケジューリング、計算能力の調整、帯域幅と送信電力の割り当てを適応的に行い、シミュレーションにより効果を確認

リアルタイムでデータが変わる中でも、効率良く学習できるなんてすごいよね✨これからのネットワークシステムにめっちゃ期待しちゃう！

**Comment:** Submitted to IEEE journals for possible publication

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.IT, eess.SP, math.IT, **投稿日時:** 2024-05-20 14:13

- - -

### [DuckDB-SGX2: The Good, The Bad and The Ugly within Confidential Analytical Query Processing](http://arxiv.org/abs/2405.11988)

**DuckDB-SGX2：機密分析クエリ処理の良い点、悪い点、醜い点**

Ilaria Battiston, Lotte Felius, Sam Ansmink, Laurens Kuiper, Peter Boncz

- DuckDBを用いて、データの静止状態と移動中のデータに対する機密分析環境を評価
- DuckDBのカラム圧縮と暗号化の組み合わせが性能向上に寄与
- SGX環境ではカテゴリック・ミスコストが最大5倍、NUMAペナルティ、ページスワップのコスト増
- 有効な環境調整のための推奨事項と非推奨事項を提供

Intel SGXを使って、データの安全性を保ちながらも性能をどれだけ犠牲にするかのバランスが良さそう。分析クエリっていかにもやってみたい感じー！



**トピック:** [TEE](tee), **カテゴリ:** cs.DB, **投稿日時:** 2024-05-20 12:44

- - -

### [Distinguished In Uniform: Self Attention Vs. Virtual Nodes](http://arxiv.org/abs/2405.11951)

**ユニフォームで際立つ：セルフアテンションvs仮想ノード**

Eran Rosenbluth, Jan Tönshoff, Martin Ritzert, Berke Kisin, Martin Grohe

- グラフ変換モデル（GT）は、MPGNNとグローバルセルフアテンションを組み合わせたもの
- これらは普遍的な関数近似器であるが、ノード特徴量に位置符号化が必要
- MPGNNや2層MLPも同様に位置符号化を用いると非一様な普遍近似器である
- セルフアテンションと仮想ノードの計算方法が異なり、どちらも一様な普遍性を持たない

セルフアテンションと仮想ノードの違いを深掘りして、そこから生まれる新しい可能性が気になるよね。実際のデータからもどちらが優れているかは決着がつかないみたいで、もっと研究したら面白いかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, 68T05, 68T07, I.2.6, **投稿日時:** 2024-05-20 11:02

- - -

### [PT43D: A Probabilistic Transformer for Generating 3D Shapes from Single Highly-Ambiguous RGB Images](http://arxiv.org/abs/2405.11914)

**PT43D: 単一の非常に曖昧なRGB画像から3D形状を生成するための確率的トランスフォーマー**

Yiheng Xiong, Angela Dai

- 単一のRGB画像から3D形状を生成する重要性はロボティクスなどで高まっている
- 現行手法は明確かつ完全な視覚情報を前提としているが、本研究は曖昧な観察を含む画像を考慮
- トランスフォーマーベースの自己回帰モデルを提案し、遮蔽や視野トリミングなど現実的なシナリオに対応
- 実験で合成データと実世界データの両方で最先端技術を上回る性能を実証

曖昧な画像からでも高精度な3D形状を再現できるのってすごいよね！ロボティクスとかでめっちゃ役立ちそうだから、未来の技術がもっと身近になるかも。

**Comment:** 10 pages, 6 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-20 09:49

- - -

### [Vertical Federated Learning Hybrid Local Pre-training](http://arxiv.org/abs/2405.11884)

**垂直連合学習におけるハイブリッドローカル事前学習**

Wenguo Li, Xinling Guo, Xu Jiao, Tiancheng Huang, Xiaoran Yan, Yao Yang

- 垂直連合学習 (VFL) は、現実世界の広範囲の応用を持ち、学術界と産業界の関心を集めている
- 企業は異なる部門から同ユーザーの価値ある特徴を活用し、モデル予測スキルを向上させたい
- 従来のVFLはアラインサンプルのみを利用し、関与するパーティが増えるとサイズが縮小する問題がある
- VFLHLPはローカルデータで先に事前学習、その後アラインデータでフェデレーテッドモデルの性能を向上させる

新しいアプローチで問題解決しようとするアイデアが魅力的！複数のパーティでの連携が未来の技術を支える鍵かもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-20 08:57

- - -

### [Federated Learning with Incomplete Sensing Modalities](http://arxiv.org/abs/2405.11828)

**不完全なセンシングモダリティを持つ連合学習**

Adiba Orzikulova, Jaehyun Kwak, Jaemin Shin, Sung-Ju Lee

- 移動と生理センサーが利用されるが、限られたバッテリーやセンサーの誤動作により利用が制限
- FLISMは不完全なモダリティに対応し、クライアント間でモデルの知識を転送
- 評価結果は3つの実データセットとシミュレーションで、FLISMが既存方法に比べ効率的
- FLISMはF1スコアが平均.067向上し、通信は2.69倍速く、計算は2.28倍効率的

FLISMの効果すごい！課題を解決しつつ効率も上げてるなんて、未来のモバイルアプリがもっと便利になりそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-20 06:53

- - -

### [FedCAda: Adaptive Client-Side Optimization for Accelerated and Stable Federated Learning](http://arxiv.org/abs/2405.11811)

**FedCAda: 連合学習の加速と安定のためのクライアントサイド最適化**

Liuzhi Zhou, Yu He, Kun Zhai, Xiang Liu, Sen Liu, Xingjun Ma, Guangnan Ye, Yu-Gang Jiang, Hongfeng Chai

- 連合学習でクライアントサイドの加速と安定化のバランスが課題
- FedCAdaはAdamアルゴリズムを利用し、クライアントでの推定修正とサーバの集約を最適化
- 初期段階では厳しい制約を導入し、進行につれて適応パラメータの影響を減少
- 広範な実験で最先端手法に対する適応性、収束性、安定性、全体的な性能で優位性を実証

実験結果がすごく気になるし、特に初期段階での制約ってどんな風に効くのか知りたい。これが明らかになったら、もっと強力な連合学習モデルができそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-20 06:12

- - -

### [Fed-Credit: Robust Federated Learning with Credibility Management](http://arxiv.org/abs/2405.11758)

**Fed-Credit: 信頼性管理による堅牢な連合学習**

Jiayan Chen, Zhirong Qian, Tianhui Meng, Xitong Gao, Tian Wang, Weijia Jia

- 連合学習(FL)は個々のデバイスからパラメータを集約するが、悪意あるデバイスがセキュリティリスクを引き起こす可能性がある
- 既存ソリューションは計算量が多いか、攻撃者の数や攻撃方法の事前知識を必要とするため制約が多い
- 提案するFed-Creditは事前知識不要で、信頼性セットを用いてクライアント貢献を評価し、時間衰退と態度価値を考慮した動的調整を行う
- MNISTやCIFAR-10データセットでの実験結果により、精度と耐攻撃性が向上し、特にデータ汚染攻撃に対して19.5%と14.5%の性能改善を示す

攻撃に対する耐性を確保しつつ、計算コストを抑えた新しいアプローチがとっても興味深いね！シンプルなのに効果的で、現実での応用も期待できそうだよ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-20 03:35

- - -

### [Decentralized Privacy Preservation for Critical Connections in Graphs](http://arxiv.org/abs/2405.11713)

**グラフにおける重要な接続の分散型プライバシー保護**

Conggai Li, Wei Ni, Ming Ding, Youyang Qu, Jianjun Chen, David Smith, Wenjie Zhang, Thierry Rakotoarivelo

- 実世界の多くの接続はグラフで表現されるが、その情報収集にはプライバシーとデータ有用性のバランスが重要
- 重要接続を保護するために、p-コヒージョンという要塞的なコヒーシブサブグラフモデルを提案
- 最少p-コヒージョン内の各参加者の重要接続を評価するための新しいメリットとペナルティスコア関数を設計
- 分散差分プライバシーメカニズム下で、重要接続を保護しつつ応答が$(\varepsilon, \delta)$-DDPを満たすことを証明

要塞的なサブグラフモデルとか、なんだか強そうで面白いね！実際のデータでも有効だなんて、これからのデータ保護に役立つかも！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, **投稿日時:** 2024-05-20 01:22

- - -

### [OFHE: An Electro-Optical Accelerator for Discretized TFHE](http://arxiv.org/abs/2405.11607)

**OFHE: 離散化されたTFHEのための電気光学アクセラレータ**

Mengxin Zheng, Cheng Chu, Qian Lou, Nathan Youngblood, Mo Li, Sajjad Moazeni, Lei Jiang

- DTFHEは、マルチビットメッセージを暗号化し準同型乗算、ルックアップテーブル操作、全領域ファンクショナルブートストラップをサポートする
- 既存のTFHEアクセラレータは、限定されたデータパスやビット幅の再構成性欠如によりDTFHE操作のサポートが困難
- OFHEはDTFHE操作の遅延を8.7%改善し、スループットを57%向上させた
- OFHEは1ワットあたりのスループットを94%向上させ、電力効率も大幅に改善

すごくおもしろそう！今後、この技術が広まればもっとセキュアなシステムが作れそうだよね。未来って本当にわくわくするね！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AR, **投稿日時:** 2024-05-19 16:27

- - -

### [Securing Health Data on the Blockchain: A Differential Privacy and Federated Learning Framework](http://arxiv.org/abs/2405.11580)

**ブロックチェーン上の健康データ保護:差分プライバシーと連合学習のフレームワーク**

Daniel Commey, Sena Hounsinou, Garth V. Crosby

- 健康データ解析と患者プライバシー保護の両立が課題
- 差分プライバシーと連合学習を活用して個人情報を保護
- ダイナミックなパーソナライズと適応的なノイズ配分でプライバシーとデータ有用性のバランスを実現
- 実験結果では高いプライバシー保証と64.50%の精度を達成し、ブロックチェーン統合も実用的であることを示す

ブロックチェーンと健康データの高度な融合、未来が開けそうな感じ！連合学習のプライバシー技術にもワクワクだね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.CY, cs.DC, cs.LG, **投稿日時:** 2024-05-19 15:15

- - -

### [Overcoming Data and Model Heterogeneities in Decentralized Federated Learning via Synthetic Anchors](http://arxiv.org/abs/2405.11525)

**分散型連合学習における合成アンカーを用いたデータおよびモデルの不均一性の克服**

Chun-Yin Huang, Kartik Srinivas, Xin Zhang, Xiaoxiao Li

- 分散型FLではサーバーレスネットワークを利用し、クライアントが異なるローカルモデルを最適化
- グローバルモデルの欠如によりモデルの一般化能力が低下する可能性がある
- 本研究では合成アンカーを導入したDeSAという新技術を提案
- DeSAは異なるクライアント間での知識移転を促進し、精度を向上させることが示された

合成アンカーかなり面白い！クライアント間の知識のやり取りがうまくいくと、全員がもっといいモデルを作れるってことかもね。

**Comment:** Paper Accepted at ICML 2024, 23 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-19 11:36

- - -

### [A GAN-Based Data Poisoning Attack Against Federated Learning Systems and Its Countermeasure](http://arxiv.org/abs/2405.11440)

**連合学習システムに対するGANベースのデータポイズニング攻撃とその対策**

Wei Sun, Bo Gao, Ke Xiong, Yuwei Wang, Pingyi Fan, Khaled Ben Letaief

- FLはプライベートデータセットで共同学習するが、直接のデータアクセスはない。
- 従来のポイズニング攻撃は統計異常を引き起こしやすく、完全には成功しない。
- 新しい攻撃モデルVagueGANにより、合法に見えるがノイズを含むデータ生成が可能。
- Model Consistency-Based Defense (MCD)により、GANポイズニングされたデータやモデルの識別ができる。

「VagueGAN」なんて名前がかっこいいし、実際の連合学習がどれだけ影響受けるのか気になるね！あと、防御策もちゃんとあるのが実用的で安心だなって思う。

**Comment:** 18 pages, 16 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, cs.NI, **投稿日時:** 2024-05-19 04:23

- - -

### [Sketches-based join size estimation under local differential privacy](http://arxiv.org/abs/2405.11419)

**ローカル差分プライバシーに基づくスケッチを用いた結合サイズ推定**

Meifan Zhang, Xin Liu, Lihua Yin

- 敏感データの結合サイズ推定は、プライバシー漏洩のリスクがある
- ローカル差分プライバシー（LDP）はプライバシーを保護するが、大規模ドメインではノイズを多く導入する
- スケッチを用いることで大規模ドメインの処理が可能になるが、ハッシュ衝突エラーが発生
- 新アルゴリズムLDPJoinSketchとLDPJoinSketch+により、ノイズエラーとハッシュ衝突エラーを低減

新しいアルゴリズムでプライバシーも精度も両立できるなんてすごいね。特にLDPJoinSketch+で高頻度アイテムと低頻度アイテムを分けられるのが面白そう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DB, cs.CR, **投稿日時:** 2024-05-19 01:21

- - -

### [NTTSuite: Number Theoretic Transform Benchmarks for Accelerating Encrypted Computation](http://arxiv.org/abs/2405.11353)

**NTTSuite: 暗号化計算を加速するための数論的変換ベンチマーク**

Juran Ding, Yuanzhe Liu, Lingbin Sun, Brandon Reagen

- プライバシー保護計算の注目度が高まっており、準同型暗号が注目されている
- 高い計算オーバーヘッドのため、準同型暗号の導入が進まない
- NTTSuiteというベンチマークスイートを開発し、数論的変換（NTT）の速度低下の研究を促進
- 提案された最適化により、我々の実装は最先端技術に比べ30%の性能向上を果たしている

準同型暗号の実用化が進むと、データの安全性が飛躍的に向上しそう！実装の30%向上ってすごいよね、楽しみ～。

**Comment:** 8 pages, 5 figures, and two tables. To download the source code, see   https://github.com/Dragon201701/NTTSuite

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AR, **投稿日時:** 2024-05-18 17:44

- - -

### [Advancing fNIRS Neuroimaging through Synthetic Data Generation and Machine Learning Applications](http://arxiv.org/abs/2405.11242)

**合成データ生成と機械学習アプリケーションによるfNIRSニューロイメージングの進展**

Eitan Waks

- 高品質な神経イメージングデータセットの不足に対処し、Monte Carloシミュレーションとパラメトリックヘッドモデルを用いて包括的な合成データセットを生成
- DockerとXarrayを使用して標準化され再現可能なデータ分析を可能にするコンテナ化環境を開発
- クラウドベースのインフラを構築しスケーラブルなデータ生成と処理を実現し、ニューロイメージングデータのアクセシビリティと品質を向上
- 合成データ生成と機械学習技術の組み合わせにより、fNIRSトモグラフィーの精度、効率、適用性を向上させ、神経疾患の診断と治療戦略に革命をもたらす可能性

合成データ生成でデータ不足をクリアしちゃうなんてすごいよね！fNIRSの技術がもっと進化して、早く実用化されるといいな～。

**Comment:** 21 pages, 12 figures

**トピック:** [合成データ](sd), **カテゴリ:** eess.SP, cs.LG, physics.med-ph, stat.ML, **投稿日時:** 2024-05-18 09:50

- - -

### ["What do you want from theory alone?" Experimenting with Tight Auditing of Differentially Private Synthetic Data Generation](http://arxiv.org/abs/2405.10994)

**理論から何を求める？ 差分プライバシー合成データ生成の高精度監査の実験**

Meenatchi Sundaram Muthu Selva Annamalai, Georgi Ganev, Emiliano De Cristofaro

- 差分プライバシー合成データ生成（DP-SDG）は機密データに類似したデータセットを作成
- 実装やアルゴリズムのバグにより、理論的な情報漏洩保証が実際に守られるか確認
- ブラックボックスモデルではDP-SDGの情報漏洩推定に限界が見られた
- 提案された手法で新たな違反を発見し、高精度監査の重要性を示した

新しい攻撃手法を使って理論と実際の乖離を明らかにするこの手法、めっちゃおもしろいね！これがうまく応用されたら、データのプライバシーがさらに強固になるかもだよね。

**Comment:** To appear at Usenix Security 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-16 14:23
