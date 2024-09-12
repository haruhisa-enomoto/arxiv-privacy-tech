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

更新: 2024-09-12T04:22:14.765663

- - -

### [Synthetic continued pretraining](http://arxiv.org/abs/2409.07431)

**合成継続事前学習**

Zitong Yang, Neil Band, Shuangping Li, Emmanuel Candès, Tatsunori Hashimoto

- 大規模な非構造化インターネットテキスト上での事前学習は、言語モデルに多くの世界知識を与える
- 知識習得はデータ効率が悪く、多様な表現で数百から数千回の学習が必要
- 小規模な特定分野コーパスを用いて合成データを生成し、合成継続事前学習を提案
- EntiGraphアルゴリズムにより、合成データ補強が可能で、知識の再配置を実現

特定分野に強いAIを作る方法として、これは革命的かも！小さいデータでも効率的に学べるなんて最高♪



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, stat.ML, **投稿日時:** 2024-09-11 17:21

- - -

### [Federated Impression for Learning with Distributed Heterogeneous Data](http://arxiv.org/abs/2409.07351)

**分散異種データを用いた学習のための連合的印象**

Sana Ayromlou, Atrin Arya, Armin Saadat, Purang Abolmaesumi, Xiaoxiao Li

- 標準的な深層学習ベースの分類アプローチは、すべてのサンプルを集中収集する必要があり、現実の臨床応用には非現実的
- FL（連合学習）はデータを共有せずにクライアント間で分散データから学習でき、プライバシーとデータの所有権問題を緩和できる
- データヘテロジニティにより、局所トレーニング中に破滅的忘却が発生しやすくなる
- FedImpresを提案し、合成データを連合的印象として復元し、グローバルな情報を表現することで破滅的忘却を軽減

データヘテロジニティ問題も解決して、FLで20%も精度がアップするなんてすごくない？それに、医療分野での実用化が進むと患者さんにも優しいね！



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CV, cs.DC, **投稿日時:** 2024-09-11 15:37

- - -

### [Federated -armed Bandit with Flexible Personalisation](http://arxiv.org/abs/2409.07251)

**柔軟なパーソナライゼーションを備えた連合$\mathcal{X}$-armedバンディット**

Ali Arabzadeh, James A. Grant, David S. Leslie

- 個別クライアントの嗜好と集約された全体的な知識を組み合わせた代替目的関数を使用
- パーソナライゼーションと集団学習の間で柔軟なトレードオフを可能にする方法を提案
- サブリニアリグレットと対数的通信オーバーヘッドを達成するフェーズベースの除去アルゴリズムを提案
- ヘルスケア、スマートホームデバイス、eコマースなどの多様な分野での応用が期待される

クライアントごとの個別化に対してしっかりとしたアプローチを取っていて面白そう！特にスマートホームデバイスで、どんどん私たちの生活にも役立ちそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-09-11 13:19

- - -

### [Riemannian Federated Learning via Averaging Gradient Stream](http://arxiv.org/abs/2409.07223)

**リーマン連合学習による勾配ストリームの平均化**

Zhenwei Huang, Wen Huang, Pratik Jawanpuria, Bamdev Mishra

- リーマン多様体上の問題を対象にRFedAGSアルゴリズムを提案
- 固定ステップサイズで近似定常解に対して収束速度がサブリニア
- 減衰ステップサイズを用いる場合、グローバル収束が証明される
- 数値シミュレーションで合成データと実データを使った性能評価

リーマン多様体上の連合学習って面白そうだね！本当に収束するかどうか、自分のデータで試してみたいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, math.OC, **投稿日時:** 2024-09-11 12:28

- - -

### [Is merging worth it? Securely evaluating the information gain for causal dataset acquisition](http://arxiv.org/abs/2409.07215)

**結合する価値はあるか？因果データセット取得のための情報ゲインの安全な評価**

Jake Fawkes, Lucile Ter-Minassian, Desi Ivanova, Uri Shalit, Chris Holmes

- 異なる機関間でデータセットを結合するのは費用がかかり、特にプライバシーを伴う
- 因果推定の場合、結合の価値は認識不確実性の低減とオーバーラップの改善に依存
- 期待情報ゲイン（EIG）を評価し、マルチパーティ計算を利用して安全に計算
- 差分プライバシー（DP）と組み合わせて、プライバシーを守りつつより正確な計算を実現

