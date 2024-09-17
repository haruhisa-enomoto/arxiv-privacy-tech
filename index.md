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

更新: 2024-09-17T04:19:47.858319

- - -

### [An Efficient Self-Learning Framework For Interactive Spoken Dialog Systems](http://arxiv.org/abs/2409.10515)

**対話型音声対話システムのための効率的な自己学習フレームワーク**

Hitesh Tulsiani, David M. Chan, Shalini Ghosh, Garima Lalwani, Prabhat Pandey, Ankish Bansal, Sri Garimella, Ariya Rastrow, Björn Hoffmeister

- 伝統的なASRシステムは各ターンを独立して認識するため、対話の文脈適応が困難
- 新たなASRフレームワークは単一ターン発話を超えて、逐次学習とユーザーフィードバックを取り入れる
- 学生-教師学習や文脈認識対話処理を利用し、オンラインハードネガティブマイニング（Ohm）を導入
- 新フレームワークにより、実際の対話システムでWERが約10%減少、合成データで最大26%減少

この研究、ASRの進化によりもっと快適な音声インターフェースが作れそうだね！これからの音声アシスタントがさらに賢くなるのが楽しみ！

**Comment:** Presented at ICML 2024

**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.AI, cs.CL, cs.SD, **投稿日時:** 2024-09-16 17:59

- - -

### [TPFL: Tsetlin-Personalized Federated Learning with Confidence-Based Clustering](http://arxiv.org/abs/2409.10392)

**TPFL：信頼度に基づくクラスタリングを用いたツェトリン個別化連合学習**

Rasoul Jafari Gohari, Laya Aliahmadipour, Ezat Valipour

- ツェトリンマシン（TM）アルゴリズムを使用することで、連合学習（FL）の新しいアプローチを提案
- モデルを特定のクラスに対する信頼度に基づいてクラスタリングする手法を採用
- 非IIDデータに対して誤った重みの集約を排除し、信頼度の高いデータのみを共有する点が利点
- 通信コストを大幅に削減し、精度と効率の両方で優れた結果を示した

ツェトリンマシンを使って連合学習の新たな道を開くなんて、めっちゃ興味深い！これでさらにプライバシーが守られつつ、効率もアップできるんだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-09-16 15:27

- - -

### [Enhancing Image Classification in Small and Unbalanced Datasets through Synthetic Data Augmentation](http://arxiv.org/abs/2409.10286)

**小規模で不均衡なデータセットにおける画像分類の向上：合成データによる拡張**

Neil De La Fuente, Mireia Majó, Irina Luzko, Henry Córdova, Gloria Fernández-Esparrach, Jorge Bernal

- 目標クラス間の不均衡とデータセットの小規模さは医療画像分類の大きな課題
- クラス特異的な変分オートエンコーダー（VAE）と潜在空間の補間を用いた新しい合成拡張戦略を提案
- 合成データで特徴空間のギャップを埋めることでデータの不足とクラス不均衡を解消
- 実験結果では、最も困難なクラスの精度が18%以上向上し、全体的な精度と精密度も改善

この研究、めっちゃおもしろそう！特に、合成データで医療画像の分類精度が上がるなんて未来感すごいね！どんどん実用化されていくといいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-09-16 13:47

- - -

### [PrePaMS: Privacy-Preserving Participant Management System for Studies with Rewards and Prerequisites](http://arxiv.org/abs/2409.10192)

**PrePaMS: 報酬と前提条件を持つ研究のためのプライバシー保護参加者管理システム**

Echo Meißner, Frank Kargl, Benjamin Erb, Felix Engelmann

- 報酬を介して参加者を増やすが、これまでプライバシー保護に注意を払わなかった
- PrePaMSは前提条件チェックと報酬支払いをプライバシー保護方式で実現
- 匿名認証やゼロ知識証明などの暗号技術を使用して参加者の身元を隠す
- プロトタイプの設計・実装と現実的な負荷条件下での性能評価を行った

報酬の手続きまでプライバシーを保護するシステムってすごいよね！これが広まったら、もっと安心して参加できる人が増えそう。

**Comment:** Prototype source code: https://github.com/vs-uulm/prepams/ Public   test deployment: https://vs-uulm.github.io/prepams/

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-16 11:35

- - -

### [RealDiff: Real-world 3D Shape Completion using Self-Supervised Diffusion Models](http://arxiv.org/abs/2409.10180)

