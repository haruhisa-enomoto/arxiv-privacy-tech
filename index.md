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

更新: 2024-12-17T04:25:10.252580

- - -

### [The Impact of Generalization Techniques on the Interplay Among Privacy, Utility, and Fairness in Image Classification](http://arxiv.org/abs/2412.11951)

**画像分類におけるプライバシー、効用、公平性の相互作用に対する一般化技術の影響**

Ahmad Hassanpour, Amir Zarei, Khawla Mallat, Anderson Santana de Oliveira, Bian Yang

- 画像分類でのプライバシーと効用のトレードオフを改善する一般化技術を探求
- SATと差分プライバシーを組み合わせたDP-SATがバランスを向上させる
- 合成データと実世界データでのバイアスを分析し、公平性を評価
- 新しいメトリック「ハーモニックスコア」で精度、プライバシー、公平性を統合評価

この研究、AI分類の公平性とプライバシーの関係を深掘りしてておもしろそう！新しい評価指標とか、いろんなバランスを探るのってすごく重要だよね。繊細なバランスを見つけて、より公平で安全なシステムを作りたいな。

**Comment:** Published as a conference paper at the 25th Privacy Enhancing   Technologies Symposium (PETS 2025)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-16 16:35

- - -

### [Beyond Dataset Creation: Critical View of Annotation Variation and Bias Probing of a Dataset for Online Radical Content Detection](http://arxiv.org/abs/2412.11745)

**データセット作成を超えて: オンライン過激コンテンツ検出用データセットのアノテーション変動とバイアスの批判的視点**

Arij Riabi, Virginie Mouilleron, Menel Mahamdi, Wissam Antoun, Djamé Seddah

- オンラインの過激コンテンツは多言語対応が難しく、既存データセットでは不十分な点が多い。
- 新たに英語、フランス語、アラビア語で過激化レベルなどをアノテーションしたデータセットを提供。
- 個人のプライバシーを守りつつ、アノテーション過程におけるバイアスと評価者間の不一致を分析。
- 合成データで社会人口統計的要因の影響を調査し、公平性や透明性の重要性を強調。

この研究って、過激なコンテンツをもっと上手に見つけるためのデータ作りがテーマなんだね。手法もいろいろ入ってて、データの公平さを大事にしているところがすごく良さそう！

**Comment:** Accepted to COLING 2025

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-16 13:03

- - -

### [Conditional Diffusion Models Based Conditional Independence Testing](http://arxiv.org/abs/2412.11744)

**条件付き独立性検定に基づく条件付き拡散モデル**

Yanfeng Yang, Shuai Li, Yingjie Zhang, Zhuoran Sun, Hai Shu, Ziqi Chen, Renmin Zhang

- 条件付き独立性検定は統計学と機械学習で重要な課題
- 条件付き分布$X|Z$の正確な近似が実務で重要
- 提案する条件付き拡散モデルは分布を正確に近似
- 試験は高次元データでもタイプIとIIのエラーを効果的に制御

この研究、条件付き独立性の検定を新しくする方法って感じでワクワクしそう！高次元でもエラーを制御できるって、これからのデータ分析がもっと自由になりそうだね！

**Comment:** 17 pages, 7 figures, aaai 2025

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-12-16 13:03

- - -

### [Efficiently Achieving Secure Model Training and Secure Aggregation to Ensure Bidirectional Privacy-Preservation in Federated Learning](http://arxiv.org/abs/2412.11737)

**連合学習における双方向プライバシー保護のための効率的な安全モデル訓練と安全集約の実現**

Xue Yang, Depan Peng, Yan Feng, Xiaohu Tang, Weijun Fang, Jun Shao

- 双方向のプライバシー保護連合学習は、局所勾配とグローバルモデルのプライバシー漏洩を防ぐために重要
- サーバー側でのモデル摂動法とクライアント側での分散差分プライバシー機構を組み合わせ、高精度で効率的なプライバシー保護を実現
- 実験結果では、計算コスト、モデル精度、プライバシー攻撃防御力で最先端の基準を上回る
- ターゲット精度を達成する際の訓練時間が他手法の約200倍以上速く、プライバシー予算が小さい場合でも低精度損失に留まる

革新的な手法だね！プライバシーを守りつつ精度も保てるなんて、連合学習の未来が楽しみだね。こんな技術がもっと日常的になるのかな？ワクワクだ！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-16 12:58

- - -

