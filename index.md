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

更新: 2024-07-09T04:20:11.027590

- - -

### [TARGO: Benchmarking Target-driven Object Grasping under Occlusions](http://arxiv.org/abs/2407.06168)

**目標駆動型オブジェクト把握のための閉塞条件下でのベンチマーキング TARGO**

Yan Xia, Ran Ding, Ziyuan Qin, Guanqi Zhan, Kaichen Zhou, Long Yang, Hao Dong, Daniel Cremers

- シングルデプス画像からの6D把握ポーズ予測の進展によりロボット把握性能が向上
- 目標物体周辺のオブジェクトが影響する混雑環境での把握モデルの課題を評価
- 大規模な合成データと一部の実世界データを含む評価ベンチマークを設定
- 形状補完モジュールを含むトランスフォーマーベースの把握モデルTARGO-Netを提案し、閉塞増加時に最もロバストに機能

この研究、やばいね！特に形状補完とか、未来のロボットがもっと賢くなる予感がしてワクワクする！

**Comment:** 19 pages, 17 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.CV, **投稿日時:** 2024-07-08 17:47

- - -

### [LPGD: A General Framework for Backpropagation through Embedded Optimization Layers](http://arxiv.org/abs/2407.05920)

**LPGD: 組み込み最適化層を通じた逆伝播の一般的なフレームワーク**

Anselm Paulus, Georg Martius, Vít Musil

- 組み込みの最適化問題が層として機械学習に利用されると強力な帰納バイアスになる
- 確率的勾配降下法のトレーニングには注意が必要で、最適化問題の退化した導関数が問題
- LPGDは組み込み最適化層の退化した導関数を有意に置き換えるために前向きソルバーを使用
- 理論的にLPGDは従来の最適化手法との深いつながりを持ち、勾配降下法よりも速く収束

これはすごい技術だね！未来の学習モデルがもっと賢くなるかも。興味津々でワクワクする～！

**Comment:** ICML 2024 conference paper

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-08 13:27

- - -

### [DFedSat: Communication-Efficient and Robust Decentralized Federated Learning for LEO Satellite Constellations](http://arxiv.org/abs/2407.05850)

**DFedSat: LEO衛星コンステレーションのための通信効率が高く堅牢な分散連合学習**

Minghao Yang, Jingjing Zhang, Shengyun Liu

- DFLは衛星間の直接通信を可能にし、従来の集中型アプローチの問題を解決する
- DFedSatは、それぞれの衛星軌道面内外での適応モデル集約を用いて訓練プロセスを迅速化
- 自己補償メカニズムが組み込まれ、通信失敗に対する耐久性を向上させる
- DFedSatは、従来のDFLベースラインに比べ、収束速度や通信効率で優れることを実証

宇宙を駆け巡るAIって、すごく未来っぽいね！いつか自分たちもそんな研究に関わってみたいな。

**Comment:** 13 pages, 10 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-08 12:00

- - -

### [FedMRL: Data Heterogeneity Aware Federated Multi-agent Deep Reinforcement Learning for Medical Imaging](http://arxiv.org/abs/2407.05800)

**FedMRL: 医用画像のためのデータ不均一性対応型連合マルチエージェント深層強化学習**

Pranab Sahoo, Ashutosh Tripathi, Sriparna Saha, Samrat Mondal

- クライアント間のデータ不均一性が存在し、これが連合学習の実用化の課題
- 公正性を確保するため新しい損失関数を導入し、最終的なグローバルモデルのバイアスを防ぐ
- マルチエージェント強化学習を使用して個別ローカル目的関数の収束をグローバル最適に導く
- サーバ側で自己組織化マップを用いた適応的ウェイト調整方法を統合し、クライアントのデータ分布シフトに対応

医用画像を使った連合強化学習の可能性が広がりそうでワクワクするね！この手法が他の分野でも応用できたらすごいと思う。

**Comment:** Accepted to MICCAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CV, cs.DC, **投稿日時:** 2024-07-08 10:10

