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

更新: 2024-12-22T04:20:19.596519

- - -

### [OnlineVPO: Align Video Diffusion Model with Online Video-Centric Preference Optimization](http://arxiv.org/abs/2412.15159)

**オンラインVPO: オンラインビデオ中心の嗜好最適化によるビデオ拡散モデルの整列**

Jiacheng Zhang, Jie Wu, Weifeng Chen, Yatai Ji, Xuefeng Xiao, Weilin Huang, Kai Han

- テキストからビデオ(T2V)生成には課題があり、画像品質の低下やちらつきが問題
- ビデオ拡散モデル(VDM)のフィードバック学習は有望だが、整合性やスケーラビリティに限界がある
- OnlineVPOは合成データで訓練されたVQAモデルを報酬として使用し、整合性のあるフィードバックを実現
- オンラインDPOアルゴリズムで既存の学習フレームワークのオフポリシー最適化とスケーラビリティ問題に対処

新しいビデオ生成の手法にワクワクだよね！この研究が未来のムービー制作にも役立ちそうで楽しみ。どんな進化が待ってるのか期待しちゃう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-19 18:34

- - -

### [Efficient Ranking, Order Statistics, and Sorting under CKKS](http://arxiv.org/abs/2412.15126)

**CKKSにおける効率的なランキング、順序統計量、ソート**

Federico Mazzone, Maarten Everts, Florian Hahn, Andreas Peter

- 完全準同型暗号(FHE)は暗号化データ上での操作を可能にし、プライバシーを保つアプリケーションに有用
- 暗号化下での要素比較はコストが高く、FHEでのランキングやソートの効率的な実装が困難
- 従来手法はスワップに基づくが、比較の深さO(log^2(N))が課題である
- 本提案は比較深さをO(1)にして並行化を実現し、計算オーバーヘッドを最小化

この研究、暗号化データでもランキングやソートできちゃうんだね！プライバシーに配慮した新たな解決策、未来のデータ処理に役立ちそう！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-19 18:06

- - -

### [Robust Federated Learning in the Face of Covariate Shift: A Magnitude Pruning with Hybrid Regularization Framework for Enhanced Model Aggregation](http://arxiv.org/abs/2412.15010)

**共変量シフトに対する堅牢な連合学習: モデル集約を強化するためのマグニチュードプルーニングとハイブリッド正則化フレームワーク**

Ozgu Goksu, Nicolas Pugeault

- 個人のデータのプライバシー保護をしながら共有モデルを開発するために、連合学習は有望
- クライアント間のデータ分布の違いは、主に集約プロセスの不安定性によりFL手法に深く影響
- 個々のパラメータのプルーニングと正則化技術を組み合わせ、共変量シフトへの影響を軽減
- 提案手法は大規模な共変量シフトやクライアントが少数でも頑強な表現を抽出可能

新しい連合学習の方法で、どんな偏ったデータにも強く立ち向かえるって凄くない？この提案が実際にどんな風に使われていくのか、色んなデータセットを通じて見ていけたら面白そうだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-12-19 16:22

- - -

### [DS-ABSA: Dual-Stream Data Synthesis with Label Refinement for Few-Shot Aspect-Based Sentiment Analysis](http://arxiv.org/abs/2412.14849)

**DS$^2$-ABSA: ラベル精緻化によるデュアルストリームデータ合成を用いた少数ショット要素ベース感情分析**

Hongling Xu, Yice Zhang, Qianlong Wang, Ruifeng Xu

- 少数ショットで要素ベースの感情分析を行う際、既存手法は多様性が不足し効果が限定的。
- LLMを活用したデータ合成技術で、要点駆動とインスタンス駆動の双方向からデータを生成。
- ラベルの精緻化を行うモジュールを導入し、生成ラベルの品質を向上。
- 評価実験で、既存の少数ショットABSA手法や他のLLMベースのデータ生成法を大きく上回る性能を示す。

デュアルストリームのアプローチって面白いね！これまでの方法に新しい風を吹き込む感じで、新たなABSA手法のスタンダードになるかも！？



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-19 13:39

- - -

### [Federated Heavy Hitter Analytics with Local Differential Privacy](http://arxiv.org/abs/2412.14832)

**連合型ヘビーヒッター分析とローカル差分プライバシー**

Yuemin Zhang, Qingqing Ye, Haibo Hu

