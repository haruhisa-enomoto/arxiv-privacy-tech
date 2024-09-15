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

更新: 2024-09-15T04:20:11.387520

- - -

### [Source2Synth: Synthetic Data Generation and Curation Grounded in Real Data Sources](http://arxiv.org/abs/2409.08239)

**Source2Synth: 実データ源に基づいた合成データ生成とキュレーション**

Alisia Lupidi, Carlos Gemmell, Nicola Cancedda, Jane Dwivedi-Yu, Jason Weston, Jakob Foerster, Roberta Raileanu, Maria Lomeli

- Source2Synthは、高価な人間のアノテーションなしでLLMに新しいスキルを教えるための方法
- カスタムデータソースを取り込み、実世界の情報に基づいた中間推論ステップ付きの合成データを生成
- 質問可能性に基づいて低品質な生成物を除去することでデータセットの質を向上
- multi-hop質問応答と表形式質問応答の挑戦領域でそれぞれ22.57%と25.51%の性能向上を実現

この研究、結構すごいよね！データ収集が大変なときに、Source2Synthで手軽にデータ品質を上げられるなんて、未来が楽しみ♪



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-09-12 17:39

- - -

### [Multi-Model based Federated Learning Against Model Poisoning Attack: A Deep Learning Based Model Selection for MEC Systems](http://arxiv.org/abs/2409.08237)

**モデル毒を防ぐためのマルチモデル連合学習: MECシステムにおける深層学習モデル選択**

Somayeh Kianpisheh, Chafika Benzaid, Tarik Taleb

- 連合学習はデータプライバシーを保ちながら分散データからグローバルモデルを訓練する技術
- 単一モデルベースの連合学習では、モデル毒攻撃のリスクが存在
- 提案手法はマスターモデルと複数のスレーブモデルの構成を利用し攻撃緩和を図る
- 強化学習を用いたモデル選択により、DDoS攻撃下でも効率的な結果を示す

モデル毒攻撃をこんな感じで防げちゃう連合学習、すごーい！強化学習とかも使ってるから、これからもっと安全になりそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.NI, **投稿日時:** 2024-09-12 17:36

- - -

### [Enhancing Canine Musculoskeletal Diagnoses: Leveraging Synthetic Image Data for Pre-Training AI-Models on Visual Documentations](http://arxiv.org/abs/2409.08181)

**犬の筋骨格系診断の強化: AIモデルの視覚的記録に対する合成画像データの活用**

Martin Thißen, Thi Ngoc Diep Tran, Ben Joel Schönbein, Ute Trapp, Barbara Esteve Ratsch, Beate Egner, Romana Piat, Elke Hergenröther

- 犬の筋骨格系の診断は難しく、新たな視覚的記録法が開発された
- 訓練データ不足を合成データで補完し、AI診断支援システムを開発
- 三つのクラスを持つ基本データセットと36クラスのデータセットを生成してAIを事前訓練
- 少数例では診断精度が約10%向上したが、大規模データセットでは効果が限定的

少ないデータの改善に合成データが使えるなんて未来っぽいよね！犬の医療もどんどん進化してるんだな～。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-12 16:13

- - -

### [On the challenges of studying bias in Recommender Systems: A UserKNN case study](http://arxiv.org/abs/2409.08046)

**推薦システムにおけるバイアス研究の課題: UserKNNケーススタディ**

Savvina Daniil, Manel Slokom, Mirjam Cuper, Cynthia C. S. Liem, Jacco van Ossenbruggen, Laura Hollink

- 推薦システムによるバイアスの伝播は検証が難しく、利用可能なデータセットに依存している
- アルゴリズムの実装選択が明示されず、バイアス伝播に影響を与える可能性がある
- 合成データとUserKNNフレームワークを組み合わせ、データ特性とアルゴリズム構成の影響を調査
- データ特性により結論が異なる場合があり、構成とデータプロパティの明示が重要

推薦システムのバイアス、めっちゃ複雑そう！でも、これちゃんと理解したら、色んな分野に応用できそうだね。未来の技術改善に期待！

**Comment:** Accepted at FAccTRec@RecSys 2024, 11 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.IR, **投稿日時:** 2024-09-12 13:51

- - -

