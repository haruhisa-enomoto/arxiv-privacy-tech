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

更新: 2024-10-04T04:21:28.532303

- - -

### [FabricDiffusion: High-Fidelity Texture Transfer for 3D Garments Generation from In-The-Wild Clothing Images](http://arxiv.org/abs/2410.01801)

**FabricDiffusion: 野外服画像から3D衣服生成のための高品質テクスチャ転送**

Cheng Zhang, Yuanhao Wang, Francisco Vicente Carrasco, Chenglei Wu, Jinlong Yang, Thabo Beeler, Fernando De la Torre

- FabricDiffusionは1枚の服画像から3D衣服へのテクスチャ転送を実現する方法を提案
- 従来の2D-3Dマッピングや深度認識生成モデルの限界を克服し、細部再現を目指す
- ノイズ除去拡散モデルを用いて入力画像の歪みを補正し、繰り返し可能な素材を抽出
- 大規模な実験によって、多様なテクスチャや状態に対して高い汎用性能を示す

この技術はファッション業界での3D衣服デザインの未来を変えちゃうかも！既存のツールとの親和性も高く、よりリアルで自由なデザインが実現できる世界が楽しみだなぁ。興味津々でワクワクしちゃうね！

**Comment:** Accepted to SIGGRAPH Asia 2024. Project page:   https://humansensinglab.github.io/fabric-diffusion

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.GR, **投稿日時:** 2024-10-02 17:57

- - -

### [KeyVisor -- A Lightweight ISA Extension for Protected Key Handles with CPU-enforced Usage Policies](http://arxiv.org/abs/2410.01777)

**KeyVisor -- CPUによる使用ポリシーが強制された保護キーを提供する軽量ISA拡張**

Fabian Schwarz, Jan Philipp Thoma, Christian Rossow, Tim Güneysu

- 暗号鍵の機密性は、コミュニケーションやファイル暗号化、アウトソースコンピュテーションのセキュリティに不可欠
- KeyVisorは、CPUが暗号鍵の取り扱いを安全に管理する軽量なISA拡張機能を提案
- KeyVisorは、CPU統合により高速な暗号操作とハードウェアで強制される鍵の使用制限を実現
- 実世界の使用例として、キー-バリュー・データベースや自動車の機能ライセンス、読み取り専用のネットワークミドルボックスを示す

本当に暗号鍵を漏らさない環境が整っていて、そういうことに興味がある企業にぴったりかもね！新しい技術のISA拡張は色々な用途に対応できそうで、これから使われていくのかも、ワクワクするね！

**Comment:** preprint

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.AR, **投稿日時:** 2024-10-02 17:31

- - -

### [Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective](http://arxiv.org/abs/2410.01720)

**LLMポストトレーニングにおける合成データの理論的理解に向けて：リバースボトルネックの観点から**

Zeyu Gan, Yong Liu

- 合成データはLLMのポストトレーニングで重要な資源だが、理論的理解が不足している
- 合成データ生成プロセスを詳細にモデル化し、新たなリバースボトルネックの視点から情報利得を分析
- GGMI（Mutual Informationを通じた一般化利得）の概念を導入し、一般化利得と情報利得の関係を解明
- 理論的基盤を提供し、合成データ生成技術の設計とポストトレーニングプロセスの最適化を支援

合成データ生成の効果を新たな視点から調査するなんて、面白そうじゃない？これでLLMの性能がもっと上がったら、未来のAIがどう変わるか楽しみだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, cs.LG, **投稿日時:** 2024-10-02 16:32

- - -

### [A Novel Framework of Horizontal-Vertical Hybrid Federated Learning for EdgeIoT](http://arxiv.org/abs/2410.01644)

**エッジIoTのための水平・垂直ハイブリッド連合学習の新しい枠組み**

Kai Li, Yilei Liang, Xin Yuan, Wei Ni, Jon Crowcroft, Chau Yuen, Ozgur B. Akan

- 新しいHoVeFLフレームワークがモバイルエッジIoT用に提案されている
- デバイスごとに同じデータ特徴を分析するもサンプルは異なる
- HoVeFLはローカルおよびグローバルモデルの訓練で全体の損失を最小化
- データセット評価でホリゾンタルデバイスが多い場合に性能向上

エッジIoTでのデバイス協調って面白そう！新しい視点で連合学習を進化させてる感じがするね。たくさんのデバイスが一緒に学ぶ未来が楽しみだな～。

**Comment:** 5 pages, 3 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, eess.SP, **投稿日時:** 2024-10-02 15:13

- - -

### [DAViD: Domain Adaptive Visually-Rich Document Understanding with Synthetic Insights](http://arxiv.org/abs/2410.01609)

**DAViD: 合成インサイトを用いたドメイン適応型視覚的にリッチな文書理解**

