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

更新: 2024-06-18T04:20:48.005099

- - -

### [Nemotron-4 340B Technical Report](http://arxiv.org/abs/2406.11704)

**Nemotron-4 340B 技術報告書**

Nvidia, :, Bo Adler, Niket Agarwal, Ashwath Aithal, Dong H. Anh, Pallab Bhattacharya, Annika Brundyn, Jared Casper, Bryan Catanzaro, Sharon Clay, Jonathan Cohen, Sirshak Das, Ayush Dattagupta, Olivier Delalleau, Leon Derczynski, Yi Dong, Daniel Egert, Ellie Evans, Aleksander Ficek, Denys Fridman, Shaona Ghosh, Boris Ginsburg, Igor Gitman, Tomasz Grzegorzek, Robert Hero, Jining Huang, Vibhu Jawa, Joseph Jennings, Aastha Jhunjhunwala, John Kamalu, Sadaf Khan, Oleksii Kuchaiev, Patrick LeGresley, Hui Li, Jiwei Liu, Zihan Liu, Eileen Long, Ameya Sunil Mahabaleshwarkar, Somshubra Majumdar, James Maki, Miguel Martinez, Maer Rodrigues de Melo, Ivan Moshkov, Deepak Narayanan, Sean Narenthiran, Jesus Navarro, Phong Nguyen, Osvald Nitski, Vahid Noroozi, Guruprasad Nutheti, Christopher Parisien, Jupinder Parmar, Mostofa Patwary, Krzysztof Pawelec, Wei Ping, Shrimai Prabhumoye, Rajarshi Roy, Trisha Saar, Vasanth Rao Naik Sabavat, Sanjeev Satheesh, Jane Polak Scowcroft, Jason Sewall, Pavel Shamis, Gerald Shen, Mohammad Shoeybi, Dave Sizer, Misha Smelyanskiy, Felipe Soares, Makesh Narsimhan Sreedhar, Dan Su, Sandeep Subramanian, Shengyang Sun, Shubham Toshniwal, Hao Wang, Zhilin Wang, Jiaxuan You, Jiaqi Zeng, Jimmy Zhang, Jing Zhang, Vivienne Zhang, Yian Zhang, Chen Zhu

- Nemotron-4 340Bファミリーがリリースされ、オープンアクセスで提供されている
- モデルは多くの評価ベンチマークで競争力があり、FP8精度で8つのGPU上で動作可能
- モデルの展開および訓練で合成データの有用性を実証、98%以上のデータが合成されている
- 合成データ生成パイプラインもオープンソース化され、研究の促進に貢献することが期待される

最新の技術でより良い合成データを生成できるなんてすごいね！これからのAI研究や商用アプリケーションでどんな応用が進むのか楽しみ～



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-06-17 16:25

- - -

### [Making Old Things New: A Unified Algorithm for Differentially Private Clustering](http://arxiv.org/abs/2406.11649)

**古いものを新しくする：差分プライバシー・クラスタリングのための統一アルゴリズム**

Max Dupré la Tour, Monika Henzinger, David Saulpic

- プライベートクラスタリング問題は様々なプライバシーモデルで広く研究されている
- 20年前のアルゴリズムを少し修正することで、すべてのモデルに対応可能にした
- 既存の多くの結果と一致しつつ、一部の結果を改善し新しいプライバシーモデルにも拡張
- 継続的観察設定という入力が時間と共に変化する新しいプライバシーモデルに対応

20年前のアルゴリズムを使って、最新の問題にも対応できるなんてすごくない？これでプライバシー保護のクラスタリングも、もっと広く使えるようになりそうだね！

**Comment:** Oral presentation at ICML 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, cs.LG, **投稿日時:** 2024-06-17 15:31

- - -

### [Feasibility of Federated Learning from Client Databases with Different Brain Diseases and MRI Modalities](http://arxiv.org/abs/2406.11636)

**クライアントデータベースから異なる脳疾患とMRIモダリティを用いた連合学習の実現可能性**

Felix Wagner, Wentian Xu, Pramit Saha, Ziyun Liang, Daniel Whitehouse, David Menon, Natalie Voets, J. Alison Noble, Konstantinos Kamnitsas

