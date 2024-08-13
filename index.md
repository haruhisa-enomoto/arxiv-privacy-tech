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

更新: 2024-08-13T04:20:53.541024

- - -

### [Decentralized Intelligence Health Network (DIHN)](http://arxiv.org/abs/2408.06240)

**分散型インテリジェンス健康ネットワーク (DIHN)**

Abraham Nash

- 健康データの断片化による課題に対処し、医療AI利用を促進する理論的枠組み
- 自己主権IDと個人健康記録（PHR）を基盤に健康データ主権を確立
- 公共ブロックチェーン上で実装されたスケーラブルな連合学習プロトコルを利用
- 信頼不要な報酬メカニズムで参加を促進し、公平な報酬分配を確保

分散型の医療データネットワークで患者がデータを管理し、経済的にも恩恵を受けるアイデアってすごいよね！未来の医療はこんなふうに進化するかもって思うとワクワクする～。

**Comment:** 17 pages, 7 figures. arXiv admin note: substantial text overlap with   arXiv:2407.02461

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.CY, cs.DC, cs.ET, **投稿日時:** 2024-08-12 15:47

- - -

### [Lancelot: Towards Efficient and Privacy-Preserving Byzantine-Robust Federated Learning within Fully Homomorphic Encryption](http://arxiv.org/abs/2408.06197)

**Lancelot: 完全準同型暗号を利用した効率的でプライバシー保護されたビザンティン耐性の連合学習に向けて**

Siyang Jiang, Hao Yang, Qipeng Xie, Chuan Ma, Sen Wang, Guoliang Xing

- 金融や医療などの分野では、データガバナンスの厳しい規制が課題である
- 連合学習（FL）は、データの分散を保ちながら複数の機関での共同モデルトレーニングを実現
- FLは、特にモデル集約中の毒性攻撃に対して脆弱でありプライバシーリスクが存在する
- 提案するLancelotは完全準同型暗号を用い、従来の方法に比べて処理速度を20倍以上向上

完全準同型暗号で連合学習を守るなんて超カッコイイじゃん！プライバシーもバッチリで、これからのデータ解析がもっと安全に進みそうだね～。

**Comment:** 26 pages

**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-08-12 14:48

- - -

### [Centralized and Federated Heart Disease Classification Models Using UCI Dataset and their Shapley-value Based Interpretability](http://arxiv.org/abs/2408.06183)

**UCIデータセットを用いた集中型および連合型心疾患分類モデルのシャプレー値に基づく解釈可能性**

Mario Padilla Rodriguez, Mohamed Nafea

- 心血管疾患は世界的な主要死因であり、正確な診断法の必要性が高い
- 集中型設定では、サポートベクターマシン（SVM）が最高精度83.3%を達成し、従来の78.7%を上回る
- 連合学習アルゴリズムを用いて、データセットの自然な分割を活かし、プライバシーを保ちながら精度を維持
- シャプレー値に基づく解釈可能性分析が心疾患指標の既存の医療知識と一致

連合学習でプライバシーも守りつつ高精度を維持できるなんてすごい！これがもっと普及すれば安心して医療データが共有される未来が来るかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-12 14:29

- - -

### [Blind-Match: Efficient Homomorphic Encryption-Based 1:N Matching for Privacy-Preserving Biometric Identification](http://arxiv.org/abs/2408.06167)

**Blind-Match: プライバシー保護を意識したバイオメトリック認証のための効率的な準同型暗号ベースの1:Nマッチング**

Hyunmin Choi, Jiwon Kim, Chiyoung Song, Simon S. Woo, Hyoungshick Kim

- Blind-Matchは準同型暗号を活用し、プライバシーを保護しつつ効率的な1:Nマッチングを実現
- 特徴ベクトルを小さな部分に分けて処理することで、計算時間を最小化しつつデータのプライバシーを確保
- 顔認識ではLFWデータセットで99.63%のRank-1精度を達成し、準同型暗号を用いることで性能を向上
- 指紋認証ではPolyUデータセットでBlind-Touchを大きく上回る99.55%のRank-1精度を達成

新しい技術で認証システムがこんなに改善されるなんて、未来が楽しみ！大量のデータも0.74秒で処理ってすごすぎ！

**Comment:** Accepted to CIKM 2024 (Applied Research Track)

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CV, cs.CR, **投稿日時:** 2024-08-12 14:13

