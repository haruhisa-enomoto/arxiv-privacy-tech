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

更新: 2024-09-08T04:20:01.869201

- - -

### [Confidential Computing Transparency](http://arxiv.org/abs/2409.03720)

**機密コンピューティングの透明性**

Ceren Kocaoğullar, Tina Marjanov, Ivan Petrov, Ben Laurie, Al Cutter, Christoph Kern, Alice Hutchings, Alastair R. Beresford

- 機密コンピューティングは、ハードウェアベースの信頼実行環境(TEEs)を活用してデータを保護するセキュリティーパラダイムである
- TEEsはセキュリティメリットを提供するが、ユーザーの信頼確保が課題で、アテステーションだけでは脆弱性やバックドアの不在を保証できない
- ユーザー、レビュアーの責任追及や技術的な安全対策を組み込んだ透明性フレームワークを提案し、現行のオープンソースコードや監査を超える
- 400人のユーザースタディで、透明性が高まるほど、特に敏感なデータタイプに対してユーザーの快適度が向上することを示した

ユーザーの信頼と安心感を高める新しいフレームワークが提案されたんだね！これでセキュリティ分野の進化がさらに楽しみになりそうだよ。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-05 17:24

- - -

### [Wind turbine condition monitoring based on intra- and inter-farm federated learning](http://arxiv.org/abs/2409.03672)

**風力タービン状態監視のための風車内および風車間連合学習**

Albin Grataloup, Stefan Jonas, Angela Meyer

- 風力タービンの効率的な運転と保守がエネルギー生産の最大化とコスト削減に不可欠
- 風力タービンや風力発電所の運用データを活用することで、AIアプリケーションの効果を高める
- 連合学習はデータプライバシーを保ちながら分散型機械学習を実現するアプローチとして注目される
- 複数の風力タービン間で連携する連合学習は、単一のタービンでのモデルよりも優れた性能を発揮

風力発電所の監視とかってめっちゃSFっぽくない？AIが風力タービンの故障を予測してくれるなんて、未来って感じでワクワクするー！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.SY, eess.SY, **投稿日時:** 2024-09-05 16:25

- - -

### [A method to benchmark high-dimensional process drift detection](http://arxiv.org/abs/2409.03669)

**高次元プロセスドリフト検出のベンチマーク法**

Edgar Wolf, Tobias Windisch

- プロセス曲線は製造プロセスから得られる多変量の有限時間シリーズデータである
- プロセス曲線のドリフト検出のための機械学習手法を研究
- 制御された方法でプロセス曲線を合成的に生成する理論的フレームワークを導入
- 時間的カーブ下面積という評価スコアを導入し、ドリフトセグメントをどれだけ明確に検出できるかを定量化

この研究で合成データというコンセプトを使っているのが面白いね！いろんな機械学習モデルの性能を公平に評価できるから、将来の研究に大きな影響を与えそうだよね。



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.AI, cs.LG, **投稿日時:** 2024-09-05 16:23

- - -

### [Privacy versus Emotion Preservation Trade-offs in Emotion-Preserving Speaker Anonymization](http://arxiv.org/abs/2409.03655)

**プライバシー対感情保存のトレードオフ：感情保存型話者匿名化における課題**

Zexin Cai, Henry Li Xinyuan, Ashi Garg, Leibny Paola García-Perera, Kevin Duh, Sanjeev Khudanpur, Nicholas Andrews, Matthew Wiesner

- 音声技術の進歩により、音声から個人情報へのアクセスが増加
- 差分プライバシー分野では、言語的および準言語的要素を保持しつつ音声を匿名化する方法を模索
- 音声の匿名化と感情状態の保持を同時に実現することは困難
- 音声匿名化が得意なものと感情保存が得意なものは分かれており、両者を同時に達成するには専用の感情認識器が必要

感情と匿名性のトレードオフって面白いよね。未来のAIがさらに人の心に近づいてくるかんじ、見逃せない！

**Comment:** accepted by 2024 IEEE Spoken Language Technology Workshop

**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.AS, cs.LG, **投稿日時:** 2024-09-05 16:10

- - -

### [On the Relativistic Zero Knowledge Quantum Proofs of Knowledge](http://arxiv.org/abs/2409.03635)

**相対論的ゼロ知識量子知識証明について**

Kaiyan Shi, Kaushik Chakraborty, Wen Yu Kon, Omar Amer, Marco Pistoia, Charles Lim

