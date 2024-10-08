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

更新: 2024-10-08T04:23:33.388692

- - -

### [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](http://arxiv.org/abs/2410.05243)

**人間のようにデジタル世界をナビゲートする: GUIエージェントのためのユニバーサルビジュアルグラウンディング**

Boyu Gou, Ruohan Wang, Boyuan Zheng, Yanan Xie, Cheng Chang, Yiheng Shu, Huan Sun, Yu Su

- 現在のGUIエージェントはテキストベースで動作し、ノイズや不完全性が問題である
- 人間らしいビジュアル操作を行うエージェントにより、計算の効率性が向上
- 新たなデータセットを用いてUGroundモデルを開発し視覚的なグラウンディングを強化
- UGroundは既存のモデルを上回り、視覚のみで高性能な結果を示す

人間のようにビジュアルでGUIを操作できるようになるなんてすごく面白そう！これが普及したら、どんな新しいアプリ体験が生まれるか今からワクワクするよね。UGroundの効果がどんどん実社会に活用される未来が楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, cs.CV, **投稿日時:** 2024-10-07 17:47

- - -

### [Towards a Modern and Lightweight Rendering Engine for Dynamic Robotic Simulations](http://arxiv.org/abs/2410.05095)

**動的ロボットシミュレーションのためのモダンで軽量なレンダリングエンジンの構築に向けて**

Christopher John Allison, Haoying Zhou, Adnan Munawar, Peter Kazanzides, Juan Antonio Barragan

- インタラクティブな動的シミュレーターは、新たなロボット制御アルゴリズムの開発を加速する
- 高精度な視覚化がユーザー訓練や合成データ生成において重要である
- Vulkan APIをサポートする軽量レンダリングエンジンを提案し、レガシーパイプラインを近代化
- PBRやアンチエイリアス、レイトレーシングシャドウなどで画質向上を実現

新しいエンジンでロボットシミュレーションをリアルに感じられるってすごい！これを使った新しいアルゴリズム開発がワクワクだね。どんな未来のロボットシステムが示されるのか楽しみだよね。

**Comment:** 8 pages, 8 figures, submitted to the 2024 IEEE International   Conference on Robotic Computing (IRC)

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.GR, cs.SE, **投稿日時:** 2024-10-07 14:50

- - -

### [SELECT: A Large-Scale Benchmark of Data Curation Strategies for Image Classification](http://arxiv.org/abs/2410.05057)

**SELECT: 画像分類のためのデータキュレーション戦略に関する大規模ベンチマーク**

Benjamin Feuer, Jiawei Xu, Niv Cohen, Patrick Yubeaton, Govind Mittal, Chinmay Hegde

- データキュレーションは効率的な学習を支えるデータセットの収集と組織化の問題
- SELECTは画像分類向けのデータキュレーション戦略の大規模ベンチマークを提供
- ImageNet++データセットを作成し、異なる戦略で新たに5つのトレーニングデータシフトを導入
- 最近の合成データ生成やCLIP埋め込みによる比較で、元のImageNet-1K戦略が基準であると判明

画像分類のためのデータ収集を見直すこの研究、最高に斬新な発見がありそう！特にImageNetと競争できる新しい手法の分析が、未来の技術革新を引き起こすかもね。どんなスタンダードが新たに生まれるのか、楽しみすぎる～！

**Comment:** NeurIPS 2024, Datasets and Benchmarks Track

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-10-07 14:14

- - -

### [FRIDA: Free-Rider Detection using Privacy Attacks](http://arxiv.org/abs/2410.05020)

**FRIDA: プライバシー攻撃を用いたフリーライダー検出**

Pol G. Recasens, Ádám Horváth, Alberto Gutierrez-Torre, Jordi Torres, Josep Ll. Berral, Balázs Pejó

- 連合学習は複数の参加者でモデルを共同訓練するが、フリーライダーの存在が問題
- フリーライダーは学習プロセスの妥当性を損ない、モデルの収束を遅らせ、コスト増加を招く
- FRIDAはプライバシー攻撃を使い、参加者のデータセットからフリーライダーを直接検出
- FRIDAは最新の手法より効果的で、特にデータが非独立同分布（非IID）の場合に優位性を示す

