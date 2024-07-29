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

更新: 2024-07-29T04:20:12.444084

- - -

### [Granularity is crucial when applying differential privacy to text: An investigation for neural machine translation](http://arxiv.org/abs/2407.18789)

**差分プライバシーをテキストに適用する際の粒度の重要性: ニューラル機械翻訳に関する調査**

Doan Nam Long Vu, Timour Igamberdiev, Ivan Habernal

- 差分プライバシー（DP）をNLPで用いる際に粒度の選択が重要である
- 現実世界のNMTデータセットでは、対話などの文が独立していない場合が多い
- DP適用の粒度を文レベルからドキュメントレベルに変更する必要がある
- ドキュメントレベルのNMTシステムは、メンバーシップ推定攻撃に対してより耐性がある

粒度とか意外と侮れないんだね！ドキュメントレベルにするだけでこんなにプライバシーが強化されるなんて面白い！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, **投稿日時:** 2024-07-26 14:52

- - -

### [Learning production functions for supply chains with graph neural networks](http://arxiv.org/abs/2407.18772)

**グラフニューラルネットワークを用いたサプライチェーンの生産関数の学習**

Serina Chang, Zhiyin Lin, Benjamin Yan, Swapnil Bembde, Qi Xiu, Chi Heem Wong, Yu Qin, Frank Kloster, Alex Luo, Raj Palleti, Jure Leskovec

- 企業と取引をノードとエッジで表したサプライチェーンの生産関数を推測することが重要
- 現行のグラフニューラルネットワーク(GNN)はノード間の隠れた関係を捉えられない課題がある
- 新しい時系列GNNと在庫モジュールを組み合わせたモデルを提案、生産関数を学習
- 実データと新たなシミュレータSupplySimで評価した結果、基準より6-50%改善し、予測精度も11-62%向上

サプライチェーンの複雑な関係を解き明かす新しい方法ってすごいよね。未来の物流がもっと効率的になりそうだから、上手くいったらすごく良いことになりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CY, cs.SI, **投稿日時:** 2024-07-26 14:32

- - -

### [FLUE: Federated Learning with Un-Encrypted model weights](http://arxiv.org/abs/2407.18750)

**FLUE: 暗号化されていないモデル重みを用いた連合学習**

Elie Atallah

- 連合学習はデバイス間でデータをローカルに保ちながらモデルを共有し訓練する
- 差分プライバシーでも勾配の逆解析によるデータ漏洩の懸念がある
- 提案手法は暗号化なしでコード化された代理パラメータを交換し、過剰なノイズを注入
- 2つの変種アルゴリズムが提案され、コーディングとデータ特性に適応した収束率を示す

ノイズを使ってデータを守りながら学習できるのは新しいね。暗号化が不要だから計算も軽くなりそうだし、色々な連合学習への応用が期待できるかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-26 14:04

- - -

### [Towards Effective and Efficient Continual Pre-training of Large Language Models](http://arxiv.org/abs/2407.18743)

**効果的かつ効率的な継続的プレトレーニングによる大規模言語モデルの改良**

Jie Chen, Zhipeng Chen, Jiapeng Wang, Kun Zhou, Yutao Zhu, Jinhao Jiang, Yingqian Min, Wayne Xin Zhao, Zhicheng Dou, Jiaxin Mao, Yankai Lin, Ruihua Song, Jun Xu, Xu Chen, Rui Yan, Zhewei Wei, Di Hu, Wenbing Huang, Ji-Rong Wen

- 継続的プレトレーニング（CPT）は、言語モデルを特定のドメインやタスクに適応させる重要な方法
- CPTの過程で、中国語能力と科学的推論能力を大幅に向上させるため、特定のデータミキシングとカリキュラム戦略を設計
- 学際的な科学的質問と回答ペアを合成し、これらの合成データを組み込んでLlama-3の科学的推論能力を強化
- 広範な実験結果により、一般的な能力と科学的推論能力の両方でモデルのパフォーマンスが大幅に向上することが確認された

大規模言語モデルがどんどん進化しているって感じだよね！特に合成データで科学的推論が向上するって、面白そうだし将来も期待大かも。

**Comment:** 16 pages, 10 figures, 16 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, 68T50, I.2.7, **投稿日時:** 2024-07-26 13:55

- - -

### [Homomorphic Encryption-Enabled Federated Learning for Privacy-Preserving Intrusion Detection in Resource-Constrained IoV Networks](http://arxiv.org/abs/2407.18503)

**プライバシー保護型侵入検知のための準同型暗号対応連合学習フレームワーク：リソース制約のあるIoVネットワークで**

Bui Duc Manh, Chi-Hieu Nguyen, Dinh Thai Hoang, Diep N. Nguyen

