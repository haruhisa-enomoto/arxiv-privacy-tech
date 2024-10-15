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

更新: 2024-10-15T04:21:35.230383

- - -

### [SimpleStrat: Diversifying Language Model Generation with Stratification](http://arxiv.org/abs/2410.09038)

**SimpleStrat: 層別化による言語モデル生成の多様化**

Justin Wong, Yury Orlovskiy, Michael Luo, Sanjit A. Seshia, Joseph E. Gonzalez

- 大規模言語モデルの生成の多様性は計画や合成データ生成で重要
- 従来手法の温度増加は生成の質を低下させる可能性あり
- SimpleStratは言語モデル自身の層別化を用いる新しいアプローチ
- 提案手法は高いリコールとKLダイバージェンスの削減を達成

SimpleStratって面白そう！温度を変えるだけじゃなくて、層別化を使うところが斬新だね。多様性が必要な場面での新しい可能性が広がりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-10-11 17:54

- - -

### [From Interaction to Impact: Towards Safer AI Agents Through Understanding and Evaluating UI Operation Impacts](http://arxiv.org/abs/2410.09006)

**相互作用から影響へ：UI操作の影響を理解し評価することで安全なAIエージェントへ**

Zhuohao Jerry Zhang, Eldon Schoop, Jeffrey Nichols, Anuj Mahajan, Amanda Swearngin

- 自律AIエージェントのUI操作によるリスクや不可逆的な影響が未解明
- UI操作の影響を分類するため、専門家とワークショップを開き分類法を開発
- データ合成研究で現実的なUIスクリーンやユーザーが重要と考えるアクションデータを収集
- 大規模言語モデルはUI操作の影響理解能力に差があり、複雑な影響分類には穴がある

安全なAIエージェントの未来に向けて、UI操作の影響をもっと理解しようとしてるんだね。複雑な問題もあるみたいだけど、これが進めばAIともっと安心して暮らせる日は近いかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.HC, **投稿日時:** 2024-10-11 17:24

- - -

### [Evaluating Federated Kolmogorov-Arnold Networks on Non-IID Data](http://arxiv.org/abs/2410.08961)

**非独立同分布データにおける連合コルモゴロフ・アーノルドネットワークの評価**

Arthur Mendonça Sasse, Claudio Miceli de Farias

- 連合コルモゴロフ・アーノルドネットワーク（F-KANs）の評価はまだ初期段階にある
- Bスプラインとラジアル基底関数を用いたKANsとMLPsを比較
- MNIST分類タスクで100名のクライアントによる非独立同分布パーティションを用いた
- スプライン-KANsはMLPsと同等の精度を半分のラウンドで達成し、計算時間はやや増加

F-KANsは精度が高いのに効率も良さそう！非独立データでの連合学習って、便利そうな未来を感じちゃうね。

**Comment:** 10 pages, 5 figures, for associated code see   https://github.com/artsasse/fedkan

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-11 16:30

- - -

### [Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory](http://arxiv.org/abs/2410.08942)

**合成データの可能性を最大化する: ランダム行列理論からの洞察**

Aymane El Firdoussi, Mohamed El Amine Seddik, Soufiane Hayou, Reda Alami, Ahmed Alzubaidi, Hakim Hacid

- 合成データは大規模言語モデルの学習に注目されるが、低品質のデータは性能を損なう可能性がある
- データプルーニングは、スコア関数に基づき高品質のデータを保持する解決策の一つ
- ランダム行列理論を用いて、実データとプルーニングされた合成データで二値分類器の性能を分析
- 合成データが性能向上をもたらす条件を特定し、生成モデルの品質と検証戦略に焦点を当てる

この研究、合成データの質をちゃんと見極めれば、結構良い効果出せるかもね！データってどれも同じじゃないっていうのが面白いし、使い方次第でポテンシャルを引き出せるのがワクワクする♪



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, math.ST, stat.TH, **投稿日時:** 2024-10-11 16:09

- - -

### [The Effect of Personalization in FedProx: A Fine-grained Analysis on Statistical Accuracy and Communication Efficiency](http://arxiv.org/abs/2410.08934)

**FedProxにおけるパーソナライゼーションの効果：統計精度と通信効率の詳細分析**

