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

更新: 2024-11-24T04:22:21.093632

- - -

### [Learning Fair Robustness via Domain Mixup](http://arxiv.org/abs/2411.14424)

**公正なロバスト性を学習するためのドメインミックスアップ**

Meiyu Zhong, Ravi Tandon

- 従来の敵対的学習は全体的なロバスト性を向上させるが、クラス毎の公平性は保証されない
- 同クラスの入力をミックスアップし、敵対的学習を行う手法を提案
- 理論的解析により、線形分類器のクラス毎ロバスト性格差を低減できることを示す
- 合成データやCIFAR-10データセットでの実験により、自然リスクと敵対的リスクの格差改善を確認

提案されたミックスアップ手法って、なんか面白そう！全てのクラスをもっと公正に守ることができるって、すごいね。これ、いろんな機械学習の応用に役立ちそうじゃない？



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, cs.IT, math.IT, **投稿日時:** 2024-11-21 18:56

- - -

### [Towards Adaptive Asynchronous Federated Learning for Human Activity Recognition](http://arxiv.org/abs/2411.14070)

**ヒューマンアクティビティ認識のための適応的非同期連合学習に向けて**

Rastko Gajanin, Anastasiya Danilenka, Andrea Morichetta, Stefan Nastic

- IoTシナリオでは、異種デバイスからデータを収集し連合学習で学習することが重要
- ヒューマンアクティビティ認識での非IIDなデータへの連合学習移行を具体的に解決
- データ拡張や最適化手法、バッチサイズ選択などがモデル性能に与える影響を評価
- Flowerフレームワークの非同期連合学習を可能にするオープンソース拡張を提供

IoTでいろんなデバイスからのデータを使って、人の動きとかが分かるって、未来感たっぷりだね！非同期での連合学習の拡張も公開しているから、これからいろんな応用が期待できそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-11-21 12:32

- - -

### [REFOL: Resource-Efficient Federated Online Learning for Traffic Flow Forecasting](http://arxiv.org/abs/2411.14046)

**REFOL：交通流予測のための資源効率の良い連合オンライン学習**

Qingxiang Liu, Sheng Sun, Yuxuan Liang, Xiaolong Xu, Min Liu, Muhammad Bilal, Yuwei Wang, Xujing Li, Yu Zheng

- FL手法は中央集中的手法の生データ漏洩を避けるために提案されている
- オフライン学習は概念ドリフトに弱く、オンライン学習がTFFに適している
- REFOLは通信と計算負担を軽減しつつ予測性能を保証する手法を提案
- 実験結果により、REFOLは予測向上と資源の節約の面で優れていることを示す

REFOLってすごく興味深い！今までの問題点を解決しつつ資源も節約、実現できたら交通流予測がもっと進化しそう。また、連合学習の進化が今後ますます期待できるね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-21 11:50

- - -

### [Generative Intervention Models for Causal Perturbation Modeling](http://arxiv.org/abs/2411.14003)

**因果的撹乱モデリングのための生成介入モデル**

Nora Schneider, Lars Lorch, Niki Kilbertus, Bernhard Schölkopf, Andreas Krause

- 因果モデルを用いて撹乱効果の予測問題に取り組む
- 薬物の特性はわかるが、細胞への因果効果は不明
- 提案するGIMは撹乱特徴を因果モデルの介入分布にマッピング
- 合成データとscRNA-seqで有望な分布外予測を実現

因果モデルを使って未知の撹乱を予測できるってすごく興味深い！医薬品の開発とかに役立ちそうでワクワクするね。科学と統計の新たなアプローチで潜在的な発見がありそうだから、今後もっと広がりそうな分野かも。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-11-21 10:37

- - -

### [FedRAV: Hierarchically Federated Region-Learning for Traffic Object Classification of Autonomous Vehicles](http://arxiv.org/abs/2411.13979)

**FedRAV: 自動運転車の交通物体分類のための階層的連合地域学習**

Yijun Zhai, Pengzhan Zhou, Yuepeng He, Fang Qu, Zhida Qin, Xianlong Jiao, Guiyan Liu, Songtao Guo

- 自動運転車のデータを保護しつつ活用するため、連合学習を提案
- 非独立同分布（Non-IID）データへの対応が必要であり、性能向上が課題
- FedRAVは地域ごとに車両をサブ領域に分割し、個別および地域モデルを最適化
- 実験で既存の連合学習アルゴリズムを上回り、精度を3.69%以上向上

