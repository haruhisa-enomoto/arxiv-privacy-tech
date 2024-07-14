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

更新: 2024-07-14T04:21:15.243913

- - -

### [DART: A Solution for Decentralized Federated Learning Model Robustness Analysis](http://arxiv.org/abs/2407.08652)

**DART: 分散型連合学習モデルの堅牢性分析のためのソリューション**

Chao Feng, Alberto Huertas Celdrán, Jan von der Assen, Enrique Tomás Martínez Beltrán, Gérôme Bovet, Burkhard Stiller

- 中央サーバーを用いる連合学習はボトルネックや単一障害点があるため分散型連合学習が提案
- 分散型連合学習でも敵対的攻撃、特に毒入れ攻撃に脆弱である点は中央型と同様
- DARTというソリューションを提案し、毒入れ攻撃に対する分散型連合学習の堅牢性を評価
- 中央型と分散型の連合学習の挙動を比較、攻撃の広がりと効果に影響する要因を特定

分散型連合学習がどれだけ堅牢かを検証するDARTってすごく面白そう！未来の研究を左右する大きな影響がありそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-11 16:32

- - -

### [CAR-MFL: Cross-Modal Augmentation by Retrieval for Multimodal Federated Learning with Missing Modalities](http://arxiv.org/abs/2407.08648)

**CAR-MFL: 欠損モダリティを含む多モーダル連合学習のための検索によるクロスモーダル拡張**

Pranav Poudel, Prashant Shrestha, Sanskar Amgain, Yash Raj Shrestha, Prashnna Gyawali, Binod Bhattarai

- 多モーダルAIは一つのモーダルに比べ、より包括的な分析が可能
- しかし、医療データセットの限定的な公開により適用が困難
- 提案された方法は欠損モダリティを補完するための検索によるクロスモーダルデータ拡張
- この方法は医療分野のベンチマークで性能を向上させ、複数の競合ベースラインを凌駕

多モーダル連合学習って面白そう！医療データを使ってプライバシーも保護するなんて未来的だね。早く導入されるといいな。

**Comment:** Accepted at MICCAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-11 16:26

- - -

### [Distributed Edge Analytics in Edge-Fog-Cloud Continuum](http://arxiv.org/abs/2407.08543)

**エッジ-フォグ-クラウド連続体における分散エッジ分析**

Satish Narayana Srirama

- クラウド中心のIoTアプリでの遅延やネットワーク負荷、プライバシー問題を軽減するためにフォグコンピューティングが利用される
- エッジ分析タスクは単一ノードで行われるが、分散エッジ分析は連続体の複数ノードを同時に使用する
- 論文はサーバーレスデータパイプライン、分散コンピューティングとエッジ分析、連合学習の3視点から分散エッジ分析を論じる
- MQTTベースのSDP、CANTO、FIDELを使用し、異なるケーススタディを通じて分散エッジ分析の実現可能性を示す

データの処理をエッジに分散するなんて、すごい考えだよね！プライバシーも守れるし、これからのIoTの未来が楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-11 14:29

- - -

### [Enhancing Privacy of Spatiotemporal Federated Learning against Gradient Inversion Attacks](http://arxiv.org/abs/2407.08529)

**勾配逆転攻撃に対する時空間連合学習のプライバシー強化**

Lele Zheng, Yang Cao, Renhe Jiang, Kenjiro Taura, Yulong Shen, Sheng Li, Masatoshi Yoshikawa

- 時空間連合学習が勾配のみを共有して価値あるモデルを訓練可能
- 勾配逆転攻撃（GIA）が画像やテキストに対して有効が示された
- 提案する時空間勾配逆転攻撃（ST-GIA）は勾配から元の位置を再構築
- 適応型防御戦略で勾配の摂動レベルを動的調整、プライバシーと実用性のトレードオフを改善

攻撃と防御の両面から考えたこの研究、めっちゃ未来感あるよね！実データでの有効性も立証されてるから、実用化が楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-11 14:17

- - -

### [Distributed Deep Reinforcement Learning Based Gradient Quantization for Federated Learning Enabled Vehicle Edge Computing](http://arxiv.org/abs/2407.08462)

