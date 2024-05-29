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

更新: 2024-05-29T04:21:51.986904

- - -

### [Feasibility of Privacy-Preserving Entity Resolution on Confidential Healthcare Datasets Using Homomorphic Encryption](http://arxiv.org/abs/2405.18430)

**準同型暗号を用いた機密医療データセットにおけるプライバシー保護型エンティティ解決の実現可能性**

Yixiang Yao, Joseph Cecil, Praveen Angyan, Neil Bahroos, Srivatsan Ravi

- 患者データセットはHIPAAやGDPRなどの法律により保護される機密情報を含む
- 既存の方法は暗号化によるセキュリティが不足しているか、現実のデータセットには非現実的
- AMPPEREを利用した安全な抽象計算モデルに基づくPPERパイプラインを提案
- 提案手法は精度と効率の面で様々なベースラインと比較して効果的

暗号技術でこんなにちゃんとデータを守りつつ、効率よく患者情報を扱えるなら、これからの医療分野でめっちゃ頼りになりそう！この研究、他の分野にも応用できるかな？超気になる！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CE, **投稿日時:** 2024-05-28 17:59

- - -

### [Interpretable classification of wiki-review streams](http://arxiv.org/abs/2405.18335)

**解釈可能なウィキレビューの分類**

Silvia García Méndez, Fátima Leal, Benedita Malheiro, Juan Carlos Burguillo Rial

- ウィキ記事は編集者によるクラウドソーシングであり、継続的なレビューの流れが発生
- いたずらや損傷から記事を守るため、レビューをリアルタイムで分類し、編集者のプロファイリング
- 自己説明可能な分類アルゴリズムを使用し、レビューが取り消される理由を理解可能
- 合成データ生成アルゴリズムを提案し、クラスのバランスを取ることで分類の公平性を向上

リアルタイムでレビューを分析して、すごい！Wikivoyageのデータ使って90％も正確なら、有効そうだね。編集者がなぜリバートされるかもわかるから、もっと協力的になりそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-05-28 16:28

- - -

### [FedSAC: Dynamic Submodel Allocation for Collaborative Fairness in Federated Learning](http://arxiv.org/abs/2405.18291)

**FedSAC: 連合学習における協調的公平性のための動的サブモデル配分**

Zihui Wang, Zheng Wang, Lingjuan Lyu, Zhaopeng Peng, Zhicheng Yang, Chenglu Wen, Rongshan Yu, Cheng Wang, Xiaoliang Fan

- 連合学習でクライアント毎の貢献に基づく報酬配分を行い、公平性を確保する「BCF」を提案
- BCFを実現するため、高性能サブモデルで貢献の大きいクライアントを優遇するモジュールを設計
- 動的集約モジュールを開発し、多様なニューロンを公平に扱うことでモデル精度を向上
- 実験でFedSACが公平性と精度の両面で既存の方法を凌駕することを証明

連合学習の大きな進歩かも！クライアントのやる気も増えそうだね。自分の貢献がちゃんと評価されるのって嬉しいもん！

**Comment:** Accepted by KDD'24

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-28 15:43

- - -

### [The Round Complexity of Proofs in the Bounded Quantum Storage Model](http://arxiv.org/abs/2405.18275)

**制限付き量子ストレージモデルにおける証明のラウンド複雑性**

Alex B. Grilo, Philippe Lamontagne

- 量子リソースはインタラクティブ証明システムのラウンド複雑性改善に大きく寄与
- 悪意のある参加者が全ての量子ビットを保存できないBQSMでプロトコルのラウンド圧縮を研究
- 記憶が制限された検証者のみの非インタラクティブ証明システムが提案され、NPやQMAにも対応
- 古典的な証明システムをBQSMで2メッセージ量子証明システムに圧縮可能

制限付き量子ストレージを使ったら、けっこういろんなことができるんだね！難しそうだけど、量子メモリの限界をうまく利用するアイデアが面白そう！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** quant-ph, cs.CC, cs.CR, **投稿日時:** 2024-05-28 15:24

- - -

