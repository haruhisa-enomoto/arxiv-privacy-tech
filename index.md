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

更新: 2024-11-07T04:22:17.644530

- - -

### [Fed-EC: Bandwidth-Efficient Clustering-Based Federated Learning For Autonomous Visual Robot Navigation](http://arxiv.org/abs/2411.04112)

**Fed-EC: 自律型視覚ロボットナビゲーションのための帯域幅効率の高いクラスタリングベースの連合学習**

Shreya Gummadi, Mateus V. Gasparino, Deepak Vasisht, Girish Chowdhary

- 中央集約型学習はデータプライバシーと帯域幅の消費に課題を抱える
- 連合学習は1つのグローバルモデルを学ぶが環境によっては不適合な場合もある
- Fed-ECは多様な環境で動作するロボットに適したクラスタリングベースの連合学習を提案
- Fed-ECはコミュニケーションサイズを23倍削減しつつ性能を維持し、新たなロボットへのモデル転送が可能

ロボットが環境に応じた学習をするなんてすごいね！どんな場所でも適応できるロボットがもっと増えていけばいいなぁって思ったよ！これからのロボティクスの発展が楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, cs.AI, cs.CV, cs.DC, **投稿日時:** 2024-11-06 18:44

- - -

### [Towards Resource-Efficient Federated Learning in Industrial IoT for Multivariate Time Series Analysis](http://arxiv.org/abs/2411.03996)

**産業用IoTにおける多変量時系列解析のためのリソース効率的な連合学習への取り組み**

Alexandros Gkillas, Aris Lalos

- 産業応用で異常や欠損データが問題で、深層学習による異常検知が重要視されているが、そのための大きなニューラルネットはコストが高い。
- ユーザープライバシーを含むデータはエッジデバイスで収集され、プライバシーを守るために連合学習を用いる必要がある。
- 処理、ストレージ、通信の課題に対処するため、ニューラルネットのプルーニングを活用し効率化を図る。
- 提案された圧縮ベースの手法は、高い圧縮率を達成し、性能損失が最小限であることが実験で示された。

プライバシーも守りつつ異常検知の精度を保てるのすごいよね！最先端技術で今後さらに効率が上がるといいな〜。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, eess.SP, **投稿日時:** 2024-11-06 15:38

- - -

### [GUIDE-VAE: Advancing Data Generation with User Information and Pattern Dictionaries](http://arxiv.org/abs/2411.03936)

**GUIDE-VAE: ユーザー情報とパターン辞書によるデータ生成の進化**

Kutay Bölat, Simon Tindemans

- 多ユーザーデータセットでの生成モデリングで、従来のモデルはユーザー情報を無視しがちである
- GUIDE-VAEはユーザー埋め込みを利用し、ユーザー指導型データ生成を実現する革新モデルである
- パターン辞書を活用し、複雑な特徴の依存関係を捉え、生成サンプルの現実性を向上
- GUIDE-VAEは不均衡なデータの中で合成データ生成と欠損データ補完で効果を発揮する

ユーザー情報をうまく活用したデータ生成って、いろんなところで役立ちそう！ガイド付きデータ生成はAIの未来をもっと面白くしてくれそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-11-06 14:11

- - -

### [Act in Collusion: A Persistent Distributed Multi-Target Backdoor in Federated Learning](http://arxiv.org/abs/2411.03926)

**共謀する: 連合学習における持続的分散型多ターゲットバックドア**

Tao Liu, Wu Yang, Chen Xu, Jiguang Lv, Huanran Wang, Yuhang Zhang, Shuchun Xu, Dapeng Man

- 連合学習はデータプライバシーを保護するが、分散型のためバックドア攻撃に弱い。
- 提案した分散型多ターゲットバックドアモデルでは、複数の攻撃者が異なるクラスにバックドアを仕込む。
- 現存の方法では、複数のバックドアを持続的に維持するのが困難であることを実証している。
- 提案手法DMBAにより、バックドア効果を持続的に維持し、93%以上の成功率を達成している。

連合学習が守らなきゃいけないってことはみんな考えてたけど、こんなに巧妙な攻撃があるんだね。面白けどちょっと怖いかも。でも、これを防ぐ術が見えてくると、一歩先に進むことができそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-06 13:57

- - -

### [FedRISE: Rating Induced Sign Election of Gradients for Byzantine Tolerant Federated Aggregation](http://arxiv.org/abs/2411.03861)

**FedRISE: Byzantine耐性連合学習のための勾配選定による評価誘導**

Joseph Geo Benjamin, Mothilal Asokan, Mohammad Yaqub, Karthik Nandakumar

