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

更新: 2024-11-03T04:20:37.706873

- - -

### [Federated Black-Box Adaptation for Semantic Segmentation](http://arxiv.org/abs/2410.24181)

**意味セグメンテーションのための連合ブラックボックス適応**

Jay N. Paranjape, Shameema Sikder, S. Swaroop Vedula, Vishal M. Patel

- 連合学習は複数の組織がデータを共有せずに共通のモデルを学ぶことができる技術
- 従来の手法では、データのプライバシーが完全に守られない可能性があると指摘されている
- 提案したBlackFedはモデル構造や勾配を交換せずにプライバシーを向上
- 零次最適化と一次最適化を活用して効果を評価し成果を示した

ゼロ知識のアプローチでデータを活用できるなんてすごく面白いよね！これが普及したら、プライバシーを守りながらもたくさんのデータを活用した進化が起こるかもってドキドキしちゃう！

**Comment:** Accepted at NEURIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-31 17:45

- - -

### [Conformalized Prediction of Post-Fault Voltage Trajectories Using Pre-trained and Finetuned Attention-Driven Neural Operators](http://arxiv.org/abs/2410.24162)

**事前学習と微調整された注意駆動型ニューラルオペレーターによる故障後電圧軌跡のコンフォーマル化予測**

Amirhossein Mollaali, Gabriel Zufferey, Gonzalo Constante-Flores, Christian Moya, Can Li, Guang Lin, Meng Yue

- 電力システムの故障後電圧軌跡を予測する新手法を提案
- Quantile Attention-Fourier Deep Operator Network (QAF-DeepONet)を設計し、複雑な電圧軌跡を捕捉
- 連合学習を活用し、データプライバシーを保ちながら事前学習を実施
- 予測範囲を保証するため、コンフォーマル予測を統合し、評価指標で高評価を得た

電力システムの電圧予測って、なんか難しそうでも、めっちゃ実用的！色々な技術が詰まってて、未来の電力インフラの安定化に生かされるといいな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-31 17:20

- - -

### [On Sampling Strategies for Spectral Model Sharding](http://arxiv.org/abs/2410.24106)

**スペクトルモデル分割のサンプリング戦略に関する研究**

Denis Korzhenkov, Christos Louizos

- 連合学習における異質なクライアント問題が注目されている
- スペクトルモデル分割において、特定の最適化問題を解いた2つのサンプリング戦略を提案
- 1つは元の重みの無偏推定、もう1つは近似誤差の最小化を目指す
- これらの方法が様々なデータセットでパフォーマンス向上に寄与することを実証

スペクトルモデルを使うなんて、ちょっと難しそうだけど面白い話だね！異質なクライアント問題とか、解決できたらすごいことになりそう！

**Comment:** Accepted to NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-31 16:37

- - -

### [Unveiling Synthetic Faces: How Synthetic Datasets Can Expose Real Identities](http://arxiv.org/abs/2410.24015)

**合成顔の暴露：合成データセットがどのように実際のアイデンティティを明らかにするか**

Hatef Otroshi Shahreza, Sébastien Marcel

- 合成データ生成は視覚応用で人気だが、プライバシー問題が存在
- 合成顔データセットは生成モデルに依存しつつ、実データ情報も漏れる可能性がある
- 合成顔認識データセット6つを分析し、実データからの情報漏洩を全体で確認
- この研究は、生成モデルからのデータ漏洩を初めて検証し、責任ある合成生成の道筋を示す

合成データのプライバシーの落とし穴が分かってドキドキするね。これをきっかけに、もっと安全なデータセットがいっぱい出てくるといいな～。未来のテクノロジーがどう変わっていくのか楽しみ♪

**Comment:** Accepted in NeurIPS 2024 Workshop on New Frontiers in Adversarial   Machine Learning

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-31 15:17

- - -

### [Space-bounded quantum interactive proof systems](http://arxiv.org/abs/2410.23958)

**空間制約付き量子対話証明システム**

François Le Gall, Yupan Liu, Harumichi Nishimura, Qisheng Wang

- 2つの空間制約付き量子対話証明システムモデルを導入
- ${\sf QIPL}$はログサイズの測定を含み、${\sf NP}$を正確に特徴付ける
- ${\sf QIP_{\rm U}L}$は単位的な回路のみに制限され、${\sf P}$に含まれる
- 統計的ゼロ知識を持つ${\sf QSZK_{\rm U}L}$が${\sf BQL}$と等しく、対話の利点を失う

量子系での対話ってすごく面白そう！特に、空間制約の中でどうやって証明を行うかが気になるよね。これが進むと、新しい量子コンピュータのアルゴリズムとかに繋がるのかもしれないね！

**Comment:** 50 pages, 4 figures

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** quant-ph, cs.CC, **投稿日時:** 2024-10-31 14:11