### [Delving into Differentially Private Transformer](http://arxiv.org/abs/2405.18194)

**差分プライバシーを備えたTransformerの探求**

Youlong Ding, Xueyang Wu, Yining Meng, Yonggang Luo, Hao Wang, Weike Pan

- 差分プライバシーを用いた深層学習は、モデルの精度とトレーニング効率を向上する多くの方法が開発されてきた
- 本論文はTransformerモデルでの差分プライバシー学習の問題に取り組む
- DP Transformer特有の問題として、Attention分散現象と効率的な勾配クリッピング技術との非互換性を指摘
- Re-Attention MechanismとPhantom Clippingを提案し、これらの問題に対応する方法を示す

どんな新しいアイディアがもっと研究を進めるのか、すごく気になる！連合学習や秘密計算にも応用できたらいいな！

**Comment:** ICML 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-28 14:04

- - -

### [Asynchronous BFT Asset Transfer: Quasi-Anonymous, Light, and Consensus-Free](http://arxiv.org/abs/2405.18072)

**非同期BFT資産転送: 準匿名、軽量、合意不要**

Timothé Albouy, Emmanuelle Anceaume, Davide Frey, Mathieu Gestin, Arthur Rauch, Michel Raynal, François Taïani

- 新しい非同期ビザンチン耐性の資産転送システムを提案
- 準匿名性を持ち、受信者や金額の情報は漏れない
- 軽量で、必要なデータは自身の転送数に対して多項対数的
- 合意不要で、資産転送の全順序に依存しないシステム

合意不要で準匿名のシステムって革命的！チェックしてみる価値ありそうだね。あと、他の暗号アプリにも応用できるって可能性広がる感じする～



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.DC, **投稿日時:** 2024-05-28 11:29

- - -

### [Fast-FedUL: A Training-Free Federated Unlearning with Provable Skew Resilience](http://arxiv.org/abs/2405.18040)

**Fast-FedUL: 訓練不要の連合学習におけるスキュー耐性のある証明付き学習削除**

Thanh Trung Huynh, Trong Bang Nguyen, Phi Le Nguyen, Thanh Tam Nguyen, Matthias Weidlich, Quoc Viet Hung Nguyen, Karl Aberer

- 連合学習(FL)の普及とプライバシー保護の重要性が増し、「忘れられる権利」やデータ改ざん攻撃への対策が必要
- 中央集権型学習には多くの学習削除方法があるが、FLの操作方法とは根本的に異なり適用が困難
- Fast-FedULは再訓練を不要にし、ターゲットクライアントの影響を順次削除するアルゴリズムを提案
- バックドア攻撃シナリオで、ターゲットクライアントの痕跡をほぼ完全に除去し、メインタスクの98%の高い精度を保持

連合学習で再訓練不要なのは大きな進歩かも！バックドア攻撃への対策もすごく重要だろうね。

**Comment:** Accepted in ECML PKDD 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, cs.ET, **投稿日時:** 2024-05-28 10:51

- - -

### [Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization](http://arxiv.org/abs/2405.17932)

**通信効率の高い連合学習を目指したスパースで整合した適応最適化**

Xiumei Deng, Jun Li, Kang Wei, Long Shi, Zeihui Xiong, Ming Ding, Wen Chen, Shi Jin, H. Vincent Poor

- 連合学習で広く使われるAdamは収束が早いが通信オーバーヘッドが大きい
- 新たに提案されたFedAdam-SSMはモデル更新とモーメント推定をスパース化
- 共有スパースマスクを使用し、通信オーバーヘッドをさらに削減
- FedAdam-SSMは収束速度とテスト精度で他の手法よりも優れている

新しいアルゴリズムが通信を減らしつつ性能を保てるか試してみたいよね。共有スパースマスクってどんな感じで実現されるんだろう？



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-28 07:56

- - -

### [Decentralized Directed Collaboration for Personalized Federated Learning](http://arxiv.org/abs/2405.17876)

**個別化連合学習のための分散指向協力**

