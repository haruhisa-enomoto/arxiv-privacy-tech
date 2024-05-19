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

更新: 2024-05-19T04:18:09.555260

- - -

### [Automated Federated Learning via Informed Pruning](http://arxiv.org/abs/2405.10271)

**インフォームドプルーニングによる自動連合学習**

Christian Internò, Elena Raponi, Niki van Stein, Thomas Bäck, Markus Olhofer, Yaochu Jin, Barbara Hammer

- 連合学習はローカルデータを交換せずに協調学習を可能にするが、エッジデバイスでの実用化は困難
- モデルのプルーニングはDLモデルの圧縮に有効だが、従来の手法は手作業での調整が多く最適解が得にくい
- 本研究はAutoFLIPを提案し、ローカルクライアントとグローバルサーバーで動的にプルーニングと圧縮を行う
- 実験で非IIDデータのシナリオにおいて、計算制約を克服し優れたグローバル収束を実現することを確認

手作業じゃなくて自動でモデルを最適化できるのはすごく面白そう！エッジデバイスでも効率的に学習できるから、実用化が進みそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, cs.ET, **投稿日時:** 2024-05-16 17:27

- - -

### [Asynchronous Federated Stochastic Optimization with Exact Averaging for Heterogeneous Local Objectives](http://arxiv.org/abs/2405.10123)

**異種ローカル目標に対する非同期連合確率最適化と正確な平均化**

Charikleia Iakovidou, Kibaek Kim

- 連合学習（FL）は、複数のクライアントのデータを中央サーバーの調整の下で安全にモデルを訓練する手法
- フェデレーティッド学習（FL）の主な課題は、ストラグラークライアントによる長い訓練時間と非i.i.d.なローカルデータによる訓練精度の低下
- AREAという新しい確率的（サブ）勾配アルゴリズムを提案し、クライアントのドリフトに対して堅牢で、非同期通信を利用して収束を高速化
- AREAは、遅延適応ステップサイズを使用せずに、遅延の長さやローカルデータセットの異質性に依存せずに収束することが保証される

非同期での連合学習の可能性が広がりそうで面白そう！レスポンスの遅いクライアントにも強いアルゴリズムって魅力的だよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-16 14:22

- - -

### [The Effect of Quantization in Federated Learning: A Rényi Differential Privacy Perspective](http://arxiv.org/abs/2405.10096)

**連合学習における量子化の効果: レーニ差分プライバシーの視点から**

Tianqu Kang, Lumin Liu, Hengtao He, Jun Zhang, S. H. Song, Khaled B. Letaief

- 連合学習は分散データを用いたプライバシー保護機械学習の新しい手法である
- 差分プライバシーと組み合わせることでプライバシー強化が可能で、モデル重みへのガウスノイズ追加が関与
- 量子化を用いることで通信オーバーヘッドを軽減できるが、量子化されたガウスノイズがプライバシー保護の理解を複雑化
- 理論と実証の結果、低量子化ビットレベルがプライバシー保護を向上させることを確認

量子化がプライバシー保護にどう影響するかを探るなんてすごいね！理論と実践が一致したところも面白い。これからの連合学習の進展が楽しみだね！

**Comment:** 6 pages, 5 figures, submitted to 2024 IEEE MeditCom

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-05-16 13:50

- - -

### [Federated Learning for Misbehaviour Detection with Variational Autoencoders and Gaussian Mixture Models](http://arxiv.org/abs/2405.09903)

**変動オートエンコーダーとガウス混合モデルを用いた連合学習による異常行動検出**

Enrique Mármol Campos, Aurora González Vidal, José Luis Hernández Ramos, Antonio Skarmeta

- 多くの連合学習は教師あり学習で、人為的なラベル付けが必要である
- サイバー攻撃検出では、未知の脅威を識別することが困難である
- 本研究は、車両環境での潜在的異常行動を識別する非教師あり連合学習を提案
- 提案手法は、公的クラウドサービスを利用し、80%を超える性能を達成している

サイバーセキュリティとか車両の異常行動検出だから、未来の車社会でとっても重要そう！クラウド使ってみんなで学習するのも、いい感じだよね。

**Comment:** 13 pages, 11 figures, 3 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-16 08:49

- - -

### [Balancing Similarity and Complementarity for Federated Learning](http://arxiv.org/abs/2405.09892)

**連合学習における類似性と補完性のバランス**

Kunda Yan, Sen Cui, Abudukelimu Wuerkaixi, Jingfeng Zhang, Bo Han, Gang Niu, Masashi Sugiyama, Changshui Zhang

- モバイルやIoTシステムで、連合学習（FL）はデータを効率的に利用しつつユーザープライバシーを保護するために重要
- FLの主要な課題は、多数のクライアントや多様なデータソースから生じる非i.i.d.データによる統計的非均一性の管理
- 極めて重要なのは、最適な協力が必ずしも最も類似したクライアントとの協力を意味しない点
- 提案された\texttt{FedSaC}は、特徴分布の補完性を強化し、特徴とターゲットの相関の乖離を抑制して最適な協力を目指す