**RealDiff: 自己教師付き拡散モデルを用いた実世界の3D形状補完**

Başak Melis Öcal, Maxim Tatarchenko, Sezer Karaoglu, Theo Gevers

- ポイントクラウド補完は部分的な観測からオブジェクトの完全な3D形状を回復するもの
- RealDiffは、実世界の観測データを直接使用し、自己教師付きの拡散プロセスを提案
- 合成データの代わりに追加の幾何学的手掛かりを利用してノイズの多い観測データに対処
- 実験結果により、RealDiffが最先端の手法を一貫して上回ることを示している

実世界のデータにそのまま適用できるのがすごいよね！もうちょっと調べてみたら、もっと面白い技術が見つかりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-16 11:18

- - -

### [SplatSim: Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using Gaussian Splatting](http://arxiv.org/abs/2409.10161)

**スプラットシム: ガウシアン・スプラッティングを使用したRGB操作ポリシーのゼロショットSim2Real転送**

Mohammad Nomaan Qureshi, Sparsh Garg, Francisco Yandun, David Held, George Kantor, Abhishesh Silwal

- RGB画像に依存する操作ポリシーのSim2Real転送は、視覚データのドメインシフトが原因で難しい
- SplatSimは、シミュレータ内のメッシュ表現をガウシアン・スプラッツに置き換える新しい手法を提案
- この手法により、フォトリアリスティックな合成データを生成し、シミュレーションの拡張性とコスト効率を維持
- 実世界でのゼロショット展開で、SplatSimが86.25%の成功率を達成し、従来の97.5%に迫る成果を示した

ガウシアン・スプラッティングでシミュレーションと実世界の差を縮めるアイデアが面白いね！実際のロボット操作がもっと効率的になりそうで新しい応用が期待できそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.AI, cs.CV, cs.LG, **投稿日時:** 2024-09-16 10:52

- - -

### [Generating Synthetic Free-text Medical Records with Low Re-identification Risk using Masked Language Modeling](http://arxiv.org/abs/2409.09831)

**マスクされた言語モデルを用いた再識別リスクの低い合成フリーテキスト医療記録の生成**

Samuel Belkadi, Libo Ren, Nicolo Micheletti, Lifeng Han, Goran Nenadic

- マスクされた言語モデル（MLM）を使用し、退院要約、入院記録、医師の書簡などの合成医療記録を生成
- Philterを用いて保護された健康情報（PHI）をマスクし、医療実体認識（NER）モデルで重要な医療情報を保持
- 合成データは多様性を持ちつつHIPAA準拠のPHI再現率0.96、再識別リスク0.035を達成
- 合成データは実データと同等の性能でモデルをトレーニング可能で、特定の使用ケースに適応できる柔軟性を持つ

医療の分野でプライバシーを守りながら重要なデータを使えるのがすごいね！MLMを使ってるところも新しい感じがして、おもしろそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-09-15 19:11

- - -

### [WASD - Water Saving Devise](http://arxiv.org/abs/2409.09798)

**WASD - 水節約装置**

Samuele Rebecchi, Samuele Marcellino, Luca Magoni

- 世界的な飲料水不足に対処するための革新的な自動システムを提案
- 既存の家庭内の水再利用システムは高コストでメンテナンスが頻繁
- WASDはセンサーとソレノイドバルブを使用し、迅速に清浄水をトイレタンクに送る
- 低コストで使いやすいアプローチによって、持続可能な水利用を促進

この装置が家庭の水利用を劇的に効率化できるかもね。これからの水不足問題に大きく貢献する未来が見える気がする！



**トピック:** [連合学習](fl), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-09-15 17:20

- - -

### [Federated Learning in Adversarial Environments: Testbed Design and Poisoning Resilience in Cybersecurity](http://arxiv.org/abs/2409.09794)

**対敵環境における連合学習：テストベッド設計とサイバーセキュリティにおける毒性耐性**

Hao Jian Huang, Bekzod Iskandarov, Mizanur Rahman, Hakan T. Otal, M. Abdullah Canbaz

- サイバーセキュリティ分野で連合学習のテストベッドを設計し実装
- Flowerフレームワークを使用し、パフォーマンスやスケーラビリティを評価
- 連合型侵入検知システムにより異常検知とネットワークデータの保護を実現
- 毒性攻撃に対するデータおよびモデルの堅牢性を評価、課題を浮き彫りに

