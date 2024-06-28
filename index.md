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

更新: 2024-06-28T04:19:31.698087

- - -

### [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](http://arxiv.org/abs/2406.19292)

**人工の針から本物の干し草の山へ：合成データで微調整した大規模言語モデルの情報検索能力の向上**

Zheyang Xiong, Vasilis Papageorgiou, Kangwook Lee, Dimitris Papailiopoulos

- 大規模言語モデル（LLMs）は長い文脈を処理する際に情報検索と推論能力が低下する
- 数値キーと値の検索タスクを含む合成データセットを用いた微調整アプローチを提案
- 合成データで微調整されたLLMsは情報検索と推論能力が大幅に向上（GPT-3.5 Turboで$10.5\%$の改善）
- 他の基準ベンチマークで性能がほぼ一定で、他のデータセットでは幻覚を引き起こす懸念がある

長い文脈処理の問題を合成データで解決するなんて面白い！もしかして、将来的にAIがもっと賢くなるキーポイントかも。ねぇ、もっと調べたいよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-06-27 16:05

- - -

### [Towards Reducing Data Acquisition and Labeling for Defect Detection using Simulated Data](http://arxiv.org/abs/2406.19175)

**欠陥検出のためのデータ収集とラベリングをシミュレートデータで削減する試み**

Lukas Malte Kemeter, Rasmus Hvingelby, Paulina Sierak, Tobias Schön, Bishwajit Gosswam

- 製造業ではデータのアノテーションコストが高く、合成データ生成が低コストである
- 合成データのみでは実際のデータに対するモデル学習が不十分、ドメインシフトの問題が重要
- アルミホイールのX線スキャン欠陥検出において、シミュレートデータと実データを組み合わせたアプローチを検討
- 合成データと未ラベル実データを用いる訓練戦略が、コスト効率が高く、良好な検出結果をもたらすと示唆

シミュレートデータで手軽にデータ集めできるなら、現場での負担も減りそうね。もっといろんな製造業に応用できそうでワクワクするよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-06-27 13:51

- - -

### [FedMap: Iterative Magnitude-Based Pruning for Communication-Efficient Federated Learning](http://arxiv.org/abs/2406.19050)

**FedMap: 連合学習における通信効率化のための反復的な重要度ベースのプルーニング**

Alexander Herzog, Robbie Southam, Ioannis Mavromatis, Aftab Khan

- 連合学習は分散されたデータでプライバシーを保ちながら機械学習を行う手法
- FedMapは無構造なプルーニングを用いて通信効率を向上させる新しい方法
- 医療や金融などプライバシーが重要な分野での利用を想定し、モデルを一から訓練
- IID環境で90%以上、非IID環境で80%以上のプルーニングを達成しつつ精度を維持

これ、すごく未来感あるね！プライバシーを守りつつ、効率的に学習できるって必須スキルかも！

**Comment:** Submitted to IEEE Transactions on Neural Networks and Learning   Systems

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-27 09:58

- - -

### [Towards Credential-based Device Registration in DApps for DePINs with ZKPs](http://arxiv.org/abs/2406.19042)

**ZKPsを用いたDePINs用DAppsにおける資格認証ベースのデバイス登録に向けて**

Jonathan Heiss, Fernando Castillo, Xinxin Fan

- DePINsはブロックチェーンによって保護・管理されるが、デバイスやサービスの信頼性を確立する手段が欠けている
- デバイス登録時の資格認証の確認はこの問題の解決策となるが、オンチェーン確認は機密属性を公開し、オフチェーン確認は望ましくない信頼を前提としている
- 本論文では、機密なデバイス属性を公開せずに資格認証をブロックチェーン上で確認するために、ZKPsを利用した資格認証ベースのデバイス登録（CDR）メカニズムを提案
- Groth16とMarlinを用いたzkSNARKsを使ってCDRを技術的に評価し、パフォーマンスへの初期の洞察と証明システム間のトレードオフを明らかにした

デバイスの信頼性を確保しながら機密情報を守る、ってすごいね！ZKPとブロックチェーンの組み合わせ、日本のデジタル社会にも影響ありそう。



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-06-27 09:50

- - -

### [VertiMRF: Differentially Private Vertical Federated Data Synthesis](http://arxiv.org/abs/2406.19008)

**VertiMRF: 差分プライバシーを利用した垂直連合データの合成**

Fangyuan Zhao, Zitao Li, Xuebin Ren, Bolin Ding, Shusen Yang, Yaliang Li

