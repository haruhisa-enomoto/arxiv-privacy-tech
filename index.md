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

更新: 2024-08-21T04:20:55.598839

- - -

### [Feature Selection from Differentially Private Correlations](http://arxiv.org/abs/2408.10862)

**差分プライベートな相関からの特徴選択**

Ryan Swope, Amol Khanna, Philip Doldo, Saptarshi Roy, Edward Raff

- 高次元データセットで最重要な特徴を特定するための$L_1$正則化回帰が非効率
- 高次元回帰は個々のデータポイントの情報漏洩のリスクがある
- 既存の二段階選択技術が実世界データセットで不安定なことを実証
- 相関に基づく順序統計量を用いた新方法が、多くのデータセットで既存技術を大幅に上回る

新しい方法が今までの限界を超えて成果を出してるから、めちゃ期待できるよね！現場での実装が楽しみじゃん？

**Comment:** To appear in Proceedings of the 17th ACM Workshop on Artificial   Intelligence and Security, 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-08-20 13:54

- - -

### [ZebraPose: Zebra Detection and Pose Estimation using only Synthetic Data](http://arxiv.org/abs/2408.10831)

**ZebraPose: 合成データのみを用いたシマウマの検出およびポーズ推定**

Elia Bonetto, Aamir Ahmad

- 合成データを用いて、シマウマの2Dポーズ推定と検出を実現
- 3Dフォトリアリスティックシミュレーターで合成データを生成
- 実際のシマウマ画像での一般化能力を証明
- この技術は少量の実データで馬にも応用可能

シマウマのための技術が他の動物にも使えるってすごくない？これ、ワイルドライフ研究の効率をめっちゃ上げちゃいそう！

**Comment:** 8 pages, 5 tables, 7 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.RO, **投稿日時:** 2024-08-20 13:28

- - -

### [NeuLite: Memory-Efficient Federated Learning via Elastic Progressive Training](http://arxiv.org/abs/2408.10826)

**NeuLite：エラスティック進行トレーニングによるメモリ効率の高い連合学習**

Yebo Wu, Li Li, Chunlin Tian, Dubing Chen, Chengzhong Xu

- 連合学習はデータプライバシーを保ちながら複数のデバイスが共同でモデルを訓練する新たな学習パラダイムである
- リソースが限られたデバイスにおいて、トレーニング中の大きなメモリ使用量が実装のボトルネックである
- NeuLiteはモデルをブロックに分割し、進行的にトレーニングを行うことでメモリ使用量を削減するフレームワークを提案している
- 実験では、NeuLiteが最大50.4%のメモリ使用量削減、最大84.2%のモデル性能向上、最大1.9倍のトレーニング速度向上を示した

NeuLiteって、メモリ使うときもすごくエコな感じだね！これでスマホとかももっと賢くなるといいなー。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-08-20 13:21

- - -

### [Generating Synthetic Fair Syntax-agnostic Data by Learning and Distilling Fair Representation](http://arxiv.org/abs/2408.10755)

**公平な表現の学習と蒸留による構文独立な合成データ生成**

Md Fahim Sikder, Resmi Ramachandranpillai, Daniel de Leng, Fredrik Heintz

- AIモデルのトレーニングはバイアスの影響を受けやすく、公正なデータ生成が必要
- 現行の生成方法は計算負荷が高く、最適化性能が低下するリスクがある
- 知識蒸留を用いた小規模アーキテクチャで、公正な潜在空間表現を蒸留
- 新手法は、公正性、合成データの質、データ利用性で現行手法より5-10%向上

バイアス取り除くのって大変だけど、モデルの性能アップにつながるのがいいよね！こういう技術が進めば、もっと公平な社会になりそうでワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-20 11:37

- - -

### [Security Assessment of Hierarchical Federated Deep Learning](http://arxiv.org/abs/2408.10752)

**階層型連合深層学習のセキュリティ評価**

D Alqattan, R Sun, H Liang, G Nicosia, V Snasel, R Ranjan, V Ojha