- 古典的通信で行う相対論的ゼロ知識量子知識証明システムを定義
- 特別な健全性を持たないプロトコル向けに知識抽出器を構築
- モノガミーな絡み合いと動揺測定補題を組み合わせ多重校正技術を開発
- 既存システムの健全性向上を証明、連続測定の影響を減少

ゼロ知識量子証明なんてすごい未来的！特にモノガミーな絡み合いを使っているところがかっこいいね。物理的な制約がこんなに役立つなんて、感動しちゃう！

**Comment:** 37 pages

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** quant-ph, cs.CR, **投稿日時:** 2024-09-05 15:50

- - -

### [VFLGAN-TS: Vertical Federated Learning-based Generative Adversarial Networks for Publication of Vertically Partitioned Time-Series Data](http://arxiv.org/abs/2409.03612)

**VFLGAN-TS: 縦方向に分割された時系列データの公開のための連合学習ベース生成敵対ネットワーク**

Xun Yuan, Zilong Zhao, Prosanta Gope, Biplab Sikdar

- データセットの規模や品質がAIモデルのトレーニングに重要だが、プライバシー問題で共有が困難
- 本研究では、縦方向に分割されたシナリオで合成時系列データを生成するVFLGAN-TSを提案
- VFLGAN-TSの性能は、中央集約型でトレーニングしたモデルの上限に近い
- ガウス機構を用いて$(\epsilon,\delta)$-差分プライバシーを満たし、強化されたプライバシー監査スキームも開発

プライバシー問題を乗り越えながら、時系列データを縦方向に扱えるなんてすごいね。VFLGAN-TSの性能が中央集約型とほぼ同等なら、これからのAI研究にすごく役立ちそう！



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-09-05 15:17

- - -

### [Enabling Practical and Privacy-Preserving Image Processing](http://arxiv.org/abs/2409.03568)

**実用的でプライバシー保護された画像処理の実現**

Chao Wang, Shubing Yang, Xiaoyan Sun, Jun Dai, Dongfang Zhao

- FHE（完全準同型暗号）はデータの機密性を保ちながら暗号化データ上で計算を可能にする
- 高精度・複雑なデータ処理時にFHEは大きな性能オーバーヘッドの問題がある
- 提案されたiCHEETAHはCKKSスキームに基づくピクセルレベルの準同型暗号アプローチ
- 3つのキャッシングメカニズムを導入し、暗号化速度が最大19倍向上し、高い画像品質を維持

ピクセルレベルの処理が可能なんてすごくない！？その上、画像品質も落ちないから嬉しいよね。未来の画像処理が楽しみ～！

**Comment:** 16 pages, 10 figures

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, C.2.0; K.6.5, **投稿日時:** 2024-09-05 14:22

- - -

### [Rethinking Improved Privacy-Utility Trade-off with Pre-existing Knowledge for DP Training](http://arxiv.org/abs/2409.03344)

**差分プライバシー（DP）トレーニングにおける既存知識を用いたプライバシーと実用性のトレードオフの再考**

Yu Zheng, Wenchao Zhang, Yonggang Zhang, Wei Song, Kai Zhou, Bo Han

- 差分プライバシー（DP）は、プライバシー保護のためにランダムなメカニズムをデータセットに適用する
- DP-SGDはノイズを勾配に追加するが、均一なノイズがモデルの性能を低下させる
- DP-Heroは既存のモデル知識を活用し、異質なノイズを用いて実用性を向上させる
- 提案手法DP-Heroは、実験で精度向上を示し、既存の手法より優れていることが分かった

既存のモデルを活用してノイズを調整するなんて面白そう！さらに実用性が上がるなんて、次世代のプライバシー技術に期待😄

**Comment:** 13 pages

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-05 08:40

- - -

### [Enhancing User-Centric Privacy Protection: An Interactive Framework through Diffusion Models and Machine Unlearning](http://arxiv.org/abs/2409.03326)

**ユーザー中心のプライバシー保護強化：拡散モデルと機械学習のアンラーニングによるインタラクティブフレームワーク**

Huaxi Huang, Xin Yuan, Qiyu Liao, Dadong Wang, Tongliang Liu

- 現在の研究はデータ共有と学習モデル公開の際のプライバシーに焦点を当てる
- 我々の研究は、データ共有とモデル公開時に画像データのプライバシーを同時に保護する
- 生成モデルで画像情報を属性レベルで変更、機械アンラーニングでモデルパラメータを保護
- 差分プライバシー拡散モデルと特徴アンラーニングアルゴリズムを導入し性能が向上

