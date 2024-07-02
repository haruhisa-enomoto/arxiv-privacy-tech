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

更新: 2024-07-02T04:19:42.906052

- - -

### [Scaling Synthetic Data Creation with 1,000,000,000 Personas](http://arxiv.org/abs/2406.20094)

**10億人のペルソナを活用した合成データのスケーリング**

Xin Chan, Xiaoyang Wang, Dian Yu, Haitao Mi, Dong Yu

- 多様な視点を持つペルソナ駆動型のデータ合成手法を提案
- ウェブデータから自動収集した10億の多様なペルソナを持つPersona Hubを導入
- 合成データ作成を様々なシナリオで大規模に実現
- 数学的・論理的推論問題やユーザープロンプト、知識豊富なテキスト、ゲームNPCなどでの応用を示す

ペルソナを使ったデータ作成、めっちゃ面白そう！これからの研究がもっと深まる予感がするね。

**Comment:** Work in progress

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-06-28 17:59

- - -

### [Into the Unknown: Generating Geospatial Descriptions for New Environments](http://arxiv.org/abs/2406.19967)

**未知への躍進: 新環境における地理空間記述の生成**

Tzuf Paz-Argaman, John Palowitch, Sayali Kulkarni, Reut Tsarfaty, Jason Baldridge

- 未知の環境で訓練データがない場合、パフォーマンスが大幅に低下する
- オープンソースの説明と座標（例：Wikipedia）を使用するが、地理解像度が低い
- 準備された地理空間データを用いて、高品質な合成データを生成する大規模な増補方法を提案
- 提案手法は、新環境において100メートル精度を45.83%向上させることに成功した

新しい場所でも効果的にナビゲーションできるようになるなんてすごい！実際にどんな風に使われるのか楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-06-28 14:56

- - -

### [Secure Outsourced Decryption for HE-based Privacy-preserving Cloud Computing System](http://arxiv.org/abs/2406.19964)

**HEベースのプライバシー保護クラウドコンピューティングシステム向けの安全な外部委託復号**

Xirong Ma, Chuan Li, Yuchang Hu, Yunting Tao, Yali Jiang, Yanbin Li, Fanyu Kong, Chunpeng Ge

- 機械学習の進展により大規模データ処理の需要が急増
- 準同型暗号を活用し、クラウド上で安全に暗号化データを処理する方法を提案
- 従来の復号プロセスを二段階に分割し、計算負荷をクラウドへ外部委託
- 実験結果として、復号速度が67%向上し、クライアントの空間使用が50%削減

クラウドの力を借りて復号を速くしてくれるんだね！クラウドの利用がもっと安全になるって期待しちゃうね。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-28 14:51

- - -

### [Calibrating LLMs with Preference Optimization on Thought Trees for Generating Rationale in Science Question Scoring](http://arxiv.org/abs/2406.19949)

**思考ツリーにおける選好最適化を用いたLLMのキャリブレーションによる科学質問採点の理由生成**

Jiazheng Li, Hainiu Xu, Zhaoyue Sun, Yuxiang Zhou, David West, Cesare Aloisi, Yulan He

- 自動採点システム向けの理由生成は説明可能性の向上に有望
- 既存方法は分類器ベースの方法ほど精度が高くない
- 大規模言語モデル（LLM）で思考ツリーを生成し合成データを作成
- 提案したフレームワークはQWKスコアで38%の改善を達成

LLMを使った新しい方法で、自動採点がもっと正確で説明しやすくなりそうだね。これ、学校のテスト採点とかにも活かせるんじゃないかな？



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-28 14:33

- - -

### [From the Least to the Most: Building a Plug-and-Play Visual Reasoner via Data Synthesis](http://arxiv.org/abs/2406.19934)

**最小から最大へ: データ合成によるプラグアンドプレイビジュアル推論器の構築**

Chuanqi Cheng, Jian Guan, Wei Wu, Rui Yan

