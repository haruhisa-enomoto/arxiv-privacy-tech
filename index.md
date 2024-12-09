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

更新: 2024-12-11T04:23:20.485304

- - -

### [FedSynthCT-Brain: A Federated Learning Framework for Multi-Institutional Brain MRI-to-CT Synthesis](http://arxiv.org/abs/2412.06690)

**FedSynthCT-Brain: 複数機関の脳MRIからCT合成のための連合学習フレームワーク**

Ciro Benito Raggio, Mathias Krohmer Zabaleta, Nils Skupien, Oliver Blanck, Francesco Cicone, Giuseppe Lucio Cascini, Paolo Zaffino, Lucia Migliorelli, Maria Francesca Spadea

- 合成CT画像は放射線治療プランニングで重要で、MRIガイドの治療を推進
- マルチセンターでのデータ集約はプライバシーの懸念を生じさせる
- FedSynthCT-Brainは連合学習を利用し、脳画像でMRIからsCTを生成する
- テストでは未見データで良好な画像品質指標が得られ、データプライバシーを保った一般化が可能と示した

これって、いろんな国の病院が協力してやってるんだね。プライバシーも守れるし、未来の医療が安心して受けられそうで、めっちゃ安心感♪



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-12-09 17:32

- - -

### [Numerical Estimation of Spatial Distributions under Differential Privacy](http://arxiv.org/abs/2412.06541)

**差分プライバシーを用いた空間分布の数値推定**

Leilei Du, Peng Cheng, Libin Zheng, Xiang Lian, Lei Chen, Wei Xi, Wangze Ni

- 空間分布の推定は交通予測や疫病予防に重要だが、ユーザーデータ収集はプライバシーを侵害する恐れがある
- 既存の一部の手法は一次元データに依存し、空間データの関連性を考慮せず誤差が大きい
- 提案されたDisk Area Mechanism (DAM)は空間データを一次元に射影し推定精度を向上させる
- DAMは最新手法と比べて一貫して優れた成果を見せ、データの細かさに依存せずに優位性を示す

空間データをうまく一元化して扱うアイデアが新鮮だし、実験結果が他の手法よりいいっていうのはすごいよね！これならプライバシーを守りながらも正確な予測できちゃうかもってワクワクしちゃう！

**Comment:** ICDE 2025

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.DB, **投稿日時:** 2024-12-09 14:53

- - -

### [A cautionary tale on the cost-effectiveness of collaborative AI in real-world medical applications](http://arxiv.org/abs/2412.06494)

**実世界の医療アプリケーションにおける協調型AIの費用対効果に関する警告的物語**

Francesco Cremonesi, Lucia Innocenti, Sebastien Ourselin, Vicky Goh, Michela Antonelli, Marco Lorenzi

- 連合学習は医療で人気だが、実装には通信インフラの課題がある
- コンセンサスベースの学習（CBL）は、効率を高める連携学習の選択肢
- CBLは連合学習と同等の精度を持ち、訓練時間と通信コストを大幅に削減
- コスト効果の高い方法を採用することでAIの持続性と普及の可能性が開く

協調型AIってすごく将来性があるね！通信コストを60倍も減らせるのは、ほんとに驚き！みんなの健康にもっと身近に役立てる日が来るかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-09 13:50

- - -

### [Improving text-conditioned latent diffusion for cancer pathology](http://arxiv.org/abs/2412.06487)

**がん病理学のためのテキスト条件付き潜在拡散の改善**

Aakash Madhav Rao, Debayan Gupta

- 合成データ生成はがん組織病理で未開発な領域
- 拡散アルゴリズムはリアルな画像生成が可能だが計算量が多い
- VAEを使うと高解像度画像の圧縮と回復が可能
- 提案手法でFIDスコア21.11を達成し、GPUメモリ使用量を7%削減

人工知能の助けでがん病理の画像がリアルに作れるなんてすごいね！これからどんどん医療に役立ちそうでワクワクするなぁ。もっと効率的な方法が生まれたら、病気の早期発見にも繋がるかもしれないよね。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, cs.LG, **投稿日時:** 2024-12-09 13:38

