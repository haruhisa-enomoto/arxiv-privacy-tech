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

更新: 2024-11-10T04:19:49.614380

- - -

### [Few-Shot Task Learning through Inverse Generative Modeling](http://arxiv.org/abs/2411.04987)

**逆生成モデリングを用いた少数ショットタスク学習**

Aviv Netanyahu, Yilun Du, Antonia Bronars, Jyothish Pari, Joshua Tenenbaum, Tianmin Shu, Pulkit Agrawal

- エージェントの意図を少数の例から学習する課題を「タスク概念学習」と呼ぶ
- 逆生成モデルを用いた少数ショットタスク学習(FTL-IGM)を提案
- 基本的な概念のデモを使い生成モデルを事前訓練し、新しい概念は逆伝播で学習
- 五つのドメインで評価し、未知環境や既存概念との組み合わせで新しい概念を学習

この研究、少数のデータから新しい動きを覚えちゃうんだね！未来のAIがさらに柔軟にそして迅速に新しいタスクを理解して行動できるようになることで、日常生活やいろんな産業の場面でもっと役立つじゃんって、ワクワクしちゃう。実際にどんな動きができるようになるのか、試してみたいね！



**トピック:** [連合転移学習](ftl), **カテゴリ:** cs.AI, cs.LG, cs.RO, **投稿日時:** 2024-11-07 18:55

- - -

### [Uncovering Hidden Subspaces in Video Diffusion Models Using Re-Identification](http://arxiv.org/abs/2411.04956)

**再識別を用いたビデオ拡散モデルにおける隠れた部分空間の発見**

Mischa Dombrowski, Hadrien Reynaud, Bernhard Kainz

- 合成データセットの安全な共有は、医療などのプライバシー重視の分野で重要
- プライバシー保存モデルの学習は、潜在空間での計算効率向上と一般化に役立つ
- 再識別モデルを利用し、合成データセットの忠実度を測定する方法を提案
- 潜在ビデオ拡散モデルは学習量が全体の30.8%に過ぎず、性能低下の要因の1つ

この研究、医療とかで本物のデータ使わずに合成データ使えるってのが革新的かもね！プライバシーを守れる合成データで、安全に研究進められる未来、ちょっとワクワクするなぁ。

**Comment:** 8 pages, 5 tables, 6 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-11-07 18:32

- - -

### [Fed-LDR: Federated Local Data-infused Graph Creation with Node-centric Model Refinement](http://arxiv.org/abs/2411.04936)

**Fed-LDR: ノード中心のモデル精緻化による連合型ローカルデータ混合グラフの作成**

Jiechao Gao, Yuangang Li, Syeda Faiza Ahmed

- 世界的な都市化の加速に伴い、都市インフラとサービス向上の新しい課題を生む
- 連合学習とグラフ畳み込みネットワークを活用し、都市環境の時空間データ分析を強化
- ローカルデータ混合グラフ作成とノード中心のモデル精緻化で都市環境の多様性に対応
- 提案手法は他6つの手法を上回り、誤差を最大81％、78％削減し高い相関係数を保持

これはちょっと面白いね！都市のデータをこんな風に複雑に分析できると、未来の街づくりに本当に役立ちそう。持続可能な発展を考えると、こういう技術ってワクワクするなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.SI, **投稿日時:** 2024-11-07 18:13

- - -

### [OpenCoder: The Open Cookbook for Top-Tier Code Large Language Models](http://arxiv.org/abs/2411.04905)

**OpenCoder: トップクラスのコード大型言語モデルのためのオープンクックブック**

Siming Huang, Tianhao Cheng, Jason Klein Liu, Jiaran Hao, Liuyihan Song, Yang Xu, J. Yang, J. H. Liu, Chenchen Zhang, Linzheng Chai, Ruifeng Yuan, Zhaoxiang Zhang, Jie Fu, Qian Liu, Ge Zhang, Zili Wang, Yuan Qi, Yinghui Xu, Wei Chu

- コード向け大型言語モデル(LLMs)は様々なドメインで不可欠だが、高品質で再現可能なオープンモデルは少ない
- OpenCoderは性能が高く、再現可能なデータ処理パイプラインと透明なトレーニングプロトコルを提供する
- この研究では、データのクリーニングと重複除去、コード関連テキストの再呼び出し、高品質の合成データが重要と示す
- OpenCoderは研究の基盤を提供し、コードAIの進歩を加速するオープンなモデルとして機能する

