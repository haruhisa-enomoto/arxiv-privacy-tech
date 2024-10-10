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

更新: 2024-10-10T04:23:57.723912

- - -

### [A Gentle Introduction and Tutorial on Deep Generative Models in Transportation Research](http://arxiv.org/abs/2410.07066)

**交通研究における深層生成モデルの入門とチュートリアル**

Seongjin Choi, Zhixiong Jin, Seungwoo Ham, Jiwon Kim, Lijun Sun

- 深層生成モデル（DGMs）は、複雑なデータ分布を学習し合成データを生成する能力で急速に進化
- 交通研究での応用が増加中、特に交通データの生成、予測、特徴抽出において重要性が高まる
- 論文は生成モデルの概観、基本モデルの詳細、文献レビュー、実践的なチュートリアルコードを提供
- 現在の課題と機会、交通研究での効果的な利用とさらなる開発方法も議論

DGMsって、交通データの予測とか生成にすごく役立ちそうだよね。これからの交通研究でどんどん使われそうだから、その流れを追ってみるのもいいかも！

**Comment:** 64 pages, 21 figures, 4 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-09 17:11

- - -

### [Distributionally Robust Clustered Federated Learning: A Case Study in Healthcare](http://arxiv.org/abs/2410.07039)

**分布的にロバストなクラスタ化連合学習: ヘルスケアにおけるケーススタディ**

Xenia Konti, Hans Riess, Manos Giannopoulos, Yi Shen, Michael J. Pencina, Nicoleta J. Economou-Zavlanos, Michael M. Zavlanos

- ヘテロなデータ分布の課題に対し、新アルゴリズムCS-RCFLを提案
- Wasserstein距離を用いて各クライアントのデータ分布の曖昧さを測定
- 最適な分布的にロバストなクラスタリングでローカルモデルの偏りを回避
- プライバシーを保持しつつの連合学習プロトコルを提案し、評価を行う

この研究って、ヘルスケアのデータをうまく活用しつつ個人情報も守れるってすごく重要だよね。クライアント間の偏りを避けるための新しいアプローチも面白そう！

**Comment:** 8 pages, 3 figures, Accepted to IEEE CDC 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-09 16:25

- - -

### [Diagnosis of Malignant Lymphoma Cancer Using Hybrid Optimized Techniques Based on Dense Neural Networks](http://arxiv.org/abs/2410.06974)

**密集ニューラルネットワークに基づくハイブリッド最適化技術を用いた悪性リンパ腫癌の診断**

Salah A. Aly, Ali Bakhiet, Mazen Balat

- リンパ腫の診断は形態の微細な違いで難易度が高い
- DenseNet201とDNNを組み合わせたハイブリッド学習フレームワークを提案
- Harris Hawks Optimizationアルゴリズムで最適化し、99.33%の精度を達成
- 精度、再現率、F1スコア、ROC-AUCでモデルの頑健性を評価

ハイブリッド学習と呼ばれる技術の進化で、医療分野でもますます効率的に精度が向上しそうだね！実際の臨床現場で、早く助かる患者さんが増えるといいなって思う。

**Comment:** 6 pages, 5 figures, 4 tables, IEEE ICCA

**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, cs.LG, **投稿日時:** 2024-10-09 15:12

- - -

### [Forgetting Through Transforming: Enabling Federated Unlearning via Class-Aware Representation Transformation](http://arxiv.org/abs/2410.06848)

**変換による忘却: クラス認識表現変換による連合消去の実現**

Qi Guo, Zhen Tian, Minghao Yao, Yong Qi, Saiyu Qi, Yun Li, Jin Song Dong

- 連合消去（FU）は、プライバシーと規制を考慮し、特定データの影響を排除する技術。
- 従来のFU法はデータ削除とモデル性能の維持のバランスが難しい課題がある。
- 提案手法（FUCRT）は、クラス認識表現の変換を用いて消去を実現。
- 実験結果でFUCRTは100%のクラス消去と性能維持を達成し、従来手法を上回る。

