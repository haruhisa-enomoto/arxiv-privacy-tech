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

更新: 2025-01-17T04:21:39.283429

- - -

### [VECT-GAN: A variationally encoded generative model for overcoming data scarcity in pharmaceutical science](http://arxiv.org/abs/2501.08995)

**VECT-GAN: 医薬品科学におけるデータ不足を克服するための変分エンコード生成モデル**

Youssef Abdalla, Marrisa Taub, Eleanor Hilton, Priya Akkaraju, Alexander Milanovic, Mine Orlu, Abdul W. Basit, Michael T Cook, Tapabrata Chakraborty, David Shorthouse

- 医薬品研究でのデータ不足が、従来の試行錯誤法への依存を招いている
- VECT-GANは、小さいノイズの多いデータセットを拡張するための新しい生成モデル
- データ拡張後に回帰モデルを開発し、既存の生成モデルよりも性能を向上させる
- 化合物データベースChEMBLで事前学習し、合成データが小さなデータセットの正則化に有効

医薬品開発ってデータ不足で大変そうだけど、このVECT-GANならその壁を乗り越えられるね！実験でも効果が証明されているし、何よりも新しいデータの生成が可能なら未来の薬の発見がもっと身近になるかも！

**Comment:** 30 pages, 6 primary figures, 3 supplementary figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2025-01-15 18:23

- - -

### [Trusted Machine Learning Models Unlock Private Inference for Problems Currently Infeasible with Cryptography](http://arxiv.org/abs/2501.08970)

**信頼された機械学習モデルが現在暗号技術で不可能な問題のプライベート推論を可能にする**

Ilia Shumailov, Daniel Ramage, Sarah Meiklejohn, Peter Kairouz, Florian Hartmann, Borja Balle, Eugene Bagdasarian

- プライバシー優先がデータ共有を制約し、効果的な相互作用を妨げることがある
- 従来の暗号技術は規模や複雑さに限界があり、信頼された第三者としての機械学習モデルを提案
- Trusted Capable Model Environments (TCMEs) は従来不可能だったセキュアな計算を拡張するアプローチ
- TCMEにより古典的な暗号問題が解決可能となり、現在の限界と今後の実装課題が提示される

信頼された機械学習モデルが暗号技術の限界を超えて新しい計算を可能にするってすごく面白いよね！未来のプライバシー技術がもっと身近になるかもしれないね。



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2025-01-15 17:28

- - -

### [Multi-View Transformers for Airway-To-Lung Ratio Inference on Cardiac CT Scans: The C4R Study](http://arxiv.org/abs/2501.08902)

**心臓CTスキャンを用いた気道対肺比推定のためのマルチビュー変換器: C4R研究**

Sneha N. Naik, Elsa D. Angelini, Eric A. Hoffman, Elizabeth C. Oelsner, R. Graham Barr, Benjamin M. Smith, Andrew F. Laine

- 肺気道樹ルーメンと肺サイズ比（ALR）はCOPDの主要なリスク因子である
- 心臓CT画像からALRを推定し、COVID-19との関連を調査する関心が高まっている
- 心臓CTは肺容量の約2/3を含み、高解像度より厚みがある
- マルチビューSwin Transformerを用いてALR推定の精度と再現性を改善した

この研究って、心臓CTを活用して肺の健康状態を予測できるから、すごく画期的だよね！多様な人種を対象にしているのも興味深いし、COPDや長期的なコロナの影響をもっと理解できそう！

**Comment:** Accepted to appear in Proceedings of International Symposium on   Biomedical Imaging (ISBI), 2025

**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, cs.LG, **投稿日時:** 2025-01-15 16:11

- - -

### [Computerized Assessment of Motor Imitation for Distinguishing Autism in Video (CAMI-2DNet)](http://arxiv.org/abs/2501.08609)

**自動化された運動模倣評価による自閉症の識別 (CAMI-2DNet)**

Kaleab A. Kinfu, Carolina Pacheco, Alice D. Sperry, Deana Crocetti, Bahar Tunçgenç, Stewart H. Mostofsky, René Vidal

- 自閉症の特徴である運動模倣の障害を評価する従来の方法は主観的で労力がかかる
- CAMI-2DNetはデータの正規化や注釈を必要としないスケーラブルな評価法を提案
- 動画を運動エンコーディングに変換し、ノイズ要因から切り離して解析する技術を採用
- CAMI-2DNetはより高い精度で自閉症と定型発達を区別し、実用性を提供する

自閉症の識別に役立つ技術って、すごく興味深いよね！動画だけで具体的な評価ができるなんて、未来感あるし、もっと発展したらいいなって思うな。

**Comment:** This work has been submitted to the IEEE for possible publication

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-15 06:15

- - -

### [Mitigating Domain Shift in Federated Learning via Intra- and Inter-Domain Prototypes](http://arxiv.org/abs/2501.08521)

**連合学習におけるドメインシフト緩和のためのプロトタイプ手法**

Huy Q. Le, Ye Lin Tun, Yu Qiao, Minh N. H. Nguyen, Keon Oh Kim, Choong Seon Hong

- 連合学習は非公開データを共有せずにグローバルモデルを訓練する技術である
- ドメイン間で特徴が異なるため、これは現実世界で課題となる
- 提案手法I$^2$PFLはドメイン内・ドメイン間プロトタイプを組み合わせて汎用モデルを構築
- MixUpベースのプロトタイプを用いて、ドメイン内とドメイン間の情報を強化する

連合学習って秘密を守りながらもみんなで協力して勉強するみたいで、面白いよね！この新しい手法でいろんな分野でもっと使いやすくなればいいなって思うよ。たとえば、医療データとかで役立ちそう！

**Comment:** 13 pages, 9 figures, 10 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-15 02:17

- - -

### [A Refreshment Stirred, Not Shaken (II): Invariant-Preserving Deployments of Differential Privacy for the US Decennial Census](http://arxiv.org/abs/2501.08449)

**A Refreshment Stirred（II）：米国10年ごとの国勢調査における差分プライバシーの不変量保持展開**

James Bailie, Ruobin Gong, Xiao-Li Meng

- 差分プライバシー仕様に基づき、2つの統計的開示制御法を分析
- PSAとTDAの方法は、機密データの一部統計を変更せず不変量とする
- PSAは差分プライバシーを満たしつつ、不変量を保持することが可能
- PSAを2020年の調査で仮定使用した場合、プライバシー損失が減少

実際のプライバシー保護に適用するには注意が必要なんだね。多様なアプローチで、もっと良い調査結果が期待できそうでワクワクする！どんな方法が一番良いのか考えるのも楽しそうだね。

**Comment:** 48 pages, 2 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.CY, cs.DS, stat.ME, **投稿日時:** 2025-01-14 21:38