- 特定の脳疾患用のセグメンテーションモデルは固定されたMRIモダリティセットで訓練される
- 連合学習を用いて異なる脳疾患と多様なMRIモダリティで単一モデルの訓練を試みる
- 全てのクライアントデータベースのモダリティをカバーする入力チャンネルやランダムなモダリティドロップの訓練を導入
- 7つの脳MRIデータベースで評価し、新規データベースでも高いセグメンテーション性能を確認

異なる脳疾患やモダリティの組み合わせでも、連合学習が有効なんて面白そう！将来はもっと多くの病気やデータに対応できるモデルが出てきてほしいな。



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, cs.LG, I.4.9; I.4.6; I.2.11; I.4.0, **投稿日時:** 2024-06-17 15:16

- - -

### [Pre-Training and Personalized Fine-Tuning via Over-the-Air Federated Meta-Learning: Convergence-Generalization Trade-Offs](http://arxiv.org/abs/2406.11569)

**空中連合メタ学習による事前トレーニングと個別調整: 収束と一般化のトレードオフ**

Haifeng Wen, Hong Xing, Osvaldo Simeone

- 大規模言語モデルなどのAIアプリでは、事前トレーニング後のファインチューニングが主流
- 連合学習（FL）が進み、事前トレーニングが中央集権型から分散型に移行中
- メタ学習ベースの個別FLは、基本的なパーソナライズを超え、新しいエージェントやタスクへの一般化を目指す
- 無線設定での一般化と収束のトレードオフを分析、チャンネルの欠陥が一般化を助ける一方で収束を悪化させる

無線通信を利用してAIモデルをパーソナライズするなんて、未来を感じるね。新しい技術がどんな風に役立つか楽しみ！

**Comment:** 37 pages, 7 figures, submitted for possible journal publication

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, eess.SP, math.IT, **投稿日時:** 2024-06-17 14:06

- - -

### [Decentralized Credential Verification](http://arxiv.org/abs/2406.11535)

**分散型資格検証**

Patrick Herbke, Anish Sapkota

- ブロックチェーンと検証可能な資格情報を用いた、安全で効率的なデジタル資格管理のdAppを紹介
- OID4VCとSD-JWTに適合したウォレットをサポートし、プライバシー保護に配慮した資格管理が可能
- 主に履歴書の検証を通じて実証され、多様な分野での応用が可能
- 分散識別子と高度な暗号技術を統合し、効率性やコスト、高額詐欺に対する問題を解決

ブロックチェーンで資格情報管理って面白そう！将来、履歴書だけじゃなくて他の証明書とかも全部デジタルで管理できたら便利だよね。

**Comment:** Preprint submitted to the 6th Conference on Blockchain Research &   Applications for Innovative Networks and Services on the 17th of June 2024

**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.CR, cs.NI, **投稿日時:** 2024-06-17 13:37

- - -

### [Private Approximate Query over Horizontal Data Federation](http://arxiv.org/abs/2406.11421)

**水平データ連合におけるプライベート近似クエリ**

Ala Eddine Laouir, Abdessamad Imine

- 複数のデータ提供者がプライベートデータの共同分析を行う課題が存在
- 暗号技術はプライバシーを向上させるが、クエリ応答時間が増加
- 近似クエリ処理と差分プライバシーを組み合わせた新手法を提案
- 計算時間を最大8倍高速化しつつ、学習ベース攻撃への耐性を維持

既存の方法が遅いのを改善できるっぽい！学習攻撃にも強いから安心だね。pliant response time with robust protectionってすごくいいかも☆

**Comment:** To appear in EDBT 2025

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DB, cs.CR, H.2.8, **投稿日時:** 2024-06-17 11:19

- - -

### [Transparency, Privacy, and Fairness in Recommender Systems](http://arxiv.org/abs/2406.11323)

**推薦システムにおける透明性、プライバシー、公正性**

Dominik Kowald

- 推薦システムに心理学的理論を導入し、透明な設計プロセスを実現
- 差分プライバシーを用いて精度とプライバシーのトレードオフを調整し、ユーザー保護を効率化
- セッションベースおよびコールドスタート推薦におけるユーザーの好み情報の不足に対処
- 人気バイアスが推薦の頻度と人気の相関を示し、公正性に影響を与えることを確認

