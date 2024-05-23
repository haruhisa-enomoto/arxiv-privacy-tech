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

更新: 2024-05-23T04:17:38.696919

- - -

### [Decentralized Federated Learning Over Imperfect Communication Channels](http://arxiv.org/abs/2405.12894)

**不完全な通信チャネル上での分散連合学習**

Weicai Li, Tiejun Lv, Wei Ni, Jingbo Zhao, Ekram Hossain, H. Vincent Poor

- 不完全な通信チャネルが分散連合学習(D-FL)に与える影響を分析
- 理想的なグローバルモデルと比較して通信エラーが蓄積しやすいことを指摘
- 通信エラーを最小化するための最適なローカル集約回数を見つけることが重要
- 実験では、最適なローカル集約回数が学習精度を10%以上向上させることを確認

理論だけじゃなくて、実際のデータでも効果があるのが面白そう！これから通信トラブルの少ない世界が近づくかもね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.IT, cs.LG, math.IT, **投稿日時:** 2024-05-21 16:04

- - -

### [Mitigating Overconfidence in Out-of-Distribution Detection by Capturing Extreme Activations](http://arxiv.org/abs/2405.12658)

**異常検出の過信を極端な活性値に基づいて軽減する方法**

Mohammad Azizmalayeri, Ameen Abu-Hanna, Giovanni Cinà

- OODインスタンス検出は、実世界での機械学習モデルの信頼性に重要
- モデルが高い確信を持つ「過信」現象はOOD検出を困難にする
- この研究では、ニューラルネットワークの前層での極端な活性値を利用して対策
- 提案手法は複数の実験で現行のOOD検出ベースラインを改善し、性能も損なわない

「過信」を直す方法って面白いね！これが普及すれば、もっと安心してAI使えるようになるかも。

**Comment:** Accepted for the 40th Conference on Uncertainty in Artificial   Intelligence (UAI 2024)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-21 10:14

- - -

### [Maverick-Aware Shapley Valuation for Client Selection in Federated Learning](http://arxiv.org/abs/2405.12590)

**連合学習におけるクライアント選択のためのマーベリック対応シェープリー評価**

Mengwei Yang, Ismat Jarin, Baturalp Buyukates, Salman Avestimehr, Athina Markopoulou

- 連合学習はクライアントがプライベートデータを共有せず協力してモデルを訓練
- データの異質性が課題で、特に珍しいデータを持つクライアント（マーベリックス）の処理が重要
- マーベリックの貢献を公平に評価するためのシェープリー評価を設計し、ラベルごとにクライアントのシェープリー値を算出
- FedMSというマーベリック対応のクライアント選択メカニズムを提案し、より良いモデル性能と公平な報酬分配を実現

この研究、マーベリックをちゃんと活用することでモデルの性能が良くなるってところ、すごいね！連合学習の実用化に向けて、面白い進展があるかもって期待しちゃう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-21 08:34

- - -

### [Uncertainty quantification by block bootstrap for differentially private stochastic gradient descent](http://arxiv.org/abs/2405.12553)

**差分プライバシー確率的勾配降下法のためのブロックブートストラップによる不確実性定量化**

Holger Dette, Carina Graw

- 従来のSGDの不確実性定量化は差分プライバシーでは適用困難
- ローカル差分プライバシー下で計算可能な新しいブロックブートストラップ法を提案
- 新手法はプライバシー予算の調整なしで利用可能で、広範囲の推定問題に適用可能
- シミュレーション研究で手法の有効性と有限サンプル特性を証明

新しい方法でプライバシーを守りながら正確な結果を得られるってすごいね！未来のAI技術に大きな影響を与えるかもね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.CR, cs.LG, math.ST, stat.CO, stat.TH, **投稿日時:** 2024-05-21 07:47

- - -

### [Exploring and Exploiting the Asymmetric Valley of Deep Neural Networks](http://arxiv.org/abs/2405.12489)

**ディープニューラルネットワークの非対称的な谷の探索と利用**

Xin-Chun Li, Jin-Lin Tang, Bo Zhang, Lan Li, De-Chuan Zhan

- DNNの損失ランドスケープを探索し、谷の非対称性の要因や影響を調査
- データセット、ネットワークアーキテクチャ、初期化、ハイパーパラメータが収束点に与える影響を分析
- ノイズの大きさと方向が1次元可視化における谷の対称性と重要な関連があることを発見
- ReLUやsoftmaxによる理論的洞察が新たなモデルフュージョンの有効性につながることを示唆