- - -

### [Federated Split Learning with Model Pruning and Gradient Quantization in Wireless Networks](http://arxiv.org/abs/2412.06414)

**モデル剪定と勾配量子化を用いたワイヤレスネットワークにおける連合分割学習**

Junhe Zhang, Wanli Ni, Dongyu Wang

- 連合学習ではエッジデバイスのリソースがボトルネックになる問題がある
- 連合分割学習(FedSL)はモデルを分割し、エッジデバイスとサーバーで協力してトレーニング
- 提案手法はモデル剪定と勾配量子化で計算負荷を軽減し、ランダムドロップアウトで通信負担を削減
- 理論解析とシミュレーションで提案手法の効率性と優位性を検証

エッジデバイスでモデルを軽くして効率的に学習できるんだね。無線ネットワークでの通信負担も減らせるのはすごい！テクノロジーが進化してもっと便利になりそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.NI, **投稿日時:** 2024-12-09 11:43

- - -

### [Exploring the Impact of Synthetic Data on Human Gesture Recognition Tasks Using GANs](http://arxiv.org/abs/2412.06389)

**合成データが人間のジェスチャー認識タスクに与える影響の探求**

George Kontogiannis, Pantelis Tzamalis, Sotiris Nikoletseas

- IoTデバイスを用いた人間活動認識において、データ不足と品質向上のため、深層生成モデルが注目
- 特にGANはリアルな世界を模倣した合成データ生成に優れている
- アレルギー関連のジェスチャー認識向けに、2つのGANを用いた合成データの性能を評価
- スマートウェアラブルデバイスから得たデータが、本研究で初めてアレルギー性鼻炎のジェスチャー認識に応用

合成データを使ってジェスチャー認識を進化させるなんて、近未来感あるよね！ウェアラブルデバイスで健康管理もどんどん進化しそうだね。

**Comment:** 8 pages, 5 figures, 20th International Conference on Distributed   Computing in Smart Systems and the Internet of Things (DCOSS-IoT), 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-09 11:15

- - -

### [H-FedSN: Personalized Sparse Networks for Efficient and Accurate Hierarchical Federated Learning for IoT Applications](http://arxiv.org/abs/2412.06210)

**H-FedSN: IoTアプリケーションのための効率的で正確な階層型連合学習を実現するパーソナライズされたスパースネットワーク**

Jiechao Gao, Yuangang Li, Yue Zhao, Brad Campbell

- IoTの普及が連合学習への関心を高める一方、従来の二層構造ではマルチティアIoT環境にうまく適応できない。
- H-FedSNはバイナリマスクメカニズムと共有・個別層を組み合わせ、通信の効率化と精度向上を図る。
- 個別層とベイズ集約を通じてデバイス間のデータの不均衡に対応し、多様なクライアントグループ間の貢献を調整。
- 評価結果では、ヒエラルFAVGと比較して通信費用を58から238倍削減し、高精度を維持することが示される。

マルチティアなIoT環境でより効率的に学習するための新しいアプローチが提案されてて面白そう！デバイス間の多様性にも対応できるなんて、実用性がすごく高まりそうだね。H-FedSNの実験結果は、リアルなデータセットでいい成果が出ているから、これからのIoT時代にますます期待できる技術かも。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-09 05:05

- - -

### [BECS: A Privacy-Preserving Computing Sharing Mechanism in 6G Computing Power Network](http://arxiv.org/abs/2412.06196)

**BECS: 6G計算力ネットワークにおけるプライバシー保護計算共有メカニズム**

Kun Yan, Wenping Ma, Shaohui Sun

- 6GネットワークはAI主導で、新しいインテリジェンスを提供
- BECSは進化的アルゴリズムとブロックチェーンでタスクオフロードを最適化
- 多目的最適化問題としてモデル化し、計算資源の利用効率向上を目指す
- ゼロ知識証明に基づく擬名スキームがユーザープライバシーを保護

