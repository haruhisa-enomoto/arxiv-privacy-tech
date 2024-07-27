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

更新: 2024-07-27T04:19:09.703346

- - -

### [VGGHeads: A Large-Scale Synthetic Dataset for 3D Human Heads](http://arxiv.org/abs/2407.18245)

**VGGHeads: 大規模な3D人間の頭部用合成データセット**

Orest Kupyn, Eugene Khvedchenia, Christian Rupprecht

- 実世界のデータセットはバイアスやプライバシー、倫理的な懸念がある
- 拡散モデルを用いて1百万枚以上の高解像度画像で構成される合成データセットを導入
- 新しいモデルアーキテクチャにより、単一の画像から頭部検出と3Dメッシュ再構築を同時に実現
- 合成データ上で訓練されたモデルは、実画像でも高いパフォーマンスを達成

このデータセット、いろんなタスクに使えそうでワクワクする！他の分野でも再利用できるなんて、めっちゃ便利だね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-07-25 17:58

- - -

### [Sparse Incremental Aggregation in Multi-Hop Federated Learning](http://arxiv.org/abs/2407.18200)

**マルチホップ連合学習におけるスパースインクリメンタルアグリゲーション**

Sourav Mukherjee, Nasrin Razmi, Armin Dekorsy, Petar Popovski, Bho Matthiesen

- 連合学習をマルチホップ通信環境で調査し、特に衛星間リンクでの適用を検討
- 各中間ホップでのインクリメンタルアグリゲーションにより通信効率を大幅に向上
- 勾配スパース化の下でインクリメンタルアグリゲーションの効果が減少する問題を解明
- 新たな関連スパース化手法を提案し、通信効率が15倍、最先端のスパースIAと比較して11倍改善

勾配スパース化の問題点を解決しつつ効率を上げるなんて、すごいじゃん！連合学習がさらに実用的になりそうね。

**Comment:** This paper is accepted for the 25th IEEE International Workshop on   Signal Processing Advances in Wireless Communications (SPAWC) conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, eess.SP, **投稿日時:** 2024-07-25 17:09

- - -

### [Enhanced Privacy Bound for Shuffle Model with Personalized Privacy](http://arxiv.org/abs/2407.18157)

**個別化プライバシーを用いたシャッフルモデルの強化されたプライバシー境界**

Yixuan Liu, Yuhan Liu, Li Xiong, Yujie Gu, Hong Chen

- シャッフルモデルは、ローカルユーザーとデータ管理者の間に中間の信頼サーバーを導入することで中央DPの保証を増幅
- 個々のユーザーごとに異なるプライバシー設定を必要とする実用的な環境での中央プライバシー境界を導出
- クローン生成の確率と隣接データセット間のクローン分布の区別不能性を定量化
- 仮説検定と$f$-DPの凸性の利用により、既存の結果よりも精度の高いプライバシー境界を提供

たとえプライバシー設定が個別でも、しっかり守れるっていいよね！私も安心してデータ使える未来を期待しちゃうなぁ。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-07-25 16:11

- - -

### [Privacy Threats and Countermeasures in Federated Learning for Internet of Things: A Systematic Review](http://arxiv.org/abs/2407.18096)

**IoT向けの連合学習におけるプライバシー脅威と対策: 系統的レビュー**

Adel ElZemity, Budi Arief

- IoT環境での連合学習は、分散データを活用するが、プライバシーとセキュリティの懸念を引き起こす
- 系統的文献レビューを通じ、49本の論文を分析しIoTでのプライバシー脅威と対策を評価
- 推論攻撃やポイズニング攻撃、盗聴などの脅威を特定し、差分プライバシーや秘密計算などの防御策を検討
- 軽量な防御策やブロックチェーンなどの新技術を活用し、IoTの変動ネットワーク条件下でFLのプライバシーを向上させる必要がある

IoTと連合学習とか、面白そう！新しい技術でどうやって脅威に対応するか、もっと知りたいなぁ。未来の研究に繋がる話ばかりでわくわくするね！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-07-25 15:01

- - -

### [Lightweight Industrial Cohorted Federated Learning for Heterogeneous Assets](http://arxiv.org/abs/2407.17999)

**異種資産向け軽量産業用コホート連合学習**

Madapu Amarlingam, Abhishek Wani, Adarsh NL