新しい技術でプライバシーがもっと守られる未来が近づいてる感じ！データ削除しつつモデルの性能を保つとか、すごく役立ちそうだよね。ますますAIの可能性が広がりそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-09 13:08

- - -

### [Transesophageal Echocardiography Generation using Anatomical Models](http://arxiv.org/abs/2410.06781)

**解剖モデルを用いた経食道心エコー生成**

Emmanuel Oladokun, Musa Abdulkareem, Jurica Šprem, Vicente Grau

- 深層学習は経食道心エコー画像の解析を自動化で強化するが、高品質データが大量に必要
- 合成データ生成パイプラインを開発し、解剖モデルからスライスを変換し合成画像を作成
- 左心室のセマンティックセグメンテーションにより、合成画像が深層学習ネットワーク性能を向上
- 合成画像を評価し、Fréchet Inception Distanceスコアで最大10%の精度向上が達成

解剖モデルから経食道心エコーを生成できるなんてすごい技術だよね！これが普及すれば、あとは画像さえあればAIに任せちゃえば良くなっちゃうんじゃない？これからの医療現場での応用も楽しみかも！

**Comment:** MICCAI2023; DALI Workshop

**トピック:** [TEE](tee), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-10-09 11:20

- - -

### [Towards Natural Image Matting in the Wild via Real-Scenario Prior](http://arxiv.org/abs/2410.06593)

**リアルシナリオによる自然画像マット化の実現**

Ruihao Xia, Yu Liang, Peng-Tao Jiang, Hao Zhang, Qianru Sun, Yang Tang, Bo Li, Pan Zhou

- 合成データ依存の既存手法は複雑な状況での一般化に失敗
- COCO-Mattingというデータセットを提案し、複雑な自然画像の人間インスタンスレベルのアルファマットを収集
- SEMatを提案し、ネットワーク構造と学習目標を改善し、微細なエッジと透明度を抽出
- 7つの多様なデータセットでの実験で高性能を実証し、手法の有効性を確認

合成データから抜け出して、リアルな場面での画像処理に挑んでるのがめっちゃ面白い！COCO-Matting使って、複雑な場面でも使える手法になるといいなって思うよ。公開されてるから、早速コードも試してみたいな！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-09 06:43

- - -

### [PFAttack: Stealthy Attack Bypassing Group Fairness in Federated Learning](http://arxiv.org/abs/2410.06509)

**PFAttack: 連合学習におけるグループフェアネスを回避するステルス攻撃**

Jiashi Gao, Ziwei Wang, Xiangyu Zhao, Xin Yao, Xuetao Wei

- 連合学習は複数のクライアントが共同で公平な決定を行うためのものである
- 攻撃者はフェアネス機構を回避しバイアスを持つグローバルモデルを作ることが可能である
- PFATTACKはグローバルモデルの精度を損なわずにフェアネス機構を回避する攻撃である
- PFATTACKは目立たず発見されにくい攻撃で、モデルのパラメータ変化が微細である

うわー、PFATTACKがやばそう！みんなが気づかないうちにモデルが偏っちゃうかも。連合学習の未来には、新しい対策が必要になるね。楽しみだなぁ、どんな展開になるか。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-09 03:23

- - -

### [FedL2G: Learning to Guide Local Training in Heterogeneous Federated Learning](http://arxiv.org/abs/2410.06490)

**FedL2G: 異種連合学習におけるローカルトレーニングのガイドを学習する方法**

Jianqing Zhang, Yang Liu, Yang Hua, Jian Cao, Qiang Yang

- 異種連合学習ではデータとモデルの異種性が課題で、モデルパラメータの集約が難しい
- グローバルなプロトタイプに合わせると、クライアントの目的と指導目標にミスマッチが生じる
- FedL2Gは、クライアントの目的に有益な形でローカルトレーニングをガイドする方法を提案
- 実験で6モデル異種性と2データ異種性において優れた性能を示した