**連合学習を活用した車両エッジコンピューティングのための分散ディープ強化学習ベースの勾配量子化**

Cui Zhang, Wenjun Zhang, Qiong Wu, Pingyi Fan, Qiang Fan, Jiangzhou Wang, Khaled B. Letaief

- 連合学習が車両データのプライバシー保護に寄与し、勾配の共有でデータを保護
- 勾配量子化が通信遅延を減少させ、適切な量子化レベルが精度と訓練時間に影響
- 時変チャネル条件が最適化を難しくし、DRLベースの量子化レベル割り当てを提案
- シミュレーションで訓練時間と量子化誤差の最適な重み係数を特定し効果を実証

車両エッジコンピューティングに連合学習を使ってるのがすごく新しい感じがするよね！時変チャンネルの問題をどうやって克服するのかも気になるポイント！

**Comment:** This paper has been submitted to IEEE Journal. The source code has   been released at:   https://github.com/qiongwu86/Distributed-Deep-Reinforcement-Learning-Based-Gradient   Quantization-for-Federated-Learning-Enabled-Vehicle-Edge-Computing

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.NI, **投稿日時:** 2024-07-11 12:58

- - -

### [Digital twins to alleviate the need for real field data in vision-based vehicle speed detection systems](http://arxiv.org/abs/2407.08380)

**視覚ベースの車両速度検出システムにおける実フィールドデータの必要性を軽減するデジタルツイン**

Antonio Hernández Martínez, Iván García Daza, Carlos Fernández López, David Fernández Llorca

- 視覚ベースの速度推定はレーダーやLiDARに比べて費用対効果が高い
- 現実の道路交通ビデオデータ取得は複雑かつ高コストで、データセットも少ない
- CARLAシミュレータを使って特定の実カメラを表す大規模な合成データセットを生成する方法を提案
- 合成データでの訓練により平均絶対誤差が3km/h以下となる

デジタルツインを使うなんて、すごく最新のテクノロジーだよね。実世界の複雑さもシミュレーションでカバーできるなんて、これから色々と応用できそう！

**Comment:** Paper accepted at the 27th IEEE International Conference on   Intelligent Transportation Systems (ITSC 2024)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-07-11 10:41

- - -

### [Skywork-Math: Data Scaling Laws for Mathematical Reasoning in Large Language Models -- The Story Goes On](http://arxiv.org/abs/2407.08348)

**Skywork-Math: 大規模言語モデルにおける数学的推論のデータスケーリング法則 - 物語は続く**

Liang Zeng, Liangjun Zhong, Liang Zhao, Tianwen Wei, Liu Yang, Jujie He, Cheng Cheng, Rui Hu, Yang Liu, Shuicheng Yan, Han Fang, Yahui Zhou

- 大規模言語モデルの数学的推論能力はデータ量の増加で向上することを示した
- Skywork-Mathモデルシリーズを提案し、Skywork-MathQAデータセットでのSFTを実施
- Skywork-Math 7BはMATHベンチマークで51.2%、GSM8Kベンチマークで83.9%の精度を達成
- 新たなデータ合成とモデルのSFTパイプラインが高性能を支えている

これってめっちゃ面白そう！数学の推論力がデータと技術でどこまで伸びるのか、もっと知りたくなるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, cs.LG, **投稿日時:** 2024-07-11 09:56

- - -

### [FedLog: Personalized Federated Classification with Less Communication and More Flexibility](http://arxiv.org/abs/2407.08337)

**FedLog: より少ない通信と柔軟性を持つ個別化された連合分類**

Haolin Yu, Guojun Zhang, Pascal Poupart

- 連合学習では、クライアントがプライベートデータでローカルモデルを訓練し、モデルパラメータを共有するが通信コストが高い
- FedLogは、モデルパラメータではなくローカルデータの要約を共有することで通信コストを削減
- Bayesian推論を用いて、FedLogは元のモデルの最終層と同じくらい小さなメッセージを伝送
- 差分プライバシーを導入し、プライバシーバジェットと精度のトレードオフを示す実験を実施

通信コストをこんな風に減らす工夫があるんだね。連合学習の柔軟性がもっと広がりそう！プライバシーも大事だし、そのバランスを見るのも楽しみ！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.DC, stat.ML, **投稿日時:** 2024-07-11 09:40