- 差分プライバシーにより合成データのプライバシー保護を実現
- Flajolet-Martinスケッチ技術でデータ属性間の相関を維持
- 垂直連合環境でのプライベートなマルコフ確率場(MRF)を生成
- 高次元属性のデータセットに対する次元削減と一貫性強制技術を導入

今回の研究は、連合学習のプライバシー問題に実践的解決策を示しているね。特に、垂直連合環境でのデータ保護に力を入れているところが面白そう！



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.DS, **投稿日時:** 2024-06-27 08:47

- - -

### [Coded Cooperative Networks for Semi-Decentralized Federated Learning](http://arxiv.org/abs/2406.19002)

**半分分散型連合学習のための符号化協力ネットワーク**

Shudi Weng, Ming Xiao, Mikael Skoglund

- フェデレーテッドラーニング（FL）システムの遅延耐性を強化するため、半分分散型アプローチを提案
- 提案手法はネットワーク全体の事前情報を必要とせず、ワイヤレス多様性を活用
- アウトエイジと収束速度の理論解析を提供
- ベンチマーク手法に比べて優れていることを、包括的なシミュレーションで実証

ネットワーク全体の事前情報がいらないのが新しいかも！シミュレーション結果も見てみたいなって思う！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, math.IT, **投稿日時:** 2024-06-27 08:42

- - -

### [FedMLP: Federated Multi-Label Medical Image Classification under Task Heterogeneity](http://arxiv.org/abs/2406.18995)

**FedMLP: 連合学習によるタスク異質性下でのマルチラベル医用画像分類**

Zhaobin Sun, Nannan Wu, Junjie Shi, Li Yu, Xin Yang, Kwang-Ting Cheng, Zengqiang Yan

- クロスサイロ連合学習は、データプライバシーを守りつつ分散型組織が共同でモデルを訓練する方法
- 臨床実践では、各機関が部分的なカテゴリしか診断しないため、タスク異質性が生じる
- FedMLPは、欠損ラベル補充のために擬似ラベル付けとグローバル知識学習の二段階法を提案
- 実験では、FedMLPが連合型半教師あり学習およびノイズラベル学習アプローチを上回る結果を示す

これかなり実践的な研究っぽいね！タスク異質性を考慮した医療画像の連合学習、将来もっと活躍しそう！

**Comment:** Early accepted by MICCAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-27 08:36

- - -

### [UniGen: A Unified Framework for Textual Dataset Generation Using Large Language Models](http://arxiv.org/abs/2406.18966)

**UniGen: 大規模言語モデルを用いたテキストデータセット生成の統一フレームワーク**

Siyuan Wu, Yue Huang, Chujie Gao, Dongping Chen, Qihui Zhang, Yao Wan, Tianyi Zhou, Xiangliang Zhang, Jianfeng Gao, Chaowei Xiao, Lichao Sun

- GPT-4やLlama3は高品質な合成データ生成で重要な役割を果たしている
- UniGenは多様性、正確性、高い制御性を持つデータセットを生成するフレームワーク
- 属性ガイド生成モジュールとグループチェック機能がデータの多様性を向上
- 特定の要件に合わせてデータ生成をカスタマイズ可能で、様々な分野での応用に有効

このフレームワーク、めっちゃ役に立ちそう！特にデータのカスタマイズができるところとか、使い勝手良さそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-27 07:56

- - -

### [Efficient Verifiable Differential Privacy with Input Authenticity in the Local and Shuffle Model](http://arxiv.org/abs/2406.18940)

**インプット認証を用いた局所およびシャッフルモデルにおける効率的な検証可能差分プライバシー**

Tariq Bontekoe, Hassan Jameel Asghar, Fatih Turkmen

- LDPは信頼できる中央サーバーなしでクライアントのデータを保護
- シャッフルモデルがLDPに追加のプライバシー層を提供
- 提案手法VLDPが出力操作攻撃を完全に防ぎ、署名データで入力攻撃も防止
- クライアントの実行時間は2秒未満、サーバーはクライアントごとに5-7ミリ秒と非常に実用的

セキュリティと効率のバランスがすごくよさそう！特に、実用的な実行時間が現実的なデプロイを感じさせるね。

**Comment:** 21 pages, 14 figures, 2 tables

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-27 07:12

- - -

### [Towards Personalized Federated Multi-scenario Multi-task Recommendation](http://arxiv.org/abs/2406.18938)

**パーソナライズされた連合学習によるマルチシナリオ・マルチタスク推薦へのアプローチ**

Yue Ding, Yanbiao Ji, Xun Cai, Xin Xin, Xiaofeng Gao, Hongtao Lu

