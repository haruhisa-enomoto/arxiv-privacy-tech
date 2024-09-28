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

更新: 2024-09-28T04:21:27.550223

- - -

### [Slowly Scaling Per-Record Differential Privacy](http://arxiv.org/abs/2409.18118)

**ゆっくりとスケーリングするレコードごとの差分プライバシー**

Brian Finley, Anthony M Caruso, Justin C Doty, Ashwin Machanavajjhala, Mikaela R Meyer, David Pujol, William Sexton, Zachary Terner

- 多くの外れ値を含むデータの統計を公開するための形式的なプライバシーメカニズムを開発
- レコードの影響が大きいほどプライバシー損失が大きくなるが、新しいメカニズムはその低下を対数関数的に抑制
- 例えば給与データのような無限に拡張可能なデータも、影響力の大きいレコードに対して意味のあるプライバシー保護を提供
- 提案したメカニズムの実用性を実証実験で評価し、その有用性を確認

めっちゃ面白そう！経済データみたいな複雑なデータもこれで安心して使えそうだね。ログ関数的に抑えるってすごい未来が広がりそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, stat.ME, **投稿日時:** 2024-09-26 17:56

- - -

### [AI-Powered Augmented Reality for Satellite Assembly, Integration and Test](http://arxiv.org/abs/2409.18101)

**衛星の組立、統合、試験のためのAI駆動型拡張現実**

Alvaro Patricio, Joao Valente, Atabak Dehban, Ines Cadilha, Daniel Reis, Rodrigo Ventura

- AIとARの統合により、衛星のAIT（組立、統合、試験）プロセスの精度向上と人為的ミスの最小化が実現
- Microsoft HoloLens 2を用いてARを実装し、技術者にリアルタイムの指示とフィードバックを提供
- 合成データを用いたAIモデルの訓練により、動的な衛星環境でのデータ取得の課題を克服
- SAMAL（Segmented Anything Model for Automatic Labelling）により、データの自動注釈が手動より20倍速く実現

AIとARがこんなに応用されてるなんてすごいね！これからどんなロボットができるのか、すごく楽しみ！技術の進歩で宇宙がもっと身近になるかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, 68T05, 68U20, I.2.1; H.5.2; I.4.8; I.2.10, **投稿日時:** 2024-09-26 17:44

- - -

### [Transferring disentangled representations: bridging the gap between synthetic and real images](http://arxiv.org/abs/2409.18017)

**分解表現の転送: 合成画像と実画像のギャップを埋める**

Jacopo Dapueto, Nicoletta Noceti, Francesca Odone

- 意味のある効率的なデータ構造の分離が表現学習で重要
- 実画像において分解表現学習が未発展である理由の調査
- 合成データを活用して使い回し可能な分解表現を学習
- 転送後の分解特性の検証と新たな評価メトリックの提案

合成データから実画像への転送が上手く行くとか、すごくない？新たなメトリックでの評価とかも気になるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-09-26 16:25

- - -

### [Safe Time-Varying Optimization based on Gaussian Processes with Spatio-Temporal Kernel](http://arxiv.org/abs/2409.18000)

**ガウス過程と時空間カーネルを用いた安全な時間変動最適化**

Jialin Li, Marta Zagorowska, Giulia De Pasquale, Alisa Rupenyan, John Lygeros

- 逐次決定問題における安全性が重要であるが、時間変動システムでは最適な決定を見つけるのが難しい
- TVSafeOptは、ベイズ最適化と時空間カーネルを用いて未知の時間変動報酬と安全制約を最適化するアルゴリズム
- 明示的な変化検出なしに安全な時間変動領域を追跡することが可能で、問題が静的になると最適性も保証される
- TVSafeOptは、ガス圧縮機のケーススタディで時間変動最適化問題の安全性を確保し、安全性と最適性でSafeOptより有利

この論文、すごくおもしろそうだね！特に、明示的な変化検出なしで最適化できるのは革新的。ガス圧縮機の例もリアルで役立ちそう！