- 連合学習(FL)は、データを共有せずにクライアント間で学習を交換することにより、分散機械学習(ML)モデルを訓練するための最も広く採用されている協調学習手法である
- しかし、FLはデータの類似性や均質性が前提となっており、産業用環境には特化されていない
- 提案する軽量産業用コホートFL(LICFL)アルゴリズムは、モデルパラメータを使用してコホーティングを行い、データの異質性に起因する欠点を軽減する
- 数値実験を通じて、提案アルゴリズムの有効性を実証し、既存の手法と比較した結果、性能向上が確認された

産業用データが対象だから、現場での実用性が高そう！FLの質を保ちながらもデータの異質性を考慮したアプローチ、これから増えそうな感じするよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-07-25 12:48

- - -

### [On the Effect of Purely Synthetic Training Data for Different Automatic Speech Recognition Architectures](http://arxiv.org/abs/2407.17997)

**様々な自動音声認識アーキテクチャに対する純粋な合成訓練データの効果について**

Nick Rossenbach, Benedikt Hilmes, Ralf Schlüter

- 合成データを利用して自動音声認識（ASR）の訓練を評価
- Text-to-Speech（TTS）システムで合成データ生成、ASRシステムを合成データで訓練
- 三つの異なるASRアーキテクチャで合成データの影響を比較
- 合成データと実データの効果比較のため、様々なアブレーション研究を実施

合成データだけでこれだけ違うって、すごいと思わない？今後のASRの発展が楽しみだね！

**Comment:** Accepted at the SynData4GenAI 2024 workshop

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, cs.SD, eess.AS, **投稿日時:** 2024-07-25 12:44

- - -

### [RDFGraphGen: A Synthetic RDF Graph Generator based on SHACL Constraints](http://arxiv.org/abs/2407.17941)

**RDFGraphGen: SHACL制約に基づく合成RDFグラフ生成器**

Marija Vecovska, Milos Jovanovik

- RDFGraphGenはSHACL制約に基づいた一般用途・ドメイン独立の合成RDFグラフ生成器である
- SHACLは既存のRDFデータを検証するための標準だが、データセット不足を解決するため、逆の役割で合成データ生成に利用
- 制約抽出、ルール化、ルールに基づく人工データ生成のプロセスを経てRDFエンティティを生成
- RDFGraphGenはベンチマーク、テスト、品質管理、トレーニングなどの用途に利用可能なオープンソースのPythonパッケージ

これ、めっちゃ面白い！データが足りない問題をこんなふうに解決できるなんて、素晴らしいよね✨ 合成データの生成でテストとかトレーニングが楽になる未来が見えるね！

**Comment:** 19 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.SE, cs.DB, **投稿日時:** 2024-07-25 10:58

- - -

### [HF-Fed: Hierarchical based customized Federated Learning Framework for X-Ray Imaging](http://arxiv.org/abs/2407.17780)

**HF-Fed: X線画像のための階層的なカスタマイズされた連合学習フレームワーク**

Tajamul Ashraf, Tisha Madame

- X線技術は非侵襲的検査で重要だが、放射線リスクが課題
- 従来の深層学習法はデータ集中化が必要で、プライバシー問題がある
- HF-Fedは問題を局所データ適応と全体的なX線画像に分解して解決
- 実験結果はデータ共有なしで競争力のある性能を示し、医療分野の連合学習に寄与

連合学習を活用することで、各病院のデータを共有せずに高品質なX線画像を実現するアプローチは未来的！将来的にさらに多様な医療画像に応用できるかもね。



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-07-25 05:21

- - -

### [Mpox Detection Advanced: Rapid Epidemic Response Through Synthetic Data](http://arxiv.org/abs/2407.17762)

**Mpox検出の進化: 合成データによる迅速な疫病対応**

Yudara Kularathne, Prathapa Janitha, Sithira Ambepitiya, Prarththanan Sothyrajah, Thanveer Ahamed, Dinuka Wijesundara

- 疫病やバイオテロの早期対応には、迅速な疾患検出モデルの開発が重要
- 合成データを用いて様々な皮膚タイプのMpox病変画像を生成した新手法を提案
- 合成データで訓練したモデルが97%の精度を達成し、偽陽性を最小限に抑えた
- F1スコア96%、ほかの皮膚疾患では98%の高評価を示し、バランスの取れた性能を立証

合成データだけでこんな高精度を出せるなんてすごい！これからの医療緊急事態にも素早く対応できる未来が見えてくるよね。

**Comment:** 8 pages, 4 figures, 1 table

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-07-25 04:33

- - -

### [DualFed: Enjoying both Generalization and Personalization in Federated Learning via Hierachical Representations](http://arxiv.org/abs/2407.17754)

**DualFed：階層的表現を利用した連合学習での一般化と個人化の両立**