- 階層型連合学習（HFL）は有望な分散型深層学習モデルであるが、敵対的攻撃に対して重要なセキュリティ問題がある
- HFLは階層構造のおかげで、ターゲティングされていない訓練時の攻撃に対する堅牢性を持つ
- 特にバックドア攻撃では、悪意のあるクライアントが辺縁サーバーの重複領域に配置されるとHFLのアーキテクチャを悪用する
- 階層的アグリゲーションにより、HFLは推論時の攻撃に対する耐性を強化し、敵対的訓練に適している

HFLのセキュリティについての研究、めっちゃおもしろそう！攻撃自体にも対策が必要なんだし、こんな感じでより安全な連合学習が実現できるのかもしれないね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-08-20 11:34

- - -

### [Federated Clustering: An Unsupervised Cluster-Wise Training for Decentralized Data Distributions](http://arxiv.org/abs/2408.10664)

**連合クラスタリング：分散データのための教師なしクラスターワイズトレーニング**

Mirko Nardi, Lorenzo Valerio, Andrea Passarella

- 連合学習はデータプライバシーが重要な場面で中心的なアプローチだが、教師なし学習の可能性は未探索
- FedCRefは異なるクライアント間で協調してクラスタデータをトレーニングし、再構成誤差分析で比較
- クライアントはデータ分布のセット内で共同トレーニングを行い、ローカルクラスタを継続的に精緻化
- EMNISTとKMNISTデータセットでの実験により、FedCRefが実際のデータ分布にクラスタモデルを整合させる能力を示した

なんかおもしろそうだよね、FedCRefっていかにも最新技術って感じだし、どんなふうに役立つのかもっと知りたくなっちゃうね。実験結果もすっごく興味深い！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-20 09:05

- - -

### [REInstruct: Building Instruction Data from Unlabeled Corpus](http://arxiv.org/abs/2408.10663)

**REInstruct: 未ラベルコーパスからのインストラクションデータ構築**

Shu Chen, Xinyan Guan, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun

- インストラクションデータの手動アノテーションは困難であり、コストがかかりスケールしにくい
- 現在の自動アノテーション手法は専有LLMに依存するが、品質と著作権問題がある
- REInstructは、未ラベルコーパスから自動でインストラクションデータを生成する新手法を提案
- REInstructで生成したデータでトレーニングしたモデルがAlpacaEvalで高い評価を獲得

この研究、特に手動アノテーションなしで効果的なデータ生成の部分がすごく面白そう！REInstructの手法が他の問題にも応用できそうだよね。

**Comment:** Accepted by ACL2024 Findings

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-08-20 09:05

- - -

### [Differentially Private Stochastic Gradient Descent with Fixed-Size Minibatches: Tighter RDP Guarantees with or without Replacement](http://arxiv.org/abs/2408.10456)

**差分プライバシー付き確率的勾配降下法における固定サイズミニバッチ: 置き換え有無に関係なく緊密なRDP保証**

Jeremiah Birrell, Reza Ebrahimi, Rouzbeh Behnia, Jason Pacheco

- 差分プライバシー付きSGDがプライバシー保護の下で深層学習モデルを訓練
- 固定サイズサブサンプリングは一定のメモリ使用量で魅力的
- 提案するRDPアカウンタントが現行の境界を4倍改善
- 固定サイズサンプリングが実践でメモリ使用と低い分散を実現

学習中のプライバシー損失がしっかり管理できるってすごく安心だよね！固定サイズの方が実用的で結果も良かったら、ますます取り入れられそう！

**Comment:** 39 pages, 10 figures

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-08-19 23:57

- - -

### [Federated Learning of Large ASR Models in the Real World](http://arxiv.org/abs/2408.10443)

**現実の世界における大規模なASRモデルの連合学習**

Yonghui Xiao, Yuxin Ding, Changwan Ryu, Petr Zadrazil, Francoise Beaufays

- 連合学習（FL）はプライバシー保護の機械学習に有望な結果を見せている
- 1億以上のパラメータを持つ大規模モデルのトレーニングは、リソース要件が障害に
- ConformerベースのASRの全サイズモデル130MパラメータをFLでトレーニングする体系的な解決策を提示
- 提案された方法でクライアントのデータとラベルの品質を精査し、モデルの品質向上を実現

