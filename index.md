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

更新: 2025-01-07T04:21:54.227863

- - -

### [Rate-My-LoRA: Efficient and Adaptive Federated Model Tuning for Cardiac MRI Segmentation](http://arxiv.org/abs/2501.03223)

**Rate-My-LoRA: 心臓MRIセグメンテーションのための効率的かつ適応的な連合モデル調整**

Xiaoxiao He, Haizhou Shi, Ligong Han, Chaowei Tan, Bo Liu, Zihao Xu, Meng Ye, Leon Axel, Kang Li, Dimitris Metaxas

- 心臓病の画像セグメンテーションは精度が重要だがデータの集約が難しい
- 連合学習によりデータを共有せずにモデルを訓練するが、通信量とデータ異質性が課題
- 低ランク適応（LoRA）を使い通信オーバーヘッドを減らしつつ性能を向上させる手法を提案
- 新しい集約技術でデータ異質性を克服し、精度と適応性が向上したと証明

新しい技術を使って心臓MRIのデータを共有せずに分析できるようになるなんてすごいね！この手法が広がれば、医療現場でのプライバシーの問題もどんどん解決していきそう。

**Comment:** Accepted in ISBI 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.DC, cs.LG, **投稿日時:** 2025-01-06 18:57

- - -

### [MObI: Multimodal Object Inpainting Using Diffusion Models](http://arxiv.org/abs/2501.03173)

**MObI: 拡散モデルを用いたマルチモーダルオブジェクトインペインティング**

Alexandru Buburuzan, Anuj Sharma, John Redford, Puneet K. Dokania, Romain Mueller

- 自動運転などの安全性が重要な分野では、多彩なマルチモーダルデータが必要
- 合成データはリアリズムと制御性が鍵であり、本研究はそれに応える枠組を提案
- MObIは拡散モデルを利用し、カメラとライダーのシーンにリアルなオブジェクトを挿入
- 3Dバウンディングボックスを使用し、位置とスケールを正確に制御可能に

この研究、すごく未来的だね！自動運転のテストも、これでますます進むんじゃない？拡散モデルでリアルにデータ増やせるなんて、ちょっと驚きだなぁ。

**Comment:** 8 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-06 17:43

- - -

### [Learning DAGs and Root Causes from Time-Series Data](http://arxiv.org/abs/2501.03130)

**時系列データからDAGと根本原因を学習する**

Panagiotis Misiakos, Markus Püschel

- DAG-TFRCという新手法が、時系列データから少ない根本原因を学習することを可能にする
- データは未知の特定ノードと時点で発生した少数のイベントにより生成されると想定
- 瞬時の依存関係と時間遅延依存関係を表現するDAGを学習し、位置と時間を特定する
- 合成データと現実の財務データで精度と実行時間が優れることを実証

少数のイベントから成る大きなネットワークを理解するって、ちょっとミステリーサスペンスみたいだよね！株式市場の動きが読み解ける技術が進むと、私たちの投資判断にも大革命が起こるかも！

**Comment:** 25 pages, 9 figures, conference preprint

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2025-01-06 16:48

- - -

### [CrowdProve: Community Proving for ZK Rollups](http://arxiv.org/abs/2501.03126)

**CrowdProve: ZKロールアップのためのコミュニティ証明**

John Stephan, Matej Pavlovic, Antonio Locascio, Benjamin Livshits

- ZKロールアップはブロックチェーンのスケーリングに貢献するが、証明生成に計算負荷がある
- 現在の解決策は中央集権的で、スケーラビリティと分散化を制限している
- CrowdProveは小規模なコミュニティのハードウェアを利用し、分散コンピューティングを可能にする手法を提案
- 実験評価により、コミュニティによる証明は中央化システムと同等以上の性能を実現可能と示された

ココ、おもしろいところだよね！コミュニティの力でZKロールアップを強化するなんて、めっちゃ革新的！みんなで力を合わせて、もっと効率的なシステムを作っていきたいよね！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.DC, **投稿日時:** 2025-01-06 16:34

- - -

### [From Models to Network Topologies: A Topology Inference Attack in Decentralized Federated Learning](http://arxiv.org/abs/2501.03119)

**モデルからネットワークトポロジーへ: 分散型連合学習におけるトポロジー推測攻撃**

Chao Feng, Yuanzhe Gao, Alberto Huertas Celdran, Gerome Bovet, Burkhard Stiller