- - -

### [Synthetic Data for Discriminating Serotonergic Neurons using Convolutional Neural Networks](http://arxiv.org/abs/2407.05701)

**畳み込みニューラルネットワークを用いたセロトニン作動性ニューロンの識別のための合成データ**

Daniele Corradetti, Alessandro Bernardi, Renato Corradetti

- 慣用的な識別方法では非典型的なセロトニン作動性細胞が見落とされがち
- CNNを用いた包括的分類は興味深いが、訓練データの不足が課題
- 実録音から平滑化されたスパイク波形と多様なノイズマスクを組み合わせた合成データ生成手法を提案
- 拡張データセットで訓練したCNNモデルは、異なる実験条件下でのデータに対して高い精度を達成

この合成データ生成のアイデア、すごく先進的！他の分野にも応用できそうでワクワクするね！

**Comment:** Contribution for EPIA 2024 Progress in Artificial Intelligence

**トピック:** [合成データ](sd), **カテゴリ:** q-bio.NC, cs.CE, **投稿日時:** 2024-07-08 08:00

- - -

### [OneDiff: A Generalist Model for Image Difference](http://arxiv.org/abs/2407.05645)

**OneDiff: 画像の差分を捉えるジェネラリストモデル**

Erdong Hu, Longteng Guo, Tongtian Yue, Zijia Zhao, Shuning Xue, Jing Liu

- 従来のIDCモデルは専門特化しており、さまざまなコンテキストでの適用に制限がある
- OneDiffモデルは視覚と言語を統合し、SiameseイメージエンコーダとVisual Delta Moduleを使用
- 新開発のDiffCap Datasetで訓練され、多様なデータタイプに対するロバスト性を強化
- Spot-the-DiffやCLEVR-Changeなどのベンチマークで、精度と適応性において既存モデルを85%上回る

画像の違いを捉える技術って、めっちゃおもしろそう！すごいのは、いろんな場面で使えそうなところだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.MM, **投稿日時:** 2024-07-08 06:14

- - -

### [Deep Learning-based Anomaly Detection and Log Analysis for Computer Networks](http://arxiv.org/abs/2407.05639)

**ディープラーニングベースの異常検知とコンピュータネットワークのログ解析**

Shuzhan Wang, Ruxue Jiang, Zhaoqi Wang, Yan Zhou

- 従来の手法は高次元データや複雑なネットワークトポロジーに弱く、高い偽陽性率を生む
- 時系列データの扱いは従来の手法では困難であり、異常検知とログ解析には重要
- 提案手法はIsolation Forest、GAN、Transformerを融合し、異なる役割を果たす
- 提案モデルは異常検知の精度向上と偽警報の削減を実現し、システムの安定性を向上

モデルの融合が効果的なのが面白いね。GANで合成データを使うなんて未来っぽくてワクワクする！

**Comment:** 38 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-07-08 06:07

- - -

### [Focus on the Whole Character: Discriminative Character Modeling for Scene Text Recognition](http://arxiv.org/abs/2407.05562)

**全体文字に注目: シーンテキスト認識のための識別的文字モデリング**

Bangbang Zhou, Yadong Qu, Zixiao Wang, Zicheng Li, Boqiang Zhang, Hongtao Xie

- 既存のモデルは著しい性能向上を見せたが、歪んだ文字の認識にはまだ困難がある
- 提案するCACEは、複数のブロックを積み重ねて文字特徴を強化し、区別能力を向上させる
- 新たに導入したI^2CLは、特徴空間でのクラス内集約性とクラス間分離性を考慮する
- 合成データで訓練し、一般的なベンチマークで94.1%、Union14M-Benchmarkで61.6%の精度を達成

精度も良くて面白そう！難しいテキストの認識をどう克服するか、読んでみたいね。

**Comment:** Accepted to IJCAI2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-08 02:33

- - -