Guogang Zhu, Xuefeng Liu, Jianwei Niu, Shaojie Tang, Xinghao Wu, Jiayuan Zhang

- 個人化連合学習（PFL）では、モデルの一般化と効果的な個人化を同時に達成することが困難
- 階層的アーキテクチャを持つ深層モデルを利用し、複数の層からの表現を組み合わせるアプローチを提案
- DualFedはデュアル表現を直接生成する新手法で、一般化と個人化を簡易化し最適化
- 多くの実験でDualFedが他のFL手法よりも優れていることを示した

一般化と個人化の両方をうまく実現するってすごく難しそうだけど、この方法ならできちゃうんだね。使い方次第で色んなアプリケーションに役立ちそうだって思ったよ。

**Comment:** Accepted by ACM MutltiMedia 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-07-25 04:09

- - -

### [Spiking Neural Networks in Vertical Federated Learning: Performance Trade-offs](http://arxiv.org/abs/2407.17672)

**スパイキングニューラルネットワークを用いた垂直連合学習の性能トレードオフ**

Maryam Abbasihafshejani, Anindya Maiti, Murtuza Jadliwala

- 垂直連合学習は、異なる特徴を持つクライアント間でデータを共有しないモデル訓練方法
- SNNはANNに比べてエネルギー効率が高く、端末での高速かつ高精度な処理が可能
- SNNモデルの適用性を評価するため、モデル分割ありとなしの2つの連合学習アーキテクチャを実装
- CIFARデータセットを用いて評価し、SNNの精度はANNと同等でありながらエネルギー効率が高いことを示した

SNNがこれからの連合学習でもっと使われるかもね。効率良くなるなら、もっと多くのデバイスでも使えるようになるよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-24 23:31

- - -

### [The Power of Graph Sparsification in the Continual Release Model](http://arxiv.org/abs/2407.17619)

**継続的リリースモデルにおけるグラフ間引きの力**

Alessandro Epasto, Quanquan C. Liu, Tamalika Mukherjee, Felix Zhou

- 差分プライバシーのグラフ問題で、更新ごとにプライベートな解を生成する
- 非プライベートなストリーミンググラフアルゴリズムは近似的な解を出力し、サブリニアの空間を使用
- グラフ間引きを用いてエッジ差分プライバシーアルゴリズムがサブリニアの空間で動作
- 間引き技術でノード差分プライバシーの新しい結果を達成し、多くの問題に適用

グラフのスペース効率を大幅に改善するんだね！これにより、リアルタイムのプライバシー保護がより実現しやすくなるかも。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, **投稿日時:** 2024-07-24 20:15

- - -

### [Automated transport separation using the neural shifted proper orthogonal decomposition](http://arxiv.org/abs/2407.17539)

**ニューラルシフト固有直交分解を用いた輸送分離の自動化**

Beata Zorawski, Shubhaditya Burela, Philipp Krah, Arthur Marmin, Kai Schneider

- 輸送支配場を分解するために、シフト固有直交分解（sPOD）をニューラルネットで実現
- 従来のsPODは輸送オペレータの事前知識が必要で、現実問題では適用が難しい
- ニューラルネットで輸送と共動場を同時に推定する手法を提案
- 合成データと森林火災モデルで適用し、効果と効率を実証

ニューラルネットでのsPODって未来感あるよね〜。現実問題への応用が無限大なのがとってもわくわくしちゃう！

**Comment:** Proceedings not peer-reviewed yet. Code available:   https://github.com/MOR-transport/automated_NsPOD

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.NA, math.NA, physics.comp-ph, physics.flu-dyn, **投稿日時:** 2024-07-24 10:47

- - -

### [SFPrompt: Communication-Efficient Split Federated Fine-Tuning for Large Pre-Trained Models over Resource-Limited Devices](http://arxiv.org/abs/2407.17533)

**SFPrompt：リソース制限デバイス上で大規模事前学習モデルの通信効率の良い連合分割微調整**

Linxiao Cao, Yifei Zhu, Wei Gong

- 従来の微調整方法は、プライバシー懸念でデータにアクセスできない場合に不可能
- SFPromptは分割学習と連合学習を組み合わせ、リソース制限デバイスでの計算負荷を軽減
- 新しいデータセット剪定アルゴリズムとローカル損失更新戦略で通信コストを削減
- SFPromptは連合学習の完全な微調整に比べ、計算リソースを0.46%使用し、通信コストを53%削減

この研究、未来感満載で楽しい感じがする！特にリソース制限のあるデバイスでも使えるように工夫されてるのってすごく実用的だね～！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-07-24 04:22