### [Privacy-preserving federated prediction of pain intensity change based on multi-center survey data](http://arxiv.org/abs/2409.07997)

**複数センター調査データに基づいた痛みの変化予測のプライバシー保護型連合学習**

Supratim Das, Mahdie Rafie, Paula Kammer, Søren T. Skou, Dorte T. Grønne, Ewa M. Roos, André Hajek, Hans-Helmut König, Md Shihab Ullaha, Niklas Probul, Jan Baumbacha, Linda Baumbach

- 患者報告データを用いて予後モデルを構築するが、データの分散により集中化が困難
- ローカル学習モデルは精度、堅牢性、一般化能力が劣る
- 連合学習技術により、データがセンターを離れずに予後モデルを構築
- 連合学習モデルはローカルモデルより性能が良く、集中型モデルと同等の成果を示す

連合学習を使うことでプライバシーを守りつつ、精度の高い予測モデルが構築できるなんてすごい！今後の医療分野での応用が楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-12 12:41

- - -

### [Modeling Human Responses by Ordinal Archetypal Analysis](http://arxiv.org/abs/2409.07934)

**序数的アーキテピカル分析による人間の応答のモデル化**

Anna Emilie J. Wedenborg, Michael Alexander Harborg, Andreas Bigom, Oliver Elmgreen, Marcus Presutti, Andreas Råskov, Fumiko Kano Glückstad, Mikkel Schmidt, Morten Mørup

- 質問票から得られる序数データに特化した新しいアーキテピカル分析（AA）のフレームワークを導入
- 提案する序数的アーキテピカル分析（OAA）は、序数データを変換せずに直接扱う方法
- 各個人の尺度認識を考慮し、最適化中に個別の尺度を学習する応答バイアス序数的アーキテピカル分析（RBOAA）を提案
- 合成データと欧州社会調査データセットでその有効性を実証し、序数データの解析における応答バイアスの重要性を強調

質問票のデータをそのまま使えるのがポイントかな！各国でのバイアスも考慮してるし、どんな結果が出るか気になるね。

**Comment:** Accepted at Machine Learning and Signal Processing 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-12 10:58

- - -

### [Non-negative Weighted DAG Structure Learning](http://arxiv.org/abs/2409.07880)

**非負重み付きDAG構造学習**

Samuel Rey, Seyed Saman Saboksayr, Gonzalo Mateos

- 有向非巡回グラフ(DAG)のトポロジーを学習する問題に取り組む
- 非凸最適化の複雑さを克服するために、非負のエッジ重みのみを含むDAGを仮定
- 隣接行列の対数行列式に基づく凸性を用いてサイクルを効果的に特定し防止
- 提案する手法は無限サンプルサイズで真のDAG構造の復元を保証し、既存の最先端手法よりも優れていることを実証

この手法、他のやり方より良い結果が出るみたいじゃん！これなら新しい応用もどんどん見つかりそうだよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-09-12 09:41

- - -

### [Over-the-Air Federated Learning via Weighted Aggregation](http://arxiv.org/abs/2409.07822)

**無線による連合学習の重み付け集約を介して**

Seyed Mohammad Azimi-Abarghouyi, Leandros Tassiulas

- 無線計算を活用した新しい連合学習手法を紹介
- 集約時に適応的な重みを使用し、無線チャネル条件の影響を軽減
- 計算の異種性と一般的な損失関数に対する収束境界を数学的に導出
- 提案手法は従来の手法に比べ、最大30%の精度向上を実現

無線チャネル条件が厳しくても、これだけ精度が上がるなんてめっちゃ興味湧くよね。数学的な部分も多そうだけど、それを乗り越えたらかなり成果が期待できそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, cs.AI, cs.LG, math.IT, **投稿日時:** 2024-09-12 08:07

- - -

### [Controllable Synthetic Clinical Note Generation with Privacy Guarantees](http://arxiv.org/abs/2409.07809)

**制御可能なプライバシー保証付き合成臨床ノート生成**

Tal Baumel, Andre Manoel, Daniel Jones, Shize Su, Huseyin Inan, Aaron, Bornstein, Robert Sim