Yihao Ding, Soyeon Caren Han, Zechuan Li, Hyunsuk Chung

- 視覚的にリッチな文書(VRD)から情報を抽出するのは労力がかかる
- 既存のVRD理解モデルは大規模な注釈データセットに依存し、スケールが難しい
- DAViDフレームワークは合成データを利用し、コストを抑えてドメイン適応を実現
- 実験によりDAViDの効果が確認され、最小限の注釈データセットで競争力を持ったパフォーマンスを示す

合成データを活用してドメイン適応を図るの、とっても頭いいんじゃない？注釈データセットの作成って大変そうなのに、上手く合成で補ってるのが興味深いなって思った！私もこの技術で何か面白い応用を考えられるかもってワクワクしちゃった！

**Comment:** Work in progress

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-02 14:47

- - -

### [OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data](http://arxiv.org/abs/2410.01560)

**OpenMathInstruct-2: 大規模なオープンソースのインストラクションデータによるAIの数学推進**

Shubham Toshniwal, Wei Du, Ivan Moshkov, Branislav Kisacanin, Alexan Ayrapetyan, Igor Gitman

- 数学的推論は言語モデル開発の課題だが、データ不足で閉鎖的な進展が多い
- データ合成の実験で、過度に詳しい解はパフォーマンスを下げると判明
- 強い教師モデルによるデータは弱い生徒モデルによるデータより優れている
- 質問の多様性がデータスケーリングの向上に重要であると示された

この研究、めっちゃ面白そう！オープンソースでみんなが使えるようにしているのがすごい親切だよね。高校の数学の授業も、こんなデータでAIが教えてくれる時代が来たらいいな！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-10-02 14:00

- - -

### [Personalized Federated Learning on Flowing Data Heterogeneity under Restricted Storage](http://arxiv.org/abs/2410.01502)

**制限されたストレージ下でデータの流動性を考慮した個別化連合学習**

Sixing Tan, Xianmin Liu

- データ異質性がFLでのクライアント要件を不一致にし、これに対応するための個別化FL（pFL）が注目されている
- 既存のpFLはデータ分布の変動を考慮せず、実際の異質データシナリオでの分布変動がモデル性能に影響を与える
- データが流れるようにクライアントを通過する状況に着目し、カテゴリ分離の考えに基づくデータ分布再構築とジェネレーターを設計
- 提案したpFedGRPフレームワークは、8つのベースライン手法と比較して優れた性能を示した

クライアントごとに流れるデータを考慮するって、FLに新しいアプローチだね。制限されたストレージ下でも効率的に学習できる工夫が詰まってて、どんどん実用的になりそう！🎵



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-10-02 12:53

- - -

### [SonicSim: A customizable simulation platform for speech processing in moving sound source scenarios](http://arxiv.org/abs/2410.01481)

**SonicSim: 移動音源シナリオでの音声処理のためのカスタマイズ可能なシミュレーションプラットフォーム**

Kai Li, Wendi Sang, Chang Zeng, Runxuan Yang, Guo Chen, Xiaolin Hu

- 移動する音源条件下での音声分離や強化モデルには、多様性のあるデータが必要。
- 現実のデータは十分でなく、合成データも現実味を欠くため、実用には両方が不十分。
- SonicSimは、シーンやマイク、音源レベルでカスタマイズ可能な合成データ生成ツール。
- SonicSimで作成したデータセットは現実世界のシナリオに効果的に一般化することができた。

SonicSimってすごく興味深い！音の世界をもっとリアルに再現するのって、なんだか未来っぽいよね。音楽や映画の制作がどう変わるか、楽しみ～！

**Comment:** Technical report

**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.AI, eess.AS, **投稿日時:** 2024-10-02 12:33

- - -

### [Selective Aggregation for Low-Rank Adaptation in Federated Learning](http://arxiv.org/abs/2410.01463)

**連合学習における低ランク適応のための選択的集約**

Pengxin Guo, Shuang Zeng, Yanran Wang, Huijie Fan, Feifei Wang, Liangqiong Qu

- 連合学習でLoRAを用いた場合、A行列が一般知識、B行列がクライアント固有の知識を学習する
- FedSA-LoRAを提案、A行列のみがサーバー側で集約される仕組みを採用
- LoRAの他の変種でのAとBの関係性も解析、FedSA-rsLoRAとFedSA-VeRAに拡張
- 自然言語理解と生成タスクでの実験により提案手法の有効性を実証

この研究って、連合学習にLoRAをどう取り入れていくのかの大きな指針を作る感じだよね！クライアント固有の情報を保持しつつ、全体の知識も共有できるなんて、スマートだなーって思った！次のLoRAのバリエーションも楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-02 12:14

