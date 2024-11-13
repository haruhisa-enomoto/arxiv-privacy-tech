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

更新: 2024-11-13T04:22:08.679560

- - -

### [A Zero-Knowledge PCP Theorem](http://arxiv.org/abs/2411.07972)

**ゼロ知識PCP定理**

Tom Gur, Jack O'Connor, Nicholas Spooner

- 任意の多項式q*に対し、NPのための定数クエリ非適応PCPが存在する
- 任意の多項式時間の敵対者に対し、完全ゼロ知識の指数サイズ定数クエリPCPを構築
- これは最適パーフェクトゼロ知識PCPの最近の構築を改善
- 1997年のKilianらの研究をさらに発展させたもの

ゼロ知識証明の最前線って感じ！新しい構築方法が既存のものを改善してるなんて、面白そうだよね。こんな研究が進むと、将来的にセキュアなシステムがもっとたくさんできそう！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CC, cs.CR, **投稿日時:** 2024-11-12 17:54

- - -

### [On the Convergence of Continual Federated Learning Using Incrementally Aggregated Gradients](http://arxiv.org/abs/2411.07959)

**増分的に集約された勾配を用いた継続的連合学習の収束について**

Satish Kumar Keshri, Nazreen Shah, Ranjitha Prasad

- 継続的連合学習（CFL）は、ストリーミングデータから学び効率、プライバシー、スケーラビリティを向上させる手法である
- CFLの課題は、古いタスクの精度が新しいタスクの学習で低下する、いわゆるグローバル破滅的忘却に対処することである
- 提案手法C-FLAGは、メモリ上のエッジベースの勾配更新と現在のデータに基づく集約勾配からなる新しい再生メモリベースの連合戦略である
- C-FLAGはタスク間での破滅的忘却を最小化し、収束速度$O(1/\sqrt{T})$を達成して多くの最先端手法を上回る性能を示した

この研究おもしろそう！C-FLAGでタスクを忘れないっていう発想、新しいかも！AIがもっと賢くなる予感がするね。しかも、プライバシーを守りながら学習するって期待できる～！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-11-12 17:36

- - -

### [A Stochastic Optimization Framework for Private and Fair Learning From Decentralized Data](http://arxiv.org/abs/2411.07889)

**プライバシーと公正さを両立した分散データからの学習のための確率的最適化フレームワーク**

Devansh Gupta, A. S. Poornash, Andrew Lowy, Meisam Razaviyayn

- 連合学習モデルのプライバシーと公正性の課題に対抗するアルゴリズムを開発
- 各シロデータの記録レベル差分プライバシー（ISRL-DP）を満たす
- 公正性として、人口平等や均等的成果を促進できる
- 以前は必要だった強凸性なしに、緩やかな滑らかさでの収束を保証

データのプライバシーも守りつつ、公正な結果を導くなんてすごくない？これ、社会にめちゃ貢献できそうな技術だよね！新しい方法でシロデータを守るなんて、聞くだけでワクワクしちゃう！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-12 15:51

- - -

### [Federated Learning for Discrete Optimal Transport with Large Population under Incomplete Information](http://arxiv.org/abs/2411.07841)

**連合学習を用いた大規模な不完全情報下での離散的最適輸送**

Navpreet Kaur, Juntao Chen, Yingdong Lu

- 最適輸送は資源の効率的な配分を目指すが、大規模で異質な集団においてスケーリングが難しい
- 既知のタイプ分布では、資源配分を最適化するための分散アルゴリズムを提案
- タイプ分布が未知の場合、プライバシーを保った連合学習アプローチを開発
- ケーススタディによって提案アルゴリズムの性能を評価し効果を実証

連合学習で巨大で多様な集団を効率的に扱うチャレンジ、面白そう！プライバシーを守りながらの最適化だから、実用的な応用も期待できるね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, **投稿日時:** 2024-11-12 14:46

- - -

### [Efficient Federated Finetuning of Tiny Transformers with Resource-Constrained Devices](http://arxiv.org/abs/2411.07826)

**リソースが限られたデバイスでの小型トランスフォーマーの効率的な連合微調整**

Kilian Pfeiffer, Mohamed Aboelenien Ahmed, Ramin Khalili, Jörg Henkel

- 大規模言語モデルは多くのデータと高いリソースを要求するが、リソースが限られた環境では困難がある
- LoRAは連合学習でパラメータ効率は良いが、メモリとFLOPsの効率が悪いことがわかった
- 新しい層の微調整スキームは、リソース制約のあるデバイスでも事前訓練されたNNを活用可能にする
- 提案手法は現在の最先端技術を超え、同質または異質な計算とメモリ制約において高い精度を達成した