- 複数のターゲット（CTRやCTCVR）を予測するマルチタスク推薦システムが重要である
- 複数のビジネスシナリオを統合し、共有知識で性能を向上させる
- PF-MSMTrecフレームワークを提案し、各シナリオに専用のクライアントを割り当てる
- 実験結果が最先端の手法を上回ることを示している

複数のシナリオを同時に扱うことで、もっとカスタマイズされた推薦ができそう！こういう新しい手法がどんどん実用化されたら、私たちのネットショッピングがもっと便利になるね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, **投稿日時:** 2024-06-27 07:10

- - -

### [From Biased Selective Labels to Pseudo-Labels: An Expectation-Maximization Framework for Learning from Biased Decisions](http://arxiv.org/abs/2406.18865)

**バイアスのかかった選択的ラベルから擬似ラベルへ: バイアスのある決定から学ぶための期待最大化フレームワーク**

Trenton Chang, Jenna Wiens

- 選択的ラベルは決定プロセスに依存し、診断などがラボテストの実施に左右される
- この研究は、異なるサブグループでのラベリングバイアスが存在する「異種検閲」を扱う
- DCEMというアルゴリズムを提案し、異種検閲の影響を理論的に緩和する方法を分析
- 合成データと臨床データの両方で検証し、ベースラインと比較してバイアス緩和が向上

実際の臨床データでも効果が再現されるなんて、めちゃくちゃ実用的じゃん！これで医療の誤診も減りそうだし、みんな安心だね。

**Comment:** 39 pages, 33 figures. ICML 2024 conference paper

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-06-27 03:33

- - -

### [QBI: Quantile-based Bias Initialization for Efficient Private Data Reconstruction in Federated Learning](http://arxiv.org/abs/2406.18745)

**QBI: 連邦学習における効率的なプライベートデータ再構築のための分位数ベースのバイアス初期化**

Micha V. Nowak, Tim P. Bott, David Khachaturov, Frank Puppe, Adrian Krenzer, Amar Hekalo

- 分散データ上でモデルを訓練する連合学習で、バイアス初期化がプライベートデータ再構築能力を向上
- QBIは疎な活性化パターンを生むバイアス値を直接解く新しい手法
- PAIRSアルゴリズムを提案し、データセットが利用可能な場合にデータ回復率を向上
- AGGPという防御フレームワークを提案し、勾配の疎密性攻撃を予防し、連合学習のセキュリティを向上

データがこんなに再現できちゃうなんて驚き！AGGPが未来の連合学習をもっと安全にしてくれそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-26 20:19

- - -

### [A Zero Auxiliary Knowledge Membership Inference Attack on Aggregate Location Data](http://arxiv.org/abs/2406.18671)

**付加的な知識なしで「メンバーシップ推論攻撃」を行う手法の検討：集合位置データの場合**

Vincent Guan, Florent Guépin, Ana-Maria Cretu, Yves-Alexandre de Montjoye

- 集合データに対するメンバーシップ推論攻撃（MIA）のリスクを評価
- 補助データセットなしで攻撃を行う新しい合成アプローチを開発
- 差分プライバシーや小カウント抑制などのプライバシー機構が適用されても攻撃が有効
- 対象者の位置情報の一部（10%）のみ知っている場合でも高い有効性を示す

合成データで補助データ不要とか斬新✨これならプライバシー保護の進化が期待できそう。

**Comment:** To be published in PETS 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-06-26 18:14

- - -

### [Contraction of Private Quantum Channels and Private Quantum Hypothesis Testing](http://arxiv.org/abs/2406.18651)

**非公開量子チャネルおよび非公開量子仮説検定の収縮**

Theshani Nuradha, Mark M. Wilde

- 量子チャネルの下での偏差の相対的減少は多くの場合、1未満であることが興味深い
- 本研究では、量子ローカル差分プライバシーの枠組みに基づきホッケースティック偏差の収縮係数の上限を確立
- 正規化されたトレース距離に対して、ビュレス距離と量子相対エントロピーの収縮の上限を決定
- 非公開の量子チャネルが量子学習設定において公平性とホレフ情報の安定性を提供することを示す

量子プライバシーの話ってすごく最先端！特にホッケースティック偏差のところ、難しそうだけど面白そうだよね。一緒にもっと学んでみたいな。

**Comment:** 36 pages; See independent work titled "Sample Complexity of Locally   Differentially Private Quantum Hypothesis Testing" by Hao-Chung Cheng,   Christoph Hirche, and Cambyse Rouz\'e

**トピック:** [差分プライバシー](dp), **カテゴリ:** quant-ph, cs.CR, cs.IT, cs.LG, math.IT, stat.ML, **投稿日時:** 2024-06-26 18:00
