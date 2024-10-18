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

更新: 2024-10-18T04:23:56.278205

- - -

### [DPFedBank: Crafting a Privacy-Preserving Federated Learning Framework for Financial Institutions with Policy Pillars](http://arxiv.org/abs/2410.13753)

**DPFedBank: 金融機関のためのプライバシー保護型連合学習フレームワークの構築と政策の柱**

Peilin He, Chenkai Lin, Isabella Montoya

- DPFedBankは、金融データの共有でデータプライバシーを守るための革新的なフレームワークを提供する
- Local Differential Privacy (LDP) を活用し、連合学習中も機密情報を開示せずに情報共有を可能にする
- 提案フレームワークは、悪意のあるクライアントやサーバー、外部の攻撃者からの脅威を効果的に緩和する
- 自己適応型LDPと暗号技術を組み合わせ、プライバシー強化とモデル性能の両立を実現する

金融データのプライバシー保護って難しそうだけど、DPFedBankの登場で新しい希望があるかも！これからもっと安心してデータを使った未来の金融サービスが進化する可能性が楽しみだね。💡✨

**Comment:** 9 pages, 1 figure

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CE, cs.CR, cs.CY, **投稿日時:** 2024-10-17 16:51

- - -

### [Privacy-Preserving Decentralized AI with Confidential Computing](http://arxiv.org/abs/2410.13752)

**プライバシー保護の分散AIと秘密計算**

Dayeol Lee, Jorge Antonio, Hisham Khan

- 分散AIは透明性と堅牢性を高めるが、プライバシー課題を生む
- ゼロ知識機械学習は計算コストが高すぎる問題がある
- 秘密計算を活用し、ハードウェアによるデータ処理の隔離を実現
- 信頼できない環境でもモデルとユーザー情報を保護する可能性を探る

分散AIと秘密計算が結びつくなんて、すごい未来を感じるよね！特に、信頼できない環境でも安全なデータ処理ができるようになったら、もっと楽しくなりそう！



**トピック:** [ゼロ知識証明](zkp), [TEE](tee), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-10-17 16:50

- - -

### [On-device Federated Learning in Smartphones for Detecting Depression from Reddit Posts](http://arxiv.org/abs/2410.13709)

**スマートフォン上での連合学習によるReddit投稿からのうつ病検出**

Mustofa Ahmed, Abdul Muntakim, Nawrin Tabassum, Mohammad Asifur Rahim, Faisal Muhammad Shah

- 人のメンタルヘルス状態を示すソーシャルメディア投稿を利用し、深層学習モデルでうつ病検出を探求
- ユーザーデータを守りつつスマートフォンで連合学習を採用し、分散的なトレーニングを実現
- Reddit投稿を用いたGRU、RNN、LSTMの3つのニューラルネットワークでうつ病の兆候を検出
- 実世界の連合学習環境で、リソース消費と通信コストを分析し、比較可能なモデル性能を実証

この研究ってほんとにすごいと思う！スマホでユーザーのプライバシーを守りつつ、うつ病を検出できるってすごく未来的だし、もっと身近な医療の一歩だよね。どんどん進化して、もっと多くの人の助けになりそう！

**Comment:** 11 pages, 7 figures, Submitted to IEEE

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-17 16:09

- - -

### [Diffusion Curriculum: Synthetic-to-Real Generative Curriculum Learning via Image-Guided Diffusion](http://arxiv.org/abs/2410.13674)

**拡散カリキュラム：画像誘導拡散による合成から実世界への生成カリキュラム学習**

Yijun Liang, Shweta Bhardwaj, Tianyi Zhou

- データの低品質や不足は深層学習の大きな課題であり、拡散モデルは高品質で多様な合成データ生成を可能にする。
- テキスト誘導のみでは元画像との距離を制御できず、外れ値データがモデル性能を低下させる。
- 画像誘導を用いることで合成と実画像間のスペクトルを実現し、適応学習が可能に。
- 提案手法DisCLは高品質な低誘導画像から始め、学習が困難な高誘導画像へと段階的に焦点を当てる。