- - -

### [A-BDD: Leveraging Data Augmentations for Safe Autonomous Driving in Adverse Weather and Lighting](http://arxiv.org/abs/2408.06071)

**悪天候および照明条件下で安全な自動運転を実現するためのデータ拡張技術の活用：A-BDD**

Felix Assion, Florens Gressner, Nitin Augustine, Jona Klemenc, Ahmed Hammam, Alexandre Krattinger, Holger Trittenbach, Sascha Riemer

- 自動運転車の認識アルゴリズムは悪天候や照明条件の影響を大きく受ける
- A-BDDはBDD100Kを基にした60,000以上の合成画像を含むデータセットである
- 合成画像は雨、霧、曇り、日差し/影などの異なる強度レベルを持つ
- 特徴ベースの画質指標を活用し、ML訓練とテストに有用なデータを識別する手法を導入

合成データで悪天候でもしっかり認識できる車が増えるのってすごいね！もっと安全な自動運転ができるようになりそうでワクワクする。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-08-12 11:44

- - -

### [Don't You (Project Around Discs)? Neural Network Surrogate and Projected Gradient Descent for Calibrating an Intervertebral Disc Finite Element Model](http://arxiv.org/abs/2408.06067)

**プロジェクト・アラウンド・ディスク？ニューラルネットワーク代理と射影勾配降下による椎間板有限要素モデルのキャリブレーション**

Matan Atad, Gabriel Gruber, Marx Ribeiro, Luis Fernando Nicolini, Robert Graf, Hendrik Möller, Kati Nispel, Ivan Ezhov, Daniel Rueckert, Jan S. Kirschke

- 椎間板有限要素モデルの正確なキャリブレーションは診断および治療計画に重要である
- 従来のキャリブレーション法は計算負荷が高く、収束に時間がかかる
- ニューラルネットワーク代理を用いた新しい効率的なキャリブレーション法を提案
- 提案手法は既存の方法に比べ、高精度かつ迅速なキャリブレーションを実現

ニューラルネットワークを使って椎間板モデルのキャリブレーションを高速化するこの方法、今後の治療に革命を起こすかもね。3秒でキャリブレーション完了とか、信じられない！

**Comment:** Under submission. Project code:   https://github.com/matanat/IVD-CalibNN/

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-12 11:39

- - -

### [Understanding Byzantine Robustness in Federated Learning with A Black-box Server](http://arxiv.org/abs/2408.06042)

**ブラックボックスサーバーを用いた連合学習のビザンチン耐性の理解**

Fangyuan Zhao, Yuexiang Xie, Xuebin Ren, Bolin Ding, Shusen Yang, Yaliang Li

- 連合学習はビザンチン攻撃に弱く、悪意ある参加者の更新によりモデルの性能が低下
- これまでは特定のアグリゲーションルールに対して、異なるビザンチン攻撃に強いルールを提案
- ブラックボックスサーバーを使用することで、攻撃者はアグリゲーションルールにアクセスできず、いくつかのビザンチン攻撃が自然に防御される
- ブラックボックスサーバーは動的防御戦略を用いることで、最悪の攻撃影響を期待値レベルにまで軽減できる

この研究、めっちゃおもしろそう！ブラックボックスサーバーがどれだけ防御力があるのか、もっと知りたいね。実際のコードが公開されてるから、自分で試してみたらさらに理解が深まりそう！

**Comment:** We have released code on   https://github.com/alibaba/FederatedScope/tree/Byzantine_attack_defense

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-08-12 10:18

- - -

### [Generative Design of Multimodal Soft Pneumatic Actuators](http://arxiv.org/abs/2408.06002)

**多モーダルソフト空気圧アクチュエータの生成的設計**

Saswath Ghosh, Sitikantha Roy

- データ駆動型方法を用いて、ソフトアクチュエータの新しい設計を生成
- 公開データがないため、合成データセットを作成し、パラメトリックデザインデータでモデルを訓練
- ガウス混合モデルを適用し、新規パラメトリックデザインを生成し、距離ベースメトリクスで新規性と多様性を定義
- 生成された設計の品質を有限要素解析で評価し、多モーダルアクチュエーションの必要性を強調

ソフトロボットの設計がどんどん進化していきそうでワクワクするね。空間的な動きも自在にできるようになるなんて、未来のロボットがもっと現実的になりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-08-12 08:49