サイバーセキュリティに連合学習を応用するなんて興味深いね。毒性攻撃への耐性とか、たくさんの課題を乗り越えた未来が見えてきそう。

**Comment:** 7 pages, 4 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, cs.LG, 68T05, 68M14, 68M15, I.2.11; I.2.6; C.2.4; K.6.5, **投稿日時:** 2024-09-15 17:04

- - -

### [From Challenges and Pitfalls to Recommendations and Opportunities: Implementing Federated Learning in Healthcare](http://arxiv.org/abs/2409.09727)

**課題と落とし穴からの提言と機会：ヘルスケアにおける連合学習の実装**

Ming Li, Pengcheng Xu, Junjie Hu, Zeyu Tang, Guang Yang

- 連合学習は大規模なヘルスケア研究と複数センター間のコラボレーションを可能にするが、データプライバシーとセキュリティが守られる
- 最近の研究の多くは連合学習を提案または利用しているが、臨床実用性のあるものは不明
- メソッドの欠陥やプライバシー問題、一般化の課題、通信コストが原因で大多数の研究は臨床利用に不適
- この問題を克服するための提言と有望な機会を提示し、モデル開発の質を改善する方法を提供

連合学習って、すごくヘルスケアに役立ちそうだけど、色々な問題もあるんだね。でも、この論文ではその問題を乗り越えるための提案があるから、実用化の可能性が広がりそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-15 13:11

- - -

### [Nebula: Efficient, Private and Accurate Histogram Estimation](http://arxiv.org/abs/2409.09676)

**Nebula: 効率的でプライベートかつ正確なヒストグラム推定**

Ali Shahin Shamsabadi, Peter Snyder, Ralph Giles, Aurélien Bellet, Hamed Haddadi

- Nebulaは、同時にプライバシー漏洩の厳格な上限を達成
- 現実的な信頼条件下でのクライアントプライバシーを保証
- 多人数計算や信頼できるハードウェアを避けながら、標準的なローカル差分プライバシーシステムよりも大幅に良い有用性を実現
- アメリカ合衆国の国勢調査データセットで88%以上の有用性向上を示し、マルチ次元データの送信も可能

Nebula、なんかすごくユニークで面白そう！特に信頼できないサーバーでも高性能を実現できるのが未来のプライバシー技術に感じるよ！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-15 09:55

- - -

### [A Statistical Viewpoint on Differential Privacy: Hypothesis Testing, Representation and Blackwell's Theorem](http://arxiv.org/abs/2409.09558)

**差分プライバシーの統計的視点：仮説検定、表現方法、そしてブラックウェルの定理**

Weijie J. Su

- 差分プライバシーは、プライバシー保護のあるデータ解析のための形式的なプライバシーであり、幅広い分野で採用されている
- 差分プライバシーを仮説検定の観点から捉えることで、その定義が統計的手法に基づくことを示す
- $f$-差分プライバシーを定義し、既存の差分プライバシーの定義を拡張する表現定理を提示
- この手法を用いたプライバシー境界の分析が、プライベートディープラーニングや合成データにおいて有益であることを実証

仮説検定とプライバシーが絡んでくるのが興味深いね。これで差分プライバシーがもっと理解しやすくなるといいなって思う！

**Comment:** To appear in Annual Review of Statistics and Its Application

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, math.ST, stat.ML, stat.TH, **投稿日時:** 2024-09-14 23:47

- - -

### [Ensuring System-Level Protection against Eavesdropping Adversaries in Distributed Dynamical Systems](http://arxiv.org/abs/2409.09539)

**分散動的システムにおける盗聴攻撃者に対するシステムレベルの保護の確保**

Dipankar Maity, Van Sy Mai

- 分散動的システムの状態を盗聴攻撃者から守る方法を提案
- 現行の分散アルゴリズムは、攻撃者に最終状態が推測されやすい脆弱性がある
- 通信するのはエージェントの状態ではなくイノベーション信号にすることで基本的な保護が実現可能
- 既存の研究が暗号化や差分プライバシー技術を追加するのに対し、新たに根本的な保護方針を紹介

技術的な工夫でこんなに違うんだね！新しいアプローチでより安全なシステムが作れるかも、すごく興味深い！



**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-09-14 21:40

- - -

