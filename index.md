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

更新: 2024-10-25T04:25:18.176041

- - -

### [FedSPD: A Soft-clustering Approach for Personalized Decentralized Federated Learning](http://arxiv.org/abs/2410.18862)

**FedSPD: ソフトクラスタリングによる個人化分散連合学習アプローチ**

I-Cheng Lin, Osman Yagan, Carlee Joe-Wong

- 従来の連合学習は集中型サーバーを使用するが、FedSPDは分散型で単一故障点を排除
- 個々のクライアントが異なるデータに最適化されたパーソナライズモデルを生成
- クラスターベースの手法でモデルの統一と個別化を両立し、低接続環境でも有効
- 通信コストが従来手法より大幅に削減され、同時に精度も向上することを実証

FedSPDってすごく面白そう！低接続ネットワークとかでのチームワークがどんどん進化しちゃうってことだよね。みんなでデータを共有しなくても、情報をうまく集めて強くなれるって感じがするよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-24 15:48

- - -

### [PSY: Posterior Sampling Based Privacy Enhancer in Large Language Models](http://arxiv.org/abs/2410.18824)

**PSY: 大規模言語モデルにおける事後サンプリングベースのプライバシー強化手法**

Yulian Sun, Li Duan, Yong Li

- LLMsのプライバシー脆弱性として、記憶による漏洩が問題となっている
- LoRAはLLMsの微調整に使われ、プライバシー強化モジュール挿入の好機である
- PSYは事後サンプリングを用い、中間情報からのプライバシー漏洩を防ぐ手法を示す
- PSYを追加したLoRAは、攻撃成功率を低下させながらモデル性能への悪影響を最小限に抑える

この研究、すっごく面白そう！Latent spaceを拡張することで新しいプライバシー強化の可能性を見せてくれて、未来のLLMがもっと安全になるかもね。私たちのデータもこの技術でしっかり守られるのかなって思うと、ワクワクしちゃう！

**Comment:** 10 pages, 2 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-24 15:15

- - -

### [Distill Visual Chart Reasoning Ability from LLMs to MLLMs](http://arxiv.org/abs/2410.18798)

**視覚的チャート推論能力をLLMからMLLMへ蒸留する**

Wei He, Zhiheng Xi, Wanxu Zhao, Xiaoran Fan, Yiwen Ding, Zifei Shan, Tao Gui, Qi Zhang, Xuanjing Huang

- 複雑なチャートQ&Aタスクには、視覚的認識と推論の能力が求められる
- 効果的なMLLM強化には、視覚とテキスト情報の統合が必要
- Code-as-Intermediary Translationでコストを抑えたデータ合成方法を提案
- 合成データセットReachQAで視覚認識と推論能力の向上を確認

視覚情報をテキスト化するこのアプローチ、なんか未来感あってワクワクする！データ合成で質の高い学習を実現するのも効率的でいいね。試してみたい！

**Comment:** Under review. The code and dataset are publicly available at   https://github.com/hewei2001/ReachQA

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-24 14:50

- - -

### [Learning Geodesics of Geometric Shape Deformations From Images](http://arxiv.org/abs/2410.18797)

**画像からの幾何学的形状変形の測地線学習**

Nian Wu, Miaomiao Zhang

- 測地線変形場の学習を画像から可能にする方法を初めて提案
- 提案手法GDNは、網絡が無視していた測地線を見つけ分析に活用
- 数学的に未知の写像関数を学習するための効率的なニューラルオペレーターを開発
- 新しい測地線損失を用いて、ネットワークの安定性と一般化能力を向上

この研究ってさ、画像から測地線を学習できちゃうところがめっちゃ新しいよね！2Dと3D両方での実験もあって、医療への応用も見えそうでドキドキしちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-24 14:49

- - -

### [Adapting MLOps for Diverse In-Network Intelligence in 6G Era: Challenges and Solutions](http://arxiv.org/abs/2410.18793)

**6G時代におけるネットワーク内インテリジェンスの多様性に適応したMLOpsの課題と解決策**

Peizheng Li, Ioannis Mavromatis, Tim Farnham, Adnan Aijaz, Aftab Khan

- AIとMLを無線システムに統合することが6Gの発展に不可欠
- 現行のMLOpsアプローチは多様な学習パラダイムやネットワークの異質性に対応できていない
- 新たなアプローチとしてRLOps、FedOps、GenOpsの3つのオペレーションパイプラインを導入
- 各オペレーションに特化した課題と解決策を示し、AIネイティブな6Gネットワークの大規模展開を可能にする