Xin Yu, Zelin He, Ying Sun, Lingzhou Xue, Runze Li

- FedProxは正則化を通じてモデルのパーソナライゼーションを可能にする連合学習法
- 正則化の強度を決めることは難しく、不適切な設定は精度を低下させうるリスクがある
- 正則化が統計精度に与える影響を分析し、適切な強度設定の理論的ガイドラインを提供
- 個別化は通信複雑度を低下させ、計算コストの追加なしに効率を向上させることが示された

FedProxってただの連合学習じゃないんだねー！正規化をうまく設定することで、通信も効率化できるなんてすごいね！どんなデータセットでもうまくいくなんて、未来の技術の一歩を感じちゃう！



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.DC, cs.LG, math.ST, stat.CO, stat.TH, **投稿日時:** 2024-10-11 16:00

- - -

### [Federated Learning in Practice: Reflections and Projections](http://arxiv.org/abs/2410.08892)

**実践における連合学習: 振り返りと展望**

Katharine Daly, Hubert Eichner, Peter Kairouz, H. Brendan McMahan, Daniel Ramage, Zheng Xu

- 連合学習は複数のエンティティがデータを交換せずに共同でモデルを学習する技術
- GoogleやApple、Metaのシステムは、連合学習の実際の適用例を示している
- 課題はサーバー側の差分プライバシー保証の検証や異種デバイス間の調整
- 新たな連合学習フレームワークはプライバシー原則を優先し、未来の課題に対応

連合学習ってすごいね！みんなでデータをシェアせずに、匿名で一緒に学習できるなんて、まるで未来の技術みたい。これからさらに進化していくと、もっと便利なことができそうでワクワクするね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), [TEE](tee), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-10-11 15:10

- - -

### [The Good, the Bad and the Ugly: Watermarks, Transferable Attacks and Adversarial Defenses](http://arxiv.org/abs/2410.08864)

**善玉、悪玉、醜悪：透かし、移行可能攻撃、対敵防御**

Grzegorz Głuch, Berkant Turan, Sai Ganesh Nagarajan, Sebastian Pokutta

- バックドア型透かしと対敵防御をプレイヤー間でのインタラクティブなプロトコルとして形式化
- ほぼ全ての識別学習タスクには透かしか対敵防御のどちらかが存在する
- 移行可能攻撃はデータ分布と見分けがつかず効率的に防御策を欺くクエリを計算する
- 移行可能攻撃の存在と暗号学的手法の関連性が示され、計算複雑性が求められる

この論文って、防御と攻撃の関係性を深掘りしてて面白いね！どんなに巧妙な敵でも、きっと防御の道はあるよって感じがして希望が持てるなぁ。攻撃手法もやっぱりしっかり研究しないとダメってことだよね！

**Comment:** 42 pages, 6 figures, preliminary version published in ICML 2024   (Workshop on Theoretical Foundations of Foundation Models), see   https://openreview.net/pdf?id=WMaFRiggwV

**トピック:** [準同型暗号](he), **カテゴリ:** cs.LG, cs.AI, cs.CR, 68T01, 94A60, 91A99, **投稿日時:** 2024-10-11 14:44

- - -

### [Unlocking FedNL: Self-Contained Compute-Optimized Implementation](http://arxiv.org/abs/2410.08760)

**FedNLの解明: 自律的かつ計算最適化された実装**

Konstantin Burlachenko, Peter Richtárik

- 連合学習は分散型で学習モデルを共同訓練し、データ共有を不要にするパラダイム
- FedNLアルゴリズムは第二次手法をFLに適用する進展を示したがプロトタイプには課題がある
- FedNL-LS, FedNL-PPをシングル・マルチノード設定で実装し、壁時計時間を1000倍短縮
- 実用的な圧縮器を提案し、FedNLの理論を実現する新しい圧縮手法を導入

連合学習の現実的なチューニングってすごくクール！プロトタイプの_TIME短縮_により実用性が飛躍的にアップしそうだね。ますます連合学習の普及が進みそうで楽しみだなぁ。

**Comment:** 55 pages, 12 figures, 12 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.MS, cs.PF, math.OC, G.4; C.3; I.2.11, **投稿日時:** 2024-10-11 12:19