最初に聞いたときに「どうやってやるの？」って思ったけど、差分プライバシーとかマルチパーティ計算とか、めっちゃすごい技術使ってるね！実際のデータでの効果も試されてて期待大だよ〜！



**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.CR, cs.LG, **投稿日時:** 2024-09-11 12:17

- - -

### [Heterogeneity-Aware Coordination for Federated Learning via Stitching Pre-trained blocks](http://arxiv.org/abs/2409.07202)

**連合学習における異質性対応調整：事前学習済みブロックのスティッチングによる手法**

Shichen Zhan, Yebo Wu, Chunlin Tian, Yan Zhao, Li Li

- 連合学習は複数デバイスで協力してモデルを学習しデータプライバシーを保護
- 訓練中の大きなメモリ使用量と高いエネルギー消費が低スペックデバイスを排除
- FedStitchは事前学習済みブロックを活用し、新たなタスクに対しモデルを構築
- 従来の手法よりも精度が最大20.93%向上し、メモリ使用量が79.5%削減

FedStitch、めっちゃ面白そう！低スペックのデバイスも活用できるようになったら、もっと多様で強力なモデルができるかもね！想像するだけでワクワクする～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-11 11:47

- - -

### [A Simple Linear Space Data Structure for ANN with Application in Differential Privacy](http://arxiv.org/abs/2409.07187)

**差分プライバシーに応用した近似最近傍検索のための単純な線形空間データ構造**

Martin Aumüller, Fabrizio Boninsegna, Francesco Silvestri

- Locality Sensitive Filtersを利用し、差分プライバシー下での近似最近傍カウント問題のためのデータ構造を構築
- 伴随統計と極値理論を利用したシンプルな解析を提供
- Andoniら（NeurIPS 2023）の最近の研究と同等の性能を、より簡潔な方法で達成
- 内積類似性に基づく近似最近傍検索において、先行研究（Aumüllerら、TODS 2022）を改良した説明と解析を提供

データプライバシー維持しながらの性能向上ってすごい！シンプルな方法で同じ成果を出すなんて、わかりやすいし研究が進みそうだね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, **投稿日時:** 2024-09-11 11:14

- - -

### [HORAM: A High-Performance Hierarchical Doubly Oblivious RAM](http://arxiv.org/abs/2409.07167)

**H$_2$O$_2$RAM: 高性能な階層的二重オブリビアスRAM**

Leqian Zheng, Zheng Zhang, Wentao Dong, Yao Zhang, Ye Wu, Cong Wang

- TEEとORAMの組み合わせが記憶アクセスパターン攻撃から保護
- H$_2$O$_2$RAMは階層構造を採用してデータ局所性と並列化を強化
- 新しい効率的なオブリビアスコンポーネントを導入し性能を向上
- 実験結果では、最新技術比で最大約1000倍の実行時間短縮と最大44倍のメモリー使用量削減

このRAM技術、本当に未来んじゃない？何といっても、データの保護と性能のバランスがすごく良さそう。これからのデバイスに取り入れられるといいなって思う。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-11 10:31

- - -

### [ZKFault: Fault attack analysis on zero-knowledge based post-quantum digital signature schemes](http://arxiv.org/abs/2409.07150)

**ZKFault: ゼロ知識ベースのポスト量子デジタル署名スキームに対するフォールト攻撃の分析**

Puja Mondal, Supriya Adhikary, Suparna Kundu, Angshuman Karmakar

- 符号理論に基づく問題により暗号スキームが構築され、量子コンピュータへの耐性があるとされているが、実用的ではないと考えられてきた
- NISTの標準化調査で提案されたLESS、CROSS、MEDSなどのコードベースのスキームをゼロ知識フレームワーク上で設計
- これらのスキームは、物理攻撃に対する安全性が十分に検討されていない
- フォールト攻撃を用いてLESSとCROSSの秘密鍵をわずか1つのフォールトで回復可能であることを示した

量子コンピュータの時代が来ても、しっかり暗号が安全じゃないと大変だよね。こんな攻撃方法があるなんてびっくり。でも、防ぐ方法もちゃんと考えてるみたいだから、未来は安心かもね。

**Comment:** 35 pages including appendix and bibliography

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, E.3.3, **投稿日時:** 2024-09-11 09:54

- - -

### [Ciphertext Policy Attribute Based Encryption with Intel SGX](http://arxiv.org/abs/2409.07149)

**Intel SGXを用いた暗号文政策ベースの属性ベース暗号**