合成データを使って、実データとのギャップを埋める新しいアプローチって面白い！学習のステージごとに適応させていけるなら、もっと汎用性や応用範囲が広がりそうだね。将来、もっと様々な課題で使われるのかなって期待しちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-10-17 15:33

- - -

### [Towards Satellite Non-IID Imagery: A Spectral Clustering-Assisted Federated Learning Approach](http://arxiv.org/abs/2410.13602)

**衛星非IID画像に向けたスペクトルクラスタリング支援連合学習アプローチ**

Luyao Zou, Yu Min Park, Chu Myaet Thwal, Yan Kyaw Tun, Zhu Han, Choong Seon Hong

- LEO衛星がIoTアプリケーション用の豊富な地球観測データを収集可能、しかしデータ処理には課題
- 地上にデータを送らず衛星で処理するための方法として、スペクトルクラスタリングを活用
- 非IIDデータに対応するため、正規化ラプラシアンベースのクラスタリングを連合学習に導入
- 実験結果として、提案手法は観測精度で既存手法を上回る成果を示した

地球に送らずに衛星でデータを処理するなんてかっこよくない!? LEO衛星を使った観測精度向上も楽しみだなー！✨

**Comment:** 10 pages, 5 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.LG, **投稿日時:** 2024-10-17 14:36

- - -

### [CCUP: A Controllable Synthetic Data Generation Pipeline for Pretraining Cloth-Changing Person Re-Identification Models](http://arxiv.org/abs/2410.13567)

**CCUP: 布の交換が可能な人物再識別モデルの事前学習用合成データ生成パイプライン**

Yujian Zhao, Chengru Wu, Yinong Xu, Xuanzheng Du, Ruiyu Li, Guanglin Niu

- 布の交換が関係する人物再識別はコンピュータビジョンで重要かつ困難なテーマ
- 高コストなデータ構築が課題で、データ不足で過学習が問題となる
- 合成データ生成パイプラインを提案し、低コストで高品質なデータを実現
- 大規模データセットCCUPを用いてモデルの一般化能力を向上

この技術が進化したら、人が何を着ていても識別できるなんて驚きだね！AIの能力がどんどん高まっていくのを感じるし、将来的には防犯にも役立ちそうだよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-10-17 14:04

- - -

### [Three-Input Ciphertext Multiplication for Homomorphic Encryption](http://arxiv.org/abs/2410.13545)

**準同型暗号における三入力暗号文乗算**

Sajjad Akherati, Yok Jye Tang, Xinmiao Zhang

- 準同型暗号は暗号文上で計算を直接行う技術で、プライバシー保護に重要
- 現在の主流技術では二入力の乗算のみが定義されている
- 本研究は三入力暗号文の乗算を提案し、計算の複雑さを軽減
- 提案手法で従来の手法と比べてレイテンシ半減、29%の小面積化、低ノイズを実現

準同型暗号って難しいけど、こんなユニークな解決策があると面白いね！これを応用することで、もっといろんなところで使われる未来が待ってるかも。

**Comment:** 5 pages, 2 figures, 2 tables, conference paper

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AR, **投稿日時:** 2024-10-17 13:40

- - -

### [Can Medical Vision-Language Pre-training Succeed with Purely Synthetic Data?](http://arxiv.org/abs/2410.13523)

**医用視覚言語事前学習は純粋な合成データで成功するか？**

Che Liu, Zhongwei Wan, Haozhe Wang, Yinda Chen, Talha Qaiser, Chen Jin, Fariba Yousefi, Nikolay Burlutskiy, Rossella Arcucci

- 医療の視覚と言語の事前学習は、大規模で高品質な画像・テキストデータセットを必要とするが、医療分野では希少
- 合成データの利用により、モデルの学習精度が実データ使用時よりも3.8%高い性能を発揮
- 合成データと実データを組み合わせると、さらに9.07%の性能向上が確認できる
- 合成データによる学習は、ゼロショット分類やセグメンテーションタスクで高品質な結果を生み出す

おぉ～、合成データってすごい！将来的に、もっと安価で手軽にデータが手に入る時代になりそうね。医療分野だけじゃなく、他のいろんな分野でも応用できそうでワクワクする～！