心理学の理論がどんな風に使われるのか気になるね！また、人気バイアスが推薦システムに与える影響がどう解決されるかも注目したいよ～！

**Comment:** Habilitation (post-doctoral thesis) at Graz University of Technology   for the scientific subject Applied Computer Science

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.IR, **投稿日時:** 2024-06-17 08:37

- - -

### [Syn-to-Real Unsupervised Domain Adaptation for Indoor 3D Object Detection](http://arxiv.org/abs/2406.11311)

**屋内3D物体検出のための合成から実世界への未学習ドメイン適応**

Yunsong Wang, Na Zhao, Gim Hee Lee

- 合成データの活用で3Dアノテーション作業を大幅に削減し、ゼロショット検出器の訓練が可能
- ドメインシフトに対応するため、オブジェクト認識に基づく階層的なドメインアライメント（OHDA）を提案
- 敵対的訓練および擬似ラベリングを用いた二枝アダプテーションフレームワーク
- 実世界データセットに対して最大9.7％のmAP25改善を達成し、従来手法を上回る

この技術なら、面倒なデータ準備の手間も解消されるし、精度もめっちゃ上がりそう！すごいね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-17 08:18

- - -

### [Federated Active Learning Framework for Efficient Annotation Strategy in Skin-lesion Classification](http://arxiv.org/abs/2406.11310)

**皮膚病変分類における効率的なアノテーション戦略のための連合能動学習フレームワーク**

Zhipeng Deng, Yuqiao Yang, Kenji Suzuki

- 連合学習（FL）は複数の機関がプライベートデータを共有せずにモデルを共同で訓練できる
- 医療シナリオではデータのアノテーションに専門知識と労働力が必要であり、FLにおいて重大な問題
- 提案する連合能動学習（FedAL）フレームワークは、FLの下で定期的かつ対話的にALを実行する
- 実データセットで検証し、50%のサンプルで最先端の性能を達成、他のAL手法より優れた結果を示す

連合能動学習がどんな未来を切り開くのか気になる！これで医療データの負担が減れば、多くの人が救われそうだよね。

**Comment:** 14 pages, 3 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-06-17 08:16

- - -

### [Enhancing Generalizability of Representation Learning for Data-Efficient 3D Scene Understanding](http://arxiv.org/abs/2406.11283)

**データ効率の高い3Dシーン理解のための表現学習の一般化性の向上**

Yunsong Wang, Na Zhao, Gim Hee Lee

- 自己教師型3D表現学習は、豊富なアノテーション付きデータセットの不足という課題を緩和する解決策として浮上
- 多様で大規模なリアルワールド3Dシーンのデータセットが不足している問題が依然として存在
- 多様なシンセティックシーンを生成するための生成的ベイジアンネットワーク(GRL)を提案し、合目的な事前学習を実施
- 事前学習した知識を用いて、3D物体検出と3Dセマンティックセグメンテーションの2つの主要なダウンストリームタスクに適用可能

GRLはすごいかも！リアルなデータセットが無くても、これならもっと効率的に3Dシーン理解ができるようになるかもって思ったよ。技術の進歩が楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-17 07:43

- - -

### [Retraining with Predicted Hard Labels Provably Increases Model Accuracy](http://arxiv.org/abs/2406.11206)

**予測されたハードラベルによる再訓練はモデル精度を証明的に向上させる**

Rudrajit Das, Inderjit S. Dhillon, Alessandro Epasto, Adel Javanmard, Jieming Mao, Vahab Mirrokni, Sujay Sanghavi, Peilin Zhong

- ノイズの多いラベルで訓練したモデルの性能は、自身の予測ハードラベルで再訓練することで向上する
- 本研究では、ランダムに破損したラベルを用いた線形分離設定での再訓練を理論的に分析
- 最初のノイズラベルで得た精度を再訓練で向上できることを証明した初の理論的結果
- ラベル差分プライバシー(DP)訓練において、予測ラベルと与えられたラベルが一致するサンプルの再訓練が有効

この研究、本当面白そう！予測ラベルと与えられたラベルに基づく再訓練でプライバシーを損ねずに精度が向上するだなんて、未来に向けてもっと探求したくなるね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-06-17 04:53

- - -