- - -

### [Leveraging GPT for the Generation of Multi-Platform Social Media Datasets for Research](http://arxiv.org/abs/2407.08323)

**研究のためのマルチプラットフォームソーシャルメディアデータセットの生成にGPTを活用する**

Henry Tari, Danial Khan, Justus Rutten, Darian Othman, Rishabh Kaushal, Thales Bertaglia, Adriana Iamnitchi

- ソーシャルメディアデータセットは虚偽情報、影響操作、ヘイトスピーチ検出など多くの研究に必要
- コストやプラットフォーム規制により、これらのデータセットへのアクセスは制限されることが多い
- 大規模言語モデルを用いてマルチプラットフォームのソーシャルメディアデータセットを生成し、実データの品質を目指すことを試みる
- 実データと合成データを比較し、レキシカルおよびセマンティックな性質を評価、合成データの品質向上が必要とされる

この研究すごく面白そう！合成データでどこまで実データに近づけるのか、未来の研究が楽しみだね。データ収集の壁が低くなるのも魅力的！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CY, **投稿日時:** 2024-07-11 09:12

- - -

### [Feature Diversification and Adaptation for Federated Domain Generalization](http://arxiv.org/abs/2407.08245)

**連合領域一般化における特徴の多様化と適応**

Seunghan Yang, Seokeon Choi, Hyunsin Park, Sungha Choi, Simyung Chang, Sungrack Yun

- 連合学習ではクライアントのデータドメインが異なるため、ドメインシフトが発生しうる
- プライバシーの問題から各クライアントは限られたドメインデータでしか学習できない
- グローバル特徴統計量を活用してデータ多様化を行い、クライアント非依存な表現を学習
- インスタンスアダプティブ推論で特徴統計量を動的に調整し、ドメインギャップを縮小

クライアントごとのデータ多様化の概念とか、面白そう！本当にそのアプローチでドメインのギャップが埋まるのか、ちょっと気になるなあ。

**Comment:** Accepted to ECCV 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-07-11 07:45

- - -

### [Differentially Private Neural Network Training under Hidden State Assumption](http://arxiv.org/abs/2407.08233)

**隠れ状態仮定下での差分プライバシーを用いたニューラルネットワーク訓練**

Ding Chen, Chen Liu

- DP-SBCDという新しい手法を提案し、差分プライバシーの保証を持つニューラルネットワークを訓練
- 訓練過程を分解し各レイヤーごとに行うことで、非凸問題や近接勾配降下法にも対応
- 適応分布からサンプルされたキャリブレーションされたノイズを用いる新たな手法を採用
- ユーティリティとプライバシーの間のトレードオフが改善される実証的な結果を示す

プライバシー技術と機械学習の融合ってすごく面白そう！特に適応分布からノイズを取るところがすごくユニークだよね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-11 07:14

- - -

### [DALL-M: Context-Aware Clinical Data Augmentation with LLMs](http://arxiv.org/abs/2407.08227)

**DALL-M：LLMを用いたコンテキスト認識型臨床データ増強**

Chihcheng Hsieh, Catarina Moreira, Isabel Blanco Nobre, Sandra Costa Sousa, Chun Ouyang, Margot Brereton, Joaquim Jorge, Jacinto C. Nascimento

- X線画像は診断に重要だが、臨床コンテキストがないと効果が限定的 
- 大規模言語モデル（LLM）を使用し、患者のコンテキスト合成データを生成する新技術を提案 
- この手法により、実データの整合性を保ちながらコンテキスト豊富な合成特徴を追加し、モデル性能を向上 
- 実験でF1スコアが16.5%、PrecisionとRecallが約25%向上するなど、機械学習モデルの性能を大幅に改善

臨床データの増強がどんだけ効果的にできるか楽しみ！これって、医療AI診断がもっと復元力が高くなることに期待できるよね。

**Comment:** we introduce a pioneering approach to clinical data augmentation that   employs large language models (LLMs) to generate patient contextual synthetic   data. It preserves the integrity of real patient data while enriching the   dataset with contextually relevant synthetic features, significantly   enhancing model performance

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.IR, cs.LG, I.5.1; J.3; H.3.3; I.2.7, **投稿日時:** 2024-07-11 07:01

