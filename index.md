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

更新: 2024-12-26T04:21:44.592001

- - -

### [FedVCK: Non-IID Robust and Communication-Efficient Federated Learning via Valuable Condensed Knowledge for Medical Image Analysis](http://arxiv.org/abs/2412.18557)

**FedVCK: 医学画像解析のための貴重な凝縮知識を活用した非独立同分布に強く通信効率の良い連合学習**

Guochen Yan, Luyuan Xie, Xinyi Gao, Wentao Zhang, Qingni Shen, Yuejian Fang, Zhonghai Wu

- 医療機関間の連携においてデータは非独立同分布であり、クライアントドリフトや成績低下を招く
- 提案するFedVCKはモデルが導く最も必要な知識を選び、通信コストを抑えつつ非IID問題を効果的に解決
- クライアント側で知識を凝縮した小さなデータセットを作成し、不要な通信を最小限に抑える
- サーバー側での関係的教師付きコントラスト学習により、モデル更新のための監視信号を強化

貴重な知識を凝縮することで通信頻度を抑えつつ、性能向上を目指すアイデアがすごいね！医療現場でのデータ共有のハードルをうまくクリアしてるのが興味深いなぁ。

**Comment:** Accepted by AAAI 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-24 17:20

- - -

### [HTR-JAND: Handwritten Text Recognition with Joint Attention Network and Knowledge Distillation](http://arxiv.org/abs/2412.18524)

**HTR-JAND: 手書き文字認識における共同注意ネットワークと知識蒸留**

Mohammed Hamdan, Abderrahmane Rahiche, Mohamed Cheriet

- 手書き文字認識（HTR）は、歴史的文書の多様な書式や劣化した品質に対応するのが難しい。
- HTR-JANDは、特徴抽出と知識蒸留を組み合わせる効率的なHTRフレームワークを提案。
- マルチヘッド自己注意とプロクシマ注意が結合した注意メカニズムで強力なシーケンスモデリングを実現。
- HTR-JANDフレームワークで、モデル圧縮しつつ認識精度を保ち、新たなCERを達成。

手書き文字認識って歴史的文書には結構難しそうだけど、技術進化ってすごいよね！この新しいアーキテクチャで効率性も精度もアップするなんて、未来の研究が楽しみだな！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-24 16:08

- - -

### [Subsampling, aligning, and averaging to find circular coordinates in recurrent time series](http://arxiv.org/abs/2412.18515)

**再帰的時系列における円形座標を見つけるための部分サンプリング、整列、平均化**

Andrew J. Blumberg, Mathieu Carrière, Jun Hou Fung, Michael A. Mandell

- データの再帰性に基づく円形座標を見つける新アルゴリズムを提案
- 不均一なサンプリング密度の補正技術を導入し、座標のロバスト性を向上
- 部分サンプルの整列と平均化により、他の方法より効率的な手法を提供
- 合成データとニューロン活動の記録を使い技術を検証し、特定の行動に対応する脳状態をモデル化

この研究、めちゃくちゃ面白そう！脳の状態が特定の行動にどうつながっているのか、C. elegansを通じて見える化しちゃうのがすごいよね。再帰データでの新手法が他の分野でも活用できるかも？！



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.CG, cs.LG, math.AT, **投稿日時:** 2024-12-24 15:52

- - -

### [FedGIG: Graph Inversion from Gradient in Federated Learning](http://arxiv.org/abs/2412.18513)

**FedGIG: 連合学習における勾配からのグラフ逆推論**

Tianzhe Xiao, Yichen Li, Yining Qi, Haozhao Wang, Ruixuan Li

- 連合学習は勾配逆推論攻撃に脆弱で、プライベートデータが漏れる可能性がある
- 従来の手法は画像やテキスト向けで、グラフデータには直接適用できない
- FedGIGはグラフ構造データに特化した新しい逆推論手法である
- テストではFedGIGが既存の手法よりも高い精度を持つことを確認した