- - -

### [On the Convergence of FedProx with Extrapolation and Inexact Prox](http://arxiv.org/abs/2410.01410)

**FedProxの収束性に関する研究: 外挿と不正確なProxについて**

Hanmin Li, Peter Richtárik

- FedProxにサーバー側の外挿を取り入れたFedExProxを提案
- 正確なプロクシマル演算は現実的に厳しいが、その仮定を除外した研究
- 不正確さは解の近傍への収束をもたらし、適切な制御で悪影響を軽減
- 局所的最適化により各クライアントの計算複雑性の分析

FedExProxって新しいアプローチなんだね！理論だけじゃなくて、実際にどうなのかも実験してるところがいい感じ～。早くデータと友達になれそうな気がする！

**Comment:** 36 pages, 6 figures

**トピック:** [連合学習](fl), **カテゴリ:** math.OC, cs.AI, 90C25, **投稿日時:** 2024-10-02 10:42

- - -

### [Overpredictive Signal Analytics in Federated Learning: Algorithms and Analysis](http://arxiv.org/abs/2410.01399)

**連合学習における過剰予測信号分析：アルゴリズムと分析**

Vijay Anavangot

- エッジ信号処理は連合学習における分散学習と推論を支援する
- IoTデバイスはデータセンターと協力し、グローバルな信号モデルを学習可能
- プライバシーと通信制約があるため、従来の生信号ではなく近似信号を使用
- 凸最適化を用いた効率的なアルゴリズムで、通信コストや誤差のトレードオフを解析

IoTデバイスが協力する未来の話って感じでワクワクするね！分散型信号分析がもっと進化すると、私たちの日常生活も便利になる予感！エネルギー消費のデータで実験してるのも、実用的でいいね～！



**トピック:** [連合学習](fl), **カテゴリ:** eess.SP, cs.LG, stat.ML, **投稿日時:** 2024-10-02 10:21

- - -

### [FLAME: Adaptive and Reactive Concept Drift Mitigation for Federated Learning Deployments](http://arxiv.org/abs/2410.01386)

**FLAME: 連合学習展開のための適応的かつ反応的な概念的変化軽減**

Ioannis Mavromatis, Stefano De Feo, Aftab Khan

- FLAMEは、IoT環境における概念ドリフトを検出し軽減する新たなソリューション
- 実世界のFLパイプラインを考慮しつつ、モデル性能と精度を維持しつつ帯域幅とプライバシーの制約にも対応
- 計算負荷と通信のオーバーヘッドを大幅に削減するためにさまざまな機能と拡張を導入
- 既存の軽量な軽減方法と比較して、大規模なIoT展開で高いF1スコアを維持し、リソース利用を削減する性能を発揮

FLAMEって名前がもうかっこいいし、実世界のIoT環境での役立ちそう！通信と計算の負荷を減らしつつプライバシーも守るなんて、これからの時代にぴったりな技術だよね〜。

**Comment:** Accepted for Publication at EMERGE Workshop - EWSN 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-02 09:55

- - -

### [Forte : Finding Outliers with Representation Typicality Estimation](http://arxiv.org/abs/2410.01322)

**Forte : 表現の典型性推定による外れ値検出**

Debargha Ganguly, Warren Morningstar, Andrew Yu, Vipin Chaudhary

- 生成モデルはフォトリアリスティックな合成データを生成できる進化を遂げた
- 特異値検出で生成モデルの尤度が最適でない可能性が指摘されている
- ピクセルではなく意味的な内容に焦点を当てる方が特異値検出に有効と仮定
- 自己教師付き学習者を用いた典型集合推定で、従来の手法を上回る性能を実現した

生成モデルって見た目そっくりのデータを作れるんだね。でも、それだけじゃ足りないってことみたい。やっぱり意味とか中身が重要らしいから、そこをうまく取り入れるのがポイントかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CV, cs.IT, math.IT, **投稿日時:** 2024-10-02 08:26

- - -

### [SurgeoNet: Realtime 3D Pose Estimation of Articulated Surgical Instruments from Stereo Images using a Synthetically-trained Network](http://arxiv.org/abs/2410.01293)

**SurgeoNet: 合成データで学習したネットワークを用いたステレオ画像からの外科用機器のリアルタイム3Dポーズ推定**

Ahmed Tawfik Aboukhadra, Nadia Robertini, Jameel Malik, Ahmed Elhayek, Gerd Reis, Didier Stricker

- Mixed Reality環境での手術モニタリングが注目され、特に手や外科用機器の追跡が重要
- サンプルデータが少なく、タスクの複雑さからこの問題に取り組んだ研究は少ない
- SurgeoNetを提案し、ステレオVRビューからの機器の検出と追跡を高精度で実現
- 合成データのみによる訓練で現実のシナリオにも対応可能、コードとデータは公開

