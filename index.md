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

更新: 2024-10-05T04:22:30.018112

- - -

### [Training Language Models on Synthetic Edit Sequences Improves Code Synthesis](http://arxiv.org/abs/2410.02749)

**合成編集シーケンスを用いた言語モデルの訓練によるコード合成の改善**

Ulyana Piterbarg, Lerrel Pinto, Rob Fergus

- ソフトウェアエンジニアは既存のプログラムを編集するが、大規模言語モデル（LLM）は一度に合成する
- 高品質の編集データは入手困難であり、その不足を補うためにLintSeqという合成データ生成アルゴリズムを開発
- LintSeqはコードを編集シーケンスとしてテキスト出力し、命令+プログラムペアを編集シーケンスに変換する
- 合成編集シーケンスで微調整した小型LLMは、GPT-4に匹敵し、特にHumanEvalでは+20%性能向上を示す

合成データでトレーニングすると、既存のモデルよりもパフォーマンスが向上するみたい！将来はもっと小型のデバイスで、高度なコード生成ができるかもね。すごく楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CL, **投稿日時:** 2024-10-03 17:57

- - -

### [Data Similarity-Based One-Shot Clustering for Multi-Task Hierarchical Federated Learning](http://arxiv.org/abs/2410.02733)

**データ類似性に基づくマルチタスク階層型連合学習のためのワンショットクラスタリング**

Abdulmoneam Ali, Ahmed Arafa

- 無秩序なタスクに対応するため、同一タスクのユーザをクラスタリングして共同学習を可能にする
- ユーザ間のデータ類似性に基づくワンショットクラスタリングアルゴリズムを提案
- プライバシーの懸念、通信負荷、事前知識不要などの課題を克服
- CIFAR-10やFashion MNISTでの実験により、精度や分散削減でベースラインを上回る性能を示す

この研究おもしろそう〜！いろんなタスクを一斉に効率的に学習できるって、まるでチームプレーみたいでワクワクするね。技術もプライバシー守りつつ進化してて、みんなが協力して良い結果を出せる時代が来るといいな！

**Comment:** To appear in Asilomar 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, cs.NI, eess.SP, math.IT, **投稿日時:** 2024-10-03 17:51

- - -

### [AlphaIntegrator: Transformer Action Search for Symbolic Integration Proofs](http://arxiv.org/abs/2410.02666)

**AlphaIntegrator: シンボリック積分証明のためのトランスフォーマー行動探索**

Mert Ünsal, Timon Gehr, Martin Vechev

- 数学的積分をステップごとに行う学習ベースのシステムを初めて提案
- GPTトランスフォーマーモデルで、積分ルールを導くポリシー学習を実現
- 準同型暗号的な正しい動作と合成データ上での強力な一般化を達成
- 標準的なLLMの微調整では解決困難、新たな創造的手法の重要性を指摘

新しい積分のアイデア超おもしろそう！知識とシンボリックな推論の組み合わせで、新しい数学の可能性が広がるかもね。こういう革新が、いろんな学問で役立ちそうな気がする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.SC, **投稿日時:** 2024-10-03 16:50

- - -

### [Plots Unlock Time-Series Understanding in Multimodal Models](http://arxiv.org/abs/2410.02637)

**プロットが時系列理解をマルチモーダルモデルで解き明かす**

Mayank Daswani, Mathias M. J. Bellaiche, Marc Wilson, Desislav Ivanov, Mikhail Papkov, Eva Schnider, Jing Tang, Kay Lamerigts, Gabriela Botea, Michael A. Sanchez, Yojan Patel, Shruthi Prabhakara, Shravya Shetty, Umesh Telang

- マルチモーダルモデルはテキスト以外のデータも扱えるが、時系列データ解析では未活用
- 視覚化で時系列データを「見る」手法を提案し、モデルの再トレーニングを不要に
- 時系列データを視覚化することで最大90%のモデルAPIコスト削減を実現
- プロットの使用でゼロショットタスクで120%、実世界タスクで150%の性能向上を確認

マルチモーダルモデルって視覚的な認識力も持ってるのね！時系列データをプロットにすると解析がすごく効率的になるんだ。これ、将来的には医療やフィンテック分野で大活躍な予感！