- - -

### [Enriching Information and Preserving Semantic Consistency in Expanding Curvilinear Object Segmentation Datasets](http://arxiv.org/abs/2407.08209)

**情報の充実と意味の一貫性を保つカーヴィリニアオブジェクトセグメンテーションデータセットの拡充**

Qin Lei, Jiang Zhong, Qizhu Dai

- カーヴィリニアオブジェクトのセグメンテーションには多くの応用があるが、データ収集と注釈のコストが高いためデータセットが小規模である
- 複数のテキスト特徴を用いて合成データの情報量を増強し、元データセットを超える分布の合成画像を得る手法を紹介
- 新しいデータセット「COSTG」を作成し、標準的な意味マップに加えてテキスト記述を含むことで従来のデータセットの制限を超える
- SCP ControlNetを導入して合成意味マップと画像の一貫性を保ち、実験結果で性能向上を確認

カーヴィリニアオブジェクトのセグメンテーションにおいて、データの収集の手間が削減できるのはすごく助かる！みんなの研究やプロジェクトに与える影響も大きそうだね。

**Comment:** ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-11 06:25

- - -

### [Privacy-Preserving Data Deduplication for Enhancing Federated Learning of Language Models](http://arxiv.org/abs/2407.08152)

**連合学習を強化するためのプライバシー保護型データ重複除去**

Aydin Abadi, Vishnu Asutosh Dasu, Sumanta Sarkar

- 連合学習の重複除去はスケーラビリティやプライバシー侵害の課題がある
- モジュラー構造のEP-MPDプロトコルを提案、データプライバシーを損なわずに重複を除去
- 新しいプライベートセットインターセクションの2つの変種を使用している
- 大規模言語モデルで最大19.61%のパープレキシティ改善と最大27.95%の実行時間短縮を実現

新しいプロトコルが、データの重複を取り除きつつプライバシーも守るってすごいね！連合学習の性能がめっちゃ良くなる予感がするよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.CL, cs.LG, **投稿日時:** 2024-07-11 03:10

- - -

### [Federated Learning and AI Regulation in the European Union: Who is liable? An Interdisciplinary Analysis](http://arxiv.org/abs/2407.08105)

**連合学習と欧州連合におけるAI規制: 誰が責任を負うのか? 学際的解析**

Herbert Woisetschläger, Simon Mertel, Christoph Krönke, Ruben Mayer, Hans-Arno Jacobsen

- 欧州連合のAI法は、機械学習アプリケーションの開発と展開における明確な責任を求めている
- 連合学習（FL）は、データセキュリティを向上させながら、モデルパラメータのみを共有してAIモデルの訓練を可能にする
- FLは協調的な学習パラダイムであり、クライアントとサーバーが法的責任を共有することが自然である
- 各主体の役割を明確にし、サーバーオペレーターへの責任転嫁の戦略とFLの実用性を向上させるための技術的課題を指摘している

欧州のAI規制と連合学習の関係が面白いね！実際の運用に向けてどんな課題を解決するのか、続きが気になるな～。

**Comment:** Accepted at the GenLaw'24 workshop in conjunction with ICML'24

**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, K.5; I.2.11; C.2.4; D.2.1, **投稿日時:** 2024-07-11 00:41

- - -

### [RoCap: A Robotic Data Collection Pipeline for the Pose Estimation of Appearance-Changing Objects](http://arxiv.org/abs/2407.08081)

**RoCap: 外観が変化する物体のポーズ推定のためのロボットデータ収集パイプライン**

Jiahao Nick Li, Toby Chong, Zhongyi Zhou, Hironori Yoshida, Koji Yatani, Xiang 'Anthony' Chen, Takeo Igarashi

- 外観が変化する物体のポーズ推定は、通常の視覚ベースの方法では困難
- RoCapはロボットアームを使用して、人間の操作を模倣しながらデータ収集
- 収集した画像とロボットアームの関節角度から自動的にラベル付きデータ生成
- 深層学習モデルを使ったポーズ推定で、従来の合成データモデルよりも優れた結果