谷の非対称性なんて考えたことなかった、面白い！ディープラーニングの理解がさらに深まりそうな予感♡



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-21 04:18

- - -

### [Leveraging Diverse Data Generation for Adaptable Zero-Shot Dialogue State Tracking](http://arxiv.org/abs/2405.12468)

**多様なデータ生成を活用した適応可能なゼロショット対話状態追跡**

James D. Finch, Boxin Zhao, Jinho D. Choi

- ゼロショット対話状態追跡（DST）の精度は、合成データ生成技術を用いた多様なデータの利用で向上する
- 現在のDSTトレーニング資源は、データ収集の高コストによりカバーするアプリケーションドメインやスロットタイプが限られている
- 新しい完全自動のデータ生成アプローチを用い、新ドメインの対話状態アノテーションやスロット説明付きデータを生成
- D0Tデータセットは1000以上のドメインをカバーし、合成データでトレーニングしたモデルはMultiWOZベンチマークで+6.7%の性能向上を達成

新しいアプローチで1000以上のドメインをカバーするのすごい！未来のAIってもっと賢くなりそうだね、ワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-05-21 03:04

- - -

### [On Measuring Calibration of Discrete Probabilistic Neural Networks](http://arxiv.org/abs/2405.12412)

**離散確率ニューラルネットワークのキャリブレーション測定に関する研究**

Spencer Young, Porter Jenkins

- 機械学習システムの安全性や信頼性の向上には、不確実性の正確な表現が重要である
- 最尤法を用いたニューラルネットワークの訓練が高次元確率分布への適応に有効
- 従来の指標である期待キャリブレーション誤差（ECE）や負の対数尤度（NLL）にはバイアスや仮定の限界がある
- 本研究では、バイアスや仮定なしでキャリブレーションの差異を測定するための条件付きカーネル平均埋め込み法を提案

キャリブレーションの問題を解決する新しい手法が出てきたよ。シンプルなデータでの実験結果も良い感じみたい。次はもっと複雑な応用が期待されるね、楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-05-20 23:30

- - -

### [Securing Blockchain-based IoT Systems with Physical Unclonable Functions and Zero-Knowledge Proofs](http://arxiv.org/abs/2405.12322)

**物理的クローン不可能関数とゼロ知識証明によるブロックチェーンベースのIoTシステムのセキュリティ強化**

Daniel Commey, Sena Hounsinou, Garth V. Crosby

- 物理的クローン不可能関数（PUF）を用いて、デバイスの一意な識別を実現
- ゼロ知識証明（ZKP）で、プライバシー保護の認証とトランザクション処理を行う
- ハイパーレッジャーファブリック環境でのフレームワークを提案し、その実験結果から性能とセキュリティを確認
- 提案フレームワークが、ブロックチェーンベースのIoTシステムにおけるセキュリティ課題を包括的に解決することを示す

PUFsとZKPsの組み合わせで、IoTシステムのセキュリティが大幅に強化されそう！この技術が普及したら、日常のデバイスもより安全になるね。



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.DC, cs.NI, **投稿日時:** 2024-05-20 18:40

- - -

### [Continual Deep Reinforcement Learning for Decentralized Satellite Routing](http://arxiv.org/abs/2405.12308)

**分散型衛星ルーティングのための継続的深層強化学習**

Federico Lozano-Cuadra, Beatriz Soret, Israel Leyva-Mayorga, Petar Popovski

- 部分的な知識と連続的な移動に対応し、時間変動する不確実性を克服する必要がある
- 各衛星が独立した意思決定エージェントとして、近隣エージェントからのフィードバックに基づいて限られた環境認識を得る
- オフライン学習フェーズでは分散型の意思決定とグローバルDNNを用い、オンラインフェーズでは継続的な学習を必要とする
- 提案されたマルチエージェントDRLフレームワークは、混雑が少ない場合に最短経路ソリューションと同等のE2E性能を達成し、混雑条件にも適応する

衛星同士が協力しながらルーティングを行うなんて、すごく未来的だね！制約がいっぱいある中で、技術の進化ってすごいなって思うよ。

**Comment:** 30 pages, 11 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, math.IT, **投稿日時:** 2024-05-20 18:12
