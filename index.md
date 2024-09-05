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

更新: 2024-09-05T04:22:22.824146

- - -

### [RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins (early version)](http://arxiv.org/abs/2409.02920)

**RoboTwin: 生成的デジタルツインを用いた二腕ロボットベンチマーク（初期版）**

Yao Mu, Tianxing Chen, Shijia Peng, Zanxin Chen, Zeyu Gao, Yude Zou, Lunkai Lin, Zhiqiang Xie, Ping Luo

- デュアルアームロボットの効果的な協力とツール使用能力が重要な研究分野
- デジタルツインから生成された合成データと実世界のテレオペレートデータを組み合わせた新しいベンチマーク「RoboTwin」を提案
- COBOT Magicプラットフォームを使用して、多様なツール使用データと人とロボットの相互作用データを収集
- AI生成コンテンツを用いて2D画像を詳細な3Dモデルに変換し、大規模言語モデルを利用して専門レベルの訓練データとタスク特有の姿勢シーケンスを生成

デュアルアームロボットがもっと賢くなる感じ！特に2D画像が3Dになるところワクワクするね。これでロボットの進化が加速しそう！

**Comment:** Project page: https://robotwin-benchmark.github.io/early-version/

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.AI, cs.CL, **投稿日時:** 2024-09-04 17:59

- - -

### [The Impact of Balancing Real and Synthetic Data on Accuracy and Fairness in Face Recognition](http://arxiv.org/abs/2409.02867)

**顔認識における精度と公平性に対する実データと合成データのバランスの影響**

Andrea Atzori, Pietro Cosseddu, Gianni Fenu, Mirko Marras

- 実データはウェブから取得されることが多く、ユーザー同意の欠如によるプライバシー問題を引き起こす
- 異なる人口群からの画像分布の自然な不均衡により、バランスの取れた大規模データセットの取得は困難
- 拡散ベースのモデルで生成したデータを用いると、単独や実データと組み合わせた場合でも精度が向上
- 事前訓練された生成方法でバランスを取ったデータは公平性にほとんど影響を与えず、場合によっては逆効果を生じる

実データと合成データを組み合わせることで精度が上がるのはすごいね。でも公平性が保たれないのは、まだまだ課題が多いなって感じるな。これからどう改善されるのかワクワクする！

**Comment:** Accepted at Synthetic Data for Computer Vision Workshop - Side Event   at ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-04 16:50

- - -

### [Key Compression Limits for -Minimum Value Sketches](http://arxiv.org/abs/2409.02852)

** $k$-最小値スケッチのためのキー圧縮限界 **

Charlie Dickens, Eric Bax, Alexander Saydakov

- $k$-最小値スケッチアルゴリズムは、データセット内のアイテムをハッシュ化して生成された$k$最小のハッシュキーを保存する方法である
- 順序と連続する差分のエンコーディングを基にした圧縮が、キーごとに期待される保存容量を$O(\log n)$ビット削減できることを示した
- $k$個の最小値を$n$個のランダム値から圧縮する場合、$O(\log n)$のビット節約が最適であり、このエンコーディング方法がほぼ最適であることを証明
- 実際に計算効率的な圧縮方法を提示し、理論的最小限に比べて5%以内の平均節約率を達成することを実証

圧縮技術ってすごく興味深いよね！特にこの研究だと実際のデータと合成データでの性能も示してるから、色んなデータセットでも試してみたくなるよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.DS, cs.IT, math.IT, **投稿日時:** 2024-09-04 16:22

- - -

### [Obsidian: Cooperative State-Space Exploration for Performant Inference on Secure ML Accelerators](http://arxiv.org/abs/2409.02817)

**Obsidian: 安全な機械学習アクセラレータ上での効率的推論のための協調的状態空間探索**

Sarbartha Banerjee, Shijia Wei, Prakash Ramrakhyani, Mohit Tiwari

- TEE（Trusted Execution Environment）は、安全で効率的な機械学習推論に不可欠
- Obsidianは、安全なMLアクセラレータへの最適なマッピングを探すための最適化フレームワーク
- 分析モデルとサイクル精度モデルを協調的に用いることで、探索空間を効果的に探索
- ラテンシとエネルギー消費の改善を達成し、クラウドとエッジでのパフォーマンスを大幅に向上

この研究、なんだか面白そう！Obsidianがエッジとクラウドの両方でどれだけ効率を上げるか、期待しちゃうね。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-09-04 15:35

- - -

### [A Joint Time and Energy-Efficient Federated Learning-based Computation Offloading Method for Mobile Edge Computing](http://arxiv.org/abs/2409.02548)

**モバイルエッジコンピューティングのための時間とエネルギー効率の高い連合学習ベースの計算オフローディング方法**

Anwesha Mukherjee, Rajkumar Buyya

- 連合学習を用いたオフローディング意思決定モデルを提案
- モデルはタスクが計算集約的かどうかを予測し、適切にオフローディングする
- 提案手法は実験環境で90%以上の予測精度を達成
- 計算集約的タスクの応答時間とエネルギー消費を11-31%削減

エッジコンピューティングって、本当便利なんだね！しかも予測精度も高いし、すごく面白そう！これからのモバイルアプリにどんな影響を与えるか楽しみだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-09-04 09:10

- - -

### [CoAst: Validation-Free Contribution Assessment for Federated Learning based on Cross-Round Valuation](http://arxiv.org/abs/2409.02495)

**CoAst: 連合学習における交差ラウンド評価に基づくバリデーション不要の貢献度評価**

Hao Wu, Likun Zhang, Shucheng Li, Fengyuan Xu, Sheng Zhong