- 医療データには個人情報が含まれており、プライバシーの懸念が大きい
- 新しい方法でPHIを含むデータセットをクローン化し、重要な特徴を維持
- 差分プライバシー技術と新しい微調整タスクを活用し、識別可能な情報を除去
- クローン化されたデータセットでのモデル訓練は、従来の匿名化データセットを上回る性能を示す

データの匿名化とモデルの性能向上を同時に実現できるなんてめちゃくちゃ画期的だよね！医療研究の未来がもっと明るくなりそうでワクワクする～！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-09-12 07:38

- - -

### [FedHide: Federated Learning by Hiding in the Neighbors](http://arxiv.org/abs/2409.07808)

**FedHide: 近隣に隠れて連合学習する方法**

Hyunsin Park, Sungrack Yun

- クライアントが単一クラスのデータを持つシナリオで、埋め込みネットワークを開発
- 真のクラスプロトタイプ共有がプライバシーを侵害する可能性を回避するため、代理クラスプロトタイプを提案
- 近隣との線形結合によって代理クラスプロトタイプを生成、真のクラスプロトタイプを隠す
- CIFAR-100、VoxCeleb1、VGGFace2の3つのベンチマークデータセットで効果を実証

クラスプロトタイプを隠すことでプライバシー保護しながら学習できるなんてすごい！その上、実験結果もあり信頼できるね。

**Comment:** ECCV 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-12 07:37

- - -

### [In-Situ Fine-Tuning of Wildlife Models in IoT-Enabled Camera Traps for Efficient Adaptation](http://arxiv.org/abs/2409.07796)

**IoT対応カメラトラップにおけるワイルドライフモデルのインシチュ調整による効率的適応**

Mohammad Mehdi Rastikerdar, Jin Huang, Hui Guan, Deepak Ganesan

- カメラトラップによる野生動物監視は重要で、機械学習モデルにはドメインシフトとリソース制約が課題
- WildFitは、高いドメイン一般化性能と効率的な推論を両立する新手法で、現在のロケーションや時間に適応する
- 背景認識のデータ合成によりトレーニング画像を生成し、新しい環境での分類精度を高め、大しな計算リソースを不要に
- 背景ドリフト検出やクラス分布ドリフト検出を使い、生成データの質の最適化と一般化性能を向上

カメラトラップでの野生動物監視がもっと効率的になるなんて面白そう！これでもっとリアルタイムの動物保護とかに役立てたら素敵だね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-09-12 06:56

- - -

### [PDC-FRS: Privacy-preserving Data Contribution for Federated Recommender System](http://arxiv.org/abs/2409.07773)

**PDC-FRS: 連合推薦システムのためのプライバシー保護データ貢献**

Chaoqun Yang, Wei Yuan, Liang Qu, Thanh Tam Nguyen

- 連合推薦システムはユーザーデータをローカルに保管しつつ、モデルパラメータを中央サーバーに送信する
- ユーザーデータの非集中化が原因で、アップロードされたモデル更新が最適から遠ざかる可能性がある
- 差分プライバシーを保証するデータ共有メカニズムを設計し、補助モデルを並行して訓練する提案
- 補助モデルが各ユーザーのローカルデータセットを拡張し、グローバルな協調情報を統合することで効果を実証

新しいプライバシー保護メカニズムが補助モデルと一緒に使われることで、システム全体のパフォーマンスが向上しそうだね！実験結果もすごく気になる〜。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.IR, **投稿日時:** 2024-09-12 06:13

- - -

### [Efficient Privacy-Preserving KAN Inference Using Homomorphic Encryption](http://arxiv.org/abs/2409.07751)

**準同型暗号を用いた効率的なプライバシー保護KAN推論**

Zhizheng Lai, Yufei Zhou, Peijia Zheng, Lin Chen

- KANの推論時にプライバシー漏洩の課題がある
- 準同型暗号でプライバシー保護の推論を可能にし、データセキュリティを確保
- SiLU活性化関数のために特定の多項式近似を導入し、高い精度を実現する
- CIFAR-10データセットでの推論遅延が従来の方法より7倍以上高速化

KANの高度なモデルをプライバシー保護しつつ利用できるのがすごいね。準同型暗号の応用がどんどん広がりそう！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-09-12 04:51

- - -