Yingqi Liu, Yifan Shi, Qinglun Li, Baoyuan Wu, Xueqian Wang, Li Shen

- 連合学習(FL)の中央サーバ依存から脱却し、分散型個別連合学習(DPFL)に焦点
- P2P方式のDPFLは非対称トポロジーの影響でモデルの個別化性能が劣化
- DFedPGPという枠組みを提案、部分モデル個別化と方向付き勾配プッシュを活用
- 提案手法はデータと計算資源の異質性シナリオでもSOTA精度を達成

非対称トポロジーを活用しながらモデルの個別化を目指しているところが面白そう。新しい方法で連合学習の可能性が広がるかもね！

**Comment:** CVPR 2024. arXiv admin note: text overlap with arXiv:2305.15157

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, math.OC, **投稿日時:** 2024-05-28 06:52

- - -

### [PeerFL: A Simulator for Peer-to-Peer Federated Learning at Scale](http://arxiv.org/abs/2405.17839)

**PeerFL: 大規模なピアツーピア連合学習のためのシミュレーター**

Alka Luqman, Shivanshu Shekhar, Anupam Chattopadhyay

- ピアツーピア連合学習ツールをNS3と統合し、新たなシミュレーターを作成
- 異なるデバイスを使った実験が可能で、既存のシミュレーターの不足を補う
- NS3を利用し、移動する参加者のためにWiFiダイナミクスをシミュレーション
- 最大450の異なるデバイスをモデリングし、計算資源の利用効率を実証

ピアツーピア連合学習のシミュレーションなんて面白そう！これなら大規模実験も簡単にできちゃうかも。オープンソースだから、みんなで使い倒せるね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.AI, **投稿日時:** 2024-05-28 05:30

- - -

### [An Innovative Networks in Federated Learning](http://arxiv.org/abs/2405.17836)

**連合学習における革新的なネットワーク**

Zavareh Bozorgasl, Hao Chen

- Wavelet Kolmogorov-Arnold Networks（Wav-KAN）を連合学習に導入し、クライアント側に実装
- 連続ウェーブレット変換（CWT）と離散ウェーブレット変換（DWT）を使い、異種データ分布を多解像度で対応
- Wav-KANは解釈性、計算速度、訓練とテストの精度に優れた結果を実験で示した
- ウェーブレットに基づく活性化関数を使用して、ローカルおよびグローバルモデルの性能を向上

ウェーブレットと連合学習って新しい感じでドキドキするね。いろんなデータに対応できるところが未来っぽい！

**Comment:** Work in progress

**トピック:** [連合学習](fl), **カテゴリ:** eess.SP, cs.LG, stat.ML, **投稿日時:** 2024-05-28 05:20

- - -

### [Post-Fair Federated Learning: Achieving Group and Community Fairness in Federated Learning via Post-processing](http://arxiv.org/abs/2405.17782)

**フェアネス後処理型連合学習：後処理による連合学習におけるグループおよびコミュニティフェアネスの実現**

Yuying Duan, Yijun Tian, Nitesh Chawla, Michael Lemmon

- 連合学習（FL）は、複数のコミュニティがデータをローカルに保持したままで共有モデルを学習する枠組み
- グループフェアネスとコミュニティフェアネスの2つのフェアネス概念が重要な問題として浮上
- 本論文はポスト処理型連合学習（post-FFL）というフレームワークを提案し、両フェアネスを同時に実現
- 菌質系モデルの使用実験で、従来の方法より高いフェアネスと効率的な通信・計算コストを達成

新しいフェアネスの実現方法が提案されていて、特に医療ネットワークで使えそうなのが面白いね！こういう具体的な応用例があると、現実に近い感じがしてワクワクするよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CY, **投稿日時:** 2024-05-28 03:26

- - -

### [Wireless Federated Learning over Resource-Constrained Networks: Digital versus Analog Transmissions](http://arxiv.org/abs/2405.17759)

**リソース制約されたネットワークにおける無線連合学習: デジタル伝送とアナログ伝送の比較**