Vivek Suryawanshi, Shamik Sural

- CP-ABEは微細なアクセス制御が可能な暗号技術
- Intel SGXを用いてCP-ABEのセキュリティを強化
- ポリシーに基づいて、SGXエンクレーブ内でデータを安全に暗号化・復号
- 実験による評価で、SGXとCP-ABEの統合がデータセキュリティを向上しつつ、実行時間の増加は最小限と確認

Intel SGXを組み合わせたCP-ABEは、より強固なデータ保護を実現しそうね。ちょっと難しそうだけど、セキュリティが強化されるのはすごく大切だよね！



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-11 09:53

- - -

### [CPSample: Classifier Protected Sampling for Guarding Training Data During Diffusion](http://arxiv.org/abs/2409.07025)

**訓練データを保護するための分類器保護サンプリング: 拡散モデルにおけるデータ複製防止**

Joshua Kazdan, Hao Sun, Jiaqi Han, Felix Petersen, Stefano Ermon

- 拡散モデルは特に小規模データセットで訓練データを正確に複製する傾向がある
- 差分プライバシーやデータの一部マスキングは画像品質を著しく低下させる
- CPSampleは、サンプリング過程を変更することでデータ複製を防ぎ、画像品質を維持
- CPSampleは、メンバーシップ推論攻撃に対する耐性を高め、モード崩壊も防止

CPSampleって、データのプライバシーを守りながら画像品質も保てるなんてすごいね！これからのAI技術の進展にすごく期待できるなぁ。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-11 05:42

- - -

### [ODYSSEE: Oyster Detection Yielded by Sensor Systems on Edge Electronics](http://arxiv.org/abs/2409.07003)

**ODYSSEE: センサーシステムを用いたエッジエレクトロニクスによるカキ検出**

Xiaomin Lin, Vivek Mange, Arjun Suresh, Bernhard Neuberger, Aadi Palnitkar, Brendan Campbell, Alan Williams, Kleio Baxevani, Jeremy Mallette, Alhim Vera, Markus Vincze, Ioannis Rekleitis, Herbert G. Tanner, Yiannis Aloimonos

- カキは沿岸生態系の重要種だが、現在のモニタリング方法は破壊的である
- 手動で行うビデオフッテージからの識別は時間と労力がかかる
- 新しい方法として安定拡散を利用した高品質な合成データ生成を提案
- YOLOv10ベースのビジョンモデルが優れた性能を示し、自律監視の可能性を示す

合成データでリアルタイムのカキ検出なんてすごいね！これで海の生物たちももっと守られるといいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.RO, **投稿日時:** 2024-09-11 04:31

- - -

### [Bridging Domain Gap of Point Cloud Representations via Self-Supervised Geometric Augmentation](http://arxiv.org/abs/2409.06956)

**自己教師あり幾何学的拡張によるポイントクラウド表現のドメインギャップ解消**

Li Yu, Hongchao Zhong, Longkun Zou, Ke Chen, Pan Gao

- 合成データは完全で揃っておりノイズがないが、幾何学的なバリエーションが限られる
- 未監督ドメイン適応では、不完全でノイズのあるポイントクラウドからドメイン不変な幾何パターンを捉えるのが難しい
- 2つの自己教師あり幾何学的拡張タスクを用いた新しい表現学習の正則化スキームを提案
- PointDA-10データセットで実験し、最先端の性能を達成

これめっちゃ面白そうじゃない？特に、ドメインギャップを自己教師ありだけで解消しようとする発想が斬新！

**Comment:** 10 pages, 6 figures, 5 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-11 02:39

- - -

### [Privacy-Preserving Federated Learning with Consistency via Knowledge Distillation Using Conditional Generator](http://arxiv.org/abs/2409.06955)

**条件生成器を用いた知識蒸留による一貫性を持つプライバシー保護連合学習**

Kangyang Luo, Shuai Wang, Xiang Li, Yunshi Lan, Ming Gao, Jinlong Shu

- 連合学習（FL）は分散学習フレームワークだが、プライバシー保護の課題がある
- FedMD-CGという新しいFL方法を提案、モデル性能とプライバシー保護を両立
- クライアントのローカルモデルを特徴抽出器と分類器に分離、条件生成器を活用
- 豊富な実験でFedMD-CGの優越性を実証、多様な画像分類タスクで効果を確認

