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

更新: 2024-09-04T04:20:31.577605

- - -

### [How Knowledge Distillation Mitigates the Synthetic Gap in Fair Face Recognition](http://arxiv.org/abs/2408.17399)

**知識蒸留が公平な顔認識における合成データのギャップをどのように緩和するか**

Pedro C. Neto, Ivona Colakovic, Sašo Karakatič, Ana F. Sequeira

- 知識蒸留（KD）を活用し、顔認識データセットの最近の撤回に対抗する戦略を立案
- 事前訓練された教師モデルを用い、合成データセットや実データと合成データの混合を利用することで驚くべき結果を達成
- KDを用いることで、すべての民族で性能が向上しバイアスが減少することが一貫して確認
- 合成データと実データの間の性能差を緩和し、顔認識モデルの精度と公平性を向上させる

知識蒸留ってすごいね！合成データでも公平な顔認識ができるようになるなんて、未来が楽しみだなぁ。

**Comment:** Accepted at ECCV 2024 Workshops

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-30 16:35

- - -

### [C-RADAR: A Centralized Deep Learning System for Intrusion Detection in Software Defined Networks](http://arxiv.org/abs/2408.17356)

** C-RADAR：ソフトウェア定義ネットワークにおける侵入検知のための集中型ディープラーニングシステム **

Osama Mustafa, Khizer Ali, Talha Naqash

- SDNはネットワーク管理を簡素化し柔軟性を向上させるが、中央制御平面はネットワーク攻撃に脆弱である
- 従来のネットワークでの侵入検知にはディープラーニング（DL）技術が有効だが、SDNへの適用は未解決の研究領域である
- 本研究では、SDNの侵入検知のためにLSTM-Attnと呼ばれるDLアーキテクチャを使用し、Fl-scoreが0.9721に達することを示した
- DLアプローチは検出精度と計算効率で既存の手法を上回り、新しい攻撃パターンの検出にも有効である

SDNとディープラーニングの組み合わせ、面白そう！いつかこれでネットワークがもっと安全になったら嬉しいな。DLの技術がこんな風に応用される未来、ワクワクするね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-08-30 15:39

- - -

### [Privacy-Preserving Set-Based Estimation Using Differential Privacy and Zonotopes](http://arxiv.org/abs/2408.17263)

**差分プライバシーとゾノトープを用いたプライバシー保護された集合ベース推定**

Mohammed M. Dawoud, Changxin Liu, Karl H. Johansson, Amr Alanwar

- サイバーフィジカルシステム内の空間的に分散されたセンサーが協力して状態推定を行う必要がある
- 提案された集合ベースの推定プロトコルは、差分プライバシーを保証しつつ、推定した集合に真の状態を保持する
- センターとローカル差分プライバシーモデルを採用し、計算効率の高いゾノトープを用いてセンシティブな測定値を守る
- 数値最適化された切断ラプラスノイズを使用して、プライバシーと推定の有用性を向上させた

サイバーとプライバシーの両立を目指してるのが未来的でステキ！現実の応用にも役立ちそうだね。

**Comment:** This article is the journal submission of "Differentially Private   Set-Based Estimation Using Zonotopes", presented at the 2023 European Control   Conference (ECC), https://ieeexplore.ieee.org/document/10178269. arXiv admin   note: text overlap with arXiv:2305.07407

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-30 13:05

- - -

### [Democratizing AI in Africa: FL for Low-Resource Edge Devices](http://arxiv.org/abs/2408.17216)

**アフリカにおけるAIの民主化：低リソースのエッジデバイス向け連合学習**

Jorge Fabila, Víctor M. Campello, Carlos Martín-Isla, Johnes Obungoloch, Kinyera Leo, Amodoi Ronald, Karim Lekadir

- アフリカの医療システムはインフラ不足や高度医療技術へのアクセス難で課題が多い
- 周産期ヘルスケアに焦点を当て、アルジェリア、ガーナ、エジプト、マラウイ、ウガンダとスペインのデータを用いて胎児面分類器を訓練
- Raspberry Piや複数のノートパソコンなどの異種デバイスでモデル訓練を実施し、中央集権型と連合モデルの性能を比較
- ローカルでの訓練よりもモデルの汎用性が大幅に向上し、少ない要件で大規模な展開が可能

