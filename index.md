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

更新: 2024-12-24T04:23:37.733311

- - -

### [FaceLift: Single Image to 3D Head with View Generation and GS-LRM](http://arxiv.org/abs/2412.17812)

**FaceLift: 単一画像からの3Dヘッド再構築とビュー生成およびGS-LRM**

Weijie Lyu, Yi Zhou, Ming-Hsuan Yang, Zhixin Shu

- FaceLiftは単一の画像から高品質な360度の頭部の3D再構築を行う技術
- マルチビュー潜在拡散モデルにより、側面および背面の視点を一貫して生成
- GS-LRM再構築により、ガウススプラットを用いて包括的な3D表現を実現
- 合成データでのみトレーニングされたが、リアルな画像にも優れた一般化を示す

この技術、ほんとすごいサバイバル能力だよね！合成データだけなのに、リアルデータにも適用できるってびっくり。動画入力での4Dビュー合成も未来的でワクワクしちゃう！

**Comment:** Project page: https://weijielyu.github.io/FaceLift

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.GR, **投稿日時:** 2024-12-23 18:59

- - -

### [Asynchronous Federated Learning: A Scalable Approach for Decentralized Machine Learning](http://arxiv.org/abs/2412.17723)

**非同期連合学習: 分散機械学習のためのスケーラブルなアプローチ**

Ali Forootani, Raffaele Iervolino

- 連合学習は多様なクライアント間で生データを共有せずにモデルを訓練する方法だが、同期的なクライアント更新で効率が悪い
- 提案する非同期連合学習（AFL）は、クライアントが独立かつ非同期にモデル更新を行えるアルゴリズム
- AFLはマーティンゲール差分と分散境界を使い、非同期更新でも堅牢な収束を保証する
- CMIP6気候データで非同期LSTMモデルを訓練し、現実的な非IIDかつ地理的に分散したデータに対応可能

この非同期アプローチは、バラバラな環境でも機械学習モデルの訓練をサポートできるのが面白いよね。特にリソースが限られた環境での省エネ性が期待できるところが魅力だなって思ったよ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.SY, eess.SY, **投稿日時:** 2024-12-23 17:11

- - -

### [FedTLU: Federated Learning with Targeted Layer Updates](http://arxiv.org/abs/2412.17692)

**FedTLU: 特定層の更新による連合学習**

Jong-Ik Park, Carlee Joe-Wong

- 連合学習はプライバシーを守りながら複数のクライアントが言語モデルを訓練に貢献する方法。
- クライアント間でデータが非独立非同分布の場合、モデルの性能が制限される問題がある。
- 提案手法はスコアリングを用いた特定層の更新で、ノイズの多い更新を避ける。
- 広範な実験で非IID条件下の収束と性能向上を実現し、効率性を示す。

連合学習でのパフォーマンス問題を特定層の更新でカバーなんて面白そう！精度も効率もいい感じがするね。どんな応用ができるのか、もっと知りたくなっちゃう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-12-23 16:17

- - -

### [Generating Completions for Fragmented Broca's Aphasic Sentences Using Large Language Models](http://arxiv.org/abs/2412.17669)

**破綻したブローカ失語症文を大規模言語モデルで完成させる手法**

Sijbren van Vaals, Yevgen Matusevych, Frank Tsiwah

- ブローカ失語症は流暢でない、断片的な発話だが理解力は良いという特徴がある
- 従来の治療法は時間がかかり、実用的な会話にそぐわないとの課題がある
- 大規模言語モデルでの断片文補完のため、合成データを用いてモデルを微調整
- モデルは特に長い入力で性能向上を示し、コミュニケーション支援の可能性を示唆

大規模言語モデルで失語症の治療を手伝うなんて、未来の医療って感じがしてワクワクするね！これで会話がスムーズになれば、失語症の人たちももっと自然に話せるようになるかも。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-23 15:54

- - -

### [Rate of Model Collapse in Recursive Training](http://arxiv.org/abs/2412.17646)

**再帰的トレーニングにおけるモデル崩壊の速度**

Ananda Theertha Suresh, Andrew Thangaraj, Aditya Nanda Kishore Khandavally