これ、色んな異種モデルを扱えるんだね！ローカルトレーニングを賢くガイドするって、まるでデジタルの先生みたい。連合学習でもっと効率的な解決策がどんどん生まれるといいね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-09 02:31

- - -

### [OledFL: Unleashing the Potential of Decentralized Federated Learning via Opposite Lookahead Enhancement](http://arxiv.org/abs/2410.06482)

**OledFL: 逆見通し強化による非中央集権型連合学習の可能性の解放**

Qinglun Li, Miao Zhang, Mengzhu Wang, Quanjun Yin, Li Shen

- 非中央集権型連合学習（DFL）は中央集権型よりも高速なトレーニングとプライバシー保護を実現
- しかし、DFLは一般化能力で中央集権型に劣り、理論理解や実証性能が不十分
- 逆見通し強化技術（Ole）を活用して、DFLの一貫性を向上させることで一般化力と収束速度を改善
- CIFAR10とCIFAR100のデータセットで、最大5%性能向上と8倍の高速化を達成

最近の連合学習の話、面白そう！逆見通しとか新しいアプローチでどんな可能性が開けるのかワクワクするよね。いろんな実験で結果がしっかり出るのも期待できて嬉しいな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-09 02:16

- - -

### [LLM Self-Correction with DeCRIM: Decompose, Critique, and Refine for Enhanced Following of Instructions with Multiple Constraints](http://arxiv.org/abs/2410.06458)

**DeCRIMを用いたLLM自己訂正：複数制約の指示追従向上のための分解・批評・改良**

Thomas Palmeira Ferraz, Kartik Mehta, Yu-Hsiang Lin, Haw-Shiuan Chang, Shereen Oraby, Sijia Liu, Vivek Subramanian, Tagyoung Chung, Mohit Bansal, Nanyun Peng

- LLMは複数制約を持つ指示に弱く、21%以上の誤りがあると明らかに
- RealInstructというベンチマークで、LLMの実世界の指示追従能力を評価
- DeCRIMは指示を分解し批評モデルを用いて改善し、性能向上を実現
- DeCRIMは公開モデルでGPT-4を超える性能を示した

LLMって指示に従わせるのが難しいんだね。でも、新しい方法で改善できるなんて、夢が広がるね！モデルがさらに賢くなる未来を想像するとワクワクする！

**Comment:** To appear at EMNLP 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-10-09 01:25

- - -

### [Communication-Efficient Federated Group Distributionally Robust Optimization](http://arxiv.org/abs/2410.06369)

**通信効率の良い連合グループ分布ロバスト最適化**

Zhishuai Guo, Tianbao Yang

- 連合学習はクライアント間のデータ量と分布の異質性により一般化能力が低下する課題がある
- 既存のグループ分布ロバスト最適化(GDRO)は通信とサンプルの複雑性が高い
- 提案するFGDRO-CVaRは平均の上位-K損失を最適化し通信複雑性を低減
- FGDRO-KLとFGDRO-KL-Adamにより、KL正則化を通じてさらに通信コストを削減

この論文、連合学習の通信コストをどんどん減らせるっていうのがすごくイケてる！特にFGDRO-KL-Adamが実用的に活躍しそうで、データ不足の問題を解決する未来が見える✨

**Comment:** Accepted to NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, stat.ML, **投稿日時:** 2024-10-08 21:07

- - -

### [Moving Faster and Reducing Risk: Using LLMs in Release Deployment](http://arxiv.org/abs/2410.06351)

**より速くリスクを減らす: リリース展開におけるLLMの使用**

Rui Abreu, Vijayaraghavan Murali, Peter C Rigby, Chandra Maddila, Weiyan Sun, Jun Ge, Kaavya Chinniah, Audris Mockus, Megh Mehta, Nachiappan Nagappan

