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

更新: 2024-06-12T04:19:54.904091

- - -

### [iMESA: Incremental Distributed Optimization for Collaborative Simultaneous Localization and Mapping](http://arxiv.org/abs/2406.07371)

**インクリメント分散最適化による協調同時自己位置推定とマッピング (iMESA)**

Daniel McGann, Michael Kaess

- C-SLAMにおける新しいインクリメンタル分散バックエンドアルゴリズムを提案
- ロボットチームがオンライン実行時制約内で正確な状態推定を実現
- ロボット間の疎なペア通信だけでリアルタイム推定が可能
- 実データと合成データで広範に評価し、最新技術と比較して優れた性能を示す

この論文、ロボットが少ない通信で協力しながら動くのがすごいと思う！どの場所でもすぐに使えそうだね。

**Comment:** Accepted to Robotic Science and Systems (RSS) 2024 in Delft,   Netherlands

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-06-11 15:40

- - -

### [Minimizing Energy Costs in Deep Learning Model Training: The Gaussian Sampling Approach](http://arxiv.org/abs/2406.07332)

**ディープラーニングモデル訓練におけるエネルギーコスト削減：ガウスサンプリングアプローチ**

Challapalli Phanindra Revanth, Sumohana S. Channappayya, C Krishna Mohan

- 逆伝搬法による損失勾配の計算は多くのエネルギーを消費
- GradSampと呼ばれる方法で、ガウス分布から勾配更新をサンプリング
- ガウス「ノイズ」でモデルパラメータを周期的またはランダムに更新
- 画像分類などのさまざまなタスクで、エネルギー削減と性能維持を実証

新しい勾配更新方法が省エネに繋がるなんて、環境にも優しいね！実験で効果が見られたから、実用化も期待できそうだね～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-11 15:01

- - -

### [Realistic Data Generation for 6D Pose Estimation of Surgical Instruments](http://arxiv.org/abs/2406.07328)

**外科用器具の6Dポーズ推定のための現実的データ生成**

Juan Antonio Barragan, Jintan Zhang, Haoying Zhou, Adnan Munawar, Peter Kazanzides

- 外科ロボットの自動化は患者の安全と手術の効率を向上させるが、堅牢な認識アルゴリズムが必要で困難
- 6Dポーズ推定には大量のアノテーションデータが必要であり、合成データの利用が提案されている
- 外科領域では商業用グラフィックソフトの限られた機能により、現実的な器具-組織の相互作用を生成することが難しい
- 改善されたシミュレーション環境と自動データ生成パイプラインにより、多様な6Dポーズデータセットが生成可能

手術ロボットのこの新しいシミュレーション環境、めっちゃ役に立ちそう！特に、組織とのリアルな相互作用をもっとリアルに再現してくれるのがすごいっ！

**Comment:** 6 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.LG, **投稿日時:** 2024-06-11 14:59

- - -

### [Merging Improves Self-Critique Against Jailbreak Attacks](http://arxiv.org/abs/2406.07188)

**マージによる自自己批判の強化で対Jailbreak攻撃が改善**

Victor Gallego

- 大規模言語モデル(LLM)の対逆操作耐性は依然として課題
- LLMの自己批判能力を強化し、合成データでさらに微調整する手法を提案
- 外部の批判モデルを追加し元のモデルとマージすることで、自己批判能力を向上
- 手法の結果、対敵攻撃成功率が大幅に減少し、有望な防御機構を提供

合成データを使ってさらに強くなるなんて面白そうね！未来の言語モデル、今よりもっと賢くなりそうな予感！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-06-11 12:01

- - -

### [DecoR: Deconfounding Time Series with Robust Regression](http://arxiv.org/abs/2406.07005)

**DecoR: ロバスト回帰による時系列データの潜在交絡調整**

Felix Schur, Jonas Peters

- 未観測の交絡因子による時系列データの因果推定問題に焦点を当てる
- 周波数領域での逆コンフェウンド問題を対戦型異常値問題としてフレーム化
- ロバスト線形回帰を用いて因果効果を推定する新しいアプローチ、Deconfounding by Robust regression (DecoR) を導入
- 合成データを用いた実験により、モデルのミススペシフィケーションにも強いロバスト性を示す

周波数領域を使った考え方がちょっと独特で面白そう！実験結果もしっかりしてそうだし、実用性がありそうだね。

**Comment:** 27 pages, 7 figures

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, 62F12 (Primary) 62F35 (Secondary), I.2.0, **投稿日時:** 2024-06-11 06:59

- - -

### [Pseudo-Entanglement is Necessary for EFI Pairs](http://arxiv.org/abs/2406.06881)