**Comment:** Accepted to NeurIPS 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, math.OC, **投稿日時:** 2024-09-26 16:09

- - -

### [Federated Learning under Attack: Improving Gradient Inversion for Batch of Images](http://arxiv.org/abs/2409.17767)

**攻撃下での連合学習：画像のバッチ処理における勾配逆転の改善**

Luiz Leite, Yuri Santo, Bruno L. Dalmazo, André Riker

- 連合学習はユーザーデータのプライバシーを保護するための機械学習手法である
- 各クライアントがローカルでモデルをトレーニングし、中央サーバがパラメータを集約する
- DLG-FBという手法を提案し、画像バッチ内での空間的相関を考慮して勾配逆転攻撃を改善
- 攻撃成功率が19.18％、攻撃画像あたりのイテレーションが48.82％向上

連合学習ってだけでプライバシーに強そうだけど、やっぱり攻撃ってあるんだね！DLG-FBでどれだけ強化されるのか楽しみ！

**Comment:** 5 pages, 7 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-09-26 12:02

- - -

### [Byzantine-Robust Aggregation for Securing Decentralized Federated Learning](http://arxiv.org/abs/2409.17754)

**ビザンチン耐性を備えた分散型連合学習のための集約技術**

Diego Cajaraville-Aboy, Ana Fernández-Vilas, Rebeca P. Díaz-Redondo, Manuel Fernández-Veiga

- 分散型連合学習(DFL)は、中央サーバーなしでスケーラビリティと堅牢性を向上するが、セキュリティ最適化が課題
- 本研究は新規ビザンチン耐性の集約アルゴリズム(WFAgg)を提案し、動的な分散トポロジーでの堅牢性を強化
- 複数のフィルターを用いて、ビザンチン攻撃を識別し軽減する仕組みを導入
- 提案手法は、多様なビザンチン攻撃シナリオでもモデル精度と収束を維持し、既存の中央集約方式を上回る

どんなビザンチン攻撃にも対応できる手法ってすごく未来的！実験結果も良好みたいだから、本当に実用されるのが楽しみだね。

**Comment:** 18 pages, 7 figures, 1 table

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-26 11:36

- - -

### [Artificial Data Point Generation in Clustered Latent Space for Small Medical Datasets](http://arxiv.org/abs/2409.17685)

**小規模医療データセットのためのクラスタ化潜在空間における人工データポイント生成**

Yasaman Haghbin, Hadi Moradi, Reshad Hosseini

- 小規模の医療データセットにおいて、機械学習モデルの性能向上を目指すため、合成データ生成が行われた
- AGCLフレームワークは、特徴抽出、K-meansクラスタリング、クラス分離指標に基づくクラスタ評価、および合成データ生成のプロセスを含む
- 本手法はパーキンソン病のスクリーニングに適用され、複数の機械学習分類器によって評価された
- 実験結果から、AGCLはベースラインおよび他の手法と比較して分類精度を大幅に向上させ、最高テスト精度83.33%、クロスバリデーション精度90.90%を達成した

医療データの不足を補うって凄いね！顔の表情データを使ってパーキンソン病をスクリーンするなんて、今後の医療に期待いっぱいだね！

**Comment:** 8 pages, 2 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.LG, **投稿日時:** 2024-09-26 09:51

- - -

### [Preserving logical and functional dependencies in synthetic tabular data](http://arxiv.org/abs/2409.17684)

**合成表データにおける論理的および機能的依存関係の保持**

Chaithra Umesh, Kristian Schultz, Manjunath Mahendra, Saparshi Bej, Olaf Wolkenhauer

- 現在の合成データ生成アルゴリズムは、属性間の依存関係を完全には保持していない
- 新たに属性間の論理的依存関係の概念を導入し、定量化する指標を提供
- いくつかの最新の合成データ生成アルゴリズムの論理的および機能的依存関係の保持能力を評価
- 研究の結果、特定のタスクに適した合成データ生成アルゴリズムの開発の必要性と機会が明らかになった