### [DFDG: Data-Free Dual-Generator Adversarial Distillation for One-Shot Federated Learning](http://arxiv.org/abs/2409.07734)

**DFDG: データフリーのデュアルジェネレータ敵対的蒸留を用いたワンショット連合学習**

Kangyang Luo, Shuai Wang, Yexuan Fu, Renrong Shao, Xiang Li, Yunshi Lan, Ming Gao, Jinlong Shu

- 連合学習は、クライアントがプライベートデータセットを共有せずにモデル情報を共有してグローバルモデルを共同訓練する分散機械学習スキームである
- 通信とプライバシーの懸念から、単一通信ラウンドによるワンショット連合学習が有望視されている
- 既存のワンショット連合学習法は、公開データセットの必要性や同質なモデル設定に依存し、ローカルモデルからの知識蒸留が限られているため、実用的ではない
- 提案するDFDGは、デュアルジェネレータの訓練を通じてローカルモデルの訓練空間を広げ、性能の向上を達成する

データフリーでどんなデータでも対応できるのかが気になる〜。いっぱい検証したみたいだから、他のベースラインに勝ったのも納得だね。期待でワクワクしちゃう！

**Comment:** Accepted by ICDM2024 main conference (long paper)

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-09-12 03:44

- - -

### [Passed the Turing Test: Living in Turing Futures](http://arxiv.org/abs/2409.07656)

**チューリングテストを突破：チューリングの未来に生きる**

Bernardo Gonçalves

- 生成的人工知能は、テキスト、画像、音声、合成データなどを生成する能力を持つ
- プリプログラムや特別なトリックを用いずに学習し、人間のように振る舞うことが可能
- 現在、これらの機械はチューリングテストを通過しうるが、これは多くの未来の一つに過ぎない
- チューリングが想定した「子供機械」は人間社会に影響を与える可能性があるとされた

生成的AIが人間らしく振る舞うなんて、すごく未来的でワクワクするよね。どんな影響が出てくるのか、ちょっと楽しみかも。

**Comment:** Author's version. Forthcoming in Intelligent Computing, a Science   Partner Journal published in affiliation with Zhejiang Lab   (https://spj.science.org/journal/icomputing). First submitted 19 Feb 2024.   Revised 16 Jul 2024. Accepted 15 Aug 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CY, **投稿日時:** 2024-09-11 22:56

- - -

### [HERL: Tiered Federated Learning with Adaptive Homomorphic Encryption using Reinforcement Learning](http://arxiv.org/abs/2409.07631)

**HERL: 強化学習を用いた適応準同型暗号を用いた階層的連合学習**

Jiaxang Tang, Zeshan Fayyaz, Mohammad A. Salahuddin, Raouf Boutaba, Zhi-Li Zhang, Ali Anwar

- 準同型暗号の統合はデータ機密性を確保するが、計算と通信のオーバーヘッドが増大
- クライアントの計算能力とセキュリティニーズの違いに対応するため、強化学習を用いる
- Q学習によって暗号化パラメータを動的に最適化し、階層別にクライアントを分類
- HERLは計算オーバーヘッドを大幅に削減し、効率性とユーティリティを向上

強化学習で連合学習が効率的になるってすごくない？計算のオーバーヘッドも減るから、リアルタイムのアプリとかにも使えそうだね！



**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-09-11 21:26

- - -

### [EchoDFKD: Data-Free Knowledge Distillation for Cardiac Ultrasound Segmentation using Synthetic Data](http://arxiv.org/abs/2409.07566)

**EchoDFKD: 合成データを用いた心臓超音波セグメンテーションのためのデータなし知識蒸留**

Grégoire Petit, Nathan Palluau, Axel Bauer, Clemens Dlaska

- 心臓超音波（エコー）動画における機械学習の応用が進展中
- 知識蒸留を用い、合成データを用いた場合でも高精度を実現
- 合成データで訓練されたモデルが実データでの訓練に近い性能を発揮
- 新たな評価法は人間の注釈なしで大型モデルの知識を利用、均一なスコアを獲得

心臓超音波のデータ解析って技術がどんどん進化していくのがすごいね！合成データだけでここまでの精度を出せるなんて、未来の医療がますます楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-11 18:38