- 機械学習モデルから合成データを生成し、それを用いた再帰的トレーニングはモデル品質に影響を与える
- 再帰的トレーニングでモデルは人間が生成した元データのニュアンスをつかみにくくなり、これを「モデル崩壊」と呼ぶ
- 離散分布とガウス分布ではモデル崩壊の正確な速度が知られていなかったが、本研究では理論的特徴を明らかにした
- 離散分布では単語忘却は元の出現回数にほぼ比例し、ガウス分布では標準偏差が$n$回の反復でゼロに近づく

モデル崩壊が起こる速さについての詳細がわかるなんて面白そう！特に、データの出現回数がこれほど影響を与えるなんて、データの質って大切なんだねって改めて実感するよ。

**Comment:** 27 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.IT, math.IT, stat.ML, **投稿日時:** 2024-12-23 15:21

- - -

### [HumanVBench: Exploring Human-Centric Video Understanding Capabilities of MLLMs with Synthetic Benchmark Data](http://arxiv.org/abs/2412.17574)

**HumanVBench: 合成ベンチマークデータでMLLMの人間中心のビデオ理解能力を探る**

Ting Zhou, Daoyuan Chen, Qirui Jiao, Bolin Ding, Yaliang Li, Ying Shen

- MLLMのビデオ理解は、人間の感情や行動、発話の視覚的調整を扱うことが課題
- HumanVBenchは17のタスクで、内面的感情と外的示現を評価し、様々な要素を網羅
- 自動アノテーションとQA生成の2つのパイプラインで、多様な技術を用いてデータ合成
- 16のMLLMの評価で現在の性能の限界を示し、人間らしい理解には更なる改善が必要

人間の複雑な感情とか、行動をちゃんと理解してくれる動画モデルがどんどん出てくると、もっと直感的にAIとやりとりできるようになりそうだね。これからの発展が楽しみ！

**Comment:** 22 pages, 24 figures, 4 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-12-23 13:45

- - -

### [ERUPD -- English to Roman Urdu Parallel Dataset](http://arxiv.org/abs/2412.17562)

**ERUPD -- 英語からローマンウルドゥーへの並列データセット**

Mohammed Furqan, Raahid Bin Khaja, Rayyan Habeeb

- ローマンウルドゥーの標準化不足と音声変異が言語処理を困難にしている
- 高度なプロンプトエンジニアリングで合成データと対話データを組み合わせた
- 人間の評価を通じ言語の不一致を修正しコードスイッチングや音声表現を改善
- このデータセットは多言語教育や機械翻訳に役立つ重要なリソースとなる

ローマンウルドゥーと英語のハイブリッド的な感じが面白そう！新しいデータセットがどんな風に活用されるのかワクワクするね。URATION_ERRORS

**Comment:** 9 pages, 1 figure

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-23 13:33

- - -

### [Multimodal Preference Data Synthetic Alignment with Reward Model](http://arxiv.org/abs/2412.17417)

**マルチモーダル嗜好データ合成整列と報酬モデル**

Robert Wijaya, Ngoc-Bao Nguyen, Ngai-Man Cheung

- MLLMは視覚と言語データを統合しキャプション生成などで進化
- 前処理データと実際のユーザープロンプトの差異が誤情報を生む場合がある
- 報酬モデルを使って人間の嗜好を代理し合成データを作成する新しいフレームワークを提案
- 合成データの活用により人手によるアノテーションへの依存を減らし、MLLMの整合性を向上

合成データでMLLMの整合性を高めるなんて、なんか未来の教科書にも出てきそう！安全なAIの活用が進むことで、どんどん私たちの生活が便利になりそうでワクワクしちゃうなぁ。

**Comment:** Project Page: https://pds-dpo.github.io/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-23 09:29

- - -

### [Better Knowledge Enhancement for Privacy-Preserving Cross-Project Defect Prediction](http://arxiv.org/abs/2412.17317)

**プライバシー保護クロスプロジェクト欠陥予測のためのより良い知識強化**

Yuying Wang, Yichen Li, Haozhao Wang, Lei Zhao, Xiaofang Zhang

- クロスプロジェクト欠陥予測（CPDP）は、データプライバシーの懸念から信頼できる欠陥予測モデルの構築が困難
- 連合学習（FL）は、データを共有せずに複数の関係者間で協力してグローバルモデルを訓練し、プライバシーを保証する新しい手法
- データの異質性がモデル訓練に問題をもたらすが、FLをCPDPに直接適用することでプライバシー問題を解決できる
- 提案するFedDPは、地元の異質性認識とグローバルな知識蒸留の二つの手法でベースラインを大きく上回る