Jiacheng Yao, Wei Xu, Zhaohui Yang, Xiaohu You, Mehdi Bennis, H. Vincent Poor

- デジタルとアナログの伝送方式を、デバイスの不均衡なサンプリングや厳しい遅延目標、送信電力制約の下で比較
- デジタル方式は通信設計をFLの計算タスクから分離し、大量のデバイスからの上り伝送は難しく主に通信に制約される
- アナログ通信はエアコンピューティング(AirComp)を可能にし、スペクトラム利用効率を改善
- 計算指向のアナログ伝送は電力効率が低く、CSIの不完全さから計算誤差に敏感である

デジタルとアナログの伝送方式、どっちが良いんだろうって悩むよね！だけど、それぞれの特性をフルに活かせればもっといい結果が出せそうだよね。

**Comment:** Accepted by IEEE TWC. arXiv admin note: text overlap with   arXiv:2402.09657

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, math.IT, **投稿日時:** 2024-05-28 02:23

- - -

### [ORLM: Training Large Language Models for Optimization Modeling](http://arxiv.org/abs/2405.17743)

**ORLM: 最適化モデリングのための大規模言語モデルの訓練**

Zhengyang Tang, Chenyu Huang, Xin Zheng, Shixi Hu, Zizhuo Wang, Dongdong Ge, Benyou Wang

- 現行のメソッドはプロンプトエンジニアリングに強く依存し、データプライバシーの懸念がある
- オープンソースLLMを訓練して最適化モデリングを行うことを提案
- OR-Instructという合成データ作成プロセスを設計し、特定の要件に対応
- 最適なORLMがIndustryORを含む各種ベンチマークで最先端のパフォーマンスを達成

これ、オープンソースでプライバシー問題をクリアするのはすごく革新的だよね！最適化モデリングの新基準を作るかも！

**Comment:** Work in progress

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.CE, cs.LG, **投稿日時:** 2024-05-28 01:55

- - -

### [ClavaDDPM: Multi-relational Data Synthesis with Cluster-guided Diffusion Models](http://arxiv.org/abs/2405.17724)

**ClavaDDPM: クラスター誘導拡散モデルを用いた多関係データ合成**

Wei Pang, Masoumeh Shafieinejad, Lucy Liu, Xi He

- 単一テーブルではなく、多くの相互接続されたテーブルを伴う複雑なデータ合成に焦点
- 従来の方法は、大規模データセットのスケーラビリティとテーブル間の長距離依存性の捕捉に欠けている
- ClavaDDPMはクラスタリングラベルを中間項として使用し、特に外部キー制約を重視
- 広範な評価により、長距離依存関係の捕捉で既存の方法を大幅に上回り、単一テーブルデータでも競争力を維持

多関係データの合成で、こんなにスゴイ進展ってヤバくない？複雑なデータそのまま扱えちゃう未来が楽しみ～！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-05-28 00:42

- - -

### [P4: Towards private, personalized, and Peer-to-Peer learning](http://arxiv.org/abs/2405.17697)

**P4：プライベートでパーソナライズされたピア・ツー・ピア学習に向けて**

Mohammad Mahdi Maheri, Sandra Siby, Ali Shahin Shamsabadi, Sina Abdollahi, Anastasia Borovykh, Hamed Haddadi

- 個々のクライアントがデータのプライバシーを保ちながらパーソナライズされたモデルを受け取る方法を開発
- クライアントをプライベートなピア・ツー・ピア(P2P)方式でグループ化する軽量なアルゴリズムを設計
- 差分プライバシーを保ちながら知識蒸留を用いて協同訓練、精度の影響を最小限に抑える
- 3つのベンチマークデータセットで評価し、最新の差分プライバシーP2P学習よりも最大40%精度が向上

パーソナライズされた学習がデータのプライバシーを守りつつP2Pで行われるなんて、すっごく未来的で期待できない？どんなデバイスでも実装できるところもかなり実用的だよね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-27 23:04

- - -

### [Data-Driven Personalized Energy Consumption Range Estimation for Plug-in Hybrid Electric Vehicles in Urban Traffic](http://arxiv.org/abs/2405.17654)

