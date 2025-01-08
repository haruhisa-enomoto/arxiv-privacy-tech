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

更新: 2025-01-08T04:23:02.983043

- - -

### [A Survey on Federated Learning in Human Sensing](http://arxiv.org/abs/2501.04000)

**ヒューマンセンシングにおける連合学習の調査**

Mohan Li, Martin Gjoreski, Pietro Barbiero, Gašper Slapničar, Mitja Luštrek, Nicholas D. Lane, Marc Langheinrich

- ヒューマンセンシングは人間行動を理解するが、プライバシーの法的・倫理的懸念がある
- 連合学習は生データを送信せずに正確なモデルを作成でき、プライバシー問題を軽減
- ヒューマンセンシングでの連合学習の利点は十分に探求されていない
- 研究は連合学習の課題を8次元評価し、5つの研究領域の課題を強調

ヒューマンセンシングって便利だけど、プライバシーが心配なとこだよね。連合学習で安心して使えるようになるなんて、未来が楽しみ！新しい研究がどんどん進むといいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.HC, **投稿日時:** 2025-01-07 18:56

- - -

### [Synthetic Data Privacy Metrics](http://arxiv.org/abs/2501.03941)

**合成データのプライバシー計測基準**

Amy Steier, Lipika Ramaswamy, Andre Manoel, Alexa Haushalter

- 合成データはリアルデータに匹敵する精度でAIモデルや統計分析を支えている
- プライバシーを測る指標は多いが、標準化されていないのが現状
- 有名なプライバシー指標の利点と欠点をレビューし、攻撃シミュレーションを用いた評価も実施
- 差分プライバシーなどを用いて生成モデルを改良し、データのプライバシーを強化する方法を提示

合成データがリアルと同じくらい使えるなんてすごいね！プライバシーの強化も進んでて、未来のデータ使用が楽しみになっちゃう。こんな議論、大事にしていきたいよね。

**Comment:** 14 pages, 2 figures

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-07 17:02

- - -

### [A precise asymptotic analysis of learning diffusion models: theory and insights](http://arxiv.org/abs/2501.03937)

**A precise asymptotic analysis of learning diffusion models: 理論と洞察**

Hugo Cui, Cengiz Pehlevan, Yue M. Lu

- 高次元のターゲット密度に対する流れや拡散に基づく生成モデルの学習問題を考慮
- 低次元の射影によって生成されたサンプル分布の厳密な漸近特性を導出
- 学習サンプル数に依存した生成モデルのサンプル分布の特性を確認
- 合成データで再訓練するとモード崩壊が原因でモデル崩壊が発生する可能性あり

この研究、モード崩壊とかモデル崩壊とかすごく面白そうじゃない？新しい洞察が得られますようにって思っちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cond-mat.dis-nn, **投稿日時:** 2025-01-07 16:56

- - -

### [Private, Auditable, and Distributed Ledger for Financial Institutes](http://arxiv.org/abs/2501.03808)

**金融機関向けのプライベートで監査可能な分散型台帳**

Shaltiel Eloul, Yash Satsangi, Yeoh Wei Zhu, Omar Amer, Georgios Papadopoulos, Marco Pistoia

- 分散型台帳技術は効率的な取引処理とクロスパーティー取引調整を提供する
- プライバシー保護、監査対応、多様なデジタル資産への柔軟性が課題
- 零知識証明を使用し、カスタマイズ可能なプライバシーを実現する取引スキームを提案
- PADLは参加者のプライバシーを保ちつつ、多資産監査の円滑化をサポート

分散型台帳って、金融での使い方次第でいろんなことができそうでワクワクする！どんなデジタル資産と組み合わせると一番便利になるのかな？



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2025-01-07 14:21

- - -

### [SMIR: Efficient Synthetic Data Pipeline To Improve Multi-Image Reasoning](http://arxiv.org/abs/2501.03675)

**SMIR: マルチイメージ推論を改善する効率的な合成データパイプライン**

Andrew Li, Rahul Thapa, Rahul Chalamala, Qingyang Wu, Kezhen Chen, James Zou

- 単一画像理解ではVLMが強力だが、マルチイメージ推論はデータ拡張が難題
- SMIRによる合成データ生成パイプラインで、効率よく関連画像と説明を結合
- 生成した16万の合成データで、コスト効果の高いトレーニングが可能に
- SMIR-BENCH評価基準で、マルチイメージタスクのパフォーマンス改善を確認

マルチイメージ推論ってなんだかSFみたいでワクワクするよね！しかも合成データでこんなに効果的にできるなんて、未来の技術って感じがする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-07 10:21

- - -

