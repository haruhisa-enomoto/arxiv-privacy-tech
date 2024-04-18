---
layout: single
title: トップページ
permalink: /
author_profile: true
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

To be written.

## 最新更新分

更新: 2024-04-18 10:50

- - -

### [MiniCheck: Efficient Fact-Checking of LLMs on Grounding Documents](http://arxiv.org/abs/2404.10774)

**MiniCheck: LLMの根拠文書に対する効率的なファクトチェック**

Liyan Tang, Philippe Laban, Greg Durrett

- LLMの出力が証拠に基づいているかを認識することが多くのNLPタスクにおいて重要
- 現在のファクトチェック手法は計算コストが非常に高い
- 合成データを使用して小型モデルを構築し、同等の性能を400倍低コストで実現
- 新たなベンチマークLLM-AggreFactを導入し、MiniCheck-FT5モデルが同規模のシステムより優れた性能を示す

**Comment:** LLM-AggreFact benchmark, MiniCheck models, data generation code at   https://github.com/Liyan06/MiniCheck

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-04-16 17:59

- - -

### [Confidential Federated Computations](http://arxiv.org/abs/2404.10764)

**機密性を重視した連合計算**

Hubert Eichner, Daniel Ramage, Kallista Bonawitz, Dzmitry Huba, Tiziano Santoro, Brett McLarnon, Timon Van Overveldt, Nova Fallen, Peter Kairouz, Albert Cheu, Katharine Daly, Adria Gascon, Marco Gruteser, Brendan McMahan

- 通常の連合学習と分析システムは匿名化メカニズムや差分プライバシーを必ずしも必要としないため、プライバシーに制限がある
- 従来の連合学習システムに差分プライバシーを追加すると、各デバイスの更新に過度のノイズが必要になる
- 秘密多数当事者計算に基づく無知識集計は、サービス提供者による個々のユーザーの更新へのアクセスを制限できるが、スケーラビリティとSybil攻撃の問題を抱える
- 本論文は、信頼実行環境とオープンソースを利用することでサーバー側の計算の機密性を保証し、外部から検証可能なプライバシー特性を提供する新しいシステムアーキテクチャを紹介する



**トピック:** [連合学習](fl), [差分プライバシー](dp), [秘密計算](mpc), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-04-16 17:47

- - -

### [Randomized Exploration in Cooperative Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2404.10728)

**協同マルチエージェント強化学習におけるランダム探索**

Hao-Lun Hsu, Weixin Wang, Miroslav Pajic, Pan Xu

- 協同マルチエージェント強化学習（MARL）における効率的なランダム探索の初の理論的研究を提示
- 並列マルコフ決定プロセス（MDP）のための統一的アルゴリズムフレームワークと、PHE及びLMC戦略を用いたThompson Sampling（TS）型アルゴリズム２種を提案
- 特定のクラスの並列MDPにおいて両アルゴリズムの後悔測度が$\widetilde{\mathcal{O}}(d^{3/2}H^2\sqrt{MK})$ であることを理論的に証明
- 実験結果は、我々のフレームワークが実世界の問題や複合的なRL環境での性能向上に寄与することを示し、連合学習との関連も確立

**Comment:** 80 pages, 14 figures, 1 table. Hao-Lun Hsu and Weixin Wang   contributed equally to this work

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-04-16 17:01

- - -

### [Efficient Parking Search using Shared Fleet Data](http://arxiv.org/abs/2404.10646)

**効率的な駐車探索のための共有車両データの利用**

Niklas Strauß, Lukas Rottkamp, Sebatian Schmoll, Matthias Schubert

- メルボルンやサンフランシスコのような都市では、駐車場所の占有情報を提供するセンサーが配備されている
- 駐車スポットの空き情報をマルコフ決定過程(MDP)としてモデル化し解決する方法が研究されている
- すべての車両からのデータが得られない現状では、一部の車両や車両グループからのデータを利用することが実現可能
- 実車両データと合成データを用いたシミュレーションにより、車両グループのデータ共有が駐車検索時間を大幅に削減することが示されている

**Comment:** Long Version; published at 2021 22nd IEEE International Conference on   Mobile Data Management (MDM)

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-04-16 15:20

- - -

### [ReWiTe: Realistic Wide-angle and Telephoto Dual Camera Fusion Dataset via Beam Splitter Camera Rig](http://arxiv.org/abs/2404.10584)

**ReWiTe: 光学ビームスプリッタリグを使用したリアルな広角・望遠デュアルカメラ融合データセット**

Chunli Peng, Xuan Dong, Tiantian Cao, Zhengqing Li, Kun Dong, Weixin Li

