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

更新: 2024-09-21T04:20:19.232861

- - -

### [Qwen2.5-Coder Technical Report](http://arxiv.org/abs/2409.12186)

**Qwen2.5-Coderテクニカルレポート**

Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Kai Dang, An Yang, Rui Men, Fei Huang, Xingzhang Ren, Xuancheng Ren, Jingren Zhou, Junyang Lin

- 5.5兆トークン以上のコーパスを用いて事前学習されたQwen2.5アーキテクチャに基づく
- Qwen2.5-Coder-1.5BとQwen2.5-Coder-7Bの2つのモデルを含む
- 綿密なデータクリーニング、合成データ生成、データ混合により高い汎用性を実現
- コード生成・完了・推論・修正など10以上のベンチマークでSOTA性能を達成

リアルな開発現場でも使えそうだし、プログラミングがもっと楽になりそう！新しい技術を試してみたいな～🎉



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-09-18 17:57

- - -

### [FedLF: Adaptive Logit Adjustment and Feature Optimization in Federated Long-Tailed Learning](http://arxiv.org/abs/2409.12105)

**FedLF: 連合長尾学習における適応ロジット調整と特徴最適化**

Xiuhua Lu, Peng Li, Xuefeng Jiang

- 連合学習は分散型機械学習におけるプライバシー問題を解決するパラダイム
- クライアント間のデータセットはヘテロであり、グローバル集約すると長尾分布になる場合が多い
- 従来の連合学習はクラス別バイアスを無視し、ヘッドクラスに焦点が当たりがち
- 提案するFedLFは適応ロジット調整、連続クラス中心の最適化、特徴の相関解除を導入

FedLFって、新しいアイデア満載で面白そう！特にデータの偏りまで考慮してるのがすごいよね。やってみたいな、この技術。

**Comment:** Accepted by ACML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-18 16:25

- - -

### [Artemis: Efficient Commit-and-Prove SNARKs for zkML](http://arxiv.org/abs/2409.12055)

**Artemis: zkML のための効率的なコミット・アンド・プルーフ SNARKs**

Hidde Lycklama, Alexander Viand, Nikolay Avramov, Nicolas Küchler, Anwar Hithnawi

- 機械学習の幅広い導入により、プライバシーや信頼性への懸念が増加
- zkML技術の発展により、敏感情報を明かさずMLモデルの検証が可能に
- 本論文では、zkMLパイプラインにおけるコミットメント検証の課題に取り組むため、2つの新しいCP-SNARK構造（ApolloとArtemis）を提案
- VGGモデルに対して、コミットメントチェックのオーバーヘッドを11.5倍から1.2倍に削減するなど、証明コストを大幅に削減

zkMLが実用化の一歩を踏み出すかも！大規模なMLモデルでも効率が保たれるのがすごいよね。未来が楽しみ～

**Comment:** 17 pages

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-18 15:30

- - -

### [Optimal Offline ORAM with Perfect Security via Simple Oblivious Priority Queues](http://arxiv.org/abs/2409.12021)

**単純なオブリビアス優先キューによる完全なセキュリティを備えた最適なオフラインORAM**

Thore Thießen, Jan Vahrenhold

- ORAMはRAM計算のメモリアクセスパターンを隠すための手法で、多岐にわたる応用がある
- この研究ではオフラインORAMを対象とし、メモリアクセスのシーケンスが事前に知られている
- 時間順処理を用いて完璧なセキュリティを持つオフラインORAMを初めて実現した
- 外部メモリに適用可能な効率的な実装方法を提案し、キャッシュ対応・非対応の両方で最適なI/O複雑性を達成

オフラインORAMの新しいアプローチ、とても興味深いよね！セキュリティと効率性を両立できるなんて、かなり画期的だと思うな。

**Comment:** 23 pages, full version of the paper to appear in ISAAC 2024

**トピック:** [秘密計算](mpc), **カテゴリ:** cs.DS, cs.CR, **投稿日時:** 2024-09-18 14:31

- - -

### [Promise and Peril of Collaborative Code Generation Models: Balancing Effectiveness and Memorization](http://arxiv.org/abs/2409.12020)

**協働コード生成モデルの約束と危険：有効性と記憶化のバランス**