- 連合学習はデータを直接交換せずにモデルを共有し、プライバシーを保つ
- 分散型FLではオーバーレイトポロジーがモデルの収束や安全性に影響を与える
- モデルの動作のみでDFLのトポロジーを推測する攻撃方法を提案
- 公開モデルの分析でトポロジーを推測可能、DFLの情報漏洩リスクを指摘

トポロジーをモデルから推測できちゃうなんて本当におもしろい発見！分散型の連合学習ってもっと安全だと思ってたけど、まだ改良の余地があるんだね。これを機にプライバシー技術も更に進化しそう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-06 16:27

- - -

### [TEE-based Key-Value Stores: a Survey](http://arxiv.org/abs/2501.03118)

**TEEベースのキーバリューストア: サーベイ**

Aghiles Ait Messaoud, Sonia Ben Mokhtar, Anthony Simonet-Boulogne

- キーバリューストア(KVS)はシンプルでスケーラブルなNo-SQLデータベースだが、データが機密な場合は強固なセキュリティが必要
- ソフトウェアベースの暗号化は機密性と完全性を維持するが、処理時セキュアでない場合が多く、信頼できるホスティングシステムを仮定
- 信頼実行環境(TEE)は処理中のデータをセキュアに保ち、非信頼環境でも信頼できるアプリケーションを構築可能
- TEEにはメモリサイズ制限やCPUコンテキストスイッチによるパフォーマンスの課題があり、それに対応する設計戦略を調査

TEEを使ったKVSのセキュリティ設計を詳しく解説してるのが面白そう！未来のデータの安全管理にどう役立つのか気になる～。仲間と意見交換して、もっと広がる可能性を見つけたいね！



**トピック:** [準同型暗号](he), [TEE](tee), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2025-01-06 16:26

- - -

### [Probably Correct Optimal Stable Matching for Two-Sided Markets Under Uncertainty](http://arxiv.org/abs/2501.03018)

**不確実性下の双方向市場におけるおそらく正しい最適安定マッチング**

Andreas Athanasopoulos, Anne-Marie George, Christos Dimitrakakis

- 左側の未知の好みに基づく安定結婚モデルの学習問題を扱う
- 純粋な探索問題として、バンディットフィードバックを用いて左側最適な安定マッチングを特定
- 最適な安定マッチングを見つけるためのバンディットアルゴリズムをいくつか提案
- 合成データによる実験分析で理論的なサンプル複雑性を検証し、理解を深める

双方向市場での好みの不確実性を考慮するのって、ちょっとワクワクするね！実践的なアプリケーションが広がったら、いろんな分野で使われそう。数学だけじゃなく、リアルな市場の問題解決にも役立てられるかも。

**Comment:** This paper was accepted to International Conference on Autonomous   Agents and Multiagent Systems (AAMAS 2025)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2025-01-06 13:59

- - -

### [CONTINUUM: Detecting APT Attacks through Spatial-Temporal Graph Neural Networks](http://arxiv.org/abs/2501.02981)

**CONTINUUM: 空間時間グラフニューラルネットワークを用いたAPT攻撃検出**

Atmane Ayoub Mansour Bahara, Kamel Soaïd Ferrahia, Mohamed-Lamine Messai, Hamida Seba, Karima Amrouche

- 高度な持続的脅威(APT)はサイバーセキュリティにおいて大きな課題であり、伝統的な侵入検知システムは不十分である
- グラフニューラルネットワーク(GNN)はネットワークデータの複雑な関係を解析し、IDS機能を強化するが、高い誤検出率とリソース消費が問題となっている
- 空間情報と時間的情報を活用し、APTの多段階的な攻撃を識別する新たなIDSを提案
- federation learning環境で秘密性を保ちつつ効率的にAPTを検出し、誤検出率とリソース使用量を最適化する

APTを空間と時間の両面から分析するってすごく頭いい！プライバシーもちゃんと守られて安心だね。ますますサイバーセキュリティが強化されて安心してインターネットを使えそうだよ！

**Comment:** 31 pages

**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** cs.CR, cs.AI, cs.NI, **投稿日時:** 2025-01-06 12:43

- - -

### [Proof-of-Data: A Consensus Protocol for Collaborative Intelligence](http://arxiv.org/abs/2501.02971)