自動運転車に連合学習を使うのってすごく新しい感じで、未来だよね！FedRAVが他よりも精度いいって聞いて、どんな仕組みかもっと知りたくなっちゃった。楽しそうだから、友達と一緒に居眠り運転をなくす方法を考えてみるのもいいかも！

**Comment:** 8 pages, 4 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.AI, **投稿日時:** 2024-11-21 09:45

- - -

### [Split Federated Learning Over Heterogeneous Edge Devices: Algorithm and Optimization](http://arxiv.org/abs/2411.13907)

**異種エッジデバイスにおけるスプリット連合学習：アルゴリズムと最適化**

Yunrui Sun, Gang Hu, Yinglei Teng, Dunbo Cai

- スプリット学習は、生データを共有せずにリソース制約のあるデバイスでモデルを訓練できる。
- 現行のスプリット学習アルゴリズムは、異種環境で訓練効率が悪く、特に遅延が問題。
- 提案するHSFLフレームワークは、異なるカット層でクライアント側モデルを並列に訓練可能。
- HSFLは、収束率とモデル精度で他のフレームワークを上回り、最適化アルゴリズムで遅延を削減。

新しいフレームワークで、どれだけ効率よく訓練できるか気になる！最適化アルゴリズムが他より優れてるってことは、スムーズに進むってことだよね。エッジデバイスの性能が不揃いなのが、逆に面白いチャレンジになりそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-21 07:46

- - -

### [Towards Full Delegation: Designing Ideal Agentic Behaviors for Travel Planning](http://arxiv.org/abs/2411.13904)

**完全な委任に向けて: 旅行計画における理想的なエージェント行動の設計**

Song Jiang, Da JU, Andrew Cohen, Sasha Mitts, Aaron Foss, Justine T Kao, Xian Li, Yuandong Tian

- ルーチンの意思決定をエージェントに委任し、人々の個別ニーズに適応する能力が求められる。
- エージェント行動の評価は成果だけでなく、手続きも重視する必要がある。
- 提案されたAPECエージェント憲法には、正確性、積極性、効率性、信頼性の基準が含まれる。
- 合成データを用いてAPEC-Travelを構築し、ベースラインを平均20.7%上回る性能を実現。

旅行計画をエージェントにお任せできるって、未来が一歩近づいた感じだね！自分好みに最適化してくれるなんて夢みたい。でもエージェントと旅行の会話がどこまで面白くなるか、今から楽しみだよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-11-21 07:30

- - -

### [Robust Detection of Watermarks for Large Language Models Under Human Edits](http://arxiv.org/abs/2411.13868)

**大規模言語モデルの水印を人間の編集下で頑強に検出する手法**

Xiang Li, Feng Ruan, Huiyuan Wang, Qi Long, Weijie J. Su

- 大規模言語モデルの生成テキストは、水印で人間の生成テキストと区別できる。
- 人間の編集が水印信号を希薄化し、従来の手法の検出性能を低下させる。
- Tr-GoFテストを提案、編集の程度を知らずに水印を適応的に検出可能。
- Tr-GoFは競争力があり、合成データとLLLaMAモデルとの比較で優れた性能を示す。

水印検出の新手法が編集されたテキストでもしっかり働くなんて面白そう！人間が手を加えた部分を考慮して、どんな場面でも応用できそうね。バランスのとれた技術だから、色んな分野で活躍するかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CL, math.ST, stat.ME, stat.ML, stat.TH, **投稿日時:** 2024-11-21 06:06

- - -

### [Asynchronous Federated Learning Using Outdated Local Updates Over TDMA Channel](http://arxiv.org/abs/2411.13861)

**非同期連合学習：TDMAチャネルを用いた古いローカル更新を用いて**

Jaeyoung Song, Jun-Pyo Hong

- TDMAベースのネットワークでは、伝統的な同期型連合学習に対し遅延が生じることがある
- 提案する非同期FLでは、デバイスを複数のTDMAグループに分けて時間効率を向上
- 古いローカル更新がグローバルモデルの更新を妨げるが収束可能であることを示した
- 意図的な遅延により収束を加速し、ローカル更新の古さを低減する戦略を提案

TDMAを使っても非同期で工夫することで効率が良くなるって、めちゃ面白いね！デバイスがたくさんになっちゃうと同期が難しいから、こういう工夫はこれからますます大事になりそうだよね。わくわくする未来だなあ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-11-21 05:42

- - -

### [Dealing with Synthetic Data Contamination in Online Continual Learning](http://arxiv.org/abs/2411.13852)

**オンライン継続学習における合成データ汚染への対処法**