- 連合学習では、参加者が保持するデータが異なるため、各参加者のモデルへの貢献度を評価する必要がある
- バリデーションデータ不要の既存手法は、一回の訓練ラウンドのパラメータと勾配の乱数性に影響を受けやすい
- 提案手法CoAstは、モデルパラメータの重要部分の重み付け量子化と、いくつかの通信ラウンドにおけるローカルとグローバルなパラメータ更新の類似性に基づいて評価を行う
- 実験結果として、CoAstは既存のバリデーションベース手法に匹敵する評価信頼性を持ち、バリデーション不要手法を上回る性能を示した

バリデーションデータがなくても精度良く貢献度が測れるなんて、めちゃ効率いいね！これで連合学習の参加者がもっと集まれば、どんどん使えるモデルが増えそうだよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-04 07:46

- - -

### [Learning Privacy-Preserving Student Networks via Discriminative-Generative Distillation](http://arxiv.org/abs/2409.02404)

**識別生成蒸留を通じたプライバシー保護学生ネットワークの学習**

Shiming Ge, Bochao Liu, Pengju Wang, Yong Li, Dan Zeng

- 深層学習モデルは大規模なデータから豊富な知識を学習できるが、プライバシー漏洩のリスクがある
- プライバシー保護型のモデル学習を実現するため、識別生成蒸留アプローチを提案
- データのない環境で生成器を訓練し、生成された合成データを用いてVAEを訓練
- 少数の合成データのラベルは差分プライベートな集約で教師モデルから取得し、多数のデータはVAEで再生成

識別生成蒸留アプローチってすごく興味深いよね！これなら、プライバシーを守りつつ高精度のモデルを学習できるかも！

**Comment:** This paper is accepted by IEEE Transactions on Image Processing (TIP)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-09-04 03:06

- - -

### [Building Math Agents with Multi-Turn Iterative Preference Learning](http://arxiv.org/abs/2409.02392)

**多ターン反復 préférence学習で構築する数学エージェント**

Wei Xiong, Chengshuai Shi, Jiaming Shen, Aviv Rosenberg, Zhen Qin, Daniele Calandriello, Misha Khalman, Rishabh Joshi, Bilal Piot, Mohammad Saleh, Chi Jin, Tong Zhang, Tianqi Liu

- 大規模言語モデルの数学解決能力を外部ツールと多ターンChain-of-Thought推論で強化する方法
- 現在の方法は合成データ生成とスーパー識別学習に焦点を当てている
- 既存の直接preference学習は一回のみのチャットタスク向けで多ターン推論に対応しない
- 提案された多ターン直接preference学習フレームワークが性能を改善

数学の問題解決能力を外部ツールでどんどん強化するなんて面白そう！今までの方法を改善して、具体的な数値での成果が示されてるのも信頼できる研究だね。

**Comment:** A multi-turn direct preference learning framework for tool-integrated   reasoning tasks

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-09-04 02:41

- - -

### [Robust Federated Finetuning of Foundation Models via Alternating Minimization of LoRA](http://arxiv.org/abs/2409.02346)

**LoRAによる基盤モデルの強靭な連合微調整と交互最小化**

Shuangyi Chen, Yue Ju, Hardik Dalal, Zhongwen Zhu, Ashish Khisti

- パラメータ効率の良いファインチューニング（PEFT）は少数のモデルパラメータを更新し、計算とメモリの負担を大幅に削減
- PEFTは連合学習において通信量を減少させるためにも有効であり、更新のサイズに依存する
- 既存のPEFTとLoRAを連合微調整に統合する従来の研究の制約を分析
- RoLoRAはLoRAの交互最小化アプローチを利用し、データの異質性や微調整パラメータの減少に対する強靭性を提供 

新しい手法が連合学習の効率と強靭性をどう改善するか、すごく興味深いね！これからの連合学習の可能性が広がりそうでワクワクしちゃう。

**Comment:** Presented at ES-FOMO-II@ICML2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-09-04 00:20

- - -

### [Arctic-SnowCoder: Demystifying High-Quality Data in Code Pretraining](http://arxiv.org/abs/2409.02326)

**Arctic-SnowCoder: コードプレトレーニングにおける高品質データの解明**

Yuxiang Wei, Hojae Han, Rajhans Samdani

- コードドメインでデータ効率の良いベースモデルArctic-SnowCoder-1.3Bを紹介
- 3段階の精緻化されたデータを用いて555Bトークンでプレトレーニング
- 少ないデータセットに基づくが、BigCodeBenchでベストパフォーマンスを達成
- 高品質データの鍵は下流アプリケーションの分布に一致することだと判明

少ないデータで高性能とか、めちゃくちゃ効率いいじゃん！データの質がどれだけ大事か、実感わくね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-09-03 22:36

- - -

### [A Lesion-aware Edge-based Graph Neural Network for Predicting Language Ability in Patients with Post-stroke Aphasia](http://arxiv.org/abs/2409.02303)

**病変認識エッジベースのグラフニューラルネットワークによる脳卒中後の失語症患者の言語能力予測**

Zijian Chen, Maria Varkanitsa, Prakash Ishwar, Janusz Konrad, Margrit Betke, Swathi Kiran, Archana Venkataraman

- 病変認識グラフニューラルネットワーク(LEGNet)を提案し、rs-fMRIの接続性から言語能力を予測
- 機能的接続をエンコードするエッジベース学習、病変をエンコードするモジュール、サブグラフ学習モジュールを統合
- Human Connectome Projectの合成データを使用し、ハイパーパラメータ調整とモデルの事前学習を実施
- 自社データセットでの10分割交差検証により、LEGNetが言語能力予測において基準のディープラーニング方法を上回る性能を示す