動いて変わる物体のポーズ推定っておもしろそうだね。これ、もっといろんな物にも適用できるようになったらすごい未来が来るかもね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.HC, **投稿日時:** 2024-07-10 22:52

- - -

### [Fine-Tuning Large Language Models with User-Level Differential Privacy](http://arxiv.org/abs/2407.07737)

**ユーザレベルの差分プライバシーによる大規模言語モデルの微調整**

Zachary Charles, Arun Ganesh, Ryan McKenna, H. Brendan McMahan, Nicole Mitchell, Krishna Pillutla, Keith Rush

- 大規模言語モデル（LLM）のユーザレベル差分プライバシー（DP）付きトレーニングアルゴリズムを研究
- 例レベルサンプリング（ELS）とユーザレベルサンプリング（ULS）の2つのDP-SGDバリアントを比較
- 実験を通じて、強力なプライバシー保証や大規模計算予算が必要な場合にULSが有利であることを確認
- LLM対応のトレーニングアルゴリズムに焦点を当て、大規模なモデルや多数のユーザーデータセットにスケール可能であることを示す

ユーザレベルの差分プライバシーで本当に各ユーザーのデータを守れるんだね！LLMの微調整にも応用できるし、未来のデータ保護技術として期待大だわ！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CL, cs.CR, cs.DC, **投稿日時:** 2024-07-10 15:07

- - -

### [Synthetic to Authentic: Transferring Realism to 3D Face Renderings for Boosting Face Recognition](http://arxiv.org/abs/2407.07627)

**合成から本物へ：顔認識向上のための3D顔レンダリングへのリアリズム移植**

Parsa Rahimi, Behrooz Razeghi, Sebastien Marcel

- 3Dレンダリングで生成された顔画像は、大規模な実顔データ収集の困難を回避できる
- しかし、合成データで訓練された顔認識システムは、実データで訓練されたシステムに劣る
- リアリズムを3Dレンダリング画像に移植することで、顔認識システムの性能が向上する
- これにより、実世界のデータを用いたベンチマークでの評価でも改善が見られ、合成データの実用性が高まる

顔認識システムの性能の課題がリアリズムで解決されるって面白そう。これからは合成データでも実データ並みに使える日が来るかもね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-10 13:07

- - -

### [On Leakage of Code Generation Evaluation Datasets](http://arxiv.org/abs/2407.07565)

**コード生成評価データセットの漏洩について**

Alexandre Matton, Tom Sherborne, Dennis Aumiller, Elena Tommasone, Milad Alizadeh, Jingyi He, Raymond Ma, Maxime Voisin, Ellen Gilsenan-McMahon, Matthias Gallé

- コード生成テストセットの汚染が現代の大規模言語モデルで問題
- 直接的なデータ漏洩、合成データを介した間接的なデータ漏洩、評価セットへの過適合が主な原因
- 発見を支持する161のプロンプトとPython解が含まれる新しいデータセットを使用
- データセットはhttps://huggingface.co/datasets/CohereForAI/lbpp で公開されている

データ漏洩の防止って重要だけど難しそう。でも、この新しいデータセットが問題解決の鍵になるといいな！色々調べたくなるね。

**Comment:** 4 main pages, 9 in total

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-07-10 11:50

- - -

### [Federated Foundation Model for Cardiac CT Imaging](http://arxiv.org/abs/2407.07557)

**心臓CT画像のための連合基盤モデル**

Malte Tölle, Philipp Garthe, Clemens Scherer, Jan Moritz Seliger, Andreas Leha, Nina Krüger, Stefan Simm, Simon Martin, Sebastian Eble, Halvar Kelm, Moritz Bednorz, Florian André, Peter Bannas, Gerhard Diller, Norbert Frey, Stefan Groß, Anja Hennemuth, Lars Kaderali, Alexander Meyer, Eike Nagel, Stefan Orwat, Moritz Seiffert, Tim Friede, Tim Seidler, Sandy Engelhardt

- 連合学習は分散データを活用しつつプライバシーを保護する技術であるが、部分的にラベル付けされたデータセットで課題がある
- この研究は、8つの病院で82,124人の患者データを用いて最大規模の連合心臓CT画像分析を実施した
- タスク固有のCNNの知識を統合するTransformerモデルを開発し、未使用のラベルなしデータを活用して精度と一般化性能を向上させた
- Transformerモデルが、下流タスクのためのより有意義な特徴を抽出し、冠動脈のセグメンテーションも解決することを示した