こういうオープンな取り組み、すごくイイね！難しいことをちゃんと誰でも試せる道具にして、みんなで進化させられるところがワクワクする！コーディングAIの未来が見えてくる気がする～✨



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.PL, **投稿日時:** 2024-11-07 17:47

- - -

### [Controlling Human Shape and Pose in Text-to-Image Diffusion Models via Domain Adaptation](http://arxiv.org/abs/2411.04724)

**ドメイン適応によるテキストから画像への拡散モデルでの人体形状とポーズ制御**

Benito Buchheim, Max Reimann, Jürgen Döllner

- 3DパラメトリックモデルSMPLを用いて人体形状とポーズを条件に拡散モデルを制御
- 合成データ生成を利用し、現実データよりも低コストで条件適合させる手法を提案
- ドメインギャップとシーン多様性の欠如を解消するドメイン適応技術を開発
- SMPL制御で形状とポーズの多様性向上を達成し、視覚的忠実度を維持

この研究、未来のアニメーションやゲーム作りにすごく役立ちそうだよね！人間の動きや姿勢をもっと自由にコントロールできるって、創造性がどんどん広がる予感で興奮しちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-07 14:02

- - -

### [Differential Privacy Overview and Fundamental Techniques](http://arxiv.org/abs/2411.04710)

**差分プライバシーの概要と基本技術**

Ferdinando Fioretto, Pascal Van Hentenryck, Juba Ziani

- データプライバシー保護の試行錯誤を説明し、失敗例と強固なプライバシー定義の要件を提示
- プライバシー保護データ分析の主要な要素や領域を定義し、差分プライバシーの基本を説明
- 差分プライバシーの構成、後処理免疫、グループプライバシーなどの特性を形式化
- 純粋形式と近似形式で差分プライバシーを実装する基本技術とメカニズムをレビュー

差分プライバシーに関する理論と実践のギャップを埋めようとしているところがいいなぁ！技術をどう応用するかが未来のプライバシーを変えるかも！？

**Comment:** Chapter 1 of book: "Differential Privacy in Artificial Intelligence:   From Theory to Practice"

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-11-07 13:52

- - -

### [BhasaAnuvaad: A Speech Translation Dataset for 14 Indian Languages](http://arxiv.org/abs/2411.04699)

**BhasaAnuvaad: 14のインド言語における音声翻訳データセット**

Sparsh Jain, Ashwin Sankar, Devilal Choudhary, Dhairya Suman, Nikhil Narasimhan, Mohammed Safi Ur Rahman Khan, Anoop Kunchukuttan, Mitesh M Khapra, Raj Dabre

- インドの公用語22言語中10言語未満しか対応していないASTデータセットの不足が問題。
- 現在のASTシステムは、読み上げ音声には対応できるが、自発的な発話には対応が難しい。
- 日常会話の重要性を考慮し、口語的言語やインフォーマルな言語の翻訳が非常に困難。
- BhasaAnuvaadは44,400時間、1700万テキストを含むデータセットで、3つのカテゴリーに分かれている。

インドの多様な言語をたくさんカバーするデータセットはすごいな！これで日常会話とかの翻訳がもっと普通にできるようになったら、いろんな文化や言語も身近に感じられるかも。楽しみだね！

**Comment:** Work in Progress

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-11-07 13:33

- - -

### [Personalized Federated Learning for Cross-view Geo-localization](http://arxiv.org/abs/2411.04692)

**個別化連合学習によるクロスビュー地理的ローカリゼーション**

Christos Anagnostopoulos, Alexandros Gkillas, Nikos Piperigkos, Aris S. Lalos

- データプライバシーと異質性の課題を連合学習で解決
- 大まかな特徴抽出は共有し、詳細な特徴は各環境に特化させる手法
- 提案手法は中央集約的な手法に近い性能でプライバシーを保持
- 部分的なモデル共有戦略で通信負荷を削減しつつ精度を維持