データの異質性を活かしつつ、ちゃんとプライバシーを守って問題を解決するなんてすごいね！実験結果も良好なのは本当に頼もしいと思うよ。これからもっと多くのプロジェクトでこの手法が広まるといいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.SE, **投稿日時:** 2024-12-23 06:21

- - -

### [FedLEC: Effective Federated Learning Algorithm with Spiking Neural Networks Under Label Skews](http://arxiv.org/abs/2412.17305)

**FedLEC: ラベルの偏りに対応したスパイキングニューラルネットワークによる効果的な連合学習アルゴリズム**

Di Yu, Xin Du, Linshan Jiang, Shunwen Bai, Wentao Tong, Shuiguang Deng

- スパイキングニューラルネットワークを用いた連合学習は省エネで、エッジデバイスに好適
- ラベルの偏りが非独立同分布のデータで問題を引き起こす
- FedLECはラベルの偏りを軽減し、各ローカルモデルの一般化能力を強化する
- 5つのデータセットで実験し、平均11.59%の精度向上を示す

この研究って、ラベルの偏りに悩む人たちに救世主的な感じがするよね。FedLECの改善効果11.59%はなかなかすごいし、新しいエッジデバイスの時代がさらに面白くなりそう〜！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-12-23 05:52

- - -

### [When Focus Enhances Utility: Target Range LDP Frequency Estimation and Unknown Item Discovery](http://arxiv.org/abs/2412.17303)

**フォーカスが効用を高めるとき：ターゲット範囲LDP周波数推定および未知アイテム発見**

Bo Jiang, Wanrong Zhang, Donghang Lu, Jian Du, Qiang Yan

- LDPプロトコルは信頼できるデータ管理者なしでランダム化クライアントメッセージを収集する
- 提案するGCMSプロトコルは通信、プライバシー、精度のトレードオフを改善
- OCMSフレームワークはターゲット周波数の項目を収集する際に分散を最小化
- ESAフレームワークにより、元データなしで精度を維持しつつ計算コストを低減

この研究、データのプライバシーと効率を両立させようとしているのがすごく面白いね。特に、元データに触れずに精度を保てるところに未来を感じるし、もっと探究したいなって思う！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-12-23 05:50

- - -

### [FedMeld: A Model-dispersal Federated Learning Framework for Space-ground Integrated Networks](http://arxiv.org/abs/2412.17231)

**FedMeld: 宇宙地上統合ネットワークのためのモデル分散型連合学習フレームワーク**

Qian Chen, Xianhao Chen, Kaibin Huang

- 宇宙地上統合ネットワーク(SGINs)は6GにおいてAIサービスを地球全域に届ける役割を担う
- 従来のSGINs FLフレームワークは地上局や高価な衛星間リンクが必要で遅延が問題
- FedMeldはモデル分散を使い、インフラ不要で衛星の移動を利用し修正を実現
- FedMeldはグローバルなモデル収束を実証し精度を向上、通信コストを削減する実験結果

FedMeldのアイデアって面白い！人工知能がもっと身近になる未来が楽しみだね。衛星の"持ち運び"で地球中どこでもサービスなんてちょっとワクワクする！

**Comment:** 13 pages, 7 figures. This work has been submitted to the IEEE for   possible publication

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, cs.NI, math.IT, **投稿日時:** 2024-12-23 02:58

- - -

### [MatchMiner-AI: An Open-Source Solution for Cancer Clinical Trial Matching](http://arxiv.org/abs/2412.17228)

**MatchMiner-AI: がん臨床試験のマッチングのためのオープンソースソリューション**

Ethan Cerami, Pavel Trukhanov, Morgan A. Paul, Michael J. Hassett, Irbaz B. Riaz, James Lindsay, Emily Mallaber, Harry Klein, Gufran Gungor, Matthew Galvin, Stephen C. Van Nostrand, Joyce Yu, Tali Mazor, Kenneth L. Kehl