**Comment:** 49 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CV, **投稿日時:** 2024-10-03 16:23

- - -

### [Personalized Quantum Federated Learning for Privacy Image Classification](http://arxiv.org/abs/2410.02547)

**プライバシー画像分類のための個別量子連合学習**

Jinjing Shi, Tian Chen, Shichao Zhang, Xuelong Li

- 量子連合学習はプライバシー画像分類を改善するが、クライアントモデルの個別性に欠ける課題がある
- 個別量子連合学習アルゴリズムを提案し、不均衡な画像分布でもクライアントモデルの個別性を強化
- 提案手法は、FashionMNISTデータセットで非個別モデルより7%高い精度でサーバーとクライアントで性能を向上
- 追加訓練なしにモデルとデータのプライバシーを守り、量子技術の普及と効果的な分散機械学習を促進

量子技術を使った連合学習で、個別性をちゃんと考慮しているのが新しいよね！これからどんどんセキュリティや効率が良くなる未来を考えるとワクワクしちゃう。みんなにとって便利な技術になるといいなって思うな。



**トピック:** [連合学習](fl), **カテゴリ:** quant-ph, cs.AI, **投稿日時:** 2024-10-03 14:53

- - -

### [Efficient learning of differential network in multi-source non-paranormal graphical models](http://arxiv.org/abs/2410.02496)

**複数ソース非正規分布グラフモデルにおける差分ネットワークの効率的学習**

Mojtaba Nikahd, Seyed Abolfazl Motahari

- 非正規分布グラフモデル間の差分ネットワークを学習し、ラッソペナルティを最適化
- 計算の複雑さが低く、特に差分ネットワークがスパースな場合に効率的
- 合成データでのシミュレーションにおいて、スピードと精度の面で既存手法を上回る
- 複数のソースからデータを組み合わせることで、実世界での差分ネットワーク推定が効果的

非正規分布のモデル間でどのように情報を効率的に学習するかって本当に興味深いよね！この手法が実際の医療研究で活かされる未来が楽しみ！新しいものが見つかるかも。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-03 13:59

- - -

### [Encryption-Friendly LLM Architecture](http://arxiv.org/abs/2410.02486)

**暗号化に優しいLLMアーキテクチャ**

Donghwan Rho, Taeseong Kim, Minje Park, Jung Woo Kim, Hyunsik Chae, Jung Hee Cheon, Ernest K. Ryu

- 大規模言語モデルは個別応答を提供するが、プライバシーが大きな課題である
- 準同型暗号は暗号状態で計算可能にし、プライバシー保護に寄与
- 変換器の計算負荷が課題、そこで変換器アーキテクチャを改良
- 新手法でチューニングや推論速度が向上、結果は平文モデルと同等

これからプライバシーを大事にしつつ、パーソナライズされたサービスができるって素敵だよね！機械学習の未来がもっと楽しくなるかも！

**Comment:** 27 pages

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-10-03 13:48

- - -

### [Personalized Federated Learning for Generative AI-Assisted Semantic Communications](http://arxiv.org/abs/2410.02450)

**ジェネレーティブAI支援による意味通信のための個別化連合学習**

Yubo Peng, Feibo Jiang, Li Dong, Kezhi Wang, Kun Yang

- セマンティック通信は意味情報のみを送信し、モバイルユーザーによるスペクトル資源の利用を効率化
- 新たに提案されたGSCモデルは、ジェネレーティブAIを活用した通信改善を目指す
- 個別化連合学習を導入し、プライバシーを保ちながらモバイルユーザーの多様な要求に対応
- 特にPLDとAGPを用いて通信エネルギーを削減し、モデルの効率化と効果を実現

これってすごく面白そう！モバイル通信がより効率的になれば、もっとスムーズに情報交換できるよね。未来の通信技術がどう発展するか、目が離せない！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.IT, math.IT, **投稿日時:** 2024-10-03 12:52

- - -

### [Clinnova Federated Learning Proof of Concept: Key Takeaways from a Cross-border Collaboration](http://arxiv.org/abs/2410.02443)

**Clinnova連合学習概念実証: 国境を越えたコラボレーションからの主要な教訓**

Julia Alekseenko, Bram Stieltjes, Michael Bach, Melanie Boerries, Oliver Opitz, Alexandros Karargyris, Nicolas Padoy

