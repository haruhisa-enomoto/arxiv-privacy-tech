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

更新: 2024-08-04T04:21:44.660742

- - -

### [Synthetic dual image generation for reduction of labeling efforts in semantic segmentation of micrographs with a customized metric function](http://arxiv.org/abs/2408.00707)

**カスタマイズされた評価関数を使用した微小構造画像の意味セグメンテーションにおけるラベリング労力削減のための合成二重画像生成**

Matias Oscar Volman Stern, Dominic Hohs, Andreas Jansche, Timo Bernthaler, Gerhard Schneider

- 材料分析の意味セグメンテーションモデルの訓練には微小構造画像と対応するマスクが必要
- VQ-VAEとPixelCNNを用いて、合成画像とマスクを生成しモデルの精度を向上
- 合成データと実データを組み合わせたU-Netモデルの評価により、合成データの有効性を確認
- カスタマイズされた評価指標により、誤ったピクセルがmIoUの値を大きく減少させないようにする

人工データを駆使して、少ないサンプルで効率的にモデルトレーニングができるかも。少ないデータでも高精度が期待できるって、すっごくいいよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CE, cs.LG, **投稿日時:** 2024-08-01 16:54

- - -

### [An Experimental Evaluation of TEE technology Evolution: Benchmarking Transparent Approaches based on SGX, SEV, and TDX](http://arxiv.org/abs/2408.00443)

**TEE技術進化の実験的評価: SGX、SEV、TDXをベースとした透過的アプローチのベンチマーク**

Luigi Coppolino, Salvatore D'Antonio, Davide Iasio, Giovanni Mazzeo, Luigi Romano

- データ使用中の保護が重要な課題で、TEE技術が有望な解決策として浮上
- Intel SGXは効率的だが使いにくいプロセスベースのTEE保護を提供
- AMD SEVはVMベースのTEE保護を導入し、レガシーアプリケーションの展開を容易に
- TDX、SEV、Gramine-SGX、Occlum-SGXの比較評価を通じて、現実的な条件下でのパフォーマンスを信頼性を持って評価

TEE技術の進化を詳しく比較するのは面白そう！TDXの独自評価ができるのも画期的だよね。近い将来の応用が楽しみ！

**Comment:** Under review at IEEE Transactions on Dependable and Secure Computing

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-01 10:29

- - -

### [A Zero-Knowledge Proof of Knowledge for Subgroup Distance Problem](http://arxiv.org/abs/2408.00395)

**部分群距離問題に関する知識のゼロ知識証明**

Cansu Betin Onur

- Hammingメトリックにおける部分群距離問題の難解さに基づく新しいゼロ知識識別スキームを導入
- 提案されたプロトコルSDZKPは暗号的に安全な疑似乱数生成器を使用して秘密をマスク
- 強固なセキュリティ特性を保証するためにStern型アルゴリズムを使用
- プロトコルの強固な識別スキームとセキュリティレベルが可能

ゼロ知識証明に新たな一歩を刻みそう！セキュリティの強化が期待できるのが面白いよね。



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, math.GR, **投稿日時:** 2024-08-01 09:04

- - -

### [ABC Align: Large Language Model Alignment for Safety & Accuracy](http://arxiv.org/abs/2408.00307)

**ABC Align：大規模言語モデルの安全性と精度のためのアラインメント**

Gareth Seneque, Lap-Hang Ho, Ariel Kuperman, Nafise Erfanian Saeedi, Jeffrey Molendijk

- 大規模言語モデル（LLM）のアラインメントは未解決の課題
- 人々の嗜好は抽象度の異なる複数のレベルで捕捉可能
- 合成データ生成や嗜好最適化などの最新技術を組み合わせた統一アプローチを提案
- 提案手法はバイアスを軽減し、標準ベンチマークでの推論能力を維持しつつ精度を向上

大規模言語モデルのアラインメントって、めっちゃ重要そうだよね！新しい技術でどこまで改善できるか楽しみだな〜。

**Comment:** 23 pages, 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, 68T50, I.2.7, **投稿日時:** 2024-08-01 06:06

