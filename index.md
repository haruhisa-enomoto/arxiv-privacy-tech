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

更新: 2024-10-21T04:23:04.541050

- - -

### [How Does Data Diversity Shape the Weight Landscape of Neural Networks?](http://arxiv.org/abs/2410.14602)

**データ多様性がニューラルネットワークの重みの風景にどのように影響するか**

Yang Ba, Michelle V. Mancenido, Rong Pan

- 過学習を防ぎつつ精度向上のためにデータ拡張と正則化法を活用する
- 多様なデータは、ドロップアウトと同様に重みの風景を変化させる
- 生成モデルによる合成データは実データの多様性を増し性能向上をもたらす
- 無分布テストにおいて合成データが特に優れた効果を示すことを実証

データ多様性の重要性が改めて分かった！合成データの力で新たな発見が生まれそう！どんな場面でも使える技術になりそうでワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-18 16:57

- - -

### [Neuro-Symbolic Traders: Assessing the Wisdom of AI Crowds in Markets](http://arxiv.org/abs/2410.14587)

**神経シンボリックトレーダー: 市場におけるAIクラウドの知恵の評価**

Namid R. Stillman, Rory Baggott

- ディープジェネレーティブモデルは金融分析に利用され始めているが、市場への影響は不明
- 仮想市場で売買判断する「神経シンボリックトレーダー」を開発し、その市場ダイナミクスを探る
- モデルは視覚言語を利用し、資産の基本価値を確立するための確率微分方程式を構築
- トレーダーは仮想市場環境で実験され、価格抑制など市場安定性へのリスクを浮き彫りに

AIが金融市場にどう影響するかって、すごく気になるテーマだよね。この研究って、未来の市場を予測する手がかりになるかもしれないし、そのリスクもちゃんと考慮してておもしろそう！

**Comment:** 8 pages, 4 figures, ACM format

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, q-fin.CP, **投稿日時:** 2024-10-18 16:37

- - -

### [RAG-ConfusionQA: A Benchmark for Evaluating LLMs on Confusing Questions](http://arxiv.org/abs/2410.14567)

**RAG-ConfusionQA: 混乱する質問に対するLLMの評価ベンチマーク**

Zhiyuan Peng, Jinming Nian, Alexandre Evfimievski, Yi Fang

- 対話型AIエージェントはRAGを用いて文書に基づく回答を生成
- 多くの自然な質問は回答が困難、25%が誤った前提を持ち、50%以上が曖昧
- 高品質データが必要で、新たに文書から多様な混乱質問を生成する方法を提案
- 複数のLLMをRAGエージェントとして評価し、精度を測定、ベンチマークデータセットを公開

これって面白いね！多くの質問が答えにくいっていう事実にかかわらず、AIがどううまく対処できるかを見るのはすごく画期的だと思う。これからのAIの成長がさらに楽しみだね！

**Comment:** under review

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.IR, **投稿日時:** 2024-10-18 16:11

- - -

### [Personalizing Low-Rank Bayesian Neural Networks Via Federated Learning](http://arxiv.org/abs/2410.14390)

**連合学習による低ランクベイズニューラルネットワークの個別化**

Boning Zhang, Dongzhu Liu, Osvaldo Simeone, Guanchu Wang, Dimitrios Pezaros, Guangxu Zhu

- モデルが現実世界での意思決定に不可欠であり、予測に信頼性のある信頼度を持たせる必要がある
- 個別化連合学習では不確実性の定量化が重要だが、ローカルデータが少なく最適なモデルパラメータを決定しにくい
- 提案手法LR-BPFLは、グローバルな決定論的モデルと低ランクなベイズ補正を学習し、クライアントごとの不確実性に適応
- LR-BPFLは様々なデータセットで評価され、キャリブレーションや精度、計算とメモリの要件で利点を示す

この論文は、パーソナライズされたモデルをよりスマートに作る方法を提案しているね！クライアントごとに適応するから、多様なデータに対応できてなんかワクワクするよね。いつか私たちも使って自分専用のモデルを作ってみたいな～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-18 11:50

- - -

### [Investigating the Capabilities of Deep Learning for Processing and Interpreting One-Shot Multi-offset GPR Data: A Numerical Case Study for Lunar and Martian Environments](http://arxiv.org/abs/2410.14386)