- 連合型ヘビーヒッター分析は、各主体間の利用者の嗜好理解を高める技術である
- プライバシー保護の課題を解決する為にローカル差分プライバシー（LDP）を使用
- LDPのノイズ注入による効用低下や通信コスト増が課題
- 提案した新機構は、適応的拡張戦略と合意に基づく剪定を活用し課題を解消

連合型のデータ分析って複数の異なるサービスでの利用者データを安全に活用できるから、もっと良いサービスが作れそうでワクワクするね。ようは、使い方次第でお互いにメリットがありそう！

**Comment:** Accepted by SIGMOD 2025

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-12-19 13:20

- - -

### [ResoFilter: Rine-grained Synthetic Data Filtering for Large Language Models through Data-Parameter Resonance Analysis](http://arxiv.org/abs/2412.14809)

**ResoFilter: データパラメータ共鳴分析による大規模言語モデルのための精密な合成データフィルタリング**

Zeao Tu, Xiangdi Meng, Yu He, Zihan Yao, Tianyu Qi, Jun Liu, Ming Li

- 大規模言語モデルは様々なドメインで効果的だが、合成データの質が問題
- ResoFilterを提案し、モデルの重みでデータ特性を表現し、解釈性を向上
- 実験でResoFilterはデータの半分で全持続的な微調整並みの結果を達成
- 合成データセット構築と高品質データ評価に有用な知見を提供

新しいフィルタリング技術で合成データの質を保つことができるなんて面白いよね。データの半分でも結果が出るのは効率的だし、活用の幅が広がりそう！

**Comment:** under review

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-19 12:57

- - -

### [ALKAFI-LLAMA3: Fine-Tuning LLMs for Precise Legal Understanding in Palestine](http://arxiv.org/abs/2412.14771)

**ALKAFI-LLAMA3: パレスチナの法的理解のためのLLMの微調整**

Rabee Qasem, Mohannad Hendi, Banan Tantour

- 大規模言語モデル(LLMs)は多様な分野で有望だが、法曹界、特に低資源環境での適用は限られている
- 政治的不安定、法律の断片化、AIリソースの制約がパレスチナの法的領域へのLLM適用を妨げている
- パレスチナの法律テキストから合成データを生成し、Llama-3.2-1B-Instructを微調整したモデルを提案
- 経済的かつ効果的な法的助言を提供し、クエリのパフォーマンスを評価し改善点も示した

パレスチナの法律の文脈に合ったAIツールを作っているのがいい感じ！限られたリソースで現地にあったソリューションを目指しててすごく応援したくなるね。ローカルにカスタマイズされた技術ってこれからの未来を作りそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-12-19 11:55

- - -

### [FLAMe: Federated Learning with Attention Mechanism using Spatio-Temporal Keypoint Transformers for Pedestrian Fall Detection in Smart Cities](http://arxiv.org/abs/2412.14768)

**FLAMe: スマートシティにおける歩行者転倒検知用の時空間キーポイントトランスフォーマによるアテンションメカニズムを用いた連合学習**

Byeonghun Kim, Byeongjoon Noh

- スマートシティでの歩行者転倒検知の課題を解決するため、FLAMeシステムを提案
- FLAMeは重要なキーポイント情報を学習し、通信コスト削減とデータプライバシーを維持
- 軽量なキーポイントトランスフォーマモデルを連合学習フレームワークに統合し、時空間特徴を効果的に学習
- 約22,672のビデオサンプルを使った実験で、94.02%の精度を達成し、通信コストを約40%削減

この論文、すごくワクワクするね！FLAMeを使ってスマートシティの安全を守るなんて、なんだか未来のまちづくりに役立ちそう。通信コストをそんなに削減できるなんて、便利すぎる♡

**Comment:** 8 pages, 7 figures, AAAI 2025 FLUID Workshop

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-19 11:51

- - -

### [How to Synthesize Text Data without Model Collapse?](http://arxiv.org/abs/2412.14689)

**モデル崩壊を起こさずにテキストデータを合成する方法**

Xuekai Zhu, Daixuan Cheng, Hengli Li, Kaiyan Zhang, Ermo Hua, Xingtai Lv, Ning Ding, Zhouhan Lin, Zilong Zheng, Bowen Zhou

- 合成データにはモデル崩壊を引き起こすリスクがある
- 合成データと人間作成データの比率が高いほど性能が低下する
- トークン編集を使った半合成データがモデル崩壊を防ぐ
- トークン編集によりデータ品質向上とモデル性能改善を実証

