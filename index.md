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

更新: 2025-01-13T04:23:21.396095

- - -

### [Explainable Federated Bayesian Causal Inference and Its Application in Advanced Manufacturing](http://arxiv.org/abs/2501.06077)

**説明可能な連合ベイジアン因果推論とその高度製造における応用**

Xiaofeng Xiao, Khawlah Alharbi, Pengyu Zhang, Hantang Qin, Xubo Yue

- 因果推論はxAIシステムで注目されているが、製造システムでの応用はまだ十分でない。
- 提案する連合ベイジアン学習フレームワークxFBCIは製造システムでの因果関係探求を目的とする。
- xFBCIはローカルのプライベートデータにアクセスせず、傾向スコアを推定し治療効果を見積もる。
- 実際のEHD印刷データを用いた実験で、既存手法よりも優れた性能を示した。

因果関係を解明するための新しい手法って、すごく革新的に感じるよね。製造業でも人工知能がもっと活用されていく未来が楽しみだな！

**Comment:** 26 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.AP, **投稿日時:** 2025-01-10 16:14

- - -

### [Encoded Spatial Attribute in Multi-Tier Federated Learning](http://arxiv.org/abs/2501.05934)

**多層連合学習における空間属性のエンコード**

Asfia Kawnine, Francis Palma, Seyed Alireza Rahimi Azghadi, Hung Cao

- 地理空間データの集約モデルを多層連合学習で評価するアプローチを提案
- クライアント層で空間情報をエンコードすることで、ターゲット結果の予測精度を向上
- 75.62%と89.52%の精度を達成し、異なる空間データ粒度を予測する複数のモデルを取得
- リアルタイムアプリケーションでの重要性とさらなる予測精度向上の必要性を強調

空間データの粒度をエンコードするなんて、なんだか未来的でわくわくする！今後の応用が楽しみだね！

**Comment:** IEEE ICCE 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2025-01-10 12:56

- - -

### [Collaborative Content Moderation in the Fediverse](http://arxiv.org/abs/2501.05871)

**フェディバースにおける協調的コンテンツモデレーション**

Haris Bin Zia, Aravindh Raman, Ignacio Castro, Gareth Tyson

- フェディバースは急速に人気になり、コンテンツモデレーションが課題として浮上している
- 中央集権的なプラットフォームとは異なり、フェディバースはラベル付きデータセットとインフラが不十分
- 本研究は連合学習に基づく協調的なコンテンツモデレーションシステム「FedMod」を設計・評価
- FedModは3つのタスクで堅牢な性能を示し、平均マクロF1スコア0.58〜0.73を達成

フェディバースって、あの分散型のSNSだよね。難しい課題も多いけど、連合学習でうまくやっちゃうなんてすごい！未来のSNSがワクワクしちゃうね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.SI, cs.LG, cs.NI, **投稿日時:** 2025-01-10 11:12

- - -

### [STHFL: Spatio-Temporal Heterogeneous Federated Learning](http://arxiv.org/abs/2501.05775)

**STHFL: 時空間異質性連合学習**

Shunxin Guo, Hongsong Wang, Shuxia Lin, Xu Yang, Xin Geng

- 異なるデータ分布による時空間異質性を考慮し、連合学習での課題に対応する新設定を提案
- 新たなGLDPフレームワークは、動的適応を可能にする個別のレイヤーを含む
- 長い尾を持つデータ分布のクラスに対し、プライバシーを漏らさずに補完的知識を提供
- 各クライアントの過去タスクの知識を活用し、学習時の忘却現象を解決

新しい学習方法って本当にすごいね！プライバシーを守りながら、前の知識を忘れないで次のステップに進めるって最高じゃん！じわじわ変化に対応できるのって未来的でワクワクするね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2025-01-10 08:15

- - -

### [Enabling Scalable Oversight via Self-Evolving Critic](http://arxiv.org/abs/2501.05727)

**自己進化型評価者による拡張可能な監視の実現**

Zhengyang Tang, Ziniu Li, Zhenyang Xiao, Tian Ding, Ruoyu Sun, Benyou Wang, Dayiheng Liu, Fei Huang, Tianyu Liu, Bowen Yu, Junyang Lin

- 大規模言語モデルは人間評価が難しいタスクで、効果的なフィードバックが課題である
- SCRITは人間や他のモデルに頼らず自己進化できる批評フレームワークを提案する
- 合成データを活用し、自己批評と自己評価メカニズムで品質を保証する
- 実装モデルで批評能力が10.3%向上し、データやモデルサイズに比例して性能が向上する

この論文のアプローチ、まるでAIが自分自身を鍛えて強くなる感じね！自己進化って、究極のAIの夢みたいでワクワクする！モデルがどんどん成長していく未来が楽しみだなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2025-01-10 05:51

- - -

### [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](http://arxiv.org/abs/2501.05707)

**マルチエージェント微調整: 多様な推論チェーンによる自己改善**

Vighnesh Subramaniam, Yilun Du, Joshua B. Tenenbaum, Antonio Torralba, Shuang Li, Igor Mordatch

- 大規模言語モデルの性能は優れているが、基盤となるトレーニングデータに限界がある。
- 合成データによる自己改善は限界が訪れることがある。
- マルチエージェント社会における微調整が、多様化を通じて自己改善を促進する。
- 提案手法は、多様な推論タスクを通じてその有効性を示している。

マルチエージェントなアプローチでモデルが賢くなるなんて、ちょっとRPGみたいでワクワクするね！いっぱいのエージェントが協力して進化していく姿が、これからどんな成果を生むのか楽しみだなぁ。

**Comment:** 22 pages, 13 figures, 7 tables; Project page at   https://llm-multiagent-ft.github.io/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2025-01-10 04:35

- - -