- - -

### [SZKP: A Scalable Accelerator Architecture for Zero-Knowledge Proofs](http://arxiv.org/abs/2408.05890)

**SZKP: ゼロ知識証明のためのスケーラブルなアクセラレータアーキテクチャ**

Alhad Daftardar, Brandon Reagen, Siddharth Garg

- ゼロ知識証明（ZKP）は検証可能計算の新たなパラダイム
- zkSNARKは証明生成が非常に時間がかかるが、簡潔な証明を迅速に検証可能
- 主要な原始には数字理論変換（NTT）とマルチスカラ乗算（MSM）があり、ハードウェアアクセラレーションの候補
- SZKPはNTTとMSMの両方をオンチップで加速し、CPU、ASIC、GPUに対してそれぞれ400倍、3倍、12倍の速度向上を実現

ゼロ知識証明めっちゃ面白そう！特に400倍の速度向上とか、どんだけ効率上がるんだろうってワクワクするよね。これからのクラウド計算がもっと快適になりそうだよね。

**Comment:** Accepted to the 33rd International Conference on Parallel   Architectures and Compilation Techniques (PACT), 2024

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.AR, cs.CR, **投稿日時:** 2024-08-12 01:53

- - -

### [Online-Score-Aided Federated Learning: Taming the Resource Constraints in Wireless Networks](http://arxiv.org/abs/2408.05886)

**オンラインスコア支援型連合学習: 無線ネットワークにおけるリソース制約の克服**

Md Ferdous Pervej, Minseok Choi, Andreas F. Molisch

- 連合学習はデータプライバシーを保護するが、無線ネットワークのパラメータの変動やシステム構成の異質性が課題
- 無線デバイスは連合学習に少量のストレージしか割けず、オンラインで新しいトレーニングデータが到着する場合がある
- 提案する新しいアルゴリズムOSAFLは、リソース制約のもとで無線アプリケーションに関連するタスクを学習する
- 正規化された勾配の類似性とスコアに基づくクライアントの更新の重み付けにより、収束率を向上させる

無線ネットワークで連合学習ってすごく大変そうだけど、それを解決する新しい方法が考えられてめっちゃ面白そう！これからの無線技術がもっと進化する予感がするよね！

**Comment:** Under review for possible publication in IEEE Transactions on   Wireless Communications (TWC)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.NI, cs.SY, eess.SY, **投稿日時:** 2024-08-12 01:27

- - -

### [SABER-6D: Shape Representation Based Implicit Object Pose Estimation](http://arxiv.org/abs/2408.05867)

** SABER-6D: 形状表現に基づく暗黙の物体ポーズ推定 **

Shishir Reddy Vutukur, Mengkejiergeli Ba, Benjamin Busam, Matthias Kayser, Gurprit Singh

- 新しいエンコーダ・デコーダアーキテクチャ「SABER」を提案し、埋め込み空間で物体の6Dポーズを学習
- 画像入力からポーズを学ぶために形状表現を補助タスクとして実行
- 任意の対称性を持つ物体に適したパイプラインで、CADモデルのみで訓練可能
- 実験評価により、Occlusion-LineMODおよびT-LESSデータセットで対称・非対称物体のベンチマークに近い結果を達成

形状を補助タスクとして使うアイディアが素敵だなぁ。これでどんな対称物体でもいけちゃうとか、未来の3Dモデリングが楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-11 21:59

- - -

### [On the Convergence of a Federated Expectation-Maximization Algorithm](http://arxiv.org/abs/2408.05819)

**連合期待最大化アルゴリズムの収束について**

Zhixu Tao, Rajita Chandak, Sanjeev Kulkarni

- データの異質性が連合学習アルゴリズムの収束率における主要な障害
- 連合$K$線形回帰モデルの期待最大化アルゴリズムの収束率を詳細に解析
- 信号対雑音比（SNR）が$\Omega(\sqrt{K})$であれば、適切に初期化されたアルゴリズムは最適距離内で収束
- クライアント数$m$がデータポイント数$n$に対して指数関数的に増加すると、一定回数の反復で収束可能

データの異質性が逆に連合学習の収束を速めることがあるんだね！収束率の解析って、本当に面白いことが分かる気がしてきたよ。



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-08-11 16:46