この研究、めっちゃ面白そう！特に、論理的依存関係の新しい指標がどれだけ役立つのか気になるね。明日の授業でこの話、みんなにもシェアしよう！

**Comment:** Submitted to Pattern Recognition Journal

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-26 09:51

- - -

### [A Comprehensive Review of TLSNotary Protocol](http://arxiv.org/abs/2409.17670)

**TLSNotaryプロトコルの包括的レビュー**

Maciej Kalka, Marek Kirejczyk

- TLSはインターネット通信を保護する暗号プロトコルであり、主にウェブ閲覧セッションを保護するために使用
- TLSNotaryプロトコルは、クライアントがTLSセッションのデータの出所を証明することを目的としている
- サーバー側の調整や許可なしで証明を実現するため、安全なマルチパーティ計算（MPC）とゼロ知識証明を使用
- TLSNotaryプロトコルを理解するために、最初に必要な暗号プリミティブと標準TLSプロトコルを紹介し、詳細を検討

TLSNotary、なんか複雑そうだけど面白そう！セキュアに通信しながらちゃんとデータの証明もできるって、すごい未来的だよね。



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-26 09:28

- - -

### [Fully Dynamic Graph Algorithms with Edge Differential Privacy](http://arxiv.org/abs/2409.17623)

**エッジ差分プライバシーを考慮した完全動的グラフアルゴリズム**

Sofya Raskhodnikova, Teresa Anna Steiner

- エッジの追加と削除が連続的に行われる完全動的な環境での差分プライベートアルゴリズムを研究
- 三角形の数、連結成分の数、最大マッチングのサイズ、次数ヒストグラムなどの基本グラフ統計に対応
- イベントレベルとアイテムレベルの2種類のエッジ差分プライバシーを研究し、それぞれの誤差に上限と下限を設定
- アイテムレベルプライバシーにおけるアルゴリズムの誤差が下限に一致する問題もいくつか存在

この研究、すごく興味深いよね！特に、エッジ差分プライバシーを使った完全動的アルゴリズムが新しい道を切り開いている感じがするよ～

**Comment:** 30 pages, 3 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, **投稿日時:** 2024-09-26 08:17

- - -

### [Diversity-Driven Synthesis: Enhancing Dataset Distillation through Directed Weight Adjustment](http://arxiv.org/abs/2409.17612)

**多様性駆動の合成：指向重み調整によるデータセット蒸留の強化**

Jiawei Du, Xin Zhang, Juncheng Hu, Wenxin Huang, Joey Tianyi Zhou

- データ関連コストの増加により、情報豊富なデータセットを凝縮する研究が進む
- データセット蒸留は、元のデータセットを代表する合成データを生成し、ニューラルネットワークの訓練に利用
- 合成データセットの冗長性を避けるため、各要素が固有の特徴を持ち、合成段階で多様性を維持することが重要
- 動的かつ指向的な重み調整技術を用いた新しい手法を導入し、多様な合成データを低コストで生成可能

面白そう！データセット蒸留でコストを抑えながら多様性を保つなんて未来の研究っぽいよね。これが実現すれば、いろんなAIモデルの訓練がもっと手軽になるかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-09-26 08:03

- - -

### [Dataset Distillation-based Hybrid Federated Learning on Non-IID Data](http://arxiv.org/abs/2409.17517)

**データセット蒸留に基づく非IIDデータ上のハイブリッド連合学習**

Xiufang Shi, Wei Zhang, Mincheng Wu, Guangyi Liu, Zhenyu Wen, Shibo He, Tejal Shah, Rajiv Ranjan

- クライアントデータの異種性がモデル訓練の性能に大きな影響を与える
- ラベル分布の偏り問題を解決するため、データセット蒸留を利用したフレームワークHFLDDを提案
- クライアントを異種クラスターに分割し、ヘッダーが蒸留データを収集してモデル訓練を実施
- 提案手法はテスト精度と通信コストの両方でベースライン手法を上回る

クライアントのデータラベルの偏りをどう克服するかがポイントみたい。本当に精度がどれくらい良くなるのか気になるね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-26 03:52

- - -