- フェデレーテッドラーニングにおけるモデル毒性を防ぐために、ロバストなアグリゲーターを使用する
- 強力な攻撃はアグリゲーターを崩壊させる可能性があることが観察されている
- FedRISEは異なる勾配方向を選定することで、全知の攻撃者に対抗するために開発された
- FedRISEは厳格な勾配の包含式により、高い堅牢性を示す

FedRISEって、どんな攻撃にも対応できるアグリゲーターなんだね！これを使えば、フェデレーテッドラーニングがもっと安全で信頼できるものになりそう♪

**Comment:** This is a work under submission/review process

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.CR, **投稿日時:** 2024-11-06 12:14

- - -

### [Attribute-Based Encryption With Payable Outsourced Decryption Using Blockchain and Responsive Zero Knowledge Proof](http://arxiv.org/abs/2411.03844)

**ブロックチェーンと応答性ゼロ知識証明を用いた支払い可能な属性ベース暗号のアウトソーシング解除**

Dongliang Cai, Borui Chen, Liang Zhang, Kexin Li, Haibin Kan

- 属性ベース暗号（ABE）はクラウドサービスのアクセス制御に有望だが、復号コストが普及の妨げ
- 復号をクラウドサービスに委託するアプローチの問題は、誤解から逃れる仕組みが不足していること
- 本研究はブロックチェーンを利用し、ゼロ知識証明での検証やオプショナルのシングルラウンドチャレンジで高コストを解決
- イーサリアム上での実験により、この属性ベース暗号スキームの効率性と実現可能性が確認された

ゼロ知識証明を使っているのが面白いよね！ブロックチェーンで公平性を実現できるなんて、未来のクラウドサービスがもっと安心できそう！

**Comment:** 12 pages, 5 figures

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-11-06 11:26

- - -

### [Overcoming label shift in targeted federated learning](http://arxiv.org/abs/2411.03799)

**ターゲット連合学習におけるラベルシフトの克服**

Edvin Listo Zec, Adam Breitholtz, Fredrik D. Johansson

- 連合学習はデータを共有せずに複数アクターがモデルを共同訓練できる技術である
- ラベルシフトがあるとモデル性能が低下し、実際のアプリケーションで問題となる
- 提案手法FedPALSはラベルシフトに適応し、目標ラベル分布の知識を活用する
- FedPALSは標準的手法より優れ、ターゲットドメインとのモデル整合を図る

FedPALSって連合学習のラベルシフト問題を解決してくれそう！これからますますプライバシーを守りながら、いろんなデータで機械学習が進化しちゃいそうでワクワクするね！次世代のAIってこんな感じなのかな？



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-06 09:52

- - -

### [VQA:Visual Question Answering for Video Quality Assessment](http://arxiv.org/abs/2411.03795)

**VQA$^2$: ビデオ品質評価のための視覚的質問応答**

Ziheng Jia, Zicheng Zhang, Jiaying Qian, Haoning Wu, Wei Sun, Chunyi Li, Xiaohong Liu, Weisi Lin, Guangtao Zhai, Xiongkuo Min

- 大規模マルチモーダルモデルの進展により、ビデオ関連コンピュータビジョンでのVQAによる新たな訓練・推論法が生まれた
- 低レベル映像評価の分野であったVQAが、視覚的品質理解へと進化中 
- VQA2 Instruction Datasetは初のビデオ品質評価特化の視覚的質問応答データセット
- VQA2シリーズモデルは品質スコアリングで最先端の成果を出し、GPT-4oを超える性能を示した

これってめっちゃ面白そうじゃない！？だって、動画の品質評価って、AIがどんどん賢くなってきてるのに、まだまだ手付かずな部分が多いんだって！VQAでそんな課題をガンガン解決しちゃう未来がすぐそこに来てる感じするね！

**Comment:** 10 pages 3 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-11-06 09:39

- - -

### [Optimal Defenses Against Gradient Reconstruction Attacks](http://arxiv.org/abs/2411.03746)

**勾配再構成攻撃に対する最適防御策**

Yuxiao Chen, Gamze Gürsoy, Qi Lei

- 連合学習はデータ漏洩防止を目的とするが、勾配再構成攻撃の脆弱性がある
- ノイズ付加と勾配プルーニングの手法は再構成誤差の理論的下限を計算
- 手法をパラメータ・モデルごとに最適化し、データ漏洩と実用性の最適なバランスを達成
- 実験結果は、従来手法よりもデータ保護と実用性の向上を示す

勾配再構成攻撃って、秘密のデータを取り出されちゃう怖いことなんだね。だけど、この論文の方法なら安心！実用性も高く保てるから、すごく素敵じゃない？みんなのデータを守る未来があるのかも！

