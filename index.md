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

更新: 2024-08-15T04:19:16.261238

- - -

### [Practical Considerations for Differential Privacy](http://arxiv.org/abs/2408.07614)

**差分プライバシーの実践的考察**

Kareem Amin, Alex Kulesza, Sergei Vassilvitskii

- 差分プライバシーは統計データ公開の金字塔であるが、普及の障壁もある
- 政府、企業、学界で使用され、その数理的な保証が特徴
- 攻撃者の知識と強さを最悪ケースとして仮定する強力なフレームワーク 
- 日常的なデータ利用と保護での普及はまだ限定的である

この論文、実践例とかも述べてるのかな？差分プライバシーの具体的な普及方法が書かれてたら、もっと知りたいかも。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-14 15:28

- - -

### [FedQUIT: On-Device Federated Unlearning via a Quasi-Competent Virtual Teacher](http://arxiv.org/abs/2408.07587)

**FedQUIT: 準コンピテントな仮想教師を用いたデバイス上の連合アンラーニング**

Alessio Mora, Lorenzo Valerio, Paolo Bellavista, Andrea Passarella

- 連合学習はデータプライバシーを改善するが、忘れられる権利行使時の対応が課題
- FedQUITは知識蒸留を用いて忘れたいデータの寄与を削除し、モデルの汎化能力を維持
- クライアントデバイス上で直接動作し、追加情報共有や公開プロキシデータを必要としない
- 実験結果では、アンラーニング後の汎化性能回復に平均2.5%未満の追加通信ラウンドが必要

「忘れられる権利」をちゃんと実現しながらモデルパフォーマンスも守るなんて面白そう！FedQUITが未来のプライバシー技術の新しいスタンダードになるかもしれないよね！

**Comment:** Submitted to The 39th Annual AAAI Conference on Artificial   Intelligence (AAAI-25)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-08-14 14:36

- - -

### [Information-Theoretic Measures on Lattices for High-Order Interactions](http://arxiv.org/abs/2408.07533)

**高次相互作用のための格子上の情報理論的測度**

Zhaolu Liu, Mauricio Barahona, Robert L. Peach

- 従来のモデルは二変量の関連性に依存し、多変量データの複雑な統計構造を捉えきれない
- 提案手法は、変数間の代数的関係構造を格子として捉え、その格子上で測度を算出
- KLダイバージェンスを用いると、高次相互作用の正確な定量化が困難になる
- 提案したStreitberg情報は、多変量データの複雑な相互作用をより正確に評価可能

従来の二変量モデルの限界を打破しようとする斬新なアプローチ、すごく興味深いね！特に、株式市場のデータや神経電気生理学のデータに適用できるところが面白いと思う。

**Comment:** 22 pages, 13 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.IT, math.IT, stat.ML, **投稿日時:** 2024-08-14 13:04

- - -

### [At Least Factor-of-Two Optimization for RWLE-Based Homomorphic Encryption](http://arxiv.org/abs/2408.07304)

**RWLEベースの準同型暗号化の少なくとも2倍の最適化**

Jonathan Ly

- 準同型暗号（HE）は暗号化されたままデータに対する代数演算が可能
- HEの暗号化には計算オーバーヘッドがあり、データ集約型作業に影響
- Smucheはキャッシング手法で暗号化プロセスを一定時間の操作に変換
- 新手法「Zinc」はキャッシングを単一のスカラー加算に置き換え、ランダム生成を導入

Zincの手法、めっちゃ興味深いよね！分散環境でも効率を犠牲にせずセキュリティを保つなんて、未来の技術が見えてきた感じ。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-14 05:42

- - -

### [Joint Graph Rewiring and Feature Denoising via Spectral Resonance](http://arxiv.org/abs/2408.07191)

**スペクトル共鳴によるグラフの再配線と特徴のノイズ除去の同時実行**

Jonas Linkerhägner, Cheng Shi, Ivan Dokmanić