- - -

### [Personalized Federated Learning for improving radar based precipitation nowcasting on heterogeneous areas](http://arxiv.org/abs/2408.05761)

**異質エリアのレーダーを用いた降水現象予測向けパーソナライズド連合学習の改善**

Judith Sáinz-Pardo Díaz, María Castrillo, Juraj Bartok, Ignacio Heredia Cachá, Irina Malkin Ondík, Ivan Martynovskyi, Khadijeh Alibabaei, Lisana Berberi, Valentin Kozlov, Álvaro López García

- 環境などの多様な分野で増加するデータの処理技術の重要性が増している
- 気象レーダーから得られる膨大なデータには、ディープラーニングが有用である
- 各機関に分散するレーダーデータに対し、パーソナライズド連合学習アーキテクチャ(adapFL)を提案
- adapFLは、従来の連合学習や個別のディープラーニングモデルを上回る性能を示している

天気予測のための新技術ってワクワクするよね！万が一の災害予測がもっと正確になったら安心だよね。

**Comment:** Accepted for publication in Earth Science Informatics

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, physics.ao-ph, **投稿日時:** 2024-08-11 12:46

- - -

### [Disposable-key-based image encryption for collaborative learning of Vision Transformer](http://arxiv.org/abs/2408.05737)

**使い捨て鍵に基づく画像暗号化によるVision Transformerの協調学習**

Rei Aso, Sayaka Shiota, Hitoshi Kiya

- 複数のクライアントから共有される機密データの安全な学習を提案
- 各クライアントが独自に準備した暗号化キーを用いて画像を暗号化
- クライアントはキーを使い捨てることができ、通信コストも低減
- CIFAR-10データセットでの実験により分類精度と制限付きランダム置換行列の有効性を確認

使い捨ての鍵を使うって、キーの管理が簡単になりそうだね。通信コスト削減も魅力的だし、これからもっとプライバシー保護が進みそうじゃない？



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-11 09:55

- - -

### [Deep Learning with Data Privacy via Residual Perturbation](http://arxiv.org/abs/2408.05723)

**残差摂動によるデータプライバシーを伴う深層学習**

Wenqi Tao, Huaming Ling, Zuoqiang Shi, Bao Wang

- ディープラーニングにおけるプライバシー保護は重要で、既存の手法はプライバシーを守るが、実用性の低下や計算過負荷の問題がある
- 本研究では、ガウスノイズをResNetの各残差写像に注入する確率微分方程式に基づいた摂動を提案
- 理論的には、この残差摂動が差分プライバシーを保証し、ディープラーニングの一般化ギャップを減少させると証明
- 経験的には、この手法が計算効率が高く、メンバーシッププライバシーを犠牲にせずに最新の差分プライバシーを用いた確率的勾配降下法よりも優れていることを示した

これめっちゃ面白そうじゃない？プライバシーを守りながらも性能を落とさない方法がどれだけ普及するか今後が楽しみ！これから色んなアプリやサービスがもっと安全に使えるようになりそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.CV, **投稿日時:** 2024-08-11 08:26

- - -

### [The Bandit Whisperer: Communication Learning for Restless Bandits](http://arxiv.org/abs/2408.05686)

**バンディットのささやき者: 静動的バンディットのためのコミュニケーション学習**

Yunfan Zhao, Tonghan Wang, Dheeraj Nagaraj, Aparna Taneja, Milind Tambe

- 連続アームバンディット(RMABs)に強化学習を適用することで、資源制約と時間的動態を持つ配分問題に対処する
- しかし、従来のRMABモデルはデータ収集プロトコルの違いや差分プライバシーによる意図的なノイズなどのデータエラーの課題を無視している
- 初のコミュニケーション学習アプローチを提案し、どのアームがコミュニケーションに関与することでデータエラーの影響を軽減するかを研究
- Qネットワークアーキテクチャを使用し、メッセージの共同効用を考慮したコミュニケーション戦略を学習することで、RMABの性能が大幅に向上することを理論的および実証的に確認

リアルタイムでデータエラーに対処できるなんて、この研究ってきっと実用的でスゴい！未来のAIがもっと賢くなりそうだね、ワクワクする！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.MA, **投稿日時:** 2024-08-11 03:39

- - -