- - -

### [Privacy-Preserving Optimal State Estimation with Low Complexity via Cramér-Rao Lower Bound Approach](http://arxiv.org/abs/2410.08756)

**低複雑度でプライバシーを保護する最適状態推定：クレーマー・ラオ下界アプローチによる解法**

Liping Guo, Jimin Wang, Yanlong Zhao, Ji-Feng Zhang

- 動的システムの最適状態推定問題をプライバシー保護しつつ解決する方法を検討
- クレーマー・ラオ下界を用い、平均二乗誤差でプライバシーレベルを評価
- 制約付き最適化問題として定式化し、プライバシーと有用性のトレードオフを実現
- 提案手法は低複雑度で微分プライバシーを達成し、実例でその有効性を示す

この研究、プライバシー保護しながら精度も妥協しないっていうのがすごいね！しかもオンラインで計算できるなんて、今後の応用も楽しみだね～。いろんな分野で役に立ちそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-10-11 12:15

- - -

### [Gradients Stand-in for Defending Deep Leakage in Federated Learning](http://arxiv.org/abs/2410.08734)

**連合学習における深層リーク防御のための勾配の代替案**

H. Yi, H. Ren, C. Hu, Y. Li, J. Deng, X. Xie

- 連合学習は、感度の高いデータをローカルにしてモデル勾配のみをサーバーに送信しプライバシーを保護する手法。
- FLの勾配交換に脆弱性が指摘されており、新手法「AdaDefense」でこれを防ぐ。
- ローカル勾配の代わりにスタンドインを使用し、勾配リークを防ぎながらモデルの性能を維持する。
- 理論的枠組みによってプライベート情報の漏えいを防ぐ手法の有効性を立証し、ベンチマーク実験でモデルの一貫性と安全性を確認。

勾配リークってそんなに危ないんだね！でも、「AdaDefense」でそれを防ぎつつも性能も落ちないなんて、すごく興味深い！これからのプライバシー技術に大きな貢献しそうだよね。❤️



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-10-11 11:44

- - -

### [DistDD: Distributed Data Distillation Aggregation through Gradient Matching](http://arxiv.org/abs/2410.08665)

**DistDD: 勾配マッチングによる分散データ蒸留集約**

Peiran Wang, Haohan Wang

- DistDDは連合学習での通信を減らし、クライアント上で直接データを蒸留する手法
- 従来のモデル更新を要さず、一度の蒸留でグローバルなデータセットを抽出しプライバシーを確保
- DistDDで得たデータは、連合学習のパラメータ調整やニューラルアーキテクチャ検索に活用できる
- 実験結果で非独立同分布や誤ラベルデータにも頑強で、コミュニケーションコスト削減を証明

DistDDってすごく未来が見えるね！データを効率的に使って、もっと賢いAIモデルができそうな予感！私たちの身近なところでも役立つ日が楽しみ〜。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-11 09:43

- - -

### [Finite Sample Complexity Analysis of Binary Segmentation](http://arxiv.org/abs/2410.08654)

**有限サンプル複雑性におけるバイナリセグメンテーションの解析**

Toby Dylan Hocking

- バイナリセグメンテーションは損失関数を最適化する貪欲アルゴリズムであり、時空データの変化点検出に利用
- 理論上、最悪でも$O(N K)$、最良で$O(N \log K)$の時間で実行可能とされている
- 本研究では、有限なデータ数と分割数での時間と空間の複雑性を新たに解析する手法を提案
- 合成データを用いた実証分析で、バイナリセグメンテーションの速度が実用上ほぼ最適に近いことを示す

バイナリセグメンテーションってすごく速くできるんだね！実際のデータでほぼ最適なスピードが出るなんて、使い方が広がりそうでワクワクするね！🌟



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.CO, **投稿日時:** 2024-10-11 09:26

- - -

### [GAI-Enabled Explainable Personalized Federated Semi-Supervised Learning](http://arxiv.org/abs/2410.08634)

**GAIを活用した説明可能な個別化連合半教師あり学習**

Yubo Peng, Feibo Jiang, Li Dong, Kezhi Wang, Kun Yang

