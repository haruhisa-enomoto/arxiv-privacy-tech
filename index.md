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

更新: 2024-07-24T04:19:37.781582

- - -

### [Aster: Fixing the Android TEE Ecosystem with Arm CCA](http://arxiv.org/abs/2407.16694)

**Aster: Arm CCAでAndroid TEEエコシステムを修正する方法**

Mark Kuhne, Supraja Sridhara, Andrin Bertschi, Nicolas Dutly, Srdjan Capkun, Shweta Shinde

- AndroidエコシステムはTrustZoneや信頼されたハイパーバイザを利用し、セキュリティ感受性の高いサービスを隔離
- これらの機構では、Android、ハイパーバイザ、セキュアワールドの相互隔離が必要である
- サンドボックス化されたサービス抽象を提案し、サンドボックス間やAndroid、ハイパーバイザ、セキュアメモリへのアクセスを防止
- Arm CCAのハードウェア分離を活用しつつ、セキュアなインターフェースや中断保護を達成

Asterって、かなり未来的な取り組みなのかな？同じスマホでも、もっと安心して使えるようになるといいね。具体的な実装例もあって、実用的なんだよね、これは期待大！



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-23 17:57

- - -

### [Unveiling and Mitigating Bias in Audio Visual Segmentation](http://arxiv.org/abs/2407.16638)

**音声映像セグメンテーションにおけるバイアスの解明と緩和**

Peiwen Sun, Honggang Zhang, Di Hu

- 先行研究は音声映像セグメンテーションモデルを進化させたが、誤った論理で異常を示すことがある
- 異常現象は「音声プライミングバイアス」と「視覚の事前知識」の二種類に分類される
- 音声プライミングバイアスには、音声の潜在的な意味情報を取り込む感知モジュールを導入
- 視覚の事前知識には、モデル構造を変更せずにバイアスを統合する対比訓練戦略を探索

音声映像セグメンテーションのバイアスって面白い！どのように解消したのかもっと知りたいなあ。これが実際の性能向上につながるとまた新しい技術が生まれそうだね！

**Comment:** Accepted by ACM MM 24 (ORAL)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-23 16:55

- - -

### [Knowledge-driven AI-generated data for accurate and interpretable breast ultrasound diagnoses](http://arxiv.org/abs/2407.16634)

**知識駆動型AI生成データによる正確かつ解釈可能な乳房超音波診断**

Haojun Yu, Youcheng Li, Nan Zhang, Zihan Niu, Xuantong Gong, Yanwen Luo, Quanlin Wu, Wangyan Qin, Mengyuan Zhou, Jie Han, Jia Tao, Ziwei Zhao, Di Dai, Di He, Dong Wang, Binghui Tang, Ling Huo, Qingli Zhu, Yong Wang, Liwei Wang

- 訓練データの長尾分布が原因で稀なケースでの診断の正確性が課題
- TAILORというパイプラインを導入し、知識駆動型モデルで合成データを生成
- 生成モデルは3,749件の病変データを元に数百万の乳房超音波画像を生成可能
- DCISの診断モデルが全ての放射線科医を大きく上回る成果を示した

TAILORのモデルで稀な症例もカバーできるってすごい！この技術がもっと広がれば、いろんな病気の早期発見とかにも役立ちそうで楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.AI, cs.CV, cs.HC, **投稿日時:** 2024-07-23 16:49

- - -

### [GenRec: A Flexible Data Generator for Recommendations](http://arxiv.org/abs/2407.16594)

**GenRec: 推薦システム用の柔軟なデータ生成器**

Erica Coppolillo, Simone Mungari, Ettore Ritacco, Giuseppe Manco

- 現実的なデータセットの不足が推薦システムとソーシャルネットワーク分析の大きな課題
- 合成データが現実的な相互作用をシミュレートする有効な解決策
- GenRecは潜在因子モデリングに基づく新しいフレームワークを提案
- 高度な柔軟性があり、ユーザー項目間相互作用の生成をカスタマイズ可能

推薦システムの問題を一気に解決できそう！さまざまな場面で役立ちそうなのが魅力だね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.IR, cs.AI, cs.SI, **投稿日時:** 2024-07-23 15:53

- - -

### [COALA: A Practical and Vision-Centric Federated Learning Platform](http://arxiv.org/abs/2407.16560)

**COALA: 実用的でビジョン中心の連合学習プラットフォーム**

Weiming Zhuang, Jian Xu, Chen Chen, Jingtao Li, Lingjuan Lyu

- COALAは、15のコンピュータビジョンタスクで連合学習をサポートし、複数タスクを同時に扱う
- 監視された連合学習に加え、半監視および未監視の連合学習もベンチマークする
- 静的データに加え、現実世界での連続的に変化するデータに対応した連合学習にも対応
- 分割モデルや異なるクライアント間での異なるモデルを用いた連合学習をベンチマーク