- 視覚と言語処理の複数ステップを含む推論データがほとんど存在しないため、課題が困難
- 質問をサブ質問に分解し、外部ツールで解決する「最小から最大へ」ビジュアル推論パラダイムを導入
- 複雑な合成タスクをいくつかの簡単なサブタスクに分割し、オープンソースモデルに依存して再現性と効率性を確保
- $50$kのビジュアル推論例を構築し、広範な既存VLMの推論能力を強化する視覚推論器を開発

データ合成のアプローチとか、ちょっと未来感あってワクワクするね。プラグアンドプレイでいろんなモデルに適応できちゃうのもヤバい！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-06-28 14:04

- - -

### [Decoupling General and Personalized Knowledge in Federated Learning via Additive and Low-Rank Decomposition](http://arxiv.org/abs/2406.19931)

**連合学習における一般的な知識と個別化された知識の分離：加法分解と低ランク分解を用いて**

Xinghao Wu, Xuefeng Liu, Jianwei Niu, Haolin Wang, Shaojie Tang, Guogang Zhu, Hao Su

- 既存の個別化連合学習（PFL）はパラメータの分割アプローチを採用し、一般知識とクライアント特有知識を分けるが効果的ではない
- FedDecompを提案し、モデルの各パラメータを共有パラメータと個別パラメータに分解して、知識の分離を実現
- クライアントに特有の知識を保持するためには、一般知識よりも低いモデル容量が必要なため、個別パラメータを低ランク行列にする
- 新しい交互トレーニング戦略を提案し、多くのデータセットと異なるデータ異質性の中で最大4.9%の性能向上を実証

FedDecompっておもしろそう！パラメータを分解して効率化しながら、結果をちゃんと出すなんてすごいよね。新しいアプローチでどんどん進化しそうだから、もっと知りたくなる～。

**Comment:** 12 pages, 8 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-28 14:01

- - -

### [Comprehensive Generative Replay for Task-Incremental Segmentation with Concurrent Appearance and Semantic Forgetting](http://arxiv.org/abs/2406.19796)

**同時に発生する外観と意味の忘却を伴うタスクインクリメンタルセグメンテーションのための包括的生成リプレイ**

Wei Li, Jingyang Zhang, Pheng-Ann Heng, Lixu Gu

- 一般的なセグメンテーションモデルは、多様なタスクに対してプライバシーを保護しつつ、連続的なタスク到着に対応する
- タスク進化に伴う外観と意味の変化が複雑に絡み合い、同時に発生する忘却問題が存在
- Comprehensive Generative Replay (CGR) フレームワークを提案、過去のタスクデータを模倣する画像とマスクのペアを生成
- 実験結果から、心臓、眼底、前立腺のセグメンテーションにおいて、外観と意味の同時忘却の緩和に効果あり

タスクの進化に合わせた学習方法がとっても面白そう！プライバシーを守りながら性能も向上するって素敵～

**Comment:** Accepted by MICCAI24

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-06-28 10:05

- - -

### [Mobile Robot Oriented Large-Scale Indoor Dataset for Dynamic Scene Understanding](http://arxiv.org/abs/2406.19791)

**動的シーン理解のためのモバイルロボット向け大規模屋内データセット**

Yifan Tang, Cong Tai, Fangxing Chen, Wanting Zhang, Tao Zhang, Xueping Liu, Yongjin Liu, Long Zeng

- 現存の多くのロボットデータセットは静的シーンデータしか含まず、動的性能評価が困難
- THUDと呼ばれるモバイルロボット向け大規模屋内データセットを提案し、動的シーン理解アルゴリズムの訓練と評価に用いる
- THUDデータセットは実世界と合成データから構成され、13の大規模動的シナリオ、90Kの画像フレーム、20Mの2D/3Dバウンディングボックスなどを含む
- THUD上での3D物体検出、セマンティックセグメンテーション、ロボットリローカライゼーションなどの評価により、動的シーンでの課題が明らかになる

動的な環境でロボットのシーン理解能力がどう進化するか、すごく気になるよね！早くもっとすごいロボットが登場する未来が見たいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-06-28 09:54

- - -

### [Less is More: Accurate Speech Recognition & Translation without Web-Scale Data](http://arxiv.org/abs/2406.19674)

