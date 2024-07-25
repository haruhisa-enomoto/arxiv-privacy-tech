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

更新: 2024-07-25T04:20:09.240509

- - -

### [HumanVid: Demystifying Training Data for Camera-controllable Human Image Animation](http://arxiv.org/abs/2407.17438)

**HumanVid: カメラ制御可能なヒューマンイメージアニメーションのためのトレーニングデータの解明**

Zhenzhi Wang, Yixuan Li, Yanhong Zeng, Youqing Fang, Yuwei Guo, Wenran Liu, Jing Tan, Kai Chen, Tianfan Xue, Bo Dai, Dahua Lin

- ヒューマンイメージアニメーションは、キャラクターの写真からビデオを生成し、ユーザーがコントロール可能にする
- 最新の手法は高品質なデータセットを使用するが、データセットの入手が難しく、フェアな評価が難しい
- HumanVidは、手作りの実データと合成データを組み合わせた、高品質な大規模データセットを提供
- 実データでは著作権フリーのビデオから選び、合成データでは3Dアバターを用いて多様なカメラモーションを生成

カメラの動きまで考慮したアニメーションデータとか面白そう！これで映画制作とかもっと自由に作れそうだね！

**Comment:** camera controllable human image animation, a dataset and a baseline

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-07-24 17:15

- - -

### [Bridging Trust into the Blockchain: A Systematic Review on On-Chain Identity](http://arxiv.org/abs/2407.17276)

**ブロックチェーンに信頼を橋渡し: オンチェーンアイデンティティに関する系統的レビュー**

Awid Vaziry, Kaustabh Barman, Patrick Herbke

- ユーザー識別はブロックチェーンベースのサービス規制に必要
- 主要な技術はゼロ知識証明、公的鍵基盤、信頼の網を含む
- オンチェーンアイデンティティの信頼性に関する研究ギャップを特定
- 未来の研究方向には、デジタルアイデンティティとアイデンティティ提供者の信頼性向上が含まれる

ブロックチェーンの上でアイデンティティをどう信頼するかってすごく大事な問題だよね。それが解決できたら、もっと安心して使えるようになるし未来が広がりそう！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.CY, cs.DC, **投稿日時:** 2024-07-24 13:42

- - -

### [A Hybrid Federated Kernel Regularized Least Squares Algorithm](http://arxiv.org/abs/2407.17228)

**ハイブリッド連合カーネル正則化最小二乗アルゴリズム**

Celeste Damiani, Yulia Rodina, Sergio Decherchi

- 連合学習はプライバシー保護の重要な場面で有用な戦略
- 臨床データに加え、オミクス特徴も含まれるため、データは病院とオミクスセンターに分散
- サンプルと特徴が分散したハイブリッド環境で効率的なカーネル正則化最小二乗アルゴリズムを提案
- データセットで検証し、攻撃対策のセキュリティ措置も議論

データがいろんな場所に散らばってても効率的に学習できるってすごい！これからの医療で大活躍しそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-07-24 12:32

- - -

### [A quantitative probabilistic relational Hoare logic](http://arxiv.org/abs/2407.17127)

**定量的確率的関係ホーア論理**

Martin Avanzini, Gilles Barthe, Davide Davoli, Benjamin Grégoire

- eRHLは確率的プログラムの関係期待特性を推論するプログラム論理である
- 定量的主張により、従来のランダム性整列制限を克服する
- eRHLはプログラムの等価性、統計的距離、差分プライバシーに対して健全かつ完全である
- PRHL及びapRHLで扱えない例をeRHLで実証する

新しいプログラム論理で複雑なセキュリティ問題に挑戦するんだね！これが実際に役立つことを示す具体的な例もあるなんて、すごく楽しみ！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LO, **投稿日時:** 2024-07-24 09:58

- - -

### [Federated Automatic Latent Variable Selection in Multi-output Gaussian Processes](http://arxiv.org/abs/2407.16935)

**連合学習による多出力ガウス過程における自動潜在変数選択**

Jingyi Gao, Seokhyun Chung

- 連合学習を用いて多出力ガウス過程の潜在プロセス数を自動選択
- 中央サーバへのデータ集中によるプライバシーリスクと計算負荷を回避
- スパイク・スラブ事前分布で必要な潜在プロセスのみを自動選択
- リチウムイオン電池劣化や気温データのシミュレーションで有効性を確認