### [Efficient Federated Learning Using Dynamic Update and Adaptive Pruning with Momentum on Shared Server Data](http://arxiv.org/abs/2408.05678)

**動的更新と適応型プルーニングを用いた効率的な連合学習の実現**

Ji Liu, Juncheng Jia, Hong Zhang, Yuhui Yun, Leye Wang, Yang Zhou, Huaiyu Dai, Dejing Dou

- 低トレーニング効率と限られた計算資源というFLの課題に対処
- サーバー上の共有データを活用し、動的に更新する簡単なアルゴリズムを提案
- 動的更新と適応最適化メソッドにより、グローバルなモメンタムを利用して精度向上
- 各層の多様な特徴に適応するレイヤー適応型モデルプルーニングメソッドを開発

この論文、効率が16.9倍向上とかすごくない？FLの新しい可能性が広がりそうでワクワクするね！

**Comment:** 27 pages, to appear in TIST

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.AI, cs.LG, **投稿日時:** 2024-08-11 02:59

- - -

### [Federated Smoothing Proximal Gradient for Quantile Regression with Non-Convex Penalties](http://arxiv.org/abs/2408.05640)

**連合平滑近似勾配法による非凸ペナルティ付き分位点回帰**

Reza Mirzaeifard, Diyako Ghaderyan, Stefan Werner

- IoTの分散センサーが生成する高次元かつスパースなデータの解析が困難
- 従来の分位点回帰法では非凸スパースペナルティと損失関数の非滑らかさに対応が難しい
- 提案する連合平滑近似勾配法（FSPG）は精度と計算速度の両面で改善を実現
- MCPやSCADなどの非凸ペナルティを活用し、スパースモデル内の重要な予測子を特定・保持

非凸ペナルティを使ってスパースデータの解析精度を上げるなんて、まさに未来感あふれるアイデアだね！IoTのデータをそのままデバイス上で処理する点もとても現実的で興味深いなって思うよ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-10 21:50

- - -

### [Quantum-secure multiparty deep learning](http://arxiv.org/abs/2408.05629)

**量子安全なマルチパーティディープラーニング**

Kfir Sulimany, Sri Krishna Vadlamani, Ryan Hamerly, Prahlad Iyengar, Dirk Englund

- セキュアなマルチパーティ計算は、分散ユーザー間で多変量関数を評価しながら入力のプライバシーを保つ
- 深層学習推論の計算強度によりクラウドサーバーでの脆弱性が生じる
- 光の量子性を利用した線形代数エンジンを導入し、既存のテレコミュニケーション技術で情報理論的に安全
- MNIST分類タスクで96%以上のテスト精度を達成し、データ漏洩は非常に低量

量子技術とディープラーニングの融合で、さらに安全なプライバシー技術が可能になるなんてワクワクするね💡専用ハードウェアが不要だから、早く実用化されそうな予感！



**トピック:** [秘密計算](mpc), **カテゴリ:** quant-ph, cs.AI, cs.IT, cs.LG, math.IT, physics.optics, **投稿日時:** 2024-08-10 20:48

- - -

### [Advancing oncology with federated learning: transcending boundaries in breast, lung, and prostate cancer. A systematic review](http://arxiv.org/abs/2408.05249)

**連合学習でがん治療を前進：乳がん、肺がん、前立腺がんの境界を越えて。系統的レビュー**

Anshu Ankolekar, Sebastian Boie, Maryam Abdollahyan, Emanuela Gadaleta, Seyed Alireza Hasheminasab, Guang Yang, Charles Beauville, Nikolaos Dikaios, George Anthony Kastis, Michael Bussmann, Sara Khalid, Hagen Kruger, Philippe Lambin, Giorgos Papanastasiou

- 連合学習 (FL) は、従来の中央集中型機械学習 (ML) のプライバシー問題を克服し、多様なマルチセンターデータを活用
- FL は乳がん、肺がん、前立腺がんにおいてMLの一般化性能、パフォーマンス、データプライバシーを向上
- 25の研究中15でFLが中央集中型MLを上回り、多様なMLモデルと臨床応用で精密医療の統合を促進
- 再現性、標準化、方法論に課題があるが、FLの実用的な利点が実世界データ活用と臨床ニーズの解決に重要な役割

これ、未来のがん治療のスタンダードになるかもね！FLの進歩で、もっと安全に患者データを活用できるようになりそう。興味深いね！