脳卒中後の失語症患者の言語能力を予測する新しいモデルが登場したんだって！この技術、将来的にもっと多くの人を助けることができるようになるかもしれないね。超楽しみ～！

**Comment:** Accepted at MICCAI 2024 International Workshop on Machine Learning in   Clinical Neuroimaging (MLCN)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, eess.SP, q-bio.NC, **投稿日時:** 2024-09-03 21:28

- - -

### [K-Origins: Better Colour Quantification for Neural Networks](http://arxiv.org/abs/2409.02281)

**K-Origins: ニューラルネットワークのためのより良い色の定量化**

Lewis Mason, Mark Martinez

- K-Originsは、色や強度の学習が有益な場合に画像ベースのネットワーク性能を向上させるニューラルネットワーク層
- 250以上のエンコーダ・デコーダ型畳み込みネットワークが16ビットの合成データで訓練され、K-Originsが物体検出と色違いの形状が同一の物体のセグメンテーションで精度を向上させる
- K-Originsは、入力特徴$\textbf{X}$から出力特徴$\textbf{Y}_k = \textbf{X}-\textbf{J}\cdot w_k$を生成する
- 受容野の長さが対象クラスのサイズを越えるべきことを示唆、十分な受容野の長さとK-Originsの併用でより良いセマンティックネットワーク性能を実現

色の微妙な違いとかもキャッチできるなんてすごいね。16ビットの合成データでこれほど精密な検出ができるって未来の可能性を感じちゃう。

**Comment:** 16 pages, 13 figures, 1 table

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-09-03 20:28

- - -

### [Collaboratively Learning Federated Models from Noisy Decentralized Data](http://arxiv.org/abs/2409.02189)

**ノイズの多い分散データから連合モデルを協力的に学習する方法**

Haoyuan Li, Mathias Funk, Nezihe Merve Gürel, Aaqib Saeed

- 連合学習(FL)はエッジデバイスからの分散データを使用し、データを分散したまま機械学習モデルを訓練
- ローカルクライアントから提供されるデータの質が問題となり、ノイズや摂動により集約プロセスが困難
- ノイズの入った入力データを識別する手法を提案し、低品質データを持つクライアントを初期段階で特定
- 提案手法Federated Noise-Sifting(FedNS)は既存のFL戦略と統合可能で、IID設定で最大13.68%、非IID設定で最大15.85%の性能向上

ノイズのあるデータでもちゃんと学習できる方法がこれからどんどん進化していきそうだね！すごく実用的だし、もっと色んな分野で使われるようになるかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-03 18:00

- - -

### [Towards Real-World Adverse Weather Image Restoration: Enhancing Clearness and Semantics with Vision-Language Models](http://arxiv.org/abs/2409.02101)

**現実世界の悪天候画像復元に向けて: ビジョン-言語モデルを用いた明瞭度とセマンティクスの向上**

Jiaqi Xu, Mengyang Wu, Xiaowei Hu, Chi-Wing Fu, Qi Dou, Pheng-Ann Heng

- 合成データで訓練された悪天候画像復元手法は、現実世界での適用に限界がある
- ビジョン-言語モデルを用いた半教師あり学習フレームワークを提案し、多様な悪天候条件での復元性能を向上させる
- 明瞭度向上には、ビジョン-言語モデルによる疑似ラベル評価と天気プロンプト学習を用いる
- セマンティクス向上には、現実世界データを統合し、天気条件をビジョン-言語モデルの記述で調整しつつ意味を保持する

悪天候の中でもクリアな画像が得られるなんて、めっちゃ便利だと思わない? 今後のお天気撮影には必須かもね!

**Comment:** Accepted by ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.MM, **投稿日時:** 2024-09-03 17:56

- - -

### [Synthetic Data Generation and Automated Multidimensional Data Labeling for AI/ML in General and Circular Coordinates](http://arxiv.org/abs/2409.02079)

**AI/MLのための合成データ生成と自動多次元データラベリングに関する研究**

Alice Williams, Boris Kovalerchuk

- トレーニングデータの不足がAI/MLモデルの開発と展開の主要課題
- 合成データ生成（SDG）と自動データラベリング（ADL）の統合アプローチを提案
- 一般座標系（GLCs）を用いた多次元データの可視化と逆変換性を活用
- 動的座標可視化システム（DCVis）により、分類器への影響を実ケーススタディで評価

新しい方法でデータ不足を克服できそうでワクワクするね！AI/MLの進化にどれだけ影響を与えるのか、もっと知りたいな！

**Comment:** 8 pages, 17 figures, 11 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-03 17:26

- - -

### [FedMinds: Privacy-Preserving Personalized Brain Visual Decoding](http://arxiv.org/abs/2409.02044)

**FedMinds: プライバシー保護を活用した個別脳視覚デコーディング**

Guangyin Bao, Duoqian Miao

- 脳の研究における視覚情報デコーディングのために、従来のモデルはfMRIデータを中央に保存する必要がある
- プライバシー問題を解決するため、新しいフレームワーク「FedMinds」を提案
- FedMindsは連合学習を使用し、各被験者の個別アダプターを導入することで個別の視覚デコーディングが可能
- 権威あるNSDデータセットを用いた実験で、高精度な視覚デコーディングとプライバシー保護を達成

実際に脳データを守りながら視覚情報をデコードするなんて、未来っぽくてワクワクする！これはプライバシー技術の次の大きな一歩かもね。

**Comment:** 5 pages, Accepted by JCRAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** q-bio.NC, cs.CV, cs.DC, eess.IV, **投稿日時:** 2024-09-03 16:46

- - -

### [Benchmarking ZK-Friendly Hash Functions and SNARK Proving Systems for EVM-compatible Blockchains](http://arxiv.org/abs/2409.01976)