**少ない方が多い: ウェブ規模のデータなしで正確な音声認識と翻訳を実現**

Krishna C. Puvvada, Piotr Żelasko, He Huang, Oleksii Hrinchuk, Nithin Rao Koluguri, Kunal Dhawan, Somshubra Majumdar, Elena Rastorgueva, Zhehuai Chen, Vitaly Lavrukhin, Jagadeesh Balam, Boris Ginsburg

- 最新の音声認識と翻訳は膨大なインターネット音声データに依存している
- Canaryモデルは、英語、フランス語、スペイン語、ドイツ語で最新のモデルよりも精度が高い
- データ効率の高いモデルを実現するための3つの要素：(1) FastConformerベースの注意エンコーダ・デコーダアーキテクチャ、(2) 機械翻訳による合成データの使用、(3) データバランシング、動的データブレンディング、動的バケット化、ノイズ耐性ファインチューニングの高度な訓練技術
- モデル、重み、訓練コードはオープンソース化される

データが少なくても高精度なモデルを実現できるのすごいね！これからの音声認識技術が楽しみだな。

**Comment:** Accepted at Interspeech-2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, cs.SD, eess.AS, **投稿日時:** 2024-06-28 06:22

- - -

### [Personalized Interpretation on Federated Learning: A Virtual Concepts approach](http://arxiv.org/abs/2406.19631)

**連合学習におけるパーソナライズされた解釈：仮想概念アプローチ**

Peng Yan, Guodong Long, Jing Jiang, Michael Blumenstein

- 非IIDデータに対する解釈が連合学習のオープンな課題
- 既存の連合学習手法は、解釈なしでモデル性能向上を目指す
- クライアントデータを説明可能な仮想概念ベクトルとして解釈
- 提案手法の有効性をベンチマークデータセットで確認

各クライアントのデータをどうやって説明するかってすごく面白そう！新しい手法がどれだけ効果的かも気になるね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-28 03:39

- - -

### [SK-VQA: Synthetic Knowledge Generation at Scale for Training Context-Augmented Multimodal LLMs](http://arxiv.org/abs/2406.19593)

**SK-VQA：コンテキスト強化型マルチモーダルLLMトレーニングのための大規模合成知識生成**

Xin Su, Man Luo, Kris W Pan, Tien Pei Chou, Vasudev Lal, Phillip Howard

- 合成データ生成は大規模視覚と言語モデルの訓練で注目されている
- しかし、コンテキスト強化型生成システムへの合成データの応用は未開拓
- SK-VQAは外部知識を必要とする200万以上の質問-回答ペアを含む大規模な合成マルチモーダルデータセット
- 実験で、SK-VQAが既存の生成マルチモーダルモデルの適応に有効であることを証明

このSK-VQA、めっちゃ興味深いね！外部知識が必要な質問って、もっと賢いAIが作れそうな予感✨



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.CV, **投稿日時:** 2024-06-28 01:14

- - -

### [Private Zeroth-Order Nonsmooth Nonconvex Optimization](http://arxiv.org/abs/2406.19579)

**プライベートなゼロ次非滑らか非凸最適化**

Qinzi Zhang, Hoang Tran, Ashok Cutkosky

- 非凸かつ非滑らかな目的に対するプライベートなゼロ次アルゴリズムを提案
- データセットのサイズ$M$に対し、$(\alpha,\alpha\rho^2/2)$-R\'enyi差分プライバシーを保証
- $(\delta,\epsilon)$-停止点を見つけるためには$M=\tilde\Omega\left(\frac{d}{\delta\epsilon^3} + \frac{d^{3/2}}{\rho\delta\epsilon^2}\right)$が必要
- 目的関数が非滑らかでも、$\rho \ge \sqrt{d}\epsilon$の条件下ではプライバシーが「無料」

非滑らかな問題でもプライバシーが保たれるってすごい！うちらの卒研でも応用できるかもね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** math.OC, cs.CR, cs.LG, **投稿日時:** 2024-06-27 23:57

- - -