**Comment:** 5 Figures, 3 Tables, 1 Supplementary Table

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CE, eess.IV, **投稿日時:** 2024-08-08 14:36

- - -

### [The Role and Applications of Airport Digital Twin in Cyberattack Protection during the Generative AI Era](http://arxiv.org/abs/2408.05248)

**空港デジタルツインの役割および生成AI時代におけるサイバー攻撃保護への応用**

Abraham Itzhak Weinberg

- デジタルツイン(DTs)は空港のセキュリティ向上に貢献
- DTsと生成AI(GenAI)の統合により、新たなサイバー攻撃防御の可能性を開拓
- サイバー攻撃シナリオをシミュレーションし、防御テストのための合成データを生成
- DTsを用いて脆弱性の評価、異常検知、脅威ハンティングを実現

空港のデジタルツインと生成AIを組み合わせるなんて、未来っぽくてワクワクするね！リアルの脅威をしっかり仮想で防ぐ技術、どんどん広がってほしいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-08-08 14:35

- - -

### [Differentially Private Data Release on Graphs: Inefficiencies and Unfairness](http://arxiv.org/abs/2408.05246)

**グラフ上の差分プライベートなデータ公開: 非効率と不公正**

Ferdinando Fioretto, Diptangshu Sen, Juba Ziani

- ネットワークデータは多くの分野で重要で、敏感なユーザーデータを含むことが多い
- 差分プライバシー(DP)は個人情報の漏洩を防ぐが、導入時に不正確さやバイアスが生じる
- DPのバイアスが異なる集団に不均等に分布し、不公正を引き起こす可能性がある
- ネットワークの重みを非公開で保ったまま最短経路を提供する問題を検討し、理論と実証的証拠を提供

実際の交通ネットワークとか、リアルな生活に直結してる問題なのが面白いね！プライバシー保護のために何ができるか学べるの、将来に役立ちそう！

**Comment:** 32 pages

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.CY, cs.LG, **投稿日時:** 2024-08-08 08:37

- - -

### [SocFedGPT: Federated GPT-based Adaptive Content Filtering System Leveraging User Interactions in Social Networks](http://arxiv.org/abs/2408.05243)

**SocFedGPT：ユーザーインタラクションを活用した連合学習ベースの適応型コンテンツフィルタリングシステム**

Sai Puppala, Ismail Hossain, Md Jahangir Alam, Sajedul Talukder

- 連合学習フレームワークでユーザーインタラクションとコンテンツの関連性を向上させる
- 個別のGPTおよび文脈ベースのソーシャルメディアLLMモデルを利用
- 4つのクライアントが基本GPT-2モデルとローカルデータを受信、連合集約でモデルを維持
- ソーシャルエンゲージメントを定量化し、行列分解技術でパーソナライズされたコンテンツを提案

内容がとても面白そう！連合学習を使ってソーシャルメディアの質が上がるって未来っぽいね！ぜひ実現してほしいなぁ。

**Comment:** This research paper is submitted to ASONAM 2024 conference on   Advances in Social Networks Analysis and Mining and going to be published in   Springer

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.IR, cs.SI, **投稿日時:** 2024-08-07 20:05

- - -

### [FLASH: Federated Learning-Based LLMs for Advanced Query Processing in Social Networks through RAG](http://arxiv.org/abs/2408.05242)

**FLASH: 連合学習を用いた高度なクエリ処理のためのLLMによるソーシャルネットワーク向けRAG**

Sai Puppala, Ismail Hossain, Md Jahangir Alam, Sajedul Talukder

- 連合学習GPTを用いた個別化チャットボットシステムを導入
- 分散データソースから訓練し、プライバシーとセキュリティを確保
- 直感的なインターフェースでソーシャルメディアのトレンドやユーザー生成コンテンツを提供
- 入力ファイルの効率的な処理、テキストデータの解析とメタデータ添付、高度な言語モデルによる質疑応答を実現

ソーシャルネットワーク上での情報取得やユーザーエンゲージメントがめっちゃ進化しそう！このチャットボット、いろんな情報源から学んでくれるから、すごく便利になりそうね。

**Comment:** This research paper is submitted to ASONAM 2024 conference on   Advances in Social Networks Analysis and Mining and going to be published in   Springer

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.IR, cs.SI, **投稿日時:** 2024-08-06 22:28
