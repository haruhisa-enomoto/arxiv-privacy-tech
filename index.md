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

更新: 2024-07-16T04:20:13.377129

- - -

### [DataDream: Few-shot Guided Dataset Generation](http://arxiv.org/abs/2407.10910)

**DataDream：少量のデータでガイドするデータセット生成**

Jae Myung Kim, Jessica Bader, Stephan Alaniz, Cordelia Schmid, Zeynep Akata

- テキストから画像への拡散モデルは画像生成で最先端の結果を達成しているが、下流の応用での効果は未証明である
- 以前の方法は画像分類器の訓練用データを生成するが、ディストリビューション内の画像生成や微細な特徴の描写に苦労している
- DataDreamは少量の実際のクラス例に基づいて、より現実のデータ分布を忠実に再現する分類データセットを生成する
- 実験を通じて、7つのデータセットのうち7つで最先端の分類精度を超え、他の3つでも競争力を保っている

画像分類の精度向上、すごいじゃない！少量データでも高精度を実現できるのは、現実的なアプローチとして期待しかないね。

**Comment:** Accepted to ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-07-15 17:10

- - -

### [GeoMix: Towards Geometry-Aware Data Augmentation](http://arxiv.org/abs/2407.10681)

**GeoMix: 幾何意識を取り入れたデータ拡張に向けて**

Wentao Zhao, Qitian Wu, Chenxiao Yang, Junchi Yan

- Mixupは画像分類では成功を収めているが、グラフ学習タスクでは難しい
- 提案するGeoMixは、インプレースグラフ編集を活用し、近隣の特徴とラベルを用いて合成ノードを生成
- 理論分析により、ノードMixupにおける幾何情報の利用の正当性を解明し、局所性向上の重要性を強調
- GeoMixは少ないラベルデータでも最先端の結果を達成し、GNNSの一般化能力を向上

GeoMixって、Mixupのアイディアをグラフ学習まで広げちゃうんだね。これで新しいグラフ構造のデータがうまく扱えるといいな。

**Comment:** Published as a conference paper at KDD 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-07-15 12:58

- - -

### [Evaluating Model Bias Requires Characterizing its Mistakes](http://arxiv.org/abs/2407.10633)

**モデルのバイアス評価には誤りの特徴づけが必要**

Isabela Albuquerque, Jessica Schrouff, David Warde-Farley, Taylan Cemgil, Sven Gowal, Olivia Wiles

- 偶発的な相関に対抗してモデル性能を適切にベンチマークすることが重要
- 誤りの単なる定量化ではなく特徴づけがモデルバイアスを正しく反映
- 新しい指標SkewSizeを提案し、バイアスを捕捉するための指標として有用
- SkewSizeは既存の指標が捕捉しないバイアスを明らかにし、多様なシナリオで有効性を実証

新しい指標SkewSizeがどれだけバイアス検出に役立つかが楽しみ！未来のモデル開発に役立ちそうだね。

**Comment:** 17 pages, 6 figures, ICML 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-15 11:46

- - -

### [What Makes and Breaks Safety Fine-tuning? Mechanistic Study](http://arxiv.org/abs/2407.10264)

**セーフティファインチューニングの成否を左右する要因とは？機構的研究**

Samyak Jain, Ekdeep Singh Lubana, Kemal Oksuz, Tom Joy, Philip H. S. Torr, Amartya Sanyal, Puneet K. Dokania

- セーフティファインチューニングは、LLMを人間の安全な使い方に合わせるために重要
- 合成データ生成フレームワークを用いて、タスクと概念の相互作用モデル化
- 3つの主要なセーフティファインチューニング手法が、MLPの重みを最小限に変換し安全性を高める
- 実世界のモデル（Llama-2 7B、およびLlama-3 8B）で成果を検証

セーフティファインチューニングが安心して使えるようになるための研究って、すごく実用的で必要だよね！安全性を高める方法がいろいろ試されて確認されてるのもポイント高いね。

**Comment:** Preprint

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-14 16:12

- - -

### [Addressing Domain Discrepancy: A Dual-branch Collaborative Model to Unsupervised Dehazing](http://arxiv.org/abs/2407.10226)

**ドメインの不一致に対処する：教師なしでの曇り除去のためのデュアルブランチ協調モデル**

Shuaibin Fan, Minglong Xue, Aoxiang Ning, Senming Zhong