大規模なモデルにも連合学習が使えるって、すごく現実的になってきたね！改善されたトレーニング方法で、これからもっと高品質なモデルができるかも～！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CL, cs.SD, eess.AS, **投稿日時:** 2024-08-19 22:44

- - -

### [Value Alignment from Unstructured Text](http://arxiv.org/abs/2408.10392)

**非構造化テキストからの価値整合**

Inkit Padhi, Karthikeyan Natesan Ramamurthy, Prasanna Sattigeri, Manish Nagireddy, Pierre Dognin, Kush R. Varshney

- 大規模言語モデル（LLM）を価値システムに整合させる研究が重要視されている
- この整合には、高品質な監督データや好みデータが必要で、手間がかかり高額
- 合成データ生成技術を用いて、非構造化データにおける価値にモデルを整合させる手法を提案
- ２つのユースケースを通じて手法の有効性を実証し、他手法よりも優れた結果を示す

非構造化テキストからの価値整合って面白そう！合成データで効率アップしちゃうなんて、未来の研究にも大きな影響ありそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-08-19 20:22

- - -

### [DELIA: Diversity-Enhanced Learning for Instruction Adaptation in Large Language Models](http://arxiv.org/abs/2408.10841)

**DELIA: 大規模言語モデルにおける指示適応のための多様性強化学習**

Yuanhao Zeng, Fei Ren, Xinpeng Zhou, Yihang Wang, Yingxia Shao

- 指示チューニングは大規模言語モデルの特定タスク形式に適合させるプロセスで、新たな知識や能力は獲得しにくい
- 指示チューニングで学習される特徴がバイアスされているため、理想的なタスク固有の特徴とは異なり、下流タスクにおけるセマンティクス学習が制限される
- DELIAは多様なデータを利用し、指示チューニングのバイアスされた特徴を理想的な特徴の近似に変換することで、この問題を解決
- DELIAは一般的な指示チューニングと比較し、翻訳タスクで17.07%-33.41%の性能向上を達成し、フォーマット化テキスト生成では36.1%の精度向上を実現

多様なデータを活かして問題解決するのって、面白そう！成果が圧倒的に良いから、これからのLLMの進化がとても楽しみだね。

**Comment:** 8 pages, 5 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, **投稿日時:** 2024-08-19 17:56

- - -

### [FEDKIM: Adaptive Federated Knowledge Injection into Medical Foundation Models](http://arxiv.org/abs/2408.10276)

**FEDKIM: 医療基盤モデルへの適応的な連合知識注入**

Xiaochen Wang, Jiaqi Wang, Houping Xiao, Jinghui Chen, Fenglong Ma

- 基盤モデルは多様なモダリティに対応し、従来のAI手法を上回る
- 医療分野では多様なモダリティと厳しいプライバシー規制が課題
- 本研究は連合学習フレームワークでの知識注入法FedKIMを提案
- FedKIMはプライバシーを保ちながら多様な医療タスクの処理能力向上を実現

医療分野でのプライバシー保護をしながら性能を上げる手法ってすごく未来感あるね！FedKIMのおかげで、もっと安全に医療AIが進化しそうで楽しみだな。

**Comment:** Submitted to EMNLP'24

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-17 15:42

- - -

### [FedKBP: Federated dose prediction framework for knowledge-based planning in radiation therapy](http://arxiv.org/abs/2408.10275)

**FedKBP: 連合学習による放射線治療の知識ベース計画における線量予測フレームワーク**

Jingyun Chen, Martin King, Yading Yuan

- 線量予測は、患者ごとの線量分布を自動生成する知識ベース計画で重要
- 連合学習（FL）は、患者データのプライバシーを保ちながら深層学習モデルを共同訓練
- IIDデータ分割では、FLの性能は中央集約型の訓練に匹敵
- 非IIDデータ分割では、データ分布の偏りが性能に影響を与える

連合学習って、特にデータが偏っているサイト間でどうやって改善していくかが面白そうだね！デザイン次第で、みんなで協力すれば最高の結果を出せるかもって感じがする。

**Comment:** Under review by SPIE Medical Imaging 2025 Conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-17 14:57