**データの証明：協調型インテリジェンスのための合意プロトコル**

Huiwen Liu, Feida Zhu, Ling Cheng

- 連合学習を中央集権から分散型へ移行する課題に着目
- PoDコンセンサスプロトコルを提案し、信頼性とインセンティブを解決
- モデル訓練と貢献度計算を分離し、効率と合意を両立
- プライバシーに配慮したデータ検証と報酬分配メカニズムを設計

分散型で公平なインセンティブを実現するって、考えるだけでワクワクするよね！Byzantine攻撃を乗り越える手法も魅力的で、技術と創造性が詰まった未来を想像しちゃうな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2025-01-06 12:27

- - -

### [AFed: Algorithmic Fair Federated Learning](http://arxiv.org/abs/2501.02732)

**AFed: アルゴリズム的公正な連合学習**

Huiqiang Chen, Tianqing Zhu, Wanlei Zhou, Wei Zhao

- 連合学習はデータをサーバに集約せずにクライアント間での協調学習を可能にする技術
- しかし、従来のバイアス除去法が使えず、公正性の課題が発生しやすくなる
- 提案されたAFedは制限されたデータアクセスを回避してグローバルなデータ分布を学習
- AFed-GとAFed-GANという二つのアプローチを導入し、実証実験で公正性の改善を確認

難しそうだけど面白そう！連合学習の公平性を改善する新しい方法なんだって。この技術が進化すれば、もっと多くの場面で使いやすいAIが増えていくかもね！やってみようよ！

**Comment:** Accepted by IEEE Transactions on Neural Networks and Learning Systems

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-06 03:05

- - -

### [Incentive-Compatible Federated Learning with Stackelberg Game Modeling](http://arxiv.org/abs/2501.02662)

**スタックルバーグゲームモデルによるインセンティブ互換な連合学習**

Simin Javaherian, Bryce Turney, Li Chen, Nian-Feng Tzeng

- 連合学習はデータプライバシーを守りつつ協調的にグローバルモデルを訓練する手法
- 従来の方法は非IID環境で公平性や効率性が欠如する問題がある
- FLammaはスタックルバーグゲームを用いて公平性を高めるフレームワーク
- 提案手法は従来の方法よりも精度の公平な分配を実現し、モデル性能を損なわない

FLでクライアント間の公平性が向上するなんて面白そう！一方的じゃなくて、ゲーム理論を使ってバランスを取るのがステキだね。どんなクライアント環境でも効率的に動く未来が楽しみだよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2025-01-05 21:04

- - -

### [FedRSClip: Federated Learning for Remote Sensing Scene Classification Using Vision-Language Models](http://arxiv.org/abs/2501.02461)

**FedRSClip: 画像と言語モデルを使用したリモートセンシングシーン分類のための連合学習**

Hui Lin, Chao Zhang, Danfeng Hong, Kexin Dong, Congcong Wen

- プライバシーとデータ共有制限により、リモートセンシングデータの集中的なトレーニングが難しい
- FedRSCLIPは、CLIPベースの画像と言語モデルを用いたリモートセンシング向け連合学習フレームワーク
- プロンプト学習を導入し、少数の調整可能パラメータに最適化し通信コストを削減
- デュアルプロンプトメカニズムとクロスモーダル特徴整合性制約でグローバルとローカルの適応を両立

リモートセンシングの世界にも連合学習の波が来てるんだねー！プライバシーを守りながら、より賢い地球把握ができるなんてワクワクしちゃう～。どんどん技術が進化して、これから未来がますます楽しくなる予感がする感じ。🌍💫



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2025-01-05 07:10

- - -

### [Efficient Deployment of Large Language Models on Resource-constrained Devices](http://arxiv.org/abs/2501.02438)

**リソース制約されたデバイスへの大規模言語モデルの効率的配置**

Zhiwei Yao, Yang Xu, Hongli Xu, Yunming Liao, Zuan Xie

- 大規模言語モデル(LLM)をリソース制約デバイスで展開するには、デバイス上でのプライベートなデータを用いた微調整が必要
- 連合学習はプライバシー保護に有望だが、従来の微調整方法だと推論遅延やメモリ問題が残る
- FedSpineフレームワークを導入し、効率的な微調整と整ったパラメータ削減でLLM展開を最適化
- MABアルゴリズムでデバイスごとに異なる削減比率を適応的に決定し、推論精度を維持しつつ効率改善