- 臨床試験はがん治療の改善に重要だが成人参加者が少なく、必要な患者数に届かないことが多い
- MatchMiner-AIはAIを用い、患者を適切な臨床試験と効率的にマッチングすることを目指している
- 患者の医療記録から情報を抽出し、試験候補をベクトル空間に基づきランク付けする手法を採用
- 合成データのコードやモデルは公開されており、シンプルな試験検索エンジンも利用可能

がん患者マッチングをAIで支援するなんてすごい！臨床試験の参加率が上がると、より良い治療法が早く見つかるかもしれないね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.LG, **投稿日時:** 2024-12-23 02:44

- - -

### [DreamOmni: Unified Image Generation and Editing](http://arxiv.org/abs/2412.17098)

**DreamOmni: 統合された画像生成と編集**

Bin Xia, Yuechen Zhang, Jingyao Li, Chengyao Wang, Yitong Wang, Xinglong Wu, Bei Yu, Jiaya Jia

- 大規模言語モデル成功を元に、画像生成と編集を統合したDreamOmniを提案
- 既存フレームワークと下流タスクを分析し、統一フレームワークを設計
- ステッカー風の要素を用いて合成データパイプラインを開発、高品質編集データを効率的に作成
- T2I生成と編集タスクを共同訓練し、編集性能を大幅に向上

画像生成と編集の融合って面白いね！視覚的なクリエイティビティがさらに広がりそうだし、実際のデータ見てみたいなー。コードとモデルも公開されるなんて、いろんな応用が期待できちゃうね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-22 17:17

- - -

### [Multi-Agent Sampling: Scaling Inference Compute for Data Synthesis with Tree Search-Based Agentic Collaboration](http://arxiv.org/abs/2412.17061)

**マルチエージェントサンプリング: ツリー探索によるエージェント協調を用いたデータ合成の推論計算のスケーリング**

Hai Ye, Mingbao Lin, Hwee Tou Ng, Shuicheng Yan

- マルチエージェントシステムの推論計算のスケーリング法が研究される
- 合成データ生成において、異なる言語モデルを協調させる手法を提案
- ツリー探索を用いたエージェントが効果的なモデル協調を実現
- 提案手法は機械翻訳や数学的推論で高性能を達成し、SOTA性能を実現

マルチエージェントで協力し合うって、新しい可能性を感じるね！ツリー探索で効率的にデータを生成するところが未来的でワクワクするよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-22 15:16

- - -

### [DR-Encoder: Encode Low-rank Gradients with Random Prior for Large Language Models Differentially Privately](http://arxiv.org/abs/2412.17053)

**DR-Encoder: 大規模言語モデルの勾配をランダムな事前分布でエンコードし差分プライバシーを保つ手法**

Huiwen Wu, Deyi Zhang, Xiaohan Li, Xiaogang Xu, Jiafei Wu, Zhe Liu

- 大規模言語モデル（LLM）の微調整で生じる情報漏えいを連合学習で検討
- 二段階の乱数導入により連合学習でのプライバシー保証を実現
- 勾配の統計情報を基にガウス分布を用いた勾配オートエンコーダを訓練
- 誤差と精度向上を複数モデルとベンチマークで示し、プライバシー分析を詳述

プライバシーをしっかりガードしつつも効率を上げてるとか素敵すぎるね！応用が進んだら、もっと安全に言語モデルを使いこなせる未来が見えてきそう。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-12-22 15:06

- - -

### [Generate to Discriminate: Expert Routing for Continual Learning](http://arxiv.org/abs/2412.17009)

**識別するための生成: 継続学習のためのエキスパートルーティング**

Yewon Byun, Sanket V. Mehta, Saurabh Garg, Emma Strubell, Michael Oberst, Bryan Wilder, Zachary C. Lipton

- モデルは共有可能だが、データは共有できない状況で新しいドメインへの適応が課題
- ドメイン固有の専門家の集合学習により個別適応が可能。ただし、どの専門家を使うか決定が難題
- 本研究のG2Dは、合成データ活用でドメイン識別を行い、適切な専門家へサンプルを振り分ける
- G2Dは視覚と言語のタスクで競合するドメインインクリメンタル学習手法より高性能

合成データって、もっと直感的な使い方でもっといい結果が出るんだね！G2Dがどれだけ現実世界で使えるようになるか、これからも楽しみだよね。持ち寄りっこで誰も取り残されない学習がこれから進化するかも♡



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-22 13:16