**データ駆動型パーソナライズドした都市交通におけるプラグインハイブリッド車のエネルギー消費範囲推定**

Mehmet Fatih Ozkan, James Farrell, Marcello Telloni, Luis Mendez, Radu Pirvan, Jeffrey P. Chrstos, Marcello Canova, Stephanie Stockar

- 都市交通におけるドライバーの行動がエネルギー消費に大きく影響
- ドライバーの行動とエネルギー使用の関係性を定量的に評価
- CQRを用いて燃料消費の不確実性を含む予測範囲を提供
- ドライバーデータと合成データを用いてモデルを訓練し評価

この研究、ドライバーの個々の行動に基づいたエコドライブ法の提案が面白そう！実際にどれぐらいの燃費改善が期待できるか知りたいよね。



**トピック:** [合成データ](sd), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-05-27 20:54

- - -

### [Calibrated Dataset Condensation for Faster Hyperparameter Search](http://arxiv.org/abs/2405.17535)

**ハイパーパラメータ検索を加速するキャリブレーションされたデータセット凝縮**

Mucong Ding, Yuancheng Xu, Tahseen Rabbani, Xiaoyu Liu, Brian Gravelle, Teresa Ranadive, Tai-Ching Tuan, Furong Huang

- データセットの凝縮は、大規模データセットで複数のモデルをトレーニングする計算コストを削減する
- 現状のアプローチでは、実データと合成データのモデル勾配を一致させるが、一般化保証がない
- ハイパーパラメータ検索に特化した新たな凝縮目標を考慮し、合成検証データを生成する
- 提案するHCDCアルゴリズムは、効率的な逆ヘッセ行列近似などによりパフォーマンス比較を維持し、検索を高速化する

新しいHCDCアルゴリズムってどんな風に効率良く動くんだろう？実際に使ってみたら、どれくらい早くなるか試してみたいよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, stat.ML, **投稿日時:** 2024-05-27 17:55

- - -

### [Efficient Model Compression for Hierarchical Federated Learning](http://arxiv.org/abs/2405.17522)

**階層型連合学習のための効率的なモデル圧縮**

Xi Zhu, Songcan Yu, Junbo Wang, Qinglin Yang

- 連合学習は、データ共有を避けつつモデルパラメータを共有することでプライバシーを維持
- モバイル・エッジコンピューティング環境での通信資源の消費が、モデルサイズ増大に伴い問題化
- 新規の階層型連合学習フレームワークと適応クラスタリングアルゴリズムを提案
- 提案アルゴリズムは予測精度を保ちながら、既存の連合学習手法よりエネルギー消費を大幅に削減

モデル圧縮とクラスタリングを融合させた連合学習の効率化、すごく革新的だよね。これで通信量の削減が叶えば、もっとエコでスマートな学習が広がりそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-27 12:17

- - -

### [Secure Hierarchical Federated Learning in Vehicular Networks Using Dynamic Client Selection and Anomaly Detection](http://arxiv.org/abs/2405.17497)

**車両ネットワークにおける動的クライアント選択と異常検出を用いた安全な階層型連合学習**

M. Saeid HaghighiFard, Sinem Coleri

- 階層型連合学習は、悪意のある車両による誤った更新でモデルの整合性が損なわれる問題に直面している
- 新しいフレームワークを提案し、動的車両選択と異常検出メカニズムを統合することでリスクを軽減
- 過去の性能、貢献頻度、異常記録を考慮した包括的な車両の信頼性評価を行う
- シミュレーション評価により、提案手法が攻撃下でも高いレジリエンスを示し、最悪のシナリオでも63%の収束時間を達成する

これ、車両ネットワークでの連合学習をさらに安全にするアイディアがいっぱいって感じね。異常検出の仕組みとかめちゃ面白そうじゃない？結果がアツい感じする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.SY, eess.SY, **投稿日時:** 2024-05-25 18:31

- - -

### [Vertical Federated Learning for Effectiveness, Security, Applicability: A Survey](http://arxiv.org/abs/2405.17495)

