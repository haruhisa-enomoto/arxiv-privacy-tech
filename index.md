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

更新: 2024-11-17T04:21:36.029409

- - -

### [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](http://arxiv.org/abs/2411.09691)

**マルチモーダルモデルにおける多スケールアライメントを活用した詳細な視覚理解の進展**

Wei Wang, Zhaowei Li, Qi Xu, Linfeng Li, YiQing Cai, Botian Jiang, Hang Song, Xingcan Hu, Pengyu Wang, Li Xiao

- マルチモーダル大規模言語モデルは、多様なタスクで細かい視覚理解を達成
- しかし、細粒度な知識の不十分なアライメントが課題で、詳細な把握が難しい
- 新たな手法でテキスト、座標、画像の多スケール知識を効果的にアライメント
- TinyGroundingGPTは約3Bパラメータで、複雑な視覚シナリオにおいても良好な性能

新しいマルチモダル技術で視覚理解がもっと進化するなんてワクワクするね！TinyGroundingGPTも、より小さなモデルで高い精度を出せるなんて、自分でも使ってみたくなるかも。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-14 18:57

- - -

### [Towards efficient compression and communication for prototype-based decentralized learning](http://arxiv.org/abs/2411.09267)

**プロトタイプベースの分散学習における効率的な圧縮と通信に向けて**

Pablo Fernández-Piñeiro, Manuel Ferández-Veiga, Rebeca P. Díaz-Redondo, Ana Fernández-Vilas, Martín González-Soto

- プロトタイプベースの連合学習では、モデルパラメータの交換をプロトタイプや量子化データの送信に置き換える。
- 中央集約型のプロトタイプなしによる分散学習は、動的な学習タスクに適応が早くなる。
- プロトタイプの冗長性を削減するために、有用なプロトタイプのみを更新メッセージで送信し、クラスタリングを使う。
- 並列ゴシッピングを使用し、通信負荷を削減しつつ収束率を維持する。

プロトタイプを使った効率的な学習ってなんかイケてる！IoTと相性良さそうだし、未来の通信技術に広がりそうでワクワクするね。

**Comment:** 15 pages, 2 tables, 7 figures, 6 algorithms

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-14 08:08

- - -

### [SAFES: Sequential Privacy and Fairness Enhancing Data Synthesis for Responsible AI](http://arxiv.org/abs/2411.09178)

**SAFES: 責任あるAIのための逐次的プライバシーと公正性を高めるデータ合成**

Spencer Giddens, Fang Liu

- データ駆動の意思決定で情報のプライバシーと公正性を確保することが重要である
- 差分プライバシーと公正性は個別に扱われがちで、その統合には課題がある
- SAFESは差分プライバシーに基づきデータ合成と公正性向上を組み合わせた手法である
- 実証実験により、SAFESの出力データは、プライバシーを保ちながら公正性を向上することを示した

プライバシーって本当に大切だよね！SAFESのように、同時に公正性も考えてくれる技術は未来のAIにぴったり。彼らのアプローチが、他の分野でも応用されていくといいな！



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-11-14 04:36

- - -

### [Mono2Stereo: Monocular Knowledge Transfer for Enhanced Stereo Matching](http://arxiv.org/abs/2411.09151)

**Mono2Stereo: 単眼知識移転によるステレオマッチングの強化**

Yuran Wang, Yingping Liang, Hesong Li, Ying Fu

- ステレオマッチングは合成データと実データ間のギャップとラベルの希薄さが問題
- 単眼深度推定の知識移転でステレオマッチングの性能向上を提案
- 合成データでの事前トレーニングと実データの微調整の2段階トレーニング
- 知識蒸留戦略でエッジぼかしを抑えつつ一貫性を向上

これは単眼データからステレオへの知識移転を活用するんだね！コードが公開されるのが楽しみ！

**Comment:** 8 pages, 6 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-14 03:01

- - -

### [Laplace Transform Interpretation of Differential Privacy](http://arxiv.org/abs/2411.09142)

