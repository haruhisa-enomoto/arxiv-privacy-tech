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

更新: 2024-12-18T04:24:01.603250

- - -

### [Are Data Experts Buying into Differentially Private Synthetic Data? Gathering Community Perspectives](http://arxiv.org/abs/2412.13030)

**データ専門家は差分プライバシーを備えた合成データにどの程度賛成しているのか？コミュニティの視点を集める**

Lucas Rosenblatt, Bill Howe, Julia Stoyanovich

- 差分プライバシー（DP）はアメリカで重要な技術だが、実務者のニーズに沿った指標が必要
- データ専門家のインタビューで、実データと合成データの成果に一貫性が必要と示唆
- 推奨として、十分に文書化されたケースの提供や分野別の標準の公表が必要
- 高プライバシーな低忠実度データでの熟練度に基づいた段階的データアクセス手法を提案

データの専門家たちが実際に差分プライバシーをどう活かしてるのか、知りたくなっちゃうね！階層的なデータアクセス方法とか、もっと研究が進むと私たちも安心してデータが利用できるかも。ちょっと未来が楽しみ！



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.HC, cs.CR, cs.DB, **投稿日時:** 2024-12-17 15:50

- - -

### [A Conceptual Model of Intelligent Multimedia Data Rendered using Flying Light Specks](http://arxiv.org/abs/2412.12938)

**飛翔する光の粒を用いたインテリジェントなマルチメディアデータの概念モデル**

Nima Yazdani, Hamed Alimohammadzadeh, Shahram Ghandeharizadeh

- FLSは小型ドローンで、3Dマルチメディアオブジェクトを照らすために設計されている
- FLSの群れがユーザーの触覚に力を返すことで、ハプティックインタラクションを提供する
- 本論文では、FLSディスプレイのデータにセマンティクスを追加し、マルチメディアリポジトリを拡張するモデルを提案
- 提案モデルがエンターテインメントとヘルスケアのアプリケーションでの拡張性を示す

この技術は、エンターテインメントだけじゃなくて、医療みたいな分野にも使えるんだね！未来のインタラクションってなんだかワクワクしちゃう！

**Comment:** Appeared in the First International Conference on Holodecks

**トピック:** [連合学習](fl), **カテゴリ:** cs.DB, cs.ET, cs.MM, **投稿日時:** 2024-12-17 14:18

- - -

### [Concurrent vertical and horizontal federated learning with fuzzy cognitive maps](http://arxiv.org/abs/2412.12844)

**あいまい認知マップを用いた同時垂直・水平連合学習**

Jose L Salmeron, Irina Arévalo

- データプライバシーは医療や金融で重要な課題である
- 連合学習は参加者がデータプライバシーを守りつつモデルを共同訓練する手法
- 非IIDデータの課題対策として新しい枠組みを提案、あいまい認知マップを使用
- 4つのフェデレーション戦略で実験し、学習成果とプライバシーの両立を確認

データを安心して使えるって大事だよね！この研究で、非IIDデータでもちゃんと連合学習できる可能性が広がりそう。ワクワクするね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-17 12:11

- - -

### [Building Gradient Bridges: Label Leakage from Restricted Gradient Sharing in Federated Learning](http://arxiv.org/abs/2412.12640)

**勾配の架け橋を作る: 連合学習における制限付き勾配共有からのラベル漏洩**

Rui Zhang, Ka-Ho Chow, Ping Li

- 連合学習での勾配共有がラベル漏洩の攻撃対象となり得る
- 既存の軽量な防御手法は勾配の共有を制限するが不十分
- 新たな攻撃手法GDBRを提案し、勾配情報からラベル分布を復元
- GDBRは80%以上のラベルを高い精度でフードバック可能と実験で判明

新しい攻撃法がいきなり80%のラベルを復元できちゃうのはスゴイ！これからもっと安全な防御策が求められるね。連合学習の未来がますます気になっちゃう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-17 08:03

- - -

### [SynthCypher: A Fully Synthetic Data Generation Framework for Text-to-Cypher Querying in Knowledge Graphs](http://arxiv.org/abs/2412.12612)

**SynthCypher: 知識グラフのText-to-Cypherクエリ生成のための完全合成データ生成フレームワーク**

Aman Tiwari, Shiva Krishna Reddy Malay, Vikas Yadav, Masoud Hashemi, Sathwik Tejaswi Madhusudhan

- Cypherクエリ生成(Text2Cypher)は、Neo4jのグラフデータベース向けに重要であるが、未開拓の問題である
- SynthCypherは新しいLLMSupervisedフレームワークを採用し、多様なドメインとクエリの複雑性に対応する
- 29.8kのText2Cypherインスタンスを含む大規模なベンチマークデータセットを生成し、精度向上につなげる
- 合成データを用いることで、Text2Cypherタスクで最先端技術の向上を達成可能であることを示す

すごく面白そう！合成データでこんなにパフォーマンスが上がるなんて、他の分野にも応用できる可能性があるかもね。どんなクエリも巧みに理解できるAIとか、考えただけでワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.IR, cs.LG, **投稿日時:** 2024-12-17 07:21

- - -

### [Libri2Vox Dataset: Target Speaker Extraction with Diverse Speaker Conditions and Synthetic Data](http://arxiv.org/abs/2412.12512)