6Gネットワークでの計算力をもっと効率的に使うための工夫が満載で面白そう！進化的アルゴリズムがどんなふうに効くのかも気になるなあ。さらにはプライバシー保護もしっかりしてるのが嬉しいポイントだね。

**Comment:** This manuscript has been submitted to the IEEE Transactions on   Wireless Communications for possible publication

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.NI, C.2.1; C.2.4, **投稿日時:** 2024-12-09 04:26

- - -

### [Membership Inference Attacks and Defenses in Federated Learning: A Survey](http://arxiv.org/abs/2412.06157)

**連合学習におけるメンバーシップ推論攻撃と防御: サーベイ**

Li Bai, Haibo Hu, Qingqing Ye, Haoyang Li, Leixia Wang, Jianliang Xu

- 連合学習は、低リソースデバイスが協力して高品質モデルを構築可能
- だが、メンバーシップ推論攻撃によりクライアントのプライバシーが脅かされる
- メンバーシップ推論攻撃と防御策を分類し、包括的にまとめた研究が不足
- 攻撃の分類法を紹介し、対策の強みと弱みを徹底分析

この論文、めっちゃ面白そう！連合学習の進化で医療とかにも使えるようになるかもね。未来のプライバシー技術がどこまで進むのか楽しみだよ！

**Comment:** To be published in ACM Computing Surveys

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-09 02:39

- - -

### [AIDE: Task-Specific Fine Tuning with Attribute Guided Multi-Hop Data Expansion](http://arxiv.org/abs/2412.06136)

**タスク固有のファインチューニングを属性ガイドのマルチホップデータ拡張で行うAIDE**

Jiayu Li, Xuan Zhu, Fang Liu, Yanjun Qi

- LLMのファインチューニングには高品質かつ多様なデータが必要
- AIDEは、10個の少数のシードデータから多様で関連性のあるデータを生成
- シードデータからトピックと属性を抽出し、マルチホッププロセスでデータを展開
- AIDEはベースモデルよりも13タスクで10%以上の精度向上を達成

AIDEのアプローチは少ないデータから多様なデータを生成できるのが魅力的！多くのタスクで精度アップだなんて、とっても強力な技術みたい。新しい方法でさらにLLMの可能性を広げられそうだね。

**Comment:** 19 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-09 01:39

- - -

### [Lightweight Federated Learning with Differential Privacy and Straggler Resilience](http://arxiv.org/abs/2412.06120)

**差分プライバシーと遅延耐性を備えた軽量な連合学習**

Shu Hong, Xiaojun Lin, Lingjie Duan

- 連合学習でモデルパラメータ交換による推論攻撃を差分プライバシーで防ぐ。
- 差分プライバシーと秘密計算の組み合わせは精度を上げるが、通信負荷が高い。
- 提案手法LightDP-FLは、低遅延、多数の騒音変異を利用してプライバシーを実現。
- CIFAR-10を用いた実験で、提案手法はより速い収束と優れた遅延耐性を示す。

これってめっちゃ便利そう！新しい手法で効率的にプライバシーを守りつつ、速く学習できるなんてすごいよね。これからのデータ時代にピッタリかも！

**Comment:** To appear at IEEE International Conference on Computer Communications   (INFOCOM) 2025

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-12-09 00:54

- - -

### [Privacy-Preserving Large Language Models: Mechanisms, Applications, and Future Directions](http://arxiv.org/abs/2412.06113)

**プライバシー保護型大規模言語モデル: メカニズム、応用、将来の方向性**

Guoshenghui Zhao, Eric Song

- 大規模言語モデルは様々な分野で活用される一方、データ漏洩などのプライバシー問題が懸念されている
- 差分プライバシーや連合学習などを用いたプライバシー保護メカニズムを検討し、プライバシー問題解決の効果を分析
- プライバシー重視分野での応用例と限界を紹介し、プライバシーとモデルの有用性のバランスを考慮
- 大規模言語モデルのライフサイクルにプライバシーを組み込むための新しいフレームワークの必要性を指摘