**効果、安全性、適用性のための垂直連合学習: 調査**

Mang Ye, Wei Shen, Eduard Snezhko, Vassili Kovalev, Pong C. Yuen, Bo Du

- 垂直連合学習（VFL）は、プライバシーを保護しつつ異なるパーティが協力してモデルを学習する手法である
- 最近の研究は、VFLにおける課題を克服し、実用的なクロスドメイン協力の可能性を示している
- 本調査では、VFLの歴史、背景、一般的なトレーニングプロトコルの概要を提供しつつ、最近のレビューの分類法とその限界を分析
- 効果、安全性、適用性の三つの視点から最近の研究を総合し、将来の重要な研究方向を議論

VFLっておもしろそう！将来的には、もっと多分野での協力が進んでいきそうだね。最新の研究をまとめてくれるのって助かるよね！

**Comment:** 31 pages, 9 figures, 10 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-25 16:05

- - -

### [Revisit, Extend, and Enhance Hessian-Free Influence Functions](http://arxiv.org/abs/2405.17490)

**ヘッセン自由影響関数の再訪、拡張、および強化**

Ziao Yang, Han Yue, Jian Chen, Hongfu Liu

- 影響関数は、サンプルの影響評価に重要であり、モデル解釈やトレーニングセット選択、ラベルの誤り検出に役立つ
- 深層モデルへの適用には困難があり、非凸損失関数や大規模なモデルパラメータが主な要因
- TracInという単純な近似手法を再訪し、ヘッセン行列の逆行列を単位行列で代用するアプローチを検証
- 公平性と堅牢性の観点を追加し、合成データと大規模言語モデルのフィンチューニングで有効性を実証

非凸損失関数って本当に難しそうだから、TracInのアプローチはかなり画期的だよね。未来のAI研究に役立つかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-05-25 03:43

- - -

### [Federated Offline Policy Optimization with Dual Regularization](http://arxiv.org/abs/2405.17474)

**二重正則化を用いた連合型オフライン政策最適化**

Sheng Yue, Zerui Qin, Xingyuan Hua, Yongheng Deng, Ju Ren

- 連合強化学習（FRL）は、人工物のインターネット時代における知的意思決定の有望な解決策である
- 既存のFRL手法は、ローカル更新の際に環境と繰り返し相互作用する必要があり、現実世界では高コストまたは不可能なことが多い
- これを克服するため、環境と相互作用せずにプライベートかつ静的なデータから意思決定を学ぶ新しいアルゴリズム$\texttt{DRPO}$を提案
- $\texttt{DRPO}$は二重正則化を活用し、ローカルの行動方針とグローバルの集約方針の2つを統合して分布のシフトに対処、理論分析によりパフォーマンス向上を確認

新しいFRLアルゴリズムで環境との相互作用を省くとかすごいね！今後、いろんな分野で応用されそうでワクワクするね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-24 04:24

- - -

### [Momentum-Based Federated Reinforcement Learning with Interaction and Communication Efficiency](http://arxiv.org/abs/2405.17471)

**モーメンタムベースの連合強化学習による相互作用と通信効率の向上**

Sheng Yue, Xingyuan Hua, Lili Chen, Ju Ren

- 連合強化学習（FRL）は注目されているが、データ分布の時空間的非定常性で高い相互作用と通信コストが課題
- モーメンタム、重要度サンプリング、サーバー側調整を利用した新アルゴリズム\alg{}を提案
- モーメンタムパラメータと相互作用頻度の適切な選定により、相互作用と通信の複雑度が大幅に改善
- 実験により、複雑かつ高次元のベンチマークで既存手法を大幅に上回る性能向上を確認

FRLで通信コストを減らせるって期待持てるね！みんなで協力して学習するともっと賢くなれるのかな、ワクワク♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-24 03:23

- - -

### [Distributed Continual Learning](http://arxiv.org/abs/2405.17466)

**分散連続学習**

Long Le, Marcel Hussing, Eric Eaton

