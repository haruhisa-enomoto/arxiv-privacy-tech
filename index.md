---
layout: single
title: トップページ
permalink: /
author_profile: true
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

To be written.

## 最新更新分

更新: 2024-04-28T04:16:33.182869

- - -

### [Privacy-Preserving Statistical Data Generation: Application to Sepsis Detection](http://arxiv.org/abs/2404.16638)

**プライバシー保護型統計データ生成：敗血症検出への応用**

Eric Macias-Fassio, Aythami Morales, Cristina Pruenza, Julian Fierrez

- 医療分野ではAIとデータ保護法の規制増加が影響を与えており、患者情報の機密性が高い
- 本研究では、合成データ生成のための統計的アプローチを提案し、敗血症検出の分類問題に適用
- 生成された合成データの有用性とプライバシーの影響を実世界で評価し、KDE-KNN法による合成データ生成が有効であることを強調
- 合成データをモデルトレーニング手順に含めることの効果を検討し、規制制約を緩和する手法としての有益性を示す



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-04-25 14:26

- - -

### [Zero-Shot Distillation for Image Encoders: How to Make Effective Use of Synthetic Data](http://arxiv.org/abs/2404.16637)

**画像エンコーダーのためのゼロショット蒸留: 合成データの効果的な利用方法**

Niclas Popp, Jan Hendrik Metzen, Matthias Hein

- CLIPのような多モード基盤モデルはゼロショット能力に優れているが、リソース制約環境での適用がパラメータ数と高い推論時間のために限定される
- 合成データの使用は、大規模な教師モデルからの表現を蒸留する際に有望であり、少数ショットやリニアプローブ性能が向上する
- 対照損失を使用する場合にゼロショット設定でのアプローチが意外にも失敗することを発見し、合成データと実データ間の一般化の悪さの原因として偽特徴の利用を特定
- 画像特徴ベースのL2蒸留損失を使用することで、問題を緩和し、最大92％少ないパラメータでDataCompXLに訓練されたViT-B/32教師モデルと同等のゼロショット性能を実現する学生モデルを訓練



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-25 14:24

- - -

### [Large Language Models Perform on Par with Experts Identifying Mental Health Factors in Adolescent Online Forums](http://arxiv.org/abs/2404.16461)

**大規模言語モデルは、思春期のオンラインフォーラムにおける精神健康要因の特定において専門家と同等の性能を発揮する**

Isablle Lorge, Dam W. Joyce, Andrey Kormilitzin

- 最近の大規模言語モデル（LLMs）は、監視や介入のコストと時間効率を向上させることが期待されている
- Redditの12歳から19歳の青少年の投稿から新たなデータセットを作成し、精神疾患のカテゴリー（トラウマ、不安定性、状態、症状、自殺性、治療）について専門家の精神科医が注釈
- GPT3.5とGPT4という2つの優れたLLMを使用し、専門家のラベリングと比較
- GPT4は人間の注釈者間の合意やパフォーマンスに匹敵し、合成データ上ではさらに高いパフォーマンスを示すが、否定や事実関連の問題で時折間違えることがある



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-04-25 09:42

- - -

### [Constructing Optimal Noise Channels for Enhanced Robustness in Quantum Machine Learning](http://arxiv.org/abs/2404.16417)

**量子機械学習における最適化されたノイズチャネルの構築とその堅牢性向上**

David Winderl, Nicola Franco, Jeanette Miriam Lorenz

- 量子ノイズチャネルと差分プライバシーの関連を明らかにし、$(\alpha, \gamma)$-チャネルとして一連のノイズチャネルを提案
- $(\alpha, \gamma)$-チャネルを使用して、消極的ノイズおよびランダム回転チャネルで観察される$\epsilon$-DPの境界を再現
- 半定義プログラミングを使用して最適な堅牢性を持つチャネルを構築
- 実験評価で、最適化ノイズチャネルが消極的ノイズよりも対向精度の向上に寄与することを示示



**トピック:** [差分プライバシー](dp), **カテゴリ:** quant-ph, cs.AI, cs.LG, **投稿日時:** 2024-04-25 08:49

- - -

### [Reverse engineering the brain input: Network control theory to identify cognitive task-related control nodes](http://arxiv.org/abs/2404.16357)

**脳への入力の逆工学：認知タスクに関連する制御ノードを特定するためのネットワーク制御理論**

Zhichao Liang, Yinuo Zhang, Jushen Wu, Quanying Liu