- - -

### [Data value estimation on private gradients](http://arxiv.org/abs/2412.17008)

**プライベート勾配におけるデータ価値推定**

Zijian Zhou, Xinyi Xu, Daniela Rus, Bryan Kian Hsiang Low

- 勾配降下法での差分プライバシー技術は、勾配をランダムなガウスノイズで摂動するものである。
- データ価値はML性能を訓練データに帰属させ、データ価格設定や連合学習で利用。
- 既存手法ではDPでノイズ摂動すると推定の不確実性が増え、ほぼランダムな推定となる。
- 提案手法では相関のあるノイズを注入し、不確実性の線形増加を防ぎ、より良い価値推定を実現。

データの価値をしっかり計算できたら、いろんなとこで使えて便利そう！ノイズをうまく扱うテクニック、なんかクールだね！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-12-22 13:15

- - -

### [FedCross: Intertemporal Federated Learning Under Evolutionary Games](http://arxiv.org/abs/2412.16968)

**FedCross: 進化ゲームに基づく時間差連合学習**

Jianfeng Lu, Ying Zhang, Riheng Jia, Shuqin Cao, Jing Liu, Hao Fu

- 連合学習は分散型機械学習でプライバシー漏洩を軽減するが、動的なモバイルネットワークが障害となる
- 高頻度なユーザ移動が問題を引き起こすため、FedCrossでは中断された学習を別デバイスに移行
- 第1段階では、リソース制約下でのタスク配分を多目的移行アルゴリズムと進化ゲーム理論で最適化
- 第2段階では、オークションメカニズムを用いて報酬配分し、高品質モデル提供者を奨励

FedCrossってすごく新しい考え方だね！動的なネットワーク環境にも柔軟に対応できるのが魅力的。これが普及したらモバイル学習の未来が変わりそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.GT, **投稿日時:** 2024-12-22 10:59

- - -

### [On the Differential Privacy and Interactivity of Privacy Sandbox Reports](http://arxiv.org/abs/2412.16916)

**プライバシーサンドボックスレポートの差分プライバシーとインタラクティビティについて**

Badih Ghazi, Charlie Harrison, Arpana Hosabettu, Pritish Kamath, Alexander Knop, Ravi Kumar, Ethan Leeman, Pasin Manurangsi, Vikas Sahu

- プライバシーサンドボックスは、プライバシー保護を目指す広告APIを提供
- Private Aggregation APIとAttribution Reporting APIが差分プライバシーを担保
- これらのAPIのプライバシーを解析するための形式モデルを提案
- クエリとデータベースがインタラクティブに変化しても差分プライバシーを保証

プライバシーと広告の両立って、すごく難しそうなのにこの研究はそこをうまく解決しようとしてて面白そう！グーグルがそういう技術を開発しているのも興味深いし、今後の展開が楽しみだな～。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-22 08:22

- - -

### [Diffusion-Based Approaches in Medical Image Generation and Analysis](http://arxiv.org/abs/2412.16860)

**医用画像生成と解析における拡散ベースのアプローチ**

Abdullah al Nomaan Nafi, Md. Alamgir Hossain, Rakib Hossain Rifat, Md Mahabub Uz Zaman, Md Manjurul Ahsan, Shivakumar Raman

- 医療画像のデータ不足はプライバシーの懸念から大きな課題である
- 拡散モデルは合成かつリアルなデータ生成において潜在的な解決策を提供
- 脳腫瘍MRI、急性リンパ性白血病、SARS-CoV-2 CTスキャンの3領域において実験を実施
- 合成データで訓練されたCNNは実際のデータに対しても有望な分類性能を示した

合成データでリアルデータ並みにCNNが学習できるなんて、医療分野に革命が起きそう。実際の患者データの使用を減らせるから、プライバシー保護にも大きな役立ちそうだよね。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-12-22 05:02

- - -

### [GME: Improving Universal Multimodal Retrieval by Multimodal LLMs](http://arxiv.org/abs/2412.16855)

**GME: マルチモーダルLLMによるユニバーサルマルチモーダル検索の改善**

Xin Zhang, Yanzhao Zhang, Wen Xie, Mingxin Li, Ziqi Dai, Dingkun Long, Pengjun Xie, Meishan Zhang, Wenjie Li, Min Zhang