こういうのって技術の進化を感じるよね！VRとかMRの環境で手術がもっと身近になる未来、すっごくワクワクする！頑張って勉強したら、面白い研究ができるかもよ～！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-02 07:40

- - -

### [ParallelSFL: A Novel Split Federated Learning Framework Tackling Heterogeneity Issues](http://arxiv.org/abs/2410.01256)

**ParallelSFL: 異種性問題に取り組む新しい分割連合学習フレームワーク**

Yunming Liao, Yang Xu, Hongli Xu, Zhiwei Yao, Liusheng Huang, Chunming Qiao

- スマホなどによるデータ収集は連合学習の重要な情報源である
- ParallelsFLはモデルを底部と頂部に分割し効率的に学習
- クラスタリング戦略でモデル精度と学習効率向上
- 実験で通信量21%削減、学習速度1.36倍、精度5%向上を実証

この方法ってさ、本当に色々な場面で活用できそうだよね！通信量を減らせるし、効率的で効果的な学習を実現できるっていうのがすっごく魅力的だと思うな！

**Comment:** arXiv admin note: text overlap with arXiv:2311.13348

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-10-02 06:03

- - -

### [Debiasing Federated Learning with Correlated Client Participation](http://arxiv.org/abs/2410.01209)

**相関クライアント参加による連合学習の偏り解消**

Zhenyu Sun, Ziyang Zhang, Zheng Xu, Gauri Joshi, Pranay Sharma, Ermin Wei

- 多くのモバイルクライアントがいる連合学習では、少数のクライアントのみが毎回参加する
- 既存のFedAvgの分析は独立サンプルを仮定するが、実際の状況と一致しない
- クライアント参加をマルコフ連鎖でモデル化し、最低参加間隔を考慮した理論を構築
- 提案手法は最小間隔が増加することで、バイアスを減少させることを理論的・実証的に示す

クライアント参加がどう影響するかをマルコフ連鎖で見るのが新しいね。そして、最低間隔を設けることでバイアスが減るなんて意外！将来の実用化が楽しみ～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-10-02 03:30

- - -

### [Unleashing the Power of Large Language Models in Zero-shot Relation Extraction via Self-Prompting](http://arxiv.org/abs/2410.01154)

**自己プロンプトを活用した大規模言語モデルによるゼロショット関係抽出の力を解き放つ**

Siyi Liu, Yang Li, Jiang Li, Shan Yang, Yunshi Lan

- ゼロショット関係抽出での大規模言語モデル使用は性能が限定的
- 問題は、詳細かつ文脈特化したプロンプト不足による
- 自己プロンプトフレームワークを提案し、3段階で多様性を持たせたプロンプト生成
- ベンチマークでの実験で、生成した合成データが性能向上に寄与することを確認

自己プロンプトでゼロショット関係抽出の精度がもっと上がるなんて、ちょっとワクワクしちゃうかも！さらに、高品質な合成データまで作っちゃうなんて凄いね。これからの応用や進化が楽しみ！

**Comment:** EMNLP 2024 Short

**トピック:** [合成データ](sd), **カテゴリ:** cs.IR, cs.CL, **投稿日時:** 2024-10-02 01:12

- - -

### [Synthetic imagery for fuzzy object detection: A comparative study](http://arxiv.org/abs/2410.01124)

**ファジー物体検出のための合成画像に関する比較研究**

Siavash H. Khajavi, Mehdi Moshtaghi, Dikai Yu, Zixuan Liu, Kary Främling, Jan Holmström

- ファジー物体検出は、視覚的特徴やぼやけた境界などで複雑さが増す
- 手動でのデータ収集と注釈付けが困難で、効率的な手法が求められている
- 3Dモデルを用いた合成画像生成と自動注釈を提案し、ファイヤー検出の精度を向上
- 合成データと実データを混合したモデルが、実データや合成データ単独のモデルを上回る性能を示す

ファジーな物体の識別ってめちゃくちゃ難しいのに、合成画像を使って解決できちゃうなんておもしろいね！これからのコンピュータビジョンの研究でまた新しい可能性がどんどん開けそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-01 23:22

- - -

### [Efficient and Private Marginal Reconstruction with Local Non-Negativity](http://arxiv.org/abs/2410.01091)

**効率的かつプライベートな周辺再構成技術と局所的非負性**

Brett Mullins, Miguel Fuentes, Yingtai Xiao, Daniel Kifer, Cameron Musco, Daniel Sheldon

- 差分プライバシーに基づく質問応答や合成データ生成では、クエリに対する回答の再構成が重要
- ReMという効率的な後処理方法を用い、周辺クエリの回答再構成を実現
- 媒介変数を用いて効率的な擬似逆を可能にする手法が導入され、再構成に寄与
- GReM-LNN拡張により、ガウスノイズ下で一貫性と非負性を満たしエラーを軽減