Zhi Chen, Lingxiao Jiang

- 隠密データセットから知識を引き出す協働的な訓練が重要である
- 中央集権化、連合学習、逐次訓練のリスクとデータリークの可能性を評価
- データセットのサイズと多様性が協働的訓練の成功に決定的な因子
- クロスオーガナイゼーションクローンが中央と連合学習の両方で課題として現れる

協働的なコード生成って面白そう！データ保護しながらも高性能なモデルができるって、未来の開発がもっと安全で効率的になるかも！

**Comment:** Paper accepted to the ASE 2024 Conference Research Track

**トピック:** [連合学習](fl), **カテゴリ:** cs.SE, cs.AI, cs.LG, **投稿日時:** 2024-09-18 14:30

- - -

### [Efficacy of Synthetic Data as a Benchmark](http://arxiv.org/abs/2409.11968)

**合成データのベンチマークとしての有効性**

Gaurav Maheshwari, Dmitry Ivanov, Kevin El Haddad

- LLMを用いた合成データは、意図分類などの簡単なタスクでは有効である
- 複雑なタスク（例：固有表現抽出）の場合、合成データの有効性は低下する
- バイアスファクターという新しい指標を提案し、同じLLM使用によるバイアスを評価
- 小型LLMは自分の生成したデータにバイアスを示すが、大型モデルはそうではない

合成データの評価がタスクによって異なるのが興味深いね。大規模モデルの重要性も改めて感じたよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-09-18 13:20

- - -

### [What to Consider When Considering Differential Privacy for Policy](http://arxiv.org/abs/2409.11680)

**プライバシーポリシー策定時に考慮すべき差分プライバシーに関する要点**

Priyanka Nanayakkara, Jessica Hullman

- 差分プライバシー（DP）はデータ公開時に広く適用できる数学的プライバシー定義
- DPは多様なプライバシー関連法規制への適合手段として認識される
- 理論から実践に移す際に生じる緊張から、DPの適用の適切さを判断するのが難しい
- プライバシー懸念に対する政策策定を支援するための3つのカテゴリーの課題と関連する質問を特定

差分プライバシーを理論から実践に移すのって、結構チャレンジングなんだね。それが政策に役立つように、具体的な質問も含めて整理されてるところが素敵だな！

**Comment:** This paper is accepted for publication in Policy Insights from the   Behavioral and Brain Sciences (2024)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CY, cs.CR, **投稿日時:** 2024-09-18 03:41

- - -

### [GReDP: A More Robust Approach for Differential Privacy Training with Gradient-Preserving Noise Reduction](http://arxiv.org/abs/2409.11663)

**GReDP: 勾配保持ノイズ低減を用いたより堅牢な差分プライバシートレーニング手法**

Haodi Wang, Tangyu Jiang, Yu Guo, Xiaohua Jia, Chengjun Cai

- 深層学習のトレーニング過程とアルゴリズム保護がプライバシー保護において重要
- 従来の差分プライバシー手法は高ノイズスケールや勾配情報の損失が課題
- GReDPは周波数領域で勾配を計算しノイズレベルを低減、元の勾配情報を保持
- GReDPは実験的に全モデルとトレーニング設定で従来手法より一貫して優れている

この新しいGReDP、かなりすごいかも！ ノイズが半分でプライバシー守れるなんて、未来のAIトレーニングがもっと安心できそうだね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-09-18 03:01

- - -

### [Few-Shot Class-Incremental Learning with Non-IID Decentralized Data](http://arxiv.org/abs/2409.11657)

**非独立同分布分散データでの少数ショットクラス増分学習**

Cuiwei Liu, Siang Xu, Huaijun Qiu, Jing Zhang, Zhi Liu, Liang Zhao

- 少数ショットクラス増分学習は、最小限の注釈データで新しいクラスを学習し、既存の知識を保つ
- 連合少数ショットクラス増分学習を導入、分散環境で新しいクラスを学習
- ノイズ対応生成リプレイモジュールを用い、新旧データのバランスを取りつつ局所モデルを微調整
- クラス固有の重み付き集約戦略でデータの異質性に対応し、効果的なグローバルモデル最適化

