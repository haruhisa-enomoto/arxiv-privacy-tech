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

更新: 2024-06-27T04:21:36.309549

- - -

### [Denoising as Adaptation: Noise-Space Domain Adaptation for Image Restoration](http://arxiv.org/abs/2406.18516)

**適応としてのデノイジング: 画像復元のためのノイズ空間ドメイン適応**

Kang Liao, Zongsheng Yue, Zhouxia Wang, Chen Change Loy

- 既存の手法はデータ合成パイプラインの改善やドメイン適応などで対応しているが、実用場面での一般化が難しい
- 拡散モデルを用いてノイズ空間を介してドメイン適応を行う手法を提案
- チャンネルシャッフリングや残差交換コントラスト学習など、トレーニング中のショートカット防止技術を提示
- デノイジング、デブラー、デレイニングの3つの古典的な画像復元タスクで有効性を実証

新しい手法で画像をきれいにするなんてワクワクするね！これで現実のシーンでももっと鮮明な画像が得られるようになるかも。

**Comment:** Github Repository: https://github.com/KangLiao929/Noise-DA/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-26 17:40

- - -

### [Enhancing Federated Learning with Adaptive Differential Privacy and Priority-Based Aggregation](http://arxiv.org/abs/2406.18491)

**適応差分プライバシーと優先順位ベースの集約による連合学習の強化**

Mahtab Talaei, Iman Izadi

- 連合学習はローカルデータセットなしでグローバルモデルを開発
- モデル更新の取得が情報漏洩の可能性を含む、モデルインバージョン攻撃のリスク
- 差分プライバシーによりパラメータにノイズを追加しプライバシーを保護
- デバイス間の異質性を考慮し、時間的に変動する影響因子で収束性を向上

デバイスごとのリソース差を考慮したカスタマイズされたプライバシー保護、革新的ね！未来のFLはますます強力になりそう。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-06-26 16:55

- - -

### [Blockchain Based Zero-Knowledge Proof of Location in IoT](http://arxiv.org/abs/2406.18389)

**IoTにおけるブロックチェーン基盤のゼロ知識証明を用いた位置証明**

Wei Wu, Erwu Liu, Xinglin Gong, Rui Wang

- 精密な位置決定技術の発展により、多くの位置情報サービス（LBS）が人々の生活を便利にしている
- LBSでは位置証明（PoL）を要求し、ユーザーのプライバシーが露出する問題がある
- ゼロ知識証明を用いた位置証明プロトコル（zk-PoL）を提案、ユーザーは必要な情報のみをサーバーに公開可能
- zk-PoLは主要な攻撃に対する優れたセキュリティを持ち、計算効率は入力パラメータに依存せず、遅延耐性のあるLBSに適している

zk-PoLの登場で、もっと安心して位置情報サービスが使えるようになるかもね！未来のLBSの進化にワクワクするね～。

**Comment:** Published on ICC 2020-2020 IEEE International Conference on   Communications (ICC)

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-26 14:30

- - -

### [Effects of Using Synthetic Data on Deep Recommender Models' Performance](http://arxiv.org/abs/2406.18286)

**合成データが深層推薦モデルの性能に与える影響**

Fatih Cihan Taskin, Ilknur Akcay, Muhammed Pesen, Said Aldemir, Ipek Iraz Esin, Furkan Durmus

- 推薦システムはデータの不均衡に直面しやすく、人気アイテムに偏ることが多い
- データの不均衡に取り組むために、6つの方法で合成データを生成
- 合成データを元のデータセットに統合すると、AUCスコアが一貫して向上
- 合成データによるデータ増強がデータの希薄化と不均衡を緩和し、推薦システムの性能を改善

合成データがこんなふうに役立つなんて、面白いね。データバランスが取れると、もっと精度の高い推薦ができそうでワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.IR, **投稿日時:** 2024-06-26 12:14

- - -

### [Generative artificial intelligence in ophthalmology: multimodal retinal images for the diagnosis of Alzheimer's disease with convolutional neural networks](http://arxiv.org/abs/2406.18247)

**眼科における生成的人工知能: アルツハイマー病診断のための多モーダル網膜画像と畳み込みニューラルネットワーク**

I. R. Slootweg, M. Thach, K. R. Curro-Tafili, F. D. Verbraak, F. H. Bouwman, Y. A. L. Pijnenburg, J. F. Boer, J. H. P. de Kwisthout, L. Bagheriye, P. J. González