**EFIペアには疑似絡み合いが必要である**

Manuel Goulão, David Elkouss

- 最も弱い計算仮定の候補であるEFIペアは、疑似絡み合いの存在を示唆
- EFIペアのみから新しい疑似絡み合い量子状態のファミリーを構築
- 疑似絡み合いが存在しないならば、大多数の暗号技術も存在しない
- 疑似絡み合いは計算暗号理論の物理現象とのつながりを強化

疑似絡み合いが暗号技術の基盤になるかもしれないなんて、新しい時代が来る予感がするね！これで物理の世界とコンピュータの世界がもっと深く結びつくなんてワクワクしちゃう！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** quant-ph, cs.CR, **投稿日時:** 2024-06-11 01:44

- - -

### [Fast White-Box Adversarial Streaming Without a Random Oracle](http://arxiv.org/abs/2406.06808)

**ランダムオラクルを用いない高速ホワイトボックスの敵対的ストリーミング**

Ying Feng, Aayush Jain, David P. Woodruff

- 敵対的に強いホワイトボックスモデルで、過去のランダムコインとパラメータにアクセス可能
- スパース回復問題において準最適解を構築し、他の問題にも適用可能
- 従来の研究はランダムオラクルが必要で更新時間が長い欠点がある
- 準同型暗号を用いたポリログ計算時間でランダムオラクル不要な解決策を提案

敵対的な状況でもランダムオラクルなしで処理できる方法ってすごくない？準同型暗号とかもカッコいいし、いろんな応用ができそうで夢が広がるね。

**Comment:** ICML 2024

**トピック:** [準同型暗号](he), **カテゴリ:** cs.DS, cs.LG, **投稿日時:** 2024-06-10 21:23

- - -

### [Scalable Private Search with Wally](http://arxiv.org/abs/2406.06761)

**スケーラブルなプライベートサーチシステム「Wally」**

Hilal Asi, Fabian Boemer, Nicholas Genise, Muhammad Haris Mughees, Tabitha Ogilvie, Rehan Rishi, Guy N. Rothblum, Kunal Talwar, Karl Tarbe, Ruiyu Zhu, Marco Zuliani

- Wallyは意味検索とキーワード検索を効率的にサポートし、大規模なデータベースで優れたパフォーマンスを発揮
- 기존의プライベートサーチシステムにおける高コストな暗号操作の問題を解決
- 各クライアントが少数のフェイククエリを追加し、匿名ネットワーク経由でランダムなタイミングで送信する手法を採用
- $(\epsilon, \delta)$-差分プライバシー保証により、強いプライバシー保護を実現し、スケーラビリティを大幅に向上

Wallyのアイデア、ちょっと天才的じゃない！？フェイククエリとか工夫がすごいし、大量のリクエストにも楽に対応できるなんて未来感あるよね。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-06-10 19:41

- - -

### [Optimal Federated Learning for Nonparametric Regression with Heterogeneous Distributed Differential Privacy Constraints](http://arxiv.org/abs/2406.06755)

**異質な分散差分プライバシー制約を持つ非パラメトリック回帰のための最適な連合学習**

T. Tony Cai, Abhinav Chakraborty, Lasse Vuursteen

- サーバごとに異なる差分プライバシー制約とサンプルサイズの非均質な環境での連合学習を研究
- ベゾフ空間の上での最適収束率を確立し、グローバルおよびポイントワイズ推定を検討
- 分散プライバシー保護推定量を提案し、そのリスク特性を調査
- プライバシーバジェットとデータ分散による損失間のトレードオフを解析

異なるサーバでプライバシーを保持しながら最適な推定を行う方法、めっちゃ興味深い！特にポイントワイズ推定とグローバル推定の違いがどうなるのか知りたいな。

**Comment:** 49 pages total, consisting of an article (24 pages) and a supplement   (25 pages)

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** math.ST, cs.LG, stat.ML, stat.TH, 62G08, 62C20, 68P27, 62F30,, **投稿日時:** 2024-06-10 19:34

- - -

### [Federated Nonparametric Hypothesis Testing with Differential Privacy Constraints: Optimal Rates and Adaptive Tests](http://arxiv.org/abs/2406.06749)

**差分プライバシー制約下における連合ノンパラメトリック仮説検定：最適レートと適応的テスト**

T. Tony Cai, Abhinav Chakraborty, Lasse Vuursteen

- 差分プライバシー制約下での白色雑音ドリフトモデルにおける連合ノンパラメトリック適合度検定を研究
- 最適レートを指数関数的な因子まで一致させる下界と上界を確立し、テスト問題の難しさを評価
- 共有ランダムネスにアクセスできる分散型のワンショットプロトコルが、それなしよりも優れている現象を発見
- 未知の規則性パラメータに適応し、差分プライバシー制約を維持したまま追加コストを最小限に抑えるデータ駆動型テスト手法を構築