プライバシーと性能の両立ってホントに難しいよね。でも、この研究はそのバランスを上手く取りつつ、これからの方向性も示してて期待大！プライバシーの未来は明るいかもね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), [TEE](tee), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-12-09 00:24

- - -

### [Accelerating Video Diffusion Models via Distribution Matching](http://arxiv.org/abs/2412.05899)

**ビデオ拡散モデルを分布マッチングで加速化する方法**

Yuanzhi Zhu, Hanshu Yan, Huan Yang, Kai Zhang, Junnan Li

- 拡散モデルはデータ合成に成功したが、計算負荷が高く動画生成に課題がある
- 新たな拡散蒸留と分布マッチングの枠組みで推論ステップを大幅に削減
- 提案手法は、2Dスコア分布マッチング損失とGAN損失を組み合わせ高品質動画生成を可能にする
- AnimateDiffを利用し、4ステップで優れた性能を実現したことを実験で示した

動画の生成をこれまでよりずっと効率的にする技術で、実際の映像制作用途に期待！色々なデータ合成の可能性が広がっていくね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-08 11:36

- - -

### [FedRBE -- a decentralized privacy-preserving federated batch effect correction tool for omics data based on limma](http://arxiv.org/abs/2412.05894)

**FedRBE -- オミクスデータの分散プライバシー保護フ​​ェデレーテッドバッチ効果補正ツール（limmaベース）**

Yuliya Burankova, Julian Klemm, Jens J. G. Lohmann, Ahmad Taheri, Niklas Probul, Jan Baumbach, Olga Zolotareva

- オミクスデータのバッチ効果が生物学的信号を隠し、プライバシー保護分析の課題となる
- 従来の補正方法はデータ集中が必要でプライバシーに問題がある
- fedRBEは分散型で欠損値を扱える自動化されたユーザーインターフェースを提供
- 秘密計算を活用し、集中型と同等の性能を持ちデータ共有なしで協調的な補正を実現

この研究、すごいね！データを共有しなくても協力できるなんて、将来的にはさまざまな分野で応用が進みそう。特に大規模なオミクス研究にはぴったりだね！

**Comment:** The first two authors listed are joint first authors. The last two   authors listed are joint last authors. 21 pages, 5 figures, 5 tables

**トピック:** [連合学習](fl), **カテゴリ:** q-bio.QM, cs.CR, cs.DC, cs.LG, **投稿日時:** 2024-12-08 11:23

- - -

### [Towards Modeling Data Quality and Machine Learning Model Performance](http://arxiv.org/abs/2412.05882)

**データ品質と機械学習モデルのパフォーマンスのモデリングに向けて**

Usman Anjum, Chris Trentman, Elrod Caden, Justin Zhan

- データ中の不確実性やノイズの影響を理解することが、信頼性の向上とパフォーマンス評価に重要
- 新たに不確実性とノイズを定量化するモデルを提案
- 信号対雑音比(SNR)の概念を基に、決定論的-非決定論的比(DDR)という新指標を開発
- 合成データを用いた実験で、DDRと精度の関係を示し、性能評価が可能なことを確認

不確実性ってやっぱり難しいけど、こういう新しい指標を開発するのってすごく面白そう！精度がどのくらい変わるのか、DDR-accuracy曲線をもう少し詳しく知りたいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-08 10:15

- - -

### [DapperFL: Domain Adaptive Federated Learning with Model Fusion Pruning for Edge Devices](http://arxiv.org/abs/2412.05823)

**DapperFL: モデル融合プルーニングによるエッジデバイス向けドメイン適応型連合学習**

Yongzhe Jia, Xuyun Zhang, Hongsheng Hu, Kim-Kwang Raymond Choo, Lianyong Qi, Xiaolong Xu, Amin Beheshti, Wanchun Dou