これって、なんかすごくない？プライバシー攻撃を逆手に取って、みんなで守る側の発想を変えるんだって！技術的に新しいチャレンジをしてるから、これからも注目したいな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-07 13:20

- - -

### [D-PoSE: Depth as an Intermediate Representation for 3D Human Pose and Shape Estimation](http://arxiv.org/abs/2410.04889)

**D-PoSE: 3D人体姿勢と形状推定のための中間表現としての深度**

Nikolaos Vasilikopoulos, Drosakis Drosakis, Antonis Argyros

- D-PoSEはRGB画像から3D人体姿勢と形状を推定する一段階法を提案
- 深度マップを中間表現として使用し、合成データでのトレーニングを実施
- 軽量設計とCNNバックボーンで、大規模モデルを上回る性能を実現
- 実世界のベンチマークデータセットで最先端の性能を達成

D-PoSEってかなり面白そう！軽量な設計なのに深度マップをうまく活用してすごい精度出してるんだね。実世界でも通用するその手法、試してみたいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-07 10:17

- - -

### [Strong Model Collapse](http://arxiv.org/abs/2410.04840)

**強いモデル崩壊**

Elvis Dohmatob, Yunzhen Feng, Julia Kempe

- 大規模ニューラルネットワークのスケーリング法におけるモデル崩壊現象を発見
- 合成データの少量でもモデル崩壊が発生し、データセット拡大は性能向上に寄与しない
- モデルサイズの増加がモデル崩壊を悪化させるか抑制するかを調査
- 理論と実験により、特定条件下で大きなモデルが崩壊を軽減する可能性を示す

モデル崩壊って怖いね！でもデータを増やす以外にも工夫が必要なんだね。大きなモデルが逆に崩壊を軽減するかもって面白い発見！だから将来のAI開発には新しい視点が必要かもね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-10-07 08:54

- - -

### [FedBiP: Heterogeneous One-Shot Federated Learning with Personalized Latent Diffusion Models](http://arxiv.org/abs/2410.04810)

**FedBiP: 個別化潜象拡散モデルを用いた異質ワンショット連合学習**

Haokun Chen, Hang Li, Yao Zhang, Gengyuan Zhang, Jinhe Bi, Philip Torr, Jindong Gu, Denis Krompass, Volker Tresp

- ワンショット連合学習（OSFL）は通信費を削減しプライバシーを保護する手法
- 従来のOSFLはクライアントデータの異質性と少量のデータが課題
- プレトレーニングされた潜象拡散モデル（LDM）は高品質画像生成に優れるが、OSFLには最適でない
- FedBiPはLDMを個別化し、データ分布を考慮した画像を合成して性能を向上

おもしろそうな論文だね！医療画像とか珍しいデータでもしっかり対応できるのってすごいな〜。プライバシーも守りつつ効果的に連合学習を実現するなんて、未来の技術って感じでワクワクする〜！



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, cs.DC, cs.MM, **投稿日時:** 2024-10-07 07:45

- - -

### [HF-NTT: Hazard-Free Dataflow Accelerator for Number Theoretic Transform](http://arxiv.org/abs/2410.04805)

**HF-NTT: 数論変換のためのハザードフリーデータフローアクセラレータ**

Xiangchen Meng, Zijun Jiang, Yangdi Lyu

- 多ビット係数を持つ多項式の計算効率がFHEの実装の課題である
- HF-NTTは異なる多項式の次数やモジュールに対応する効率的なアクセラレータを提供
- ビットリバーサル不要のデータ移動戦略でハザードを解消し、クロックサイクルを削減
- Xilinx Virtex-7 FPGAでの評価で他の設計に比べてATPと遅延が大幅に改善される

この研究、未来の準同型暗号を加速させそうでワクワクするね！データ移動の工夫でリソース効率も上がるなんて、すごい構造じゃない？



**トピック:** [準同型暗号](he), **カテゴリ:** cs.AR, cs.CR, **投稿日時:** 2024-10-07 07:31

- - -

### [Federated Learning Nodes Can Reconstruct Peers' Image Data](http://arxiv.org/abs/2410.04661)