- ユニバーサルマルチモーダル検索（UMR）は、テキストや画像を統一モデルで検索する技術である
- 既存の手法はテキストデータに依存するが、多様なマルチモーダル訓練データが必要と判明
- 合成データパイプラインを開発し、高品質な融合モーダル訓練データセットを構築した
- 新たな手法GMEはUMRベンチマークにおいて最高のパフォーマンスを達成

新しい検索技術ってすごいね！マルチモーダルの可能性が広がれば、情報検索がもっと便利になりそう😊

**Comment:** 32 pages, models at   https://huggingface.co/Alibaba-NLP/gme-Qwen2-VL-2B-Instruct

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.IR, **投稿日時:** 2024-12-22 04:40

- - -

### [SoK: Usability Studies in Differential Privacy](http://arxiv.org/abs/2412.16825)

**SoK: 差分プライバシーのユーザビリティ研究**

Onyinye Dibia, Brad Stenger, Steven Baldasty, Mako Bates, Ivoline C. Ngong, Yuanyuan Feng, Joseph P. Near

- 差分プライバシーはプライバシー保護に重要だが、実装やコミュニケーションでの使いやすさに課題がある。
- ユーザビリティ向上のため、既存の差分プライバシー研究を系統化し、実用的なツールとパラメータ伝達の戦略を整理。
- 開発者やデータ分析者、非技術者を含む多様なユーザーグループでの採用における主なチャレンジやギャップを特定。
- 分かりやすいコミュニケーションとユーザー中心設計を重視し、差分プライバシーツールの普及と実用性向上を目指した研究の方向性を示唆。

ユーザビリティとコミュニケーションを重視してるってすごくいいね！差分プライバシーがもっと身近になるかも。未来のプライバシー技術、どんどん使いやすくなってくれるといいなあ。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.HC, cs.CR, **投稿日時:** 2024-12-22 02:21

- - -

### [Fed-ZOE: Communication-Efficient Over-the-Air Federated Learning via Zeroth-Order Estimation](http://arxiv.org/abs/2412.16779)

**Fed-ZOE: ゼロ次推定を用いた効率的なオーバーザエアの連合学習**

Jonggyu Jang, Hyeonsu Lyu, David J. Love, Hyun Jong Yang

- 6G時代において、連合学習は重要なパラダイムである
- オーバーザエア連合学習はデバイス数に依存せず一定の通信オーバーヘッドを実現
- Fed-ZOEはランダム化勾配推定器を用い、通信コストを大幅に削減
- 数値評価でFed-OtAと同等性能を維持しつつ通信コストの削減を実証

Fed-ZOEって、6G時代の通信問題を解決してくれるんだね。高度なネットワークをうまく活用するための重要なステップかも！楽しみだね。

**Comment:** 13 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-12-21 21:24

- - -

### [Label Privacy in Split Learning for Large Models with Parameter-Efficient Training](http://arxiv.org/abs/2412.16669)

**大規模モデルのためのラベルプライバシー保護付きパラメータ効率的学習**

Philip Zmushko, Marat Mansurov, Ruslan Svirschevski, Denis Kuznedelev, Max Ryabinin, Aleksandr Beznosikov

- 大規模なモデルのファインチューニング時にクライアントデータのプライバシー懸念がある
- LoRAを用いるAPI上でのプライバシー保護手法を分析
- 複数者分散学習アルゴリズムP$^3$EFTを提案し、プライバシーと効率を両立
- LoRAアダプターを用いて多くのNLPタスクで高精度を達成

新しいプライバシー保護の方法って、どんな風に進化しているのかなってワクワクするね！P$^3$EFTが他の方法と比べてどれくらい精度が高いのか気になるなー。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-21 15:32

- - -

### [Leveraging Contrastive Learning for Semantic Segmentation with Consistent Labels Across Varying Appearances](http://arxiv.org/abs/2412.16592)

**異なる外観に対する一貫したラベルを用いた意味セグメンテーションのためのコントラスト学習の活用**

Javier Montalvo, Roberto Alcover-Couso, Pablo Carballeira, Álvaro García-Martín, Juan C. SanMiguel, Marcos Escudero-Viñolo