### [Semantic Segmentation for Real-World and Synthetic Vehicle's Forward-Facing Camera Images](http://arxiv.org/abs/2407.05452)

**実世界および合成車載前方カメラ画像のセマンティックセグメンテーション**

Tuan T. Nguyen, Phan Le, Yasir Hassan, Mina Sartipi

- さまざまな屋外状況に対応する堅牢なモデルを構築
- 高解像度ネットワーク(HRNet)をベースラインとして活用
- 粗から細への2つのモデル(OCRとHMA)で特徴強化
- ドメインベースのバッチ正規化で多様なドメイン間の分布シフトを低減

合成データまで使ってるなんて未来っぽいね！自動運転とかも進んだらこんなとこで活躍するのかな？すごくおもしろそう！

**Comment:** 13 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-07 17:28

- - -

### [Synthetic Test Data Generation Using Recurrent Neural Networks: A Position Paper](http://arxiv.org/abs/2407.05410)

**リカレントニューラルネットワークを用いた合成テストデータ生成に関する見解論文**

Razieh Behjati, Erik Arisholm, Chao Tan, Margrethe M. Bedregal

- 本番環境に似たテスト環境でのテストが品質保証に重要
- プライバシーの問題で生産データを直接使用できない組織が多い
- 匿名化データや合成データの使用を検討、その中でリカレントニューラルネットワークを利用
- 初期実験で高精度な代表データ生成に成功、新たな研究課題を提示

リカレントニューラルネットでの合成データ生成、面白そうね。今後の研究がどう進むかワクワクする！

**Comment:** This paper was published in the proceedings of RAISE@ICSE in 2019

**トピック:** [合成データ](sd), **カテゴリ:** cs.SE, cs.DB, cs.LG, cs.LO, **投稿日時:** 2024-07-07 15:28

- - -

### [On the power of data augmentation for head pose estimation](http://arxiv.org/abs/2407.05357)

**データ拡張による頭部姿勢推定の可能性について**

Michael Welter

- 単眼画像からの人間の頭部姿勢予測でディープラーニングが成功してきた
- 自然画像の一般化向上のため、異なる合成データの組み合わせを提案
- データ量の追加拡張として伝統的な平面外回転合成も考慮
- 新しい損失組み合わせと標準特徴抽出器によるネットワークアーキテクチャでリアルタイム推定を実現

異なる合成データの組み合わせって新しい発想じゃない？リアルタイムでの6自由度推定も含めて、実用性バッチリだね！

**Comment:** Version submitted to NeurIPS

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-07 13:19

- - -

### [Gradient Diffusion: A Perturbation-Resilient Gradient Leakage Attack](http://arxiv.org/abs/2407.05285)

**勾配拡散: 摂動耐性のある勾配漏洩攻撃**

Xuan Liu, Siqi Cai, Qihua Zhou, Song Guo, Ruibin Li, Kaiwei Lin

- 連合学習における勾配漏洩攻撃の脅威に対処するため、勾配保護が重要である
- 差分プライバシーのような摂動ベースのメカニズムが一般的だが、摂動の頑強性は注入されたノイズに依存
- 本研究は摂動逆プロセス中の摂動レベルを捕捉し、摂動回復モデルを構築する
- 提案手法PGLAは既存モデルに比べて最良の勾配復元とデータ回復を実現

連合学習の安全性、もう一度考え直さないと！PGLAが広まったらどんな防御策が取られるのか、未来が楽しみだね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-07-07 07:06

- - -

### [BFLN: A Blockchain-based Federated Learning Model for Non-IID Data](http://arxiv.org/abs/2407.05276)

**BFLN: 非IIDデータのためのブロックチェーンベースの連合学習モデル**

Yang Li, Chunhe Xia, Dongchi Huang, Lin Sun, Tianbo Wang