- 連合学習はモバイルユーザーのAIモデル訓練に使われるが、ラベル不足やデータの非IID性、説明不能性などの課題がある
- 提案するXPFLフレームワークは、生成AIを用いた個別化連合半教師あり学習GFedでローカルFLモデルを強化
- グローバル集約では、ローカルとグローバルFLモデルの知識を特定の割合で融合し、個別化を保ちながら知識を共有
- FLモデルの説明性を向上させるため、決定木とt-SNEを活用してモデルの入力と出力や集約前後の可視化を実現

生成AIを使ってラベル不足を補うアイデア、めっちゃ新しい！モデルの融合方法もよく考えられてて、個別化のまま力を合わせる感じがいいと思った～。可視化の部分も面白そう、データが目に見えるってすごいよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, math.IT, **投稿日時:** 2024-10-11 08:58

- - -

### [Balancing Innovation and Privacy: Data Security Strategies in Natural Language Processing Applications](http://arxiv.org/abs/2410.08553)

**革新とプライバシーのバランス：自然言語処理アプリケーションにおけるデータセキュリティ戦略**

Shaobo Liu, Guiran Liu, Binrong Zhu, Yuanshuai Luo, Linxiao Wu, Rui Wang

- 差分プライバシーに基づく新しいアルゴリズムを提案し、チャットボットや感情分析などでユーザーデータを保護する
- 差分プライバシー機構によりランダムノイズを追加し、情報漏洩リスクを削減しつつデータ処理を効果的に実現
- 従来のデータ匿名化や準同型暗号と比較して、計算効率とスケーラビリティにおいて優位性がある
- 各種性能指標で他の手法を上回り、プライバシーと有用性のバランスを効果的に実現

差分プライバシーを使ってるのがすごく面白いって思った！これからのNLPアプリは、安全に楽しめる時代になりそうだね。ユーザーのプライバシーを守りつつ、どんどん進化していく未来が楽しみ！



**トピック:** [差分プライバシー](dp), [準同型暗号](he), **カテゴリ:** cs.CR, cs.AI, cs.CL, **投稿日時:** 2024-10-11 06:05

- - -

### [Accelerated Distributed Stochastic Non-Convex Optimization over Time-Varying Directed Networks](http://arxiv.org/abs/2410.08508)

**時間変動する有向ネットワークにおける加速分散確率非凸最適化**

Yiyue Chen, Abolfazl Hashemi, Haris Vikalo

- 信号処理やコンピュータビジョン、自然言語処理など分散学習システムの応用で注目される。
- 時間変動する有向ネットワークをモデル化、通信遅延やストラグラー効果を考慮した分布設定。
- 勾配追跡とモメンタム付き確率的勾配降下法を用いて、非凸最適化問題を解決するアルゴリズムを提案。
- 提案手法は既存手法を上回る性能を示し、様々な学習タスクで有効であることを実証。

分散学習システムが活躍する未来がますます近づいてきた感じ！この手法でさらに色んなタスクが効率よくできちゃうのかな？MNISTやCIFAR-10みたいな有名な学習タスクで試されてるところもすごく興味深いね！

**Comment:** This work has been accepted at IEEE Transactions on Automatic Control

**トピック:** [連合学習](fl), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-10-11 04:18

- - -

### [Quantum Operating System Support for Quantum Trusted Execution Environments](http://arxiv.org/abs/2410.08486)

**量子信頼実行環境のための量子OSサポート**

Theodoros Trochatos, Jakub Szefer

- クラウドベースの量子計算では、計算の機密性と完全性が重要
- 量子信頼実行環境(QTEE)は、ユーザーの量子回路を保護
- QTEEの展開には、QTEEのハードウェアと操作をサポートする量子OSが必要
- 初の量子OSアーキテクチャを紹介し、セキュアな量子タスク実行を実現

量子技術が身近になるのって未来っぽいよね！クラウドで安全に量子計算できるようになるなら、新しいアプリとかどんどん出てきそうでわくわくする～！



**トピック:** [TEE](tee), **カテゴリ:** quant-ph, cs.AR, cs.CR, **投稿日時:** 2024-10-11 03:27

- - -

### [Driving Privacy Forward: Mitigating Information Leakage within Smart Vehicles through Synthetic Data Generation](http://arxiv.org/abs/2410.08462)