**Comment:** The code for this project is available at   https://github.com/cyx78/Optimal_Defenses_Against_Gradient_Reconstruction_Attacks

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, stat.ML, **投稿日時:** 2024-11-06 08:22

- - -

### [NeurIPS 2023 Competition: Privacy Preserving Federated Learning Document VQA](http://arxiv.org/abs/2411.03730)

**NeurIPS 2023コンペティション: プライバシー保護連合学習による文書VQA**

Marlon Tobaben, Mohamed Ali Souibgui, Rubèn Tito, Khanh Nguyen, Raouf Kerkouche, Kangsoo Jung, Joonas Jälkö, Lei Kang, Andrey Barsky, Vincent Poulain d'Andecy, Aurélie Joseph, Aashiq Muhamed, Kevin Kuo, Virginia Smith, Yusuke Yamasaki, Takumi Fukami, Kenta Niwa, Iifan Tyou, Hiro Ishii, Rio Yokota, Ragul N, Rintu Kutum, Josep Llados, Ernest Valveny, Antti Honkela, Mario Fritz, Dimosthenis Karatzas

- プライバシーを保ちつつ連合学習で請求書処理を行う課題に挑む競技
- 既存の多モーダル言語モデルを利用し、リアルな請求書データセットで微調整を行う
- トラック1では通信コスト削減とユーティリティの維持、トラック2では差分プライバシーで情報保護を目指す
- プライバシー重視の連合学習手法のテストベッドとして活用し、将来のプライバシー対策の成功例を提供

新しい連合学習の挑戦って感じだね！請求書のプライバシーを守りながら処理するなんて、実生活で活かされそう！未来ではもっとプライバシーが守られる世界になりそうでワクワクするよね。

**Comment:** 27 pages, 6 figures

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.CV, **投稿日時:** 2024-11-06 07:51

- - -

### [Where Do We Stand with Implicit Neural Representations? A Technical and Performance Survey](http://arxiv.org/abs/2411.03688)

**暗黙的ニューラル表現の現状は？技術的および性能の調査**

Amer Essakine, Yanqi Cheng, Chun-Wun Cheng, Lipei Zhang, Zhongying Deng, Lei Zhu, Carola-Bibiane Schönlieb, Angelica I Aviles-Rivero

- 暗黙的ニューラル表現（INR）は柔軟性と性能が高く、解像度独立性やメモリ効率に優れる。
- INRは音声や画像、3Dオブジェクトの再構成、高次元データの合成で効果的とされる。
- 研究はINRをカテゴリー分けし、活性化関数や位置エンコーディングなど4つの領域で分析。
- 課題としては活性化関数の表現力向上、位置エンコーディングの改善、スケーラビリティ拡大がある。

これ、本当に面白そう！未来のAI技術の発展にどんな影響があるか考えるとワクワクしちゃう。特に画像や3Dの再構成の進化って、私たちが日常で体験することをどう変えるんだろう？



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-06 06:14

- - -

### [Privacy-Preserving Resilient Vector Consensus](http://arxiv.org/abs/2411.03633)

**プライバシー保護の強靱なベクター合意**

Bing Liu, Chengcheng Zhao, Li Chai, Peng Cheng, Jiming Chen

- マルチエージェントシステムでのプライバシー保護される強靱な合意形成問題を研究
- 差分プライバシーの一種である集中ジオプライバシーを用いる
- PP-ADRCでは多変量ガウスノイズを加えてエージェントの状態をプライバシー保護
- 収束精度をマハラノビス距離とハウスドルフ距離で評価し、理論を数値シミュレーションで実証

プライバシーを守りながらも合意形成を行うアイデアってすごく未来的だよね！これでシステムの信頼性もグッと上がるかも。技術の進歩で、もっと安全な社会が実現できるってワクワクするね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-11-06 03:17

- - -

### [Towards Personalized Federated Learning via Comprehensive Knowledge Distillation](http://arxiv.org/abs/2411.03569)

**包括的な知識蒸留によるパーソナライズド連合学習の実現に向けて**

Pengju Wang, Bochao Liu, Weijia Guo, Yong Li, Shiming Ge

- 連合学習はプライバシーを保護する分散型機械学習パラダイムである
- データの不均一性により、学習モデルは以前の知識を忘れやすい
- 提案手法はグローバルモデルと履歴モデルを教師として活用
- 知識蒸留を通じて、忘却を軽減し個別モデルの性能を向上

知識蒸留を使って、いろんな情報をしっかりと学べるところが面白そう！個別化と汎用化のバランスを取るのが大変そうだけど、きっとすっごく役に立つ方法になるはずだよね！🌟