**ディープラーニングによるワンショット・マルチオフセットGPRデータ解析の可能性：月・火星環境を対象とした数値ケーススタディ**

Iraklis Giannakis, Craig Warren, Antonios Giannopoulos, Georgios Leontidis, Yan Su, Feng Zhou, Javier Martin-Torres, Nectaria Diamanti

- 地中レーダー（GPR）は月や火星の地質データ取得で利用され、特有の課題を抱える。
- 従来の処理手法は手動調整が必要で曖昧な結果を生むが、自動処理が求められている。
- ディープラーニングを用いた研究で惑星表層の誘電体分布再構築とデータ補填を検討。
- 合成データは現実的かつ挑戦的に設定され、今後の研究促進を目指し公開された。

ディープラーニングで惑星データを解析ってなんだか未来っぽい！GPRデータの質を向上させて、未知の地底世界ももっと詳しく探索できるようになるかもね。楽しみだな～！



**トピック:** [合成データ](sd), **カテゴリ:** physics.geo-ph, astro-ph.EP, astro-ph.IM, cs.LG, **投稿日時:** 2024-10-18 11:38

- - -

### [Synthesizing Post-Training Data for LLMs through Multi-Agent Simulation](http://arxiv.org/abs/2410.14251)

**連合学習を通じてLLMのための後処理データを合成するための多エージェントシミュレーション**

Shuo Tang, Xianghe Pang, Zexi Liu, Bohan Tang, Rui Ye, Xiaowen Dong, Yanfeng Wang, Siheng Chen

- 大規模言語モデル（LLMs）の後処理には、人間の指示に従えるようにすることが不可欠
- LLMsで人間社会をシミュレートし、多エージェントシミュレーションで多様なテキストシナリオを生成
- MATRIXというシミュレーターを提案、現実的かつスケーラブルなシナリオを作成可能
- 少ないデータでMetaのモデルを超える性能を示し、MATRIX-Genが生成データの品質を向上

MATRIXって面白そうじゃない？少ないデータで大きな成果を上げているのがすごいよね。しかも、現実に近いシナリオを生成できるのか、どんな活用ができるのかなってワクワクする～！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, **投稿日時:** 2024-10-18 08:01

- - -

### [Comparative Evaluation of Clustered Federated Learning Method](http://arxiv.org/abs/2410.14212)

**クラスタ化連合学習法の比較評価**

Michael Ben Ali, Omar El-Rifai, Imen Megdiche, André Peninou, Olivier Teste

- 連合学習は分散学習の一手法であり、データプライバシーを保護する
- 非IIDデータ分布がFLプロトコルの参加者間で生じるのが課題
- クラスター化連合学習（CFL）は参加者を均質な分布に分ける手法
- 提案するデータ異質性の分類に基づき、2つのCFLアルゴリズムの性能を評価

クラスター化連合学習って、学習グループを使い分ける工夫で効率が上がるみたい！データがバラバラでもやり方次第でいい結果を出せるんだね。将来もっと使いやすくなると良いなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-10-18 07:01

- - -

### [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](http://arxiv.org/abs/2410.14208)

**Montessori-Instruct: 学習者に合わせた影響力のある訓練データ生成**

Xiaochuan Li, Zichun Yu, Chenyan Xiong

- 合成データは学習モデル訓練に使われるが、ノイズや誤解を招く信号も含む。
- Montessori-Instructは、学習プロセスに合わせたデータ合成フレームワークを提案。
- ローカルデータの影響を用い学習者の嗜好を測定し、DPOでモデルを最適化。
- 既存手法よりも大幅に性能が向上し、強力なモデルの合成データにも勝る。

この論文、すごく面白そう！AIがどんどん賢くなってく感じ。教育の未来にも応用できそうだし、可能性は無限大だね！

**Comment:** Codes and data are open-sourced at   https://github.com/cxcscmu/Montessori-Instruct

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-10-18 06:50

- - -

### [FedMSE: Federated learning for IoT network intrusion detection](http://arxiv.org/abs/2410.14121)

**FedMSE: IoTネットワーク侵入検知のための連合学習**

Van Tuan Nguyen, Razvan Beuran

- IoTの拡大でサイバー攻撃のリスク増加、従来の集中型学習ではプライバシーが課題
- 半教師あり連合学習により、異常検知を強化するSAE-CENモデルを提案
- MSEAvgアルゴリズムで、正確なローカルモデルを重視しグローバル性能を向上
- 実験では、異なるIoTネットワークでの検出精度と学習コストを改善し、堅牢性を示す