- - -

### [Head360: Learning a Parametric 3D Full-Head for Free-View Synthesis in 360°](http://arxiv.org/abs/2408.00296)

**Head360: 360°自由視点合成のためのパラメトリック3Dフルヘッド学習**

Yuxiao He, Yiyu Zhuang, Yanwen Wang, Yao Yao, Siyu Zhu, Xiaoyu Li, Qi Zhang, Xun Cao, Hao Zhu

- 人間の頭部360°パラメトリックモデルの生成は非常に難しい
- 芸術家がデザインした高精細な頭部のデータセットを基に新しいパラメトリックモデルを提案
- 顔の動き/形状と顔の外観を分離し、それぞれ古典的な3Dメッシュモデルとニューラルテクスチャで表現
- 単一画像入力に基づく高い汎用性と忠実度を持つ新しい反転適合方法を提案

これって他のアプリケーションにも使えそうでワクワクするね！見た目の編集やアニメーションがこんなに自由って、もうすぐ私たちも簡単にキャラクターデザインできるかもしれないね。

**Comment:** ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-01 05:46

- - -

### [RDP: Ranked Differential Privacy for Facial Feature Protection in Multiscale Sparsified Subspace](http://arxiv.org/abs/2408.00294)

**RDP: 顔特徴保護のためのランキング差分プライバシーによるマルチスケール希薄化サブスペース**

Lu Ou, Shaolin Liao, Shihui Gao, Guandong Huang, Zheng Qi

- 顔画像が公開データベースで共有されることで、顔認識システムに対する侵害のリスクが高まる
- 提案する手法「Ranking Differential Privacy (RDP)」は、プライバシー予算に基づき特徴係数に軽量ラプラスノイズを追加
- 最適なノイズスケールパラメータを求めるために二つの手法を提案：NA法とLMGD法
- 実験結果では、提案手法RDPは最先端の手法より優れており、PSNRが約10dB高い

こんなにすごい手法があれば、顔認識の技術も安心して使えちゃいそう！プライバシーを守りつつ、画像の品質も保てるなんてびっくりだよね。

**Comment:** 13 pages, 6 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CV, cs.IR, **投稿日時:** 2024-08-01 05:41

- - -

### [Mobility-Aware Federated Self-supervised Learning in Vehicular Network](http://arxiv.org/abs/2408.00256)

**モビリティ対応型連合自己教師あり学習の車両ネットワークにおける応用**

Xueying Gu, Qiong Wu, Pingyi Fan, Qiang Fan

- 連合学習 (FL) は、複数デバイス上で同時にモデルをトレーニングし、各車両のプライバシーを保護する
- ラベル付けコストが高いため、車両ネットワークやモバイルIoTでは、ラベルに頼るモデルが適さない
- 自己教師あり学習により、ラベルなしでトレーニングが可能に
- 提案されたFLSimCoは、画像のぼかしレベルに基づいて集約し、シミュレーション結果で高速かつ安定した収束を示す

車両ネットワークでのデータ活用がもっと楽になるかも！もうすぐ自動運転がさらに進化しそうな予感がするね。

**Comment:** This paper has been submitted to urban lifeline. The source code has   been released at: The source code has been released at:   https://github.com/qiongwu86/FLSimCo

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.NI, **投稿日時:** 2024-08-01 03:28

- - -

### [A Survey on the Applications of Zero-Knowledge Proofs](http://arxiv.org/abs/2408.00243)

**ゼロ知識証明の応用に関する調査**

Ryan Lavin, Xuekai Liu, Hardhik Mohanty, Logan Norman, Giovanni Zaarour, Bhaskar Krishnamachari

- ゼロ知識証明（ZKP）は、情報を明かさずに安全に交換する技術である
- 他のプライバシー技術と比較して普遍性と最小限のセキュリティ仮定がある
- ブロックチェーンのプライバシー強化から計算タスクの検証まで幅広く適用される
- 実用的な側面に焦点を当て、最新利用例を多く紹介している