- 合成データは取得の課題を軽減するが、ドメインバイアスの問題を導入する
- デュアルブランチ協調無対デハーズモデル（DCM-dehaze）を提案
- デュアル深度分離畳み込みモジュールで情報の表現力と浅い特徴の相関を強化
- 残差高密度アーキテクチャを用いた特徴強化により、不要な特徴を除去しドメイン偏差を軽減

画像の鮮明さを保ちつつ曇りを除去できる技術なんてめっちゃすごいね！リアルタイムで動くのか、気になるかも。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-14 14:47

- - -

### [Sensitivity Analysis and Monte Carlo Based Uncertainty Quantification of the In-process Modal Parameters in Milling](http://arxiv.org/abs/2407.10202)

**フライス加工中のモードパラメータにおける感度分析とモンテカルロベースの不確実性定量化**

M. Hashemitaheri, T. T. Le, T. Khan, H. Cherukuri

- 切削深さと主軸回転速度が材料除去速度に影響しやすい
- 通常、安定ローブ図(SLD)は静的状態での機械動力学を用いるため信頼性に欠ける
- マルチバリアントのニュートン-ラフソン法を用い、加工中の動的パラメータを逆に抽出
- 合成データと実データを使用し、アルゴリズムの有効性を検証

新しいアプローチでフライス加工の効率が更に上がるかもなんてワクワクするよね！新しい技術でどんな未来が作られるのか楽しみ〜。



**トピック:** [合成データ](sd), **カテゴリ:** math.NA, cs.NA, math.DS, 49M15, 65Z05, 90-08, **投稿日時:** 2024-07-14 13:47

- - -

### [Lost and Found: Overcoming Detector Failures in Online Multi-Object Tracking](http://arxiv.org/abs/2407.10151)

**失われたものと見つけたもの: オンラインの複数物体追跡における検出器の失敗を克服する**

Lorenzo Vaquero, Yihong Xu, Xavier Alameda-Pineda, Victor M. Brea, Manuel Mucientes

- トラッキングによる検出（TbD）は、物体検出とそのリンクを行う簡単で効果的な方法である
- 現代の検出器は特定のフレームで物体を見逃すことがあり、それが追跡中断の原因となる
- BUSCAフレームワークは、隣接するトラック、動き、および学習されたトークンに基づく提案を生成する
- 5つの異なるトラッカーで一貫したパフォーマンス向上を示し、3つの異なるベンチマークで新しい基準を確立した

オンライン追跡の精度向上ってめっちゃ未来感あるよね！これ、ビデオ監視とか防犯カメラの進化に使えそうでワクワクする！

**Comment:** Accepted at ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-14 10:45

- - -

### [Optimal Kernel Choice for Score Function-based Causal Discovery](http://arxiv.org/abs/2407.10132)

**スコア関数に基づく因果発見のための最適カーネル選択**

Wenjie Wang, Biwei Huang, Feng Liu, Xinge You, Tongliang Liu, Kun Zhang, Mingming Gong

- スコアベースの手法は様々な因果構造を評価し、その適合度に基づいて因果関係を発見
- 再生核ヒルベルト空間（RKHS）を用いて一般的なデータ分布と因果関係をモデル化
- カーネルパラメータの手動選択は困難で最適性を確保しにくい
- 提案手法はマージナル尤度を最大化し、自動で最適なカーネルを選択

カーネル選択を自動化したことで、より正確な因果関係の発見が期待できるね。この技術が発展すると、因果関係の解析がもっと手軽になるかも！

**Comment:** Accepted by ICML2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ME, **投稿日時:** 2024-07-14 09:32

- - -

### [Sim-to-Real Domain Adaptation for Deformation Classification](http://arxiv.org/abs/2407.10011)

**変形分類のためのシム・トゥ・リアルドメイン適応**

Joel Sol, Jamil Fayyad, Shadi Alijani, Homayoun Najjaran

- 変形検出は素材の構造変化を評価・予測するために不可欠である
- データセット作成が困難なため、コンピュータビジョンによる自動化に課題がある
- 変形をシミュレートする合成データを生成する新しいフレームワークを提案
- インテリジェントなアダプターネットワークがシム・トゥ・リアル適応を促進し、分類結果を改善

実際のデータなしでの分類精度が上がるのがすごく興味深い！シミュレーションでここまでリアルにできるなんて、未来の技術が楽しみだね。