人間が作るデータに手を加えて合成データを作るなんて面白い考え方！どんなトークン編集方法がいいのか気になるね。これ、将来のAIモデルにすごく役立ちそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-12-19 09:43

- - -

### [Bel Esprit: Multi-Agent Framework for Building AI Model Pipelines](http://arxiv.org/abs/2412.14684)

**Bel Esprit: 複数エージェントによるAIモデルパイプライン構築フレームワーク**

Yunsu Kim, AhmedElmogtaba Abdelaziz, Thiago Castro Ferreira, Mohamed Al-Badrashiny, Hassan Sawaf

- 単一のAIモデルでは複雑な現実のタスクに対応が難しいため、複数モデルの統合が必要である  
- Bel Espritはユーザーの要求に基づきAIモデルパイプラインを構築する会話エージェントである  
- 複数エージェントが協力し、要求の明確化、モデル構築、妥当性検証、パイプライン内モデルの配置を行う  
- Bel Espritは曖昧なユーザーの問い合わせからパイプラインを生成する効果を示し、詳細なエラー分析も実施  

AIパイプラインを自動で組めるとかすごくない！？曖昧な指示にも対応できるから、初心者でも簡単にパイプラインを使いこなせるかもだね。これ、試してみたいと思わない？



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.HC, cs.MA, **投稿日時:** 2024-12-19 09:36

- - -

### [LoLaFL: Low-Latency Federated Learning via Forward-only Propagation](http://arxiv.org/abs/2412.14668)

**LoLaFL: 順方向のみの伝播による低遅延連合学習**

Jierui Zhang, Jianhao Huang, Kaibin Huang

- 従来の連合学習はバックプロパゲーションにより低遅延の要求に応えにくい問題がある
- LoLaFLは最大符号化率を用いて白箱のニューラルネットワークを拡張し低遅延を実現
- 層ごとの伝送と集約を可能とし通信ラウンド数を大幅に減少させる
- 非線形集約手法により遅延を91%および98%削減しながら類似の精度を維持

将来のネットワークでさらに速く学習できるのはすごくワクワクするね！また、いろんな方法で遅延を減らすアプローチが面白いなと思った！

**Comment:** 14 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.NI, **投稿日時:** 2024-12-19 09:20

- - -

### [Summary of Point Transformer with Federated Learning for Predicting Breast Cancer HER2 Status from Hematoxylin and Eosin-Stained Whole Slide Images](http://arxiv.org/abs/2412.14545)

**連合学習を用いたHE染色全スライド画像からの乳癌HER2状態予測のためのポイントトランスフォーマーの概要**

Kamorudeen A. Amuda, Almustapha A. Wakili

- 連合学習でHE染色の全スライド画像からHER2状態を予測し、治療決定速度とコストを改善
- マルチサイトデータセットのラベル不均衡や特徴表現を解決するためにポイントトランスフォーマーを提案
- ダイナミックなラベル分布、補助的な分類器、最遠コサインサンプリングを組み合わせて使用
- 4サイト（2687WSI）での実験で最先端の性能を示し、2つの未見のサイト（229WSI）への一般化も強力

医療画像解析に連合学習を使うなんてすごい！未見データへの強い一般化性能があるなら、現場の負担も減りそうで期待大だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-12-19 05:51

- - -

### [FedMUP: Federated Learning driven Malicious User Prediction Model for Secure Data Distribution in Cloud Environments](http://arxiv.org/abs/2412.14495)

**FedMUP: クラウド環境における安全なデータ分配のための連合学習駆動型悪意ユーザ予測モデル**

Kishu Gupta, Deepika Saxena, Rishabh Gupta, Jatinder Kumar, Ashutosh Kumar Singh

- クラウド環境のデータセキュリティ問題の解決を目的とする連合学習モデルを提案
- ユーザの行動を分析し、複数のセキュリティリスクパラメータを取得する方法を採用
- 各地でローカルデータセット上で訓練を行い、平均化でグローバルモデルを更新
- 提案手法は悪意ユーザ予測精度で14%以上の性能向上を示す

既存の技術と比較して、予測精度がかなり上がるのがスゴイね！クラウド利用者にとっては安心できる未来が見えてきた感じ。悪意ユーザーを独自に予測するところが興味深いなぁ。

**Comment:** 33 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-19 03:39

- - -