Maorong Wang, Nicolas Michel, Jiafeng Mao, Toshihiko Yamasaki

- 画像生成技術の進展で、リアルな合成画像が大量にインターネットに流通
- 合成データが研究やディープラーニングのデータ収集に悪影響を及ぼす可能性
- 合成画像混入データセット使用で、学習モデル性能が低下することを実験で確認
- ESRM法を提案し、合成画像での性能低下を緩和することを実証

AIが生成する画像が、人間の収集したデータを汚染する時代だね。でも、解決策があるから安心！特にESRMで問題を和らげられるなんて、未来の学習モデルも安心して使えそうな気がするよ。新しい方法がどんどん出てきて、どんな変化が起きるのか楽しみだな。

**Comment:** Accepted to NeurIPS'24

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-11-21 05:24

- - -

### [Adaptable Embeddings Network (AEN)](http://arxiv.org/abs/2411.13786)

**適応型埋め込みネットワーク (AEN)**

Stan Loosmore, Alexander Titus

- 言語モデルはテキスト分類に多用されているが、計算コストが高い
- AENはカーネル密度推定を用いた新たな二重エンコーダー構造を提案
- 再学習不要で分類基準の適応が可能で、非自己回帰型である
- 合成データの実験で、AENはより大きな自己回帰モデルと同等か、それ以上の結果を示す

AENって、すごく使いやすそうで注目の技術だね！特にエッジコンピューティングとか、リアルタイムなシステムで活躍しそう！私も試してみたくなっちゃった♪

**Comment:** 20 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-21 02:15

- - -

### [-Privacy for Text and the Curse of Dimensionality](http://arxiv.org/abs/2411.13784)

**$d_X$プライバシーと次元の呪いについての考察**

Hassan Jameel Asghar, Robin Carpentier, Benjamin Zi Hao Zhao, Dali Kaafar

- $d_X$-プライバシーは、差分プライバシーを緩和した手法であるが、多次元ラプラス機構を使う
- ラプラス機構を言葉単位で用いると、元の単語かまったく異なる単語が出力され、意味の類似する単語は少ない
- この現象は、単語埋め込みモデルにおける近傍単語との距離が並び順内で大差ないことと関連している
- 提案された後処理ステップにより、この問題を解消することが可能である

この研究、ちょっと面白そうだよね！高次元空間のせいでプライバシー保護しにくいっていう課題を解決する提案が、お洒落な感じ✨次元の呪いも上手く乗り越えて、もっと良いプライバシー技術になるといいな！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-11-21 01:59

- - -

### [Preserving Expert-Level Privacy in Offline Reinforcement Learning](http://arxiv.org/abs/2411.13598)

**オフライン強化学習における専門家レベルのプライバシー保護**

Navodita Sharma, Vishnu Vinod, Abhradeep Thakurta, Alekh Agarwal, Borja Balle, Christoph Dann, Aravindan Raghuveer

- オフライン強化学習は、履歴データから最適なポリシーを学習するが、専門家の選択がプライバシーに敏感
- 医療や広告、パーソナライズされた情報検索では専門家の選択が機微なデータとされる
- 専門家のプライバシーを証明可能に保護するため、合意ベースの差分プライバシー手法を新たに開発
- 大規模連続状態空間を持つ環境で提案手法を検討し、従来のベースラインを超える成果を実証

プライバシーを守りつつ、しっかりとした成果を出せる方法を研究していてすごい！特に医療とか他の分野にも適用できる点は今後にも期待が膨らむねー。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-11-18 21:26

- - -

### [Deep learning waterways for rural infrastructure development](http://arxiv.org/abs/2411.13590)

**地方インフラ開発のためのディープラーニングによる水路検出**

Matthew Pierson, Zia Mehrabi

- 地球上の多くの水路が未だにマッピングされておらず、特に低中所得国に多い。
- 高解像度衛星画像と標高モデルを基に、水路を学習するモデルWaterNetを構築。
- アフリカでの新環境に展開し、従来マッピングされていなかった水路構造を示す。
- 新たに生成された水路マップは、コミュニティニーズをOpen Street Mapなどよりも高精度に把握。

新しい技術で今まで見えなかったものが見えるようになるなんてワクワクするね！特に地方の橋建設に役立てられると、教育や医療アクセスが良くなって地域の未来も明るそう！

**Comment:** 18 pages, 6 figures

**トピック:** [TEE](tee), **カテゴリ:** cs.CV, cs.AI, cs.LG, 68, D.0, **投稿日時:** 2024-11-18 05:36