連合学習でのグラフデータのプライバシーを守るための技術なんて新鮮！グラフ構造特有のデータ扱いに特化しているところが特に興味深いなぁ。どんな応用ができるのかワクワクするね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-24 15:52

- - -

### [An Empirical Analysis of Federated Learning Models Subject to Label-Flipping Adversarial Attack](http://arxiv.org/abs/2412.18507)

**ラベルフリップ攻撃を受ける連合学習モデルの実証的分析**

Kunal Bhatnagar, Sagana Chattanathan, Angela Dang, Bhargav Eranki, Ronnit Rana, Charan Sridhar, Siddharth Vedam, Angie Yao, Mark Stamp

- 連合学習モデルに対するラベルフリップ攻撃を実証的に分析
- MLR、SVC、MLP、CNN、RNN、ランダムフォレスト、XGBoost、LSTMを用いて実験
- 10から100の連合クライアント、ラベルの変更率10%から100%で攻撃をシミュレート
- モデルによって対抗能力が異なり実用的な影響を考察

ラベルフリップ攻撃がどのモデルにどんな影響を与えるのか、リアルに分析しているのが面白いね。同じアルゴリズムでもこれだけ違いがあるのなら、攻撃対策もさらに必要だなって思う！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-24 15:47

- - -

### [GeFL: Model-Agnostic Federated Learning with Generative Models](http://arxiv.org/abs/2412.18460)

**GeFL: ジェネレーティブモデルを用いたモデルアグノスティックな連合学習**

Honggu Kang, Seohyeon Cha, Joonhyuk Kang

- 連合学習はユーザープライバシーを守る分散学習の有望な手法
- 大規模モデルは一部のユーザーには負担で、異なる計算能力のために異種モデルが必要
- ジェネレーティブモデルを用いるGeFLは異種モデル間の知識統合を図る
- GeFL-Fは特徴生成モデルでプライバシーとスケーラビリティを改善する

連合学習って未来的だよね！いろんな能力のデバイスが一緒に学習できるって、まるでチームプレイみたいでおもしろいなぁ。技術がもっと進むと、セキュリティもさらに向上して安心かな。

**Comment:** 20 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-24 14:39

- - -

### [GUI Testing Arena: A Unified Benchmark for Advancing Autonomous GUI Testing Agent](http://arxiv.org/abs/2412.18426)

**GUIテストアリーナ: 自律的GUIテストエージェントを進化させるための統一ベンチマーク**

Kangjia Zhao, Jiahui Song, Leigang Sha, Haozhan Shen, Zhi Chen, Tiancheng Zhao, Xiubo Liang, Jianwei Yin

- 現状のGUIエージェント研究は自動化に焦点を当て、様々なGUIシナリオで制限がある
- GUI自動テスト環境GTArenaを提案し、一貫した操作を可能にする標準化された環境を提供
- テストを3つのサブタスクに分け、実際のアプリや合成データを用いて包括的評価を実施
- 現存の先進的モデルでも全サブタスクで高性能を発揮できず、実用性に大きなギャップがある

新しいGUIエージェントの開発に向けての基準ができる感じがするよね！特に、今後の技術の進化がどこに向かうのか見える指針になるのがワクワクする♪



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-12-24 13:41

- - -

### [Addressing Spatial-Temporal Data Heterogeneity in Federated Continual Learning via Tail Anchor](http://arxiv.org/abs/2412.18355)

**連合継続学習における時空間データの不均一性への対応**

Hao Yu, Xin Yang, Le Zhang, Hanlin Gu, Tianrui Li, Lixin Fan, Qiang Yang

- 連合継続学習は、各クライアントがタスクストリームから知識を継続的に更新する手法
- クライアント間の空間データの不均一性とタスク間の時間データの不均一性が課題
- Federated Tail Anchor (FedTA)を提案し、モデルのパラメータと出力の忘却を克服
- 入力強化や選択的入力知識融合などを含むFedTAが、既存手法より優れた性能を実証

連合学習の課題を解決する新しい手法が提案されてて面白そう！時空間の不均一性をどう克服するのかっていう技術が、実用に向けた大きな一歩になりそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-12-24 11:35