### [Save It All: Enabling Full Parameter Tuning for Federated Large Language Models via Cycle Black Gradient Descent](http://arxiv.org/abs/2406.11187)

**すべてを保存：Cycle Black Gradient Descentによる連合大規模言語モデルの完全なパラメータチューニングの実現**

Lin Wang, Zhichao Wang, Xiaoying Tang

- 大規模言語モデル（LLMs）の登場により、深層学習のパラダイムが革命的に変わった
- 連合学習（FL）では、LLMsの事前学習やファインチューニングが計算資源やメモリ消費、通信ボトルネックに直面する
- 提案手法FedCyBGDは、Cycle Block Gradient Descentを用いて周期的にモデルを更新し、通信や計算、メモリコストを削減する
- FedCyBGDは選択されたブロックの更新とアップロードだけで完全なパラメータ学習を可能にし、FL LLMトレーニングで最先端の性能を実現

この方法を使えば、みんなのパソコンの負担が軽くなるってことかな？本当に実用化されたら影響大きそうでワクワクするね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-17 03:49

- - -

### [Federated Face Forgery Detection Learning with Personalized Representation](http://arxiv.org/abs/2406.11145)

**個別化表現による連合型顔偽造検出学習**

Decheng Liu, Zhan Dang, Chunlei Peng, Nannan Wang, Ruimin Hu, Xinbo Gao

- 深層生成技術は高品質な偽動画を作成でき、深刻な社会的脅威である
- 連合学習戦略により、データのプライバシーを保護しつつモデルパラメータを集約
- クライアントごとの個別化表現学習で、検出性能を向上
- 公開顔偽造検出データセットの実験で、最先端手法と比べて優れた性能を示した

個別化表現で性能向上とか新しい感じでワクワクする！実用化が進んだら、偽動画の脅威も怖くなくなるかもね。楽しみ〜。

**Comment:** The code is publicly available

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-17 02:20

- - -

### [Scorecards for Synthetic Medical Data Evaluation and Reporting](http://arxiv.org/abs/2406.11143)

**合成医療データ評価および報告のためのスコアカード**

Ghada Zamzmi, Adarsh Subbaswamy, Elena Sizikova, Edward Margerrison, Jana Delfino, Aldo Badano

- 合成医療データ（SMD）の利用が増加しているが、その品質評価のための体系的な枠組みが求められている
- 現在、SMDの評価方法が標準化されておらず、特に様々な医療シナリオでの適用性についての評価が課題である
- 本研究は、医療アプリケーションの特有の要件を満たす評価枠組みを提案し、SMDスコアカードの概念を紹介
- スコアカードは、人工的に生成されたデータセットに付随する包括的な報告書として機能し、SMDの品質向上を促進する

合成データってすごく期待されている分野なんだね！スコアカードの概念が入ることで、医療でもっと安心してAIを使えるようになるといいよね！

**Comment:** 7 pages, 2 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CY, cs.DB, **投稿日時:** 2024-06-17 02:11

- - -

### [Text Grafting: Near-Distribution Weak Supervision for Minority Classes in Text Classification](http://arxiv.org/abs/2406.11115)

**テキストグラフティング: テキスト分類の少数派クラスに対する近似分布弱教師あり学習**

Letian Peng, Yi Gu, Chengyu Dong, Zihan Wang, Jingbo Shang

- 従来の方法は生コーパスからクラス名に似たテキストを採掘し、少数派クラスにはほとんどサンプルがない可能性がある
- 最近の研究はクラス名や定義を用いてLLMにプロンプトを与え関連テキストを生成するが、分布内データが生成されないリスクが高い
- 本論文では、この2つのアプローチの利点を組み合わせ、少数派クラスに対してきれいで近似分布の弱教師あり学習を得る新しいフレームワーク「テキストグラフティング」を提案
- LLMベースのロジットを使用し、生コーパスからマスクされたテンプレートを採掘し、これを最先端のLLMで満たして少数派クラスに分布するテキストを合成することで、少数派クラスの分類性能が大幅に向上

新しい手法で少数派クラスのテキストを上手く生成できるなんて、おもしろそう！こういう方法だと、少数派データもちゃんと扱える未来が期待できるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-17 00:23

- - -