- 幅広い視野と高解像度画質を兼ね備えた画像を生成するために、広角カメラと望遠カメラからの画像を融合
- 既存の手法はディープラーニングに依存し、監督学習と合成データに基づくが、現実の広角画像と高品質の基準画像が不足
- 新たなハードウェアセットアップを導入し、リアルな広角および望遠画像と基準画像を同時に2台のスマートフォンカメラで捉える
- 提案したReWiTeデータセットは、広角・望遠デュアル画像融合タスクの実際のパフォーマンスを大幅に向上させることを実験で検証



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-16 14:10

- - -

### [A Phone-based Distributed Ambient Temperature Measurement System with An Efficient Label-free Automated Training Strategy](http://arxiv.org/abs/2404.10401)

**スマートフォンを用いた分散型室内温度計測システムと効率的な自動トレーニング戦略**

Dayin Chen, Xiaodan Shi, Haoran Zhang, Xuan Song, Dongxiao Zhang, Yuntian Chen, Jinyue Yan

- スマートフォンを用いて室内の小エリアごとに正確な温度測定を実現する分散型システムを提案
- 新しいスマートフォンの追加時にラベル付きデータの手動収集不要でモデルをトレーニングする効率的かつコスト効果的な戦略を導入
- 新規添加されたデータに対して自動で正確な推測ラベルを提供するクラウドソーシング機能を実装
- 連合学習をシステムに統合することで、プライバシー保護を強化する可能性を探求



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-04-16 09:03

- - -

### [Second Edition FRCSyn Challenge at CVPR 2024: Face Recognition Challenge in the Era of Synthetic Data](http://arxiv.org/abs/2404.10378)

**CVPR 2024での第2回FRCSynチャレンジ：合成データの時代における顔認識チャレンジ**

Ivan DeAndres-Tame, Ruben Tolosana, Pietro Melzi, Ruben Vera-Rodriguez, Minchul Kim, Christian Rathgeb, Xiaoming Liu, Aythami Morales, Julian Fierrez, Javier Ortega-Garcia, Zhizhou Zhong, Yuge Huang, Yuxi Mi, Shouhong Ding, Shuigeng Zhou, Shuai He, Lingzhi Fu, Heng Cong, Rongyu Zhang, Zhihong Xiao, Evgeny Smirnov, Anton Pimenov, Aleksei Grigorev, Denis Timoshenko, Kaleb Mesfin Asfaw, Cheng Yaw Low, Hao Liu, Chuyi Wang, Qing Zuo, Zhixiang He, Hatef Otroshi Shahreza, Anjith George, Alexander Unnervik, Parsa Rahimi, Sébastien Marcel, Pedro C. Neto, Marco Huber, Jan Niklas Kolf, Naser Damer, Fadi Boutros, Jaime S. Cardoso, Ana F. Sequeira, Andrea Atzori, Gianni Fenu, Mirko Marras, Vitomir Štruc, Jiang Yu, Zhangjie Li, Jichun Li, Weisong Zhao, Zhen Lei, Xiangyu Zhu, Xiao-Yu Zhang, Bernardo Biesseck, Pedro Vidal, Luiz Coelho, Roger Granada, David Menotti

- 合成データはデータプライバシー、人種の偏見、新しいシナリオへの一般化、厳しい条件下でのパフォーマンス制約といった現代技術の限界を克服するために顔認識での使用を探求する
- 第1回目のチャレンジと異なり、第2回目では参加者が新しい顔生成メソッドを探求するための新しいサブタスクを提案
- FRCSynの目標は、リアルデータの欠如、クラス内変動、手動ラベリングの時間とエラー、プライバシーの問題等に動機づけられている
- このチャレンジと提案された実験プロトコルおよびベンチマークは合成データを顔認識に応用する上で大きな貢献をする

**Comment:** arXiv admin note: text overlap with arXiv:2311.10476

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.CY, cs.LG, **投稿日時:** 2024-04-16 08:15

- - -

### [Privacy-Preserving Training-as-a-Service for On-Device Intelligence: Concept, Architectural Scheme, and Open Problems](http://arxiv.org/abs/2404.10255)

**デバイス上インテリジェンスのためのプライバシーを守るトレーニング・アズ・ア・サービス：概念、アーキテクチャスキーム、および未解決の問題**

Zhiyuan Wu, Sheng Sun, Yuwei Wang, Min Liu, Bo Gao, Tianliu He, Wen Wang

- デバイス上でリアルタイムかつカスタマイズされたAIサービスを提供するが、プライバシーに敏感な分散データおよび端末側制約による課題が存在
- 既存のトレーニングパラダイムでは、これらの実用的な制約に十分に対応できていない
- プライバシーを保護しつつ、端末側の計算負荷を軽減するカスタマイズ可能なAIモデルトレーニングサービスである、PTaaS（プライバシー保護トレーニング・アズ・ア・サービス）を提案
- PTaaSの定義、目標、設計原則を探求し、PTaaSサポートの新技術とそのアーキテクチャスキームを示す

**Comment:** 7 pages, 3 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-04-16 03:18
