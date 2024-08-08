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

更新: 2024-08-08T04:21:32.476156

- - -

### [PHOCUS: Physics-Based Deconvolution for Ultrasound Resolution Enhancement](http://arxiv.org/abs/2408.03657)

**PHOCUS: 超音波解像度向上のための物理ベースデコンボリューション**

Felix Duelmer, Walter Simson, Mohammad Farid Azampour, Magdalena Wysocki, Angelos Karlas, Nassir Navab

- 超音波画像は回折と有限開口による解像度の制限があり、診断用途が制約される
- 従来のデコンボリューション技術は無線周波(RF)データに直接依存していたが、アクセスが困難
- 提案手法は、Bモード画像に基づく物理ベースのデコンボリューションとINRを用いて連続的なエコー強度マップを生成する
- 合成データや実測データで評価し、従来法よりもPSNRおよびSSIMでの改善を示した

超音波画像の解像度が上がれば、診断の精度がもっと高まるね！Bモード画像だけで高品質にできるなんて絶対便利だよね。

**Comment:** Accepted at the Workshop of Advances in Simplifying Medical   Ultrasound at MICCAI 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-07 09:52

- - -

### [A three-stage method for reconstructing multiple coefficients in coupled photoacoustic and diffuse optical imaging](http://arxiv.org/abs/2408.03496)

**連続した光音響および拡散光学イメージングにおける複数の係数を再構成するための三段階法**

Yinxi Pan, Kui Ren, Shanyin Tong

- 吸収係数、拡散係数、グリューナイゼン係数の同時再構成を目指した三段階の画像再構成法を提案
- グリューナイゼン係数が既知の場合、光測定の追加により散乱係数と吸収係数の再構成精度向上
- グリューナイゼン係数が未知の場合でも、光測定によりグリューナイゼン、散乱、および吸収係数を一意に再構成できる
- 合成データを基にした数値シミュレーションで提案手法の有効性を実証

この研究ってすごくおもしろいね！未知のグリューナイゼン係数も再構成できるなんて、実際の応用がいっぱいありそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** math.NA, cs.NA, math.OC, physics.comp-ph, physics.med-ph, 35J47, 35R30, 49M15, 65M32, 78A46, 78A60, 78A70, 80A23, 92C55, 94A08, **投稿日時:** 2024-08-07 01:33

- - -

### [Optimizing NOMA Transmissions to Advance Federated Learning in Vehicular Networks](http://arxiv.org/abs/2408.03446)

**車両ネットワークにおける連合学習を進歩させるためのNOMA伝送の最適化**

Ziru Chen, Zhou Ni, Peiyuan Guan, Lu Wang, Lin X. Cai, Morteza Hashemi, Zongzhi Li

- IoTデバイスが収集する位置情報や運転パターンは、運転体験と道路安全を向上させる
- プライバシー保護のために、生データではなくモデルパラメータを送信する連合車両ネットワーク（FVN）が有望
- 連合学習（FL）の性能は加入率に依存し、無線リソースの制限で制約される
- 非直交多元接続（NOMA）を適用し、車両選択と送信電力制御で加入率を向上させる戦略を提案

連合学習とNOMAの組み合わせがすごく面白そう！車がもっと効率よく情報を共有できる未来が見えてくるね。これで運転体験も道路安全も向上するなんて最高じゃん！

**Comment:** The paper is accepted by IEEE Globecom 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, eess.SP, **投稿日時:** 2024-08-06 20:54