この研究、すごく面白そう！少ないデータでも新しいことをどんどん学べるとか、未来のAIって感じでワクワクするね！連合学習でプライバシーも守れるなんて、実用化が待ちきれないな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-18 02:48

- - -

### [A novel pedestrian road crossing simulator for dynamic traffic light scheduling systems](http://arxiv.org/abs/2409.11623)

**動的交通信号スケジューリングシステムのための新しい歩行者道路横断シミュレーター**

Dayuan Tan, Mohamed Younis, Wassila Lalouani, Shuyao Fan, Guozhi Song

- 歩行者の体験が十分に考慮されていないが、信号交差点は都市部で重要
- シミュレーターは詳細なレベルでの信号付き横断歩道における人間の動きを再現
- 大規模な歩行者集団の行動を扱い、最適な道路構成管理に貢献
- 実験データに基づき98.37%の精度で横断時間を推定、信号待ち時間も削減

都市に繰り出すのが楽しみになるね。未来の交差点、ストレスなく歩けるなんて嬉しいことばかりじゃない？



**トピック:** [合成データ](sd), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-09-18 01:01

- - -

### [Blockchain-Enabled IoV: Secure Communication and Trustworthy Decision-Making](http://arxiv.org/abs/2409.11621)

**ブロックチェーン対応のIoV：安全な通信と信頼できる意思決定**

Jingyi Sun, Qi Shi, Guodong Jin, Hao Xu, Erwu Liu

- 車両間、インフラ、および環境との相互作用を実現するIoVが対象
- 通信の安全性と信頼できる自動化された意思決定が課題
- ブロックチェーンベースのプロトコルBiSAとDBNRを実装
- 安全で分散型のアイデンティティ管理とデータ交換を実現し、自動運転車の運用をサポート

自動運転車の世界って夢があるよね！ブロックチェーンで車と車が会話するなんて、サイバーパンクみたいでワクワクする。未来の道路はもっと安全になるかも。

**Comment:** The 2024 7th IEEE Conference on Dependable and Secure Computing

**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.CR, cs.DC, cs.NI, **投稿日時:** 2024-09-18 00:56

- - -

### [The Sample Complexity of Smooth Boosting and the Tightness of the Hardcore Theorem](http://arxiv.org/abs/2409.11597)

**スムースブースティングのサンプル複雑性とハードコア定理の厳密性**

Guy Blanc, Alexandre Hayderi, Caleb Koch, Li-Yang Tan

- スムースブースターは、差分プライバシーや量子学習理論に応用される技術である
- 弱学習が$m$サンプルで可能なクラスを示し、強学習には$\tilde{\Omega}(1/\gamma^2)\cdot m$サンプルが必要
- これは既存のスムースブースターのオーバーヘッドと一致し、分配独立ブースティングとの初の分離を提供
- ハードコア定理の既知の証明はスムースブースティングの枠組みで理解可能、サイズ損失が不可避であることを証明

サンプル数の話とかすごく複雑そうだけど、スムースブースティングの分野で初の発見ってすごいことだよね！ハードコア定理にも関係してるから、幅広い応用が期待できそう！

**Comment:** 46 pages, FOCS 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CC, cs.DS, cs.LG, stat.ML, **投稿日時:** 2024-09-17 23:09

- - -

### [Advances in APPFL: A Comprehensive and Extensible Federated Learning Framework](http://arxiv.org/abs/2409.11585)

**APPFLの進展：包括的かつ拡張可能な連合学習フレームワーク**

Zilinghan Li, Shilan He, Ze Yang, Minseok Ryu, Kibaek Kim, Ravi Madduri

- 連合学習は、データプライバシーを保持しつつモデルを共同で訓練する分散型機械学習パラダイムである
- APPFLは、ヘテロジェネイティおよびセキュリティの課題に対応するための包括的なソリューションを提供する
- APPFLの能力は、通信効率、プライバシー保護、計算性能、リソース利用の各側面で評価されている
- APPFLの拡張性は、垂直、階層、および分散型連合学習におけるケーススタディを通じて示されている

新しいアルゴリズムとかを簡単に試せるフレームワークっぽいから、これからの連合学習がガンガン進みそう！オープンソースなのもいい感じだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-09-17 22:20