**プライバシーを前進させる: 合成データ生成によるスマート車両での情報漏えいの軽減**

Krish Parikh

- スマート車両のデータは機密性が高いため、情報漏えいのリスクがある
- 攻撃者は匿名化メタデータを利用してドライバーをプロファイル可能
- 合成データは実データの相関を保ちつつ機密情報漏えいのリスクを軽減
- Tabular Variational Autoencoderで生成したデータは90.1%の統計類似性を達成

合成データでスマート車両のプライバシー問題を改善する方法って面白いよね！データを守りながらも便利な技術を活かせる可能性があるなんて、未来の車社会がもっと安全になりそうでワクワクするなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-10-11 02:28

- - -

### [JurEE not Judges: safeguarding llm interactions with small, specialised Encoder Ensembles](http://arxiv.org/abs/2410.08442)

**JurEEではなくJudges: 小規模で専門化されたエンコーダーエンセmblesによってLLMインタラクションを保護する**

Dom Nasrabadi

- JurEEはLLMベースシステム内でのAIユーザー間のインタラクションを強化するエンコーダー専用のトランスフォーマーモデルのエンセmbles
- 既存のLLM-as-Judge法が苦手なリスク分類の一般化に強く、確率的なリスク推定を提供
- 多様なデータソースを活用し合成データ生成技術を用いてモデルの堅牢性と性能を向上させる
- 発言の精度や速さ、コスト効果に優れたJurEEは顧客向けチャットボットなど厳格なコンテンツモデレーションが必要なアプリケーションに適している

JurEEが従来のLLMよりも効率的で経済的な選択肢になるってすごいよね！今後もっと広がって、多くのアプリで使われそうなのがワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-11 01:20

- - -

### [Evaluating Differentially Private Synthetic Data Generation in High-Stakes Domains](http://arxiv.org/abs/2410.08327)

**高リスク領域における差分プライバシー合成データ生成の評価**

Krithika Ramesh, Nupoor Gandhi, Pulkit Madaan, Lisa Bauer, Charith Peris, Anjalie Field

- 差分プライバシー言語モデルによる合成データ生成を試みた研究
- 実際の高リスク領域における合成データの利用を提案
- シンプルな評価では気づかなかった有用性、プライバシー、公平性の課題を指摘
- 合成データ生成の改善がプライバシーデータ共有の実現に不可欠と強調

高リスクな分野でのデータ共有の壁を合成データで突破しようとしてるのね！プライバシーを守りつつ、みんなが使いやすいデータになるといいなって思うな。革新的な技術で未来が切り開かれるかもってワクワクしちゃう！

**Comment:** Accepted to EMNLP 2024 (Findings)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-10 19:31

- - -

### [Randomized Asymmetric Chain of LoRA: The First Meaningful Theoretical Framework for Low-Rank Adaptation](http://arxiv.org/abs/2410.08305)

**ランダム化非対称LoRAチェーン：低ランク適応の初の有意義な理論フレームワーク**

Grigory Malinovsky, Umberto Michieli, Hasan Abed Al Kader Hammoud, Taha Ceritli, Hayder Elesedy, Mete Ozay, Peter Richtárik

- LoRAは効率的なファインチューニング手法だが、フルパラメータファインチューニングと比べると性能が劣ることがある。
- LoRAやその拡張には収束の問題があることを示し、これを解決するためにRAC-LoRAを提案。
- RAC-LoRAはLoRAの経験的な利点を活かしつつ、収束が証明された方法に変えるための小さなアルゴリズム調整を加える。
- 提案手法はFPFTへの収束を理論的に保証し、スムーズな非凸損失関数への収束分析も行い、その結果を実験で支持。

RAC-LoRAがLoRAの弱点を補強して、理論的な裏付けを提供しているのが面白いな！これからの研究で、実際の応用が楽しみだね。技術的な部分もだけど、実験結果と理論がマッチしてるところがすごい！

**Comment:** 36 pages, 4 figures, 2 algorithms

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, math.OC, **投稿日時:** 2024-10-10 18:51

- - -

### [Privately Learning from Graphs with Applications in Fine-tuning Large Language Models](http://arxiv.org/abs/2410.08299)