### [An Analysis on Quantizing Diffusion Transformers](http://arxiv.org/abs/2406.11100)

**拡散変換器の量子化に関する分析**

Yuewei Yang, Jialiang Wang, Xiaoliang Dai, Peizhao Zhang, Hongbo Zhang

- 拡散モデル(DMs)は反復的なノイズ除去プロセスでランダムノイズを合成データに変換する
- UNet構造から始まったが、その後のトランスフォーマーのみの構造で性能が向上
- 潜在拡散モデル(LDMs)は計算要件を軽減するが、パラメータ量と特徴量サイズの多さで推論が高コスト
- 本研究は最適化なしで効率的なトランスフォーマーのPTQを実現し、条件付き画像生成での効率性と有効性を実証

トランスフォーマー構造の最適化なし量子化って、おもしろいよね！今後の画像生成技術の可能性が広がりそう。

**Comment:** CVPR T4V workshop

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-16 23:18

- - -

### [MemDPT: Differential Privacy for Memory Efficient Language Models](http://arxiv.org/abs/2406.11087)

**MemDPT: メモリ効率型言語モデルのための差分プライバシー**

Yanming Liu, Xinyue Peng, Jiannan Cao, Yuwei Zhang, Chen Ma, Songhang Deng, Mengchen Fu, Xuhong Zhang, Sheng Cheng, Xun Wang, Jianwei Yin, Tianyu Du

- 大規模言語モデルは優れた性能を発揮するが、ユーザープライバシーのリスクがある
- トレーニング時のメモリ消費が大きく、資源消耗の課題がある
- 提案するMemDPTはメモリコストを2~3倍最適化し、データプライバシーを強化
- MemDPTはさまざまなタスクシナリオで差分プライバシー効率のファインチューニングを実現

MemDPTって、メモリも節約しながらプライバシーも守るなんて最強じゃない？色んな応用ができそうでめちゃくちゃワクワクするね！

**Comment:** 12 pages first version

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.CL, cs.LG, **投稿日時:** 2024-06-16 22:11

- - -

### [Leveraging Foundation Models for Multi-modal Federated Learning with Incomplete Modality](http://arxiv.org/abs/2406.11048)

**基礎モデルを活用した不完全モダリティによるマルチモーダル連合学習**

Liwei Che, Jiaqi Wang, Xinyue Liu, Fenglong Ma

- 連合学習は分散データ環境での共同訓練をプライバシー保証と共に実現
- クライアントが複数のデータモダリティを保有する現実的なシナリオに注目
- モダリティ欠損問題を解決するためFedMVPを提案し、事前訓練モデルを利用
- モデルは現実世界の画像とテキスト分類データセットで優れた性能を示す

異なるモダリティ間でも連合学習を効率的に行えるってすごい！これが実用化されたら、もっと複雑なデータもプライバシーを守りながら分析できるようになるかもね。

**Comment:** Accepted by ECML-PKDD 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-16 19:18

- - -

### [Physics-Informed Deep Learning and Partial Transfer Learning for Bearing Fault Diagnosis in the Presence of Highly Missing Data](http://arxiv.org/abs/2406.11023)

**物理に基づく深層学習と部分的転移学習によるベアリング故障診断における高度な欠損データへの対応**

Mohammadreza Kavianpour, Parisa Kavianpour, Amin Ramezani

- ラベル付きデータの欠如がベアリング故障診断の主要な障害となっている
- 深層学習に基づく技術で合成ラベル付きデータを生成するPTPAI法を提案
- RF-Mixupアプローチを用い、クラスの不均衡問題を解消
- ドメイン適応戦略にMK-MMSDとCDANを採用し、合成データと実データの分布の違いを緩和

物理に基づく深層学習なんて、かっこいいね！高度な欠損データでもうまくいくみたいだし、実用性が高そう。



**トピック:** [合成データ](sd), **カテゴリ:** eess.SP, cs.AI, cs.LG, cs.SY, eess.SY, **投稿日時:** 2024-06-16 17:36

- - -

### [Promoting Data and Model Privacy in Federated Learning through Quantized LoRA](http://arxiv.org/abs/2406.10976)

**量子化されたLoRAによる連合学習におけるデータおよびモデルプライバシーの促進**