### [BioZero: An Efficient and Privacy-Preserving Decentralized Biometric Authentication Protocol on Open Blockchain](http://arxiv.org/abs/2409.17509)

**BioZero: 効率的かつプライバシー保護型の分散バイオメトリクス認証プロトコルのオープンブロックチェーン上での実装**

Junhao Lai, Taotao Wang, Shengli Zhang, Qing Yang, Soung Chang Liew

- デジタルアイデンティティの重要性と従来の認証手法の限界
- ブロックチェーン技術を活用した分散型認証の可能性と既存の課題
- BioZeroはPedersenコミットメントと準同型計算でユーザープライバシーを保護
- Zero-knowledge proofsを使った効率的なオンチェーン検証が可能

バイオメトリクスを使って、ブロックチェーンでこんな分散認証ができるなんてすごい！最新技術をフル活用してて、かなり興味深いよね。

**Comment:** 14 pages, 3 figures

**トピック:** [SSI/DID/VC](ssi), [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-26 03:37

- - -

### [Does Worst-Performing Agent Lead the Pack? Analyzing Agent Dynamics in Unified Distributed SGD](http://arxiv.org/abs/2409.17499)

**最もパフォーマンスの低いエージェントがリーダーになるのか？統一分散SGDにおけるエージェント動態の分析**

Jie Hu, Yi-Ting Ma, Do Young Eun

- 統一分散SGDについて、非中央集権型SGDとフェデレーティッドラーニングの文脈で分析
- i.i.d.サンプリング、シャッフル、マルコフサンプリングがUD-SGDの収束速度に与える影響を調査
- 高パフォーマンスエージェントの効率的なサンプリング戦略が収束を改善することを理論と実証で示す
- シミュレーションで、少数の高効率エージェントが大多数の中程度効率エージェントと同等以上の成果を達成することを確認

少数のエージェントのパフォーマンスが全体の結果に大きく影響するのって面白い！いかに効率よくサンプリングするかがカギだね。

**Comment:** To appear in NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, math.OC, stat.ML, **投稿日時:** 2024-09-26 03:12

- - -

### [Efficient Federated Learning against Heterogeneous and Non-stationary Client Unavailability](http://arxiv.org/abs/2409.17446)

**異質かつ非定常なクライアントの不在に対する効率的な連合学習**

Ming Xiang, Stratis Ioannidis, Edmund Yeh, Carlee Joe-Wong, Lili Su

- 非定常なクライアントの不在が連合学習の現実展開に大きな影響を与える
- 既存の手法はクライアントの不在の動的な変動を無視または高コスト
- 新手法FedAPMはクライアント不在分を$O(1)$メモリ/計算増のみで補完
- この手法は非定常に対応可能かつ線形スピードアップを達成し収束

新しい手法が本当に便利そうだね！FedAPMなら労力少なくて済むし、これは注目かも。未来の連合学習はこれで決まりか？！

**Comment:** Accepted to NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, math.OC, **投稿日時:** 2024-09-26 00:38

- - -

### [A Hierarchical Gradient Tracking Algorithm for Mitigating Subnet-Drift in Fog Learning Networks](http://arxiv.org/abs/2409.17430)

**フォグ学習ネットワークにおけるサブネットドリフト軽減のための階層的勾配追跡アルゴリズム**

Evan Chen, Shiqiang Wang, Christopher G. Brinton

- 連合学習は、従来の星型トポロジーを採用しないフォグネットワークで拡張性の問題に直面
- セミデセントラライズドFLは、デバイス間通信を活用した二段階モデル協力を提案
- 新たに提案するSD-GTは、各通信層のデバイス更新に追跡項を組み込み、従来の仮定を排除
- 数値評価により、SD-GTは訓練モデルの品質および通信コストで顕著な改善を示す

従来の方法とは全然違う視点から解決策を提案してるなんてすごいね！これでデータがより分散している環境でも精度が上がるといいね。

**Comment:** This paper is under review in IEEE/ACM Transactions on Networking

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, **投稿日時:** 2024-09-25 23:38

- - -

### [Sociotechnical Approach to Enterprise Generative Artificial Intelligence (E-GenAI)](http://arxiv.org/abs/2409.17408)

**企業向け生成人工知能 (E-GenAI) の社会技術的アプローチ**

Leoncio Jimenez, Francisco Venegas

- SCM、ERP、CRMプラットフォームを通じ、プロバイダー、企業、顧客間の関係を強調する事業エコシステムを分析
- OIDモデルを通じて、ビジネスインテリジェンス（BI）、ファジィロジック（FL）、TRIZを整合
- OIDKモデルを通じて、知識管理(KM)と不完全知識管理(IKM)を整合する方法を探求
- フォロワーとフォロイー間の関係を有限オートマトンでモデル化し、特定のユーザー特性を識別するLLMを構築

企業と顧客の関係を生成AIで強化！？この技術、私たちの未来でどう活用されるか、めっちゃ気になるね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CY, cs.AI, cs.IT, math.IT, **投稿日時:** 2024-09-25 22:39

- - -

### [Exploring synthetic data for cross-speaker style transfer in style representation based TTS](http://arxiv.org/abs/2409.17364)

**スタイル表現に基づくTTSにおける話者間スタイル転送のための合成データの探求**

Lucas H. Ueda, Leonardo B. de M. M. Marques, Flávio O. Simões, Mário U. Neto, Fernando Runstein, Bianca Dal Bó, Paula D. P. Costa

- 音声における話者とスタイル情報の分離が難しく、TTSモデルにおける話者間スタイル転送が課題
- 資源が限られた表現データ環境では、VCが目標話者のための表現音声を生成できる
- VCモデルが生成する合成データを利用することで、TTSモデルの自然さと話者の類似性を向上可能
- このアプローチを異言語シナリオに拡張することで、アクセント転送も強化される

なんか、いろんな言葉のアクセントとか声の違いを真似できるTTSができるって感じで面白そう！もっといろんな言葉がスムーズに話せるAIになりそうだよね。

**Comment:** Accepted at SynData4GenAI 2024

**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.SD, **投稿日時:** 2024-09-25 21:16

- - -

### [Language Grounded Multi-agent Communication for Ad-hoc Teamwork](http://arxiv.org/abs/2409.17348)

**アドホックチームワークのための言語に基づくマルチエージェントコミュニケーション**

Huao Li, Hossein Nourkhiz Mahjoub, Behdad Chalaki, Vaishnav Tadiparthi, Kwonjoon Lee, Ehsan Moradi-Pari, Charles Michael Lewis, Katia P Sycara

- MARLは共有通信プロトコルを学習し、難しいチームタスクを実施
- エージェント間の通信は人間に理解できないことが多く、アドホックチームでの適用が困難
- 大規模言語モデル(LLM)で生成された合成データを基に通信空間を人間の自然言語の埋め込み空間に整合
- 言語基盤を導入することでタスクのパフォーマンスを保ちながら、通信の出現を加速

これ、エージェントと人間とが一緒にチーム組んでゲームとかできる未来も見えるかも！私たちもいつかロボットと一緒にグループ活動することになるのかな？なんかワクワクするね！

**Comment:** Accepted to Neurips 2024, 16 pages, 3 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.MA, **投稿日時:** 2024-09-25 20:49

- - -

### [The poison of dimensionality](http://arxiv.org/abs/2409.17328)

**次元の毒性**

Lê-Nguyên Hoang

- 機械学習モデルのサイズがその毒性に対する脆弱性に影響することを検証
- 線形およびロジスティック回帰で特定のパラメータ条件下でモデル操作が可能であることを証明
- モデルの表現力の増加と攻撃可能性のトレードオフを示す実験を実施
- 線形分類器におけるMNISTおよびFashionMNISTデータでの調査結果と潜在的な影響について議論

うわぁ、モデルのサイズが大きいほど攻撃がしやすくなるなんて意外だね！これがどれだけ深層学習に影響を及ぼすのかも気になる～。

**Comment:** 29 pages, 3 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-09-25 20:06

- - -

### [KIPPS: Knowledge infusion in Privacy Preserving Synthetic Data Generation](http://arxiv.org/abs/2409.17315)

**KIPPS: プライバシー保護型合成データ生成における知識注入**

Anantaa Kotal, Anupam Joshi

- 差分プライバシー技術の統合により、合成データのプライバシーが保証される
- 生成モデルはサイバーセキュリティやヘルスケアなどの重要な領域でのデータ生成に課題がある
- トレーニングデータセットが限定的で多様性がない場合、繰り返し生成される敏感な特徴がプライバシーリスク
- 新しいKIPPSモデルは知識グラフからドメインと規制知識を注入し、現実的でドメイン準拠の合成データ生成を実現

この研究、実際のサイバーセキュリティやヘルスケアデータで試してるんだね。だから、個人情報保護とデータ品質のバランスがとれたデータがどれくらい作れるか、期待しちゃう！



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-09-25 19:50

- - -

### [Investigating Privacy Attacks in the Gray-Box Setting to Enhance Collaborative Learning Schemes](http://arxiv.org/abs/2409.17283)

**グレーボックス設定におけるプライバシー攻撃の調査と協調学習方式の強化**

Federico Mazzone, Ahmad Al Badawi, Yuriy Polyakov, Maarten Everts, Florian Hahn, Andreas Peter

- 協調学習では生データを隠してもプライバシーが完全に保護されるわけではない
- グレーボックス設定では攻撃者のアクセスが限定されているため、新たなインサイトが得られる
- 準同型暗号を用いたSmartCryptNNで、高プライバシーリスク部分のモデルを保護する手法を提案
- 密なニューラルネットワークでの評価では、特定層だけの保護がプライバシーと効率を最適化

この研究、めっちゃ「協調学習」の未来を変えるかも！特にSmartCryptNNの部分が面白そう♪

**Comment:** 19 pages, 7 figures, in submission

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-25 18:49

- - -

### [Immersion and Invariance-based Coding for Privacy-Preserving Federated Learning](http://arxiv.org/abs/2409.17201)

**プライバシー保護連合学習のためのイマージョン・不変性に基づくコーディング**

Haleh Hayati, Carlos Murguia, Nathan van de Wouw

- 連合学習（FL）は、プライバシーを保護しながら分散学習を行う方法である
- FLでは、クライアントがデータを共有せずにデバイス上でモデルを訓練するが、モデル更新から情報が漏れる可能性がある
- 本研究では、差分プライバシーと制御理論のシステムイマージョンツールを組み合わせたFLフレームワークを提案
- 提案フレームワークは、元のアルゴリズムのパラメータが符号化パラメータに収束するように設計され、サーバでデコード可能である

差分プライバシーも制御理論も使ってプライバシーと精度を両立できるアイデアがワクワクするね！連合学習がますます安心して使えるようになるかも～✨



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-09-25 15:04

- - -

### [Decentralized Federated Learning with Gradient Tracking over Time-Varying Directed Networks](http://arxiv.org/abs/2409.17189)

**時間変化する有向ネットワーク上での勾配追跡を用いた分散連合学習**

Duong Thuy Anh Nguyen, Su Wang, Duong Tung Nguyen, Angelia Nedich, H. Vincent Poor

- 時間変化する有向グラフ上での連合学習を対象に、DSGTm-TVアルゴリズムを提案
- アルゴリズムには勾配追跡とヘビーボールモーメンタムを組み込み、グローバル目標関数を分散的に最適化
- 提案手法は隣接エージェントとの情報交換を通じて、モデルパラメータと勾配推定値を更新する仕組み
- 実世界の画像分類や自然言語処理タスクで、最先端手法に対する優位性を実証

この研究、すごく面白そうだね！特に分散連合学習の新しいアプローチでいろいろな課題を解決しそうなところがワクワクするよ。



**トピック:** [連合学習](fl), **カテゴリ:** math.OC, cs.LG, **投稿日時:** 2024-09-25 06:23