**Comment:** Under Review

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-10-17 13:11

- - -

### [Towards Formal Verification of Federated Learning Orchestration Protocols on Satellites](http://arxiv.org/abs/2410.13429)

**衛星上での連合学習オーケストレーションプロトコルの形式的検証に向けて**

Miroslav Popovic, Marko Popovic, Miodrag Djukic, Ilija Basicevic

- PTB-FLAはIoT向けの連合学習フレームワークで、中央集権型と分散型アルゴリズムを提供
- 静止ノード向けプロトコルの検証にCSPを用いて形式的検証を行うが、移動ノードには適用不可
- 本研究では天体力学を用いて宇宙機の動きをモデル化し、中央集権型プロトコルを二段階で検証
- 初段階でTAモデルによるプロパティの証明、二段階で確率モデルでタイミングと終了確率を推定

ええ、連合学習の技術が宇宙レベルまで応用されるなんて、ワクワクしちゃうね！信頼性もちゃんと検証しようとしてるところが未来を感じる！

**Comment:** 4 pages, 5 figures, submitted to a conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-10-17 10:52

- - -

### [Unsupervised Skull Segmentation via Contrastive MR-to-CT Modality Translation](http://arxiv.org/abs/2410.13427)

**無監督の頭蓋骨セグメンテーション: 対照的なMRからCTへのモダリティ翻訳**

Kamil Kwarciak, Mateusz Daniol, Daria Hemmerling, Marek Wodzinski

- MR画像の頭蓋骨セグメンテーションは骨ではなく軟組織が主で、CTよりも複雑
- MRを直接セグメントせず、合成CTデータ生成を介して頭蓋骨セグメンテーションを実施
- 無監督手法でMRとCTデータセットのペアリングしない問題や解像度低下を克服
- 合成データの医療画像利用を促進し、手術計画などの下流タスクに寄与

CTとの変換を使ってMRでの課題を解決しちゃうなんてすごい！合成データでの新しい試みも、医療の世界にもっと広がってほしいなって思った！

**Comment:** 16 pages, 5 figures, ACCV 2024 - GAISynMeD Workshop

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-10-17 10:51

- - -

### [Enhancing Dataset Distillation via Label Inconsistency Elimination and Learning Pattern Refinement](http://arxiv.org/abs/2410.13311)

**ラベル不整合の排除と学習パターンの改良によるデータセット蒸留の強化**

Chuhao Zhou, Chenxi Jiang, Yi Xie, Haozhi Cao, Jianfei Yang

- データセット蒸留（DD）は、モデルが全データセットを使用した場合と同様の性能を実現するために必要なデータセットの要約を作成する技術。
- 膨大なデータ処理を不要にし、計算リソース、保存スペース、時間のコストを削減する。
- ECCV-2024 Data Distillation Challengeで1位を獲得した手法M-DATMを紹介。
- ソフトラベル技術を削除し不整合を緩和、合成データが簡単なパターンに集中できるように改良。

データの要約力アップでコスパ最高だね！画像データでも性能1位なんてすごい！もっと効率良くAIモデルを改善できそうだよね。これからの研究、楽しみになっちゃう！

**Comment:** ECCV 2024 Dataset Distillation Challenge

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-17 08:09

- - -

### [FRAG: Toward Federated Vector Database Management for Collaborative and Secure Retrieval-Augmented Generation](http://arxiv.org/abs/2410.13272)

**FRAG: 協調的かつ安全な検索補強型生成のための連合ベクトルデータベース管理に向けて**

Dongfang Zhao

- FRAGは、対話を信頼しない複数の関係者が共に暗号化されたベクトルデータベースで検索する仕組みを提供
- 強いセキュリティ保証を持ちながら、プラクティカルな性能を伝統的システムに匹敵させるのが課題
- 単一鍵準同型暗号プロトコルと乗算キャッシュを用いて鍵管理を簡素化し、計算性能を改善
- クリプトグラフィックな還元を用いた強固なセキュリティ証明と大規模実験での実用的スケーラビリティを実証