- 都市シーンを多様な天候条件下で捉える新たな合成データセットを導入。
- 各シーンの複数バージョンを利用し、異なる天候シナリオ間で機能の一貫性を強制する手法を提案。
- このデータセットにより、ドメイン適応と一般化の課題を解決しながら、いくつかの整列メトリクスで性能が向上。
- 合成データ生成の重要な側面を探求し、画像の量と変動性のバランスを最適化。

この論文は天候による見た目の変化を考慮に入れているので、実用的なデータ活用ができそう。学生のプロジェクトとかで使ったら楽しそうだよね。未来の技術を垣間見る感じ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-21 11:50

- - -

### [FedGA: Federated Learning with Gradient Alignment for Error Asymmetry Mitigation](http://arxiv.org/abs/2412.16582)

**FedGA: エラー非対称性緩和のための勾配整列を用いた連合学習**

Chenguang Xiao, Zheming Zuo, Shuo Wang

- 連合学習はクライアント間でのクラス不均衡を引き起こし、偏った更新を招く
- FedGAは勾配整列を利用して、誤差の非対称性を軽減する手法を提案する
- 本手法はラベル校正を用いてモデルの収束と精度を向上させる
- FedGAは他の手法と比較して、バイアス軽減やF1スコア・精度改善で優れる

FedGAって初めて聞いたけど、勾配整列を使って誤差を調整するなんて面白いよね！今後もいろんな手法が工夫されて、もっと精度があがるかもってワクワクしちゃう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-21 11:15

- - -

### [Accelerating Private Large Transformers Inference through Fine-grained Collaborative Computation](http://arxiv.org/abs/2412.16537)

**微細な協力計算によるプライベートな大型トランスフォーマー推論の加速**

Yuntian Chen, Zhanyong Tang, Tianpei Lu, Bingsheng Zhang, Zhiying Shi, Zheng Wang

- 準同型暗号と秘密分散は医療や金融などでのプライバシー保護に有効だが、計算コストが高い
- FASTLMPIは微細な計算最適化により、効率的なプライベート推論を実現
- 準同型暗号と秘密分散の細かい設計調整で、行列の積やSoftMaxなどを改善
- 他の解決策と比較して計算時間を54-64%短縮、通信コストを72.2%削減

精密な計算で、プライバシーを守りつつも効率よくなるってすごいね！これ、医療機関とかで使われたら安心だし、もっと活用される未来が楽しみ🎶

**Comment:** 14 Pages (with 4 Pages appendix; 14 Figures)

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-21 08:33

- - -

### [Privacy in Fine-tuning Large Language Models: Attacks, Defenses, and Future Directions](http://arxiv.org/abs/2412.16504)

**大規模言語モデルの微調整におけるプライバシー: 攻撃、防御、そして将来の方向性**

Hao Du, Shang Liu, Lele Zheng, Yang Cao, Atsuyoshi Nakamura, Lei Chen

- 微調整はLLMの性能を引き出す一方で、プライバシーリスクを伴う
- メンバーシップ推論やデータ抽出攻撃など、微調整における脆弱性を調査
- 差分プライバシーなどの防御策を総括し、その利点と制限を考察
- 現行研究のギャップを指摘し、プライバシー保護の新たな道筋を提案

プライバシーを守りながら大規模モデルを微調整するなんて、なんだかスリリングだよね！何もかもがAIなのに人間らしさを求めたりして、ちょっと未来っぽい感じがするなぁ。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.AI, **投稿日時:** 2024-12-21 06:41

- - -

### [Autonomous Crack Detection using Deep Learning on Synthetic Thermogram Datasets](http://arxiv.org/abs/2412.16499)

**合成サーモグラムデータセットを用いた深層学習による自律的亀裂検出**

Chinmay Makarand Pimpalkhare, D. N. Pawaskar

- 鋼板の亀裂検出は加熱されたサーモグラム画像による人間の判別に依存
- CNNを用いたAI技術で人間の介入を減らす試みが進行中
- データ生成は、有限要素シミュレーションを用いた合成データで対応
- 実験データへの適用可能性も確認し、成功条件を示す

機械学習でのデータ不足を合成データで補うなんて、まるで魔法みたい！AIが材料検査の手助けをする未来が楽しみだね。

**Comment:** 9 pages, 14 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-21 06:10