**Comment:** 7 pages, 5 figures, submitted to SMC

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-07-13 21:35

- - -

### [Harvesting Private Medical Images in Federated Learning Systems with Crafted Models](http://arxiv.org/abs/2407.09972)

**連合学習システムにおけるクラフトモデルを用いたプライベート医療画像の収集**

Shanghao Shi, Md Shahedul Haque, Abhijeet Parida, Marius George Linguraru, Y. Thomas Hou, Syed Muhammad Anwar, Wenjing Lou

- MediLeak攻撃を提案し、悪意のあるサーバーがクライアントからモデル更新を通じて高精度な患者画像を復元する方法を示す
- サーバーは元のモデルにクラフトモジュールを追加し、連合学習の過程でクライアントに配布してローカルトレーニングを実行させる
- クラフトモジュールのパラメーター更新を基に、サーバーがプライベートデータを解析・復元する技術を実装
- MedMNISTとCOVIDx CXR-4データセットで検証し、高い復元率と定量スコアを達成、患者画像の病気分類精度も元のデータと遜色ない

連合学習の裏に潜む危険性が明らかにされるとか、本当にびっくりだよね。最先端技術を悪用するアイデアにはドキドキしちゃうけど、対策も必要だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-07-13 18:31

- - -

### [Partner in Crime: Boosting Targeted Poisoning Attacks against Federated Learning](http://arxiv.org/abs/2407.09958)

**共犯関係: 連合学習に対するターゲット型ポイズニング攻撃の強化**

Shihua Sun, Shridatt Sugrim, Angelos Stavrou, Haining Wang

- 連合学習（FL）はターゲット型ポイズニング攻撃に対して脆弱である
- BoTPAはFLトレーニング前にデータラベルを偽装することで攻撃を強化
- BoTPAは複数の攻撃に対してその効果と適合性を評価
- BoTPAは様々な防御方法に対して攻撃成功率の大幅な向上を達成

FLへの攻撃方法ってこんなに工夫されているんだね！BoTPAの強化策は未来の研究にすごく活かせそう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-13 17:59

- - -

### [LFFR: Logistic Function For (single-output) Regression](http://arxiv.org/abs/2407.09955)

**LFFR: 単一出力回帰のためのロジスティック関数**

John Chiang

- プライバシーを保護しながら回帰モデルを訓練するため、完全同型暗号化を用いてデータを保つ。
- 固定ヘシアン行列を使用した線形回帰訓練を提案し、正規化されていなくても適用可能である。
- 新しい効率的なロジスティック回帰アルゴリズムLFFRを開発し、より複雑な関係モデルを可能にする。
- データと目標予測を正規化し、線形回帰で重みを小さく保つことで、リッジ回帰の代替となり得る。

なんか、プライバシーを守りながら機械学習ができるってすごいね！データの正規化とか、ちゃんと役立つの知らなかった！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-13 17:33

- - -

### [Benchmarking LLMs for Optimization Modeling and Enhancing Reasoning via Reverse Socratic Synthesis](http://arxiv.org/abs/2407.09887)

**最適化モデリングのためのLLMの評価と逆ソクラテス合成による推論の強化**

Zhicheng Yang, Yinya Huang, Wei Shi, Liang Feng, Linqi Song, Yiwei Wang, Xiaodan Liang, Jing Tang

- LLMの問題解決能力は数学的推論に優れているが、現実的な最適化問題には対応が難しい
- E-OPTというベンチマークを提案し、人間が理解可能な入力と出力を持つ最適化問題を評価
- ReSocraticという新しいデータ合成方法を提案し、少ないデータから最適化シナリオを段階的に生成
- LLMの精度をテストし、有望な結果を示すことで、GPT-4に近い性能を達成

この研究って、めっちゃ面白そうだね！特にReSocraticでどうやってデータを合成して推論を強化するかっていう新しいアプローチに注目！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-13 13:27

- - -

### [Enhancing Semantic Segmentation with Adaptive Focal Loss: A Novel Approach](http://arxiv.org/abs/2407.09828)

**適応焦点損失による意味セグメンテーションの強化: 新たなアプローチ**

Md Rakibul Islam, Riad Hassan, Abdullah Nazib, Kien Nguyen, Clinton Fookes, Md Zahidul Islam