周産期ヘルスケアに連合学習を使えば、アフリカでも高度な医療が提供できるね！特にインフラ不足って聞くけど、低リソースでも効果があるなら別に心配いらないよって思っちゃった。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-30 11:46

- - -

### [Secure Ownership Management and Transfer of Consumer Internet of Things Devices with Self-sovereign Identity](http://arxiv.org/abs/2408.17184)

**消費者向けIoTデバイスのセキュアな所有権管理と移転における自己主権型アイデンティティの活用**

Nazmus Sakib, Md Yeasin Ali, Nuran Mubashshira Momo, Marzia Islam Mumu, Masum Al Nahid, Fairuz Rahaman Chowdhury, Md Sadek Ferdous

- IoTデバイスの普及に伴い、消費者向けデバイスのアイデンティティ管理や所有権移転に課題がある
- ブロックチェーン技術を用いた解決策が試みられるも、成功は限定的であった
- 提案するシステムはSSIを基盤にし、ブロックチェーンや分散型識別子（DID）、認証情報（VC）を活用
- 提案システムの脅威モデルと要件分析に基づくアーキテクチャや実証実験、セキュリティ評価を実施

ブロックチェーンと分散技術を使ってIoTデバイスの管理がもっと簡単になりそう。これが普及すれば、私たちもデバイス管理で悩むことが減るかも！



**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.CR, cs.ET, **投稿日時:** 2024-08-30 10:35

- - -

### [Towards Hyper-parameter-free Federated Learning](http://arxiv.org/abs/2408.17145)

**超パラメータ不要の連合学習に向けて**

Geetika, Drishya Uniyal, Bapi Chatterjee

- 連合学習の自動同期技術は従来のFederated Averagingより優れた性能を示す
- 提案手法ではサーバー上のスケーリング因子を自動調整するアルゴリズムを導入
- クライアントで適切なステップサイズを確保することで線形収束を実現
- 実験結果は凸問題および非凸問題の両方で既存手法よりも良好な性能を示す

これからは、もっと簡単に連合学習ができるようになるのかな？パラメータの調整って面倒だから、自動でやってくれるなら嬉しいね！

**Comment:** 28 pages, 3 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, math.OC, **投稿日時:** 2024-08-30 09:35

- - -

### [Sparse Uncertainty-Informed Sampling from Federated Streaming Data](http://arxiv.org/abs/2408.17108)

**連合ストリーミングデータからの疎な不確実性情報に基づくサンプリング**

Manuel Röder, Frank-Michael Schleif

- 数値的に堅牢で計算効率の高い非I.I.D.データのストリーミングサンプリング手法を提案
- ローカルモデル適応のためのラベル付きデータが希少で高価な環境に対応
- メモリバッファ戦略に依存せず、瞬時にラベル付けの意思決定を行う
- 大規模データストリームに対し、トレーニングバッチの多様性と数値的な堅牢性を向上

ラベル付きデータが限られている中で即座に判断を下す方法ってすごい！FL環境のトレーニングをもっと効率的にできるなんて、未来が楽しみだね。

**Comment:** Preprint, 6 pages, 3 figures, Accepted for ESANN 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-08-30 08:49

- - -

### [FissionVAE: Federated Non-IID Image Generation with Latent Space and Decoder Decomposition](http://arxiv.org/abs/2408.17090)

**FissionVAE: 潜在空間およびデコーダ分解による連合非IID画像生成**

Chen Hu, Jingjing Deng, Xianghua Xie, Xiaoke Ma

- 連合学習の枠組みで、非IIDデータ環境における潜在空間の一貫性維持が困難
- FissionVAEを提案し、潜在空間を分解しデコーダをクライアントグループごとに構築
- 階層型VAEと異なるデコーダアーキテクチャを導入し、特有のデータ分布に対応
- MNISTとFashionMNIST、カートゥーンと人間の顔などの複合データセットで品質向上を実証