### [Advancing the Understanding of Fine-Grained 3D Forest Structures using Digital Cousins and Simulation-to-Reality: Methods and Datasets](http://arxiv.org/abs/2501.03637)

**デジタル・カズンズとシミュレーションからリアリティへの手法を用いた精密な3D森林構造の理解の向上**

Jing Liu, Duanchu Wang, Haoran Gong, Chongyu Wang, Jihua Zhu, Di Wang

- 森林資源の監視と生態系研究において、空間的意味と構造の理解が重要である
- 大規模なアノテーション付きデータセットの不足が、先進技術の普及を妨げている
- 本研究では、デジタル・カズンズとSim2Realを用いた自動的な合成データ生成と処理フレームワークを提案
- 提案手法は、少量の実世界データで高パフォーマンスを実現し、大規模3D森林解析に貢献するとされる

この研究、かなり革新的だよね！シミュレーションで作ったデータが実世界にどう役立つかを実証しているし、森林解析がどんどん進んでいきそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-07 09:12

- - -

### [Dynamic Authentication and Granularized Authorization with a Cross-Domain Zero Trust Architecture for Federated Learning in Large-Scale IoT Networks](http://arxiv.org/abs/2501.03601)

**大規模IoTネットワークにおける連合学習のためのクロスドメインゼロトラストアーキテクチャによる動的認証と詳細な認可**

Xiaoyu Ma, Fang Fang, Xianbin Wang

- IoTシステムでのクロスドメイン認証と認可はセキュリティ向上を促進するが、新たな効率と安全性の課題を生む。
- ゼロトラストアーキテクチャ（ZTA）は、より詳細かつ堅牢なセキュリティ環境を提供するが、データ交換でプライバシー問題が発生する。
- 提案手法はZTAと分散型連合学習を統合し、IoTネットワークでの動的認証と粒度の細かい認可を実現する。
- 提案手法は低レイテンシーと高スループットを実現し、他の手法と比較して優れた性能をシミュレーションで実証した。

IoTネットワークのセキュリティ強化って大変だけど、クロスドメインとZTAの組み合わせって未来感あるよね。連合学習をうまく使ってるところが、これからのネットワークセキュリティの鍵になるのかなって思った！

**Comment:** 12 pages, 7 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, **投稿日時:** 2025-01-07 07:59

- - -

### [A study on performance limitations in Federated Learning](http://arxiv.org/abs/2501.03477)

**連合学習における性能限界の研究**

Karthik Mohan

- プライバシー懸念が高まり、連合学習が注目される新たな機械学習のパラダイムとして登場
- フェデレーション最適化アルゴリズム、モデル圧縮、差分プライバシーなど多様な研究が進行
- コミュニケーションのボトルネックとデータの非IID性の課題が性能に与える影響を検討
- 基本モデルで課題を特徴付け、性能評価を行い、解決策を議論

連合学習って、端末で学習ができるから安全って感じ！でもコツも多そうで、工夫次第でめっちゃ面白い進化が起こりそうだね。どれくらい早く日常生活に取り入れられるか気になるなぁ！

**Comment:** archive 2021 work

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2025-01-07 02:35

- - -

### [Reading with Intent -- Neutralizing Intent](http://arxiv.org/abs/2501.03475)

**意図を持って読む - 意図の中和**

Benjamin Reichman, Adar Avsian, Larry Heck

- 大規模言語モデル（LLM）のクエリは、指示/質問と文脈の2つに分かれる
- 検索補強生成（RAG）システムは多様なスタイルのテキストにより課題が発生
- 文脈の感情を11種類に変換する合成データ生成アプローチを開発
- 合成データでトレーニングされた感情翻訳モデルが自然界の文脈を中和

感情を理解して対応できるモデルが出来るなんて、人間みたい！ニュアンスのない会話が減るといいな。感情を中和する技術が発展した先、どんな世の中になるのか楽しみ♪



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2025-01-07 02:33

- - -

### [MTRAG: A Multi-Turn Conversational Benchmark for Evaluating Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2501.03468)

**MTRAG: 取得増強生成システムを評価するためのマルチターン会話ベンチマーク**

Yannis Katsis, Sara Rosenthal, Kshitij Fadnis, Chulaka Gunasekara, Young-Suk Lee, Lucian Popa, Vraj Shah, Huaiyu Zhu, Danish Contractor, Marina Danilevsky

- MTRAGは人間生成のマルチターン会話ベンチマークで、多様な次元のRAGパイプラインを評価
- 110の会話を含む842タスクから構成され、4つのドメインで平均7.7ターンの会話
- 合成データとLLM-as-a-Judge評価を行い、最先端のRAGシステムの課題を示す
- 後半のターンや無回答質問、複数ドメインに対応する強力な生成システムの必要性を示す