ゼロ知識証明の実用例について幅広く知ることができそうでワクワクするよね！未来のブロックチェーン技術やプライバシー保護の進展に繋がるのが楽しみだな！



**トピック:** [準同型暗号](he), [秘密計算](mpc), [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.CC, **投稿日時:** 2024-08-01 02:47

- - -

### [Load Balancing in Federated Learning](http://arxiv.org/abs/2408.00217)

**連合学習における負荷分散**

Alireza Javani, Zhiying Wang

- 連合学習は、複数のリモートデバイスに分散したデータから学習を行うフレームワークである
- 負荷メトリックの分散を最小化することで、ワークロードの公平な分配と効率的なリソース利用を実現
- 分散型マルコフスケジューリングポリシーが提案され、ネットワークサイズに関係なく管理オーバーヘッドを排除
- シミュレーションを通じてアプローチを検証し、学習モデルの収束速度が向上することを示した

分散学習の負荷分散を工夫することで、効率よく学習できるみたい！特にネットワークが大きくなっても管理が楽になるのが魅力的だよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, math.IT, **投稿日時:** 2024-08-01 00:56

- - -

### [S-SYNTH: Knowledge-Based, Synthetic Generation of Skin Images](http://arxiv.org/abs/2408.00191)

**知識ベースの合成画像生成による皮膚画像のシミュレーション「S-SYNTH」**

Andrea Kim, Niloufar Saharkhiz, Elena Sizikova, Miguel Lago, Berkman Sahiner, Jana Delfino, Aldo Badano

- 医療画像のAI開発には大量で多様なデータセットが必要だが、皮膚科では得難い
- S-SYNTHは適応可能なオープンソース皮膚シミュレーションフレームワークを提案
- このモデルは皮膚色、毛、病変形状、血液割合などのパラメータを変化させられる
- 合成データにより既存データセットのバイアスや限界を軽減し、AIモデル開発を支援

S-SYNTHが皮膚画像のデータ不足を補うなんてすごい！これでAIがもっと正確に診断できるようになるといいね。

**Comment:** Accepted to the International Conference on Medical Image Computing   and Computer Assisted Intervention (MICCAI) 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-07-31 23:16

- - -

### [WAS: Dataset and Methods for Artistic Text Segmentation](http://arxiv.org/abs/2408.00106)

**WAS: 芸術的テキストセグメンテーションのためのデータセットと手法**

Xudong Xie, Yuzhe Li, Yang Liu, Zhifei Zhang, Zhaowen Wang, Wei Xiong, Xiang Bai

- 芸術的テキストセグメンテーションは多様で複雑な局所ストローク形状が課題
- 特殊な形状のストローク領域を無視しない層ごとのモメンタムクエリデコーダーを提案
- 複雑なグローバルトポロジー構造に対応するためスケルトン支援ヘッドを設計
- 多モーダルモデルと拡散モデルに基づくデータ合成戦略でモデルの汎化性能を強化

芸術的なテキストって本当に複雑だけど、この研究で新しい方法が出てきて解決できるかもね！データ合成とか、技術の進歩がすごい！

**Comment:** Accepted by ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-07-31 18:29

- - -

### [Algorithms for Collaborative Machine Learning under Statistical Heterogeneity](http://arxiv.org/abs/2408.00050)

**統計的不均一性下での協調型機械学習アルゴリズム**

Seok-Ju Hahn

- 各種データの分散トレーニングが必要になってきている
- 連合学習（FL）でデータ所有者間の生データを移動せずにトレーニング実施
- 統計的不均一性問題がFLの最大の課題であり解決が急務である
- 3つの新しいアプローチを提案し、統計的不均一性問題を軽減する

連合学習における統計的不均一性の問題に焦点を当てた画期的な研究だね！SuPerFedとAAggFF、FedEvgを使った解決策がどれも魅力的で未来の応用が楽しみだね。

**Comment:** Doctoral Dissertation. For the conference version of Chapter II, see   arXiv:2109.07628v3, and for the conference version of Chapter III, see   arXiv:2405.20821v1

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** stat.ML, cs.DC, cs.LG, **投稿日時:** 2024-07-31 16:32