デバイスの制約がある中でも、しっかりと先端技術を活かしつつ効率を高める工夫が面白そう！新しい微調整スキーム、ぜひ試してみたいね。連合学習の世界もますます広がりそうで楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-11-12 14:22

- - -

### [Dual-Criterion Model Aggregation in Federated Learning: Balancing Data Quantity and Quality](http://arxiv.org/abs/2411.07816)

**連合学習におけるデュアル基準モデル集約: データ量と質のバランス**

Haizhou Zhang, Xianjia Yu, Tomi Westerlund

- 連合学習ではクライアントのデータを交換せずにモデルを共有する手法が主流
- 従来の集約アルゴリズムはデータを量的に評価しがちで、質的な違いを無視
- 本研究は、データ量と質を考慮したデュアル基準の集約アルゴリズムを提案
- 提案手法はCIFAR-10などで既存の最先端手法を上回る性能を示した

これって、データの量だけじゃなくて質もバランスよく考えるのがポイントなんだね！クライアントのデータがバラバラでもちゃんと貢献できるのが面白いな〜。

**Comment:** 6 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-12 14:09

- - -

### [Federated Low-Rank Adaptation with Differential Privacy over Wireless Networks](http://arxiv.org/abs/2411.07806)

**差分プライバシーを用いた無線ネットワーク上の連合低ランク適応**

Tianqu Kang, Zixin Wang, Hengtao He, Jun Zhang, Shenghui Song, Khaled B. Letaief

- 大規模モデルの連合学習はプライバシー保護の問題を軽減する。
- LoRAの利用で計算負荷を減らし効率的にモデル微調整が可能。
- 分割されたFMがデバイス間で共有されプライバシー攻撃の懸念。
- 無線チャンネルノイズを利用し差分プライバシーを実現。

差分プライバシーの工夫が面白いね！通信の「ノイズ」を役立てちゃうなんて発想がユニークだし、これは革新的な無線通信のプライバシー保護の手法になる予感！

**Comment:** 6 pages, 3 figures, submitted to IEEE ICC 2025

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, eess.SP, **投稿日時:** 2024-11-12 14:01

- - -

### [ALANINE: A Novel Decentralized Personalized Federated Learning For Heterogeneous LEO Satellite Constellation](http://arxiv.org/abs/2411.07752)

**ALANINE: 異種LEO衛星コンステレーション向けの新たな分散個別連合学習**

Liang Zhao, Shenglin Geng, Xiongyan Tang, Ammar Hawbani, Yunhe Sun, Lexi Xu, Daniele Tarchi

- 最近のLEO衛星コンステレーションは、通信やナビゲーション、リモートセンシングなど多様な機能の統合で成長。
- データの多様性や異なる画像解像度の不一致が、衛星間の効率的な共同計算の妨げになっている。
- ALANINEは分散型FLで衛星画像超解像を行い、個別化PFLにより各衛星データの特性に対応。
- モデル剪定技術を活用し、モデルの複雑さと伝送効率を最適化、データ処理の精度向上を実現。

LEO衛星の世界ってなんか未来っぽくてワクワクするね！データの個別化も、宇宙での通信がもっと身近になりそうな予感！🌟

**Comment:** 14 pages, 8 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-11-12 12:23

- - -

### [Maritime Search and Rescue Missions with Aerial Images: A Survey](http://arxiv.org/abs/2411.07649)

**航空画像を用いた海上捜索救助ミッションの調査**

Juan P. Martinez-Esteso, Francisco J. Castellanos, Jorge Calvo-Zaragoza, Antonio Javier Gallego

- 海上捜索救助の迅速な対応が重要で、生存率に影響を与える
- 無人航空機とカメラが海上捜索で効率的な人物検出を可能に
- ディープラーニング利用が10年で進展し、自動検出技術が発展
- 合成データを用いた幅広いシナリオ適用がデータ収集の課題に対処

未来の海難救助がどんどん進化してるんだね！無人航空機とか映画みたいですごいし、技術が使えれば多くの命を救えるんじゃないかなってワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-12 08:57

- - -

### [Collaborative and Federated Black-box Optimization: A Bayesian Optimization Perspective](http://arxiv.org/abs/2411.07523)

**協調型および連合型ブラックボックス最適化：ベイズ最適化の視点**