これから連合学習の新しい可能性を見つけることができそう！データの種類によっても色々試せるみたいだから、めっちゃ面白そうじゃない？

**Comment:** ICML'24

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.DC, **投稿日時:** 2024-07-23 15:14

- - -

### [CrudiTEE: A Stick-and-Carrot Approach to Building Trustworthy Cryptocurrency Wallets with TEEs](http://arxiv.org/abs/2407.16473)

**CrudiTEE: TEEを使用した信頼できる暗号通貨ウォレット構築へのスティック＆キャロットアプローチ**

Lulu Zhou, Zeyu Liu, Fan Zhang, Michael K. Reiter

- 暗号通貨は署名鍵の管理のためユーザーに課題をもたらす
- TEEはこの課題を解決する有望な技術だが、実装はサイドチャネル攻撃に弱い
- 経済的インセンティブでサイドチャネル攻撃を緩和する新アプローチを提案
- マルコフ決定過程を用いて攻撃者の行動をモデル化し、報奨金の効果を評価

TEEの経済的アプローチ、なんか新しくて面白そう！もっと安全なウォレットが広がるといいね。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-23 13:44

- - -

### [On Differentially Private 3D Medical Image Synthesis with Controllable Latent Diffusion Models](http://arxiv.org/abs/2407.16405)

**差分プライバシーを用いた制御可能な潜在拡散モデルによる3D医療画像合成**

Deniz Daum, Richard Osuala, Anneliese Riess, Georgios Kaissis, Julia A. Schnabel, Maxime Di Folco

- 公開医療画像データセットの小ささとプライバシー問題が深層学習モデルの進展を阻害
- 医療属性に基づいて合成画像を生成する潜在拡散モデルを提案し、差分プライバシーを確保
- 公開データで事前学習後、UKBiobankデータセットで差分プライバシーを用いて微調整
- プライバシー制約と画像品質のトレードオフを探求し、プライバシー強化が性能低下を引き起こす可能性を示す

プライバシーを守りつつも高品質な医療画像を生成できるなんて、新しい扉が開ける感じがするね！でも、まだ完璧じゃないところが挑戦しがいありそう。



**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-07-23 11:49

- - -

### [On ADMM in Heterogeneous Federated Learning: Personalization, Robustness, and Fairness](http://arxiv.org/abs/2407.16397)

**異質連合学習におけるADMMの活用: パーソナライズ、ロバスト性、公平性**

Shengkun Zhu, Jinshan Zeng, Sheng Wang, Yuan Sun, Xiaodong Li, Yuan Yao, Zhiyong Peng

- 統計的な異質性は連合学習における精度、公平性、ロバスト性に緊張を生む主要な原因
- パーソナライズ連合学習(PFL)は、個人のモデルを開発し、統計的な異質性の影響を軽減
- 既存のPFLフレームワークはパーソナライズモデルの性能向上に焦点を当て、グローバルモデルを軽視
- 提案するFLAMEフレームワークは、ADMMを活用してパーソナライズとグローバルモデルの両方をトレーニング

FLAMEのフレームワークは、新しいモデル選択戦略を通じて、多様なデータを持つクライアントに対応するのが面白そうだよね。お互いに良い成績が出せるようサポートし合えるかも！

**Comment:** arXiv admin note: text overlap with arXiv:2311.06756

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-23 11:35

- - -

### [STATE: A Robust ATE Estimator of Heavy-Tailed Metrics for Variance Reduction in Online Controlled Experiments](http://arxiv.org/abs/2407.16337)

**STATE: オンライン制御実験における分散削減のための頑健な重尾分布を持つ平均処置効果推定量**

Hao Zhou, Kun Sun, Shaoming Li, Yangfeng Fan, Guibin Jiang, Jiaqi Zheng, Tao Li

- 分散削減は高い統計検出力を達成し、少ないサンプルと短い実験期間で効果を発揮する技術
- 従来の分散削減法はガウス分布前提で、重尾分布を持つ実際のビジネスメトリックを正確に反映できない
- Student's t分布と機械学習ツールを組み合わせ、外れ値の影響を排除することで頑健な平均処置効果推定量を構築
- 合成データとMeituan実験プラットフォームでの長期実証により、STATEが最先端の推定器に比べて50%以上の分散削減を達成

実験期間を短くできて、同じ精度の実験結果が得られるってすごいよね！さまざまなビジネスメトリックに適用できそうだから、今後のオンライン実験の新スタンダードになるかもね。

**Comment:** Accepted by KDD 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-23 09:35

- - -

### [Federated Learning for Face Recognition via Intra-subject Self-supervised Learning](http://arxiv.org/abs/2407.16289)

**顔認識のための連合学習：被写体内自己教師あり学習によるアプローチ**