- 連合学習はプライベートデータを共有せずにグローバルモデルを最適化するが、ドメインシフトで効率低下
- DapperFLはModel Fusion Pruningでシステムの不均一性に対応し、個別のローカルモデルを作成
- Domain Adaptive Regularizationによって、異なるドメイン間で強力な表現を学ぶことを目指す
- 実世界のFLプラットフォームでテストし、最大2.28%の性能向上と20%-80%のモデル縮小を達成

この技術のおかげで、みんなが一緒に勉強する時、お互いの強みをうまく活かし合えるって感じで面白いね！今後もプライバシーを守りながら賢い機械がもっと増えるのかなってワクワクする！

**Comment:** Oral accepted by NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-08 05:50

- - -

### [Adversarially Robust Dense-Sparse Tradeoffs via Heavy-Hitters](http://arxiv.org/abs/2412.05807)

**敵対的状況に対する高密度-疎密トレードオフの実現**

David P. Woodruff, Samson Zhou

- 敵対的なストリーミングモデルでデータセットの統計を小さな空間で近似する手法を研究
- 既存技術を用いた高密度-疎密トレードオフ技術が敵対的耐性の$L_p$推定を実現
- 改善された敵対的耐性の$L_p$-ヘビーヒッターアルゴリズムを提案し、効率向上
- クラシカルなストリーミング設定用の新アルゴリズムで頻度モーメント推定を改善

敵対的な環境でのアルゴリズムとか重みのトレードオフが面白そう！より効率的な推定方法が実際にどう役立つか気になるね。området

**Comment:** NeurIPS 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, **投稿日時:** 2024-12-08 04:09

- - -

### [Prism: Semi-Supervised Multi-View Stereo with Monocular Structure Priors](http://arxiv.org/abs/2412.05771)

**Prism: 単眼構造事前知識を用いた半教師ありマルチビューステレオ**

Alex Rich, Noah Stier, Pradeep Sen, Tobias Höllerer

- 無監督MVSは大規模なラベルなしデータを活用するが、困難なデータで性能が低い
- 合成データセットの高品質さは実世界への一般化が困難
- 実画像と合成画像を連携して学習する半教師ありフレームワークを提案
- 深層特徴損失と多スケール統計損失を活用し、大幅な改善を実現

Prismって名前がカッコいいね！合成データと実データを一緒に使うアイデア、なんかイノベーティブでワクワクする！スマホ動画でも使えるようになると、日常がもっと楽しくなりそう！

**Comment:** 11 pages, 6 figures, 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-08 01:05

- - -

### [DeMem: Privacy-Enhanced Robust Adversarial Learning via De-Memorization](http://arxiv.org/abs/2412.05767)

**DeMem: 逆記憶化によるプライバシー強化型のロバスト敵対的学習**

Xiaoyu Luo, Qiongxiu Li

- 敵対的ロバスト性はモデルの信頼性に必須だが、プライバシー攻撃に弱くなる
- 差分プライバシーはプライバシー攻撃を軽減するが、サンプルのロバスト性を損なう
- DeMemを提案し、高リスクサンプルに焦点を当てロバスト性とプライバシーのバランスを向上
- DeMemは複数の訓練方法やデータセットで有効性が確認されている

DeMemって面白そうじゃない？プライバシーを守りながらモデルの強さを保てるなんていい感じ！普段使ってるアプリにも応用される日が来るかもって考えたらワクワクするよね。

**Comment:** 8 pages

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-08 00:22

- - -

### [A Game-Theoretic Framework for Privacy-Aware Client Sampling in Federated Learning](http://arxiv.org/abs/2412.05636)

**連合学習におけるプライバシー考慮型クライアントサンプリングのゲーム理論的フレームワーク**

Wenhao Yuan, Xuehe Wang

- 連合学習モデルの精度損失のため、プライバシー考慮型クライアントサンプリング確率の上限を導出
- クライアントと中央サーバーの相互作用を2段階のStackelbergゲームとしてモデル化
- 平均場推定器を導入し、他のクライアントのプライベート情報を推定して戦略の最適化
- 提案したクライアントサンプリング戦略がPoAを削減し、効率損失を軽減することを理論的に証明