- - -

### [FedNE: Surrogate-Assisted Federated Neighbor Embedding for Dimensionality Reduction](http://arxiv.org/abs/2409.11509)

**FedNE: 代理支援連合近傍埋め込みによる次元削減**

Ziwei Li, Xiaoqi Wang, Hong-You Chen, Han-Wei Shen, Wei-Lun Chao

- 連合学習は、データを交換せずにモデルを共同で訓練する手法で、多くの分野で応用されている
- 近傍埋め込みは高次元データの視覚化に不可欠で、局所データを共有せずに共同でモデルを学習することが難しい
- FedNEは、FedAvgフレームワークと対照的な近傍埋め込み技術を統合し、代理損失関数を導入して全体の埋め込み空間での整合性を向上
- 提案手法は見えない隣接点と偽の隣接点の問題を解消するためにデータミキシング戦略を用いて効果を実証

この研究、すごく興味深いね！連合学習に視覚化技術を取り入れることで、新しい可能性が広がりそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-17 19:23

- - -

### [A Green Multi-Attribute Client Selection for Over-The-Air Federated Learning: A Grey-Wolf-Optimizer Approach](http://arxiv.org/abs/2409.11442)

**グレーウルフ最適化アプローチによるOTA連合学習のグリーンな多属性クライアント選択**

Maryam Ben Driss, Essaid Sabir, Halima Elbiaze, Abdoulaye Baniré Diallo, Mohamed Sadik

- 連合学習はプライバシー保護と通信オーバーヘッドの低減を特徴とする
- OTA連合学習はエネルギー消費とネットワーク遅延の課題を抱える
- GWOを用いて参加デバイスの属性を最適化し、OTA-FLプロセスを改善
- 実験結果はモデル損失の減少とエネルギー効率の向上を示し、既存手法を上回る

新しいアプローチでエネルギー効率がこんなに上がるのはすごいね！これでどれだけ未来の連合学習が進化するか楽しみ～



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-09-16 20:03

- - -

### [Federated Learning with Quantum Computing and Fully Homomorphic Encryption: A Novel Computing Paradigm Shift in Privacy-Preserving ML](http://arxiv.org/abs/2409.11430)

**量子コンピューティングと完全準同型暗号を用いた連合学習：プライバシー保護型機械学習における新たな計算パラダイムシフト**

Siddhant Dutta, Pavana P Karanth, Pedro Maciel Xavier, Iago Leal de Freitas, Nouhaila Innan, Sadok Ben Yahia, Muhammad Shafique, David E. Bernal Neira

- 機械学習モデルの普及に伴い、データプライバシーと情報セキュリティの懸念が増大
- 連合学習は、プライベートデータを共有せずにモデル知識を共有するための代替手段
- 完全準同型暗号（FHE）は、暗号化された重みへの操作を可能にする量子安全な暗号システム
- 本研究は、FHEスキームを連合学習ニューラルネットワークに適用し、古典レイヤーと量子レイヤーを統合

量子コンピューティングと連合学習の組み合わせができるんだね！これって、新しいプライバシー保護技術をどのように現実に応用できるか知るための素晴らしいステップじゃない？また話しましょう！



**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** quant-ph, cs.AI, cs.CR, cs.LG, cs.NE, **投稿日時:** 2024-09-14 01:23

- - -

### [Generated Data with Fake Privacy: Hidden Dangers of Fine-tuning Large Language Models on Generated Data](http://arxiv.org/abs/2409.11423)

**生成データによる偽りのプライバシー: 大規模言語モデルの生成データによるファインチューニングの隠れた危険性**

Atilla Akkus, Mingjie Li, Junjie Chu, Michael Backes, Yang Zhang, Sinem Sav

- 実世界データでのファインチューニングはプライバシーリスクを伴う
- 仮想データを用いたファインチューニングもプライバシーリスクを引き起こす可能性がある
- 生成データでのファインチューニング後、PIIの抽出成功率が20%以上上昇
- メンバーシップ推論攻撃のROC-AUCスコアが40%以上改善

生成データでもプライバシーリスクがあるんだね〜。これは新しい視点で興味深い！次はどうやってリスク低減できるか気になるなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-09-12 10:14