- リリース工学では大規模環境でのリリース判断が難しくなり、責任がコードを書くエンジニアに戻る。
- 差分リスクスコア(DRS)モデルを開発し、重大障害(SEV)を引き起こす可能性を予測する。
- ロジスティック回帰モデルでSEVの18.7%、27.9%、84.6%をキャプチャし、リスクに応じてゲーティングする。
- ジェネレーティブLLM「iCodeLlama-34B」と「iDiffLlama-13B」は、ロジスティック回帰モデルよりもSEVを多く捉える。

この論文、リリースの自動化でめっちゃ便利になりそうだね！モデルを使ってリスク低減まで狙うなんて、エンジニアの未来をぐっと引き寄せてる感じがする！すごいなー。



**トピック:** [TEE](tee), **カテゴリ:** cs.SE, **投稿日時:** 2024-10-08 20:40

- - -

### [Bayesian Estimation and Tuning-Free Rank Detection for Probability Mass Function Tensors](http://arxiv.org/abs/2410.06329)

**ベイズ推定とチューニング不要なランク検出による確率質量関数テンソルの解析**

Joseph K. Chege, Arie Yeredor, Martin Haardt

- 確率質量関数をテンソルで低ランク分解することで推定を効率化
- ランク選択は通常、検証誤差や情報基準の計算が必要
- ベイズフレームワークによりランクを自動推定する新手法を提案
- 新手法はVIとSVIを用いた高効率なアルゴリズムを実現

ベイズ推定ってなんかワクワクするね！自動でランクがわかるなんて、すごく便利そう。これでどんな応用ができるのか気になるね。データが大きくてもスムーズって、未来のデータサイエンスに革命を起こしそうだよ！



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, eess.SP, **投稿日時:** 2024-10-08 20:07

- - -

### [EVOLvE: Evaluating and Optimizing LLMs For Exploration](http://arxiv.org/abs/2410.06238)

**EVOLvE: 探索のための大規模言語モデルの評価と最適化**

Allen Nie, Yi Su, Bo Chang, Jonathan N. Lee, Ed H. Chi, Quoc V. Le, Minmin Chen

- 大規模言語モデルは不確実性下での最適な意思決定が求められる場面での研究が不足。
- 文脈のないバンディット問題や文脈バンディットを用いて、最適な意思決定能力を評価。
- 探索アルゴリズムの知識を取り入れて、より小さなモデルでも優れた成果を実現。
- 探索効率に関する因子を徹底分析し、モデルサイズや基盤アルゴリズムとの関係を検討。

大規模言語モデルがどのようにして不確実な状況で賢く決定をするのか学んでいく過程が面白そう！小さなモデルが大きなモデルを超えるところも、なんだか胸熱だね。私たちも勉強頑張って、この研究のように自分なりのベストな探求をしてみたいな！

**Comment:** 28 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-10-08 17:54

- - -

### [De-VertiFL: A Solution for Decentralized Vertical Federated Learning](http://arxiv.org/abs/2410.06127)

**分散型垂直連合学習のためのDe-VertiFL**

Alberto Huertas Celdrán, Chao Feng, Sabyasachi Banik, Gerome Bovet, Gregorio Martinez Perez, Burkhard Stiller

- 水平連合学習と異なり、垂直連合学習は同一エンティティの異なるデータを扱うため未開拓
- De-VertiFLは新しいネットワークアーキテクチャや知識交換方式を導入した
- 各クライアント間で隠れ層の出力を共有し、中間計算の利益を享受しつつ効率的に学習
- 評価結果は高性能でプライバシーも守りつつF1スコアで最新手法を上回る

新しい仕組みを使って色々工夫してるから、どんなデータでも上手くできちゃうってことなのかな？分散型でプライバシーを守りつつ性能が良いのは、なんだか安心して使える未来が待ってる感じ♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-08 15:31

- - -