- - -

### [Efficient Long Context Language Model Retrieval with Compression](http://arxiv.org/abs/2412.18232)

**効率的な長文コンテキスト言語モデルの圧縮による情報検索**

Minju Seo, Jinheon Baek, Seongyun Lee, Sung Ju Hwang

- 長文コンテキスト言語モデル（LCLM）は、多量の情報を一度に処理し、伝統的な検索手法を超える可能性を持つ
- 多数のパッセージを処理するには計算コストが高く、推論時も時間がかかる
- パッセージを圧縮する新手法を提案し、検索性能を最大化しつつ長さを削減
- 9つのデータセット実験で、圧縮サイズを1.91倍にしながら検索性能を6%向上

データを圧縮しても情報がしっかり取り出せるってすごいね！これからは、もっと早く情報が見つかるようになるかな？圧縮の技術がこんなに効くとは思わなかった！



**トピック:** [合成データ](sd), **カテゴリ:** cs.IR, **投稿日時:** 2024-12-24 07:30

- - -

### [KunServe: Elastic and Efficient Large Language Model Serving with Parameter-centric Memory Management](http://arxiv.org/abs/2412.18169)

**KunServe: パラメータ中心メモリ管理による弾性で効率的な大規模言語モデルのサービス提供**

Rongxin Cheng, Yifan Peng, Yuxin Lai, Xingda Wei, Rong Chen, Haibo Chen

- 大規模言語モデルの状態保持は、高負荷時にGPUメモリを圧迫し、遅延を引き起こす
- 既存のKVCache中心のアプローチは、リクエストの性能とのトレードオフがあり、SLOの違反を招く
- パラメータを選択的に削除し、リクエスト用のメモリを確保する方法を提案
- 新しいリモートアテンションメカニズムで、他のGPUからメモリを借りることで高効率なサービスを実現

このアプローチは、メモリ管理を効果的にしながらも、リクエストの処理をスムーズにするなんて、すごいね！これからの多様なリクエストに対しても強力な武器になりそうだなぁ。



**トピック:** [TEE](tee), **カテゴリ:** cs.DC, cs.AI, **投稿日時:** 2024-12-24 05:07

- - -

### [AIGT: AI Generative Table Based on Prompt](http://arxiv.org/abs/2412.18111)

**AIGT: プロンプトに基づくAI生成表**

Mingming Zhang, Zhiqing Xiao, Guoshan Lu, Sai Wu, Weiqiang Wang, Xing Fu, Can Yi, Junbo Zhao

- 企業データ資産の80%以上を占める表形式データは重要で、プライバシーの懸念が高まっている。
- 大規模言語モデル（LLMs）は高次元データの課題を克服しつつ、リアルな合成データ生成に有効。
- 新たなAIGTアプローチは、テーブルのメタデータ情報をプロンプトとして利用し、超高品質なデータを生成。
- 長トークン分割アルゴリズムにより、LLMsのトークン制約を克服し、様々なスケールのテーブルをモデル化。

合成データ生成の最先端を行ってる感じでワクワクしちゃう！プライバシー守りながら分析できるのって、未来のデータサイエンスの革命になりそうだよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-12-24 02:51

- - -

### [Generating Traffic Scenarios via In-Context Learning to Learn Better Motion Planner](http://arxiv.org/abs/2412.18086)

**コンテキスト学習による交通シナリオ生成でより良いモーションプランナーを学習**

Aizierjiang Aiersilan

- 自動運転のモーションプランニングでは、希少なシナリオの対応が課題。
- 手動でのシナリオ作成はコストが高く、効率的でない。
- 大規模言語モデルを用いてテキストからシナリオを生成する方法を提案。
- 合成データを使うことで、モーションプランナーの性能が向上することを実証。

わたし、この研究めっちゃおもしろいと思った！合成データでモーションプランナーがもっと安全になったら、未来の交通ってもっと平和でスムーズになりそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.AI, cs.CL, cs.GR, cs.LG, **投稿日時:** 2024-12-24 01:52