Hansol Kim, Hoyeol Choi, Youngjun Kwak

- 顔認識の連合学習（FL）は、個々のクライアントのモデルを集約し、一般化された顔認識モデルを構築
- 既存の研究では自己教師あり学習の不足と複数被写体の対応が課題
- 提案するFedFSは、被写体を固定せずに個別化された顔認識モデルを訓練する新しいFLアーキテクチャ
- FedFSは、適応的なラベル構築と被写体内自己教師あり学習を活用し、精度と安定性を向上

FedFSって新しい連合学習のアーキテクチャなんだって！自己教師あり学習を活用するアイデアがすごく興味深いね。実験結果も良好らしいし、もっと詳しく知りたいな。

**Comment:** Accepted at the The 35th British Machine Vision Conference 2024 (BMVC   2024), Glasgow, UK. Youngjun Kwak is corresponding author

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-07-23 08:43

- - -

### [Tackling Feature-Classifier Mismatch in Federated Learning via Prompt-Driven Feature Transformation](http://arxiv.org/abs/2407.16139)

**連合学習における特徴-分類器の不一致問題をプロンプト駆動の特徴変換で解決**

Xinghao Wu, Jianwei Niu, Xuefeng Liu, Mingjia Shi, Guogang Zhu, Shaojie Tang

- 連合学習（FedAvg）はデータの異質性によりグローバルモデルの性能が低下
- FedAvgの特徴抽出器が多くのPFL（パーソナライズド連合学習）手法より優れている
- ローカル特徴を線形変換し分類器に合わせるとFedAvgはほとんどのPFL手法を凌駕
- 提案手法FedPFTはプロンプト駆動の特徴変換モジュールで特徴と分類器の不一致を解決

FedPFTがどの程度成果を出せるか非常に興味深い！連合学習の新しいアプローチが、特にパーソナライズにどれだけ役立つか見てみたいな。

**Comment:** 23 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-23 02:52

- - -

### [Escalation of Commitment: A Case Study of the United States Census Bureau Efforts to Implement Differential Privacy for the 2020 Decennial Census](http://arxiv.org/abs/2407.15957)

**コミットメントのエスカレーション: 2020年国勢調査における米国国勢調査局の差分プライバシー実装努力の事例研究**

Krish Muralidhar, Steven Ruggles

- 2010年の国勢調査で使用された方法（データ交換）の高い開示リスクに基づき、2020年の国勢調査で差分プライバシーを導入
- 2010年のタブラー形式データの開示リスク主張についての厳密な評価は行われていなかった
- 開示リスク評価の手順が不安定で、リスクが過大評価されていたことを示す
- 新手順でリリースされたデータ製品は、プライバシーと精度の両方で不十分

差分プライバシーを導入したのに、どっちつかずになっちゃったなんてビックリだね。技術の進化が期待できるけど、課題もたくさんだね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DB, **投稿日時:** 2024-07-22 18:13

- - -

### [Decentralized Federated Anomaly Detection in Smart Grids: A P2P Gossip Approach](http://arxiv.org/abs/2407.15879)

**スマートグリッドにおける分散型連合異常検出：P2Pゴシップアプローチ**

Muhammad Akbar Husnoo, Adnan Anwar, Md Enamul Haque, A. N. Mahmood

- スマートグリッドのセキュリティとプライバシー懸念が強まり、強固な侵入検出システムの需要が増加
- 連合学習がデータ共有なしで攻撃検出モデルの協調訓練を実現。しかし、集中型アグリゲータに依存しプライバシー漏洩のリスクも
- ランダムウォークとエピデミックゴシッププロトコルを用いた新しい分散型連合異常検出スキームを提案
- 実験結果でランダムウォークが高性能を示し、通信遅延や遅延ノードの影響を軽減しつつ、従来の連合学習よりも35%トレーニング時間を短縮

これはすごく興味深い論文ね！ランダムウォークプロトコルがエピデミックよりも効率的に機能するなんて、高校のネットワーク授業でもちょっと触れてみたいかも。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.DC, cs.LG, **投稿日時:** 2024-07-20 10:45

- - -

### [A Survey on Differential Privacy for SpatioTemporal Data in Transportation Research](http://arxiv.org/abs/2407.15868)

**交通研究における時空間データの差分プライバシーに関する調査**

Rahul Bhadani

- 低コストの計算デバイスと向上したセンサ技術でデータ量が急増
- 時空間データは位置情報を含むため、公開にはリスクが大きい
- 研究と推論のため、プライバシーを保護する差分プライバシー技術が提案されている
- 差分プライバシーの実装と広範な採用に関する課題を議論

差分プライバシーを交通研究に応用するアイデアが面白いね。これが進むと、もっと安心してデータが使える未来が来るかも！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.CY, cs.LG, stat.ME, stat.ML, **投稿日時:** 2024-07-18 03:19