### [AIVIO: Closed-loop, Object-relative Navigation of UAVs with AI-aided Visual Inertial Odometry](http://arxiv.org/abs/2410.05996)

**AIVIO: AI支援のビジュアル慣性オドメトリによるUAVの閉ループ、対象相対ナビゲーション**

Thomas Jantos, Martin Scheiber, Christian Brommer, Eren Allak, Stephan Weiss, Jan Steinbrener

- 対象相対の移動ロボットナビゲーションは、重要なインフラ点検に不可欠
- 深層学習(DL)が画像から対象情報を推論するが、高負荷で物理制約がある
- 提案システムはUAVをIMUとRGBカメラのみで対象相対の閉ループナビに対応
- 合成データで訓練されたDLベースの姿勢推定を用い、実験で性能を検証

この研究面白そう！モノだけじゃなく、合成データを使って実験もしてるってめっちゃ効率的！本当に空をスムーズに飛べるか見てみたいな～。地味だけどインフラの点検に役立つとか未来感あるね！

**Comment:** Accepted for publication in the IEEE Robotics and Automation Letters   (RA-L), 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-10-08 12:52

- - -

### [Chameleon: An Efficient FHE Scheme Switching Acceleration on GPUs](http://arxiv.org/abs/2410.05934)

**カメレオン: GPU上での効率的なFHEスキーム切り替えの加速**

Zhiwei Wang, Haoqi He, Lutan Zhao, Peinan Li, Zhihao Li, Dan Meng, Rui Hou

- 完全準同型暗号（FHE）は暗号化データ上の直接計算を可能にするが、性能瓶頸がある
- 従来の研究は単一のFHEに焦点を当て多様な要求に適合せず、複数クラスのFHEが開発される
- 本研究「Chameleon」は、GPUを活用したFHEスキームの切り替えの効率的な加速を実現
- 最先端GPUと比較して1.23倍から最大67.3倍の速度向上をCPU実装と比較して達成

GPUの力を借りてFHEの性能を一気にアップさせるってすごいアイディアだよね！プライバシー保護がより実用的になると、未来の色んなサービスがもっと安心して使えそう！

**Comment:** 15 pages, 14 figures

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-08 11:37

- - -

### [Fortify Your Foundations: Practical Privacy and Security for Foundation Model Deployments In The Cloud](http://arxiv.org/abs/2410.05930)

**基盤モデルのクラウド展開における実用的なプライバシーとセキュリティの強化**

Marcin Chrapek, Anjo Vahldiek-Oberwagner, Marcin Spoczynski, Scott Constable, Mona Vij, Torsten Hoefler

- 基盤モデルは自然言語処理で優れた性能を発揮するが、プライベートデータを使うことで知的財産のリスクが高まる。
- マルチモーダル基盤モデルは機密情報を流出させる可能性がある。
- 信頼できる実行環境（TEEs）がセキュリティ、使いやすさ、性能のバランスに優れている。
- 研究では、TEEsを用いた実装の実用性と情報を初めて示し、設定ファイルや知見も共有。

基盤モデルを安全に使うための手法がわかってよかった！TEEsならセキュリティしっかりで安心して使えそうだし、実用性もあるってのがいいね。新しい取り組みを応用して、どんどんセキュリティが進化していくといいなあ！



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-10-08 11:33

- - -

### [Ordering-Based Causal Discovery for Linear and Nonlinear Relations](http://arxiv.org/abs/2410.05890)

**線形および非線形関係のための順序ベースの因果発見**

Zhuopeng Xu, Yujie Li, Cheng Liu, Ning Gui

- 観測データからの因果関係の特定には、通常追加の仮定が必要
- 現行の多くの手法は線形や非線形に限定され、現実世界のデータに適さない
- CaPSというアルゴリズムを提案、トポロジカル順序の新しい識別基準を導入
- 実験結果は、合成データと実世界のデータで優れた成果を示している