**EVM互換ブロックチェーン向けのZKフレンドリーハッシュ関数とSNARK証明システムのベンチマーク**

Hanze Guo, Yebo Feng, Cong Wu, Zengpeng Li, Jiahua Xu

- ZKツールのベンチマークは、ゼロ知識証明の急速な発展に伴い重要である
- プライバシー保護トランザクションプロトコルの効率改善のために「バッチ処理」を提案
- Poseidon2ハッシュ関数は、予算削減と処理時間短縮において優れている
- Poseidon2ハッシュ関数は、EVMチェーンでオンチェインコストを73%、Hederaでは26%削減することができた

この論文、Poseidon2の使い方でコスト削減してるのがすごいね！私たちのプライバシーを守りながら、もっと効率的なブロックチェーンが実現できるかもって思ったよ。



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-03 15:19

- - -

### [Private Electronic Payments with Self-Custody and Zero-Knowledge Verified Reissuance](http://arxiv.org/abs/2409.01958)

**自己管理型プライベート電子決済とゼロ知識検証リイシュアンス**

Daniele Friolo, Geoffrey Goodell, Dann Toliver, Hazem Danny Nakib

- ゼロ知識証明と監査ログを組み合わせて、決済資産の検証を行うプロトコルを提案
- 発行者以外が新たな資産を作成できないようにするルールの遵守を保証
- 取引履歴の情報漏洩リスクを防ぎ、支払者の匿名性を強力に保護
- デジタル資産の安全な保管や取引履歴の流出リスクに対処する必要性を強調

資産を使っても個人情報が漏れない仕組みだって！未来はもっと安心して電子決済ができるようになるから楽しみだね！

**Comment:** 19 pages, 3 figures

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.CY, **投稿日時:** 2024-09-03 14:56

- - -

### [Securing Federated Learning in Robot Swarms using Blockchain Technology](http://arxiv.org/abs/2409.01900)

**ブロックチェーン技術を用いたロボット群連合学習のセキュリティ確保**

Alexandre Pacheco, Sébastien De Vos, Andreagiovanni Reina, Marco Dorigo, Volker Strobel

- 連合学習は通信要件の削減とコスト分散が利点である
- セントラルサーバーなしでデータを集約するためにブロックチェーン技術を利用
- 故障したロボットが学習プロセスを大きく乱す可能性がある
- Ethereumブロックチェーンを用いて、スマートコントラクトで保護メカニズムを実装

これはめっちゃ面白そう！ロボット群が自律的に学習しながら安全にデータを同期できるなんて、未来のテクノロジーって感じでワクワクするよね。