**Comment:** Accepted by IEEE SMC 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, cs.CV, **投稿日時:** 2024-11-06 00:17

- - -

### [Forecasting Outside the Box: Application-Driven Optimal Pointwise Forecasts for Stochastic Optimization](http://arxiv.org/abs/2411.03520)

**型にはまらない予測: 確率最適化のためのアプリケーション駆動型最適点予測**

Tito Homem-de-Mello, Juan Valencia, Felipe Lagos, Guido Lagos

- コンテクスト情報を活用して、データ駆動の確率最適化問題の精度を向上
- マシンラーニングで得られるのは点推定で、分布全体ではないことが課題
- 固定再起行列と固定コストの二段階確率プログラムは一つのシナリオで解決可能
- 提案した手法は実証実験で既存手法と比較して良好な結果を示す

マシンラーニングってすごく幅広い応用があるんだね！単なる予測に留まらず、最適化問題にも活用できちゃうあたり、未来はもっと便利になりそうだね。しかも、ほんのひとつのシナリオで解決できるっていうのも、省エネでいい感じ！

**Comment:** Submitted for publication

**トピック:** [合成データ](sd), **カテゴリ:** math.OC, cs.LG, 90C15, **投稿日時:** 2024-11-05 21:54

- - -

### [Enhancing Table Representations with LLM-powered Synthetic Data Generation](http://arxiv.org/abs/2411.03356)

**LLMを活用した合成データ生成によるテーブル表現の強化**

Dayu Yang, Natawut Monaikul, Amanda Ding, Bozhao Tan, Kishore Mosaliganti, Giri Iyengar

- データ駆動型の意思決定において、テーブルの表現と推薦システムの効率化が重要。
- 既存の手法はセルレベルに限定され、高品質な訓練データが不足している。
- LLMを利用した新しい合成データ生成パイプラインを提案、大規模な合成データセットを作成。
- この合成データがテーブルの類似性を高め、推薦のパフォーマンスが向上することを示した。

LLMを使って合成データでテーブルの表現を強化するなんて、なんだか近未来な感じ！ぜひ使ってみたいよね。これでデータ管理や分析がもっと効率的になれば、研究者にも嬉しい技術だと思うな。

**Comment:** the Thirty-Eighth Annual Conference on Neural Information Processing   Systems Table Representation Workshop

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-04 19:54

- - -

### [Tabular Data Synthesis with Differential Privacy: A Survey](http://arxiv.org/abs/2411.03351)

**差分プライバシーによる表形式データ合成の調査**

Mengmeng Yang, Chi-Hung Chi, Kwok-Yan Lam, Jie Feng, Taolin Guo, Wei Ni

- 表形式のデータを個人情報と切り離し、合成データを生成することでプライバシー問題に対処する。
- 背景知識を用いた攻撃への対策として差分プライバシーを導入し、プライバシー保護を強化する。
- 差分プライバシー制約下での表形式データ生成モデルを統計的アプローチと深層学習アプローチに分類。
- 各アプローチの効用、プライバシー、計算複雑性を評価し、データ合成の質を測る評価方法も提案。

データが安全にシェアできるようになると、いろんな分野でビッグデータが活用されそうでワクワクするね！特に、差分プライバシーがどうやって攻撃から守るか、今後ももっと知りたくなる内容だよね。



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.DB, **投稿日時:** 2024-11-04 06:32

- - -

### [OML: Open, Monetizable, and Loyal AI](http://arxiv.org/abs/2411.03887)

**OML: オープンで収益化可能、かつ信頼できるAI**

Zerui Cheng, Edoardo Contente, Ben Finch, Oleg Golev, Jonathan Hayase, Andrew Miller, Niusha Moshrefi, Anshul Nasery, Sandeep Nailwal, Sewoong Oh, Himanshu Tyagi, Pramod Viswanath

- 現在のAI開発は少数の組織が集中管理し、予期せぬ結果をもたらすことがある
- OMLはAI、ブロックチェーン、暗号技術を用いてAI開発を民主化するアプローチ
- AIネイティブ暗号という新科学分野を提案し、AIデータ表現を活用した安全性向上を図る
- モデルの所有権と整合性を守るためモデル指紋技術を使用し、権力集中を防ぐ

AIがもっとみんなで開発できる時代が来るかもね！ブロックチェーンで透明性が高まるのも良さそうだし、一緒に進化していくAIの未来が楽しみだね～。

**Comment:** 60 pages, 22 figures

**トピック:** [準同型暗号](he), [TEE](tee), **カテゴリ:** cs.AI, cs.CR, **投稿日時:** 2024-11-01 18:46