6Gがますます現実味を帯びてくる中、AIとMLがどんな風にネットワークと関連付けられるのか興味津々だね！新しいMLOpsのアイデアがこれからの技術の進化を加速させるのかも。

**Comment:** 7 pages, 5 figures. This paper has been submitted to IEEE for   possible publication

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.LG, **投稿日時:** 2024-10-24 14:47

- - -

### [Does Differential Privacy Impact Bias in Pretrained NLP Models?](http://arxiv.org/abs/2410.18749)

**差分プライバシーは事前学習されたNLPモデルにおけるバイアスに影響を与えるか？**

Md. Khairul Islam, Andrew Wang, Tianhao Wang, Yangfeng Ji, Judy Fox, Jieyu Zhao

- 差分プライバシー (DP) は学習データ漏洩を防ぐために大規模言語モデルに適用される
- DP はプライバシー-ユーティリティトレードオフを改善するだけでなく、少数派グループにバイアスを引き起こす場合がある
- DP による学習は AUC に基づくバイアスメトリクスにより保護グループに対するバイアスを増加させる
- DP のバイアスへの影響はプライバシー保護レベルだけでなくデータセットの分布にも左右される

差分プライバシーって、プライバシーを守ってくれるはずなのにバイアスが増えちゃうこともあるんだね。データの分布も大事なんだって、これからはただプライバシーを守るだけじゃなくって、公平性まで考えないとだね！

**Comment:** Github https://github.com/khairulislam/DP-on-NLP-Bias

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-10-24 13:59

- - -

### [Unleashing Reasoning Capability of LLMs via Scalable Question Synthesis from Scratch](http://arxiv.org/abs/2410.18693)

**LLMの推論能力を解き放つためのスケーラブルな質問合成法**

Yuyang Ding, Xinyu Shi, Xiaobo Liang, Juntao Li, Qiaoming Zhu, Min Zhang

- 高品質なデータはLLMの推論能力向上に重要である
- 既存の方法はシード質問や知識ベースからデータ生成を行う
- ScaleQuestはオープンソースモデルを用いシードデータなしで問題生成可能
- 作成したデータセットは主要モデルの性能を最大46.4%向上させた

ScaleQuestってオープンソースのモデルだけで強い性能を実現してるんだね。これで推論能力がもっとすごくなるかも！他の企業のプロプライエタリモデルに負けない存在になるなんて胸アツだよね。

**Comment:** Preprint. Project page: https://scalequest.github.io/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-10-24 12:42

- - -

### [Little Giants: Synthesizing High-Quality Embedding Data at Scale](http://arxiv.org/abs/2410.18634)

**小さな巨人たち: 高品質な埋め込みデータを大規模に生成する**

Haonan Chen, Liang Wang, Nan Yang, Yutao Zhu, Ziliang Zhao, Furu Wei, Zhicheng Dou

- 合成データ生成は大規模なデータセットなしでモデル訓練を可能にする手法
- テキスト埋め込みには多様でスケーラブルな訓練例を提供し、人間の注釈コストを削減
- 現行のアプローチはGPT-4などの専有モデルに依存し高コストで非効率
- SPEEDフレームワークは小型オープンソースモデルを使い効率的に高品質データを生成

合成データで大規模にデータを生成できるなんてすごいよね！専用モデルに頼らずに質を上げられる方法を追求していくのが未来の方向性かも。興味をひかれちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.IR, **投稿日時:** 2024-10-24 10:47

- - -

### [Knowledge Distillation Using Frontier Open-source LLMs: Generalizability and the Role of Synthetic Data](http://arxiv.org/abs/2410.18588)

**先端オープンソースLLMを用いた知識蒸留: 一般化可能性と合成データの役割**

Anup Shirgaonkar, Nikhil Pandey, Nazmiye Ceren Abay, Tolga Aktas, Vijay Aski

- オープンソースの大型言語モデル（LLM）は強力だが、推論のコストと遅延が大きい。
- 知識蒸留により、大型教師モデルの性能を小型生徒モデルに移し、低コストで利用可能に。
- 合成データを活用することで、小型モデルの精度が向上し、大型モデルを超える場合も。
- 知識蒸留の評価には、タスクごとの多面的な精度や品質評価が重要と判明。

合成データを使って小さくても優秀なモデルを作るなんて、すごいよね！これで低コストでも高性能なAIが実現できちゃうかも。色んなタスクで試せるのもワクワクする！

**Comment:** 25 pages, 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-24 09:37

- - -