画像データのプライバシーがこんなに進化するって、未来を感じさせるよね。この技術、顔認識とかで役立ちそうでワクワクする～。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-05 07:55

- - -

### [Federated Prototype-based Contrastive Learning for Privacy-Preserving Cross-domain Recommendation](http://arxiv.org/abs/2409.03294)

**プライバシー保護のための連合プロトタイプベースコントラスト学習を用いたクロスドメインレコメンデーション**

Li Wang, Quangui Zhang, Lei Sang, Qiang Wu, Min Xu

- クロスドメインレコメンデーション（CDR）は、データが少ないドメインでのレコメンデーション精度を向上させるが、ユーザープライバシーの問題を見落としている
- 従来のCDR方法は、ドメイン間でユーザーとアイテムの相互作用データを共有することを前提としており、ユーザーのプライバシー保護を考慮していない
- 提案しているFedPCL-CDRは、非重複ユーザーの情報とプロトタイプを利用して、マルチドメインパフォーマンスを向上させながらユーザープライバシーを保護する手法
- 4つのCDRタスクにおいて実施した実験で、2つの実データセットを用いた結果、FedPCL-CDRは最先端技術よりも優れたパフォーマンスを示すことが確認された

非重複ユーザー情報の利用でプライバシー問題を解決するアイデアがめちゃ革新的だよね！改善されたマルチドメインパフォーマンスってところも重要だし、これからの技術の進展が楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, **投稿日時:** 2024-09-05 06:59

- - -

### [Minimizing Cost Rather Than Maximizing Reward in Restless Multi-Armed Bandits](http://arxiv.org/abs/2409.03071)

**レストレス・マルチアーム・バンディットにおける報酬の最大化ではなくコストの最小化**

R. Teal Witter, Lisa Hellerstein

- RMABsはリソース制約最大化問題を解く強力なフレームワークだが、報酬閾値が制約の設定には不適切
- 報酬閾値を達成しつつ総コストを最小化するための制約最適化問題を導入
- 問題のPSPACE-hard性を示し、分離問題、インデックス性、Whittleインデックスを定義
- 最大化問題におけるWhittleインデックスから最小化問題のインデックスを簡単に計算可能

最大化だけじゃなくて、コストをどう最適化するかも重要なんだね。いろんなヘルスケア分野とかに応用できそうで面白そうだし、実際に役立ちそうだよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.DS, **投稿日時:** 2024-09-04 20:47

- - -

### [Boundless: Generating Photorealistic Synthetic Data for Object Detection in Urban Streetscapes](http://arxiv.org/abs/2409.03022)

**Boundless: 都市の街並みでの物体検出のためのフォトリアリスティック合成データ生成**

Mehmet Kerem Turkcan, Ian Li, Chengbo Zang, Javad Ghaderi, Gil Zussman, Zoran Kostic

- Boundlessは、密集した都市街並みでの高精度な物体検出を可能にする合成データ生成システムである
- Unreal Engine 5をベースにして、異なる照明やシーンの変化条件での3Dバウンディングボックス収集を改善
- Boundlessで生成されたデータセットで訓練したモデルは、CARLA訓練モデルに比べて7.8 mAPの改善を示す
- 合成データ生成が都市シーンの物体検出モデルの訓練や微調整に有効であることを実証した

合成データでの訓練がこんなに効果あるんだね！現実データ収集の手間が省けるなら、応用の幅が広がりそうでワクワクするな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-04 18:28

- - -

### [Inverse decision-making using neural amortized Bayesian actors](http://arxiv.org/abs/2409.03710)

**ニューラル・アモータイズド・ベイズ・アクターを用いた逆意思決定**

Dominik Straub, Tobias F. Niehues, Jan Peters, Constantin A. Rothkopf

- ベイズ観察者とアクターモデルは、知覚や感覚運動制御などで行動変異を説明
- 複雑なタスクではベイズ意思決定問題が解析的に解決困難
- ニューラルネットワークを利用し、非教師あり学習でベイズアクターをアモータイズ
- 合成データを用いて、推論分布が解析解とほぼ一致し、経験的データでも行動パターンの違いを説明

ニューラルネットでベイズ推論を高速化するなんて、これからの認知科学の研究がもっと面白くなりそう！自分の行動パターンも分析できるかもって思うとワクワクするよね。

**Comment:** 19 pages, 7 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, q-bio.NC, stat.ML, **投稿日時:** 2024-09-04 10:31