**Libri2Voxデータセット: 多様な話者条件および合成データによるターゲット話者抽出**

Yun Liu, Xuechen Liu, Xiaoxiao Miao, Junichi Yamagishi

- 現在のターゲット話者抽出はデータの多様性や現実世界でのロバスト性が課題
- LibriTTSとVoxCeleb2を組み合わせたLibri2Voxデータセットを提案、ノイズ下での多様な話者実現
- 合成話者生成とカリキュラム学習でデータ多様性と段階的なモデル訓練を向上
- 実験でSpeakerBeamが1.39dB改善、Conformerは追加で0.78dBの改善を達成

ターゲット話者抽出の研究がどんどん進化していて面白いね！これでノイズの多い環境でも、もっとクリアに話者を特定できそう。今後の音声アプリも期待大だね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, eess.AS, **投稿日時:** 2024-12-17 04:06

- - -

### [if-ZKP: Intel FPGA-Based Acceleration of Zero Knowledge Proofs](http://arxiv.org/abs/2412.12481)

**if-ZKP: インテルFPGAによるゼロ知識証明のアクセラレーション**

Shahzad Ahmad Butt, Benjamin Reynolds, Veeraraghavan Ramamurthy, Xiao Xiao, Pohrong Chu, Setareh Sharifian, Sergey Gribok, Bogdan Pasca

- ゼロ知識証明（ZKP）はプライバシー保護に重要だが、従来はスケーラビリティの問題があった
- zk-SNARKsがこの問題を解決し、多くのパブリックライブラリで実装が進む
- 本研究は、FPGA上でzk-SNARKの証明者計算を加速するスケーラブルなアーキテクチャを提案
- MSM計算の並列性を活かし、インテルOneAPIを使って110x-150xの高速化を実現

すごい、ZKPの高速化でプライバシー技術が一気に進化しそう！FPGAを使ったこのアプローチ、様々な分野で応用されそうでめっちゃおもしろーい！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.AR, cs.CR, **投稿日時:** 2024-12-17 02:35

- - -

### [Differential Privacy Preserving Distributed Quantum Computing](http://arxiv.org/abs/2412.12387)

**差分プライバシー保持分散型量子計算**

Hui Zhong, Keyi Ju, Jiachen Shen, Xinyue Zhang, Xiaoqi Qin, Ohtsuki Tomoaki, Miao Pan, Zhu Han

- 既存の量子コンピュータはNISQ状態でしか動作できず、QDCがその制限を克服する手段とされる
- 量子分散計算にもプライバシー漏洩の問題があり、既存研究では中央量子計算向けにQDPが導入された
- 本研究は、QDCに適用可能な新しい概念QRDPを提案し、クラシカルなR\'enyi DPの利点を取り入れる
- シミュレーションではノイズ追加でデータ利用性が減少するが、プライバシー保護水準が向上することが示された

量子計算に差分プライバシーを導入するなんておもしろいね！QRDPって新しい発想で、量子の複雑さを活かしたプライバシーの守り方になりそう。きっと未来のコンピューティングに貢献するような先進的な研究だね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** quant-ph, cs.DC, **投稿日時:** 2024-12-16 22:46

- - -

### [F-RBA: A Federated Learning-based Framework for Risk-based Authentication](http://arxiv.org/abs/2412.12324)

**F-RBA: リスクベース認証のための連合学習ベースのフレームワーク**

Hamidreza Fereidouni, Abdelhakim Senhaji Hafid, Dimitrios Makrakis, Yaser Baseri

- インターネットの発展により、私的データ保護の重要性が高まっている
- F-RBAは、データをローカルに保ちながら学習を分散する連合学習を活用
- 類似性に基づく特徴量工学で、連合環境でのデータ異質性問題に対応
- 実験により、不正ログイン検出で優れた成績を示し、従来モデルを上回る

リスクベース認証と連合学習を組み合わせて攻撃リスクとプライバシーを両立するフレームワークだって！分散環境でのスムーズな適応が期待できそうだし、インターネットの未来が楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-12-16 19:42

- - -

### [SprayCraft: Graph-Based Route Optimization for Variable Rate Precision Spraying](http://arxiv.org/abs/2412.12176)

**SprayCraft: 変動施肥精密噴霧のためのグラフベースルート最適化**

Kiran K. Kethineni, Saraju P. Mohanty, Elias Kougianos, Sanjukta Bhowmick, Laavanya Rachakonda

- 植物病害管理のために、IoATを統合したA-CPSが開発されている
- 病害の広がりは病巣から徐々に減衰する感染密度の勾配があり、精度高い変動施肥が必要
- SprayCraftは、グラフベース手法で病害のホットスポットを特定し、噴霧ドローンの最適経路を計算
- グラフ上でメッセージパッシングを行い、病害ホットスポットの確率を計算し、精密な変動施肥に活用

この技術、未来の農業がもっと効率的になるのに役立ちそうだよね。ドローンが自動で病気を見つけてピンポイントで対策できるなんて、まさにハイテク農業って感じ！

**Comment:** 28 pages, 40 figures, 2 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.OH, cs.SY, eess.SY, **投稿日時:** 2024-12-12 22:46