クロスビュー地理的ローカリゼーションもこれで安心だね！連合学習が未来の車たちの道案内をもっとスマートにしてくれそうでワクワクする～。自分の環境に合った情報を上手に使うって、なんだか人間みたいで面白いよね。

**Comment:** 6 pages, 2 figures, Preprint submitted to the IEEE 26th International   Workshop on Multimedia Signal Processing (MMSP)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-11-07 13:25

- - -

### [Differentially Private Continual Learning using Pre-Trained Models](http://arxiv.org/abs/2411.04680)

**事前学習モデルを使用した差分プライバシー対応の継続学習**

Marlon Tobaben, Marcus Klasson, Rui Li, Arno Solin, Antti Honkela

- 継続学習モデルはタスク間で知識を保持するが、個々のサンプルをメモライズしないという差分プライバシーの要件と矛盾する
- 事前学習モデルを活用し、プライバシーと性能のトレードオフを解消する方法を提案
- 差分プライバシーのもとで学習される、パラメータを必要としない分類器と効率的なアダプターを組み合わせる
- 実験で有効性を示し、継続学習とプライバシーの競合する要求のバランスを取る方法に洞察を提供

継続学習と差分プライバシーを両立させるために、事前学習モデルの力を利用するのが面白いよね！これでプライバシーを守りながらも、よりスマートなモデルが作れるなんてワクワクするな〜！

**Comment:** 15 pages, 3 figures, Accepted at Scalable Continual Learning for   Lifelong Foundation Models Workshop at 38th Conference on Neural Information   Processing Systems (NeurIPS 2024)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-11-07 13:08

- - -

### [Improved Multi-Task Brain Tumour Segmentation with Synthetic Data Augmentation](http://arxiv.org/abs/2411.04632)

**合成データ拡張による多タスク脳腫瘍セグメンテーションの改善**

André Ferreira, Tiago Jesus, Behrus Puladi, Jens Kleesiek, Victor Alves, Jan Egger

- 自動化ツールの増加はより洗練された信頼性あるアルゴリズムの開発に起因
- 臨床基準を達成することと実生活で使えるツールの開発が大きな挑戦
- 合成データを用いることで成人の術後神経膠腫や放射線治療の髄膜腫のセグメンテーションを改善
- 合成データはアルゴリズムの強化に効果的だが、髄膜腫のタスクには直接適合しない

合成データがより強力なアルゴリズムにつながるなんて面白いわ！リアルな臨床試用に向けての発展も期待しちゃうね。GitHubのコードも公開されてるんだし、いろんな応用に挑戦してみたい！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-11-07 11:35

- - -

### [Towards Robust Federated Analytics via Differentially Private Measurements of Statistical Heterogeneity](http://arxiv.org/abs/2411.04579)

**頑健な連合分析のための統計的不均一性の差分プライバシー測定**

Mary Scott, Graham Cormode, Carsten Maple

- 統計的不均一性はデータサンプルの偏り具合を測る指標である
- 連合シナリオでは不均一性に起因し精度損失がより深刻な問題となる
- 3つの有望な測定方法を探り、差分プライバシーを組み込んで精度を算出
- 分析的メカニズムが異なる不均一性に対して高精度を示し、実験で検証

連合学習の新しいチャレンジだね！差分プライバシーを上手に使って、どんなに偏ったデータでもちゃんとした分析ができるって、世界がまた少し安全に進化しそうな予感！

**Comment:** 26 pages, 6 tables, 1 figure

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.DB, **投稿日時:** 2024-11-07 10:03

- - -

### [Experimental Secure Multiparty Computation from Quantum Oblivious Transfer with Bit Commitment](http://arxiv.org/abs/2411.04558)

**量子オブリビアストランスファーとビットコミットメントを用いた実験的秘密計算**

Kai-Yi Zhang, An-Jing Huang, Kun Tu, Ming-Han Li, Chi Zhang, Wei Qi, Ya-Dong Wu, Yu Yu

- 秘密計算は、個々のプライバシーを守りつつ共同計算を可能にする技術である
- この研究は、量子オブリビアストランスファー(QOT)を使い、ビットコミットメント方式を導入
- 最初の実用的応用として、プライベートセットインターセクション問題を解決し、共通要素を発見
- 2つの銀行が疑わしい口座を情報漏洩せずに特定することで、商業的応用の可能性を示す