### [Just a Simple Transformation is Enough for Data Protection in Vertical Federated Learning](http://arxiv.org/abs/2412.11689)

**単純な変換だけで垂直連合学習におけるデータ保護は十分である**

Andrei Semenov, Philip Zmushko, Alexander Pichugin, Aleksandr Beznosikov

- 垂直連合学習は協調的に深層学習モデルを訓練しつつプライバシーを保護する手法
- 特徴再構成攻撃はデータの事前分布の知識なしに成功しないと理論的に主張
- 単純なモデルの変換が入力データ保護に大きな影響を与えることを実証
- 実験でMLPベースのモデルが最先端の特徴再構成攻撃に対抗できることを示す

攻撃に対する防御策がシンプルな変換だけでできちゃうなんて面白いよね！垂直連合学習がもっと安全に使われるようになりそうで、すごく未来が楽しみだな～。

**Comment:** 29 pages, 12 figures, 3 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, I.2.m; F.2.0, **投稿日時:** 2024-12-16 12:02

- - -

### [UA-PDFL: A Personalized Approach for Decentralized Federated Learning](http://arxiv.org/abs/2412.11674)

**UA-PDFL: 分散型連合学習のための個別化アプローチ**

Hangyu Zhu, Yuxiang Fan, Zhenping Xie

- 連合学習はデータ漏洩を防ぎつつグローバルモデルを学習するが、中央サーバーがボトルネックとなる。
- 分散型連合学習（DFL）は中央サーバーを排除し、参加者全員が通信するが、非IIDデータで性能が低下する。
- 新たな個別化レイヤーを導入したUA-PDFLは、非IIDデータの問題に対処し、データの偏りを軽減する。
- クライアントごとのドロップアウトやレイヤーごとの個別化でDFLの学習性能を向上させることを示した。

UA-PDFLって、個別化ってところがすごくユニークで面白そう！非IIDデータの対応、どんなふうに効果を発揮するのか見てみたいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-16 11:27

- - -

### [Non-Convex Optimization in Federated Learning via Variance Reduction and Adaptive Learning](http://arxiv.org/abs/2412.11660)

**連合学習における非凸最適化: 分散削減と適応学習による改善**

Dipanwita Thakur, Antonella Guzzo, Giancarlo Fortino, Sajal K. Das

- 勢いに基づく分散削減と適応学習を組み合わせた新たな連合アルゴリズムを提案
- 非同質なデータでの勾配分散や学習率調整による収束遅延を解決
- 改善されたコミュニケーション複雑性で、$\mathcal{O}(\epsilon^{-1})$の収束を実現
- MNISTやCIFAR-10での画像分類タスクで効率性と精度を実証

ある意味で、この研究は未来の連合学習技術がどのように成長していくのかを垣間見せてくれるかも！イノベーションを活かして、より効率的な学習モデルの開発につながると素敵だね！

**Comment:** FLUID Workshop@AAAI 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-16 11:02

- - -

### [BA-BFL: Barycentric Aggregation for Bayesian Federated Learning](http://arxiv.org/abs/2412.11646)

**BA-BFL: ベイジアン連合学習のためのバリセントリック集約**

Nour Jamoussi, Giuseppe Serra, Photios A. Stavrou, Marios Kountouris

- ベイジアン連合学習(BFL)の集約ステップを情報幾何学的視点で解釈
- パラメトリックなα-ダイバージェンスのバリセントリック問題を研究
- 逆カラバック・ライブラーと平方ワッサースタイン-2のバリセントリを理論的に導出
- 提案手法は非IID環境での精度、不確実性、モデルキャリブレーション、公平性でSOTAに匹敵

ベイジアン連合学習の集約って、幾何的な解釈もできるんだね！数学的に綺麗な解法が見つけられるかも。性能もいいみたいだから、どんな応用が広がるのかワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, cs.NI, math.IT, **投稿日時:** 2024-12-16 10:47

- - -

### [Capacity of Hierarchical Secure Coded Gradient Aggregation with Straggling Communication Links](http://arxiv.org/abs/2412.11496)

**階層的安全コーデッド勾配集約における遅延コミュニケーションリンクの容量**

Qinyi Lu, Jiale Cheng, Wei Kang, Nan Liu