分散して学習する時にそれぞれのデータの特徴を活かせるなんてすごいなぁ。色んなデータからどんな画像が生成されるのかワクワクするよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2024-08-30 08:22

- - -

### [SIMD-Aware Homomorphic Compression and Application to Private Database Query](http://arxiv.org/abs/2408.17063)

**SIMD対応準同型圧縮とプライベートデータベースクエリへの応用**

Jung Hee Cheon, Keewoo Lee, Jai Hyun Park, Yongdong Yeo

- 準同型暗号を使用したプライベートデータベースクエリ(PDQ)の重要なステップは、暗号化された疎ベクトルの圧縮である
- 提案した新しい準同型圧縮方式はSIMD技術を活用し効率的な実装が可能である
- 提案方式は、理論上最適な圧縮率と良好な復号複雑度を両立している
- 実験結果として、提案方式は従来の最良結果よりも4.7倍から33.2倍高速である

新しい圧縮方式ってすごくない？データベースクエリがもっと速くて安全になるなんて未来が楽しみだね。実験結果も驚異的だし、この技術がどう発展してくのか気になる！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-30 07:49

- - -

### [Contrastive Learning with Synthetic Positives](http://arxiv.org/abs/2408.16965)

**合成ポジティブを用いたコントラスト学習**

Dewen Zeng, Yawen Wu, Xinrong Hu, Xiaowei Xu, Yiyu Shi

- 近傍アルゴリズムは「簡単」なポジティブペアのみを識別
- 拡散モデルによって生成された合成画像を追加ポジティブとして提案
- 異なる背景だが同じ意味内容を持つ「難しい」ポジティブを生成
- 複数ベンチマークで性能が向上し、転送学習ベンチマークでも優れた結果を達成

合成データを使った新しい自己教師あり学習の手法、面白そう！CLSPは今後のSSL研究に大きな影響を与えそうだよね。

**Comment:** 8 pages, conference

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-30 01:47

- - -

### [Analyzing Inference Privacy Risks Through Gradients in Machine Learning](http://arxiv.org/abs/2408.16913)

**機械学習における勾配を通じた推論プライバシーリスクの分析**

Zhuohang Li, Andrew Lowy, Jing Liu, Toshiaki Koike-Akino, Kieran Parsons, Bradley Malin, Ye Wang

- 分散学習において勾配シェアのプライバシーリスクを体系的に分析
- 属性、特性、分布、ユーザー開示などの攻撃に対する包括的なフレームワークを提案
- 勾配を通じたプライバシー侵害に対するデータ集約化の無効性を実験で証明
- 差分プライバシーなど5つの防御策の有効性を情報理論的視点で分析

いろんなデータを使って、守れるか試しているのが興味深いね。こういう研究が進むとみんなの情報がもっと安全になるかもね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, stat.ML, **投稿日時:** 2024-08-29 21:21

- - -

### [Maven: A Multimodal Foundation Model for Supernova Science](http://arxiv.org/abs/2408.16829)

**マーベン: 超新星科学のためのマルチモーダル基盤モデル**

Gemma Zhang, Thomas Helfer, Alexander T. Gagliano, Siddharth Mishra-Sharma, V. Ashley Villar

- 天文学では高品質の観測データが少なく、低品質や合成データが多いアンバランスな状況が一般的
- マーベンは、対照学習目標を用いて異なるデータモダリティを共有埋め込み空間に整列させる初の基盤モデル
- 合成データ50万個の超新星データで事前訓練し、Zwicky Transient Facilityから観測された超新星4,702個で微調整
- 最新の性能を達成し、特に合成データで事前訓練すると全体的な性能が向上することがアブレーション研究で確認された

この研究、なんだか面白そうだね！特に対照学習を使って高性能なモデルを作る部分、これからの観測データが増えるとさらに活躍しそうだね。

**Comment:** code: https://github.com/ThomasHelfer/multimodal-supernovae data:   https://huggingface.co/datasets/thelfer/multimodal_supernovae

**トピック:** [合成データ](sd), **カテゴリ:** astro-ph.HE, astro-ph.IM, cs.LG, **投稿日時:** 2024-08-29 18:00