- データプライバシーの課題を解決する新しいフレームワークを提案
- ネットワーク車両が持つリソースの制約に対応、従来のFLの限界を克服
- 準同型暗号を用いたセキュアなデータオフロードを実現
- 暗号化されたデータに対して直接計算可能な訓練アルゴリズムを開発

これって未来の自動車ネットワークにすっごく役立ちそう！車のデータも安全に扱えるなんて、すごくクール♪



**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-26 04:19

- - -

### [Revisit Event Generation Model: Self-Supervised Learning of Event-to-Video Reconstruction with Implicit Neural Representations](http://arxiv.org/abs/2407.18500)

**イベント生成モデルの再考察: 暗黙的ニューラル表現によるイベントからビデオ再構築の自己教師あり学習**

Zipeng Wang, Yunfan Lu, Lin Wang

- イベントデータから高時間分解能・動的範囲を維持して強度フレームを再構築することが重要
- 以前の方法は合成データに基づく教師あり学習であり、解釈性が乏しく過適合のリスクがある
- EvINRはラベルデータや光学フロー推定を不要にした新しい自己教師ありアプローチを提案する
- 実験結果では、EvINRがMSEで38%向上し、最先端の教師あり学習方法に匹敵または上回る性能を示す

自己教師あり学習でここまで精度が上がるなんてすごい！これがもっと広がると、イベントベースのビデオ解析ももっと身近になりそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-26 04:18

- - -

### [FedUD: Exploiting Unaligned Data for Cross-Platform Federated Click-Through Rate Prediction](http://arxiv.org/abs/2407.18472)

**FedUD: クロスプラットフォーム連合クリック率予測のための非整合データの利用**

Wentao Ouyang, Rui Dong, Ri Tao, Xiangzheng Liu

- 広告プラットフォームでのクリック率（CTR）予測は重要であり、多くの現在の方法は自身のデータのみを使用する
- 他のプラットフォームのユーザー行動データも活用できれば、ユーザーの興味をより良くモデル化しCTR予測精度を向上できる
- プライバシーの問題から、異なるプラットフォーム間のデータを中央サーバーで集中モデル学習することはできない
- 提案手法FedUDは、非整合データを含む全てのデータを活用し、従来の縦型連合学習では使用できなかった非整合データをもCTR予測に貢献させる

この研究、めちゃくちゃ興味深い内容だね！特に、データのプライバシーを守りつつも複数のプラットフォームからデータを活用する方法って未来っぽくてすごくいい感じ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, cs.LG, **投稿日時:** 2024-07-26 02:48

- - -

### [Machine Unlearning using a Multi-GAN based Model](http://arxiv.org/abs/2407.18467)

**マルチGANモデルを用いた機械学習のアンラーニング**

Amartya Hatua, Trung T. Nguyen, Andrew H. Sung

- GANモデルを用いたデータ再編成と事前学習モデルの微調整を含む2つのフェーズからなる
- GANの生成器と識別器のペアを使用し、保持と忘却データセットの合成データを生成
- 合成データと元のデータのクラスラベルを反転し、すべてのデータセットを用いて事前学習モデルを微調整
- CIFAR-10データセットを用いて実験を行い、合成データとMIAテストでモデルの優越性を証明

新しいアンラーニング方法ってすごく魅力的！GANモデルの使い方には未来の可能性を感じるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-26 02:28

- - -

### [Self-Directed Synthetic Dialogues and Revisions Technical Report](http://arxiv.org/abs/2407.18421)

**自己指導による合成対話と修正の技術レポート**

Nathan Lambert, Hailey Schoelkopf, Aaron Gokaslan, Luca Soldaini, Valentina Pyatkin, Louis Castricato

- 合成データは、言語モデルの指示に従う能力を向上させる重要なツールである
- 多くの公開データは、多回ターンデータや閉じたモデルで収集され、進展が制限されている
- Self-Directed Synthetic Dialogues (SDSD)は、モデルが自身と対話する実験的データセットを導入
- この研究は、Constitutional AIの原則を活用し、最終対話ターンを修正して合成嗜好データを作成

言語モデル同士が自分とおしゃべりするデータ集めるなんて、ちょっと未来っぽくてワクワクするよね！これがもっと広がったら、AIが自分で学習しちゃうかも！？

**Comment:** 25 pages, 3 figures, 4 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-07-25 22:42

- - -

### [SCALE: Self-regulated Clustered federAted LEarning in a Homogeneous Environment](http://arxiv.org/abs/2407.18387)

**同質環境における自己調整クラスタ連合学習 (SCALE)**

Sai Puppala, Ismail Hossain, Md Jahangir Alam, Sajedul Talukder, Zahidur Talukder, Syed Bahauddin