### [Drive-1-to-3: Enriching Diffusion Priors for Novel View Synthesis of Real Vehicles](http://arxiv.org/abs/2412.14494)

**Drive-1-to-3: 現実の車両の新しいビュー合成のための拡散事前分布の強化**

Chuang Lin, Bingbing Zhuang, Shanlin Sun, Ziyu Jiang, Jianfei Cai, Manmohan Chandraker

- 合成3Dデータは実世界の画像には性能が低下する問題がある
- 既存モデルを自動運転向けに調整し車両データを収集する
- 実走行のデータとの対比でビュー調整や焦点距離を一貫させる
- 潜在空間での訓練と対称的事前分布利用により精度向上を実現

この研究、車の視点合成にめっちゃ役立ちそうだね！特に自動運転技術の発展にもつながりそうで、ドライブがもっと楽しく安全になりそうな予感がするよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-19 03:39

- - -

### [MegaPairs: Massive Data Synthesis For Universal Multimodal Retrieval](http://arxiv.org/abs/2412.14475)

**MegaPairs: 普遍的なマルチモーダル検索のための大規模データ合成**

Junjie Zhou, Zheng Liu, Ze Liu, Shitao Xiao, Yueze Wang, Bo Zhao, Chen Jason Zhang, Defu Lian, Yongping Xiong

- マルチモーダル検索の進展がデータ不足で制約されている
- MegaPairsは視覚言語モデルとオープンドメイン画像を利用したデータ合成手法
- マルチモーダル検索性能が従来の70倍のデータより優れている
- 新しいモデルはゼロショット性能やデータセット全体で最高の成果を達成

データ合成でここまで成果を出しているってすごい！これからもどんな面白いモデルが登場するのか楽しみだね。マルチモーダル検索が次世代の検索にどう貢献してくるのかが気になる！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, **投稿日時:** 2024-12-19 02:49

- - -

### [FedPIA -- Permuting and Integrating Adapters leveraging Wasserstein Barycenters for Finetuning Foundation Models in Multi-Modal Federated Learning](http://arxiv.org/abs/2412.14424)

**FedPIA -- ワッサースタインバリーセンターを活用したアダプタの順列と統合によるマルチモーダル連合学習での基盤モデルの微調整**

Pramit Saha, Divyanshu Mishra, Felix Wagner, Konstantinos Kamnitsas, J. Alison Noble

- 医療分野では、厳しいプライバシー規制により大規模データ収集が困難である
- 連合学習とパラメータ効率の良い微調整でプライバシーとリソース制限に対応できる
- FedPIAはアダプタのデータとタスクの多様性を取り込み、ワッサースタインバリーセンターで知識を融合
- 2000以上のクライアントレベル実験でFedPIAがPEFT-FLのベースラインを上回るパフォーマンスを示した

大規模なデータがなくても、うまく活用する方法があるなんて、すごくワクワクしてくるね！医療分野でこんな工夫ができるなら、他の分野でも応用できそうだなあ。

**Comment:** Accepted for publication in AAAI 2025 (Main Track)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-12-19 00:24

- - -

### [Fingerprinting Codes Meet Geometry: Improved Lower Bounds for Private Query Release and Adaptive Data Analysis](http://arxiv.org/abs/2412.14396)

**指紋コードと幾何学の出会い: プライベートクエリと適応的データ分析の改善された下限**

Xin Lyu, Kunal Talwar

- 指紋コードは差分プライバシーにおける下限証明の重要なツールである
- 提案手法により、クエリ集合の幾何学に基づいた下限証明が可能となる
- 差分プライバシーに基づく手法が最適であることを証明し、従来の下限を大幅に改善
- ランダムクエリのサンプル複雑性を特徴付け、新しい上限と下限を提供

指紋コードがこんなに使えるとは驚きだね！差分プライバシーの最適な手法が示されたことで、さらなる技術向上が期待できそう。どんな応用が広がるのかワクワクしちゃう！

**Comment:** Abstract slightly shortened to meet the arXiv requirement; 50 Pages   and 1 Figure

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, cs.LG, **投稿日時:** 2024-12-18 23:11

- - -

### [Nemesis: Noise-randomized Encryption with Modular Efficiency and Secure Integration in Machine Learning Systems](http://arxiv.org/abs/2412.14392)

**Nemesis: ノイズランダム化暗号によるモジュラー効率と機械学習システムへの安全な統合**

Dongfang Zhao