量子技術を使って実用的な秘密計算を試したんだね！これで、プライバシーを守りながらもっと安心してデータの共有と分析ができる未来が広がりそう！量子コンピューティングっていつもハイテクで、ちょっとワクワクするなぁ。



**トピック:** [秘密計算](mpc), **カテゴリ:** quant-ph, cs.CR, **投稿日時:** 2024-11-07 09:29

- - -

### [FedDP: Privacy-preserving method based on federated learning for histopathology image segmentation](http://arxiv.org/abs/2411.04509)

**FedDP: 連合学習に基づくヒストパトロジー画像セグメンテーションのためのプライバシー保護法**

Liangrui Pan, Mao Huang, Lian Wang, Pinle Qin, Shaoliang Peng

- 中央集約型のデータ保存はプライバシー規制で困難、分散型アプローチが必要
- 連合学習を使用し、医療機関間で協力しながらプライバシー保護を実現
- 差分プライバシーでモデルの更新にノイズを加え、データの貢献度を推測不能にする
- FedDPは精度をほぼ保持しつつプライバシーを保護し、Dice, Jaccard, Accがわずかに減少

この研究、医療データを安全に使える方法を提案しててすごく画期的だと思う！他の分野にもこのアイデアが展開されていくと、新しい未来が見えてきそうだね。

**Comment:** Accepted in BIBM2024

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-11-07 08:02

- - -

### [Enhancing Bronchoscopy Depth Estimation through Synthetic-to-Real Domain Adaptation](http://arxiv.org/abs/2411.04404)

**合成から実データへのドメイン適応による気管支鏡深度推定の向上**

Qingyao Tian, Huai Liao, Xinyan Huang, Lujie Li, Hongbin Liu

- 単眼深度推定は3D再構築に役立つが、気管支鏡画像ではラベルデータ不足が問題
- 合成データを用い、深度ラベル付きでトレーニングし、実データへの深度推定を改善
- 提案するフレームワークは、合成データを活用しつつドメイン知識を適用
- ドメイン適応で合成データのみの学習に比べ、実データでの深度予測が向上

これってなんか、医学の世界がどんどん進化してるって感じで面白いよね！実際の医療現場でもどんどん使えるようになったらすごいことになりそう！



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-11-07 03:48

- - -

### [Generating Synthetic Electronic Health Record (EHR) Data: A Review with Benchmarking](http://arxiv.org/abs/2411.04281)

**合成電子健康記録データの生成：レビューとベンチマーク**

Xingran Chen, Zhenke Wu, Xu Shi, Hyunghoon Cho, Bhramar Mukherjee

- 合成EHRデータ生成の既存手法をレビューし、主要な方法をベンチマークで比較
- MIMIC-III/IVを用いてデータ忠実度、実用性、プライバシー保護、計算コストを評価
- GANベースの方法はデータ忠実度と実用性で優れ、ルールベースはプライバシー保護で優秀
- Pythonパッケージ「SynthEHRella」で多様な手法と評価基準の探索が可能

この論文、おもしろそう！特に個人情報をうまく保護しつつ、データを忠実に生成する工夫が気になるよね。SynthEHRellaを使って、自分でも色んな生成手法を試してみたくなっちゃうかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, stat.ML, **投稿日時:** 2024-11-06 21:59

- - -

### [Pose-Transformation and Radial Distance Clustering for Unsupervised Person Re-identification](http://arxiv.org/abs/2411.04255)

**ポーズ変換と放射距離クラスタリングによる教師なし人物再識別**

Siddharth Seth, Akash Sonth, Anirban Chakraborty

- 教師なし学習により、人物再識別問題を解決する方法を提案
- 真のラベル情報なしで学習し、識別能力を向上させる二段階の学習戦略
- ポーズ変換データセットを用いたディープネットワークの訓練が第一段階
- 新しい放射距離損失を導入し、低いクラスタ内差異と高いクラスタ間差異を実現

人の再識別ってすごいね、監視カメラの映像とかで人を見分けるのに役立ちそう！この方法、ラベルなしでやるからどの場所でも応用できて面白いよね。新しいクラスター手法で精度も上がるなんて、未来の監視システムがちょっと身近に感じる～！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-06 20:55