- 独立したエージェントがそれぞれの環境でユニークなタスクに取り組み、知識を徐々に共有する。
- 分散連続学習の本質を捉える数学的フレームワークを紹介し、エージェントモデルや統計的異質性、継続的分布シフト、ネットワークトポロジー、通信制約を含む。
- 情報交換のモードをデータインスタンス、フルモデルパラメータ、モジュラーパラメータの3つに分類し、それぞれのアルゴリズムを開発。
- 複数のデータセット、トポロジー構造、通信制約を通じた実験で、モジュラーパラメータの共有が最も効率的で、共有モードの組み合わせが累積的な性能向上をもたらすことを明らかに。

エージェント同士が協力し合って学習するなんて、すごく面白そうだね！もしその技術が普及したら、みんなもっと効率的に賢くなれるかもね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.MA, **投稿日時:** 2024-05-23 21:24

- - -

### [Ferrari: Federated Feature Unlearning via Optimizing Feature Sensitivity](http://arxiv.org/abs/2405.17462)

**Ferrari: フェデレーテッド特徴忘却を特徴感度の最適化を通じて**

Hanlin Gu, WinKent Ong, Chee Seng Chan, Lixin Fan

- フェデレーテッドラーニングでは「忘れられる権利」が重要で、ユーザーがデータ削除を要求できる必要がある
- 現行の方法は他のクライアントの協力が必要なため非現実的であり、特徴忘却の有効性評価が欠けている
- 本研究では、特徴感度を定義し、リプシッツ連続性に基づく特徴忘却の評価指標を提案
- 提案したフレームワーク「Ferrari」は特徴感度を最小化し、多様な特徴忘却シナリオで効果的であることを実証

新しい方法で解決策を見つけるのってすごく楽しみだね！クライアント同士の協力がいらないのも便利そうだし、もっと広く使われる未来が見えてきた感じ。

**Comment:** 9 pages of main paper

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-23 07:20

- - -

### [Data-Free Federated Class Incremental Learning with Diffusion-Based Generative Memory](http://arxiv.org/abs/2405.17457)

**拡散ベースの生成メモリを用いたデータフリーフェデレーテッドクラスインクリメンタル学習**

Naibo Wang, Yuchen Deng, Wenjie Feng, Jianwei Yin, See-Kiong Ng

- 既存技術はGANを用いるが、不安定で高感度であり効果を損なう
- 新たに拡散モデルを使用して高品質な画像を生成し、破滅的忘却を軽減する手法を提案
- 非IID問題を緩和するためのバランスサンプラーと、生成サンプルの品質を向上させるエントロピーベースのサンプルフィルタリング技術を導入
- ベースラインのFedAvg方法と比較して追加の通信コストを発生させず、多くのデータセットで平均精度を4%向上させた

拡散モデル使って安定した画像生成するなんて面白いね！エントロピーベースのフィルタリング技術もぜひ試してみたいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.DC, cs.LG, **投稿日時:** 2024-05-22 20:59

- - -

### [Semi-Federated Learning for Internet of Intelligence](http://arxiv.org/abs/2405.17453)

**インターネット・オブ・インテリジェンスのためのセミ連合学習**

Wanli Ni, Zhaohui Yang

- 大規模なIoTネットワークでのデータとデバイスの異質性に対応するため、SemiFLフレームワークを導入
- SemiFLでは、計算資源が十分なユーザのみがローカルモデルをトレーニングし、残りのユーザは生データを基地局に送信
- 次世代のマルチアクセス方式では、通信と計算を一体化し効率的なスペクトラム利用を実現
- リコンフィギャラブルインテリジェントサーフェスと無線エネルギー転送技術で、バンド幅とエネルギーが制約されたIoTネットワークの性能向上を図る

次世代IoTのための新しい学習フレームワークなんてワクワクする！未来のスマートシティや自動運転車でこの技術がどう活躍するか楽しみ〜

**Comment:** 8 pages, submitted to IEEE magazines

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.SY, eess.SY, **投稿日時:** 2024-05-22 11:53