JianHao Zhu, Changze Lv, Xiaohua Wang, Muling Wu, Wenhao Liu, Tianlong Li, Zixuan Ling, Cenyuan Zhang, Xiaoqing Zheng, Xuanjing Huang

- 通常の連合学習は異なるエッジデバイス間でデータのプライバシーを保護
- 大規模言語モデル（LLMs）の開発には多くのデータと計算リソースが必要で、それは知的財産である
- 量子化されたモデルパラメータを分配することで、データとモデルの両方のプライバシーを保護
- LoRAを使った量子化戦略により通信コストを大幅に削減し、リソース効率の良い学習を実現

この方法で通信コストを削減しながら、データとモデルのプライバシーも守れるなんてすごいよね！未来の連合学習がもっと使いやすくなりそう、楽しみだな～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CL, cs.CR, **投稿日時:** 2024-06-16 15:23

- - -

### [Linkage on Security, Privacy and Fairness in Federated Learning: New Balances and New Perspectives](http://arxiv.org/abs/2406.10884)

**連合学習におけるセキュリティ、プライバシー、公平性の結びつき：新たなバランスと新しい視点**

Linlin Wang, Tianqing Zhu, Wanlei Zhou, Philip S. Yu

- モバイルデバイスや銀行システム、ヘルスケア、IoTシステムで連合学習が急速に普及中
- この研究では、プライバシー漏洩、セキュリティ脅威、公平性の相互関係を詳述
- 公平性とプライバシー、セキュリティと勾配共有のトレードオフを指摘
- 公平性がプライバシーとセキュリティ間の橋渡しとして機能し得る

プライバシーと公平性のバランスなんて難しそうだけど、めっちゃおもしろいね！未来の連合学習モデルがどんどん進化して、安全かつ公平になるといいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-06-16 10:31

- - -

### [Knowledge Distillation in Federated Learning: a Survey on Long Lasting Challenges and New Solutions](http://arxiv.org/abs/2406.10861)

**連合学習における知識蒸留：長年の課題と新たな解決策に関する調査**

Laiqiao Qin, Tianqing Zhu, Wanlei Zhou, Philip S. Yu

- 連合学習はデータをローカライズしたまま複数のクライアントがモデルを訓練する分散型プライバシー保護機械学習である
- 課題にはプライバシーリスク、データ異質性、通信のボトルネック、およびシステムの異質性が含まれる
- 知識蒸留はモデル圧縮および強化アルゴリズムとして2020年以降広く適用されている
- 知識蒸留の連合学習における適用例を包括的に調査し解決策を提示

知識蒸留が連合学習の課題をどう克服できるかを明らかにするなんて面白そう！未来の研究方向も示して、これからの進展が楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-16 09:12

- - -

### [Federated Learning Optimization: A Comparative Study of Data and Model Exchange Strategies in Dynamic Networks](http://arxiv.org/abs/2406.10798)

**連合学習最適化：動的ネットワークにおけるデータとモデル交換戦略の比較研究**

Alka Luqman, Yeow Wei Liang Brandon, Anupam Chattopadhyay

- 大規模な動的連合学習において、データとモデルのどちらを共有するべきかが重要な課題
- デバイス間での生データ、合成データ、（部分）モデル更新の交換を比較
- 基礎モデルの文脈でこれらの交換戦略の影響を詳細に調査
- 時間制限のある知識移転効率が最大で9.08%異なることが判明

効率的なデータとモデル交換ってどれがいいんだろうね？この研究で明らかになった9.08%の違い、実用的にどのくらい役立つのか気になるな～



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-16 03:46

- - -

### [GenMM: Geometrically and Temporally Consistent Multimodal Data Generation for Video and LiDAR](http://arxiv.org/abs/2406.10722)

**GenMM：ビデオおよびLiDARのための幾何学的および時間的一貫性を持つマルチモーダルデータ生成**

Bharat Singh, Viveka Kulharia, Luyu Yang, Avinash Ravichandran, Ambrish Tyagi, Ashish Shrivastava

- 自律走行やロボティクスなどで重要なマルチモーダル合成データ生成技術を提案
- RGBビデオとLiDARスキャンを一体的に編集し、時間的・幾何学的一貫性を持つ3Dオブジェクトを挿入
- 2D領域を一貫させるために、拡散ベースのビデオインペインティングモデルを使用
- 新しいオブジェクトの3D形状を最適化し、LiDAR深度データも更新して一致させる