条件生成器とか知識蒸留とか、難しそうだけどすごく挑戦的な感じ！これが実用化されたら、もっと安全にデータを使えて、色んな分野で役に立ちそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-09-11 02:36

- - -

### [Applied Federated Model Personalisation in the Industrial Domain: A Comparative Study](http://arxiv.org/abs/2409.06904)

**産業分野における連合学習モデルの個別化応用: 比較研究**

Ilias Siniosoglou, Vasileios Argyriou, George Fragulis, Panagiotis Fouliras, Georgios Th. Papadopoulos, Anastasios Lytos, Panagiotis Sarigiannidis

- 複雑な機械学習および深層学習モデルのトレーニングと展開は時間がかかり、特に連合学習の分野で課題が多い
- Active Learning、Knowledge Distillation、Local Memorizationという3つの方法が、効率的な最適化とトレーニング時間の短縮を目指して提案されている
- これらの方法により、計算リソースを少なくしながらモデルを個別化し、現行モデルの有効性を向上させることができる
- 新しい連合学習システムを提案し、これらの個別化方法の効果をローカルおよび連合ドメインで比較し、高精度とユーザー体験向上を目指している

連合学習で個別に最適化する方法がたくさん試されてて、すごく実践的だと思う！特にNG-IoTアプリでの効果が気になるな～！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.PF, **投稿日時:** 2024-09-10 23:00

- - -

### [Object Modeling from Underwater Forward-Scan Sonar Imagery with Sea-Surface Multipath](http://arxiv.org/abs/2409.06815)

**海面の多重経路を伴う前方スキャンソナー画像からの水中物体モデリング**

Yuhan Liu, Shahriar Negaharipour

- 2次元前方スキャンソナー画像からの3次元水中物体モデリング手法を提案
- 空気-水界面の多重経路によるアーティファクトを除去し、歪みのない3次元形状を得る
- 鏡像成分の境界からの視覚的手がかりを用いて3次元モデリングの精度を向上
- 反復的な形状調整により、データと合成ビューの不一致を最小化し、3次元モデルを洗練

海面が風で揺らいだりしても、ちゃんと精度良くモデル化できるのはすごい！進化した水中探索技術で、将来的にはもっと多くの発見が期待できそうね！

**Comment:** Copyright 2024 IEEE. Personal use of this material is permitted.   Permission from IEEE must be obtained for all other uses, in any current or   future media, including reprinting/republishing this material for advertising   or promotional purposes, creating new collective works, for resale or   redistribution to servers or lists, or reuse of any copyrighted component of   this work in other works

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-10 18:46

- - -

### [Personalized Federated Learning Techniques: Empirical Analysis](http://arxiv.org/abs/2409.06805)

**パーソナライズド連合学習技術：実証分析**

Azal Ahmad Khan, Ahmad Faraz Khan, Haider Ali, Ali Anwar

- 個人化された連合学習（pFL）は、データプライバシーを保ちながら個別のユーザーニーズに応じたモデルを構築可能
- pFLの性能を最大化するには、メモリのオーバーヘッドとモデルの精度のバランスが重要
- 10の主要なpFL技術を様々なデータセットとデータ分割で評価した結果、大きな性能差が見られた
- データの不均一性や潜在的な攻撃に直面する微調整法よりも、個別の集計技術が通信と計算の効率性で最速の収束を実現

pFLの通信効率が資源使用に大きく影響するのは面白そうだよね！実践に役立つ具体的な技術がどんどん出てきたらいいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-09-10 18:16

- - -

### [Understanding and Mitigating the Impacts of Differentially Private Census Data on State Level Redistricting](http://arxiv.org/abs/2409.06801)

**差分プライバシーによる国勢調査データの州レベルの区割りへの影響の理解と緩和**

Christian Cianfarani, Aloni Cohen

- 2020年の差分プライバシー導入により、国勢調査データの公開方法が大幅に変更された
- プライバシー保護ノイズの影響を考慮しないと、解析結果に誤りが生じる場合がある
- 少しの適応で政策目標を達成可能で、バランスの取れた区割計画が描ける
- アラバマ州の主張とは異なり、州の公正な選挙区を引く権利を妨げないことが示された

差分プライバシーって当然守らなければならないけど、そのせいで逆効果になっちゃうかも？と思った。でも、この論文読むとちゃんと対策すれば大丈夫そう！興味深い～

**Comment:** 24 pages, 5 figures, 7 tables

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CY, **投稿日時:** 2024-09-10 18:11