共有ランダムネスをうまく利用することで効率が上がるなんて、すごく面白いね！これからのプライバシー保護技術がもっと進化していくのが楽しみ～！

**Comment:** 77 pages total; consisting of a main article (28 pages) and   supplement (49 pages)

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** math.ST, cs.LG, stat.ML, stat.TH, 62G10, 62C20, 68P27, 62F30, **投稿日時:** 2024-06-10 19:25

- - -

### [PatchRefiner: Leveraging Synthetic Data for Real-Domain High-Resolution Monocular Metric Depth Estimation](http://arxiv.org/abs/2406.06679)

**PatchRefiner：高解像度単眼距離推定のための合成データ活用**

Zhenyu Li, Shariq Farooq Bhat, Peter Wonka

- PatchRefinerはタイルベース手法を採用し、高解像度の距離推定を改良プロセスとして再構成
- 合成データを利用した疑似ラベリング戦略により、被写体の細部を正確に捉える
- Detail and Scale Disentangling (DSD)ロスにより、細部の精度とスケールの正確さを強化
- Unreal4KStereoデータセットで既存のベンチマークを18.1%上回る性能を発揮

細部まで精度を追及しているのがすごいね！特にDSDロスってどんな感じなんだろう、気になるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-10 18:00

- - -

### [SecureNet: A Comparative Study of DeBERTa and Large Language Models for Phishing Detection](http://arxiv.org/abs/2406.06663)

**SecureNet: DeBERTaと大型言語モデルを用いたフィッシング検出の比較研究**

Sakshi Mahendru, Tejul Pandit

- フィッシング攻撃の脅威を識別するため、LLMsの性能を評価し、DeBERTa V3モデルと比較
- 公共データセットを用いて、DeBERTaとLLMsのポテンシャルと限界を体系的に評価
- LLMsが生成する説得力のあるフィッシングメールの困難さと、DeBERTaのトレーニングフェーズの課題
- DeBERTaが最も効果的で、95.17%の再現率を達成し、GPT-4は91.04%の再現率に続いた

おもしろいね！DeBERTaの方がLLMsよりちょっとだけ優れているなんて、新しい発見がいっぱいだよね。フィッシングメールの進化にも注目だね！

**Comment:** Preprint. 10 pages, Accepted in IEEE 7th International Conference on   Big Data and Artificial Intelligence (BDAI 2024)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.CL, cs.LG, **投稿日時:** 2024-06-10 13:13

- - -

### [Fed-Sophia: A Communication-Efficient Second-Order Federated Learning Algorithm](http://arxiv.org/abs/2406.06655)

**Fed-Sophia: 通信効率の高い二次連合学習アルゴリズム**

Ahmed Elbakary, Chaouki Ben Issaid, Mohammad Shehab, Karim Seddik, Tamer ElBatt, Mehdi Bennis

- 連合学習は複数のデバイスがパラメータサーバーを介して局所更新を共有し学習する方法
- 二次導関数情報は収束を早めるために重要であるが、それを活用する新たな方法を提案
- 提案手法であるFed-Sophiaは、勾配の加重移動平均とクリッピング操作を組み合わせる
- 提案手法は、数値評価において従来の一次および二次手法と比較して優越性、堅牢性、スケーラビリティを示す

二次導関数の力ってやっぱりすごいんだね！この方法で連合学習がもっと速くなるのかもね。

**Comment:** ICC 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-06-10 09:57

- - -

### [1-D CNN-Based Online Signature Verification with Federated Learning](http://arxiv.org/abs/2406.06597)

**連合学習を用いた1次元CNNベースのオンライン署名認証**

Lingfeng Zhang, Yuheng Guo, Yepeng Ding, Hiroyuki Sato

- オンライン署名認証は、セキュリティインフラで重要な役割を果たす
- 従来のモデルはトレーニング時にデータプライバシーの大きなリスクを伴う
- 1次元CNNと連合学習を活用し、データプライバシーの懸念を軽減する新たな枠組みを提案
- 提案した枠組みは、計算リソースの最小化、初期データでの効果向上、優れたスケーラビリティを示す

署名認証ってセキュリティにめっちゃ大事なんだね。連合学習でプライバシー保護しながらも高い精度を保つなんて、未来の標準技術になるかも！

**Comment:** 8 pages, 11 figures, 1 table

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.CV, cs.LG, **投稿日時:** 2024-06-06 08:27