- マルチモーダル網膜イメージングとCNNを用いてAmyloidPETステータスを予測
- 合成データでの事前学習によって性能向上を目指す
- DDPMsが多様でリアルな画像生成に成功し、事前学習でAUPRが向上
- 最良のマルチモーダルCNNはメタデータ統合でAUPRが0.634に改善

マルチモーダルイメージングでアルツハイマー病の早期発見が一段と進みそうでワクワクするね！また、生成データを使った事前学習の新たな可能性も広がってて、今後の展開が楽しみだな。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, cs.LG, **投稿日時:** 2024-06-26 10:49

- - -

### [FedAQ: Communication-Efficient Federated Edge Learning via Joint Uplink and Downlink Adaptive Quantization](http://arxiv.org/abs/2406.18156)

**FedAQ: 共同アップリンクおよびダウンリンク適応量子化による通信効率の高い連合エッジ学習**

Linping Qu, Shenghui Song, Chi-Ying Tsui

- 連合学習(FL)はクライアントのデータプライバシーを保護しつつ、データと計算資源を活用する
- モデルサイズの大きさと頻繁な集約が通信オーバーヘッドの原因となり、リソース制限のある無線ネットワークでの展開が難しい
- 本研究では量子化を用いて通信オーバーヘッドを軽減し、最適なアップリンクおよびダウンリンク量子化ビット長を決定
- 提案手法により既存のスキームと比較して最大66.7%のエネルギー節約が可能

通信効率をこんなに上げられるのはすごいね！アップリンクとダウンリンクの両方に適応できる新しい量子化手法、未来のネットワークで大活躍しそう！

**Comment:** This work has been submitted to the IEEE for possible publication.   Copyright may be transferred without notice, after which this version may no   longer be accessible

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.NI, eess.SP, **投稿日時:** 2024-06-26 08:14

- - -

### [SynRS3D: A Synthetic Dataset for Global 3D Semantic Understanding from Monocular Remote Sensing Imagery](http://arxiv.org/abs/2406.18151)

**SynRS3D: 単眼リモートセンシング映像からのグローバルな3Dセマンティック理解のための合成データセット**

Jian Song, Hongruixuan Chen, Weihao Xuan, Junshi Xia, Naoto Yokoya

- 単眼の高解像度リモートセンシング画像からのグローバルなセマンティック3D理解は重要、しかし注釈とデータ収集のコストが高い
- 合成データは容易にアクセスできるため、大規模で多様なデータセットの提供が可能
- SynRS3Dは69,667枚の高解像度光学画像を含み、六つの異なる都市スタイルと八つの土地被覆タイプが含まれる
- 合成データからリアルなシナリオへの移行を支援するため、新しいマルチタスク無監督ドメイン適応法RS3DAdaを開発

地球観測の未来がどんどん広がっていく感じがする！実験結果も良好みたいだし、現実でも使えるかもね。伝統的な方法から新しい手法への転換を見るのはワクワクするよねー。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-26 08:04

- - -

### [Beyond Statistical Estimation: Differentially Private Individual Computation in the Shuffle Model](http://arxiv.org/abs/2406.18145)

**統計推定を超えて：シャッフルモデルにおける差分プライバシーのための個別計算**

Shaowei Wang, Changyu Dong, Di Wang, Xiangfu Song

- シャッフルモデルは非信頼当事者間での非集中型計算で威力発揮し、匿名化とメッセージの順序入れ替えによりプライバシーと有用性を向上
- 従来の手法で計算困難または有用性損失が大きい空間クラウドソーシング、組み合わせ最適化、位置ベースのソーシャルシステム、インセンティブ付き連合学習において、シャッフルプライバシー増幅の実現可能性を探る
- メッセージ認証や結果アクセス制御などの重要なセキュリティ機能を提供しつつ、プライバシー強化効果を維持する新たなシャッフルモデルを提案
- 実験結果: 非プライベート設定に対しエラー最大90％削減、100％-300％有用性向上し、適切なプライバシー予算で実用的

シャッフルモデルって、すごく面白そう！特に連合学習でこれだけ効果が出るなら、未来の技術革新に大いに貢献しそうだよね！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-06-26 07:53

- - -

### [A Communication Satellite Servises Based Decentralized Network Protocol](http://arxiv.org/abs/2406.18032)

**通信衛星サービスに基づく分散型ネットワークプロトコル**

Xiao Yan, Bernie Gao