新しいアプローチで医療データをもっと有効活用できるんだね。これからの研究の基盤になるっていうのも、なんか夢が広がる感じするね！



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-07-10 11:30

- - -

### [Generative AI for RF Sensing in IoT systems](http://arxiv.org/abs/2407.07506)

**IoTシステムにおけるRFセンシングのための生成AI**

Li Wang, Chao Zhang, Qiyang Zhao, Hang Zou, Samson Lasaulce, Giuseppe Valenzise, Zhuo He, Merouane Debbah

- 従来のRFセンシングでは雑音や干渉、不完全なデータ、高コストが問題である
- 生成AI技術は高品質な合成データ生成や信号品質の向上、多モーダルデータ統合を提供する
- IoTデバイスの新環境への適応能力を強化し、効率と性能を向上させる
- ケーススタディを通じて、生成AIモデルの統合の有効性を示し、スケーラブルで知的なIoTシステムを実現

生成AIを使ってRFセンシングの問題を解決するなんて、未来の技術っぽくてすごくワクワクするね！IoTシステムがもっと賢くなりそう♡



**トピック:** [合成データ](sd), **カテゴリ:** eess.SP, cs.AI, **投稿日時:** 2024-07-10 09:51

- - -

### [FUNAvg: Federated Uncertainty Weighted Averaging for Datasets with Diverse Labels](http://arxiv.org/abs/2407.07488)

**FUNAvg: 多様なラベルを持つデータセットのための連合不確実性重み付き平均化**

Malte Tölle, Fernando Navarro, Sebastian Eble, Ivo Wolf, Bjoern Menze, Sandy Engelhardt

- 連合学習は分散型でプライバシーを保護する訓練手法だが、部分的なアノテーションが障害となる
- 各サイトは独自のマルチラベルセグメンテーションヘッドを受け取り、連合的に共同バックボーンを学習
- ベイズ技術を利用して、個別のクライアントのラベルだけでなく他のラベルに関する情報も学習
- 分散したセグメンテーションヘッドの不確実性を利用し、重み付き平均化で最終予測を行う

同じデータセットで訓練・テストされたモデルと同等の性能を達成するってすごい！未来のプライバシー保護技術に大きなインパクトを与えそうだね。

**Comment:** Accepted at MICCAI24

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-07-10 09:23

- - -

### [TDML -- A Trustworthy Distributed Machine Learning Framework](http://arxiv.org/abs/2407.07339)

**TDML -- 信頼できる分散型機械学習フレームワーク**

Zhen Wang, Qin Wang, Guangsheng Yu, Shiping Chen

- 大規模生成モデルの進展でGPUリソースの需要が急増
- 供給チェーンの遅延や独占によりGPUの入手が困難
- 連合学習などの分散学習法でデータとモデルを複数サーバーに分散
- ブロックチェーン技術はデータの完全性、スケーラビリティ、信頼性を確保

複雑な分散環境でも信頼性と効率を保てるTDMLのフレームワークが面白そう！これで未来の機械学習も安全にスムーズに進みそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-10 03:22

- - -

### [ViTime: A Visual Intelligence-Based Foundation Model for Time Series Forecasting](http://arxiv.org/abs/2407.07311)

**ViTime: 時系列予測のための視覚インテリジェンス基盤モデル**

Luoxiao Yang, Yun Wang, Xinqi Fan, Israel Cohen, Yue Zhao, Zijun Zhang

- NLPやCVの大規模事前学習モデルの成功により、時系列予測の基盤モデル構築に新たな道が開けた。
- 従来の時系列予測モデルは数値データのフィッティングに依存しがちであった。
- ViTimeは、視覚情報処理パラダイムを用いることで数値データフィッティングの限界を克服する。
- 実験により、多様な予測データセットで最先端のゼロショット性能を達成し、一部の状況では最高の個別学習モデルを超えることが示された。

視覚で時系列データを分析するなんて新しい視点だよね！これで予測精度が上がるなら、AIの未来ももっと広がりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2024-07-10 02:11