### [Too Good to be True? Turn Any Model Differentially Private With DP-Weights](http://arxiv.org/abs/2406.19507)

**すごすぎる？どんなモデルでも差分プライベートにできるDP-Weights**

David Zagardo

- 従来のDP-SGDは、トレーニング後にノイズレベルが高すぎたり低すぎたりして再トレーニングが必要になる課題がある
- 提案する新しいアプローチは、トレーニング後にノイズをモデルの重みに適用して差分プライバシーを達成するものである
- 数学的証明と形式的な手法でプライバシー保証の検証を行い、メンバーシップ推論攻撃と性能評価を用いて効果を実証
- 従来のDP-SGDモデルと比べても統計的に同等の性能とプライバシー保証を提供し、時間の節約と柔軟な微調整を可能にする

トレーニング後にノイズを付加するだけでプライバシー確保って素敵じゃない？これで研究や開発の手間が大幅に減るかもね。楽しみだな〜。

**Comment:** For code visit the following repository,   https://github.com/dzagardo/forgetnet/

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-06-27 19:58

- - -

### [High-resolution segmentations of the hypothalamus and its subregions for training of segmentation models](http://arxiv.org/abs/2406.19492)

**高解像度視床下部およびその亜領域のセグメンテーションモデル訓練用のセグメンテーション**

Livia Rodrigues, Martina Bocchetta, Oula Puonti, Douglas Greve, Ana Carolina Londe, Marcondes França, Simone Appenzeller, Leticia Rittner, Juan Eugenio Iglesias

- 脳構造のセグメンテーションはMRI解析の基礎であり、体積測定や形状解析に不可欠
- 自動セグメンテーションは大規模コホートの研究を促進、手動セグメンテーションよりも効率的
- 合成画像を用いた新技術が手動アノテーションの必要性を削減
- HELMと呼ばれるラベルマップデータセットを提供、合成データを用いたセグメンテーション法の開発が可能

視床下部のセグメンテーションに特化した方法がどれくらい効果的か気になるね。合成データの使い方もすごく面白そう！



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-06-27 19:16

- - -

### [Data Poisoning Attacks to Locally Differentially Private Frequent Itemset Mining Protocols](http://arxiv.org/abs/2406.19466)

**ローカル差分プライバシーを用いた頻出アイテム集合抽出プロトコルへのデータポイズニング攻撃**

Wei Tong, Haoyu Chen, Jiacheng Niu, Sheng Zhong

- ローカル差分プライバシー（LDP）は信頼できないデータ収集者がユーザーのプライバシーを侵害せずにデータを集約できる方法である。
- 最近の研究では、LDPプロトコルがデータポイズニング攻撃に対して脆弱であることが示されている。
- 本論文では、LDP頻出アイテム集合抽出プロトコルに対する新しい実践的なデータポイズニング攻撃を提案している。
- 提案された攻撃は、3つのデータセットを用いた実験で脅威の深刻さと攻撃の効果を実証している。

LDPの脆弱性を狙った攻撃って、本当に怖いよね。でも、これが改善されたらもっと安全なデータ解析ができそう！未来のセキュリティ技術に期待だね🌟

**Comment:** To appear in ACM Conference on Computer and Communications Security   (ACM CCS 2024)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-27 18:11

- - -

### [A Quantization-based Technique for Privacy Preserving Distributed Learning](http://arxiv.org/abs/2406.19418)

**プライバシー保護分散学習のための量子化技術**

Maurizio Colombo, Rasool Asal, Ernesto Damiani, Lamees Mahmoud AlQassem, Al Anoud Almemari, Yousof Alhammadi

- 機械学習モデルの大規模展開によりデータ保護に深刻な懸念がある
- 規制に準拠した新しいデータ保護技術を提案
- Hash-Combとランダム化に基づくプロトコルでトレーニングデータとモデルパラメータを保護
- 実験結果で堅牢性と精度保持プロパティを実証

これはめっちゃ面白そう！プライバシー守りながらも精度を保つなんて未来が楽しみだね。



**トピック:** [差分プライバシー](dp), [PETs](pets), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-06-26 14:54