- 認知タスク実行中の脳への入力特定のためのフレームワークを提案
- 合成データを使用してフレームワークの有効性を検証し、入力を確実に再構築可能であることを示す
- 実際のヒトの運動課題fMRIデータにフレームワークを適用し、ニューラルダイナミクスを再現
- モデルは28の制御ノードを特定し、それらは主に運動システムと重なる



**トピック:** [合成データ](sd), **カテゴリ:** q-bio.NC, cs.SY, eess.SY, **投稿日時:** 2024-04-25 06:36

- - -

### [FedStyle: Style-Based Federated Learning Crowdsourcing Framework for Art Commissions](http://arxiv.org/abs/2404.16336)

**FedStyle: 芸術委託のためのスタイルベースの連合学習クラウドソーシングフレームワーク**

Changjuan Ran, Yeting Guo, Fang Liu, Shenglan Cui, Yunfan Ye

- 芸術家のユニークなスタイルを重視し、個人の作品を晒すことなくスタイルベースの検索を実現するために、FedStyleという新しいフレームワークを提案
- 芸術家はローカルでスタイルモデルを訓練し、作品ではなくモデルパラメータを共有することで協力する
- 異なる芸術家間でのモデルドリフトの問題に対処するため、抽象的なスタイル表現を学び、サーバーとの整合を取る
- 対照学習を導入し、似たスタイルの作品を近づけ、異なるものを分離するスタイル表現空間を慎重に構築

**Comment:** Accepted to ICME 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-04-25 04:53

- - -

### [Differentially Private Federated Learning: Servers Trustworthiness, Estimation, and Statistical Inference](http://arxiv.org/abs/2404.16287)

**差分プライバシーを用いた連合学習：サーバーの信頼性、推定、および統計的推論**

Zhe Zhang, Ryumei Nakada, Linjun Zhang

- 信頼できない中央サーバーを含むシナリオでは、高次元問題における正確な推定が困難であることが示された
- データの高次元性に基づく厳密なミニマックスレートが、疎性を仮定しても変化する
- 信頼できる中央サーバーを持つシナリオで線形回帰モデルに特化した新しい連合推定アルゴリズムを提案
- 統計的推論のための手法も提案しており、個々のパラメーターに対する座標ごとの信頼区間や同時推論の戦略が含まれる

**Comment:** 56 pages, 3 figures

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.CR, cs.LG, math.ST, stat.ME, stat.TH, **投稿日時:** 2024-04-25 02:14

- - -

### [Enhancing Privacy in Face Analytics Using Fully Homomorphic Encryption](http://arxiv.org/abs/2404.16255)

**顔分析におけるプライバシーの強化：全準同型暗号を用いたアプローチ**

Bharat Yalavarthi, Arjun Ramesh Kaushik, Arun Ross, Vishnu Boddeti, Nalini Ratha

- 現代の顔認識システムはディープネットワークを使用して顔の重要な特徴を抽出し、テンプレートとして格納
- これらのテンプレートはデータ漏洩のリスクがあり、顔画像の再構築に使用される可能性がある
- 全準同型暗号（FHE）とPolyProtectという既存の保護スキームを組み合わせた新技術を提案
- 提案技術は認識精度を損なうことなく、顔の埋め込みからのソフトバイオメトリック属性の漏洩を効果的に防止



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.CV, **投稿日時:** 2024-04-24 23:56

- - -

### [SECO: Secure Inference With Model Splitting Across Multi-Server Hierarchy](http://arxiv.org/abs/2404.16232)

**SECO: 複数のサーバ階層にわたるモデル分割を利用した安全な推論**

Shuangyi Chen, Ashish Khisti

- SECOは複数のサーバノードを使用し、ニューラルネットワークモデルを分割してデータのプライバシーを保護しながら予測計算を行うプロトコルである
- 従来の単一サーバノード上での全モデル配置から複数サーバ階層への拡張を実現し、ユーザーからゲートウェイサーバを経てリモートサーバへ通信する
- 複数方面同型暗号と複数方面ガーブドサーキット手法を採用し、半正直なサーバの不正多数に対しても安全なシステムを構築
- SECOを複数のモデルで評価し、ユーザーの計算と通信コストを削減し、リソースに制限のあるユーザーデバイスに適用可能



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-04-24 22:24

- - -

### [Blind Federated Learning without initial model](http://arxiv.org/abs/2404.16180)

**連合学習における初期モデルなしのブラインド方式**