最初に読んだとき、連合学習でプライバシーを守りつつ効率よく推論する部分が気になったよ！応用範囲も広そうだね。



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-07-24 02:03

- - -

### [Synthetic Data, Similarity-based Privacy Metrics, and Regulatory (Non-)Compliance](http://arxiv.org/abs/2407.16929)

**合成データ、類似性に基づくプライバシーメトリクス、および規制の（非）遵守**

Georgi Ganev

- 類似性に基づくプライバシーメトリクスは、規制の遵守を確保できない
- 分析と反例を通じて、特定とリンク可能性に対する保護が不足していると示した
- メトリクスは、動機のある侵入者テストを完全に無視するなどの根本的な問題がある
- 他にもいくつかの重要な問題が存在し、それらが合成データの規制遵守を阻害する

類似性って便利な感じするけど、システムの抜け穴になっちゃうんだね。規制ってやっぱり大切だね～！

**Comment:** Accepted to the 2nd Workshop on Generative AI and Law (GenLaw 2023),   part of ICML 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.AI, cs.CY, **投稿日時:** 2024-07-24 01:45

- - -

### [Inference Load-Aware Orchestration for Hierarchical Federated Learning](http://arxiv.org/abs/2407.16836)

**推論負荷に対応した階層型連合学習のオーケストレーション**

Anna Lackinger, Pantelis A. Frangoudis, Ivan Čilić, Alireza Furutanpey, Ilir Murturi, Ivana Podnar Žarko, Schahram Dustdar

- 階層型連合学習(HFL)は通信コスト削減とサーバ負荷分散のため、中間集約ノードを導入
- モデルレプリカがクライアント端末、中間ノード、グローバルサーバに分散配置される
- トレーニングと推論のプロセスが結合し、共同オーケストレーションが必要になる
- 提案手法により推論遅延が大幅に低減し、通信コストもフラットな連合学習に比べて劇的に削減

HFLのオーケストレーションが上手くいくと、推論の速度がすごく向上するみたい！移動体や交通関係での継続学習に使えたら、未来の交通システムがもっと賢くなりそうでワクワクするね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-23 21:01

- - -

### [Theoretical Analysis of Privacy Leakage in Trustworthy Federated Learning: A Perspective from Linear Algebra and Optimization Theory](http://arxiv.org/abs/2407.16735)

**信頼できる連合学習におけるプライバシー漏洩の理論的分析: 線形代数と最適化理論の視点から**

Xiaojin Zhang, Wei Chen

- 連合学習はプライバシーを守りながらの共同モデル訓練が可能だが、データ再構成攻撃などの脅威に対して脆弱
- 線形代数の視点では、バッチデータのヤコビ行列がフルランクでない場合、同じモデル更新を生成する複数のデータバッチが存在し、ある程度のプライバシーが保証されることを証明
- 特定バッチサイズによりデータ再構成攻撃を防ぐための十分条件を導出
- 最適化理論の視点から、バッチサイズや歪みの程度などに基づくプライバシー漏洩の上限を設定し、連合学習の様々な要素とプライバシー漏洩の関係についての洞察を提供

連合学習がこれからもっと普及したら、こんな風にプライバシーが守られる仕組みって本当に重要になるよね。研究が進んでいく中で、より安全な学習方法が増えるのはすごく楽しみ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, stat.ML, **投稿日時:** 2024-07-23 16:23

- - -

### [PateGail: A Privacy-Preserving Mobility Trajectory Generator with Imitation Learning](http://arxiv.org/abs/2407.16729)

**PateGail: 模倣学習を用いたプライバシー保護型の移動軌跡生成器**

Huandong Wang, Changzheng Gao, Yuchen Wu, Depeng Jin, Lina Yao, Yong Li

- プライバシー懸念により大規模な軌跡データ不足を解決するための移動軌跡生成が課題
- PateGailを提案し、生成的逆模倣学習モデルを用いて人間の意思決定プロセスをシミュレート
- ユーザーデバイスに保存された分散データでモデルをトレーニングし、個別の判別器を使用
- 結果と報酬のみ共有し、差分プライバシーを満たす摂動メカニズムを理論的に証明

これすごいね！プライバシーに配慮しつつリアルな移動データ生成するなんて、未来感満載だよね。みんなの移動パターンを守りながら学習できるなんて、日常生活の予測とかにも役立ちそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-23 14:59