- 通信衛星サービスに基づく分散型ネットワークプロトコルを提案
- 衛星通信サービスのステータス情報を全ブロックチェーンネットワークで分配
- PoD（Proof of Distribution）とPoF（Proof of Flow）を提案し、オンライン状態とデータフローを認証
- ゼロ知識証明とマルチパーティ暗号計算を使用し、不正があってもサービスパラメータを評価

これって宇宙通信の未来を見据えたプロトコルなんだね！技術的に難しそうだけど、めちゃワクワクする内容だよね。



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.DC, cs.NI, **投稿日時:** 2024-06-26 03:01

- - -

### [Explicit Diversity Conditions for Effective Question Answer Generation with Large Language Models](http://arxiv.org/abs/2406.17990)

**効果的な質問応答生成のための明示的な多様性条件についての研究**

Vikas Yadav, Hyuk Joon Kwon, Vijay Srinivasan, Hongxia Jin

- 質問応答生成（QAG）はデータ拡張技術で、特に低リソース領域での質問応答システムの精度向上に寄与
- 既存の暗黙的な多様性技術（サンプリング、多様なビームサーチ）は効果的だが、得られる多様性は小さい
- 空間的側面、質問タイプ、エンティティに焦点を当てた明示的な多様性条件を提示し、これによりQA生成の多様性が大幅に向上
- 明示的な多様性条件を用いたQAペアは、下流のQAモデルでの平均4.1%のEMと4.5%のF1の向上を示す

明示的な多様性条件を強調することで、特に低リソースデータセットでの性能向上が見込めるのが面白そう！

**Comment:** Published at COLING 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-06-26 00:12

- - -

### [Navigating High-Degree Heterogeneity: Federated Learning in Aerial and Space Networks](http://arxiv.org/abs/2406.17951)

**高い異質性への対応：航空・宇宙ネットワークにおける連合学習**

Fan Dong, Henry Leung, Steve Drew

- 連合学習はドローンや衛星を通じたデータプライバシー問題の解決策として有望
- しかし、異質性とクラス不均衡がモデルの収束を阻む主要な障害
- 異質性とクラス不均衡の相関を示し、バッテリー寿命の制約が課題をさらに悪化
- 異質性の度合いが大きいと現行アルゴリズムは効果的に対処できず性能が低下

宇宙や空のデータも連合学習で使えるってすごいことだよね！だけど、クラス不均衡の問題はもっとよく考えていかないといけないみたいね。技術が進化する未来に期待しちゃう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-25 21:57

- - -

### [Entity Augmentation for Efficient Classification of Vertically Partitioned Data with Limited Overlap](http://arxiv.org/abs/2406.17899)

**限定的な重複を持つ垂直分割データの効率的な分類のためのエンティティ拡張**

Avi Amalanshu, Viswesh Nagaswamy, G. V. S. S. Prudhvi, Yash Sirvi, Debashish Chakravarty

- 垂直連合学習（VFL）は、特徴が複数の「ゲスト」クライアント間で分散し、ラベルを所有する「ホスト」サーバと学習を行う
- 従来のVFLは、ホストが共通のエンティティを特定する「エンティティ解決」フェーズと、プライベートセットインターセクションを含む
- 提案されたエンティティ拡張技術は、明示的なエンティティ整列なしで有意義なラベルを生成し、効率的なVFLを実現
- CIFAR-10データセットで、訓練データの重複が5%の場合で48.1%から69.48%に精度向上、100%重複でもわずかに性能向上

エンティティ拡張って、新しいアイディアだね！VFLの効率が上がることで、将来もっと色々なデータを活用できそうでワクワクする！

**Comment:** GLOW @ IJCAI 2024 (12 pages + 2 page bibliography. 15 figures.)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, cs.DC, **投稿日時:** 2024-06-25 19:20

- - -

### [Federated Dynamical Low-Rank Training with Global Loss Convergence Guarantees](http://arxiv.org/abs/2406.17887)

**グローバル損失収束保証を持つ連合動的低ランクトレーニング**

Steffen Schotthöfer, M. Paul Laiu

- 連合学習におけるクライアントの計算および通信コストを低減するためのスキームを提案
- 動的低ランク分割スキームを用いてネットワーク重みのグローバル低ランク基底を作成
- クライアントのトレーニングが小さい係数行列で可能になり、計算リソースおよび通信リソースの最適化ができる
- コンピュータビジョンベンチマークで効率を実証し、コストを約10分の1に削減しつつ精度にほとんど影響を与えない

新しいけどすっごく素敵な研究だね！次のレポートで役立つ資料見つけちゃった。試すっきゃないね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, math.OC, **投稿日時:** 2024-06-25 18:51