**連合学習ノードが他のノードの画像データを再構築できる**

Ethan Wilson, Kai Yue, Chau-Wai Wong, Huaiyu Dai

- 連合学習はプライバシーを保ちつつノード間でモデルを訓練する技術だが、データのプライバシーは保証されない
- 誠実だが好奇心旺盛なノードが、他のノードの画像データを再構築できることを示す
- 単一のクライアントが連続した更新情報を利用し、他のクライアントの画像を密かに再構築できる
- 拡散モデルを使って再構築画像の質を高め、セマンティックな情報漏洩のリスクを強調

連合学習って便利そうだったけど、ちゃんと考えないと他人のデータを覗かれちゃうんだね！もっと安全な仕組みができたら、いろんな分野で活用できそうでワクワク！

**Comment:** 12 pages including references, 12 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-07 00:18

- - -

### [GAMformer: In-Context Learning for Generalized Additive Models](http://arxiv.org/abs/2410.04560)

**GAMformer: 一般化加法モデルのためのコンテキスト学習**

Andreas Mueller, Julien Siems, Harsha Nori, David Salinas, Arber Zela, Rich Caruana, Frank Hutter

- 一般化加法モデル（GAM）の通常の学習法とは異なる、コンテキスト学習を使った手法を紹介
- GAMformerは、反復法ではなく、単一の情報伝達で形状関数を推定
- この方法は、合成データで訓練しながらも実際のデータで優れた適応力を示す
- 実験で、他の主要なGAMと同等の性能を発揮し、解釈性の高い形状関数を生成

GAMformerって名前からしてすごく強そう！しかも、今までの反復計算なしでやっちゃうなんて、まさに新時代だね。どんなデータでも柔軟に対応できそうで、ちょっとワクワクしちゃう！

**Comment:** 20 pages, 12 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-10-06 17:28

- - -

### [Pullback Flow Matching on Data Manifolds](http://arxiv.org/abs/2410.04543)

**データ多様体上でのプルバックフローマッチング**

Friso de Kruiff, Erik Bekkers, Ozan Öktem, Carola-Bibiane Schönlieb, Willem Diepeveen

- 新しいフレームワークPFMを提案し、データ多様体上での生成モデルを実現
- PFMはプルバック幾何学と等角学習を活用し、多様体の幾何を保持
- ネットワークODEを用いて等角学習を強化し、スケーラブルな訓練目標を提案
- 合成データやタンパク質動態などで効果を実証し、薬物発見や材料科学に貢献

新しい多様体生成モデルPFMって面白そう！このアプローチで、薬や素材の新しい発見に繋がるなんてワクワクするね！新しい技術でどんな未来が切り開かれるのか、期待しちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, math.DG, q-bio.BM, **投稿日時:** 2024-10-06 16:41

- - -

### [CONFINE: Preserving Data Secrecy in Decentralized Process Mining](http://arxiv.org/abs/2410.04453)

**CONFINE: 分散型プロセスマイニングにおけるデータ秘密保持**

Valerio Goretti, Davide Basile, Luca Barbaro, Claudio Di Ciccio

- 組織間の協力はコスト削減や技術進化といった多くの機会をもたらす
- プロセスマイニングはビジネス理解を深めるが、データの機密性への懸念が大きい
- CONFINEは秘密保持しつつ複数のデータ提供者のイベントデータを処理
- 信頼実行環境で機能し、関与者間と外部への情報漏洩を防ぐ分散型アーキテクチャ

CONFINEのアプローチを使ったら、データの機密性を守りながら他社とも協力できそう！分散型アーキテクチャを使っているって、安全面で安心だね。きっとこれからもビジネスの世界で重要になってくるよね！



**トピック:** [TEE](tee), **カテゴリ:** cs.DC, **投稿日時:** 2024-10-06 11:38

- - -

### [Test-Time Adaptation for Keypoint-Based Spacecraft Pose Estimation Based on Predicted-View Synthesis](http://arxiv.org/abs/2410.04298)

**予測ビュー合成に基づくキー・ポイント型宇宙機姿勢推定のテスト時適応**

Juan Ignacio Bravo Pérez-Villar, Álvaro García-Martín, Jesús Bescós, Juan C. SanMiguel