Jose L. Salmeron, Irina Arévalo

- 連合学習は、複数の参加者が自身の秘密データを保持しつつモデルを構築する手法
- 本研究では、プライバシーを保護する方法として、Particle Swarm Optimisationを基にしたFuzzy Cognitive Mapsの学習手法を提案
- 連合学習過程で初期モデルを使用しない新しいアプローチを採用、これによりプロセスがブラインド（非依存）化
- 複数の公開データセットを用いたテストで、精度と正確性が向上



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-04-24 20:10

- - -

### [zkLLM: Zero Knowledge Proofs for Large Language Models](http://arxiv.org/abs/2404.16109)

**zkLLM: 大規模言語モデルのためのゼロ知識証明**

Haochen Sun, Jason Li, Hongyang Zhang

- 大規模言語モデル（LLM）の出力の真正性を確立するために、zkLLMという新たなゼロ知識証明を提案
- ディープラーニングにおける非算術演算の課題に対処するために、パラレライズされたルックアップ引数tlookupを導入
- 注意機構専用のゼロ知識証明zkAttnを開発し、実行時間、メモリ使用量、精度のバランスを考慮
- 13億パラメータを持つLLMで完全な推論プロセスの正確性証明を15分未満で生成可能、証明サイズは200kB以下でモデルパラメータのプライバシーを保護

**Comment:** Accepted to ACM CCS 2024, camera-ready version under preparation.   This is the author's version of the work. It is posted here for your personal   use. Not for redistribution

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-04-24 18:04

- - -

### [ORBIT-Surgical: An Open-Simulation Framework for Learning Surgical Augmented Dexterity](http://arxiv.org/abs/2404.16027)

**ORBIT-Surgical: 精度が高く迅速な外科用拡張運動能力学習のためのオープンシミュレーションフレームワーク**

Qinxi Yu, Masoud Moghani, Karthik Dharmarajan, Vincent Schorp, William Chung-Ho Panitch, Jingzhou Liu, Kush Hari, Huang Huang, Mayank Mittal, Ken Goldberg, Animesh Garg

- 物理ベースのシミュレーションを利用して、ドライビング、操作、移動のロボット学習の進歩が促進されているが、外科手術のシミュレーション環境の実現はまだ課題である
- ORBIT-Surgicalは、NVIDIA Omniverse上でリアリスティックなレンダリングを提供する外科ロボットシミュレーションフレームワークを開発し、dVRKとSTARでの標準的な外科研修課題を14項目提供
- シミュレーションから実際のdVRKロボットへのポリシー転移を実証
- GPUの並列処理を活用し、強化学習と模倣学習アルゴリズムのトレーニングを行うことで、人間の外科技術をサポートするロボット学習を研究する支援を提供



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-04-24 17:57

- - -

### [Decentralized Personalized Federated Learning based on a Conditional Sparse-to-Sparser Scheme](http://arxiv.org/abs/2404.15943)

**分散型パーソナライズ連合学習に基づく条件付きスパースからスパーサーへのスキーム**

Qianyu Long, Qiyuan Wang, Christos Anagnostopoulos, Daning Bi

- 分散型連合学習（DFL）はその堅牢性と中央集権的な調整を避ける点で人気がある
- DFLは訓練と通信のコスト増加をもたらすが、既存の手法は訓練効率とデータの異質性をしばしば無視している
- 新たに「スパースからスパーサーへ」の訓練スキームであるDA-DPFLを提案、動的集約を用いて訓練中にモデルパラメーターを段階的に削減しエネルギーコストを大幅に削減
- DA-DPFLはテスト精度において従来のDFLよりも優れており、エネルギーコストを最大5倍削減することが実験で示された

**Comment:** 15 pages, 9 figures, 3 pages theory

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-24 16:03

- - -

### [An Element-Wise Weights Aggregation Method for Federated Learning](http://arxiv.org/abs/2404.15919)

**連合学習における要素毎の重み付け手法**

Yi Hu, Hanchi Ren, Chen Hu, Jingjing Deng, Xianghua Xie

- 連合学習では、クライアントごとに異なるデータ特性を考慮しつつ、各要素に特定の割合を割り当てることが有効である
- 提案された要素毎の重み付け集約手法（EWWA-FL）は、学習性能の最適化と収束速度の加速を目指す
- EWWA-FLは、クライアントが要素レベルで学習プロセスに貢献することを可能にし、グローバルモデルの堅牢性を強化
- 複数の戦略を用いて柔軟に重み付け可能であり、実験を通じて精度と収束速度の向上が示された

