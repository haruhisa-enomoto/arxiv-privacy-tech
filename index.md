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

更新: 2024-07-31T04:16:21.155267

- - -

### [Add-SD: Rational Generation without Manual Reference](http://arxiv.org/abs/2407.21016)

**Add-SD: 手動参照なしの合理的生成**

Lingfeng Yang, Xinyu Zhang, Xiang Li, Jinwen Chen, Kun Yao, Gang Zhang, Errui Ding, Lingqiao Liu, Jingdong Wang, Jian Yang

- Add-SDはテキストプロンプトのみを条件にオブジェクトを現実的なシーンに挿入
- RemovalDatasetという、削除されたオブジェクトの画像ペアを含むデータセットを提案
- 安定拡散モデルをファインチューニングし、合理的な生成を実現
- LVIS valデータセット実験でレアクラスに対して4.3 mAPの改善を確認

シーンに必要な物を合理的に追加できるなんて未来的でワクワクしちゃう！様々な応用が期待できそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-30 17:58

- - -

### [Federated Knowledge Recycling: Privacy-Preserving Synthetic Data Sharing](http://arxiv.org/abs/2407.20830)

**連合知識リサイクル：プライバシー保護型合成データ共有**

Eugenio Lomurno, Matteo Matteucci

- 現在の連合学習技術はモデルやパラメータの露出による脆弱性が存在
- FedKRは合成データを使用し、機関間の協力を促進
- 高度なデータ生成技術と動的な集約プロセスを組み合わせ、プライバシー攻撃に対するセキュリティを強化
- 実験結果では、FedKRが競争力のあるパフォーマンスを達成し、データ不足のシナリオで特に効果的

FedKRの適用範囲が広くて、どんなデータでも活用できそう！セキュリティ面でも安心だし、まさに未来の技術って感じだよね！



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2024-07-30 13:56

- - -

### [Integrating audiological datasets via federated merging of Auditory Profiles](http://arxiv.org/abs/2407.20765)

**聴覚プロファイルの連合的統合による聴覚データセットの統合**

Samira Saak, Dirk Oetting, Birger Kollmeier, Mareike Buhl

- 聴覚データセットは、患者の聴覚損失に関する貴重な知識を含む
- 複数のデータセットを統合し、類似性に基づいて聴覚プロファイル（AP）を統合
- ランダムフォレストモデルを作成し、さまざまな聴覚測定の組み合わせを評価
- 統合APセットは詳細な患者情報を保持しつつ、良好な分類性能を達成

似たようなデータを色々なデータセットから統合して、もっと詳細な聴覚プロファイルを作るなんてすごいね！これからはどのデバイスからでも患者の状態が分かるようになるかもしれないね。



**トピック:** [連合学習](fl), **カテゴリ:** physics.med-ph, cs.SD, eess.AS, physics.data-an, **投稿日時:** 2024-07-30 12:08

- - -

### [SynthVLM: High-Efficiency and High-Quality Synthetic Data for Vision Language Models](http://arxiv.org/abs/2407.20756)

**SynthVLM: ビジョン言語モデルのための高効率・高品質な合成データ**

Zheng Liu, Hao Liang, Wentao Xiong, Qinhan Yu, Conghui He, Bin Cui, Wentao Zhang

- ウェブ画像の増加に伴い、大規模な画像データセットの管理と理解が重要
- SynthVLMは、高解像度の画像とキャプションのペアを生成し、高品質なアラインメントを実現
- 従来のGPT-4 Visionベースの生成方法と比較し、性能が向上し計算負荷が大幅に削減
- 純粋な生成データを利用することでプライバシーを保護し、100kデータポイントでSoTA性能を達成

ビジョン言語モデルって難しそうだけど、これなら効率よく高性能が狙えるんだね！プライバシーも守れてるのがすごい安心感だよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, **投稿日時:** 2024-07-30 11:57

- - -