- 連合学習は、各クライアントに分散しているローカルデータを利用するため、プライバシーとセキュリティが向上する
- 非均衡なデータ分布は、データが独立かつ同一分布（IID）を仮定する従来の連合学習にとって課題である
- 提案モデルBFLNは、ブロックチェーン技術と新しい集約方法およびインセンティブアルゴリズムを組み合わせ、非IIDデータの精度を向上させる
- 公開データセットの実験で、BFLNは最先端モデルと比較してトレーニングの精度を向上させ、個別化された連合学習の持続可能なインセンティブメカニズムを提供する

ブロックチェーン技術を使って連合学習の課題解決なんて、まるでSFの世界みたい！この研究が実用化されたら、色んな分野でセキュリティと効率がさらにUPしそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-07 06:21

- - -

### [Federated Knowledge Transfer Fine-tuning Large Server Model with Resource-Constrained IoT Clients](http://arxiv.org/abs/2407.05268)

**連合知識転送による大規模サーバーモデルのリソース制約付きIoTクライアントでの微調整**

Shaoyuan Chen, Linlin You, Rui Liu, Shuo Yu, Ahmed M. Abdelmoniem

- 大規模モデルのトレーニングは高品質データの不足に直面している
- IoTでの学習はクライアントのプライベートかつ異種データの調整が困難
- KOALAを提案し、連合学習と知識蒸留を用いて大規模モデルを更新
- 実験結果は、従来の方法と比較してローカルストレージと計算リソースの大幅な削減を証明

分散した小規模データを使いながらも、大規模モデルのトレーニングができるようになるのはすごいね！KOALAがどれだけ効率的か、もっと知りたくなったよ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2024-07-07 05:46

- - -

### [Privacy of the last iterate in cyclically-sampled DP-SGD on nonconvex composite losses](http://arxiv.org/abs/2407.05237)

**非凸複合損失におけるサイクルサンプリングDP-SGDの最終反復のプライバシーについて**

Weiwei Kong, Mónica Ribero

- DP-SGDは、微分プライベートな最適化アルゴリズムで、微分プライバシーを保証する
- 現行のDP計算技術は、実際のDP-SGD実装とは異なる仮定をすることが多い
- サイクルサンプリングと勾配クリッピングを用いたDP-SGDの新しいRDP境界を確立
- 新しい境界は、弱凸条件で既存の凸境界に収束し、非リプシッツ滑らかな損失関数でも良好にスケールする

サイクルサンプリングを使うときのDP-SGDのプライバシー解析とか面白そう！特に、弱凸条件下でも他の条件に収束する話が今後役立ちそうな気がするね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.DS, math.OC, stat.ML, 65K10 (Primary), 60G15, 68P27, G.3; G.1.6, **投稿日時:** 2024-07-07 02:35

- - -

### [Matrix perturbation bounds via contour bootstrapping](http://arxiv.org/abs/2407.05230)

**コンターブーツストラッピングによる行列摂動境界**

Phuc Tran, Van Vu

- 行列摂動境界はスペクトルアルゴリズムの設計と解析に重要である
- 新たに「コンターブーツストラッピング」という手法を提案
- この手法で固有部分空間計算と低ランク近似に新たな境界を求めた
- これらの境界を用いて差分プライバシー領域の有用性問題を研究した

新手法「コンターブーツストラッピング」ってちょっと面白そう！差分プライバシーにも役立つなら今後も期待大だね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** math.NA, cs.NA, math.ST, stat.TH, 68W40, 47A55, **投稿日時:** 2024-07-07 01:51

- - -

### [Synthetic Data Aided Federated Learning Using Foundation Models](http://arxiv.org/abs/2407.05174)

**基盤モデルを利用した合成データ支援連合学習**

Fatima Abacha, Sin G. Teo, Lucas C. Cordeiro, Mustafa A. Mustafa

- 連合学習（FL）は、非独立同分布のデータ分布によりデータの不均一性問題に直面
- DPSDA-FLを提案、データの均一化を支援し、局所モデルのトレーニングを改善
- 差分プライバシーを適用した合成データで局所モデルを強化し、基盤モデルを活用
- CIFAR-10データセットで評価し、グローバルモデルの分類精度と再現率が最大26%および9%向上