- 分散学習でのプライバシー問題解決のため、セキュアな集約技術が採用されている
- 階層的ネットワークでのコーデッド勾配集約問題を考案し、遅延リンクへの対策も含む
- ユーザー情報を守りつつ勾配の合計を取得、新たな手法を提案して最適結果を追求
- Vandermonde行列を使って特別な構造の通信を実現、最適なバウンドを導出

頭がいい話だね！分散学習の中でどうやって安全性を高めるのか、すごく興味深いね。未来にはもっとシームレスに個人情報が守られそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, math.IT, **投稿日時:** 2024-12-16 07:16

- - -

### [Vertical Federated Unlearning via Backdoor Certification](http://arxiv.org/abs/2412.11476)

**垂直連合学習におけるバックドア認証による消去技術**

Mengde Han, Tianqing Zhu, Lefeng Zhang, Huan Huo, Wanlei Zhou

- 垂直連合学習はデータプライバシーを保ちながら協調学習を可能にする方法である
- プライバシー規制で個人の「忘れられる権利」が強調され、特定のデータを消去する機能が求められる
- 特定クライアントの影響を消しつつ、他のデータは保持するメカニズムを研究
- 勾配上昇法とバックドア機構を活用し、安全かつ効果的にデータ貢献の消去を実現

この研究、消去技術がどんどん面白くなってきたね！個人情報を守りつつ、協調もできるって未来的だしワクワクする～！でも、これ使いこなすのは難しそうー、お互いに協力しなきゃだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-16 06:40

- - -

### [FedCAR: Cross-client Adaptive Re-weighting for Generative Models in Federated Learning](http://arxiv.org/abs/2412.11463)

**FedCAR: 連合学習における生成モデルのためのクライアント間適応リウェイト**

Minjun Kim, Minjee Kim, Jinhoon Jeong

- 複数の病院データを集めた生成モデルは、多様なデータ分布で深い理解を提供できる
- プライバシーでデータを共有しにくい問題に対して、連合学習が解決策として浮上
- 生成モデルに特化した集約アルゴリズムが未開発で、新アルゴリズムを提案
- 提案手法は生成画像の分布距離を測定し学習効率を向上、既存手法を上回る成果を示す

生成モデルでのクライアント貢献度を柔軟に変えるアイデアが面白いよね！しかも、そのアプローチで医療画像を生成するって、未来にはすごく実用的かもって思った！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-12-16 05:43

- - -

### [TRAIL: Trust-Aware Client Scheduling for Semi-Decentralized Federated Learning](http://arxiv.org/abs/2412.11448)

**TRAIL: 信頼を考慮したクライアントスケジューリングによる半分散型連合学習**

Gangqiang Hu, Jianfeng Lu, Jianmin Han, Shuqin Cao, Jing Liu, Hao Fu

- 半分散型連合学習ではクライアントの通信と学習状態が動的に変化する
- 信頼意識を持つクライアントスケジューリング(TRAIL)を提案し、選択的クライアント参加で効率化
- 適応型隠れセミマルコフモデルでクライアントの通信状態と貢献度を推定する
- 実験結果ではテスト精度が8.7%向上し、学習損失が15.3%減少と効果を示した

この研究、すごくない！？連合学習の新しい可能性が広がりそうでワクワクするよね。データを守りながら効率よく学習できるなんて未来が楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-12-16 05:02

- - -

### [Federated Domain Generalization with Label Smoothing and Balanced Decentralized Training](http://arxiv.org/abs/2412.11408)

**ラベルスムージングとバランスの取れた分散トレーニングを活用した連合領域一般化**

Milad Soltany, Farhad Pourpanah, Mahdiyar Molahasani, Michael Greenspan, Ali Etemad

- FedSBは連合学習におけるデータ異質性の課題を解決するために提案
- クライアントレベルでのラベルスムージングがドメイン固有の特徴への過適合を防止
- 分散予算制御によりクライアント間のトレーニングバランスを向上し、全体的なモデル性能が向上
- PACS、VLCS、OfficeHome、TerraIncの4つのデータセットで最先端の結果を達成

分散トレーニングでのバランスってすごく面白いよね！効率的に学習するには欠かせないし、こういう方法がもっと普及すると未来のAIの可能性が広がってワクワクするな～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-16 03:25

- - -

### [Modeling Inter-Intra Heterogeneity for Graph Federated Learning](http://arxiv.org/abs/2412.11402)

**グラフ連合学習のための異種性間・異種性内モデリング**

Wentao Yu, Shuo Chen, Yongxin Tong, Tianlong Gu, Chen Gong