- - -

### [Towards Fast Algorithms for the Preference Consistency Problem Based on Hierarchical Models](http://arxiv.org/abs/2410.23934)

**階層モデルに基づく選好整合性問題の高速アルゴリズムに向けて**

Anne-Marie George, Nic Wilson, Barry O'Sullivan

- 階層モデルを用いた選好整合性問題は、NP完全である
- 問題の解決法として、混合整数線形計画法と2つの再帰アルゴリズムを開発
- 再帰アルゴリズムは、探索空間を狭める特性を活用し高速化を実現
- 合成データでの実験で、再帰アルゴリズムがMILP法よりも極めて速く動作することが判明

階層モデルを使って、より効率的なアルゴリズムが作れるんだね。ただ、再帰アルゴリズムがMILPよりも速いってどんな速さなのか気になる！進化した先の未来が楽しみだな～。

**Comment:** Longer Version of IJCAI'16 publication   https://www.ijcai.org/Proceedings/16/Papers/157.pdf

**トピック:** [合成データ](sd), **カテゴリ:** cs.LO, cs.AI, **投稿日時:** 2024-10-31 13:48

- - -

### [QuACK: A Multipurpose Queuing Algorithm for Cooperative -Armed Bandits](http://arxiv.org/abs/2410.23867)

**QuACK: 協力的なk-アームドバンディットのための多目的キューイングアルゴリズム**

Benjamin Howson, Sarah Filippi, Ciara Pike-Burke

- 複数のエージェントが協力して最適な行動を見つける問題を研究
- 単一エージェントアルゴリズムを任意に多エージェント設定に拡張可能
- 単一プレイヤーのアルゴリズムの後悔保証を多エージェントにも適用可能
- 提案手法が特化型アルゴリズムを超える性能を実証

この論文、めっちゃ面白そう！マルチエージェントで協力しちゃうところが未来っぽいよね。どのアルゴリズムにも応用できるって、可能性がめちゃ広がるじゃん！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-31 12:20

- - -

### [Generative AI-Powered Plugin for Robust Federated Learning in Heterogeneous IoT Networks](http://arxiv.org/abs/2410.23824)

**異種IoTネットワークにおける堅牢な連合学習のための生成AI駆動プラグイン**

Youngjoon Lee, Jinu Gong, Joonhyuk Kang

- 連合学習はデータをローカルに保ちながら協調的にグローバルモデルをトレーニング
- デバイス間のデータ分布の偏りがモデル収束を妨げ、性能を低下させる
- 生成AIを用いてデータを合成し、不足クラスの情報を補完し均衡を図る
- バランスの取れたサンプリングにより収束を加速、データ不足環境でも柔軟に対応

この技術、すごく面白そう！生成AIでデータを補うとか、未来の研究にもいろいろ可能性が広がりそうだね。連合学習がもっと広がって、プライバシーも守りつつ賢いAIがいっぱい生み出される未来が楽しみ！

**Comment:** 8 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-10-31 11:13

- - -

### [Local Superior Soups: A Catalyst for Model Merging in Cross-Silo Federated Learning](http://arxiv.org/abs/2410.23660)

**ローカルスーペリアスープ: クロスサイロ連合学習におけるモデル統合の触媒**

Minghui Chen, Meirui Jiang, Xin Zhang, Qi Dou, Zehua Wang, Xiaoxiao Li

- 連合学習は分散データでモデルを共同訓練するが、事前学習モデルの複雑さが通信ラウンドの課題を増加
- 通信コスト問題に対処し、事前学習モデル適応を改善するために、ローカルモデル補間技術「ローカルスーペリアスープ」を提案
- 「ローカルスーペリアスープ」は、クライアント間で低損失領域を探索し、通信ラウンドを減らす手法
- 提案手法は、多様な連合学習データセットで効果的かつ効率的であることを実証

既存の連合学習の問題を解決する新手法の名前が「ローカルスーペリアスープ」って面白いよね！名前もユニークだし、実際に効率を上げる方法として役立ちそう。この分野ますます注目されそうだね。

**Comment:** Accepted at NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-31 06:20

- - -

### [Biologically-Inspired Technologies: Integrating Brain-Computer Interface and Neuromorphic Computing for Human Digital Twins](http://arxiv.org/abs/2410.23639)

**生物に着想を得た技術: 人間デジタルツインのためのブレイン−コンピュータインターフェースとニューロモルフィックコンピューティングの統合**

Chen Shang, Jiadong Yu, Dinh Thai Hoang