Raed Al Kontar

- 連合型ブラックボックス最適化における分散実験、異質性、プライバシーが課題
- グローバル、ローカル、予測の3つのフレームワークを提案し、課題に対応
- ローカルフレームワークでは最小限の情報共有で意思決定を支援
- ベイズ最適化を用い、記述的・予測的から処方的な学習への移行を目指す

ベイズ最適化を使って連合学習をもっとステキな方向に持っていくのってワクワクするね。これが進化したら私たちの日常でも活用されるかもしれないよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-11-12 03:47

- - -

### [Privacy-Preserving Verifiable Neural Network Inference Service](http://arxiv.org/abs/2411.07468)

**プライバシー保護可能な検証可能ニューラルネットワーク推論サービス**

Arman Riasi, Jorge Guajardo, Thang Hoang

- MLaaSは便利だが、顧客データのプライバシー漏洩と信頼性が課題
- vPINは部分準同型暗号と知識非対話型証明技術を使用し、データのプライバシーと検証性を両立
- 証明回路の最適化を通じ、効率や性能を向上
- 標準データセットでの実験で、vPINは証明時間や検証時間で高効率を達成

プライバシーと信頼性を両立させたこの技術、これからのMLaaSのスタンダードになりそうじゃない？性能とプライバシーを犠牲にしなくて良さそうで、ワクワクするね！

**Comment:** This paper is to appear at the Annual Computer Security Applications   Conference (ACSAC) 2024. The source code for our implementation can be found   at $\href{https://github.com/vt-asaplab/vPIN}{github.com/vt-asaplab/vPIN}$

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-11-12 01:09

- - -

### [Feature-Space Semantic Invariance: Enhanced OOD Detection for Open-Set Domain Generalization](http://arxiv.org/abs/2411.07392)

**特徴空間における意味的変動の抑制：オープンセット領域一般化におけるOOD検出の強化**

Haoliang Wang, Chen Zhao, Feng Chen

- オープンセット領域一般化は未見のドメインとクラスを扱う課題に焦点を当てる
- 特徴空間における意味的一貫性を保つFSIを導入し、OOD検出の精度を向上
- 生成モデルで合成データを作り出し、モデルの頑健性を強化する
- 初期実験でAUROCが最大18.9%向上し、分布内分類精度も大幅に向上

未知のクラスとドメインを一緒に扱えるなんてすごいね！新しいデータを合成してモデルを強化するなんて、次世代のAIっぽくてワクワクする！

**Comment:** IEEE BigData 2024, Ph.D. Forum

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-11-11 21:51

- - -

### [Federated Learning Client Pruning for Noisy Labels](http://arxiv.org/abs/2411.07391)

**雑音ラベルのための連合学習クライアントプルーニング**

Mahdi Morafah, Hojin Chang, Chen Chen, Bill Lin

- 連合学習はデータプライバシーを保持しつつモデルをトレーニングするが、ノイズの多いラベルが課題
- 既存手法はラベル修正や堅牢なトレーニングだが、高ノイズ下で効果が限定的
- ClipFLはノイズクライアントを識別し除外する新たなフレームワークでNCSを用いる
- ClipFLは雑音クライアント識別、性能向上、速い収束、通信コスト削減を達成

ノイズがある中でも効率的に連合学習できるのってすっごく重要だよねー。クライアントのプルーニングでより正確に学べるのは、未来のAIを賢くしてくれそうな気がする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CV, cs.DC, **投稿日時:** 2024-11-11 21:46

- - -

### [SynRL: Aligning Synthetic Clinical Trial Data with Human-preferred Clinical Endpoints Using Reinforcement Learning](http://arxiv.org/abs/2411.07317)

**SynRL: 強化学習を用いた人間の好む臨床エンドポイントに合致する合成臨床試験データの整合**

Trisha Das, Zifeng Wang, Afrah Shafquat, Mandis Beigi, Jason Mezey, Jimeng Sun

- 臨床試験の患者記録共有はプライバシーと規制の問題で困難
- 既存の合成データ生成法は臨床結果の特性を考慮していない
- SynRLは強化学習でデータ生成をカスタマイズし品質を向上
- SynRLは多様な合成データ生成法をカスタマイズ可能な汎用フレームワーク

SynRLって、実際の患者データを使わなくてもよい方向性を示してくれる感じが素敵だね！プライバシーを守りながら研究を進められるところが未来を感じるよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-11 19:19