- 小さく不規則な物体のセグメンテーション効果が低下する問題がある
- SmoothnessとVolume情報を取り入れた損失関数で改善を試みる
- 適応焦点損失(A-FL)はクラス不均衡を軽減し困難な例に重点を置く
- ResNet50-encoded U-NetでA-FLを評価し、一般的な手法を上回る成果を達成

この研究、医療画像の精度がすごく向上しそう！新しい診断工具の発展に繋がるって、未来が楽しみ♡

**Comment:** 15 pages, 4 figures

**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.AI, cs.CV, **投稿日時:** 2024-07-13 09:41

- - -

### [Preserving the Privacy of Reward Functions in MDPs through Deception](http://arxiv.org/abs/2407.09809)

**MDPにおける報酬関数のプライバシーをデセプションで保護する**

Shashank Reddy Chirra, Pradeep Varakantham, Praveen Paruchuri

- MDPにおいて、報酬関数は保護すべき嗜好構造を示す
- 差分プライバシーの現行研究ではIRLを用いた攻撃に対抗する理論的保証が不十分
- 新たにデセプション理論に基づくアプローチを提案し、特にシミュレーションを使用
- 実験結果から、シミュレーションを用いた新手法は既存手法よりも優れたプライバシー保護を実現

報酬関数のプライバシー保護って面白いね。新しい手法が既存の問題を解決していて、未来の応用が期待できそう！

**Comment:** ECAI 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.AI, **投稿日時:** 2024-07-13 09:03

- - -

### [Convex space learning for tabular synthetic data generation](http://arxiv.org/abs/2407.09789)

**表形式の合成データ生成のための凸空間学習**

Manjunath Mahendra, Chaithra Umesh, Saptarshi Bej, Kristian Schultz, Olaf Wolkenhauer

- 少数派クラスの凸空間からの合成サンプル生成が不均衡分類問題に有効
- NextConvGeNという生成器と識別器を持つディープラーニングアーキテクチャを提案
- 他の5つの最新モデルと比較し、分類とクラスタリング性能が高い
- 医学分野のデータセットで実験し、高ユーティリティモデルの必要性を議論

凸空間から生成したデータが本物そっくりで性能も良いなんてすごい！これで医療研究がもっと進むといいね。

**Comment:** 30 pages, 10 figures, submitted to Pattern Recognition journal

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-13 07:07

- - -

### [Private Heterogeneous Federated Learning Without a Trusted Server Revisited: Error-Optimal and Communication-Efficient Algorithms for Convex Losses](http://arxiv.org/abs/2407.09690)

**信頼できるサーバーなしでのプライベート異種連合学習再訪：凸損失に対する誤差最適・通信効率のアルゴリズム**

Changyu Gao, Andrew Lowy, Xingyu Zhou, Stephen J. Wright

- プライバシー保護のため、各シロ（例：病院）は患者データをサーバーや他のシロから守る必要がある
- ISRL-DPは各シロのデータを差分プライバシーで守り、データ漏洩を防ぐ
- 先行研究は同質データ（i.i.d.）での最適リスク境界を示していたが、異質データ（非i.i.d.）でも最適リスクが達成可能と確認
- 新アルゴリズムは、通信ラウンドを削減しつつ、滑らかな損失関数に対して最適リスクと一致する通信複雑性を達成

この研究、めっちゃ興味深いね！プライバシー守りながら効率的にデータ使う方法が現実的になりそうだよね。未来の医療とかにすごく役立ちそう！

**Comment:** The 41st International Conference on Machine Learning (ICML 2024)

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, math.OC, **投稿日時:** 2024-07-12 21:20

- - -

### [BoBa: Boosting Backdoor Detection through Data Distribution Inference in Federated Learning](http://arxiv.org/abs/2407.09658)

**BoBa: 連合学習におけるデータ分布推論を利用したバックドア検出の強化**

Ning Wang, Shanghao Shi, Yang Xiao, Yimin Chen, Y. Thomas Hou, Wenjing Lou

- 連合学習は分散性により中毒攻撃に脆い
- 非IIDデータはバックドア検出が困難であり、以前の手法は効果が低い
- 提案されたBoBaは、データ分布推論を用いてクラスタリングと投票システムに基づく検出を行う
- BoBaは、重複クラスタリングを用いて検出の堅牢性を向上し、攻撃成功率を0.001以下に抑えつつ高精度を維持

バックドア攻撃をした犯人も見つけられるかもね！次世代の連合学習の基礎になりそう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-07-12 19:38