**グラフからのプライベートな学習と大規模言語モデルの微調整への応用**

Haoteng Yin, Rongzhe Wei, Eli Chien, Pan Li

- グラフは、テキストや画像といったデータと共に関係性の洞察を提供し、AIモデルの能力を拡張する。
- 金融や医療などの分野では、プライベート情報を含むため、関係データのプライバシー保護が重要である。
- 提案手法は、サンプルされた関係の依存性を分離し、DP-SGDを活用して差分プライバシーを確保する。
- 提案手法により、LLMのプライバシーを維持しつつも関係学習タスクの性能を向上させることができる。

グラフからプライバシーを守って学ぶって、すごく未来的じゃない？これでプライバシーを気にせずにAIがさらに賢くなるなんて、どんな発展があるのかワクワクだよね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CL, cs.CR, **投稿日時:** 2024-10-10 18:38

- - -

### [Increasing the Difficulty of Automatically Generated Questions via Reinforcement Learning with Synthetic Preference](http://arxiv.org/abs/2410.08289)

**強化学習と合成嗜好を用いた自動生成質問の難易度向上**

William Thorne, Ambrose Robinson, Bohua Peng, Chenghua Lin, Diana Maynard

- 文化遺産セクターでの個別化検索のために特化した評価データセットが求められている
- ドメイン特化型MRCデータセットを強化学習と合成嗜好データで低コスト生成する手法を提示
- 質問の難しさを既存モデルの正答率で測定し、PPOと合成データで難易度を向上させる
- 手法の効果を示す実験結果、誤り分析、オープンソースコードを提供

文化遺産のデータに特化した難しい質問を自動で作るなんて、この技術すごく知的じゃない？たくさんの難しい質問に対応できたら、文化遺産の理解がもっと広がりそうで、未来が楽しみだね！

**Comment:** is to be published in NLP4DH 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, 68T50 (Primary) 91F20 (Secondary), I.2.7; J.5, **投稿日時:** 2024-10-10 18:21

- - -

### [Federated Graph Learning for Cross-Domain Recommendation](http://arxiv.org/abs/2410.08249)

**クロスドメイン推薦のための連合グラフ学習**

Ziqi Yang, Zhaopeng Peng, Zihui Wang, Jianzhong Qi, Chaochao Chen, Weike Pan, Chenglu Wen, Cheng Wang, Xiaoliang Fan

- クロスドメイン推薦（CDR）はデータ不足を解消するが、プライバシーや負の転移のリスクがあり多ドメインで課題。
- FedGCDRという新しい連合グラフ学習フレームワークを提案し、複数のソースドメインから安全に正の知識を活用。
- 差分プライバシーに基づく知識抽出と特徴マッピングで、フェデレーショングラフから信頼できるドメイン知識を生成。
- 知識活性化モジュールで負の転移を防ぎつつ、ターゲットモデルを微調整し、精度の高い予測を実現。

この論文って、連合学習を使ってめっちゃ賢く複数のデータを使い分けるってことかな！プライバシーもちゃんと守りつつ、精度の高い予測ができるようになるなんてすごい！きっと未来のレコメンドシステムがもっと便利に進化しそうな予感がするよね。

**Comment:** Accepted by NeurIPS'24

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-10 12:19

- - -

### [RAB-DEF: Dynamic and explainable defense against adversarial attacks in Federated Learning to fair poor clients](http://arxiv.org/abs/2410.08244)

**RAB$^2$-DEF: 連合学習における貧弱なクライアントに対してフェアな動的で説明可能な敵対的攻撃防御**

Nuria Rodríguez-Barroso, M. Victoria Luzón, Francisco Herrera

- 連合学習はデータプライバシー問題解決の手法として提案されている
- 既存の防御メカニズムは敵対的攻撃に対してのみ焦点を当て、他の重要な特性を無視している
- RAB$^2$-DEFは動的で説明可能、貧弱なクライアントにフェアな敵対的攻撃防御を提案
- 画像データセットでのテストで、既存の防御に比べて信頼性のあるAI実現に貢献すると判明

なんかすごい！連合学習の問題を解決して、貧弱なクライアントにも優しいところが素敵だね。もっといろんな攻撃に強いAIができそうで、未来が楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-10-10 09:32