- - -

### [Enhancing Nighttime Vehicle Detection with Day-to-Night Style Transfer and Labeling-Free Augmentation](http://arxiv.org/abs/2412.16478)

**日中から夜間へのスタイル変換とラベリングフリー拡張による夜間車両検出の強化**

Yunxiang Yang, Hao Zhen, Yongcan Huang, Jidong J. Yang

- 夜間の物体検出は深層学習モデルで挑戦的で、特に低照度でのラベル付けが難しい
- 本研究は、ラベリング不要なデータ拡張を提案し、CARLA合成データを利用して日中から夜間へのスタイル転送を行う
- Efficient Attention GANを用いてリアルな日中から夜間へのスタイル転送を実現し、モデルが車両のヘッドライト効果を学ぶ
- YOLO11モデルを農村の夜間環境に特化したデータセットで微調整し、夜間車両検出を大幅に改善

これってなんか未来の車の運転支援技術に応用できそうじゃない？夜の安全対策が簡単に強化されて、ドライブがもっと楽しくなりそうだね！

**Comment:** 12 pages, 8 figures, 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, stat.ML, **投稿日時:** 2024-12-21 04:13

- - -

### [Deepfake detection, image manipulation detection, fairness, generalization](http://arxiv.org/abs/2412.16428)

**ディープフェイク検出における公正性と一般化の課題**

Uzoamaka Ezeakunne, Chrisantus Eze, Xiuwen Liu

- ディープフェイク検出のトレーニングデータのバイアスが、人種や性別で異なる性能を示す
- 伝統的方法は未見データセットでの性能が低下し、公正性の一般化が課題となる
- 合成データを活用し、多様な人口集団を代表するデータでバランス良くモデルを訓練
- 提案手法は、ベンチマークを超えて公正性を維持し、合成データセットの有効性を示す

合成データを使って公平性を実現するなんて、ちょっとワクワクするよね！これでディープフェイク界の不平等を克服できるかもしれないね。技術がどんどん進化して、未来が楽しみすぎる〜！

**Comment:** Accepted at ICAART 2025

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CV, cs.CY, **投稿日時:** 2024-12-21 01:28

- - -

### [Improving Equity in Health Modeling with GPT4-Turbo Generated Synthetic Data: A Comparative Study](http://arxiv.org/abs/2412.16335)

**GPT4-Turbo生成合成データによる医療モデリングの公平性向上: 比較研究**

Daniel Smolyak, Arshana Welivita, Margrét V. Bjarnadóttir, Ritu Agarwal

- 医療データセットの代表性欠如が機械学習の偏りの原因である
- LLMベースの合成データ生成技術を活用し、グループごとにデータを生成
- グループ別データ生成におけるGPT4-Turboの効果は一貫していない
- グループ特定をしないプロンプトでも性能に大差ないことが判明

この研究ってどっちかっていうと医学系だけど、合成データの活用で公平性が向上するなんて面白いよね！今後もっと実用の幅が広がるかもって考えるとワクワクする！

**Comment:** 26 pages, 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CY, **投稿日時:** 2024-12-20 20:49

- - -

### [SplitFedZip: Learned Compression for Data Transfer Reduction in Split-Federated Learning](http://arxiv.org/abs/2412.17150)

**SplitFedZip: 分割型連合学習におけるデータ転送削減のための学習圧縮**

Chamani Shiranthika, Hadi Hadizadeh, Parvaneh Saeedi, Ivan V. Bajić

- 連合学習は複数のクライアントがデータを共有せずにモデルを訓練するものである
- 分割学習はモデルを異なる場所で訓練することを可能にする
- SplitFedは連合学習と分割学習の強みを組み合わせた新しい学習アプローチである
- 学習圧縮を用いたSplitFedZipは、データ転送を大幅に削減しつつモデル精度を維持

連合学習と分割学習のいいとこ取りのSplitFedって賢いアイデアだね！しかも医療データで特に役立ちそうだし、ちゃんと精度もキープしているところがすごい！圧縮まで工夫しているなんて、これから他の分野でも応用できそうでワクワクしちゃう。

**Comment:** Accepted for paper presentation at the the 1st Workshop on Federated   Learning for Unbounded and Intelligent Decentralization (FLUID), in AAAI 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-18 19:04