連合学習とセキュリティを融合したアイデアってなんか面白そうだよね！データを互いに知られずに共同作業できる未来が現実に近づいてる感じがするなぁ。そんな仕組みって、例えば友だちと一緒に勉強する時にもプライバシーを守れるのかも！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-10-17 06:57

- - -

### [Cyber Attacks Prevention Towards Prosumer-based EV Charging Stations: An Edge-assisted Federated Prototype Knowledge Distillation Approach](http://arxiv.org/abs/2410.13260)

**サイバー攻撃予防に向けたプロシューマー型EV充電ステーションへのエッジ支援型連合プロトタイプ知識蒸留アプローチ**

Luyao Zou, Quang Hieu Vo, Kitae Kim, Huy Q. Le, Chu Myaet Thwal, Chaoning Zhang, Choong Seon Hong

- プロシューマー型EV充電ステーションのサイバー攻撃予防が研究対象で、攻撃検出と介入を含む
- 傾向として、プロシューマーのネットワークトラフィックデータは非独立同分布であり、攻撃の境界が不明瞭
- 提案するエッジ支援型連合プロトタイプ知識蒸留（E-FPKD）では、知識蒸留とプロトタイプ集約を組み込む
- 提案手法は、ODC計算で資源効率を向上し、実験では基準を超える高い検出性能を実証

サイバー攻撃に強いEV充電ステーションって未来に必要だよね！この研究、トラフィックデータをうまく分析するアプローチが面白そうじゃない？きっと持続可能なモビリティ社会にとって重要な一歩になると思うな。

**Comment:** 27 pages, 12 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-17 06:31

- - -

### [Investigating Effective Speaker Property Privacy Protection in Federated Learning for Speech Emotion Recognition](http://arxiv.org/abs/2410.13221)

**音声感情認識におけるフェデレーション学習の話者属性プライバシー保護の効果的な調査**

Chao Tan, Sheng Li, Yang Cao, Zhao Ren, Tanja Schultz

- フェデレーション学習はユーザーデータの代わりにモデルを集約してプライバシーを保護
- 音声感情認識での応用においても推論攻撃に弱点があることが判明
- 音声データの属性を分解し、摂動を加える新しい保護手法を提案
- 提案手法は既存方法よりもプライバシーと実用性のバランスが良く、攻撃防止効果が高い

フェデレーション学習が音声感情認識のプライバシー保護に使われるなんて面白いよね！新しい方法がこんなに効果的なら、もっといろんなアプリでこの手法が使われるようになったらいいな。



**トピック:** [連合学習](fl), **カテゴリ:** eess.AS, cs.SD, **投稿日時:** 2024-10-17 05:03

- - -

### [Failing Forward: Improving Generative Error Correction for ASR with Synthetic Data and Retrieval Augmentation](http://arxiv.org/abs/2410.13198)

**前進の失敗: 合成データとリトリーバル増強によるASRの生成的誤り訂正の改善**

Sreyan Ghosh, Mohammad Sadegh Rasooli, Michael Levit, Peidong Wang, Jian Xue, Dinesh Manocha, Jinyu Li

- ASRの生成的誤り訂正(GEC)は、特定の誤りの一般化が難しく、新しい誤りを訂正しにくい
- 名前付き実体(NE)に特に困難があり、新しいNEは文脈や知識不足で解決が難しい
- DARAGは合成データを活用し、トレーニングデータを増強してGECを改善するアプローチである
- さまざまなデータセットでの実験でDARAGが優れた性能を示し、WERが向上

ASRシステムをもっともっと賢くするために、合成データでいっぱい練習させてるみたい！新しい名前とかも上手に認識できるようになるなんてすごいよね。試してみたら、精度がぐんと上がるなんて、これからいろんな場面で役立ちそうだね！

**Comment:** Preprint. Under Review

**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.CL, cs.SD, **投稿日時:** 2024-10-17 04:00

- - -

### [L1-Regularized ICA: A Novel Method for Analysis of Task-related fMRI Data](http://arxiv.org/abs/2410.13171)