**差分プライバシーのラプラス変換解釈**

Rishav Chourasia, Uzair Javaid, Biplap Sikdar

- 差分プライバシーの概念をプライバシー損失分布のラプラス変換で表現
- 時間と周波数領域の二重性を利用し、DPの特性について新たな考察を提供
- R\'enyi DP曲線と$(\epsilon, \delta(\epsilon))$-DP曲線がラプラス・逆ラプラス変換であることを示す
- すべての$\epsilon$の値に対して正確な$(\epsilon, \delta)$-DPの適応合成定理を証明

この研究は、差分プライバシーをもっと視覚的に理解するための新しいアプローチを示していて面白そう！ラプラス変換を使って、複雑な概念をより直感的に説明できるかもしれないね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-11-14 02:52

- - -

### [Drone Detection using Deep Neural Networks Trained on Pure Synthetic Data](http://arxiv.org/abs/2411.09077)

**深層ニューラルネットワークを使用した純粋な合成データによるドローン検出**

Mariusz Wisniewski, Zeeshan A. Rana, Ivan Petrunin, Alan Holt, Stephen Harman

- ドローン検出におけるデータ不足を合成データで補い、軽減可能
- 合成データで訓練されたモデルの実世界データへの移行性を検証
- 合成データで訓練したモデルでも実データに近い性能を発揮
- 空港でのドローン検出など安全性重要なシナリオ生成に応用可能

すごいね、合成データでこんなに高い精度が出るなんて。空港なんかで実際に使われるようになったら安心だよね。もっといろんな場面で合成データを活用する研究が進んでくるといいな。

**Comment:** 12 pages, 8 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-11-13 23:09

- - -

### [Minimax Optimal Two-Sample Testing under Local Differential Privacy](http://arxiv.org/abs/2411.09064)

**局所差分プライバシーにおけるミニマックス最適な2標本検定**

Jongmin Mun, Seungwoo Kwak, Ilmun Kim

- 局所差分プライバシーに基づく多項分布と連続データの2標本検定で、プライバシーと統計的有用性のトレードオフを探求
- ラプラスやGoogleのRAPPORなどのメカニズムを用いた多項分布向けのプライベートな置換検定を提案
- ヒルダーとベゾフの滑らかさクラスについて、LDPにおける一様分離率を調査し、連続データ検定に拡張
- 非適応的なスムーズネスパラメータを持つ密度検定向けに、ボンフェローニアプローチを基にした適応型検定を提案

この論文、プライバシーを保持しつつしっかりとした検定ができるの面白そう！特にGoogleのRAPPORみたいな実用的な手法を活かせるってところがいいね。やっぱりプライバシーと便利さは天秤にかけたくなるけど、そこをうまくバランス取ってる感じがする！

**Comment:** 59 pages, 5 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.CR, cs.LG, 62G10, **投稿日時:** 2024-11-13 22:44

- - -

### [SAFELOC: Overcoming Data Poisoning Attacks in Heterogeneous Federated Machine Learning for Indoor Localization](http://arxiv.org/abs/2411.09055)

**SAFELOC: 異種連合学習によるインドアローカライゼーションにおけるデータポイズニング攻撃の克服**

Akhil Singampalli, Danish Gufran, Sudeep Pasricha

- インドアローカライゼーションの精度は、デバイスの多様性やデータポイズニング攻撃によって低下しやすい
- SAFELOCという新しいフレームワークを提案し、これらの課題下でもローカライゼーションの誤差を最小化する
- 連合学習を利用することでユーザーデータのプライバシーを守りつつ、データポイズニング検出と位置特定を行う
- 実験では、既存フレームワークに比べ誤差5.9倍、最悪誤差7.8倍、推論遅延2.1倍の改善を実現

面白そう！デバイスが異なっても性能が上がるんだね。セキュリティとプライバシーを両立させて、将来のアプリケーションに役立ちそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-11-13 22:28