- フランス、ドイツ、スイス、ルクセンブルクが連携し、データの連合化と標準化により精密医療を促進
- AIとデータサイエンスを駆使して、医療成果と効率を向上させるヨーロッパの統一基準を構築
- 統合され連携されたアルゴリズムで個別化医療を推進し、MS患者のデジタルバイオマーカーを検証
- MSセグメンテーションでの国境を超えた連合学習の概念実証において技術的、倫理的な課題が浮き彫りに

異文化が交わる連携って、とっても力強いね！課題も多そうだけど、それを超えるデータ活用が未来の医療をどう変えるか楽しみだな。それに、欧州の巨匠たちがどんなAIを作るのか、ワクワクしちゃうね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-10-03 12:40

- - -

### [Federated Reinforcement Learning to Optimize Teleoperated Driving Networks](http://arxiv.org/abs/2410.02312)

**連合強化学習による遠隔操作運転ネットワークの最適化**

Filippo Bragato, Marco Giordani, Michele Zorzi

- 第6世代(6G)技術は信頼性と低遅延が重要で、特に遠隔操作運転で要求される。
- 学習強化を用いて、ネットワーク条件に応じたTDアプリの動的設定を提案。
- 複数のRLアルゴリズムを使用し、連合学習で収束時間や公平性を向上。
- Q-ラーニングが少数パラメータで最適なPQoSを提供し、平均報酬や計算コストが良好。

最適化のために連合学習を活用するの面白そう！未来の遠隔操作技術が更に進化しそうでワクワクする。QoSとQoEのトレードオフを解決するための詳細なアプローチが気になるね。

**Comment:** This paper has been accepted for publication at IEEE Global   Communications Conference (GLOBECOM), 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, **投稿日時:** 2024-10-03 08:51

- - -

### [FedScalar: A Communication efficient Federated Learning](http://arxiv.org/abs/2410.02260)

**FedScalar: 通信効率の良い連合学習**

M. Rostami, S. S. Kia

- 連合学習はプライバシーを守るが、大規模問題では通信コストが課題
- FedScalarはエージェント間通信をスカラーで行い通信効率を向上
- 提案手法は非凸損失関数で$O(1/\sqrt{K})$の収束率を実現
- ランダムベクトルの分布調整で集約ステップの分散を低減可能

めっちゃ面白そう！FedScalarが連合学習の通信の問題をすっごく効率的にしてくれるんだ。数学的にもしっかり証明してるから、実生活にもすぐ役立ちそうだよね。どんな応用ができるのか楽しみ〜！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-03 07:06

- - -

### [Probabilistic road classification in historical maps using synthetic data and deep learning](http://arxiv.org/abs/2410.02250)

**合成データとディープラーニングを活用した歴史的地図における確率的道路分類**

Dominik J. Mühlematter, Sebastian Schweizer, Chenjing Jiao, Xue Xia, Magnus Heitzler, Lorenz Hurni

- 歴史的地図から道路ネットワークをデジタル化するのはコストが高く時間がかかる
- 提案された新しいフレームワークは、ラベルなしでの道路幾何学の抽出と分類を実現
- 合成データを用いて、道路クラスのピクセル単位の確率を予測するディープラーニングを実施
- スイスのSiegfried地図で94%以上の正確度を達成し、都市計画に有用

地図って時代を超えていろんな情報を教えてくれるね！技術が発展して、昔の地図からも効率的にデータが引き出せるようになってくると、都市計画とかにももっと活かせそうでワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-10-03 06:43

- - -

### [PFGuard: A Generative Framework with Privacy and Fairness Safeguards](http://arxiv.org/abs/2410.02246)

**PFGuard: プライバシーと公平性を確保した生成フレームワーク**

Soyeon Kim, Yuji Roh, Geon Heo, Steven Euijong Whang

- 生成モデルは信頼性のためにプライバシーと公平性の両方を確保する必要がある
- プライバシーと公平性技術を単純に組み合わせても、対立が発生し十分でないことがある
- PFGuardは、複数の教師モデルのアンサンブルを使用しプライバシーと公平性の対立を解決
- 高次元データにおいて合成データを生成しつつ、公平性収束と厳密なDP保証を提供する