### [Cascaded Self-Evaluation Augmented Training for Efficient Multimodal Large Language Models](http://arxiv.org/abs/2501.05662)

**効率的なマルチモーダル大規模言語モデルのためのカスケード自己評価強化トレーニング**

Zheqi Lv, Wenkai Wang, Jiawei Wang, Shengyu Zhang, Fei Wu

- 連鎖的な思考推論と自己評価で効率的な大規模言語モデルの性能は向上
- 制約あるパラメータが自己評価を難しくしている課題を解決するためSEATを提案
- SEATを改良し長いプロンプトを分割するCas-SEATを導入してリソース削減を達成
- 実験によりMathVistaなどで19.68%の性能向上を記録し、後続研究のリソースを提供

なんか、長い説明がスッキリ短くしてもちゃんとした結果を出すなんて使えそうじゃない？コスト削減で学習をアップグレードできるのはポイント高いよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2025-01-10 02:28

- - -

### [Constrained Over-the-Air Model Updating for Wireless Online Federated Learning with Delayed Information](http://arxiv.org/abs/2501.05637)

**遅延情報を考慮したワイヤレスオンラインフェデレーテッドラーニングにおける制約付きOTAモデル更新**

Juncheng Wang, Yituo Liu, Ben Liang, Min Dong

- ワイヤレスネットワーク上でオンラインなフェデレーテッドラーニングを研究
- 遅延した情報と時間変動する電力制約下でモデル更新手法COMUDOを提案
- COMUDOは動的後悔、静的後悔、制約違反の境界を提供
- シミュレーションでCOMUDOが低電力領域で高精度を達成

この研究って、電力が限られてる時でも高精度な学習ができるのがポイントだよね！遅延があってもこれだけ精度をあげられる技術があるなら、未来の通信にも色々活用できそうってワクワクしちゃう！

**Comment:** To appear in INFOCOM 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2025-01-10 00:50

- - -

### [Kite: How to Delegate Voting Power Privately](http://arxiv.org/abs/2501.05626)

**Kite: 投票権をプライベートに委任する方法**

Kamilla Nazirkhanova, Vrushank Gunjur, X. Pilli Cruz-De Jesus, Dan Boneh

- 選挙の投票プライバシーは民主主義のプロセスにおいて重要だが、従来は公開の委任しか対応していない
- KiteはDAOにおける投票権のプライベートな委任を可能にする新しいプロトコルを提案
- プロトコルはUniversal Composabilityフレームワークで設計・検証され、Ethereum上の拡張として実装
- 委任にはゼロ知識証明が必要で、消費者向けラップトップで7から167秒かかる

投票をもっとプライベートにできるってすごい！DAOでも使えるようにして、これからの民主主義が安全に進むといいなって思ったよ。自分の投票行動がバレず、しかもお手軽に運用できる未来が楽しみ！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2025-01-09 23:49

- - -

### [On Fair Ordering and Differential Privacy](http://arxiv.org/abs/2501.05535)

**公正な取引順序と差分プライバシーについて**

Shir Cohen, Neel Basu, Soumya Basu, Lorenzo Alvisi

- ブロックチェーンでは公正な取引順序が信頼性と規制準拠に重要である
- 関連機能だけで取引の順序を決定し、平等な順番を保証する枠組を提案
- State Machine Replicationと差分プライバシーの意外な関連性を発見
- 差分プライバシー技術を使った新しい公正な分散プロトコル設計の可能性を示唆

ブロックチェーンの取引順序にまで差分プライバシーが応用できるなんてすごいね！新しい公正なプロトコル設計の未来が楽しみだなー。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2025-01-09 19:17

- - -

### [A Survey of Interactive Verifiable Computing: Utilizing Low-degree Polynomials](http://arxiv.org/abs/2501.05500)

**インタラクティブな検証可能計算の調査：低次多項式の利用**

Angold Wang

- 検証可能計算の進化を基礎理論からZK-SNARKsまで追跡
- 低次多項式を用いて誤り検出と検証効率を強化するプロトコルを探究
- 伝統的なNPベースの証明システムの限界を克服する新たな手法を提示
- GKRプロトコルを中心に現代の検証可能計算モデルの基礎を解説

この論文では、計算の検証を効率的かつ安全に行うための最先端技術が詳しく解説されていて、これからのコンピュータサイエンスの理解に役立ちそう！特に低次多項式を使ったアプローチが気になるなぁ。検証のスピードアップにつながる技術、ますます研究が進むといいね！

**Comment:** 29 pages

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.LO, cs.CR, **投稿日時:** 2025-01-09 18:42

- - -

### [FedSA: A Unified Representation Learning via Semantic Anchors for Prototype-based Federated Learning](http://arxiv.org/abs/2501.05496)

**FedSA: プロトタイプベースの連合学習のためのセマンティックアンカーによる統一表現学習**

Yanbing Zhou, Xiangmou Qu, Chenlong You, Jiyang Zhou, Jingyue Tang, Xin Zheng, Chunmao Cai, Yingbo Wu

- プロトタイプベースの連合学習は、軽量なプロトタイプを用いて異種データを持つクライアント間で知識を共有する。
- 従来の手法ではローカルモデルから直接プロトタイプを集めるため、表現学習に不整合が生じやすい。
- FedSAは、セマンティックアンカーを使ってプロトタイプ生成とローカル表現学習を分離し一貫した表現を学習させる。
- 同手法により、クライアント間でのプロトタイプの一貫性と判別力を高めることで、表現学習の一般化を向上させる。

「セマンティックアンカー」って新鮮な響き！これでデータの違いも気にせずに連合学習できるなんて、未来の協力体制がどんどん進化していくね。ワクワクする！

**Comment:** Accepted by AAAI2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-09 16:10