- グラフニューラルネットワーク(GNN)は、グラフ構造とノードの特徴ベクトルの両方にノイズが含まれている
- JDR（共同ノイズ除去と再配線）アルゴリズムを提案、グラフ構造と特徴を同時にクリーンアップ
- グラフと特徴行列の主要な固有空間の整合を最大化することで、性能向上を実現
- 実験により、JDRが既存の再配線方法を一貫して上回ることを確認

GNNの性能改善の新しい方法なんて超ワクワクする！特に、ノイズ除去と再配線を同時にやっちゃうのが斬新だよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.SI, stat.ML, **投稿日時:** 2024-08-13 20:16

- - -

### [FedMADE: Robust Federated Learning for Intrusion Detection in IoT Networks Using a Dynamic Aggregation Method](http://arxiv.org/abs/2408.07152)

**FedMADE: 動的集約法を用いたIoTネットワークの侵入検知のための堅牢なフェデレーテッドラーニング**

Shihua Sun, Pragya Sharma, Kenechukwu Nwodo, Angelos Stavrou, Haining Wang

- IoTデバイスの急増によりネットワークセキュリティの懸念が増大
- 伝統的な機械学習モデルはデータプライバシーの問題を抱える
- FedMADEはデバイスのトラフィックパターンに基づきローカルモデルを集約
- FedMADEはマイノリティ攻撃の分類精度を71.07%改善し、毒性攻撃に強い

FedMADEってマイノリティ攻撃の分類精度がめっちゃ上がるんだって！それに、毒性攻撃にも耐性があって、超便利じゃん。未来のセキュリティが楽しみだね。

**Comment:** To appear in the Information Security Conference (ISC) 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.NI, **投稿日時:** 2024-08-13 18:42

- - -

### [OFL-W3: A One-shot Federated Learning System on Web 3.0](http://arxiv.org/abs/2408.07096)

**OFL-W3: Web 3.0におけるワンショット連合学習システム**

Linshan Jiang, Moming Duan, Bingsheng He, Yulin Sun, Peishen Yan, Yang Hua, Tao Song

- 連合学習（FL）はデータサイロの課題を扱い、プライバシーやセキュリティ規制を保ちながら協調学習を実現
- Web 3.0のブロックチェーン技術と分散型アプリケーション（DApps）は、ウェブ開発の新たな可能性を提示
- Ethereumのトランザクション速度制約とスマートコントラクトの遅延を克服するために、ワンショットFLがWeb 3.0に適している
- OFL-W3はスマートコントラクトとIPFSを活用してトランザクションを管理し、既存のワンショットFLアルゴリズムを使用するバックエンドサーバー操作を円滑にする

Web 3.0とAIを統合した最先端の研究で、これからの技術の方向性にも大きな影響を与えそう！ワンショットFLの実用性がどれくらい高いのか、もっと詳しく知りたいね。

**Comment:** VLDB 24 demo paper

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-08-12 07:31

- - -

### [InfinityMATH: A Scalable Instruction Tuning Dataset in Programmatic Mathematical Reasoning](http://arxiv.org/abs/2408.07089)

**InfinityMATH: プログラム的数学的推論における拡張可能な指導調整データセット**

Bo-Wen Zhang, Yan Yan, Lin Li, Guang Liu

- CoTとPoT手法により、言語モデルの数学的推論能力が大きく向上
- 既存の大規模データセット作成手法は高い計算コストと大量のシードデータを必要とする
- InfinityMATHは数値を問題から分離して合成することで、拡張性と効率性を向上
- Llama2やCodeLlamaでの実験結果、ベンチマークにおいて184.7%から514.3%の改善を示した

数値を具体的に切り離して拡張性を持たせる発想、すごく面白いよね！これから先、数学の勉強で AI がもっと頼りになる時代が来るのかも！

**Comment:** Accepted by CIKM 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, I.2.7, **投稿日時:** 2024-08-09 08:18
