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

更新: 2024-05-16T04:16:21.345710

- - -

### [BEHAVIOR Vision Suite: Customizable Dataset Generation via Simulation](http://arxiv.org/abs/2405.09546)

**BEHAVIOR Vision Suite: シミュレーションによるカスタマイズ可能なデータセット生成**

Yunhao Ge, Yihe Tang, Jiashu Xu, Cem Gokmen, Chengshu Li, Wensi Ai, Benjamin Jose Martinez, Arman Aydin, Mona Anvari, Ayush K Chakravarthy, Hong-Xing Yu, Josiah Wong, Sanjana Srivastava, Sharon Lee, Shengxin Zha, Laurent Itti, Yunzhu Li, Roberto Martín-Martín, Miao Liu, Pengchuan Zhang, Ruohan Zhang, Li Fei-Fei, Jiajun Wu

- コンピュータビジョンモデルの評価には大量のデータが必要だが、現実のデータセットでは困難
- 現行の合成データ生成器は資産とレンダリングの品質、物理特性に限界がある
- BEHAVIOR Vision Suite (BVS)は、シーンやオブジェクト、カメラのパラメータを調整して合成データを生成
- モデルのドメインシフト評価、シーン理解評価、シミュレーションから実世界への転送で活用可能

ツールでデータをカスタム生成して評価できるのすごいよね！新しい視覚タスクに使えるって、研究がもっと面白くなる予感✨

**Comment:** CVPR 2024 (Highlight). Project website:   https://behavior-vision-suite.github.io/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-15 17:57

- - -

### [MicroPython Testbed for Federated Learning Algorithms](http://arxiv.org/abs/2405.09423)

**連合学習アルゴリズムのためのMicroPythonテストベッド**

Miroslav Popovic, Marko Popovic, Ivan Kastelan, Miodrag Djukic, Ilija Basicevic

- 低コードと生成型大規模言語モデルを用いて、非専門的プログラマーが分散アプリケーションを開発
- 純粋なPythonで書かれた軽量フレームワークで、IoTの小型メモリに適合
- 旧フレームワークの制限を克服し、個別アプリケーションインスタンスが異なるネットワークノードで実行可能
- 非同期I/O抽象に基づいた設計で、PCとRaspberry Pi Pico Wボードを含む無線ネットワークで実験的検証

分散アプリをIoTで実行できちゃうのはすごいね！Pythonだから扱いやすそう。ぜひ試してみたいね！

**Comment:** 20 pages, 6 figures, 12 tables, the extended paper preprint

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-05-15 15:17

- - -

### [Real-World Federated Learning in Radiology: Hurdles to overcome and Benefits to gain](http://arxiv.org/abs/2405.09409)

**放射線学における実世界の連合学習：克服すべき障害と得られる利益**

Markus R. Bujotzek, Ünal Akünal, Stefan Denner, Peter Neher, Maximilian Zenk, Eric Frodl, Astha Jaiswal, Moon Kim, Nicolai R. Krekiehn, Manuel Nickel, Richard Ruppel, Marcus Both, Felix Döllinger, Marcel Opitz, Thorsten Persigehl, Jens Kleesiek, Tobias Penzkofer, Klaus Maier-Hein, Rickmer Braren, Andreas Bucher

- 連合学習（FL）はデータをローカルに保ちながら協調的なモデル訓練が可能
- 現在の放射線学のFL研究は、多くが実世界への適用を妨げる障害によりシミュレート環境で実施
- ドイツ放射線協力ネットワーク（RACOON）を用いて、6つの大学病院で肺病変のセグメンテーションモデルを訓練
- 実験結果はFLがすべての評価シナリオで他の手法に勝ることを示し、FLの実世界への適用の努力が正当化される

実世界で活用できる連合学習が提案されているの、すごく気になる！放射線学における医療データの共有が安全に進む未来が見えるね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.DC, **投稿日時:** 2024-05-15 15:04

- - -

### [SA-FedLora: Adaptive Parameter Allocation for Efficient Federated Learning with LoRA Tuning](http://arxiv.org/abs/2405.09394)

**SA-FedLora: LoRAチューニングを用いた効率的な連合学習のための適応パラメータ割り当て**

Yuning Yang, Xiaohong Liu, Tianrun Gao, Xiaodong Xu, Guangyu Wang

- 連合学習は分散フレームワークであり、ローカルデータセット上でモデルをトレーニングしつつ、生データを保護
- 大規模な事前学習モデルは通信コストが高く、効率的なパラメータ使用が必要
- Low-Rank Adaptation (LoRA)は固定パラメータ予算では過適合や収束遅延のリスクがある
- SA-FedLoRAは、初期段階でパラメータ正則化を行い、アニーリング段階でパラメータを徐々に削減する新手法

パラメータを効率よく使うことで、通信コストを下げられるなんてすごいね。収束を早める方法も入ってるから、これ実用化されたら便利だね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-15 14:50

- - -