デバイスでスムーズにAIが動くようになるなんて未来がますます楽しみだよね！こんな研究があると、みんなの手元でAIのパワーをもっと生かせるようになりそう♡



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CL, cs.DC, **投稿日時:** 2025-01-05 04:38

- - -

### [JammingSnake: A follow-the-leader continuum robot with variable stiffness based on fiber jamming](http://arxiv.org/abs/2501.02410)

**JammingSnake: 繊維ジャミングに基づく可変剛性を持つリーダーフォロー型コンティニュアムロボット**

Chen Qian, Tangyou Liu, Liao Wu

- コンティニュアムロボットのFTL動作は脆弱で狭い環境を傷つけない動作に必要
- 新しい蛇型ロボットは繊維ジャミングモジュールで可変剛性を実現
- テンションとFJMの動きを独立制御するアルゴリズムにより形状維持と力の最小化を両立
- 伝統的なロボットと比較試験の結果、新設計は周囲への接触依存減少を実証

繊維ジャミングを使ってロボットが環境に優しくなるなんて、未来の手術にも活躍しそうで期待できるかも！従来の難しい環境でも、このロボットならスムーズに動きそうだね。

**Comment:** 8 pages, 4 figures, submitted to T-MECH

**トピック:** [連合転移学習](ftl), **カテゴリ:** cs.RO, cs.SY, eess.SY, **投稿日時:** 2025-01-05 01:04

- - -

### [PrivDPR: Synthetic Graph Publishing with Deep PageRank under Differential Privacy](http://arxiv.org/abs/2501.02354)

**PrivDPR: 差分プライバシー下のディープPageRankを用いた合成グラフの公開**

Sen Zhang, Haibo Hu, Qingqing Ye, Jianliang Xu

- プライバシーを保護しつつ、元データの有用性を維持することが目的。
- 現在の手法は差分プライバシーで高感度や小さなプライバシー予算に悩む。
- PrivDPRは学習中の特定の重みにノイズを加えることで差分プライバシーを実現。
- 実データでの実験で、複数のグラフ特性にわたりデータの有用性を保つことを確認。

うわー、PageRankを利用したプライバシー保護って新鮮だね！なんか未来のグラフ解析がもっと安心してできるようになる予感！😆

**Comment:** Accepted by KDD 25

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DB, cs.CR, **投稿日時:** 2025-01-04 18:19

- - -

### [Reweighting Improves Conditional Risk Bounds](http://arxiv.org/abs/2501.02353)

**再重み付けが条件付きリスク境界を改善**

Yikai Zhang, Jiahe Lin, Fengpei Li, Songzhu Zheng, Anant Raj, Anderson Schneider, Yuriy Nevmyvaka

- 加重ERMは、データ依存の重み関数を組み込んだ経験リスク最小化の手法である
- 「バランス可能」なベルンシュタイン条件に基づき、加重ERM推定量は特定の領域で高性能を発揮
- クラス分類では大きなマージン、ヘテロスケダスティック回帰では低分散の領域に対応
- 合成データによる実験で、加重ERMの利点が証明されている

難しそうだけど、データに応じた重みを付けることで、分析がもっと正確にできそうだよね。それに、この方法なら特定の条件で他の手法よりも有利になるなんて面白そう！

**Comment:** 33 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, G.3; I.3, **投稿日時:** 2025-01-04 18:16

- - -

### [PM-Dedup: Secure Deduplication with Partial Migration from Cloud to Edge Servers](http://arxiv.org/abs/2501.02350)

**PM-Dedup: クラウドからエッジサーバへの部分移行による安全な重複除去**

Zhaokang Ke, Haoyu Gong, David H. C. Du

- クラウド上のデータ保存には暗号化が必要で、鍵違いが重複除去を困難にする
- 暗号化重複除去は同一データに同じ暗号文を生成し、重複を効率的に除去可能にする
- 現行手法はクライアントの負担を増やし、ネットワークやクラウドに高いオーバーヘッドを生じさせる
- PM-Dedupは一部のプロセスをエッジサーバに移し、セキュリティと効率を向上させる

クラウドとエッジをうまく使えば、もっと快適に安全なデータ管理ができそう！重複除去の新しいアプローチが、きっとこれからのデータ保存に役立つよね。興味津々だわ！



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.NI, **投稿日時:** 2025-01-04 18:12