これはめっちゃ面白そう！RAGの課題をちゃんと検証できる環境が用意されているから、もっと賢い対話システムが期待できそうだね。学んでいく中でリアルな場面に近づけるの、超ワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2025-01-07 01:52

- - -

### [Structure-Preference Enabled Graph Embedding Generation under Differential Privacy](http://arxiv.org/abs/2501.03451)

**差分プライバシーに基づく構造・嗜好可能なグラフ埋め込み生成**

Sen Zhang, Qingqing Ye, Haibo Hu

- グラフ埋め込み生成技術は、低次元ベクトルを生成し、構造的同等性やリンク予測を実現
- 差分プライバシーを用いた既存手法は、大きなノイズ注入による精度低下が問題
- 新手法SE-PrivGEmbは、任意の構造嗜好を保ちつつノイズ耐性メカニズムを用いて劣化を軽減
- スキップグラムの設計により、理論的に構造的特徴の保持が可能で、多くの実験で優位性を示す

SE-PrivGEmbは、単なる理論ではなく実際に効果が感じられる実験結果が魅力的！スキップグラムを活用した工夫も興味深いね。これからのグラフ分析がもっと安全で便利になる未来が楽しみ！

**Comment:** Accepted by ICDE 25

**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.LG, cs.SI, **投稿日時:** 2025-01-07 00:43

- - -

### [Optimizing Value of Learning in Task-Oriented Federated Meta-Learning Systems](http://arxiv.org/abs/2501.03448)

**タスク指向の連合メタ学習システムにおける学習価値の最適化**

Bibo Wu, Fang Fang, Xianbin Wang

- 従来の連合学習は共通のグローバルモデルを配布し、タスク要件に応じたカスタマイズができない
- 連合メタ学習は、共有メタモデルを使ってデバイスがローカルモデルを微調整することで解決する
- 新しい指標「学習の価値（VoL）」を導入し、デバイスごとのトレーニングニーズを評価
- パラメータ化された深層Qネットワーク（PDQN）を用いて非凸問題を解決し、提案手法がベースラインを上回る

学習の価値に着目して、効果的にタスクに応じた個別最適化を目指すなんて面白い！連合メタ学習がどんなふうに進化するのか、これからの展開が楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2025-01-07 00:30

- - -

### [Over-the-Air Fair Federated Learning via Multi-Objective Optimization](http://arxiv.org/abs/2501.03392)

**無線通信による多目的最適化型の公平な連合学習**

Shayan Mohajer Hamidi, Ali Bereyhi, Saba Asaad, H. Vincent Poor

- 連合学習ではクライアント間のデータセット分布の異質性が公平性を損なう可能性がある
- 本研究は、無線通信を活用したフェアな連合学習アルゴリズム（OTA-FFL）を提案
- 多目的最小化問題として連合学習を定式化し、適応的な重み付け係数を計算する手法を導入
- 最適な送信スカラーとノイズ除去スカラーの解析的解を導出し、公平性と頑健性向上を実現

フェアさって理系でも重要なんだね！無線通信使うとか技術の融合でワクワクする！もっと友達とAIの進化について語りたいよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-06 21:16

- - -

### [Privacy-Preserving Smart Contracts for Permissioned Blockchains: A zk-SNARK-Based Recipe Part-1](http://arxiv.org/abs/2501.03391)

**許可制ブロックチェーンのプライバシー保護型スマートコントラクト：zk-SNARKを用いたレシピ Part-1**

Aldenio Burgos, Eduardo Alchieri

- ブロックチェーンの透明性がプライバシー問題を引き起こし、初期の匿名性措置は効果がなかった
- スマートコントラクトのプライバシー解決策にゼロ知識証明や準同型暗号などが使われている
- 従来の手法には機能制限や計算時間の長さ、第三者への信頼などの欠点がある
- zk-SNARKを活用し、プライバシー保護を提供しトークンの取引や新しい取引形態を可能にする

ブロックチェーンの世界でプライバシーを保ちながら非中央集権性を高めるってすごくクールだよね。デジタル取引がもっと安心して使えるようになったら、未来はもっと明るくなる気がする！