これ、なんかすごく面白そうだね！最適な協力ネットワークの構築とか、今後の技術にめっちゃ役立ちそう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-16 08:16

- - -

### [Advances in Robust Federated Learning: Heterogeneity Considerations](http://arxiv.org/abs/2405.09839)

**ロバストな連合学習の進展: 異質性の考慮**

Chuan Chen, Tianchi Liao, Xiaojun Deng, Zihou Wu, Sheng Huang, Zibin Zheng

- 異質的な連合学習では、異なるデータ分布やモデル構造、タスク目標、計算能力、通信リソースが問題の核である
- 異質性がモデル訓練の複雑さを増すため、データ、モデル、タスク、デバイス、通信の5つの観点から課題を整理
- 既存の最先端アプローチをデータレベル、モデルレベル、アーキテクチャレベルの3つに分類し、レビュー
- 異質的連合学習環境におけるプライバシー保護戦略を詳述し、今後の研究方向を提示

異なるクライアントでも協力できるのすごくない？そんな異質な環境でもうまくやれる技術、未来の連合学習が楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-16 06:35

- - -

### [Rethinking Barely-Supervised Segmentation from an Unsupervised Domain Adaptation Perspective](http://arxiv.org/abs/2405.09777)

**教師なしドメイン適応の観点から再考するほぼ教師なしセグメンテーション**

Zhiqiang Shen, Peng Cao, Junming Su, Jinzhu Yang, Osmar R. Zaiane

- 医療画像セグメンテーションのBSS問題を調査し、単一のスライスアノテーションと多数のラベルなし画像を含むデータセットを使用
- 従来のBSSメソッドは画像レジストレーションに依存し信頼性の低い擬似ラベルを生成
- 新たに提案されたメソッドでは単一アノテーションを用い画像レジストレーションを用いないBSSをUDAP問題として扱う
- この手法は左心房セグメンテーションで80.77%のダイススコアを達成し、SOTAを大幅に上回る性能を示した

医療画像の新しい教師なし技術ってすごく面白そう！単一スライスでそんなに正確にできるなんて、ちょっと未来が変わりそうな予感がするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-16 02:46

- - -

### [Harmonizing Generalization and Personalization in Federated Prompt Learning](http://arxiv.org/abs/2405.09771)

**連合プロンプト学習における一般化と個別化の調和**

Tianyu Cui, Hongxia Li, Jingya Wang, Ye Shi

- 連合プロンプト学習（FPL）は、大規模な事前学習済み視覚言語モデル（VLM）を連合学習に組み込む。
- データの異質性に応じて各クライアント間の個別化が必要だが、過剰な個別化はモデルの一般化能力を損なう。
- FedPGPは、CLIPを用いて知識ガイダンスを提供し、低ランク適応で個別化を実現することで、一般化と個別化のバランスを取る。
- 実験結果から、FedPGPが異なるデータセットでの一般化と個別化のバランスに優れていることが示された。

新しい技術を使って個別化と一般化のバランスを取る研究ってすごくおもしろそう！視覚言語モデルが連合学習にどんな影響を与えるのか、結果が楽しみだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-16 02:22

- - -

### [DP-RuL: Differentially-Private Rule Learning for Clinical Decision Support Systems](http://arxiv.org/abs/2405.09721)

**DP-RuL: 臨床意思決定支援システムのための差分プライバシー規則学習**

Josephine Lamp, Lu Feng, David Evans

- 患者データを使用する際のプライバシー懸念が存在する
- ローカルな差分プライバシー（LDP）を用いた人口規則セットの学習フレームワークを開発
- ルール発見プロトコルは、モンテカルロ木探索（MCTS）法とLDPを統合し、ルール構造を発見
- 適応的な予算配分方法により、プライバシーと有用性のトレードオフを改善

プライバシーを保ったまま、効果的な意思決定をサポートする技術が興味深いよね！未来の医療がもっと安全で便利になりそう♡



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-15 22:31

- - -

### [When AI Eats Itself: On the Caveats of Data Pollution in the Era of Generative AI](http://arxiv.org/abs/2405.09597)

**AIが自らを食う時代：生成AI時代のデータ汚染の注意点について**

Xiaodan Xing, Fadong Shi, Jiahao Huang, Yinzhe Wu, Yang Nan, Sheng Zhang, Yingying Fang, Mike Roberts, Carola-Bibiane Schönlieb, Javier Del Ser, Guang Yang

- 生成AIがリアルな出力を生む一方で、合成データの効果が常に良好とは限らない
- 合成データと実データのバランスは難しく、戦略的な使用が必要
- 合成データの無秩序な拡散がデータセット汚染を引き起こし、将来の性能や倫理問題を懸念させる
- 合成データの無分別な使用がもたらす影響を調査し、少モード情報融合への悪影響も考察

生成AIが自己生成データに頼りすぎると、パフォーマンスがどうなるか不安だよね。うまくバランスを取る方法を探るのが未来のカギになりそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-15 13:50