- - -

### [BoostCom: Towards Efficient Universal Fully Homomorphic Encryption by Boosting the Word-wise Comparisons](http://arxiv.org/abs/2407.07308)

**BoostCom: ワード単位の比較を強化することで効率的なユニバーサル完全準同型暗号化を目指す**

Ardhi Wiratama Baskara Yudha, Jiaqi Xue, Qian Lou, Huiyang Zhou, Yan Solihin

- 完全準同型暗号（FHE）は、データを暗号化したまま計算を実行可能にし、プライバシー保護の計算操作に大きな可能性を提供
- アリスマティックベースのFHE（ar-FHE）は、非アリスマティックFHE（na-FHE）よりもワード単位の比較操作において優れた性能を示す
- BoostComは、多層ヘテロジニアス並列化やGPU関連の改善などによるインフラ強化と、アルゴリズムに対する最適化を通じてuFHEシステムの効率を向上
- BoostComは、最先端のCPUベースのuFHEシステムに比べて、エンドツーエンドで11.1倍以上の性能向上を達成

厳重に守られたデータでもサクサク処理できる技術とか、夢が広がるよね！データのプライバシーを保ちながら高度な計算ができちゃう未来が楽しみ。

**Comment:** To be appeared on PACT 2024

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-07-10 02:09

- - -

### [Differential privacy and Sublinear time are incompatible sometimes](http://arxiv.org/abs/2407.07262)

**差分プライバシーとサブリニアな時間は時に両立しない**

Jeremiah Blocki, Hendrik Fichtenberger, Elena Grigorescu, Tamalika Mukherjee

- 差分プライバシーとサブリニアアルゴリズムはビッグデータ解析で重要なテーマである
- これまでの研究は差分プライバシーサブリニアアルゴリズムの存在を示してきた
- 本研究は差分プライバシーとサブリニア時間アルゴリズムの下限を初めて解析する
- 一方向マージナルに基づく単純な問題が両立不可能であることを証明した

この論文、具体的な問題に対して、理論的な限界を明らかにしているのが面白い！これからのビッグデータ解析に大きなインパクトを与えそうだよね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, **投稿日時:** 2024-07-09 22:33

- - -

### [Tracing Back the Malicious Clients in Poisoning Attacks to Federated Learning](http://arxiv.org/abs/2407.07221)

**連合学習における毒入攻撃の悪意あるクライアントの追跡**

Yuqi Jia, Minghong Fang, Hongbin Liu, Jinghuai Zhang, Neil Zhenqiang Gong

- 毒入攻撃は、連合学習の訓練フェーズを妥協させて、攻撃者が選んだターゲット入力をミス分類させる
- 既存の防御策は、連合学習の訓練フェーズを保護し、グローバルモデルを毒から守るものが多い
- FLForensicsは、毒入攻撃後に悪意あるクライアントを追跡する初の方法で、既存の防御策を補完する
- 理論的にFLForensicsは毒入攻撃の正式な定義のもとで悪意あるクライアントを正確に区別できることを示し、実証実験でも効果的であることを確認

毒入攻撃に対する新しいアプローチがとても興味深い！効果できちんと追跡できるなら、連合学習の安全性も格段に上がりそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.CR, **投稿日時:** 2024-07-09 20:35

- - -

### [Synthetic Data: Revisiting the Privacy-Utility Trade-off](http://arxiv.org/abs/2407.07926)

**合成データ: プライバシーと有用性のトレードオフ再考**

Fatima Jahan Sarmin, Atiquer Rahman Sarkar, Yang Wang, Noman Mohammed

- 合成データは従来の匿名化技術と比較して、プライバシーと有用性のトレードオフが優れているとは限らない。
- PATEGANやPrivBayesの差分プライバシー保証に関する違反が報告された。
- 上記の研究には特殊な環境やデータ分布が前提とされ、一般的なケースには適用が難しい。
- より一般的な環境で実験した結果、合成データはk-匿名化よりも有利なプライバシーと有用性のトレードオフを示した。

合成データが本当に有効かどうか再検討する姿勢が興味深い！結局、従来の技術と比べても合成データの価値が再確認できたのは朗報だね。



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-07-09 14:48