プライバシー技術とデータ処理の両立を目指してるのが面白いよね！どれだけエラー減らせるか実用的にも期待できそう。研究結果が早く現場で活かされるといいな🌟

**Comment:** To appear at NeurIPS 2024

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-01 21:39

- - -

### [Convergent Privacy Loss of Noisy-SGD without Convexity and Smoothness](http://arxiv.org/abs/2410.01068)

**非凸・非スムーズな損失に対するノイジーSGDのプライバシー損失の収束**

Eli Chien, Pan Li

- ノイジーSGDでの通常のプライバシー分析は、内部状態の公開を仮定している
- 非凸・非スムーズな損失に対しても収束する差分プライバシーを証明
- H\"older連続な勾配があれば十分であり、滑らかな強凸損失よりも良いプライバシー限界を提供
- 改良されたシフトダイバージェンス分析を利用し、多方面からアプローチした

プライバシー保証が非凸で非スムーズな状況でも適用できるなんてすごいよね！もっと色んな機械学習の場面で差分プライバシーが活躍できそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-01 20:52

- - -

### [Towards Fairness and Privacy: A Novel Data Pre-processing Optimization Framework for Non-binary Protected Attributes](http://arxiv.org/abs/2410.00836)

**公平性とプライバシーに向けて: 非二値保護属性のための新しいデータ前処理最適化フレームワーク**

Manh Khoi Duong, Stefan Conrad

- AIの不公平な結果の原因は、バイアスのあるデータセットに根ざしていることが多い
- 提案されたフレームワークは、保護属性のあるデータセットをデバイアス化して公平性を向上
- 遺伝的アルゴリズムを用いた組合せ最適化問題で、特定の差別測定を最小化するデータ部分集合を見つける
- フレームワークは柔軟で、メトリックやタスクに依存せず、効率的な実行時間を示す

バイアスのないAIを目指すってすごく重要だよね！データの公平性を向上させるアプローチが新しい技術によって実現できるのって、これからのAI開発にいい影響を与えそうだって思う！

**Comment:** The Version of Record of this contribution is published in Data   Science and Machine Learning, volume 1943, CCIS (Springer Singapore) 2023. It   is available online at https://doi.org/10.1007/978-981-99-8696-5

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CY, **投稿日時:** 2024-10-01 16:17

- - -

### [Geometric shape matching for recovering protein conformations from single-particle Cryo-EM data](http://arxiv.org/abs/2410.00833)

**単一粒子クライオ電子顕微鏡データからのタンパク質コンフォメーション回復のための幾何学的形状マッチング**

Erik Jansson, Jonathan Krook, Klas Modin, Ozan Öktem

- 単一粒子クライオ電子顕微鏡データからタンパク質の3次元バックボーン構造を回復する課題
- ノイジーなトモグラフィ投影から、形状解析を用いて3次元構造を再構築
- タンパク質バックボーンの点群表現を2Dトモグラフィデータに一致させる間接的マッチング問題として解釈
- 行列Lie群の作用を用いて変形を行い、最適性条件に基づく計算アルゴリズムを提案

タンパク質の構造を形状解析の技術で復元するのってすごいよね！全く新しい視点でのアプローチで、今後の研究の方向性にも影響を与えそう！合成データでも成果が出ているから、実際のデータにも応用できたら面白そう！

**Comment:** 41 pages, 10 figres

**トピック:** [合成データ](sd), **カテゴリ:** q-bio.BM, cs.NA, math.DG, math.NA, math.OC, 53Z50, 90C26, 68U10, 53Z10, 92C55, **投稿日時:** 2024-10-01 16:14

- - -

### [Targeted synthetic data generation for tabular data via hardness characterization](http://arxiv.org/abs/2410.00759)

**ターゲットとなるタブデータのための難易度特性に基づく合成データ生成**

Tommaso Ferracci, Leonie Tabea Goldmann, Anton Hinel, Francesco Sanna Passino

- 合成データ生成は、データが不足または低品質の場合にモデルの性能と堅牢性を向上させる。
- データ評価フレームワークを使用し、役に立つ観測値を特定し、高値の訓練ポイントを生成する新しい拡張パイプラインを導入。
- Shapleyベースのデータ評価方法は、学習ベースの方法と同等の性能を発揮し、理論的および計算的な利点がある。
- 難易度の高いポイントで訓練された合成データ生成器は、非ターゲットのデータ拡張よりも優れており、計算効率が高い。

この研究って、データが少ないとか低品質でも合成データだけで良い予測ができるってことだよね。合成データの生成に特化してるから、より効率的にモデルを強化できるのかも。興味深いね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-10-01 14:54