CaPSってどんな風に世界を見つめ直すのかな？現実のデータにもっとぴったり寄り添うことで、私たちがまだ知らない関係性が見つかるかもしれないね！データの背後に隠された秘密が解き明かされるのが楽しみ！

**Comment:** NeurIPS 2024 poster

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-08 10:33

- - -

### [Private and Communication-Efficient Federated Learning based on Differentially Private Sketches](http://arxiv.org/abs/2410.05733)

**差分プライベートスケッチに基づくプライバシーと通信効率の良い連合学習**

Meifan Zhang, Zhanhong Xie, Lihua Yin

- 連合学習ではプライバシーの漏洩リスクと通信の非効率が課題
- DPSFLは差分プライバシースケッチを使用し通信効率とプライバシーを向上
- 勾配クリッピングはノイズの影響を抑えるがバイアスを生むため性能に悪影響
- DPSFL-ACは適応クリッピングによりバイアスを軽減し優れた性能を実証

連合学習って、ただ共有すればいいってもんじゃないのが面白いね！DPSFLでプライバシーも通信も改善できちゃうなんて、実用化されたらすごく便利そうだし、頼もしいなって思っちゃう！💡



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-08 06:50

- - -

### [KnowledgeSG: Privacy-Preserving Synthetic Text Generation with Knowledge Distillation from Server](http://arxiv.org/abs/2410.05725)

**KnowledgeSG: サーバからの知識蒸留によるプライバシー保護付き合成テキスト生成**

Wenhao Wang, Xiaoyu Liang, Rui Ye, Jingyi Chai, Siheng Chen, Yanfeng Wang

- 大規模言語モデルの記憶化でプライバシー懸念が生じる
- 合成データ利用は性能向上とプライバシー保護の両立が難しい
- KnowledgeSGは、差分プライバシーと知識蒸留で品質と性能を向上
- 連合学習に着想を得て、モデルをクライアント・サーバ間で共有しプライバシーを保護

この方法は、プライバシーも守りつつ性能も上げるなんてすごくおもしろそう！医療や金融みたいなデータが重要でセンシティブな分野でもうまくいくなら、めっちゃ役立ちそうだね。どんな時代が来るんだろう、ワクワクする～！

**Comment:** EMNLP 2024 Main