**Comment:** 2023 IEEE International Conference on Data Mining Workshops (ICDMW)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-04-24 15:16

- - -

### [Sketch2Human: Deep Human Generation with Disentangled Geometry and Appearance Control](http://arxiv.org/abs/2404.15889)

**Sketch2Human: 人体生成におけるジオメトリと外見制御の分離**

Linzi Qu, Jiaxiang Shang, Hui Ye, Xiaoguang Han, Hongbo Fu

- ジオメトリと外見の両方を制御可能な全身人体画像生成を目指す
- 既存のアプローチは明確な制御が欠けているため、高忠実度と多様性を持つ結果が得られにくい
- Sketch2Humanでは、意味的スケッチと参照画像を用いてジオメトリと外見を制御
- スケッチエンコーダーとStyleGAN-Humanの潜在空間を利用し、新しいトレーニングスキームで学習を行う



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.GR, **投稿日時:** 2024-04-24 14:24

- - -

### [Privacy-Preserving Billing for Local Energy Markets (Long Version)](http://arxiv.org/abs/2404.15886)

**プライバシー保護型地域エネルギーマーケット課金プロトコル（PBP-LEMs）に関する研究**

Eman Alqahtani, Mustafa A. Mustafa

- 地域エネルギーマーケットの参加者が入札からのエネルギー量の逸脱を考慮したプライバシーを保護する課金プロトコルを提案
- マーケットエンティティが分散型でプライバシーを保ちながら参加者の課金を共同で計算できるようにする
- 情報理論的セキュリティを実現する個々の課金スキームを新たに提案し、これを基礎として利用
- 多者計算、ペダーセンコミットメント、内積機能暗号を使用し、データの機密性と正確性を確保



**トピック:** [秘密計算](mpc), **カテゴリ:** cs.CR, **投稿日時:** 2024-04-24 14:12

- - -

### [SynthEval: A Framework for Detailed Utility and Privacy Evaluation of Tabular Synthetic Data](http://arxiv.org/abs/2404.15821)

**SynthEval: 合成データの詳細な有用性とプライバシー評価のためのフレームワーク**

Anton Danholt Lautrup, Tobias Hyrup, Arthur Zimek, Peter Schneider-Kamp

- 合成データの有用性とプライバシーのリスク評価に、新規のオープンソースフレームワークSynthEvalを提案
- SynthEvalは、カテゴリカルおよび数値属性を等しく扱い、特殊な前処理を必要としない
- 統計手法と機械学習技術を利用して、合成データの忠実性とプライバシー保護の完全性を総合的に評価
- 合成データのモデルの能力をより良く比較するためのベンチマークと一貫した比較が可能



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.PF, **投稿日時:** 2024-04-24 11:49

- - -

### [APACHE: A Processing-Near-Memory Architecture for Multi-Scheme Fully Homomorphic Encryption](http://arxiv.org/abs/2404.15819)

**APACHE: マルチスキーム全準同型暗号をサポートするメモリ近傍計算アーキテクチャ**

Lin Ding, Song Bian, Penggao He, Yan Xu, Gang Qu, Jiliang Zhang

- 全準同型暗号(FHE)は計算負荷が非常に高いため、APACHEはマルチスキームFHEの加速を目指すメモリ近傍計算階層を提案
- 異なるFHEスキーム間のデータフローを検証し、計算リソースとメモリ帯域の利用率を向上させるために細粒度の機能単位を持つアーキテクチャを開発
- マルチスキームオペレータコンパイラを提案し、低レベルの機能単位間で高レベルFHE計算を効率的にスケジュール
- 実験結果によれば、APACHEは最新のASIC FHEアクセラレータに比べ、2.4倍から19.8倍の性能向上を達成



**トピック:** [準同型暗号](he), **カテゴリ:** cs.AR, **投稿日時:** 2024-04-24 11:48

- - -

### [Collaborative Heterogeneous Causal Inference Beyond Meta-analysis](http://arxiv.org/abs/2404.15746)

**メタ解析を超える異種協調因果推論**

Tianyu Guo, Sai Praneeth Karimireddy, Michael I. Jordan

- 異なるデータセンター間の協力は、各サイト間の異質性によって困難である
- 従来のメタ解析に基づく方法に代わって、共同逆傾向スコア加重推定子を提案し、異種データで因果推論を行う
- 提案手法は、伝統的なメタ解析ベースの手法よりも異質性が増大した場合の改善を実証
- アウトカムモデルを協調して訓練するための連合学習アルゴリズムを提案し、プライバシーを保護