PFGuardってすごいよね！データのプライバシーと公平性を同時に守る方法を見つけたなんて、考えただけでワクワクしちゃう！これでAIの信頼性がさらにアップするかもね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-03 06:37

- - -

### [A Survey on Point-of-Interest Recommendation: Models, Architectures, and Security](http://arxiv.org/abs/2410.02191)

**地点推薦に関する調査：モデル、アーキテクチャ、セキュリティ**

Qianru Zhang, Peng Yang, Junliang Yu, Haixin Wang, Xingwei He, Siu-Ming Yiu, Hongzhi Yin

- スマートフォンと位置情報型ソーシャルネットワークの普及により、地点推薦システムにとっての機会が拡大。
- 伝統的なアプローチではなく、新しいモデルやセキュリティを考慮した最新の地点推薦システムを包括的にレビュー。
- 地点推薦の進化として、集中的から分散型・連合学習システムへ移行し、プライバシーと拡張性が向上。
- セキュリティの重要性が増しており、潜在的な脆弱性とプライバシー保護の方法を検討。

最新技術の進化を詳しく知ることで、新しい方向性を見つけられるのは面白いよね。セキュリティとプライバシーがどんどん大事になっていくのも納得だし、自分に合ったおすすめができる時代ってワクワクするよね。

**Comment:** 20 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, cs.AI, cs.CE, cs.LG, **投稿日時:** 2024-10-03 04:11

- - -

### [Active Learning of Deep Neural Networks via Gradient-Free Cutting Planes](http://arxiv.org/abs/2410.02145)

**勾配を使わないカッティングプレーンによる深層ニューラルネットワークのアクティブラーニング**

Erica Zhang, Fangzhao Zhang, Mert Pilanci

- アクティブラーニングは機械学習のサンプル複雑性を向上させる方法の一つ
- 本研究ではReLUネットワークにおける勾配不要のカッティングプレーン法を提案
- 非線形な決定境界を持つ深層ニューラルネットへの拡張が初めて示された
- 提案手法は収束保証を達成し、既存手法と比較して有効性を実験で実証

勾配を使わなくてもカッティングプレーン法って深層ニューラルネットワークでも使えるんだね！それに、収束保証までつけたアクティブラーニングの手法ってちょっとすごい気がするよ。新しい可能性を感じるなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, math.OC, **投稿日時:** 2024-10-03 02:11

- - -

### [Deep Generative Modeling for Identification of Noisy, Non-Stationary Dynamical Systems](http://arxiv.org/abs/2410.02079)

**ノイズと非定常な動的システムの識別のための深層生成モデリング**

Doris Voina, Steven Brunton, J. Nathan Kutz

- 時間変化する測定データの差分方程式復元は難しい課題
- 提案手法は動的SINDyで、時変係数の疎ODAモデル化を行う
- variational inferenceを用い、不確実性を評価しながら自律動的モデル化
- 合成データとC. elegansのニューロン活動データで手法を検証

この研究すっごく面白いね！ノンステーショナリティにも対応できるなら、もっと広い分野で活用されそう！データ生かしていく未来が楽しみだね。

**Comment:** 19 pages + 7 figures + Supplementary Materials (and supplementary   figures)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, q-bio.QM, **投稿日時:** 2024-10-02 23:00

- - -

### [Synthio: Augmenting Small-Scale Audio Classification Datasets with Synthetic Data](http://arxiv.org/abs/2410.02056)

**Synthio: 合成データによる小規模音声分類データセットの拡張**

Sreyan Ghosh, Sonal Kumar, Zhifeng Kong, Rafael Valle, Bryan Catanzaro, Dinesh Manocha

- 小規模データセットの音声分類精度向上を目指し、合成データで拡張
- 従来の人工変換手法は、多様性を表現し切れない問題がある
- T2A拡散モデルでの合成音声生成により、多様性と一貫性を両立
- 提案手法はベースラインを0.1%-39%上回る成果を示した

合成音声データで音声分類の精度を上げるなんてすごい！テキストから音声を生成する技術がここまで進化しているとはね。どんな音声が生成されるのか試してみたいな。

**Comment:** Code and Checkpoints will be soon available here:   https://github.com/Sreyan88/Synthio