この研究、本当に面白そうだよね！プライバシーも守りつつ、連合学習の効率を上げるなんてすごく未来的でワクワクするよ！しかも、数学的にしっかり保証されているところが安心感あるなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.GT, **投稿日時:** 2024-12-07 12:42

- - -

### [Can large language models be privacy preserving and fair medical coders?](http://arxiv.org/abs/2412.05533)

**大規模言語モデルはプライバシー保護と公平な医療コード化が可能か？**

Ali Dadsetan, Dorsa Soleymani, Xijie Zeng, Frank Rudzicz

- 医療における機械学習のプライバシー保護は重要な課題
- 差分プライバシー適用でパフォーマンス低下、特にMIMIC-IIIデータで40%以上のマイクロF1スコア減少
- プライバシーと公平性のトレードオフで、男女間のリコールギャップが3%以上増加
- トレードオフの理解が現実世界での課題解決に役立つ可能性

難しいテーマだね！プライバシーを守りながら、医療分野のAIをどれだけ公平に使えるか注目だよね。もっと多くのデータで検証してみる価値がありそう～。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-07 04:27

- - -

### [Upcycling Noise for Federated Unlearning](http://arxiv.org/abs/2412.05529)

**連合学習におけるノイズのアップサイクリングによる忘却**

Jianan Chen, Qin Hu, Fangtian Zhong, Yan Zhuang, Minghui Xu

- 連合学習は生データを共有せずに複数のクライアントでモデルを訓練するが、差分プライバシーで保護される
- クライアントの「忘れられる権利」を満たすには、差分プライバシー連合学習が新たな課題となる
- 提案手法FUIは、差分プライバシー連合学習内で目標クライアントのデータを初めて忘却する方法
- 実験では、提案手法FUIが他の主流の忘却手法より優れた性能と効率を示すことを確認

この研究楽しいね！連合学習の新しい課題を解決する方法って、すごくわくわくするよね。難しい問題を解決するための新しい道筋が具体的に見えてきて、私も挑戦してみたいって思ったよ！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-12-07 04:07

- - -

### [Multi-Armed Bandit Approach for Optimizing Training on Synthetic Data](http://arxiv.org/abs/2412.05466)

**合成データの最適化トレーニングのための多腕バンディットアプローチ**

Abdulrahman Kerim, Leandro Soriano Marcolino, Erickson R. Nascimento, Richard Jiang

- 合成データの使用性を評価する新しいUCBベースのトレーニング手法を提案
- 合成画像の低レベル・高レベル情報を統合した動的メトリックを導入
- LLMとStable Diffusionを統合した属性対応バンディットパイプラインを提案
- 提案手法で分類精度が最大10%向上し、幅広い分類器の性能を向上

この研究、合成データをもっと賢く使うための方法なんだねー！特に分類精度がぐんと上がるって、すごいなぁって思った！未来のデータサイエンスに期待できそうだよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-12-06 23:36

- - -

### [Generative Model-Based Fusion for Improved Few-Shot Semantic Segmentation of Infrared Images](http://arxiv.org/abs/2412.05341)

**生成モデルベースの融合による赤外線画像の改良型Few-Shotセマンティックセグメンテーション**

Junno Yun, Mehmet Akçakaya

- 赤外線画像のセマンティックセグメンテーションはデータ不足や異なるコントラストなどの課題がある
- 既存のFew-ShotセグメンテーションモデルはRGB画像とのペアリングが必須で、データ獲得が困難
- 本研究は生成モデルと融合技術を用いて補助データを生成しIR画像の限定コントラストを補う
- 提案手法は異なるIRデータセットで評価され、最先端のFSSモデルを上回る成果を得る

赤外線画像のセグメンテーションって、すごく難しいのにこんな方法で解決できるなんて面白いよね。未来の技術がもっと身近になりそうで、わくわくするなぁ！

**Comment:** Winter Conference on Applications of Computer Vision (WACV), 2025

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, eess.IV, **投稿日時:** 2024-12-06 05:14