- 合成データで訓練された姿勢推定アルゴリズムは、実際の運用データで性能が低下する
- テスト時適応手法を提案し、接近操作中の画像の時間的冗長性を活用
- 連続した宇宙機画像から特徴を抽出し、ポーズを推定して再構築したビューを合成
- 合成ビューと実際のビューを比較し、自己教師あり学習を目的とする

宇宙機の実際の運用データに適応するための新しい手法って感じでおもしろそう！特に、訓練時とテスト時で異なる環境にうまく対応しちゃうところに可能性を感じるよね！🌟

**Comment:** Preprint

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-05 22:24

- - -

### [Implicit to Explicit Entropy Regularization: Benchmarking ViT Fine-tuning under Noisy Labels](http://arxiv.org/abs/2410.04256)

**暗黙から明示的なエントロピーレギュラリゼーションへの移行: ノイズラベル下におけるViTファインチューニングのベンチマーク**

Maria Marrium, Arif Mahmood, Mohammed Bennamoun

- 大規模データセットの自動アノテーションはノイズラベルを導入し、DNNの学習に悪影響を与える
- ViTのファインチューニングはノイズラベルに脆弱で、CNNと比較した頑健性を評価した
- CNN向けに開発されたNLL手法がViTにも同様に効果的かどうかを調査
- エントロピー正則化が既存の損失関数やNLL手法の頑健性を向上させることが判明

ノイズラベルによる悪影響を軽減するために、エントロピーの役割が重要ってことなんだね！データサイエンスの未来に貢献できる研究だし、ViTが普及してきた今、私たちも頑張らなきゃって思った！✨



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-10-05 18:24

- - -

### [ConDa: Fast Federated Unlearning with Contribution Dampening](http://arxiv.org/abs/2410.04144)

**ConDa: 貢献抑制による高速連合アンラーニング**

Vikram S Chundawat, Pushkar Niroula, Prasanna Dhungana, Stefan Schoepf, Murari Mandal, Alexandra Brintrup

- 連合学習では参加者の追加は簡単だが、参加者の削除は難題である
- ConDaは、不要な情報の寄与を弱体化することで効率的にデータを消去
- クライアントのデータ再学習や計算負荷なく、プライバシーの確保を実現
- 非IID環境で、他の方法より100倍以上の速さでアンラーニングが可能

すごい！データの消去ってずっと難しかったけど、こんなに早くて簡単にできちゃうなんて驚きだよね！プライバシーが守られる世界がさらに近づいてるのかもって思うとワクワクするな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-05 12:45

- - -

### [pFedGame -- Decentralized Federated Learning using Game Theory in Dynamic Topology](http://arxiv.org/abs/2410.04058)

** pFedGame -- 動的トポロジーにおけるゲーム理論を用いた分散型連合学習 **

Monik Raj Behera, Suchetana Chakraborty

- 連合学習の課題として、中央集約サーバへの負荷やデータバイアスが存在
- pFedGameは中央サーバ不要のゲーム理論ベースの手法を提案
- 動的ネットワークでの消失する勾配と収束の問題を対応
- pFedGameは異種データで精度70%以上を達成し有望な結果

面白そう！分散型で部分連合学習ができるなんて、なんだか未来を感じるね。この技術が新しい協力関係を生むかもって思ったよ。



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.CR, cs.GT, cs.LG, **投稿日時:** 2024-10-05 06:39

- - -

### [Is Score Matching Suitable for Estimating Point Processes?](http://arxiv.org/abs/2410.04037)

**スコアマッチングは点過程の推定に適しているか？**

Haoqun Cao, Zizhuo Meng, Tianjun Ke, Feng Zhou

- スコアマッチング推定量は正規化定数の積分を計算せずに済むため注目される
- 既存のスコアマッチング推定量は特定の問題にしか適用できず、より一般的な点過程では失敗する
- 本研究は加重スコアマッチング推定量を点過程に導入し、一貫性と収束速度を理論的に証明
- 実験結果では合成データでモデルパラメータを正確に推定し、実データでMLEと一致する結果を得る