**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.AI, cs.CL, **投稿日時:** 2024-10-02 22:05

- - -

### [EAB-FL: Exacerbating Algorithmic Bias through Model Poisoning Attacks in Federated Learning](http://arxiv.org/abs/2410.02042)

**EAB-FL: 連合学習におけるモデル改ざん攻撃によるアルゴリズムバイアスの悪化**

Syed Irfan Ali Meerza, Jian Liu

- 連合学習はプライバシーを保ちながらモデルを共同訓練する技術
- 異なるデータと参加者により、モデルに人種や性別のバイアスが生じる
- 一部の悪意ある参加者による攻撃が、バイアスやモデル精度を低下させる可能性
- 提案されたEAB-FL攻撃が公平性を悪化させつつ、モデルの有用性を保持することを実証

攻撃によって公平性が揺らぐって、なんだか怖いよね。でも、これを理解して対策を考えることが、公平な社会を作るのに役立ちそう！もっと安全で公平な技術が広まればいいなって思ったよ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-10-02 21:22

- - -

### [Addressing Data Heterogeneity in Federated Learning with Adaptive Normalization-Free Feature Recalibration](http://arxiv.org/abs/2410.02006)

**連合学習におけるデータの不均一性を適応的な正規化不要の特徴再調整で解決**

Vasilis Siomos, Sergio Naval-Marimont, Jonathan Passerat-Palmbach, Giacomo Tarroni

- 連合学習は分散協調訓練手法でデータオーナーシップを保持しつつ性能向上を図る。
- クライアント間の統計的異質性がシステム性能を低下させる課題を解決するためにANFRを提案。
- ANFRは重み標準化とチャンネルアテンションを組み合わせ、クライアント間での不一致を抑制。
- 差分プライバシー下でも強力なプライバシー保証を維持しつつ性能を犠牲にしない。

新しい手法を提案することで、連合学習をもっと効率的にできるんだね。特に異質性っていう難しい問題を解決しつつプライバシーを守れるっていうのが魅力的。もっと色んな現場で応用されるとすごく面白そう！

**Comment:** 10 pages

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2024-10-02 20:16

- - -

### [Differentially Private Parameter-Efficient Fine-tuning for Large ASR Models](http://arxiv.org/abs/2410.01948)

**大型ASRモデルのための差分プライバシーによるパラメーター効率良好な微調整**

Hongbin Liu, Lun Wang, Om Thakkar, Abhradeep Thakurta, Arun Narayanan

- 大型ASRモデルは差分プライバシーを用いることでプライバシー漏れを軽減できる。
- 従来の差分プライバシー訓練は計算コストが高く、モデル性能に悪影響を及ぼす可能性がある。
- 差分プライバシーを考慮したパラメーター効率良好な微調整で計算と性能のコストを削減。
- 微調整で新しい性能基準を達成し、(10, 3.52e-6)-DPを維持しながら優れた結果を報告。

大規模モデルで安全性と効率性の両立ができるなんて素敵じゃない？機械学習の未来がますます楽しみだよね！プライバシーを守りつつ、高性能も実現する技術がさらに進化しそうでワクワクする。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-02 18:49

- - -

### [NTK-DFL: Enhancing Decentralized Federated Learning in Heterogeneous Settings via Neural Tangent Kernel](http://arxiv.org/abs/2410.01922)

**NTK-DFL: ニューラルタンジェントカーネルによる異種環境での分散型連合学習の向上**

Gabriel Thompson, Kai Yue, Chau-Wai Wong, Huaiyu Dai

- 分散型連合学習(DFL)は中央サーバーや生データ交換なしでモデルをトレーニングするフレームワーク。
- 統計的異質性が課題だが、NTKアプローチを用いることで効率的な収束とデータ異質性の克服を実現。
- NTKを利用し、分散設定でのクライアントモデルを強化し、モデル平均化とシナジーを導入。
- 提案手法はモデル認識力を向上させ、通信ラウンドが4.6分の1で目標を達成し正確性を向上。

分散型でもNTKを活用すれば精度や効率がぐんとアップするなんてワクワクだね！通信が少なくても済むのは、特に多様な環境で協力が必要な状況にぴったりかも。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-02 18:19