**L1-正則化ICA: タスク関連fMRIデータの解析のための新手法**

Yusuke Endo, Koujin Takeda

- 高次元データから適切な特徴を抽出する新しい独立成分分析(ICA)手法を提案
- 特徴の解釈可能性向上のため、因子分解行列にスパース制約を適用
- ICAのコスト関数にL1-正則化項を追加し、凸関数の差による最小化を行う
- 提案手法の有効性は、合成データと実際のfMRIデータを用いて検証

fMRIデータって脳の神経活動をキャッチするから、解釈の改善って大事だよね。この手法が脳研究にどんどん貢献する未来が楽しみ！

**Comment:** 29 pages, 9 figures, 4 tables. Python code is available. Please   contact the corresponding author for the code

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cond-mat.dis-nn, cs.LG, q-bio.NC, **投稿日時:** 2024-10-17 02:54

- - -

### [Federated scientific machine learning for approximating functions and solving differential equations with data heterogeneity](http://arxiv.org/abs/2410.13141)

**データの異質性を考慮した関数近似と微分方程式を解くための連合科学機械学習**

Handi Zhang, Langchen Liu, Lu Lu

- 科学機械学習(SciML)は、偏微分方程式(PDE)に基づく複雑な問題に対応するための新しい手法を提供する。
- 連合学習(FL)は、データプライバシーを保持しつつ分散データの課題を解決し、グローバルモデルを協同で学習する枠組みである。
- FedPINNとFedDeepONetの2つの新しいモデルを提案し、1-Wasserstein距離を用いて関数近似とPDE学習におけるデータの異質性を定量化する。
- フェデレーションされた手法は、ローカルデータのみを使用したモデルよりも性能が優れており、集中型モデルとほぼ同等の精度を達成することが示された。

連合学習と科学機械学習の組み合わせは、今後さらに発展しそうだよね。データの異質性を克服しつつ精度を向上できるのは魅力的かも！これで大規模データを扱う時代にも対応できそうだなって思ったよ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, physics.comp-ph, **投稿日時:** 2024-10-17 01:57

- - -

### [A Little Human Data Goes A Long Way](http://arxiv.org/abs/2410.13098)

**少量の人間データがもたらす大きな効果**

Dhananjay Ashok, Jonathan May

- NLPシステムで合成データ生成が注目されているが、全てを人間アノテーションで置き換える効果は不明
- 合成データで人間生成データを徐々に置き換える実験で、90%まで置き換えた際の性能低下が小さい
- 最後の10%を合成データにすると急激な性能低下が発生し、人間生成データ125点で性能向上が得られる
- 価格比を推定し、人間アノテーションが合成データよりも経済的なケースを示す

合成データって、少ない人間データと組み合わせると、思ったより効果があるんだ！コスト考える上で、この研究は企業が導入する際の指針になりそうで面白いね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-10-17 00:04

- - -

### [Communication-Efficient and Tensorized Federated Fine-Tuning of Large Language Models](http://arxiv.org/abs/2410.13097)

**大規模言語モデルのコミュニケーション効率的かつテンソル化された連合ファインチューニング**

Sajjad Ghiasvand, Yifan Yang, Zhiyu Xue, Mahnoosh Alizadeh, Zheng Zhang, Ramtin Pedarsani

- 大規模言語モデルは通常、単一クライアントのデータでのトレーニングを想定
- 連合学習でプライバシーを守りつつ、複数デバイスでのファインチューニングを提案
- FedTTとFedTT+の手法で、通信負荷とデータ異質性に対応可能
- 実験では通信コストを最大10倍削減しつつ、高性能を実証

連合学習でのファインチューニングって、まるでみんなで一緒に特訓しているみたいでワクワクするよね。今後もさらなる効率化を期待しちゃうな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CL, **投稿日時:** 2024-10-16 23:50

- - -

### [FedCAP: Robust Federated Learning via Customized Aggregation and Personalization](http://arxiv.org/abs/2410.13083)

**FedCAP: カスタマイズされた集約と個別化を通じた堅牢な連合学習**

Youpeng Li, Xinda Wang, Fuxun Yu, Lichao Sun, Wenbin Zhang, Xuyu Wang