連合学習に合成データを使う発展が面白いね！プライバシーを守りながら精度が上がる将来に期待大♪



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-06 20:31

- - -

### [Impact of Network Topology on Byzantine Resilience in Decentralized Federated Learning](http://arxiv.org/abs/2407.05141)

**ネットワークトポロジーが分散型連合学習におけるビザンチン耐性に与える影響**

Siddhartha Bhattacharya, Daniel Helo, Joshua Siegel

- 連合学習は、ユーザー間でトレーニングデータを共有せずに機械学習モデルを共同トレーニングする
- 分散型連合学習は、中央集約サーバ不要のピアツーピアでモデルをトレーニングする新しいパラダイム
- ビザンチンノードの影響を考慮し、複雑なネットワークトポロジーでのビザンチン耐性を評価
- 大規模で非完全に接続されたネットワークでは、最新のビザンチン耐性集約戦略は耐性が弱いことが判明

分散型連合学習って、本当にワクワクする未来が待ってる感じだよね! でも、まだ課題も多そうで、これからの研究がとても楽しみ！

**Comment:** 8 pages, 6 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, I.2.11; C.4; C.2.4, **投稿日時:** 2024-07-06 17:47

- - -

### [A Joint Approach to Local Updating and Gradient Compression for Efficient Asynchronous Federated Learning](http://arxiv.org/abs/2407.05125)

**効率的な非同期連合学習のためのローカル更新と勾配圧縮の統合アプローチ**

Jiajun Song, Jiajun Luo, Rongwei Lu, Shuzhao Xie, Bin Chen, Zhi Wang

- 非同期連合学習はデバイスの異質性や低帯域幅環境による古いモデル更新問題に直面
- 従来のアプローチはローカル更新か勾配圧縮のどちらか一方に焦点を当てるが両方は扱わない
- 新アプローチはローカル更新頻度と勾配圧縮率の相互作用が収束速度に与える影響を検討
- 提案するFedLuckフレームワークは通信消費を56%、訓練時間を平均55%削減し、競争力を実証

非同期連合学習の効率化を目指す新しい方法、すごく興味深い！多様な環境でも効果があるのが楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-07-06 16:19

- - -

### [Releasing Malevolence from Benevolence: The Menace of Benign Data on Machine Unlearning](http://arxiv.org/abs/2407.05112)

**善意からの悪意の解放: 機械学習の未学習における良性データの脅威**

Binhao Ma, Tianhang Zheng, Hongsheng Hu, Di Wang, Shuo Wang, Zhongjie Ba, Zhan Qin, Kui Ren

- 機械学習モデルは広範な実データや合成データで訓練され、優れた予測性能を達成
- プライバシー懸念のため、モデルから特定のデータを削除する「未学習」の技術が提案
- 新たな攻撃「未学習ユーザビリティ攻撃」は善意データを利用してモデル性能を低下
- 善意データの未学習により、モデル精度が最大50%低下し、高いリソース消費が必要

データの毒性って面白いよね。未学習技術の未来がますます気になる！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-07-06 15:42

- - -

### [FedTSA: A Cluster-based Two-Stage Aggregation Method for Model-heterogeneous Federated Learning](http://arxiv.org/abs/2407.05098)

**FedTSA: モデル異種連合学習のためのクラスタベース二段階集約法**

Boyu Fan, Chenrui Wu, Xiang Su, Pan Hui

- システムの異種性がFLの大きな課題であり、既存の手法はこれを十分に考慮していない
- 実際のFLでは各クライアントのハードウェア資源が異なり、それが学習タスクに影響する
- FedTSAはクライアントの能力に基づいたクラスタリングと二段階集約、異種モデルの相互学習を提案
- 実験の結果、FedTSAは既存のベースラインを上回り、様々な要因がモデル性能に影響を与えることを示した