### [Using Synthetic Data to Mitigate Unfairness and Preserve Privacy through Single-Shot Federated Learning](http://arxiv.org/abs/2409.09532)

**合成データを用いた単発連合学習による不公平性緩和とプライバシー保護**

Chia-Yuan Wu, Frank E. Curtis, Daniel P. Robinson

- 従来のFL手法は頻繁なモデルパラメータ更新と通信で、顧客情報の漏えいや高い通信コストが課題
- 我々の提案は、顧客とサーバー間の情報交換を省き、不公平性を緩和しつつデータ漏えいを防ぐ
- 各顧客のローカルデータセットを用いて、不公平性の問題を考慮した合成データセットを生成
- 合成データをサーバーで集めてモデルを訓練することで、公平性の特定重み付けを回避し、プライバシーを保護

合成データを使って効率的に公平性を保ちながら、プライバシーも保護するなんてすごいね！通信回数が少なくて済むから、通信コストも下がるっていうのもいい感じ。



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.CY, math.OC, G.1.6; I.2.6; C.2.4; K.4.1; D.4.6, **投稿日時:** 2024-09-14 21:04

- - -

### [Leveraging Foundation Models for Efficient Federated Learning in Resource-restricted Edge Networks](http://arxiv.org/abs/2409.09273)

**リソース制約のあるエッジネットワークにおける効率的な連合学習のための基盤モデルの活用**

S. Kawa Atapour, S. Jamal SeyedMohammadi, S. Mohammad Sheikholeslami, Jamshid Abouei, Konstantinos N. Plataniotis, Arash Mohammadi

- 基盤モデル（FM）は連合学習（FL）と組み合わせることで下流タスクのトレーニングとプライバシー保護を向上させる
- 本論文は、基盤モデルをエッジデバイスにローカルにデプロイすることなく利用する新たなフレームワーク「FedD2P」を提案
- FedD2Pは、IoTデバイスの集約された知識をプロンプトジェネレーターに蒸留し、基盤モデルを下流タスクに適応させる
- 公開データセットへの依存をなくすため、各クラスのローカル知識とクラスの言語記述を利用してプロンプトジェネレーターをトレーニング

新しいフレームワーク「FedD2P」めっちゃ気になる！エッジデバイスに基盤モデルを直接適用しなくても、高性能が期待できるってすごいんじゃない？実験結果も楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-09-14 02:54

- - -

### [Batched Online Contextual Sparse Bandits with Sequential Inclusion of Features](http://arxiv.org/abs/2409.09199)

**バッチオンライン文脈疎バンディットの特徴の順次選択**

Rowan Swiers, Subash Prabanantham, Andrew Maher

- 文脈バンディット問題に線形報酬、スパース性、バッチデータの条件を適用
- 公平性を考慮し、関連のない特徴を排除する新しいアルゴリズムを提案
- OBSIアルゴリズムが、それらの特徴の影響に対する信頼が増すにつれて特徴を順次選択
- 合成データにおいて、他のアルゴリズムに比べて後悔、使用された特徴の関連性、計算上で優れた性能を示す

特徴の順次選択によって、不要な情報を排除しながら効率化を図るところが超おもしろいね！やっぱり、ユーザ体験を最適化するための技術がどんどん進化していくのがすごい！

**Comment:** 4 pages, 4 figures, Accepted at the CONSEQUENCES 24 workshop,   co-located with ACM RecSys 24

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-09-13 21:22

- - -

### [Exploring Biological Neuronal Correlations with Quantum Generative Models](http://arxiv.org/abs/2409.09125)

**量子生成モデルを用いた生物学的神経相関の探求**

Vinicius Hernandes, Eliska Greplova

- 生物学的神経ネットワークの情報処理理解は現在の大きな科学的課題
- 古典モデルは多くのパラメータを必要とし、解釈性が困難
- 量子機械学習は少ないパラメータで効率的な訓練が可能
- 量子生成モデルは生物学的神経活動の空間的・時間的相関を捉える合成データ生成ができる

量子コンピューティングが神経科学の未来を切り拓くなんてワクワクするね！次のブレイクスルーになるかも知れないし、探求してみたいな。

**Comment:** 33 pages, 14 figures, code: https://gitlab.com/QMAI/papers/spiqgan

**トピック:** [合成データ](sd), **カテゴリ:** quant-ph, cs.LG, cs.NE, q-bio.NC, **投稿日時:** 2024-09-13 18:00