**Comment:** To be published in the Proceedings of the 17th International   Symposium on Distributed Autonomous Robotic Systems (DARS 2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, **投稿日時:** 2024-09-03 13:43

- - -

### [What are the Essential Factors in Crafting Effective Long Context Multi-Hop Instruction Datasets? Insights and Best Practices](http://arxiv.org/abs/2409.01893)

**効果的な長文コンテキストマルチホップ指示データセット作成の重要要因: 洞察とベストプラクティス**

Zhi Chen, Qiguang Chen, Libo Qin, Qipeng Guo, Haijun Lv, Yicheng Zou, Wanxiang Che, Hang Yan, Kai Chen, Dahua Lin

- LLMの進展により、情報抽出や質問応答、複雑な計画が向上
- 既存の手法では長文コンテキスト能力向上のため合成データを利用
- 我々の新たなフレームワークMIMGは、品質を85%以上に向上
- 実験により、合成データが人間注釈データを超える性能を示す

長文の指示データをより効果的に使う方法が分かるなんてワクワクするよね！これでAIがもっと賢くなったら、どんな新しい可能性が広がるのかな。

**Comment:** Work in progress

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-09-03 13:30

- - -

### [Federated Prediction-Powered Inference from Decentralized Data](http://arxiv.org/abs/2409.01730)

**連合予測駆動推論による分散データからの推定**

Ping Luo, Xiaoge Deng, Ziqing Wen, Tao Sun, Dongsheng Li

- 機械学習の発展により、補助データを活用した統計推論が可能となった
- 予測駆動推論（PPI）は信頼性の低いデータでも統計的な妥当性を確保
- プライベートデータを共有せずに有効な結論を導くためにFed-PPIフレームワークを提案
- Fed-PPIは連合学習を用い、ローカルモデルを集約して信頼区間を算出する

初耳だけど、分散データから信頼できる推論が可能になるなんてすごいよね！これ、データ共有が難しい現場でも役立ちそうで未来が楽しみ♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-03 09:14

- - -

### [ACCESS-FL: Agile Communication and Computation for Efficient Secure Aggregation in Stable Federated Learning Networks](http://arxiv.org/abs/2409.01722)

**ACCESS-FL: 安定した連合学習ネットワークにおける効率的な安全な集約のための機敏な通信と計算**

Niousha Nazemi, Omid Tavallaie, Shuaijun Chen, Anna Maria Mandalario, Kanchana Thilakarathna, Ralph Holz, Hamed Haddadi, Albert Y. Zomaya

- 連合学習（FL）はプライバシーに配慮した分散学習フレームワークである
- 従来のFLは、モデル更新の送信に伴うセキュリティリスクが存在する
- ACCESS-FLは、クライアントのドロップアウトが少ないシナリオにおいて通信と計算コストを一定に抑える
- ACCESS-FLはMNIST、FMNIST、CIFARデータセットを用いて評価され、SecAggやSecAgg+と比較して大幅なコスト削減を実現

これめっちゃ興味深いね！FLネットワークが安定することで、もっと効率的なプライバシー保護が可能になるかもって感じだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-09-03 09:03

- - -

### [Buffer-based Gradient Projection for Continual Federated Learning](http://arxiv.org/abs/2409.01585)

**継続的連合学習のためのバッファベースの勾配射影**

Shenghong Dai, Jy-yong Sohn, Yicong Chen, S M Iftekharul Alam, Ravikumar Balakrishnan, Suman Banerjee, Nageen Himayat, Kangwook Lee

- 継続的連合学習（CFL）は、分散するクライアントが連続データから学習するために重要である
- 大きな課題は、学習中に以前の知識を失う「破滅的忘却」の軽減である
- Fed-A-GEMが、ローカルバッファサンプルと集約バッファー勾配を活用して破滅的忘却を緩和する
- CIFAR-100データセットを用いた実験では、従来の手法と比較して最大27%の精度向上が示された

破滅的忘却を克服するアイデアがスゴイ！ローカルと集計のデータを巧みに使うなんて、めちゃくちゃ画期的だよね。

**Comment:** A preliminary version of this work was presented at the Federated   Learning Systems (FLSys) Workshop @ Sixth Conference on Machine Learning and   Systems, June 2023

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-09-03 03:50

- - -

### [EvoChart: A Benchmark and a Self-Training Approach Towards Real-World Chart Understanding](http://arxiv.org/abs/2409.01577)

**EvoChart: 実世界のチャート理解に向けたベンチマークと自己学習アプローチ**

Muye Huang, Lai Han, Xinyu Zhang, Wenjun Wu, Jie Ma, Lingling Zhang, Jun Liu

- チャート理解は自動データ分析を可能にし、高い視覚理解能力が必要
- 高品質トレーニングデータと包括的ベンチマークの不足が課題
- EvoChartは合成チャートデータ生成の自己学習法を提案
- EvoChart-QAは実世界のチャート理解能力を評価するためのベンチマーク

実世界のデータ分析を進めるための進化した手法にワクワクするね。EvoChartの提案で視覚言語モデルの能力がどれほど向上するか見ものだなー。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-03 03:23

- - -

### [Efficient and Scalable Estimation of Tool Representations in Vector Space](http://arxiv.org/abs/2409.02141)

**ベクトル空間におけるツール表現の効率的かつスケーラブルな推定**

Suhong Moon, Siddharth Jha, Lutfi Eren Erdogan, Sehoon Kim, Woosang Lim, Kurt Keutzer, Amir Gholami

- 大規模言語モデル（LLM）は外部情報源との連携と複雑なタスクの実行が可能
- LLMの限られたコンテキストウィンドウの問題を解決するため、新しいデータ駆動型のツールリトリーバル戦略を提案
- ToolBankとしてリアルな人間の使用状況を反映する新しいツールリトリーバルデータセットを作成
- 提案手法でRecall@KがToolBenchデータセットで最大27.28、ToolBankで最大30.5向上

ツールリトリーバルの新しい技術とか面白そう！これからのツール管理の手間が削減されるんじゃないかなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-09-02 19:39

- - -

### [Achieving Byzantine-Resilient Federated Learning via Layer-Adaptive Sparsified Model Aggregation](http://arxiv.org/abs/2409.01435)

**ビザンチン耐性のある連合学習をレイヤー適応型スパース化モデル集約によって実現**

Jiahao Xu, Zikai Zhang, Rui Hu

- 連合学習(FL)はデータを共有せずに複数のクライアントがモデルを共同で訓練する技術
- FLは悪意あるビザンチン攻撃に弱く、既存の対策はモデル更新の多様性を無視し限界がある
- LASAアプローチは事前スパース化とレイヤー適応集約を組み合わせてロバスト性を向上
- 実験結果はLASAの効果を示しており、IIDと非IIDデータセットで有効性が確認された

この方法なら、ビザンチン問題に対してもっと頑丈になりそう！データ共有なしでモデル訓練って、プライバシーも守れるし安心感があるよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-09-02 19:28

- - -

### [Assessing the Impact of Image Dataset Features on Privacy-Preserving Machine Learning](http://arxiv.org/abs/2409.01329)

**画像データセットの特徴がプライバシー保護機械学習に与える影響の評価**

Lucas Lange, Maurice-Maximilian Heykeroth, Erhard Rahm

- データセットの不均衡は少数派クラスの脆弱性を高めるが、差分プライバシーがこの問題を緩和
- クラス数が少ないデータセットはモデルの有用性とプライバシーを両立させるのに有利
- 高エントロピーまたは低Fisher Discriminant比率のデータセットは有用性-プライバシーのトレードオフを悪化させる
- この研究はデータとプライバシーの最適化に関する貴重なガイダンスを提供

プライバシー学習の課題がこんなに複雑だなんてびっくりした！画像データの選び方一つでこんなに違うんだね。未来の研究が楽しみ！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.CV, **投稿日時:** 2024-09-02 15:30

- - -

### [LoGex: Improved tail detection of extremely rare histopathology classes via guided diffusion](http://arxiv.org/abs/2409.01317)

**LoGex: 指導拡散による極めて稀な病理学クラスの尾部検出の改善**

Maximilian Mueller, Matthias Hein

- 医療データはほとんどのサンプルが少数のクラスに集中し、稀なクラスが長い尾を形成する
- 限られたデータのため、稀なクラスは検出が重要で分類が難しい
- LoRAと拡散ガイダンスを用いて、検出用のターゲット合成データを生成
- 尾部クラスの10サンプルのみでOOD検出性能を大幅に向上させ、主要クラスの分類精度は低下させない

稀な病理学クラスの検出を合成データを使って向上させるって、具体的にどうやってるんだろう？これを使えば、異常な病気とかもっと早く見つけられるようになるかもね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-09-02 15:18

- - -

### [Generating Packet-Level Header Traces Using GNN-powered GAN](http://arxiv.org/abs/2409.01265)

**GNNを活用したGANによるパケットレベルヘッダートレース生成**

Zhen Xu

- GNNとGANを組み合わせた新しい方法を提案
- word2vecエンコーディングを用いて、次元の呪いを軽減
- 実験結果では、word2vecが従来のone-hotエンコーディングより効果的
- GNNの導入で、ディスクリミネータがよりリアルなデータを生成可能に

ネットワークデータ生成がすごく進化しそう！word2vecとかGNNの活用で、もっと自然で正確なデータが簡単に作れちゃうんだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.NI, **投稿日時:** 2024-09-02 13:59

- - -

### [GAS: Generative Activation-Aided Asynchronous Split Federated Learning](http://arxiv.org/abs/2409.01251)

**GAS：生成活性化支援非同期分割連合学習**

Jiarong Yang, Yuan Liu

- 分割連合学習（SFL）は、クライアントとサーバー間でモデルを協力してトレーニングする手法
- 非同期伝送による遅延がSFLのパフォーマンスを大幅に劣化させる
- サーバーに活性化バッファとモデルバッファを埋め込み、非同期に対処する方法を提案
- バイアスを減らすために、生成活性化支援を導入し、サーバーモデルの更新精度を向上

非同期伝送の問題をうまく解決するなんてすごいね！未来の分散学習の効率がもっと良くなりそうな感じがしてわくわくしちゃうよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-09-02 13:37

- - -

### [Fed-MUnet: Multi-modal Federated Unet for Brain Tumor Segmentation](http://arxiv.org/abs/2409.01020)

**Fed-MUnet: 脳腫瘍セグメンテーションのためのマルチモーダル連合U-net**

Ruojun Zhou, Lisha Qu, Lei Zhang, Ziming Li, Hongwei Yu, Bing Luo

- 脳腫瘍セグメンテーションで連合学習（FL）を用いることで、データ共有のプライバシー問題を軽減
- 現在のFL手法は単一モーダルのMRIに焦点を当てており、マルチモーダルMRIの研究は少ない
- 提案手法Fed-MUnetは、複雑な構造や大規模なパラメータ、過学習の問題を解決
- BraTS2022データセットで評価し、SOTA手法より高いパフォーマンスを達成しつつプライバシーを保護

提案しているFed-MUnetが、データのプライバシーを守りながらも性能を高める新しい視点を提供していて、すごく興味深い！コードも公開されているから、これからの研究に大いに役立ちそうだね。

**Comment:** 6 pages, 3 figures, 2 tables. It was accepted by 2024 IEEE   International Conference on E-health Networking, Application & Services   (HealthCom)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, eess.IV, **投稿日時:** 2024-09-02 07:55

- - -

### [Federated Deep Reinforcement Learning-Based Intelligent Channel Access in Dense Wi-Fi Deployments](http://arxiv.org/abs/2409.01004)

**高密度Wi-Fi導入におけるフェデレーテッドディープ強化学習ベースのインテリジェントチャネルアクセス**

Xinyang Du, Xuming Fang, Rong He, Li Yan, Liuming Lu, Chaoming Luo

- IEEE 802.11 MAC層はCSMA/CAメカニズムを利用し、チャネル競合とアクセスを管理
- 高密度Wi-Fi環境では激しい競争がパケット衝突を引き起こす可能性がある
- 本研究はFLとDDPGアルゴリズムを組み合わせたインテリジェントなチャネル競合アクセスメカニズムを提案
- シミュレーション結果により、提案手法が静的および動的なシナリオで従来のアルゴリズムに対して優れた性能を示した

高密度なWi-Fi環境での通信効率を大幅に改善する手法を考えるなんて未来感あるよね！これでもっと快適なネット環境が期待できるかも！

**Comment:** submitted to a conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, **投稿日時:** 2024-09-02 07:28

- - -

### [Uplink Over-the-Air Aggregation for Multi-Model Wireless Federated Learning](http://arxiv.org/abs/2409.00978)

**マルチモデル無線連合学習のためのアップリンク空中集約**

Chong Zhang, Min Dong, Ben Liang, Ali Afana, Yahia Ahmed

- 無線連合学習（FL）で複数モデルを同時に訓練するアップリンク空中集約（OAA）法を提案

- マルチモデル訓練の収束率を最大化するため、グローバルモデル更新の最適性ギャップの上限を導出

- 上限を最小化するためにアップリンク送信受信ビームフォーミング最適化問題を定式化し、ブロック座標下降法で解決

- シミュレーション結果では、従来の単一モデルアプローチよりも、提案する高速OAAを用いたマルチモデルFLが大幅に優れている

複数モデルを同時に訓練して収束率アップとか、すごく効率よさそうだね！シミュレーション結果もかなり良好みたいだし、実用化が楽しみ💡

**Comment:** 5 pages, 5 figures. Accepted by IEEE SPAWC 2024. arXiv admin note:   text overlap with arXiv:2312.13424

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, eess.SP, math.IT, **投稿日時:** 2024-09-02 06:49

- - -

### [Enhancing Privacy in Federated Learning: Secure Aggregation for Real-World Healthcare Applications](http://arxiv.org/abs/2409.00974)

**連合学習におけるプライバシーの強化：実世界のヘルスケアアプリケーションのためのセキュアな集約**

Riccardo Taiello, Sergen Cansiz, Marc Vesin, Francesco Cremonesi, Lucia Innocenti, Melek Önen, Marco Lorenzi

- 実世界の連合学習、特にヘルスケアでは通信とセキュリティの課題が存在
- Joye-Libert（JL）とLow Overhead Masking（LOM）という2つのセキュア集約プロトコルを実装し比較
- 4つのデータセットで理論的および実験的評価を行い、タスクの正確性を維持したままプライバシーを保護
- 大規模モデルの訓練時の計算オーバーヘッドはCPUで1％未満、GPUでは50％未満、保護フェーズは10秒未満

セキュア集約が現実世界でどこまで使えるかの実証ってすごく興味深いね。連合学習が医療でもっと安全に使える未来が見えてきた気がするな。

**Comment:** Accepted at the 5-th MICCAI Workshop on Distributed, Collaborative   and Federated Learning in Conjunction with MICCAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-09-02 06:43

- - -

### [ToolACE: Winning the Points of LLM Function Calling](http://arxiv.org/abs/2409.00920)

**ToolACE: LLM関数呼び出しのポイントを制するツール**

Weiwen Liu, Xu Huang, Xingshan Zeng, Xinlong Hao, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Zhengying Liu, Yuanqing Yu, Zezhong Wang, Yuxian Wang, Wu Ning, Yutai Hou, Bin Wang, Chuhan Wu, Xinzhi Wang, Yong Liu, Yasheng Wang, Duyu Tang, Dandan Tu, Lifeng Shang, Xin Jiang, Ruiming Tang, Defu Lian, Qun Liu, Enhong Chen

- 大規模言語モデルの関数呼び出しは応用範囲を広げるが、実データの収集と注釈が難しい
- ToolACEは正確かつ多様なツール学習データを生成する自動パイプラインを提供
- 自己進化合成プロセスを利用し、26,507の多様なAPIプールを作成
- 生成データの正確性を確保するため、ルールベースとモデルベースの二層検証システムを実装

すごいね！自動的にデータ生成して、実際のモデルと同じくらいの性能を出せるなんて驚きだね。どんな未来が広がるのか楽しみ～！

**Comment:** 21 pages, 22 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-09-02 03:19

- - -

### [Digital Homunculi: Reimagining Democracy Research with Generative Agents](http://arxiv.org/abs/2409.00826)

**デジタルホムンクルス: 生成エージェントによる民主主義研究の再構築**

Petr Specian

- 技術の進展が民主的制度の進化を超え、民主主義改革に新たなアプローチが求められている
- 実験ボトルネックにより民主主義研究の進展が遅延し、費用と倫理リスクが障害である
- 本研究は生成人工知能を利用し、社会的文脈で人間行動を模倣するデジタルホムンクルスを提案
- 生成AIを使った大規模社会シミュレーションにより、複雑な制度メカニズムのテストが可能になる

この研究って、AIで民主主義ももっと進化させるってことだよね！デジタルホムンクルスとかどんな風に動くのか、想像するだけで楽しみだな〜。

**Comment:** 36 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CY, **投稿日時:** 2024-09-01 19:57

- - -

### [Enabling Trustworthy Federated Learning in Industrial IoT: Bridging the Gap Between Interpretability and Robustness](http://arxiv.org/abs/2409.02127)

**産業用IoTにおける信頼性の高い連合学習の実現：解釈可能性とロバスト性のギャップを埋める**

Senthil Kumar Jagatheesaperumal, Mohamed Rahouti, Ali Alfatemi, Nasir Ghani, Vu Khanh Quy, Abdellah Chehri

- 連合学習はデータをローカルに保持しながら協調的なモデル訓練を可能にする
- 産業用IoTでデータのプライバシー保護やセキュリティ、効率的なリソース利用が重要
- 解釈可能性とロバスト性の確保が連合学習の普及における主要な課題
- 信頼性を高めるための設計戦略と実地ケーススタディを示している

産業用IoTでプライバシーを守りながら高精度な学習を実現するなんて、未来が楽しみだね！ロバスト性と解釈可能性の両立ができたら、もっと安心して使えそう。

**Comment:** 7 pages, 2 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, 68Txx, I.2.6, **投稿日時:** 2024-09-01 15:13

- - -

### [A Novel Taxonomy for Navigating and Classifying Synthetic Data in Healthcare Applications](http://arxiv.org/abs/2409.00701)

**ヘルスケアアプリケーションにおける合成データの分類法の新提案**

Bram van Dijk, Saif ul Islam, Jim Achterberg, Hafiz Muhammad Waseem, Parisis Gallos, Gregory Epiphaniou, Carsten Maple, Marcel Haas, Marco Spruit

- データ駆動型技術はヘルスケアの効率性や信頼性を向上させたが、プライバシーの課題がある
- 合成データが注目されているが、研究が多岐にわたり潜在能力を把握しづらい
- 新たな分類法を提案し、データ比率、データの形式、データ変換の3種類に分類
- 研究者がデータセット、データ形式、変換の種類を把握し、課題と重複点を理解しやすくする

ヘルスケア分野で合成データの分類が大事なんて面白い！これからの研究がどんな風に進むか楽しみだね。

**Comment:** Accepted at the 23rd EFMI Special Topic Conference, Romania, November   2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CY, **投稿日時:** 2024-09-01 12:04

- - -

### [DAMe: Personalized Federated Social Event Detection with Dual Aggregation Mechanism](http://arxiv.org/abs/2409.00614)

**DAMe：二重集約メカニズムを用いた個別化連合型ソーシャルイベント検出**

Xiaoyan Yu, Yifan Wei, Pu Li, Shuaishuai Zhou, Hao Peng, Li Sun, Liehuang Zhu, Philip S. Yu

- 連合学習を通じたソーシャルイベント検出モデルの訓練を目指すが、既存のパラダイムは不十分
- 本研究では二重集約メカニズムを用いた個別化連合学習フレームワークDAMeを提案
- ベイズ最適化による新しいローカル集約戦略とグローバル集約戦略を導入し、過学習を防止
- 六つの言語と二つのソーシャルメディアプラットフォームを用いた実験で有効性を実証

新しいアプローチでソーシャルイベント検出の精度が上がりそうで楽しみ！攻撃にも耐性があるのはめっちゃ安心だね。

**Comment:** CIKM 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-09-01 04:56

- - -

### [Post-OCR Text Correction for Bulgarian Historical Documents](http://arxiv.org/abs/2409.00527)

**ブルガリアの歴史的文書のためのOCR後のテキスト修正**

Angel Beshirov, Milena Dobreva, Dimitar Dimitrov, Momchil Hardalov, Ivan Koychev, Preslav Nakov

- 歴史的文書のデジタル化は文化遺産保護に重要であり、OCR技術が不可欠
- 歴史的文書の正確なOCR処理は難題であり、追加のテキスト修正工程が必要
- 19世紀のDrinov正書法に基づいたブルガリアのベンチマークデータセットを作成
- 最新のLLMとエンコーダ・デコーダフレームワークを活用し、テキスト修正の誤りを25%削減

ブルガリアの歴史って興味深いね！昔の書き方をデジタル化するなんて、未来の探検家になった気分だね。

**Comment:** Accepted for publication in the International Journal on Digital   Libraries

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.DL, cs.LG, **投稿日時:** 2024-08-31 19:27

- - -

### [Chatting Up Attachment: Using LLMs to Predict Adult Bonds](http://arxiv.org/abs/2409.00347)

**会話型AIによる愛着スタイル予測: LLMを使った成人の絆予測**

Paulo Soares, Sean McCurdy, Andrew J. Gerber, Peter Fonagy

- 医療分野のデータ取得は困難で、AI技術の採用が遅れ高リスク
- GPT-4とClaude 3 Opusを用いて個々のプロフィール、子供時代の記憶、愛着スタイルを持つエージェントを作成
- シミュレートされた成人愛着インタビューでの回答を使用して、愛着スタイルを予測するモデルを訓練
- 合成データのみで訓練したモデルが人間データで訓練したモデルと同等の性能を達成

AIで心理学的な要素まで予測できるなんてすごいね。合成データでこんなに高精度になるとはびっくり！これからの医療とかカウンセリングに活かせそうでワクワクするよ～。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CL, **投稿日時:** 2024-08-31 04:29

- - -

### [Demo: FedCampus: A Real-world Privacy-preserving Mobile Application for Smart Campus via Federated Learning & Analytics](http://arxiv.org/abs/2409.00327)

**デモ: FedCampus：連合学習とアナリティクスによるスマートキャンパスのプライバシー保護モバイルアプリケーション**

Jiaxiang Geng, Beilong Tang, Boyan Zhang, Jiaqi Shao, Bing Luo

- FedCampusは連合学習（FL）と連合アナリティクス（FA）を利用し、クロスプラットフォームでのオンデバイス学習を実現している
- 差分プライバシーを用いてスマートウォッチからプライバシー保護されたデータを収集
- Duke Kunshan Universityで100台のスマートウォッチをボランティアに配布し、睡眠追跡やフィジカルアクティビティの監視などのタスクを成功させた
- プロジェクトはオープンソースで公開されており、詳細なデモビデオも提供されている

実際にキャンパスで使いながらモデルを鍛えるって、未来の学校っぽくてワクワクするよね！プライバシーも守りながら、健康トラッキングとか個別アドバイスもできるって最高じゃない？

**Comment:** 2 pages, 3 figures, accepted for publication in ACM Mobihoc 2024

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.DC, **投稿日時:** 2024-08-31 01:58

- - -

### [Differentially Private Synthetic High-dimensional Tabular Stream](http://arxiv.org/abs/2409.00322)

**差分プライバシーに基づく高次元タブ送信データの合成**

Girish Kumar, Thomas Strohmer, Roman Vershynin

- 差分プライバシーを満たす複数の合成データセットを生成するアルゴリズムを提案
- 入力データが変更されても継続的に差分プライバシーを満たす
- 高次元のタブularデータに適用可能
- 実世界のデータセットを用いた実験で有用性を示した

常に新しいデータに対応できる差分プライバシーの合成データが作れるとか、すごく便利そう。データが変わっても安心だね！試してみたくなるよ。



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.IT, cs.LG, math.IT, math.ST, stat.TH, **投稿日時:** 2024-08-31 01:31

- - -

### [A Survey for Large Language Models in Biomedicine](http://arxiv.org/abs/2409.00133)

**バイオメディシンにおける大規模言語モデルの調査**

Chong Wang, Mengyao Li, Junjun He, Zhongruo Wang, Erfan Darzi, Zan Chen, Jin Ye, Tianbin Li, Yanzhou Su, Jing Ke, Kaili Qu, Shuxin Li, Yi Yu, Pietro Liò, Tianyun Wang, Yu Guang Wang, Yiqing Shen

- 484件の論文を分析し、バイオメディカル分野でのLLMの最新動向、応用、課題、将来性を詳細に調査
- ゼロショット学習による診断補助、薬物発見、個別化医療など幅広いバイオメディカルタスクにおけるLLMの能力を探る
- バイオメディカル領域での特定タスク向け多モーダルLLMの微調整方法や適応戦略を議論
- LLMが直面するデータプライバシー懸念、モデルの解釈性制限、データセットの質の問題、倫理的課題を挙げ、今後の対応策として連合学習と説明可能AIの統合を提案

バイオメディカルの分野でのLLMの実用性に焦点を当てているのが面白い。ゼロショット学習って未来の医療にもすごく役立ちそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-08-29 12:39