システム異種性の課題に対してこんなにスマートなアプローチが出てくるなんて、私も研究したくなっちゃうかも〜！将来のFLに革命をもたらすかもしれないよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-06 14:59

- - -

### [GCON: Differentially Private Graph Convolutional Network via Objective Perturbation](http://arxiv.org/abs/2407.05034)

**GCON: 目的摂動による差分プライバシーグラフ畳み込みネットワーク**

Jianxin Wei, Yizheng Zhu, Xiaokui Xiao, Ergute Bao, Yin Yang, Kuntai Cai, Beng Chin Ooi

- グラフ畳み込みネットワーク（GCN）は多岐にわたる分野で使用され、プライバシー問題が生じる
- 差分プライバシー（DP）はランダムノイズをモデル重みに追加することでプライバシーを守る
- 大規模GCNのDPトレーニングは、ネットワークのメッセージパッシングに歪みをもたらす課題がある
- GCONは、最適化問題と目的関数の摂動を利用し、実験で優れた性能を示した

大規模なデータでもプライバシーを守りつつ学習できる技術って、未来にすごく役立ちそうだよね。実用化が進むと、安心してデータ解析ができるようになるかも！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-06 09:59

- - -

### [Beyond the Federation: Topology-aware Federated Learning for Generalization to Unseen Clients](http://arxiv.org/abs/2407.04949)

**連合を超えて: 未見クライアントへの一般化のためのトポロジー対応連合学習**

Mengmeng Ma, Tang Li, Xi Peng

- 既存の連合学習はフェデレーション内のデータ異質性に対応するが、未見クライアントには効果が低い
- 大規模分散設定では高コストなため、新手法もスケーリングに課題
- トポロジー対応連合学習(TFL)を提案し、クライアントの関係性をグラフで表現
- クライアントトポロジー学習とトポロジー上の学習モジュールで効率的に強固なモデルを構築

新しいTFL手法がどれだけ効果的に未見クライアントへの一般化を達成するか気になるな！これが実用化されたら、もっと多様なデータを分析できそうでワクワクするね。

**Comment:** ICML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-07-06 03:57

- - -

### [Quantifying Privacy Risks of Public Statistics to Residents of Subsidized Housing](http://arxiv.org/abs/2407.04776)

**公的統計が補助住宅の居住者のプライバシーに与えるリスクの定量化**

Ryan Steed, Diana Qing, Zhiwei Steven Wu

- 回答者が不法投棄の恐れから未承認の家族を記載しない可能性がある
- 住宅補助データを用いた再構成攻撃で不正居住者を識別可能
- 合成データはランダムスワップ機構で攻撃精度が低減しないと示唆
- 差分プライバシー機構が攻撃精度を効果的に低減

差分プライバシーの力、これから普及していきそうだね。公共政策に活かしたら、多くの人が安心して暮らせるかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CY, **投稿日時:** 2024-07-05 18:00

- - -

### [A Unified Learn-to-Distort-Data Framework for Privacy-Utility Trade-off in Trustworthy Federated Learning](http://arxiv.org/abs/2407.04751)

**信頼できるフェデレーテッドラーニングにおけるプライバシーと有用性のトレードオフを実現する統一的なデータ歪曲学習フレームワーク**

Xiaojin Zhang, Mingcong Xu, Wei Chen

- フェデレーテッドラーニングにおけるプライバシーと有用性の均衡を理論的に紹介
- プライバシー保護メカニズムの歪曲を学習変数としてモデル化し、モデルパラメータと共同最適化
- データ歪曲に基づくプライバシー保護メカニズムの適用可能性を実証
- 関連領域（対抗訓練、入力の堅牢性、学習不能な事例）との繋がりを強調

プライバシーを守りつつどうやって有用性を保つかのバランスが大事なんだね！実際の応用が期待できそうでワクワクする～。未来の技術に一歩近づけそうで面白そうだなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-07-05 08:15