**Comment:** submitted to ICML

**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.CR, cs.LG, **投稿日時:** 2024-04-24 09:04

- - -

### [Noise Variance Optimization in Differential Privacy: A Game-Theoretic Approach Through Per-Instance Differential Privacy](http://arxiv.org/abs/2404.15686)

**差分プライバシーにおけるノイズ分散の最適化：個別インスタンス差分プライバシーを通じたゲーム理論的アプローチ**

Sehyun Ryu, Jonggyu Jang, Hyun Jong Yang

- 差分プライバシー（DP）は、データセットに個人が含まれることによる分布の変化を観察することでプライバシー損失を定量的に測定する
- 従来のDPメカニズムはケースごとの最悪のシナリオに基づいてプライバシー損失を計算し、小さいデータセットでは過度のノイズが問題となる
- この研究では、個別インスタンスDP（pDP）を制約として利用し、個々のインスタンスに合わせて最適化されたノイズを導入するノイズ分散最適化（NVO）ゲームを提案
- 提案されたpDPアルゴリズムは、従来のDPアルゴリズムと比較してKL分散において最大99.53%の平均性能向上を実証



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-04-24 06:51

- - -

### [FedSI: Federated Subnetwork Inference for Efficient Uncertainty Quantification](http://arxiv.org/abs/2404.15657)

**効率的な不確実性評価のための連合サブネットワーク推論 FedSI**

Hui Chen, Hengyu Liu, Zhangkai Wu, Xuhui Fan, Longbing Cao

- 深層ニューラルネットワークを用いたパーソナライズされた連合学習はデータの多様性に対応するが、効率的な体系的不確実性の評価には課題がある
- 既存のベイジアンDNNベースのPFLは、モデル構造が過度に単純化されているか、計算コストとメモリコストが高いとされる
- FedSIは、ベイジアン手法を利用して体系的不確実性を効果的に取り込むことで、シンプルかつスケーラブルな新しいフレームワークである
- FedSIはクライアント特有のサブネットワーク推論メカニズムを用い、体系的不確実性を最大限に保持しつつ、速やかでスケーラブルな推論を実現する



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-24 05:24

- - -

### [FEDSTR: Money-In AI-Out | A Decentralized Marketplace for Federated Learning and LLM Training on the NOSTR Protocol](http://arxiv.org/abs/2404.15834)

**FEDSTR: Money-In AI-Out | NOSTRプロトコル上での連合学習とLLMトレーニングのための分散型マーケットプレイス**

Konstantinos E. Nikolakakis, George Chantzialexiou, Dionysis Kalogerias

- NOSTRは社会的ウェブ用に設計された通信プロトコルで、w3cのウェブソケット標準に基づいている
- 提案されたデザインでは、顧客はトレーニング用のデータセットを提供し、サービスプロバイダーはそのデータセットを用いてAIモデルをトレーニングし、最適化されたAIモデルを報酬と交換に返す
- NOSTRの分散型および検閲抵抗性の特徴を活用して、AIモデルおよびLLMのトレーニング用に公正でオープンなマーケットプレイスを設計することが可能
- このマーケットプレイスは連合学習とLLMトレーニングのために特に設計されている

**Comment:** 19 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.AI, cs.CR, cs.LG, **投稿日時:** 2024-04-15 20:51

- - -

### [Implications of computer science theory for the simulation hypothesis](http://arxiv.org/abs/2404.16050)

**コンピュータ科学理論がシミュレーション仮説に及ぼす影響**

David H. Wolpert

- 物理学と哲学のコミュニティでシミュレーション仮説に対する関心が再び高まっている
- 物理的な宇宙をシミュレートするコンピュータに関連するため、コンピュータ科学理論と物理学を結合する必要がある
- クリーンの第二再帰定理に基づき、私たちによって実行されるコンピュータ上で私たちがシミュレーションされている可能性が数学的に証明されている
- ライスの定理はシミュレーションおよび自己シミュレーションに関するいくつかの興味深い不可能性の結果を提供する

**Comment:** 44 pages of text, 5 pages of references, 10 pages of appendices

**トピック:** [準同型暗号](he), **カテゴリ:** cs.LO, physics.hist-ph, F.1; F.m, **投稿日時:** 2024-04-09 18:39