連合学習を使ってIoTの侵入検知を効率化するって、すごく未来的だよね！半教師ありってことはちょっとギリギリ知らないデータでもいけちゃうのかな？ワクワクするね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-18 02:23

- - -

### [A Communication and Computation Efficient Fully First-order Method for Decentralized Bilevel Optimization](http://arxiv.org/abs/2410.14115)

**通信と計算が効率的な分散双レベル最適化のための完全一階手法**

Min Wen, Chengchang Liu, Ahmed Abdelmoniem, Yipeng Zhou, Yuedong Xu

- 双レベル最適化は分散学習であまり探求されていない
- 従来の手法は計算と通信の負荷が高い二階情報を利用
- この研究は一階情報のみを使用し効率的な方法を提案
- 提案手法は様々なデータ分布で優れた性能を実証

この論文、分散環境でも双レベル最適化を一階情報で進めるなんてすごいね！特に通信の効率化が注目ポイントだし、どんな場面で応用されるのか気になるよ。

**Comment:** 19 Pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, math.OC, **投稿日時:** 2024-10-18 02:00

- - -

### [FedPAE: Peer-Adaptive Ensemble Learning for Asynchronous and Model-Heterogeneous Federated Learning](http://arxiv.org/abs/2410.14075)

**FedPAE: 非同期かつモデルが異なる連合学習のためのピア適応型アンサンブル学習**

Brianna Mueller, W. Nick Street, Stephen Baek, Qihang Lin, Jingyi Yang, Yankun Huang

- 連合学習は複数クライアントが共同でモデルを訓練しつつデータプライバシーを守る
- 既存の個別化連合学習はスケーラビリティや通信問題があり、モデル共通の構造を必要とする
- FedPAEは完全に分散化された方法でモデルの異質性と非同期学習をサポートする
- FedPAEは既存の最先端アルゴリズムを上回り、多様なクライアント能力と統計的異質性に強い

非同期でモデルが異なるクライアント同士が連携できるなんてすごいね！完全に分散化されているから、将来のプライバシー技術の可能性が広がりそう！

**Comment:** 10 pages, 5 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-17 22:47

- - -

### [Tensor Decomposition with Unaligned Observations](http://arxiv.org/abs/2410.14046)

**アライメントしていない観測データを用いたテンソル分解**

Runshi Tang, Tamara Kolda, Anru R. Zhang

- アライメントしていない観測のテンソル分解を提案し、RKHSを使って表現している
- バイナリ、整数、正の値など様々なデータ型に対応した多用途な損失関数を導入
- 最適化アルゴリズムと確率的勾配法で計算効率向上を図る
- 合成データと幼児のヒト微生物データセットを用いて手法の有効性を示す

テンソル分解の手法って面白そう！特に様々なデータ型に対応した損失関数がどんな風に役立つのか見てみたいかも。それに、幼児の微生物データを使っているのがユニークで楽しいよね。



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, cs.NA, math.NA, stat.CO, stat.ME, **投稿日時:** 2024-10-17 21:39

- - -

### [Optimal Communication and Key Rate Region for Hierarchical Secure Aggregation with User Collusion](http://arxiv.org/abs/2410.14035)

**階層構造のセキュア集約におけるユーザー共謀に対する最適な通信と鍵レート領域**

Xiang Zhang, Kai Wan, Hua Sun, Shiqiang Wang, Mingyue Ji, Giuseppe Caire

- 複数のユーザー入力を安全に集約サーバにアップロードするのがセキュア集約の目的
- 連合学習などの分散学習で、暗号技術を使いサーバが入力以上の情報を得られないようにする
- 階層型ネットワークでのセキュア集約における通信の効率と鍵生成のトレードオフを解析
- 集約サーバと中継の両方がユーザーの入力を知ることなく、希望する集合を学ぶことが課題

階層的なネットワーク構造の中で、セキュアな集約をどう実現するかにフォーカスしているね。未来の分散型AIシステムのプライバシー問題を考える上で大切な役割を持ちそうだね。テクノロジーが進化する中で、プライバシーを守る新しい方法の模索が面白いよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, math.IT, **投稿日時:** 2024-10-17 21:17

- - -