**トピック:** [準同型暗号](he), [ゼロ知識証明](zkp), [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2025-01-06 21:16

- - -

### [License Plate Images Generation with Diffusion Models](http://arxiv.org/abs/2501.03374)

**拡散モデルによるナンバープレート画像生成**

Mariia Shpir, Nadiya Shvai, Amir Nakib

- GDPRなどのプライバシー規制で公開データセットが制限される
- 拡散モデルを用いてリアルなナンバープレートを合成
- ウクライナのデータセットで1000枚の合成画像を生成・分析
- 合成データの追加でナンバープレート認識精度が3%向上

拡散モデルを使ってナンバープレートを作れるなんてすごいね！合成データで制度が上がるのもワクワクするし、新しい技術がプライバシー問題を解決できるかもって期待だね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2025-01-06 20:22

- - -

### [FTA-FTL: A Fine-Tuned Aggregation Federated Transfer Learning Scheme for Lithology Microscopic Image Classification](http://arxiv.org/abs/2501.03349)

**FTA-FTL: 微細調整型集約連合転移学習法による岩石学顕微鏡画像分類**

Keyvan RahimiZadeh, Ahmad Taheri, Jan Baumbach, Esmael Makarian, Abbas Dehghani, Bahman Ravaei, Bahman Javadi, Amin Beheshti

- 岩石学の区別は油の貯留層の特徴付けに重要であり、顕微鏡画像の処理が必要
- ディープラーニングは強力だが、大規模なデータセットの収集が困難
- プライバシーの理由からデータ共有が難しく、連合学習が有効である
- FTA-FTLは、精度を中央集約方式と同等まで高める転移学習法を提案

これって、画像分類とかに連合学習をうまく利用してるってことだよね！プライバシーを守りつつ高精度を実現するアイデアは、ほんと未来的でドキドキしちゃう！



**トピック:** [連合学習](fl), [連合転移学習](ftl), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2025-01-06 19:32

- - -

### [The Robustness of Spiking Neural Networks in Federated Learning with Compression Against Non-omniscient Byzantine Attacks](http://arxiv.org/abs/2501.03306)

**圧縮を用いた連合学習におけるスパイキングニューラルネットワークのビザンチン攻撃に対する頑健性**

Manh V. Nguyen, Liang Zhao, Bobin Deng, Shaoen Wu

- スパイキングニューラルネットワーク（SNN）は、推論において優れたエネルギー効率を持つ
- 連合学習（FL）はプライバシーを保護しつつ分散学習を提供し、IoT機器に有用
- ビザンチン攻撃と帯域制限はFL-SNNの収束や学習時間に大きな脅威
- Top-\k{appa}のスパース化を用いることで、帯域使用と非全知的ビザンチン攻撃への耐性が向上

スパイキングニューラルネットワークが何だか可愛い名前だよね。連合学習での非全知の攻撃に対しても強くなるってことは、もっと多くのデバイスで安全に使えるようになっていくのかな〜、すごく楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, cs.LG, **投稿日時:** 2025-01-06 18:09

- - -

### [Rethinking Byzantine Robustness in Federated Recommendation from Sparse Aggregation Perspective](http://arxiv.org/abs/2501.03301)

**疎集合観点から見た連合推奨におけるビザンチン耐性の再考**

Zhongjian Zhang, Mengmei Zhang, Xiao Wang, Lingjuan Lyu, Bo Yan, Junping Du, Chuan Shi

- 連合推奨は、連合学習に基づき、個人データを保ちながら協調モデルを更新する技術である
- 一般的な連合学習とは異なり、部分的なクライアントによって項目の埋め込みを更新する疎集合則が特異
- 現在のビザンチン攻撃研究は、連合推奨の疎集合則を考慮しておらず問題が存在する
- Spattackという新しい攻撃戦略を提案し、少数の悪意あるクライアントで耐性を破壊可能であることを示す

この研究、未来の連合学習システムにとってかなり重要な示唆がありそう！悪意あるクライアントをどう防ぐかって、これからの大きな課題になりそうだね。しかも、この攻撃戦略はすごく効果的みたいなんだ！

**Comment:** accepted by AAAI 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.DC, cs.LG, **投稿日時:** 2025-01-06 15:19

- - -

### [Multi-Modal One-Shot Federated Ensemble Learning for Medical Data with Vision Large Language Model](http://arxiv.org/abs/2501.03292)

**医療データのためのビジョン大規模言語モデルを用いたマルチモーダルワンショット連合学習**

Naibo Wang, Yuchen Deng, Shichen Fan, Jianwei Yin, See-Kiong Ng

- 連合学習は医療分野で注目されているが、従来の方法は通信負担が大きい
- ワンショット連合学習は1回の通信でモデル訓練と集約を行い、通信コストを削減
- FedMMEはマルチモーダルデータを使い、医療画像分析で高精度な診断を可能にする
- 4つのデータセットで既存手法を超える性能を実証し、RSNAデータセットでは17.5%以上の精度向上

マルチモーダル学習で医療データの分析精度を上げるのすごいね！未来の医療現場がもっと効率的になる感じがするし、ワンショットでの連合学習だなんて、まるで魔法みたい！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-06 08:36