### [Words Blending Boxes. Obfuscating Queries in Information Retrieval using Differential Privacy](http://arxiv.org/abs/2405.09306)

**言葉ブレンドボックス：差分プライバシーを用いた情報検索クエリの隠蔽**

Francesco Luigi De Faveri, Guglielmo Faggioli, Nicola Ferro

- 情報検索システムがユーザのプライバシーを保護しないと、クエリを通じて機密情報が漏洩
- NLPの進歩により差分プライバシーを用いてテキストを隠蔽しつつ効果を保持する可能性
- 提案するWord Blending Boxesは、安全なボックスを用いてユーザクエリの語句を保護
- オリジナルと隠蔽後のクエリの語彙・意味的類似性と、文書検索の効果を評価

この研究はプライバシー保護と検索精度を同時に両立できるかもね。実際に使われたら便利そう！

**Comment:** Preprint submitted to Information Science journal

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.IR, cs.CR, **投稿日時:** 2024-05-15 12:51

- - -

### [Dual-Segment Clustering Strategy for Federated Learning in Heterogeneous Environments](http://arxiv.org/abs/2405.09276)

**異種環境における連合学習のための二重セグメントクラスタリング戦略**

Pengcheng Sun, Erwu Liu, Wei Ni, Kanglei Yu, Rui Wang, Abbas Jamalipour

- 連合学習は効率的で通信負荷が少ないが、非独立同分布データが悪影響を及ぼす
- 通信品質の異質性がパラメータ伝送の精度に影響し、システムの性能低下を招く
- 二重セグメントクラスタリング（DSC）戦略を提案し、通信条件とデータ特性で二度クラスタリング
- DSC戦略により収束速度が向上し、異質環境でも精度が優れると実験で示される

通信品質とデータ特性の二面でクラスタリングするなんて面白そう！成功すれば、異質環境でももっと効率的な学習ができるようになるね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-15 11:46

- - -

### [Unmasking Efficiency: Learning Salient Sparse Models in Non-IID Federated Learning](http://arxiv.org/abs/2405.09037)

**効率の果て: 非独立同分布連合学習における注目すべきスパースモデルの学習**

Riyasat Ohib, Bishal Thapaliya, Gintare Karolina Dziugaite, Jingyu Liu, Vince Calhoun, Sergey Plis

- SSFL（Salient Sparse Federated Learning）はスパース連合学習の通信効率を高める
- ローカルクライアントデータで算出されたパラメータの重要度スコアを利用し、訓練前にスパースなサブネットワークを識別
- スパースモデルの重みのみを各ラウンドでクライアントとサーバ間で通信する
- 非独立同分布ベンチマークで有効性を検証し、通信時間の改善を実現

SSFL、かなり面白そう！通信時間がどれだけ減るか、実際に試してみたら驚きの結果が出たりするかもね～。"Sparse"ってキーワードが新鮮だし、これからもっと注目されそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-15 02:13

- - -

### [Feature-based Federated Transfer Learning: Communication Efficiency, Robustness and Privacy](http://arxiv.org/abs/2405.09014)

**特徴ベースの連合転移学習: 通信効率、堅牢性、プライバシー**

Feng Wang, M. Cenk Gursoy, Senem Velipasalar

- 特徴ベースの連合転移学習を提案し、通信効率を大幅に向上させる
- パラメータ更新の代わりに抽出された特徴と出力をアップロードする新しいモデル
- パケット損失、データ不足、量子化に対しての堅牢性を分析
- ラベルや特徴のプライバシー漏洩を定義・分析し、軽減方法を探求

通信効率が格段にアップするってことは、デバイスの負荷も減るし、秘密も守られるから安心だね！新しいモデルの効果を実験で見せてくれてるのも期待大。

**Comment:** Accepted by IEEE Transactions on Machine Learning in Communications   and Networking. arXiv admin note: text overlap with arXiv:2209.05395

**トピック:** [連合学習](fl), [連合転移学習](ftl), **カテゴリ:** cs.LG, cs.MA, **投稿日時:** 2024-05-15 00:43

- - -

### [A QPTAS for Facility Location on Unit Disk graphs](http://arxiv.org/abs/2405.08931)

**単位円グラフにおける施設配置問題に対する準多項式時間近似スキーム（QPTAS）**

Zachary Friggstad, Mohsen Rezapour, Mohammad R. Salavatipour, Hao Sun

- 単位円グラフは平面上の点集合であり、各点間の距離が1以下のときエッジが存在する
- 問題設定にはクライアント集合と施設集合が含まれ、それぞれの施設には開設コストがある
- 目標は、施設開設コストとクライアントを最寄りの施設に割り当てるコストを最小化すること
- この研究は、UDGsの一般設定に対する初の準多項式時間近似スキーム（QPTAS）を提案

施設配置問題って、実際の都市計画とかでも応用できそうだよね。このQPTASが広まったら、効率よく施設を配置できて、もっと住みやすくなるかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DS, **投稿日時:** 2024-05-14 19:50