- 連合学習には通信の非効率性や中央インフラへの依存が課題である
- 新手法はエッジサーバーへの依存を排除しデータの類似性などに基づいて動的にクラスタを形成
- ハイブリッド分散集約プロトコルで局所モデル訓練とピアツーピアの重み交換を行い通信オーバーヘッドを削減
- 乳癌データセットで検証しながら、訓練遅延やエネルギー消費を減少させつつ通信オーバーヘッドを10分の1に削減

この研究は、効率面とプライバシー面で大きく進化しそうだね！将来的に連合学習の標準になりそうな予感がする！

**Comment:** This research article got accepted in COMPSAC conference and going to   be published to IEEE

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.AI, cs.ET, cs.LG, cs.PF, **投稿日時:** 2024-07-25 20:42

- - -

### [FADAS: Towards Federated Adaptive Asynchronous Optimization](http://arxiv.org/abs/2407.18365)

**FADAS：連合適応非同期最適化に向けて**

Yujia Wang, Shiqiang Wang, Songtao Lu, Jinghui Chen

- 連合学習は、プライバシーを保護した機械学習のための広く採用されているトレーニング手法
- 従来の同期集約設計は、大規模モデルの適応的連合最適化の実装における課題
- FADASという非同期更新を取り入れた新しい適応的連合最適化手法を提案
- 提案手法の収束速度を理論的に確立し、他の非同期連合学習ベースラインよりも優れた性能を実証

非同期更新の導入や遅延調整が、実際の使用にどんな効果をもたらすのか楽しみだな。その最先端な技術、ぜひ使ってみたいね！

**Comment:** Accepted by ICML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, math.OC, **投稿日時:** 2024-07-25 20:02

- - -

### [Generative AI like ChatGPT in Blockchain Federated Learning: use cases, opportunities and future](http://arxiv.org/abs/2407.18358)

**ブロックチェーン連合学習におけるChatGPTのような生成的AI：ユースケース、機会、未来**

Sai Puppala, Ismail Hossain, Md Jahangir Alam, Sajedul Talukder, Jannatul Ferdaus, Mahedi Hasan, Sameera Pisupati, Shanmukh Mathukumilli

- 連合学習はデータを共有せずに分散データで機械学習モデルをトレーニングするアプローチ
- 生成的AIの組み込みにより、プライバシー保護やデータ拡充、モデルのカスタマイズが可能
- 生成的AIは生成的敵対ネットワーク（GAN）や変分オートエンコーダ（VAE）を用い、合成データを生成
- 合成データはデータ不足問題に対処し、頑健なモデル開発を助ける

連合学習と生成的AIの組み合わせ、すごく革新的だね！これでプライバシーを守りつつ、もっと個別化されたモデルが作れそうでわくわくする！

**Comment:** We are going to submit this research article into a conference which   is best fit for this topic

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-07-25 19:43

- - -

### [Privacy-Preserving Model-Distributed Inference at the Edge](http://arxiv.org/abs/2407.18353)

**プライバシー保護型エッジにおけるモデル分散推論**

Fatemeh Jafarian Dehkordi, Yasaman Keshtkarjahromi, Hulya Seferoglu

- クライアントデータを用いたML推論のため、プライバシーを保つプロトコルを設計
- エッジサーバーでモデル分散推論を行い、通信量を削減
- 加法的秘密分散や線形準同型暗号を用いて線形計算処理
- Garbled Circuitと新しい三者間の秘密保持転送を使い非線形関数を处理

エッジサーバーでのモデル分散推論とかすごく興味津々！通信量削減で効率アップが期待できるんだね、この技術革命が未来のプライバシー保護をどれだけ進めるか楽しみ！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-07-25 19:39

- - -

### [Adaptive Differentially Private Structural Entropy Minimization for Unsupervised Social Event Detection](http://arxiv.org/abs/2407.18274)

**適応型差分プライバシー構造エントロピー最小化による教師なしソーシャルイベント検出**

Zhiwei Yang, Yuecen Wei, Haoran Li, Qian Li, Lei Jiang, Li Sun, Xiaoyan Yu, Chunming Hu, Hao Peng

- ソーシャルイベント検出は、ソーシャルメディアデータストリームから特定のイベントを表現する関連メッセージクラスターを抽出する
- 現在の大部分の手法は教師ありで、大量のデータと事前知識を必要とし、敏感情報の漏洩リスクが高い
- ADP-SEMEventという新しいフレームワークを提案し、適応型差分プライバシーを用いた教師なしのソーシャルイベント検出を実現
- 実験では、2つの公開データセットを用いて、最先端の方法と同等の検出性能を維持しつつ、合理的なプライバシー予算パラメータを維持することを確認

ソーシャルメディアのデータをリアルタイムで監視してプライバシーも守るなんて、未来感バツグン！データのプライバシーと有用性を両立するアプローチ、絶対注目されそう！

**Comment:** Accepted to ACM CIKM 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.SI, cs.AI, **投稿日時:** 2024-07-23 11:19