### [Identifying Privacy Personas](http://arxiv.org/abs/2410.14023)

**プライバシー・ペルソナの特定**

Olena Hrynenko, Andrea Cavallaro

- プライバシー・ペルソナは、ユーザーの知識、行動、自己効力感、プライバシー保護意識の違いを表す
- 現行のペルソナは、制御レベルの認識やPET利用動機で異なる人々を一括りにしている
- 新しい8つのペルソナを提案し、教育的な質問票への回答を用いて分析
- 提案したペルソナは統計的に有意差があり、従来よりも詳細かつ包括的な理解を提供する

この研究ってめちゃ興味深いよね！プライバシー意識って人それぞれ違うから、こうやって詳しく分類していくことで、もっと個々に合ったサポートができるようになるのが良さそう！わたしも自分のペルソナ知りたくなっちゃった！



**トピック:** [PETs](pets), **カテゴリ:** cs.LG, cs.CY, **投稿日時:** 2024-10-17 20:49

- - -

### [Conformal Prediction for Federated Graph Neural Networks with Missing Neighbor Information](http://arxiv.org/abs/2410.14010)

**連合グラフニューラルネットワークに対する近傍情報欠損時の適合予測**

Ömer Faruk Akgül, Rajgopal Kannan, Viktor Prasanna

- グラフデータセットの拡大と連合学習フレームワークでの分散的な部分グラフ管理の重要性
- 近傍情報の欠損が安全性に影響を与えるため、モデルの不確実性が課題
- 適合予測（CP）が連合グラフ学習にも適用可能であることを提案
- 変分オートエンコーダを用いて欠損データを再構築し、予測セットを小さくしつつ保証を維持

グラフニューラルネットワークの連合学習という未来的なコンセプトが面白い！近傍情報が欠けているとき、変分オートエンコーダで解決するアプローチが斬新だね。保証付きの小さい予測セットが実現できるなんて、データが多様化した現代にピッタリかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-17 20:22

- - -

### [Debiasing Large Vision-Language Models by Ablating Protected Attribute Representations](http://arxiv.org/abs/2410.13976)

**大規模視覚言語モデルのバイアス除去: 保護属性表現の削除による手法**

Neale Ratzlaff, Matthew Lyle Olson, Musashi Hinck, Shao-Yen Tseng, Vasudev Lal, Phillip Howard

- 大規模視覚言語モデルは社会的バイアスの影響を受け、画像に対する応答に偏りを生じさせることがある。
- 本研究では、テキスト生成中にバイアス属性を削除し保護属性に関するテキストの生成を回避する新しいフレームワークを提案。
- 提案手法はトレーニングを必要とせず、数千のバイアス出力を用いるだけで実現可能である。
- バイアス除去後も、実データでのキャプション生成性能を維持しつつ、モデルの精度を保つことができると実験で示された。

この論文、大規模モデルのバイアスを取り除きながら精度を落とさないってすごくない？合成データを活用することで、実データへの応用もしやすいからもっと色んなところに役立ちそうだね！

**Comment:** NeurIPS workshop on SafeGenAI, 10 pages, 2 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, cs.LG, **投稿日時:** 2024-10-17 19:02

- - -

### [CoreGuard: Safeguarding Foundational Capabilities of LLMs Against Model Stealing in Edge Deployment](http://arxiv.org/abs/2410.13903)

**CoreGuard: エッジでのモデル盗難に対抗するLLM基盤能力の保護**

Qinfeng Li, Yangfan Xie, Tianyu Du, Zhiqiang Shen, Zhenghan Qin, Hao Peng, Xinkui Zhao, Xianwei Zhu, Jianwei Yin, Xuhong Zhang

- 専有の大規模言語モデル（LLM）は多様なタスクで優れた一般化能力を持つ
- エッジデバイスへのLLM展開は効率およびプライバシーの理由で人気がある
- エッジでのLLMの展開は新たなセキュリティ脅威、基盤能力の盗難につながる
- CoreGuardを提案、効率的な計算と通信でエッジデバイス上でのモデル保護を実現

エッジデバイスって小型のデバイスでプライバシーを守るためにモデルをそのまま動かすこともできるんだね！CoreGuardがあれば、そのプライバシーも侵されないようにしっかり守ってくれるのかな？なんか未来の話みたいでワクワクするね！



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.AI, cs.DC, **投稿日時:** 2024-10-16 08:14