- 連合学習における異種性は特にグラフデータで複雑なノード関係により課題となる
- 既存の方法ではサブグラフ間の類似性を算出して重み付けしているが限界がある
- 提案手法FedIIHは異種性間・異種性内を統合的にモデル化し、精度の高い学習が可能に
- 実験ではFedIIHが他の9つの最先端手法よりも平均5.79%優れた結果を示す

この論文って、グラフデータの複雑さをうまく処理する新しい方法を提案してて、すごく面白そうだね！実験でも既存手法より良い結果が出てるし、これが応用される未来が楽しみだなって思うんだ。

**Comment:** accepted by AAAI 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-16 03:02

- - -

### [PSGraph: Differentially Private Streaming Graph Synthesis by Considering Temporal Dynamics](http://arxiv.org/abs/2412.11369)

**PSGraph: 時間的ダイナミクスを考慮した差分プライバシーのストリーミンググラフ合成**

Quan Yuan, Zhikun Zhang, Linkang Du, Min Chen, Mingyang Sun, Yunjun Gao, Michael Backes, Shibo He, Jiming Chen

- ストリーミンググラフには多くのプライバシーリスクがあるため、直接共有は危険
- 現行の方法では静的グラフに焦点を当てており、隣接グラフの関係性が無視されがち
- PSGraphはストリーミンググラフにおける差分プライバシーのための枠組みを提案
- 実験結果に基づき、PSGraphの優位性が4つの実世界データセットで示された

PSGraphって革新的で面白そう！リアルタイムでプライバシーを重視しつつデータを扱えるから、未来のソーシャルメディアとかで便利かもね。どんな風に活用されるのかが楽しみだな！



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-16 01:56

- - -

### [ProFe: Communication-Efficient Decentralized Federated Learning via Distillation and Prototypes](http://arxiv.org/abs/2412.11207)

**ProFe: 蒸留とプロトタイプによる通信効率の良い分散型連合学習**

Pedro Miguel Sánchez Sánchez, Enrique Tomás Martínez Beltrán, Miguel Fernández Llamas, Gérôme Bovet, Gregorio Martínez Pérez, Alberto Huertas Celdrán

- 分散型連合学習はモデルの集中化リスクを排除し通信ボトルネックを改善する
- 異種データ分布環境での通信管理とモデル集約に課題がある
- ProFeは知識蒸留とプロトタイプ学習、量子化技術を融合した通信最適化アルゴリズムを提案
- 最大40-50%の通信コスト削減を実現しつつモデル性能を維持または向上するが、訓練時間が20%増加する

このProFeって、通信コストをグッと減らせるのにモデルの性能落ちないなんてすごいね！でも、訓練時間がちょっと増えるみたいだから、ここを工夫できたらもっと完璧になりそうな予感！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, cs.NI, **投稿日時:** 2024-12-15 14:49

- - -

### [OccScene: Semantic Occupancy-based Cross-task Mutual Learning for 3D Scene Generation](http://arxiv.org/abs/2412.11183)

**OccScene: セマンティック占有ベースのタスク間相互学習を用いた3Dシーン生成**

Bohan Li, Xin Jin, Jianan Wang, Yukai Shi, Yasheng Sun, Xiaofeng Wang, Zhuang Ma, Baao Xie, Chao Ma, Xiaokang Yang, Wenjun Zeng

- 既存の方法は3Dシーン生成と知覚を区別し合成データを生成するだけ
- OccSceneはこれらを統合し、タスク間で相乗効果を実現することを提案
- セマンティック占有に基づきテキストからリアルな3Dシーンを生成
- 双方向の学習で知覚と生成の性能を相互に向上させる

楽しそうなシーンの生成ができるなんてすごい！現実世界での応用が進めばすっごく面白いことになりそうだよね。思わず3D世界に飛び込みたくなっちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-15 13:26

- - -

### [AD-LLM: Benchmarking Large Language Models for Anomaly Detection](http://arxiv.org/abs/2412.11142)

**AD-LLM: 異常検知のための大規模言語モデルのベンチマーク**

Tiankai Yang, Yi Nian, Shawn Li, Ruiyao Xu, Yuangang Li, Jiaqi Li, Zhuo Xiao, Xiyang Hu, Ryan Rossi, Kaize Ding, Xia Hu, Yue Zhao