### [Infinity-MM: Scaling Multimodal Performance with Large-Scale and High-Quality Instruction Data](http://arxiv.org/abs/2410.18558)

**Infinity-MM: 大規模かつ高品質な指導データでマルチモーダルパフォーマンスを向上**

Shuhao Gu, Jialing Zhang, Siyuan Zhou, Kevin Yu, Zhaohu Xing, Liangdong Wang, Zhou Cao, Jintao Jia, Zhuoyi Zhang, Yixuan Wang, Zhenchong Hu, Bo-Wen Zhang, Jijie Li, Dong Liang, Yingli Zhao, Yulong Ao, Yaoqi Liu, Fangxiang Feng, Guang Liu

- オープンソース指導データの規模と質の制限がVLMの性能を制約している
- Infinity-MMは4000万件のデータを持つ大規模マルチモーダル指導データセット
- 合成指導生成法を提案し、詳細な画像注釈や多様な質問生成を行う
- 新たに訓練した2ビリオンパラメータのモデルがSOTA性能を達成

新しいデータセットでVLMがどこまで進化できるのかワクワクするね！それに合成データのパワーもどんどん活用されていくのが面白いなって思う。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-24 09:03

- - -

### [Synth4Seg -- Learning Defect Data Synthesis for Defect Segmentation using Bi-level Optimization](http://arxiv.org/abs/2410.18490)

**Synth4Seg -- 欠陥セグメンテーションのための二段階最適化による欠陥データ合成の学習**

Shancong Mou, Raviteja Vemulapalli, Shiyu Li, Yuxuan Liu, C Thomas, Meng Cao, Haoping Bai, Oncel Tuzel, Ping Huang, Jiulong Shan, Jianjun Shi

- 欠陥セグメンテーションは品質管理に重要だが、データ不足が深層学習の課題である
- 合成欠陥データ生成はデータ不足を補う手段だが、固定ルールでは下流の性能に影響を与えかねない
- 二段階最適化に基づく新しい合成欠陥データ生成フレームワークを提案
- 最適化手法で訓練し18.3%の性能向上、異なるデータソースの重みを学習し2.6%の向上を達成

この研究は、二段階最適化による賢いデータ生成で性能をグイっと引き上げてるみたいで興味深いね！データが少なくても工夫次第でこんなに精度上げられるなんて、技術の進歩にはワクワクしちゃうね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-24 07:25

- - -

### [Classifier Clustering and Feature Alignment for Federated Learning under Distributed Concept Drift](http://arxiv.org/abs/2410.18478)

**連合学習における分散概念ドリフトへの分類器クラスタリングと特徴整合**

Junbao Chen, Jingfeng Xue, Yong Wang, Zhenyan Liu, Lu Huang

- 分散概念ドリフトは、クライアントごとに異なるドリフトを経験するため、連合学習において大きな課題である
- 条件付き分布$P(Y|X)$とデータ不均一性の度合いの2つが特徴整合において重要な要素である
- 提案されたFedCCFAフレームワークは、分類器クラスタリングと特徴整合を採用し、ドリフト下での協調を強化する
- FedCCFAは、ラベル分布$P(Y)$のエントロピーに基づいて特徴空間を適応的に整合し、既存の手法を凌駕する結果を示す

クライアントのデータが異なっても、連合学習をうまく適用できるように工夫されてておもしろい！違うデータセットでも一緒に活用できる未来の技術なんだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-24 07:04

- - -

### [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](http://arxiv.org/abs/2410.18447)

**ToolFlow: 自然で一貫した対話合成によるLLMツール呼び出しの強化**

Zezhong Wang, Xingshan Zeng, Weiwen Liu, Liangyou Li, Yasheng Wang, Lifeng Shang, Xin Jiang, Qun Liu, Kam-Fai Wong

- 大規模言語モデルのツール呼び出し能力を強化するための教師あり微調整法を提案
- 現在の合成データ手法では無関連なツール組み合わせになりがちで多様性が低い
- グラフベースのサンプリングと一貫性ある対話合成手法で自然さと一貫性を向上
- ToolFlowが生成した合成会話データにより、GPT-4と同等またはそれ以上の性能を実現

ToolFlowのアプローチすごくユニークで、ツールの組み合わせをもっと的確にサンプリングできるんだね。対話が自然でまとまりがあるってかなり重要だと思う。GPT-4を超える性能も夢じゃないなんて、これからの応用事例が楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-24 05:45

- - -

### [Enhancing Feature-Specific Data Protection via Bayesian Coordinate Differential Privacy](http://arxiv.org/abs/2410.18404)