- 連合学習はプライバシーを保護するが、データの偏りやビザンチン攻撃に脆弱
- FedCAPは、モデル更新の較正メカニズムでクライアント間の更新差を捉える
- 類似クライアント間での協調学習を促進し、悪意あるクライアントの悪化を加速
- ユークリッドノルムに基づく異常検出で悪意あるクライアントを迅速に排除

連合学習ってとっても便利そうだけど、どうやって攻撃とか偏りから守るのかって大変そう。でもこのFedCAPなら、その辺うまくやってくれそうで安心かもね。データの偏りとか、悪意あるユーザーへの対応を考えられるなんて、未来の技術だね！

**Comment:** 14 pages, 12 figures, 5 tables, accepted by 2024 Annual Computer   Security Applications Conference (ACSAC 2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-10-16 23:01

- - -

### [FedGTST: Boosting Global Transferability of Federated Models via Statistics Tuning](http://arxiv.org/abs/2410.13045)

**FedGTST：統計調整による連合モデルのグローバル移行性向上**

Evelyn Ma, Chao Pan, Rasoul Etesami, Han Zhao, Olgica Milenkovic

- 移行学習は大規模データセットと多大な計算資源を要し、単独では困難
- 連合学習はコラボでデータセットを間接的に拡大し、計算コストを分散しプライバシーを保護
- 現行のFLはローカルドメイン転送性最適化にとどまり、グローバルドメイン未考慮
- FedGTSTを提案し、クライアント間の勾配ノルムを活用し、ターゲットロスを制御

この研究って、すごく画期的だよね！移行学習の課題を連合学習でうまく解決しようとしているところが面白そう。これからの連合学習がもっと進化していくのが楽しみだな～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-16 21:13

- - -

### [A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'](http://arxiv.org/abs/2410.12954)

**Shumailovらによる「再帰的に生成されたデータで訓練されたAIモデルは崩壊する」に関する一考察**

Ali Borji

- Shumailovらは合成データでの繰り返し訓練がモデル崩壊を引き起こすことを示した
- データがほぼ枯渇している現在、この発見は大きな関心と議論を呼んでいる
- 本研究はデータへの分布適合後の繰り返しサンプリングの影響を調査する
- 結果は統計的現象であり、避けられない可能性が示唆された

データが枯渇しつつある中で、生成データによるモデル崩壊の避けられない問題があるなんて、AIの未来がどう展開していくのか気になるよね。これからどうやってこの問題に向き合っていけるのか、ワクワクする！

**Comment:** Comment on https://doi.org/10.1038/s41586-024-07566-y

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-16 18:43

- - -

### [Syn2Real Domain Generalization for Underwater Mine-like Object Detection Using Side-Scan Sonar](http://arxiv.org/abs/2410.12953)

**サイドスキャンソナーを用いた海中機雷対象検出のためのSyn2Realドメイン一般化**

Aayush Agrawal, Aniruddh Sikdar, Rajini Makam, Suresh Sundaram, Suresh Kumar Besai, Mahesh Gopi

- 深層学習を用いた海中機雷検出は、現実世界のデータ不足が原因で過学習を起こしやすい
- 本研究は、拡散モデルを使用したSyn2Realドメイン一般化アプローチでこの問題に対処
- DDPMとDDIMモデルを用いて生成した合成データは、現実のサンプルを効果的に補強する
- 合成データとオリジナルデータセットを合わせた場合、平均精度が約60%向上

海中での機雷検出に合成データを使って精度を大幅に上げるなんてすごいよね。未来の探査技術がますます進化しそうでワクワクするし、海の謎がもっと解き明かされる予感がするよ！

**Comment:** 7 pages, 4 figures and 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, eess.IV, **投稿日時:** 2024-10-16 18:42

- - -

### [DEeR: Deviation Eliminating and Noise Regulating for Privacy-preserving Federated Low-rank Adaptation](http://arxiv.org/abs/2410.12926)

**DEeR: プライバシー保護されたフェデレーテッド低ランク適応のための偏差除去とノイズ調整**

Meilu Zhu, Axiu Mao, Jun Liu, Yixuan Yuan

- LoRAとFLの直接的な組み合わせは集約偏差とDPノイズ増幅問題を引き起こす
- DEeRはLoRAパラメータの同等性を保証して集約偏差をゼロにすることを理論的に証明
- ノイズ増幅はDPノイズとLoRAの「線形関係」が原因で、これを規制するノイズレギュレータを提案
- ablated実験でDEeRの偏差除去器とノイズレギュレータの効果を実証し、高性能を確認

プライバシーを保ちながら医療データを使った学習ができるって、すごく現代的よね！これからの医療AIの発展に貢献しそうでワクワクしちゃう！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-16 18:11

- - -

### [A Survey on Data Synthesis and Augmentation for Large Language Models](http://arxiv.org/abs/2410.12896)

**大規模言語モデルのためのデータ生成と拡張に関する調査**

Ke Wang, Jiahui Zhu, Minjie Ren, Zeming Liu, Shiwei Li, Zongye Zhang, Chenkai Zhang, Xiaoyu Wu, Qiqi Zhan, Qingjie Liu, Yunhong Wang

- 大規模言語モデル(LLMs)の成功は多様かつ高品質なデータの豊富さに依存
- データの成長速度が追いつかず、データ枯渇の危機が差し迫っている
- 合成データが有望な解決策として浮上し、データ生成には増強と合成の2つのアプローチがある
- これらの手法の制約と将来の開発・研究の可能性も探る

データをどんどん生成する方法とか、LLMs用のデータが足りなくなるかもって聞いたらワクワクしちゃうね！合成データとかまだまだ進化する分野だし、これからどんな新しい技術が登場するか楽しみだね！ちょっと勉強してみたくなるよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-16 16:12

- - -

### [REFINE on Scarce Data: Retrieval Enhancement through Fine-Tuning via Model Fusion of Embedding Models](http://arxiv.org/abs/2410.12890)

**乏しいデータでのREFINE: 埋め込みモデル融合による微調整を通じた検索向上**

Ambuje Gupta, Mrinal Rawat, Andreas Stolcke, Roberto Pieraccini

- 質問応答タスクで、適切な文書を取得し不正確な文脈でエラーや幻覚が発生
- 新ドメインの適応が難しいため、微調整が解決策となるが必要データが不足
- 提案技術REFINEは合成データ生成とモデル融合で新ドメインの検索性能を向上
- TOURISMデータセットで5.76％改善、SQUADでは6.58％、RAG-12000で0.32％の向上

REFINEって技術、新しい領域でのパフォーマンスをぐっと引き上げてるんだね！データが少ない中での合成データ生成とモデル融合がカギみたい。これは新しい応用が楽しみだね！

**Comment:** Accepted in AJCAI'24

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.IR, **投稿日時:** 2024-10-16 08:43

- - -

### [MIND: Math Informed syNthetic Dialogues for Pretraining LLMs](http://arxiv.org/abs/2410.12881)

**MIND: LLMsの事前学習のための数学に基づいた合成対話**

Syeda Nahida Akter, Shrimai Prabhumoye, John Kamalu, Sanjeev Satheesh, Eric Nyberg, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro

- 合成データは事前学習データの質を向上させ、下流タスクの精度を高めるが、複雑な数学的推論には不十分
- 提案手法MINDはOpenWebMathに基づく数学対話を生成し、数学的推論能力を強化する新しいコーパスを作成
- 対話参加者間の知識ギャップを活用することで、高品質な数学データ生成が可能であると発見
- MIND-OWMで事前学習したモデルは数学的推論を大幅に向上し、専門知識や一般的な推論タスクでも優れた性能を示す

この研究、数学的な推論力が重要な時にすごく役立ちそう！MINDで生成される合成データが、対話的にわかりやすい形で質を上げてくれるなら、勉強ももっと楽しくなりそう！数学に苦手意識があったって、これならいけるかも？って感じ！

**Comment:** 31 pages, 5 figures, 14 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, **投稿日時:** 2024-10-15 18:25