- 異常検知は、詐欺検出や医療診断などで重要な機械学習課題である
- NLPでは、スパムや誤情報の検出に異常検知が役立ち、大規模言語モデルの可能性は未充分
- この論文は、異常検知におけるLLMの評価ベンチマーク「AD-LLM」を初めて提案
- 実験では、LLMの零ショット検出や生成データが有用で、モデル選択に課題が残るとした

AIってこんなに幅広く使えるなんてすごい！異常検知ってSFみたいでワクワクするよね。もっと日常生活でも活用されそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-12-15 10:22

- - -

### [Understanding and Mitigating Memorization in Diffusion Models for Tabular Data](http://arxiv.org/abs/2412.11044)

**拡散モデルにおける表形式データの記憶問題の理解と軽減**

Zhengyu Fang, Zhimeng Jiang, Huiyuan Chen, Xiao Li, Jing Li

- 拡散モデルでの記憶は、画像やテキストで研究されているが、表形式データでは未検討
- 記憶は学習エポックの増加によって拡散モデルで発生し、データセットサイズや特徴量次第
- TabCutMixというデータ拡張技術を提案し、クラス内での特徴交換により記憶を軽減
- TabCutMixPlusでは特徴間の相関に基づきクラスター化し、特徴のコヒーレンスを保持

記憶の抑制について詳しく調べてるの面白いかも！自然なデータ生成を目指す工夫がすごそうだし、どんな応用ができるかワクワクしちゃうね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-15 04:04

- - -

### [Predicting Survival of Hemodialysis Patients using Federated Learning](http://arxiv.org/abs/2412.10919)

**連合学習を用いた血液透析患者の生存率予測**

Abhiram Raju, Praneeth Vepakomma

- 腎移植待機中の血液透析患者は誤認識されることがあり、待機時間が延びることがある
- 生存率予測には敏感な大規模データが必要だが、データは分散しており統合モデルが困難
- 連合学習を用いることでデータを共有せずに局地モデルより高性能な予測が可能
- インド最大の透析センターであるNephroPlusのデータで、連合学習の性能を検証した

連合学習を用いることで、データのプライバシーを守りつつも高精度な予測が可能になるってすごくない？体育の時間にこのテーマで話したら盛り上がりそうな予感がするんだけど！

**Comment:** 6 pages, 2 figures, 4 tables, Presented at MIT Undergraduate Research   Technology Conference and to be published as conference proceeding at IEEE   Xplore

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-14 18:10

- - -

### [Task Diversity in Bayesian Federated Learning: Simultaneous Processing of Classification and Regression](http://arxiv.org/abs/2412.10897)

**ベイズ連合学習におけるタスク多様性: 分類と回帰の同時処理**

Junliang Lyu, Yixuan Zhang, Xiaoling Lu, Feng Zhou

- 現行の連合学習は同質タスクに偏重し、多様性を十分に考慮していない。
- マルチタスク学習を取り入れ、局所でMOGPを使用し、連合学習を全球的に適用。
- MOGPは分類と回帰の関連タスクを扱い、確率を定量化するベイズ非パラメトリックアプローチ。
- ポリア・ガンマ補完技法と平均場変分推論を用い、計算効率と収束速度を向上。

この研究、マルチタスクに対応する連合学習を提案してるのがすごく面白いね！特に、不確実性の計量をベイズ的にやっているところが、実用化の可能性を高めそう。未来が楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-12-14 17:10

- - -

### [Adaptive Quantization Resolution and Power Control for Federated Learning over Cell-free Networks](http://arxiv.org/abs/2412.10878)

**連合学習のためのセルフリーネットワークにおける適応量子化解像度と電力制御**

Afsaneh Mahmoudi, Emil Björnson

- 連合学習はデータプライバシー保持と通信オーバーヘッド削減を目指すが、ユーザー数とモデルサイズで待機時間が増加
- CFmMIMO技術は空間多重化でアップリンク待機時間を減少させ、多数ユーザーに同じリソースを提供
- 重要部分に高解像度を割り当てる適応量子化スキームの導入で、待機時間の分散を軽減
- 提案手法は通信オーバーヘッドを93%以上削減、比較手法より10%高いテスト精度を達成

この論文、新しい技術を使って通信量を大幅に減らして、しかも精度も上がってるってすごいね！たくさんのデータやユーザーを扱う未来のネットワークでは、この技術がさらに活躍しそうで魅力的だと思ったよ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.NI, eess.SP, **投稿日時:** 2024-12-14 16:08