**ベイズ座標差分プライバシーによる機能特異的なデータ保護の強化**

Maryam Aliakbarpour, Syomantak Chaudhuri, Thomas A. Courtade, Alireza Fallah, Michael I. Jordan

- LDPはユーザーが第三者を信頼しなくても強固なプライバシーを提供する
- ベイズ座標差分プライバシー（BCDP）により、機能別のプライバシー量を調整可能
- BCDPは通常のLDPと比較し、機能に応じた保護でタスク性能を向上
- BCDPを用い、プライベートな平均推定と回帰で精度を向上

面白そうなポイントは、プライバシーに敏感な部分を調整できるところ！これでデータ分析もますます安全で賢くなりそうだね。私たちの個人情報ももっと守られるって思うと安心できるよね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-10-24 03:39

- - -

### [Faster Algorithms for User-Level Private Stochastic Convex Optimization](http://arxiv.org/abs/2410.18391)

**ユーザーレベルのプライベート確率的凸最適化の高速アルゴリズム**

Andrew Lowy, Daogao Liu, Hilal Asi

- ユーザーレベル差分プライバシー（DP）での確率的凸最適化に取り組む
- 従来の手法は滑らかさの仮定が強く、大規模学習に向かない問題があった
- 線形時間アルゴリズムを開発し、滑らかさ仮定を緩和しつつ最先端の性能を実現
- 新アルゴリズムでユーザー数の多項式増加を必要とせずに効率的な計算を達成

この研究、速くて効率的なアルゴリズムができたみたいでワクワクするね！大規模データも安心して扱える時代が近づいてきてるのかも？✨

**Comment:** NeurIPS 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, math.OC, **投稿日時:** 2024-10-24 03:02

- - -

### [FedBaF: Federated Learning Aggregation Biased by a Foundation Model](http://arxiv.org/abs/2410.18352)

**FedBaF: 基盤モデルによる連合学習の偏りを抑える手法**

Jong-Ik Park, Srinivasa Pranav, José M. F. Moura, Carlee Joe-Wong

- 基盤モデルは多様なタスクに汎化する能力で注目され、連合学習に利用されている
- 既存手法はモデル重みをクライアントに開示しプライバシーを守るが、情報セキュリティにリスク
- FedBaFは重みの秘密を保持しつつ、連合学習の統合過程で基盤モデルを活用する新手法
- 実験で既存手法を最大15.8%上回る精度を示し、言語モデルの困惑度を最大39.2%削減

FedBaFって、すごくおもしろいアイディアだよね！基盤モデルを使ってるのに秘密を守りつつ精度も向上できるなんて。これから連合学習がもっと広まっていきそう♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-10-24 01:14

- - -

### [LEGO: Language Model Building Blocks](http://arxiv.org/abs/2410.18287)

**LEGO: 言語モデル構築ブロック**

Shrenik Bhansali, Alwin Jin, Tyler Lizzo, Larry Heck

- 大規模言語モデル(LLM)は重要だが、データ収集や学習が高コストである
- タスク特化型小規模言語モデル(SLM)は安価だが、頑健性と一般化に欠ける
- LEGO技術はLLMからSLMsを抽出して再結合し、効率的なモデル微調整を可能にする
- LEGOは連合学習と新しい集約スキームを使用し、データの多様性に対応しつつ頑健性を維持

LEGOって、なんか組み合わせて新しいものを作る感じが楽しそうだよね！ユーザーのデータも守りつつ、効率よくモデル化できるなんて高校のプロジェクトとかにも応用できそうじゃない？



**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-10-23 21:31

- - -

### [CARLA2Real: a tool for reducing the sim2real gap in CARLA simulator](http://arxiv.org/abs/2410.18238)

**CARLA2Real: CARLAシミュレーターにおけるシム2リアルギャップを縮小するツール**

Stefanos Pasios, Nikos Nikolaidis

- 自動運転やドローン研究のシミュレーターは重要だが、仮想と現実の差が依然存在する
- CARLA2Realは、シミュレーションデータのフォトリアリズムを向上させ現実世界に近づける
- 本ツールで生成された合成データは、Cityscapesなどの現実データセットにスタイル転送
- 提案した方法を用いた実験で、シム2リアルギャップが重要であることを確認し縮小が証明された

CARLAって人気のシミュレーターなんだね！リアリズムを向上させることで、もっとリアルな実験ができるようになって、すごく楽しみだよ。これがどれだけ実世界のテストに役立つのかワクワクしちゃう。

**Comment:** 22 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-23 19:33