- 人間デジタルツイン(HDT)構築には、データ収集の異質性や高エネルギー消費とプライバシーが課題。
- ブレイン−コンピュータインターフェース(BCI)センサー技術で脳信号を収集し、HDTの効率的なデータ収集と個別化の強化を図る。
- スパイキングニューラルネットワーク(SNN)に基づくニューロモルフィック学習モデルで、脳の情報処理を模倣しつつエネルギー消費を削減。
- フェデレーテッドラーニング(FL)を統合し、データプライバシーを強化するためのモデルを提案。

このアプローチってすごく未来的！データのプライバシー問題もちゃんと考えてるし、脳の働きに着想を得たモデルってどんなことができるんだろう、ワクワクする～。これからのHDTはどんな進化を遂げるのか、楽しみだよね！

**Comment:** 8 pages, 4 figures,

**トピック:** [連合学習](fl), **カテゴリ:** cs.HC, cs.NI, **投稿日時:** 2024-10-31 05:21

- - -

### [Development and Comparative Analysis of Machine Learning Models for Hypoxemia Severity Triage in CBRNE Emergency Scenarios Using Physiological and Demographic Data from Medical-Grade Devices](http://arxiv.org/abs/2410.23503)

**救急シナリオにおける低酸素血症重症度トリアージのための機械学習モデル開発と比較分析**

Santino Nanini, Mariem Abid, Yassir Mamouni, Arnaud Wiedemann, Philippe Jouvet, Stephane Bourassa

- CBRNE状況での低酸素血症予測に機械学習モデルを開発し、医療グレードデータを活用
- 勾配ブースティングモデルは学習速度、解釈能力、信頼性で優れ、リアルタイム意思決定に適している
- NEWS2+から重要な生理学的変数を用いることで、予測精度の向上を実現
- 将来的には複数の病院のデータを統合し、モデルの一般化能力向上を目指す

機械学習で緊急時の判断がもっとスマートになるってことだね！リアルタイムで使えるなら、きっと現場で役立つに違いない！将来的にはさらに多くのデータと組み合わせてもっと汎用性の高いものになるといいな。

**Comment:** 12 figures, 12 tables and 39 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-30 23:24

- - -

### [PACER: Preference-conditioned All-terrain Costmap Generation](http://arxiv.org/abs/2410.23488)

**PACER: 好みを条件とした全地形コストマップ生成**

Luisa Mao, Garrett Warnell, Peter Stone, Joydeep Biswas

- 現在の自律ロボットでは、地形は事前に訓練されたセマンティック分類器でラベル付けされ、コストが割り当てられる
- しかし、この方法だと既知の地形に対するユーザーの好みしか反映できない
- PACERは、新たな地形でのユーザーの好みに迅速に対応できるコストマップ生成手法を提案
- 実データと合成データを使った評価で、従来手法よりも広く適応できることを示した

PACERって、まるでオーダーメイドの道を作ってくれちゃうみたいで楽しそう！どんな地形でも、それぞれの好みに合わせて対応してくれるから、ロボットたちはもっと自由に動ける時代が来るかもね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.CV, **投稿日時:** 2024-10-30 22:43

- - -

### [Communication-Efficient Federated Learning over Wireless Channels via Gradient Sketching](http://arxiv.org/abs/2410.23424)

**ワイヤレスチャネル上での勾配スケッチングによる通信効率の良い連合学習**

Vineet Sunil Gattani, Junshan Zhang, Gautam Dasarathy

- ワイヤレス多元接続チャネルでの大規模連合学習は重要だが、帯域幅制限やデータの不均一性が課題。
- FPSを提案し、帯域幅制限に対処するためにカウントスケッチ構造を使用し圧縮を効率化。
- FPSの損失関数を改良し、データ不均一性に対応できるよう調整し、収束性も確認。
- 理論と数値実験で、FPSの安定性や精度、効率性を確認し、現行手法と比較して有望であると示された。

これ、めっちゃ面白いよね！データの不均一性に対処しているところがすごく実用的。無線通信での連合学習の新しい可能性が広がりそう♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-30 20:01

- - -

### [Multilingual Vision-Language Pre-training for the Remote Sensing Domain](http://arxiv.org/abs/2410.23370)

**リモートセンシング領域における多言語視覚言語事前学習**

João Daniel Silva, Joao Magalhaes, Devis Tuia, Bruno Martins

- CLIPの手法はリモートセンシングデータの視覚と言語タスクで広く使われている
- 提案手法は多言語CLIPモデルの微調整と自己教師あり手法を用いる
- 英語キャプション付き画像データセットを多言語に自動翻訳し学習に利用
- 提案モデルRS-M-CLIPは多言語画像テキスト検索やゼロショット分類で成果

多言語対応なんてワクワクする！リモートセンシングがもっと便利になる予感がするね！提案モデルで画像検索がさらに進むといいなぁ。

**Comment:** Accepted at ACM SIGSPATIAL 2024 - Research Papers

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-30 18:13