- - -

### [FedClust: Tackling Data Heterogeneity in Federated Learning through Weight-Driven Client Clustering](http://arxiv.org/abs/2407.07124)

**FedClust: 重み駆動クライアントクラスタリングによる連合学習のデータ異質性への対処**

Md Sirajul Islam, Simin Javaherian, Fei Xu, Xu Yuan, Li Chen, Nian-Feng Tzeng

- 連合学習は分散デバイス上でローカルデータを公開せずに協調的訓練を可能にするが、データ異質性が課題
- 既存のクラスター化連合学習は多数の通信ラウンドを必要とし、事前定義されたクラスター数に依存する
- FedClustはローカルモデルの重みとデータ分布の相関を利用し、部分的重みを基にクライアントを一回でクラスタリング
- FedClustはベンチマーク実験で最大45％の精度向上と2.7倍の通信コスト削減を実現

この研究、新しい手法で連合学習の問題を解決するなんて面白そう！省エネかつ効率的な方法だから、これからますます応用が広がりそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.AI, cs.LG, **投稿日時:** 2024-07-09 02:47

- - -

### [A Trustworthy AIoT-enabled Localization System via Federated Learning and Blockchain](http://arxiv.org/abs/2407.07921)

**信頼できるAIoT対応ローカライゼーションシステム: 連合学習とブロックチェーンによる実現**

Junfei Wang, He Huang, Jingze Feng, Steven Wong, Lihua Xie, Jianfei Yang

- スマートビル向け室内ローカライゼーション技術にはRFセンサーとフィンガープリンティング手法が有望
- これらの手法はIoTデバイスから収集されるデータを使用するためプライバシー問題が発生
- 連合学習を使うことでプライバシー問題を部分的に解決する提案がされているが、セキュリティ上の懸念が残る
- 提案するDFLocフレームワークは、3Dローカライゼーションを精密に実現し、単一障害点と悪意のある攻撃への対策も行う

ブロックチェーンを使ってローカライゼーションの信頼性を高めるなんてセキュリティ面でも安心だね。未来のスマートビル構想がますます楽しみ～！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, eess.SP, **投稿日時:** 2024-07-08 04:14

- - -

### [Non-Cooperative Backdoor Attacks in Federated Learning: A New Threat Landscape](http://arxiv.org/abs/2407.07917)

**連合学習における非協力的バックドア攻撃: 新たな脅威の地平**

Tuan Nguyen, Dung Thuy Nguyen, Khoa D Doan, Kok-Seng Wong

- 連合学習はプライバシー保護が期待されるが、バックドア攻撃の脅威が潜む
- 非協力的な複数トリガー攻撃を調査し、攻撃者が独立して異なるトリガーを導入
- 実験で、連合学習がこのような非協力的攻撃に対して著しく脆弱であることを確認
- 主タスクに影響を与えない個別のバックドアが成功し、検出が困難であると判明

非協力的な攻撃がどれだけ効果的か驚いたね！連合学習の安全性を強化する新しい方法がどんどん出てきそうで楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.CV, cs.LG, **投稿日時:** 2024-07-05 22:03

- - -

### [UAV-assisted Unbiased Hierarchical Federated Learning: Performance and Convergence Analysis](http://arxiv.org/abs/2407.07739)

**UAV支援によるバイアスのない階層的連合学習: パフォーマンスと収束解析**

Ruslan Zhagypar, Nour Kouzayha, Hesham ElSawy, Hayssam Dahrouj, Tareq Y. Al-Naffouri

- 階層的連合学習（HFL）はエッジデバイス間で学習を分散し、地上サーバーでのグローバルモデル集約を目指す
- 通信チャネルの信頼性の欠如がHFLシステムの真の利益評価の障壁となる
- 本論文では、UAV支援の無線ネットワーク向けにバイアスのないHFLアルゴリズムを提案
- 提案手法の理論的収束保証を検証し、UAVの数や高さなどのシステムパラメータの最適化が可能

UAVでHFLの通信の信頼性がアップするの面白そう！UAV支援の影響は将来の無線ネットワークインフラでも期待大だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, cs.LG, cs.NI, math.IT, **投稿日時:** 2024-07-05 06:23