- - -

### [Thinking Outside of the Differential Privacy Box: A Case Study in Text Privatization with Language Model Prompting](http://arxiv.org/abs/2410.00751)

**差分プライバシーにとどまらない発想：言語モデルによるテキストプライバタイズのケーススタディ**

Stephen Meisenbacher, Florian Matthes

- 大規模言語モデルの普及に伴い、プライバシー保護を施した自然言語処理が注目されている
- 差分プライバシー(DP)はNLPへの統合で支持されるが、制約と課題がある
- DP-Promptは、言語モデルを用いてテキストを再構築する新しいプライバタイズ手法
- 実験結果は、DPと非DPアプローチの利点と課題についてさらなる議論の必要性を示している

DP-Promptが、言語モデルを活用してどうやってテキストのプライバシーを守るのか気になる！実際の利用シーンにおいて、どれだけ便利に使えるのか、もっと深掘りしてみたいな。

**Comment:** 10 pages, 3 tables, Accepted to EMNLP 2024 (Main)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-01 14:46

- - -

### [Improved Generation of Synthetic Imaging Data Using Feature-Aligned Diffusion](http://arxiv.org/abs/2410.00731)

**特徴整合型拡散による合成イメージングデータ生成の改善**

Lakshmi Nair

- 合成データ生成は医療画像分野で重要な機械学習応用である
- 特徴整合型拡散を用いて従来の生成パイプラインを改善
- 拡散モデルの中間特徴を専門家の出力特徴に整合させた
- 生成精度が9%向上し、SSIM多様性が約0.12改善

医療画像の生成で、より正確な合成データを作るためのアプローチだね！特徴整合型拡散の技術が既存の方法とも一緒に使えるなんて、汎用性も抜群でワクワクするね。勉強してみたくなっちゃう！

**Comment:** Accepted to First International Workshop on Vision-Language Models   for Biomedical Applications (VLM4Bio 2024) at the 32nd ACM-Multimedia   conference

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-10-01 14:18

- - -

### [AR-Sieve Bootstrap for the Random Forest and a simulation-based comparison with rangerts time series prediction](http://arxiv.org/abs/2410.00942)

**ランダムフォレストにおけるAR-Sieveブートストラップとrangertsと時間系列予測のシミュレーションベース比較**

Cabrel Teguemne Fokam, Carsten Jentsch, Michel Lang, Markus Pauly

- ランダムフォレストは時間系列予測に適用可能だが、従来のブートストラップ手法はデータ生成過程に完全には対応していない
- IIDブートストラップをAR-Sieveブートストラップ（ARSB）に置き換え、残差ブートストラップ技術とRFを組み合わせることを提案
- シミュレーションスタディで、様々なデータ生成過程から合成データを用いて新モデルの予測性能を評価
- ARSBは木の多様性を増し、RFの他のブートストラップ戦略と比較して精度が向上するが、効率コストもある

この研究ちょっと面白そう！AR-Sieveブートストラップだと予測の精度がアップするなんて革新かも！効率のコストがちょっと気になるけど、どんな応用に使われるのか楽しみだよね。📚🌟



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-10-01 14:07

- - -

### [Integrating PETs into Software Applications: A Game-Based Learning Approach](http://arxiv.org/abs/2410.00661)

**プライバシー技術をソフトウェアアプリケーションに統合する: ゲームベースの学習アプローチ**

Maisha Boteju, Thilina Ranbaduge, Dinusha Vatsalan, Nalin Arachchilage

- ソフトウェアアプリにデータ保護がないと情報漏洩が発生し、個人情報保護が脅かされる
- プライバシーを強化する技術（PETs）はデータ漏洩を防ぎつつ有用な洞察を引き出す
- 開発者はPETsを統合する知識や意識が不足しており、学習アプローチが不十分
- "PETs-101"という学習フレームワークを提案し、開発者がプライバシーを考慮した行動を取ることを目指す

ゲームで学ぶって楽しそう！デベロッパーがもっとプライバシーに敏感になってくれたら、私たちの情報ももっと安心だよね。これからどう成長するのか楽しみ！

**Comment:** 10

**トピック:** [PETs](pets), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-01 13:15

- - -

### [Cafca: High-quality Novel View Synthesis of Expressive Faces from Casual Few-shot Captures](http://arxiv.org/abs/2410.00630)

**カフカ：カジュアルな少数ショット撮影から表情豊かな顔の新しいビューを高品質で合成**

Marcel C. Bühler, Gengyan Li, Erroll Wood, Leonhard Helminger, Xu Chen, Tanmay Shah, Daoye Wang, Stephan Garbin, Sergio Orts-Escolano, Otmar Hilliges, Dmitry Lagun, Jérémy Riviere, Paulo Gotardo, Thabo Beeler, Abhimitra Meka, Kripasindhu Sarkar