### [Neural Fields for Continuous Periodic Motion Estimation in 4D Cardiovascular Imaging](http://arxiv.org/abs/2407.20728)

**4D心血管イメージングにおける連続的な周期運動推定のためのニューラルフィールド**

Simone Garzia, Patryk Rygiel, Sven Dummer, Filippo Cademartiri, Simona Celi, Jelmer M. Wolterink

- 現在の4DフローMRI分析法は静的な動脈壁を使用しているが、完全なサイクルのセグメンテーションが困難であるため
- 提案したニューラルフィールドベースの方法により、心臓サイクル全体で連続的な周期壁変形を直接推定できる
- 3D+時間撮影データセットに対して、時間依存の速度ベクトル場（VVF）を表現した暗黙のニューラル表現（INR）を最適化
- 提案手法の効果は、異なる周期パターンを持つ合成データ、ECG連動CT、および4DフローMRIデータで実証した

これすごくない？心臓の動きも正確に捉えられそうで、医療診断がもっと進化しそうだよね！4Dイメージングの時代が来たって感じ！

**Comment:** 10 pages, 5 figures, STACOM 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-30 10:50

- - -

### [Federated Learning as a Service for Hierarchical Edge Networks with Heterogeneous Models](http://arxiv.org/abs/2407.20573)

**異種モデルを持つ階層型エッジネットワーク向け連合学習サービス**

Wentao Gao, Omid Tavallaie, Shuaijun Chen, Albert Zomaya

- 連合学習(FL)とは、ユーザーの元データを共有せずにローカルでトレーニングされたモデルを集約する分散型機械学習フレームワークである
- FLaaSは異なる計算資源を持つデバイス上でプライバシーを保護しながら機械学習モデルをトレーニングできる
- 現在のFLは全クライアントデバイスに同じモデルをトレーニングさせるが、計算資源に差があるため効果が限定される
- 提案されているHAF-EdgeはIoT、エッジ、クラウド環境にまたがる階層型FLシステムで異種モデルの集約問題を解決し、高い性能を示す

階層型FLシステムで異なる計算力を持つデバイスにも対応できるなんて、すごく実用的だね！エッジとクラウドで効率的にデータを集約する工夫がされてるところが面白そう♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-30 06:04

- - -

### [CELLM: An Efficient Communication in Large Language Models Training for Federated Learning](http://arxiv.org/abs/2407.20557)

**CELLM: 連合学習における大規模言語モデル訓練の効率的な通信**

Raja Vavekanand, Kira Sam

- 連合学習はデータを集約せずにモデルを訓練し、プライバシーとセキュリティの利点を提供する
- 大規模言語モデルは、ノイズの多いデータから学習することで統計的不均一性を解決する可能性がある
- LoRAを用いて局所的なモデル訓練の計算負荷を低減し、スパースアップデートで通信コストを低減
- 提案手法は通信コストを10倍、複雑なベースラインと比べて5倍削減しつつ高い有用性を達成

大規模言語モデルの訓練を効率化する方法ってめっちゃ気になる！連合学習の課題をうまく克服できたら、さらにプライバシー保護が進みそうね！

**Comment:** 22 pages, 10 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-30 05:24

- - -

### [Boosting Efficiency in Task-Agnostic Exploration through Causal Knowledge](http://arxiv.org/abs/2407.20506)

**因果知識を活用したタスク非依存探索の効率向上**

Yupei Yang, Biwei Huang, Shikui Tu, Lei Xu

- 予算制約がデータ収集に制限を課し、モデル訓練の効果に影響
- 因果知識を利用した探索戦略「因果探索」を提案
- タスク非依存強化学習の学習効率と信頼性を向上
- 実験結果により、因果探索がデータを少なくしても正確な世界モデルを学習可能と実証

因果知識を活用して少ないデータでモデルを訓練する工夫がめっちゃ面白そう！理論と実践の両方で有効性が証明されてるのも期待度高いね！

**Comment:** This paper was accepted by IJCAI'24

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-30 02:51