- - -

### [Client-Side Patching against Backdoor Attacks in Federated Learning](http://arxiv.org/abs/2412.10605)

**連合学習におけるバックドア攻撃に対するクライアントサイドパッチング**

Borja Molina Coronado

- 連合学習は、分散環境でモデルを訓練する有用な枠組みだが、悪意ある参加者によるバックドア攻撃に脆弱。
- 提案手法は、連合学習システムでクライアントサイドのバックドア攻撃を緩和する新たな防御メカニズム。
- 敵対的学習技術とモデルのパッチングを活用し、バックドア攻撃の影響を中和する。
- MNISTやFashion-MNISTでの実験で、既存防御を上回る成果を示し、クリーンデータで競争力を保持。

マジ面白そう！バックドア攻撃を防ぐのって超重要じゃん。しかも実験でちゃんと成果出てるとかすごいね。連合学習の信頼性がもっと高まると、いろんな分野での活用が進みそう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-12-13 23:17

- - -

### [ExclaveFL: Providing Transparency to Federated Learning using Exclaves](http://arxiv.org/abs/2412.10537)

**ExclaveFL: エンクレーブによる連合学習の透明性提供**

Jinnan Guo, Kapil Vaswani, Andrew Paverd, Peter Pietzuch

- 連合学習ではデータプロバイダがトレーニングデータを開示せずにモデルを共同でトレーニングするが、不正プロバイダによる攻撃のリスクがある。
- 現在の対応策は信頼できる実行環境（TEE）を利用しているが、FLには不必要な機密性保障を提供し、側面チャネル攻撃に弱い。
- ExclaveFLはインテグリティのみに注力した新しいハードウェアセキュリティ抽象「エンクレーブ」を使用し、攻撃検出のためのエンドツーエンドの透明性と整合性を提供する。
- ExclaveFLはタスク実行時に細粒度のハードウェアベースのアテステーションレポートを生成し、9%以下のオーバーヘッドで多様な攻撃を検出可能。

すごくおもしろそう！FLの透明性も確保しつつ攻撃を防ぐ手法とかワクワクする。そして、エンクレーブのアイデアってほんと革新的で未来が広がりそうだね。



**トピック:** [連合学習](fl), [TEE](tee), **カテゴリ:** cs.CR, cs.DC, cs.LG, **投稿日時:** 2024-12-13 20:20

- - -

### [Differentially Private Multi-Sampling from Distributions](http://arxiv.org/abs/2412.10512)

**差分プライバシーによる分布からのマルチサンプリング**

Albert Cheu, Debanuj Nayak

- 差分プライバシーアルゴリズムは、分布からのサンプルを推定し、従来は単一サンプルを対象にしていた
- マルチサンプリングでは、複数サンプルのプライベートな近似を目指し、実データ分析に適用可能
- 有限ドメインでは、従来の方法よりサンプルの複雑さをm倍改善することができる
- ガウス分布では、純粋な差分プライバシー下でのシングルおよびマルチサンプリングが可能で、独自のラプラス機構を使用

差分プライバシーでマルチサンプリングとか、なんか未来っぽくてワクワクするよね！プライバシーを守りつつデータ使えるのって便利だし、もっと普及してほしいなー。

**Comment:** 22 pages

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, cs.LG, stat.ML, **投稿日時:** 2024-12-13 19:14

- - -

### [Benchmarking Federated Learning for Semantic Datasets: Federated Scene Graph Generation](http://arxiv.org/abs/2412.10436)

**意味のあるデータセットに対する連合学習のベンチマーク: 連合シーングラフ生成**

SeungBum Ha, Taehwan Lee, Jiyoun Lim, Sung Whan Yoon

- 連合学習は、データを分散したまま深層モデルを学習する枠組みとして注目されている
- 既存のベンチマークは単純な分類タスクの取り扱いに偏っているが、複雑なセマンティクスには対処していない
- 提案手法では、意味情報でデータをクラスタリングし、クライアント間でセマンティックな多様性を制御して分配
- 提案手法により、データの異質性を考慮した連合学習アルゴリズムの性能向上を実証

連合学習を複雑なシーングラフ生成に応用するのって新しいね！意味情報の多様性を制御することで、実用性が広がりそうでワクワクするよ～。どんな応用が考えられるのか楽しみだなぁ。

**Comment:** This work has been submitted to the IEEE for possible publication

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-12-11 08:10