リアルな3Dオブジェクトの挿入でマルチモーダルデータ作成がもっと簡単になりそうだね。これが実用化されたら、いろんな分野で革新的なデータ収集ができちゃうかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-06-15 19:29

- - -

### [RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics](http://arxiv.org/abs/2406.10721)

**RoboPoint: ロボティクスにおける空間的アフォーダンス予測のための視覚言語モデル**

Wentao Yuan, Jiafei Duan, Valts Blukis, Wilbert Pumacay, Ranjay Krishna, Adithyavairavan Murali, Arsalan Mousavian, Dieter Fox

- ロボットはテーブル上の物体との再配置や棚への食料品の配置など、正確な行動ポイントを計画する必要がある
- 自動合成データ生成パイプラインを導入し、VLMをロボットの分野とニーズに合わせて指示調整
- 提案手法は現実世界のデータ収集や人間のデモンストレーションを必要とせず、多様な環境や視点にスケーラブル
- RoboPointはロボットナビゲーション、マニピュレーション、AR支援などの下流アプリケーションに対応し、最先端のVLMより21.8%、下流タスクでは30.5%の精度向上を達成

ロボットの操作がここまで進化すると、日常生活がもっと楽しく便利になりそうだね！未来がすぐそこに来てる感じでわくわくする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.AI, cs.CV, **投稿日時:** 2024-06-15 19:22

- - -

### [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](http://arxiv.org/abs/2406.10630)

**連合指示調整における大規模言語モデルの新たな安全攻撃と防御**

Rui Ye, Jingyi Chai, Xiangrui Liu, Yaodong Yang, Yanfeng Wang, Siheng Chen

- 連合学習（FL）は、複数の当事者がデータを共有せずに協力して大規模言語モデル（LLM）を微調整できる
- この研究では、FedITの安全調整の脆弱性を暴露し、シンプルだが効果的な攻撃手法を提案
- 悪意のあるクライアントは自動生成された攻撃データを使い、FedITシステムの安全性を損なう
- 提案された防御法により、多くの既存のFL防御法が効果的でない中で、攻撃されたLLMの安全性を大幅に向上

安全性の調整がこんなに簡単に損なわれるのって怖いね。でも、新しい防御法がちゃんと対策できるなら、もっと安心して使えそう。楽しみだな。

**Comment:** 18 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.AI, cs.CR, cs.MA, **投稿日時:** 2024-06-15 13:24

- - -

### [Privacy-Preserving Heterogeneous Federated Learning for Sensitive Healthcare Data](http://arxiv.org/abs/2406.10563)

**センシティブな医療データに対するプライバシー保護を図る異なる連合学習**

Yukai Xu, Jingfeng Zhang, Yujie Gu

- 医療データの集中化によるプライバシー漏洩の課題
- 知的財産保護のため、異なるローカルモデルの機密性を保ちながら共同訓練が必要
- 新たなAAFVフレームワークを提案。差分プライバシー機構と棄権認識投票を組み合わせる
- 糖尿病と院内患者死亡率の予測において有効性と機密性を実証

新しい仕組みでデータのプライバシーを守りつつ、正確な医療予測ができるなんてすごいよね。これからモデル同士も秘密を守りながら仲良く協力する時代になるのかも！

**Comment:** Accepted to the 2024 IEEE Conference on Artificial Intelligence (IEEE   CAI 2024)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-06-15 08:43

- - -

### [MALLM-GAN: Multi-Agent Large Language Model as Generative Adversarial Network for Synthesizing Tabular Data](http://arxiv.org/abs/2406.10521)

**多エージェント大規模言語モデルを生成的敵対ネットワークとして利用した表データの生成**

Yaobin Ling, Xiaoqian Jiang, Yejin Kim

- データ不足問題解決のため、合成表データ生成法を提案
- 大規模言語モデル（LLM）を生成的敵対ネットワーク（GAN）として使用
- 小規模データサンプルでも高品質な合成データ生成が可能
- 実験結果は、既存モデルよりも高品質な合成データ生成とプライバシー保護を実証