- - -

### [Diffusion Model-Based Data Synthesis Aided Federated Semi-Supervised Learning](http://arxiv.org/abs/2501.02219)

**拡散モデルを用いたデータ合成による連合半教師あり学習の支援**

Zhongwei Wang, Tong Wu, Zhiyong Chen, Liang Qian, Yin Xu, Meixia Tao

- 連合半教師あり学習はラベル付きデータの不足と非IIDなデータ分布が課題
- 拡散モデルにより合成データを生成し、ローカルとグローバルデータ分布の差を埋める
- 未ラベルデータには擬似ラベリングを行い、合成データの生成を協力して改善
- CIFAR-10で10%ラベル付きデータの精度が38.46%から52.14%に向上

拡散モデルと連合学習の組み合わせでこんなに精度が上がるのすごいね！ラベル付きデータが少ない中で、新たなアプローチがデータ分布の課題をうまく解決してくれそう。面白そうだなぁ！

**Comment:** accepted by IEEE WCNC 2025

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.IT, math.IT, **投稿日時:** 2025-01-04 07:38

- - -

### [Automatically Learning a Precise Measurement for Fault Diagnosis Capability of Test Cases](http://arxiv.org/abs/2501.02216)

**テストケースの故障診断能力を精密に測定するための自動学習**

Yifan Zhao, Zeyu Sun, Guoqing Wang, Qingyuan Liang, Yakun Zhang, Yiling Lou, Dan Hao, Lu Zhang

- 故障の特定にはテストが重要で、FDCを測定することでテストが効果的に利用可能
- 現行のFDC指標は結果無関係型と結果関係型に分けられ、それぞれ用途が異なる
- 新しい結果無関係型指標RLFDCを強化学習で提案し、より正確な測定を自動学習
- RLFDCは既存の結果無関係型指標を上回り、テスト選定や生成で良好な性能を示す

強化学習を使ってテストケースの故障診断能力を自動で精密に測るなんてすごく斬新！プログラムのバグ取りがもっと効率的になる未来が見えるね、すごく楽しみなの！

**Comment:** This paper has been accepted by TOSEM

**トピック:** [連合学習](fl), **カテゴリ:** cs.SE, **投稿日時:** 2025-01-04 07:16

- - -

### [Phase Retrieval by Quaternionic Reweighted Amplitude Flow on Image Reconstruction](http://arxiv.org/abs/2501.02180)

**イメージ再構成における四元数リウェイト振幅フローによる位相復元**

Ren Hu, Pan Lian

- 四元数信号処理により、信号の次元間での相関を保ちながらカラーデータを効率的に管理
- 振幅ベースのモデルを用いて四元数の位相復元問題を解決する新アルゴリズムを開発
- Quaternionic Reweighted Amplitude Flow (QRAF) アルゴリズムを提案し、3つのバリエーションを追加
- 合成データと実画像での実験により、高速かつ高性能な復元を実現

四元数って知ってた？数学的には難しそうだけど、画像の色を効率よく扱うって結構すごいかも！画像復元がもっと早くてきれいになるなら、未来の技術が楽しみだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, math.CV, 94A08, 46S05, 11E88,, **投稿日時:** 2025-01-04 04:09

- - -

### [DreamMask: Boosting Open-vocabulary Panoptic Segmentation with Synthetic Data](http://arxiv.org/abs/2501.02048)

**DreamMask: 合成データによるオープンボキャブラリー全画素セグメンテーションの強化**

Yuanpeng Tu, Xi Chen, Ser-Nam Lim, Hengshuang Zhao

- オープンボキャブラリー全画素セグメンテーションでは、既存のカテゴリ以外の新しいクラスへの一般化が課題
- DreamMaskは、実データと合成データを活用し、モデルのトレーニングデータ生成をシステマチックに行う方法を提案
- 自動データ生成パイプラインを通じ、オフ・ザ・シェルフなモデルを利用して語彙やレイアウトを拡張する
- 合成データと実データのギャップを埋める損失設計により、複数ベンチマークで性能向上を実現

この論文、めっちゃ未来感あるね！合成データで汎用性を高めるなんて、新しいアイディアが詰まってる感じがする。これからの技術にとって、すごく発展しそうだよね。

**Comment:** Project url: https://yuanpengtu.github.io/Dreammask-Page/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-03 19:00