**トピック:** [連合学習](fl), [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-10-08 06:42

- - -

### [Federated Learning with Dynamic Client Arrival and Departure: Convergence and Rapid Adaptation via Initial Model Construction](http://arxiv.org/abs/2410.05662)

**動的クライアント到着と離脱を伴う連合学習: 収束と初期モデル構築による迅速な適応**

Zhan-Lun Chang, Dong-Jun Han, Rohit Parasnis, Seyyedali Hosseinalipour, Christopher G. Brinton

- 従来の連合学習は固定されたクライアントを想定するが、実際にはクライアントは動的に参加や離脱を行う。
- クライアントの変動によって、最適化目標が動的に変化するため、適応が遅れる可能性がある。
- 最適モデルを動的に調整するための初期モデル構築戦略を提案し、クライアントのデータ特性に基づくモデルを使用。
- 様々なデータセットとアルゴリズムで検証を行い、多様なクライアント変化において強力な性能を示した。

動的なクライアントの参加と離脱を考慮した連合学習なんて、なんかめっちゃ面白そう！これからはもっと柔軟で適応力のあるAIが求められるから、この研究が実現したら、いろんなアプリに応用できそうでワクワクするね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-08 03:22

- - -

### [On the Modeling Capabilities of Large Language Models for Sequential Decision Making](http://arxiv.org/abs/2410.05656)

**大規模言語モデルによる逐次的意思決定のモデリング能力について**

Martin Klissarov, Devon Hjelm, Alexander Toshev, Bogdan Mazoure

- 大規模言語モデル（LLM）は強化学習における意思決定ポリシーの生成能力を評価
- AIによる報酬の設計が、一般的かつ高性能な報酬モデリングを可能にする
- 課題に特化した微調整を行わなくても、LLMは報酬モデリングに優れる
- 未知の環境では、合成データでの微調整が報酬モデリング能力を向上

大規模言語モデルが強化学習にまで役立つってすごいかも！報酬設計とか新しい活用法もあるし、未知の環境への適応能力が向上するのは未来っぽくてワクワクする～！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-10-08 03:12

- - -

### [A Blockchain-Enhanced Framework for Privacy and Data Integrity in Crowdsourced Drone Services](http://arxiv.org/abs/2410.05653)

**ブロックチェーン強化型フレームワークによる群衆からのドローンサービスのプライバシーとデータ完全性**

Junaid Akram, Ali Anaissi

- 消費者向けドローンをブッシュファイア管理に統合し、サービス改善とデータプライバシーに対処
- ブッシュファイア当局がデータを利用し、ドローン運営者が提供する市場を形成
- データ提供者のプライバシーを局所的差分プライバシーで保護し、プライバシー基準に準拠
- ブロックチェーンで公正なデータと料金交換を促進し、不変の記録で責任を強化

災害管理にドローンを使うってすごく活用されてるよね！このシステムでなら、みんなにとって安全で信頼できる情報が飛び交う未来が見えてきそうだよ。大規模への適応もばっちりだから、実際の現場でも活躍してくれるかも！

**Comment:** 8 pages, 5 figures, accepted and to be published in the proceedings   of 22nd International Conference on Service-Oriented Computing (ICSOC 2024)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-08 03:08

- - -

### [Aiding Global Convergence in Federated Learning via Local Perturbation and Mutual Similarity Information](http://arxiv.org/abs/2410.05545)

**ローカル摂動と相互類似情報による連合学習のグローバル収束支援**

Emanuel Buttaci, Giuseppe Carlo Calafiore

- 連合学習は、携帯端末の増加による分散最適化パラダイムとして注目される技術
- 類似性グラフを用い、クライアント間の統計的類似性を活かす新たなフレームワークを提案
- 提案手法は、FedAvgやFedProxに比べて強凸な場合の収束速度を理論的に向上
- 実験ではCIFAR10とFEMNISTを用い、最大30ラウンドの収束高速化と一般化の改善を確認

連合学習の収束を加速するために、クライアントの類似性を活用しているんだね！技術的には難しそうだけど、実験結果が30ラウンド早くなるなんてすごくおもしろいよね！実際の活用が楽しみだな〜！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, math.OC, **投稿日時:** 2024-10-07 23:14

- - -

### [Privacy Vulnerabilities in Marginals-based Synthetic Data](http://arxiv.org/abs/2410.05506)

**周辺確率に基づく合成データのプライバシー脆弱性**

Steven Golob, Sikha Pentyala, Anuar Maratkhan, Martine De Cock

- 合成データ生成（SDG）は実データと似つつ個人情報を排除することを目指している
- 数多くのSDGアルゴリズムは強力な差分プライバシー保証を提供している
- 周辺確率を保持するSDGアルゴリズムには個人情報が漏洩する危険があると判明
- 新たなメンバーシップ推論攻撃MAMA-MIAを使い、脆弱性が効率的に暴かれる

個人情報の安全性って、どんな技術でも100%確保するのは難しいんだね。それでも続々と新しい手法が開発されててすごいと思う！どんな対策がこれから登場するのかすっごく楽しみ〜！



**トピック:** [合成データ](sd), [差分プライバシー](dp), [PETs](pets), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-10-07 21:24

- - -

### [Exact sensitivity analysis of Markov reward processes via algebraic geometry](http://arxiv.org/abs/2410.05471)

**代数幾何学によるマルコフ報酬過程の正確な感度分析**

Timothy C. Y. Chan, Muhammad Maaz

- マルコフ報酬過程の感度分析を多項式系に再定式化し取り組む
- 円筒代数分解（CAD）を応用し、正確な解の記述を可能にした
- 特定の多項式系を解析しやすくする理論的結果とアルゴリズムを開発
- オープンソースソフトウェアで実装し、実証により利点を示した

マルコフ報酬過程の感度分析を代数幾何学で解決するなんてすごくクールだよね！将来的にはもっと多くの分析に応用されるかもね。ソフトウェアもオープンだから、自分でも試してみたいな。

**Comment:** 46 pages

**トピック:** [合成データ](sd), **カテゴリ:** math.OC, cs.MS, math.AG, math.PR, **投稿日時:** 2024-10-07 20:08

- - -

### [Testing Credibility of Public and Private Surveys through the Lens of Regression](http://arxiv.org/abs/2410.05458)

**回帰の視点から見る公共およびプライベート調査の信頼性**

Debabrota Basu, Sourav Chakraborty, Debarshi Chanda, Buddha Dev Das, Arijit Ghosh, Arnab Ray

- サンプル調査が母集団の信頼できる表現かどうかを回帰分析でテストするアルゴリズムを設計
- Gaussian Differential Privacyを用いて、信頼性の検証を差分プライバシー下の調査にも拡張
- 提案したアルゴリズムで、ノイズがあるデータから線形回帰モデルを学習することが可能
- リアルデータと合成データでアルゴリズムの性能を数値的に実証し、理論的な正しさを証明

サンプル調査とプライバシー技術って、ずっと複雑だと思ってたから、こうやってアルゴリズムで検証できるってすごいよね！しかも、ノイズのあるデータからも学習できるなんて、もっと幅広く応用が効きそう～！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ME, stat.ML, **投稿日時:** 2024-10-07 19:44

- - -

### [Over-the-Air Federated Learning in Cell-Free MIMO with Long-term Power Constraint](http://arxiv.org/abs/2410.05354)

**セルフリーMIMOにおける長期的な電力制約を考慮した無線連合学習**

Yifan Wang, Cheng Zhang, Yuanndong Zhuang, Yongming Huang

- 無線ネットワークでのAI対応が注目され、無線連合学習が重要な応用として浮上
- セルフリーMIMOシステムでの無線連合学習の誤差境界を導出し、最適化問題を設定
- MOP-LOFPCアルゴリズムを提案し、長期制約をラウンドごとに切り離しつつ、随時のチャネル状態情報を利用
- 実験結果で、MOP-LOFPCが既存のベースラインに比べて、モデルの訓練損失と長期電力制約のバランスを改善

この技術を使えば、無線ネットワーク上でのAI応用がさらにスムーズに！MOP-LOFPCの適応性もキーポイントで、新たな可能性が広がりそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-07 13:44

- - -

### [An Intelligent Native Network Slicing Security Architecture Empowered by Federated Learning](http://arxiv.org/abs/2410.05312)

**連合学習によって強化されたインテリジェントなネイティブネットワークスライシングセキュリティアーキテクチャ**

Rodrigo Moreira, Rodolfo S. Villaca, Moises R. N. Ribeiro, Joberto S. B. Martins, Joao Henrique Correa, Tereza C. Carvalho, Flavio de Oliveira Silva

- ネットワークスライシングは、5G/6Gネットワークなどでのリソース共有を変革
- 既存のアーキテクチャは、インテリジェントなセキュリティ機能が不足
- 提案するアーキテクチャは、機械学習ベースの連合エージェントを活用
- 提案手法により、DDoSと侵入攻撃を高精度で検出、約95.60%の平均精度を達成

新しいセキュリティアーキテクチャが連合学習で賢くなるなんてすごいよね！通信技術がもっと安全で便利になっちゃう未来が楽しみ。みんなも早くこの技術を体験できるといいなーって思ったよ。

**Comment:** 18 pages, 12 figures, Future Generation Computer Systems (FGCS)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.ET, cs.LG, cs.NI, I.2; I.6; F.2.2, **投稿日時:** 2024-10-04 21:12