大規模言語モデルをこんなふうに使うなんてさすが～。少ないデータでも高品質なシミュレーションができるって、たくさんの分野で応用できそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-15 06:26

- - -

### [A Label is Worth a Thousand Images in Dataset Distillation](http://arxiv.org/abs/2406.10485)

**データセット蒸留におけるラベルの価値は千の画像に匹敵する**

Tian Qin, Zhiwei Deng, David Alvarez-Melis

- データの質が機械学習モデルの性能に重要であり、データセット蒸留法はこれを小規模なデータセットに圧縮して活用
- 蒸留法は複雑で多様な合成データ生成手法を用いるが、共通点としてソフトラベルを使用
- ソフトラベルの役割を深く研究し、具体的な手法ではなくソフトラベルの使用が性能を決定する主因と判明
- ソフトラベルには構造化情報が必要であり、イメージ数ごとの効果やデータ効率のパレートフロンティアも提示

この研究、めっちゃ興味深い！ソフトラベルが鍵みたいだから、新しい蒸留法もいろいろ考えられそうだね。未来の機械学習がもっと効率的になりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-06-15 03:30

- - -

### [Federated Neural Radiance Field for Distributed Intelligence](http://arxiv.org/abs/2406.10474)

**分散インテリジェンスのための連合ニューラルラジアンスフィールド**

Yintian Zhang, Ziyu Shao

- ARやVR応用における新規視点合成（NVS）の重要性
- Neural Radiance Field（NeRF）のNVSタスクでの性能優位性
- データプライバシーを保持しつつ異なるデータ所有者の画像を活用するFedNeRF
- 機能的多様でリソース豊富な連合学習テストベッドの構築とFedNeRFアルゴリズムの実験

FedNeRFってめっちゃおもしろそう！これで、異なる場所にあるデータでも効率的に活用できちゃうんだって。新しいAR/VR体験がさらに進化するかもね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-06-15 02:32

- - -

### [Byzantine-Robust Decentralized Federated Learning](http://arxiv.org/abs/2406.10416)

**ビザンチン耐性分散型連合学習**

Minghong Fang, Zifan Zhang, Hairi, Prashant Khanduri, Jia Liu, Songtao Lu, Yuchen Liu, Neil Gong

- 連合学習（FL）は、複数のクライアントがプライベートな訓練データを公開せずに協力して機械学習モデルを訓練する技術である
- 従来の連合学習は中央サーバーを介して調整されるが、スケーラビリティと信頼依存性の問題がある
- 分散型連合学習（DFL）はサーバーレスかつピアツーピア方式でモデルを共同訓練するが、完全に分散型であるため攻撃に弱い
- 新アルゴリズム「BALANCE」は、クライアントがローカルモデルを基準に受信モデルが悪意かどうかを判断し、防御力と収束保証を提供する

これは革新的だね！完全ピアツーピアでの連合学習、未来のAIインフラに道を開く革新かも！

**Comment:** To appear in ACM Conference on Computer and Communications Security   2024 (CCS '24)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, cs.LG, **投稿日時:** 2024-06-14 21:28

- - -

### [L4GM: Large 4D Gaussian Reconstruction Model](http://arxiv.org/abs/2406.10324)

**L4GM: 大規模4Dガウス再構成モデル**

Jiawei Ren, Kevin Xie, Ashkan Mirzaei, Hanxue Liang, Xiaohui Zeng, Karsten Kreis, Ziwei Liu, Antonio Torralba, Sanja Fidler, Seung Wook Kim, Huan Ling

- L4GMは単一視点の動画入力からアニメーションオブジェクトを生成する最初の4D再構成モデル
- 44K種類のオブジェクトと110Kのレンダリングされたアニメーションを含むマルチビュー動画データセットを使用
- L4GMは低フレームレートの動画フレームから3Dガウススプラッティング表現を生成し、アップサンプリングして時間的な滑らかさを実現
- 合成データのみで学習したL4GMは、実環境の動画でも高品質なアニメーション3Dアセットを生成

未来の動画制作がどんどん簡単になりそうでワクワクするね！ゲームとか映画の制作にも役立ちそうじゃない？

**Comment:** Project page: https://research.nvidia.com/labs/toronto-ai/l4gm

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-06-14 17:51