スコアマッチングの新しい方法が提案されて、実験でも結果が一致するみたい！コードも公開されてるから、自分で試してみるのも楽しそうだね。もっと一般的な点過程にも対応できるようになったら、色んな分野で役立ちそう！



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-10-05 05:10

- - -

### [Take It Easy: Label-Adaptive Self-Rationalization for Fact Verification and Explanation Generation](http://arxiv.org/abs/2410.04002)

**気楽に考えよう: 事実検証と説明生成のためのラベル適応型自己合理化**

Jing Yang, Anderson Rocha

- 自己合理化手法をファクト検証に拡張し、ラベル適応型学習を提案
- モデルのファインチューニングにより、事実性予測の精度を10%以上向上
- 合成データを用いて少ないコストで説明注釈を生成しモデルを改良
- 少数サンプルの合成説明で、完全ファインチューンモデルと同等の性能を実現

面白そうなのは、自動記事検証の精度を上げるだけじゃなくて、コストも削減できちゃうところ！合成データで手軽に学べるなんて未来がワクワクするね。

**Comment:** Paper accepted in the 16th IEEE INTERNATIONAL WORKSHOP ON INFORMATION   FORENSICS AND SECURITY (WIFS) 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-10-05 02:19

- - -

### [DiSK: Differentially Private Optimizer with Simplified Kalman Filter for Noise Reduction](http://arxiv.org/abs/2410.03883)

**DiSK: ノイズ低減のためのカマンフィルターを用いた差分プライベート最適化技術**

Xinwei Zhang, Zhiqi Bu, Borja Balle, Mingyi Hong, Meisam Razaviyayn, Vahab Mirrokni

- 差分プライバシーは個人データを保護する枠組みであり、差分プライベート最適化技術が注目されている
- 既存の技術は大規模なトレーニングで性能が低下する問題があり、それが大量のノイズ注入に起因
- DiSKという新しいフレームワークを提案し、カマンフィルターを用いてプライベート化された勾配をデノイズ
- 広範な実験でDiSKが標準のDP最適化手法を超える性能を示し、複数のベンチマークで差をつけた

わー、このDiSKって技術すごいね！大規模データでもプライバシーを保ちつつ性能アップできるなんて、今後のAIの発展に大きな影響を与えそう♪



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-10-04 19:30

- - -

### [A Survey on Group Fairness in Federated Learning: Challenges, Taxonomy of Solutions and Directions for Future Research](http://arxiv.org/abs/2410.03855)

**連合学習におけるグループ公正性の調査：課題、解決策の分類と今後の研究の方向性**

Teresa Salazar, Helder Araújo, Alberto Cano, Pedro Henriques Abreu

- 機械学習におけるグループ公正性は重要で、連合学習が異なるデータの偏りを増幅させる可能性がある。
- 連合学習とグループ公正性の交差点に関する47の研究があるが、包括的な調査はなかった。
- 本研究は新しい分類法を用いて関連するアプローチを整理し、データ分割、位置、戦略による評価を行う。
- 将来の研究に必要な領域を強調し、連合システムにおけるグループ公正性の達成の複雑さに対応する方法を提案する。

この研究面白そうだよね！連合学習でのグループ公正性の課題をバッチリ解決できたら、多様なデータを持つサービスにとって革命的になりそう。これからの研究で、もっと公正な未来が開けるといいな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CY, 68T01, I.2.6; I.5.1; K.4.1, **投稿日時:** 2024-10-04 18:39

- - -

### [Accelerating Deep Learning with Fixed Time Budget](http://arxiv.org/abs/2410.03790)

**固定時間予算での深層学習の加速**

Muhammad Asif Khan, Ridha Hamila, Hamid Menouar

- 深層学習は大量のデータと大規模モデルに依存し、学習時間が延びる傾向がある。
- 実用的な応用分野では限られた時間予算が求められ、効率的な学習法が必要。
- この論文では任意の深層学習モデルを固定時間内で訓練する手法を提案。
- 提案手法は分類と回帰タスクで一貫した学習性能の向上を示す。

この論文、時間が限られてるときにどうやって効果的にモデルを訓練するかのアイデアがすごくヒントになるかも。時間がないときの効率的な学習ってまるでテスト前の自分たちみたいだよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-10-03 21:18