- 従来の3D顔キャプチャー手法は多数のビュー入力が必要で、少数入力には不適用
- 少数の視点からの高精度な顔モデリングを実現する新しいボリュメトリック事前知識を提案
- 合成データで訓練された事前知識が現実世界のアイデンティティや表情に一般化
- 3Dモーフィング顔モデルを用いて大規模なトレーニングセットを合成し、微調整でリアルな再構築を実現

この研究ってめっちゃ面白いよね！少ない写真だけで動きのある顔を3Dで再現できるなんて、未来の顔キャプチャーがもっと楽しくなりそうだね！映画やアニメの制作なんかも、もっとリアルになりそうでワクワクする〜！

**Comment:** Siggraph Asia Conference Papers 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-10-01 12:24

- - -

### [Differentially Private Active Learning: Balancing Effective Data Selection and Privacy](http://arxiv.org/abs/2410.00542)

**差分プライバシーを活用したアクティブラーニング: 効果的なデータ選択とプライバシーのバランス**

Kristian Schwethelm, Johannes Kaiser, Jonas Kuntzer, Mehmet Yigitsoy, Daniel Rueckert, Georgios Kaissis

- アクティブラーニングと差分プライバシーの組み合わせの課題を探求
- 差分プライバシーSGDを統合する際の予算配分とデータ利用困難を発見
- データ利用を最適化するステップ増幅法を提案し効果を実証
- プライバシー制約下で使用する取得関数の限界を明らかに

プライバシーを守りながらしっかりとデータを活かす方法が見つかるといいね！アクティブラーニングって言葉だけ聞くとすごく積極的なイメージだけど、プライバシーとのバランスって難しいんだね。でも、新しい提案が明日をもっと明るくしてくれるかも！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-01 09:34

- - -

### [Pre-training with Synthetic Patterns for Audio](http://arxiv.org/abs/2410.00511)

**合成パターンを用いたオーディオの事前学習**

Yuchi Ishikawa, Tatsuya Komatsu, Yoshimitsu Aoki

- 合成パターンを用いたオーディオエンコーダの事前学習を提案
- マスク付きオートエンコーダ(MAE)でデータの再構築を自己教師あり学習
- 合成データを用いることでプライバシーやライセンスの問題を回避
- 13のオーディオタスクと17の合成データセットで性能を検証し、AudioSet-2Mと同等の成果を示す

なんかこの研究めっちゃ画期的じゃない？合成データでプライバシー問題を回避しつつ、リアルデータと同じくらいの精度を出せるなんて、これから音声認識の分野がもっと進化しそう！どんな合成パターンが効果的なのかも気になる〜。

**Comment:** Submitted to ICASSP'25

**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.AI, cs.CV, **投稿日時:** 2024-10-01 08:52

- - -

### [PrivTuner with Homomorphic Encryption and LoRA: A P3EFT Scheme for Privacy-Preserving Parameter-Efficient Fine-Tuning of AI Foundation Models](http://arxiv.org/abs/2410.00433)

**プライバシーを保護するAI基盤モデルの効率的微調整手法: 準同型暗号化とLoRAを用いたPrivTuner**

Yang Li, Wenhan Yu, Jun Zhao

- AI基盤モデルの微調整にはパラメーター効率とプライバシー保護を両立する手法が必要
- PrivTunerは準同型暗号化を利用し、LoRAでモデルのパラメーターを効率良く設定
- 無線通信環境でのプライバシーとエネルギー最適化問題を解決するアルゴリズムを開発
- 実験により、様々なプライバシー要求に応じたエネルギー消費削減が可能であると示した

この研究って、プライバシーをちゃんと守りつつAIモデルを調整する方法にすっごくこだわってる感じがして面白そう！準同型暗号とか難しそうだけど、将来の技術が見えてくるとワクワクするね！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-01 06:30

- - -

### [FedPT: Federated Proxy-Tuning of Large Language Models on Resource-Constrained Edge Devices](http://arxiv.org/abs/2410.00362)

**FedPT: 資源制約のあるエッジデバイスでの大規模言語モデルの連合プロキシ調整**

Zhidong Gao, Yu Zhang, Zhenxiao Zhang, Yanmin Gong, Yuanxiong Guo

- 大規模言語モデルの微調整はデータ収集が必要でプライバシー問題が発生する
- 連合学習でデータを共有せずに共同モデル訓練が可能になる
- FedPTは出力予測のみを利用し大規模言語モデルをプロキシ調整する新手法を提案
- FedPTは計算や通信の負担を大幅に削減しながら競合性能を実現する