- プライバシーを保証する機械学習システムは、準同型暗号に依存している
- 準同型暗号は計算効率が低く、大規模な応用に不向き
- NemesisはRacheのキャッシング技術を拡張し、計算効率を改善
- 実験により、Nemesisは計算負荷を大幅に軽減できることを示す

難しい準同型暗号を効率化するなんてすごいじゃん！これでプライバシー考慮した技術の普及が、もっと進むといいね。みんなが安心して新技術を使えるようになったら最高だね！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-12-18 22:52

- - -

### [Covariances for Free: Exploiting Mean Distributions for Federated Learning with Pre-Trained Models](http://arxiv.org/abs/2412.14326)

**無料の共分散: 事前学習済みモデルを用いた連合学習における平均分布の活用**

Dipam Goswami, Simone Magistri, Kai Wang, Bartłomiej Twardowski, Andrew D. Bagdanov, Joost van de Weijer

- 事前学習モデルはデータ異質性を低減し連合学習の速度を向上させる
- 提案手法はクラスの共分散行列を推定し、統計量の通信コストを削減
- クラス平均のみを用いて線形分類器を初期化し、共分散を活用
- 提案手法は他の最先端手法に比べ通信コストは同じで性能が向上

この方法って、通信コストが少なくてパフォーマンス向上なんて、魔法みたいで面白いよね。クラスター間で共有せずに情報活用できるのは未来の技術って感じ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-12-18 20:40

- - -

### [FedSTaS: Client Stratification and Client Level Sampling for Efficient Federated Learning](http://arxiv.org/abs/2412.14226)

**FedSTaS: 効率的な連合学習のためのクライアント階層化とクライアントレベルサンプリング**

Jordan Slessor, Dezheng Kong, Xiaofen Tang, Zheng En Than, Linglong Kong

- 連合学習は複数の分散クライアントでグローバルモデルを共同訓練する手法
- 通信効率を改善するFL方法は存在するが、クライアント選定方法は不十分
- FedSTaSはクライアントを圧縮勾配に基づき階層化し、最適なサンプリングを行う
- 実験でFedSTSより高い精度を固定ラウンド数内で達成

「特にクライアントの層化ってめっちゃ新しい発想で面白そう！しかも、精度が上がるなんて実用性もバッチリだね！未来の連合学習技術に期待したいな〜！」

**Comment:** 6 pages, 3 figures, to be submitted to ICML

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.ML, 68T05 (Primary) 62H30, 62J05 (Secondary), **投稿日時:** 2024-12-18 16:31

- - -

### [Data sharing in the metaverse with key abuse resistance based on decentralized CP-ABE](http://arxiv.org/abs/2412.13770)

**分散型CP-ABEに基づくキー乱用耐性を備えたメタバースでのデータ共有**

Liang Zhang, Zhanrong Ou, Changhui Hu, Haibin Kan, Jiheng Zhang

- メタバースではデータ共有が普及し、ブロックチェーン技術が基盤として利用されている
- CP-ABEは機密性と細かいアクセス制御を提供するが、キー乱用と権限の説明責任が課題
- 非対話型ゼロ知識証明をCP-ABEキーに統合し、検証をスマートコントラクトで行う手法を提案
- 提案手法は公平なデータ共有を促進し、ゲームファイにおける実例にも活用される

提案手法、めっちゃおもしろいじゃん！ゼロ知識証明を使ってキー乱用を防ぐから、安全性もバッチリだね。メタバースのゲームで遊んで稼ぐ未来、早く来て欲しい！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-18 12:06

- - -

### [A Comprehensive Review on Traffic Datasets and Simulators for Autonomous Vehicles](http://arxiv.org/abs/2412.14207)

**自動運転車のための交通データセットとシミュレータに関する包括的レビュー**

Supriya Sarker, Brent Maples, Weizi Li

- 高品質なデータセットは信頼性のある自動運転アルゴリズムの開発に不可欠である
- アノテーションプロセスやツールを分析し、標準的なアノテーションパイプラインの重要性を示す
- 地理的・敵対的環境条件が自動運転システム性能に与える影響を分析
- シミュレータの現状と合成データ生成の重要性を議論し、自動運転データの課題と将来展望を示す

自動運転の進化を支える影の立役者って、やっぱりデータだよね！シミュレータの話もだけど、次世代の車がどう変わるのかワクワクしちゃうな～。



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-12-17 07:43