- - -

### [Debiasing Synthetic Data Generated by Deep Generative Models](http://arxiv.org/abs/2411.04216)

**深層生成モデルによって生成された合成データの偏り修正**

Alexander Decruyenaere, Heidelinde Dehaene, Paloma Rabaey, Christiaan Polet, Johan Decruyenaere, Thomas Demeester, Stijn Vansteelandt

- 合成データはプライバシー保護に有望だが、統計解析において偏りが生じる
- 深層生成モデル利用時にバイアスや不正確さが発生し、推測の有用性が低下
- 新手法でバイアスを考慮し、収束速度を向上、推定量の大標本分散を近似可能に
- シミュレーションと実データを用いて提案手法を実証し、データ解析向けモデル強化

合成データのバイアスを解決するなんて、ほんと画期的だよね！あたしもデータ解析にもっと信頼性が加えられるよう、これからの進化に期待しちゃう～。なんて、ちょっと大げさかな？でも未来が楽しみ！

**Comment:** Accepted for the 38th Conference on Neural Information Processing   Systems (NeurIPS 2024), joint first authors

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-11-06 19:24

- - -

### [Topology Bench: Systematic Graph Based Benchmarking for Core Optical Networks](http://arxiv.org/abs/2411.04160)

**Topology Bench: コア光ネットワークのための体系的グラフベースベンチマーク**

Robin Matzner, Akanksha Ahuja, Rasoul Sadeghi, Michael Doherty, Alejandra Beghelli, Seb J. Savory, Polina Bayvel

- Topology Benchは光ネットワーク研究のための包括的なトポロジデータセット
- 分析は105の実世界のネットワークと270,900の合成トポロジを用いて行われる
- 合成データが実世界の制約を補完し、トポロジ選択の偏りを減少させる
- 非教師あり学習でトポロジをクラスター化し、多様なセット選定を提案

この研究、なんだかワクワクするね！これまでバラバラだったデータをひとつにまとめて、より客観的で多様な光ネットワーク研究につながるかも。新しい知見がどんどん出てきそうで楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.NI, **投稿日時:** 2024-11-06 14:36

- - -

### [Cooperation and Personalization on a Seesaw: Choice-based FL for Safe Cooperation in Wireless Networks](http://arxiv.org/abs/2411.04159)

**シーソー上での協力とパーソナライズ: ワイヤレスネットワークにおける安全協力のための選択型連合学習**

Han Zhang, Medhat Elsayed, Majid Bavand, Raimundas Gaigalas, Yigit Ozcan, Melike Erol-Kantarci

- 連合学習は分散AI技術で、医療や金融などで応用されているがワイヤレスネットワークでは初期段階
- パーソナライズと協力の関係を分析し、既存の連合学習フレームワークの新たな視点を提供
- 協力レベルを調整可能な選択型アプローチを提案、安全かつ柔軟な連合学習を実現
- 選択型連合学習は、安全性や公平性の懸念に対処し、悪意のある攻撃から参加者を保護することを目指す

ワイヤレスネットワークでも連合学習が活かせるなんてすごい！貢献とプライバシーがうまくバランスとれるといいよね。これからの展開が楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.AI, cs.DC, cs.LG, **投稿日時:** 2024-11-06 14:09

- - -

### [Bayesian inference for geophysical fluid dynamics using generative models](http://arxiv.org/abs/2411.04140)

**生成モデルを用いた地球物理流体力学のベイズ推論**

Alexander Lobbe, Dan Crisan, Oana Lang

- データ同化は数値モデルの精度と予測能力を向上させる重要な役割を持つ
- 高次元非線形システムでのモデル校正は大きな課題
- 拡散生成モデルを用いて観測に統計的に一致する合成データ生成を行う
- 新しいサンプルを粒子フィルタリングに組み込み、計算効率を向上させることに成功

生成モデルを使って予測精度を上げるなんて面白いよね！これからの天気予報とか地球環境のモデリングにも、もっと役立てられるんじゃないかなってワクワクするよ。



**トピック:** [合成データ](sd), **カテゴリ:** math.NA, cs.NA, math.DS, 68T05, 76M35, **投稿日時:** 2024-11-01 15:57
