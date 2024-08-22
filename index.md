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

更新: 2024-08-22T04:19:45.255491

- - -

### [RFID based Health Adherence Medicine Case Using Fair Federated Learning](http://arxiv.org/abs/2408.11782)

**RFIDを活用した公平な連合学習による健康管理薬ケース**

Ali Kamrani khodaei, Sina Hajer Ahmadi

- 薬の不履行が治療効果を著しく低減し、死亡リスクや入院リスクが増加
- 既存のツール (IDASやSmart Blisterなど) は商業的な実用化に課題あり
- RFIDベースのデータ記録とNFCベースのデータ抽出を利用したSmart Pill Caseを提案
- 連合学習を統合し、データプライバシーを保ちつつ個別化されたサポートを提供

面白そうなポイントは、連合学習でみんなのデータを活かしつつプライバシーを守ること！スマホのアプリがあるから便利そうだし、続けやすそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-21 17:12

- - -

### [FedGS: Federated Gradient Scaling for Heterogeneous Medical Image Segmentation](http://arxiv.org/abs/2408.11701)

**FedGS: 異種医用画像セグメンテーションのための連合勾配スケーリング**

Philip Schutte, Valentina Corbetta, Regina Beets-Tan, Wilson Silva

- 連合学習（FL）は、患者データを共有せずに医用画像分割モデルの共同訓練を可能にし、プライバシーを保護する
- データの異種性により、FLは各機関間で異なるデータセットがあり、最適でないグローバルモデルが生成されがち
- 既存のDisentangled Representation Learning（DRL）は、スタイル特性の異種性のみを仮定し、病変のサイズや形状といったコンテンツベースの変動を見落としている
- 提案するFedGSは、小さく代表が少ないターゲットに対するセグメンテーション性能を向上させ、PolypGenとLiTSデータセットで特に小さな病変に対して優れた性能を示した

連合学習って、個人データを共有しないでいいから本当にすごいよね！提案された方法で、小さな病変もきちんと見逃さないなんて、今後の医療画像分析に大きな進展が期待できるよね。

**Comment:** 10 pages, 2 figures, 1 table, accepted at MICCAI 2024 Workshop on   Distributed, Collaborative, & Federated Learning Workshop (DeCaF). This is   the submitted manuscript with added link to github repo, funding   acknowledgements and author names and affiliations. No further post   submission improvements or corrections were integrated. Final version not   published yet

**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-08-21 15:26

- - -

### [Private Counting of Distinct Elements in the Turnstile Model and Extensions](http://arxiv.org/abs/2408.11637)

**ターンスタイルモデルにおける個別要素のプライベートカウントとその拡張**

Monika Henzinger, A. R. Sricharan, Teresa Anna Steiner

- ターンスタイルモデルでの個別要素のカウントは、機械学習で多用途に利用される基本的なデータ解析問題である
- Jainらは、要素の最大フリッパンシー（カウントが0から増減する回数）をパラメータに問題を研究した
- 彼らは、そのパラメータに対してタイトな加算誤差を持つアイテムレベルの差分プライベートアルゴリズムを提案した
- 本研究では、スパースベクター技術に基づくシンプルなアルゴリズムが従来のパラメータと異なるパラメータに対してもタイトな誤差を達成することを示した

この研究、めっちゃワクワクする！他のパラメータでもうまくいくなんて、斬新な視点だね。やっぱりプライバシーを守りながらデータ解析するのってスゴイ技術だよね～！

**Comment:** accepted at RANDOM 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, **投稿日時:** 2024-08-21 14:06

- - -

### [Confidential Computing on Heterogeneous Systems: Survey and Implications](http://arxiv.org/abs/2408.11601)

**異種システムにおける機密計算: 調査と影響**

Qifan Wang, David Oswald

- 異種システムが多様な計算コアを統合し、データ爆発に対応している
- ハードウェアベースの信頼実行環境がGPUアプリの保護に効果的
- GPU TEEの拡張に伴う潜在的なセキュリティリスクは不明確
- GPU TEE設計と攻撃手法を比較し、設計上の重要考慮事項を提供

異なる計算ユニットをまとめたハードウェア環境ってすごいよね！でも、セキュリティ問題がまだ調査中みたいで、これからの技術進化に注目だね。

**Comment:** 35 pages, 7 figures

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.AR, **投稿日時:** 2024-08-21 13:14

- - -

### [Technical Report: Coopetition in Heterogeneous Cross-Silo Federated Learning](http://arxiv.org/abs/2408.11355)

**異種交差サイロ連合学習における協力と競争**

Chao Huang, Justin Dachille, Xin Liu

- 異種データを共有せずに企業がFLで協働して共有モデルを訓練
- FL協力と市場競争の二重問題を動的2期間ゲームモデルで分析
- 非凹型問題に対処するため、複数の凹型サブ問題に分解して最適アルゴリズムを開発
- 数値結果から、FL訓練が性能向上と競争損失をもたらし、データ異種性が市場浸透と価格競争を促進する

この研究めっちゃおもしろい！FLでのコラボは一方が儲かるともう一方が損するみたいな感じで、すごくダイナミックな戦いになるね。企業同士でどうやって戦略を立てるのかワクワクするなぁ。

**Comment:** Technical report; main paper accepted to ECAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.GT, **投稿日時:** 2024-08-21 05:47

- - -

### [FedMoE: Personalized Federated Learning via Heterogeneous Mixture of Experts](http://arxiv.org/abs/2408.11304)

**FedMoE: 異種エキスパートの混合による個人化された連合学習**

Hanzi Mei, Dongqi Cai, Ao Zhou, Shangguang Wang, Mengwei Xu

- 大規模言語モデルの進化に伴い、データ需要が増加している
- クライアント間のデータ異質性と多様なタスクが連合学習の課題
- MoEアーキテクチャを用いることで柔軟性を向上させた
- FedMoEはモジュール的な集約戦略により効率的な個人化を実現

FedMoEを使うことで、各クライアントに最適なモデルを構築できるって面白いね。これからのAIがもっと個別に対応できるようになりそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-21 03:16

- - -

### [The Key of Parameter Skew in Federated Learning](http://arxiv.org/abs/2408.11278)

**連合学習におけるパラメータ歪度の鍵**

Sifan Wang, Junfeng Liao, Ye Yuan, Riquan Zhang

- FLは異なるデータ保有者間で生のデータを交換せずに深層学習を行う優れた解決策である
- FLにおける統計的異質性が主要な課題で、ローカルモデルパラメータ分布の歪度を引き起こす
- パラメータ歪度はグローバルモデルの精度に大きく影響し、そのための集約戦略FedSAを提案
- FedSAは三つのデータセットで既存手法と比較して約4.7%の精度向上を達成

連合学習の新たな障害にアプローチする方法を提案していて面白い！これがうまくいけば、もっと正確なモデルが作れるかもしれないね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-21 02:01