FedPTってすごく新しいアプローチじゃない？資源が限られているデバイスでも大規模モデルを使えるってめっちゃ便利だよね！プライバシーも守りながら効率的っていうのが最高だと思うな。

**Comment:** 29 pages, 19 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-10-01 03:20

- - -

### [DoPAMine: Domain-specific Pre-training Adaptation from seed-guided data Mining](http://arxiv.org/abs/2410.00260)

**DoPAMine: 種指導データマイニングによるドメイン特化事前学習適応**

Vinayak Arannil, Sourav Sanjukta Bhabesh, Neha Narwal, Sai Nikhil Thirandas, Darren Yow-Bang Wang, Graham Horwood, Alex Anto Chirayath, Gouri Pandeshwar

- LLMは多くの業界ドメインで一般化する能力を持つが、専門またはリソースの乏しいドメインでは限界がある
- ドメイン特化した合成データ生成はあるが、真実性と複雑さに欠けることが多い
- DoPAMineは大規模データの中からドメイン特化の訓練データを自動的に抽出する手法を提案
- ヘルスケアと金融のタスクでLLMの性能を向上し、ゼロショットおよび5ショット設定での成果を示す

ドメイン特化の訓練データを効率よく作成するDoPAMineってすごく便利そう！これで業界ごとの精度が上がったら、いろんな分野で活躍しそうだね。特に医療とか金融ではとっても役立ちそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-09-30 22:15

- - -

### [Quantized and Asynchronous Federated Learning](http://arxiv.org/abs/2410.00242)

**量子化および非同期型連合学習**

Tomas Ortega, Hamid Jafarkhani

- 非同期型連合学習は同期型に比べて速く拡張性が高いが、量子化を考慮していない。
- 通信ボトルネックを解消するための量子化非同期型連合学習(QAFeL)を提案。
- QAFeLは隠れ状態量子化とバッファーを用いて、スケーラビリティとセキュアな集約を実現。
- 階乗誤差の影響は高次誤差項に限定され、非凸目的の勾配降下法で最適な収束率を達成。

未来の学び方が変わりそう！非同期と量子化の最強コンボで楽しくて自由な学びが可能になるかもね！QAFeLって難しそうだけど、学びの場をもっと広げてくれそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, eess.SP, math.OC, 68W10, 68W15, 68W40, 90C06, 90C35, 90C26, G.1.6; F.2.1; E.4, **投稿日時:** 2024-09-30 21:22

- - -

### [Fisher Information-based Efficient Curriculum Federated Learning with Large Language Models](http://arxiv.org/abs/2410.00131)

**大規模言語モデルを用いたフィッシャー情報に基づく効率的カリキュラム連合学習**

Ji Liu, Jiaxiang Ren, Ruoming Jin, Zijie Zhang, Yang Zhou, Patrick Valduriez, Dejing Dou

- 連合学習は分散データでモデルを共同訓練する有望な手法である
- LLMは巨大で非IIDデータに対する訓練コストが高くなる
- 提案手法FibecFedは適応的データサンプリングと効率的なスパースパラメータ更新を行う
- 実験結果で最大45.35%の精度と98.61%の高速化を実現

フィッシャー情報を使うあたりが素敵！効率的なパラメータ更新で連合学習がもっと普及するのかもってワクワクするね。データサンプリングを工夫することで、精度と速度がこれだけ改善されるのは面白いな～。

**Comment:** 27 pages, 8 figures, 14 tables, to appear in EMNLP 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CL, cs.DC, **投稿日時:** 2024-09-30 18:12

- - -

### [Survey of Security and Data Attacks on Machine Unlearning In Financial and E-Commerce](http://arxiv.org/abs/2410.00055)

**金融および電子商取引における機械学習虚勢に対するセキュリティおよびデータ攻撃の調査**

Carl E. J. Brodzinski

- 機械学習虚勢に対する主要なプライバシー脅威として、メンバーシップ推論攻撃やデータ再構成攻撃を紹介
- 機械学習虚勢データ中毒、虚勢要求攻撃、虚勢ジェイルブレイク攻撃などのセキュリティ攻撃を分析
- 差分プライバシーや暗号的保証、ゼロ知識証明による防御戦略を紹介、検証可能で改ざん防止のメカニズム提供
- 金融や電子商取引でのデータ整合性とプライバシー保護のため、進化する攻撃ベクトルに対抗する防御が重要

機械学習の虚勢技術をめぐるセキュリティの世界ってすっごく面白そう！金融とかの大事なデータを守るために、新しい技術や考え方をもっとたくさん勉強してみたいって思ったよ。どんな攻撃が来ても負けないように、ますます安全な仕組みを作れたら最高だよね！



**トピック:** [差分プライバシー](dp), [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-09-29 00:30
