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

更新: 2025-01-12T04:20:40.574545

- - -

### [Arc2Avatar: Generating Expressive 3D Avatars from a Single Image via ID Guidance](http://arxiv.org/abs/2501.05379)

**Arc2Avatar: IDガイダンスを用いた単一画像からの表現豊かな3Dアバター生成**

Dimitrios Gerogiannis, Foivos Paraperas Papantoniou, Rolandos Alexandros Potamias, Alexandros Lattas, Stefanos Zafeiriou

- 3D Gaussian Splattingに着想を得て、単一画像から3Dアバターを再構築
- 合成データを用いてファインチューニングし、見下ろし人間の頭部を多様に生成
- 人間の顔メッシュテンプレートと密接に対応し、表情生成に展開
- スタートアップ戦略やアイデンティティ保存により色問題を解決しつつ高詳細を維持

3D技術って本当にすごい！一枚の写真から表情豊かなアバターを作るなんて、まるで魔法みたいだね。これからいろんな分野で使われそうだから楽しみだなぁ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-09 17:04

- - -

### [Validation of GPU Computation in Decentralized, Trustless Networks](http://arxiv.org/abs/2501.05374)

**分散型、信頼のないネットワークにおけるGPU計算の検証**

Eric Boniardi, Stanley Bishop, Alison Haire

- GPU計算の検証は、非決定性のため正確な再計算が難しい
- Trusted Execution Environmentsは特別なハードウェアが必要である
- 準同型暗号は計算コストが高く現実的でない
- バイナリ参照モデルと三者合意フレームワークを用いて信頼不要なネットワークを実現

未来志向で分散型ネットワークの面白さを感じるね！GPUの計算って本当に重要になってくるし、この方法でさらに安全性が高まるのってワクワクするね。新しい技術で私たちの未来がますます便利になりそう！



**トピック:** [準同型暗号](he), [TEE](tee), **カテゴリ:** cs.ET, cs.DC, **投稿日時:** 2025-01-09 16:58

- - -

### [Biomedical Relation Extraction via Adaptive Document-Relation Cross-Mapping and Concept Unique Identifier](http://arxiv.org/abs/2501.05155)

**適応型ドキュメント関係クロスマッピングと概念ユニーク識別子による生物医薬品関係抽出**

Yufei Shang, Yanrong Guo, Shijie Hao, Richang Hong

- 生物医薬品関係抽出(Bio-RE)は長文内の関係を特定するが、文を跨ぐ推論が難しい
- 従来の方法は外部知識の統合が不足し、ドキュメントの文脈が貧弱になる
- ChatGPTを用いた合成データ生成手法でデータ不足を解決する
- 新しいCUI RAGアプローチにより、生物医薬品関連の文脈を充実させることができる

新しいアプローチが生物医薬品テキストの関係抽出をグッと進化させているのが面白いね！大きなデータがなくてもChatGPTで解決できるって、かなり革新的かも！

**Comment:** 13 pages, 6 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2025-01-09 11:19

- - -

### [TAPFed: Threshold Secure Aggregation for Privacy-Preserving Federated Learning](http://arxiv.org/abs/2501.05053)

**TAPFed: プライバシー保護型連合学習のための閾値安全集約**

Runhua Xu, Bo Li, Chao Li, James B. D. Joshi, Shuai Ma, Jianxin Li

- 連合学習は個人データを明示せずにモデルを共同訓練するプライバシー保護手法
- 既存の連合学習には勾配交換によるプライバシー漏洩の問題がある
- TAPFedは、悪意ある集約者を考慮したプライバシー保護手法を提案
- TAPFedは新しい推論攻撃に耐えつつ、通信オーバーヘッドを減少させる成果を示す

TAPFedってすごく未来を感じるよね！悪意ある存在にも対応できるなんて、これからのプライバシー保護にとても頼もしい武器になりそう！🥰

**Comment:** The paper has been published in IEEE TDSC

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2025-01-09 08:24

- - -

### [MORDA: A Synthetic Dataset to Facilitate Adaptation of Object Detectors to Unseen Real-target Domain While Preserving Performance on Real-source Domain](http://arxiv.org/abs/2501.04950)

**MORDA: 未知の実世界ターゲット領域に適応しつつ実世界ソース領域の性能を維持するための合成データセット**

Hojun Lim, Heecheol Yoo, Jinwoo Lee, Seungmin Jeon, Hyeongseok Jeon

- 自動運転車のための深層神経ネットワークモデルは、大量で高品質なデータ依存に課題がある
- 新しい地域でのデータセット収集には時間とコストがかかるためソースドメイン外のデータ適応が必要
- 合成環境を補助ドメインとして利用し、リアルドメインの特性を再現するアプローチを提案
- MORDAを使用し、South Koreaのリアルデータセットで検出器の精度mAPが向上し、nuScenesもわずかに改善

新しい環境でも性能発揮できるのってすごいよね！合成データとリアルデータの融合が未来の鍵になりそう！

**Comment:** 7 pages, 6 figures, 4 tables, This work has been submitted to the   IEEE for possible publication (the paper is submitted to the conference   ICRA2025 and is under review)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-09 03:58

- - -

### [A New Perspective on Privacy Protection in Federated Learning with Granular-Ball Computing](http://arxiv.org/abs/2501.04940)

**連合学習における粒状ボール計算によるプライバシー保護の新しい視点**

Guannan Lai, Yihui Feng, Xin Yang, Xiaoyu Deng, Hao Yu, Shuyin Xia, Guoyin Wang, Tianrui Li

- 連合学習は直接データ共有せず協調的にモデルを訓練しつつプライバシーを強調
- 従来の手法はモデルの内部パラメータに注目、入力レベルの課題は未解決
- 粒状ボール連合学習（GrBFL）は画像を最適な粗さで分割し、グラフ構造に再構築
- GrBFLはプライバシー保護、効率向上を実現しつつ、他の最先端手法を上回る性能を示す

画像データを上手に加工してプライバシーを守るって面白いね！連合学習の新しいアプローチって、未来のデータ共有の形を変えちゃいそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2025-01-09 03:14

- - -

### [Decentralised Resource Sharing in TinyML: Wireless Bilayer Gossip Parallel SGD for Collaborative Learning](http://arxiv.org/abs/2501.04817)

**TinyMLにおける分散リソース共有：協調学習のための無線二層ゴシップ並列SGD**

Ziyuan Bao, Eiman Kanjo, Soumya Banerjee, Hasib-Al Rashid, Tinoosh Mohsenin

- マイクロコントローラーの性能向上に伴い、エッジデバイスで機械学習が可能になっている
- ただし、分散連合学習に関する通信の制約とネットワーク変動を克服する必要がある
- 提案手法は二層ゴシップの分散パラレルSGDで、効率的なモデル統合を実現
- 提案手法はCFLに近い精度を保ちながら、エッジデバイスでの学習を可能にしている

提案手法の通信階層とゴシッププロトコルを組み合わせたアプローチが面白そう！リソースの限られたデバイスが持つ小さな力を合わせて大きな力に変えるなんて、まさに「塵も積もれば山となる」だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-08 20:14
