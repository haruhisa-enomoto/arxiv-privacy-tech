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

更新: 2024-07-03T04:21:02.803265

- - -

### [Decentralized Intelligence Network (DIN)](http://arxiv.org/abs/2407.02461)

**分散型インテリジェンスネットワーク (DIN)**

Abraham Nash

- データの断片化とサイロ化から生じるデータ主権とAI利用の課題を解決
- 個人データストアと連合学習プロトコルをブロックチェーン上で利用し、データは参加者に保持
- スケーラブルで信頼のない報酬メカニズムが参加を促進し、公平な報酬分配を実現
- 参加者がデータの制御と経済的利益を享受しつつ、分散型エコシステムに貢献

ブロックチェーンとAIの融合が新しい時代を切り開くね！分散型のソリューションで公平性が保たれるなんて、未来が楽しみ♪

**Comment:** 10 pages, 1 figure

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.CY, cs.DC, cs.ET, cs.LG, **投稿日時:** 2024-07-02 17:40

- - -

### [Enable the Right to be Forgotten with Federated Client Unlearning in Medical Imaging](http://arxiv.org/abs/2407.02356)

**医療画像における連合クライアントの学習解除による忘れられる権利の実現**

Zhipeng Deng, Luyang Luo, Hao Chen

- 連合学習における忘れられる権利は未解決の課題である
- 提案された連合クライアントの学習解除（FCU）が初めて医療画像に適用される
- 特徴レベルの学習解除と頻度ガイドの記憶保持により、モデルの一般化能力を維持しつつ忘却を実現
- 2つの医療画像データセットで評価され、再学習からの速度が10-15倍向上

医療画像の分野で初のこのアプローチ、やばいかも。これ、診断のスピードアップとかにめっちゃ効くかもね！



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, cs.LG, **投稿日時:** 2024-07-02 15:21

- - -

### [FedIA: Federated Medical Image Segmentation with Heterogeneous Annotation Completeness](http://arxiv.org/abs/2407.02280)

**FedIA: 異種アノテーション完成度を持つ連合医用画像セグメンテーション**

Yangyang Xiang, Nannan Wu, Li Yu, Xin Yang, Kwang-Ting Cheng, Zengqiang Yan

- 連合学習は医用画像セグメンテーションにおいて有望だが、クライアント間のアノテーションの一様性と完全性は厳しい仮定である
- 医療実務では不完全なアノテーションが一般的であり、誤ったピクセルラベルがニューラルネットワークの性能を損なうことがある
- 本研究で導入されたFedIAは、不完全なアノテーションを低品質データとして捉え、その影響を軽減する
- クライアントレベルでアノテーションの完全性を評価し、包括的なアノテーションを持つクライアントの影響を強化することで、モデルが正確なデータで訓練されるようにする

不完全なデータをうまく活用する仕組みが新しいね！みんな違うデータを持ってても、ちゃんと成果が出るのはすごい。これ、医療現場での導入が進んだらデータ共有で役立ちそうだね。

**Comment:** Early accepted by MICCAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-07-02 14:08

- - -

### [Federated Distillation for Medical Image Classification: Towards Trustworthy Computer-Aided Diagnosis](http://arxiv.org/abs/2407.02261)

**医療画像分類のための連合蒸留: 信頼できるコンピューター支援診断に向けて**

Sufen Ren, Yule Hu, Shengchao Chen, Guanjun Wang

- 医療画像分類は臨床診断支援において重要な役割を果たす
- プライバシーの観点から集中型のデータ保存とモデル訓練が複雑化
- FedMICは連合学習を用いて、プライバシーを保ちながらローカルとグローバルな知識で学習
- 通信オーバーヘッドを最小限に抑えつつ、多様なデータを扱うカスタマイズモデルを提供

病院同士が団結して、みんなで一緒に学ぶってステキだね！特に、通信効率を保ちつつプライバシーも守るところが未来感あってワクワクする☆

**Comment:** work in progress. arXiv admin note: text overlap with   arXiv:2401.01493

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-02 13:38

- - -

### [Synthetic Multimodal Question Generation](http://arxiv.org/abs/2407.02233)

**合成マルチモーダル質問生成**

Ian Wu, Sravan Jayanthi, Vijay Viswanathan, Simon Rosenberg, Sina Pakazad, Tongshuang Wu, Graham Neubig

- MMRAGはマルチモーダル文書への質問応答に強力だが、高品質なデータセットが不足
- SMMQGは、リトリーバー、LLM、LMMを活用して質問と回答ペアを生成
- Wikipedia文書を対象に1024の質問を生成し、最先端モデルの評価を実施
- 人間による評価で、合成データの品質がクラウドソースベンチマークMMQAと同等であると確認

合成データでモデル評価がもっと細かくできるなんてすごいね！これからのマルチモーダル研究がますます進化しそう。

**Comment:** Submitted to ARR June 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-07-02 12:57

- - -

### [RollupTheCrowd: Leveraging ZkRollups for a Scalable and Privacy-Preserving Reputation-based Crowdsourcing Platform](http://arxiv.org/abs/2407.02226)

**RollupTheCrowd: zkRollupsを活用したスケーラブルでプライバシー保護を備えた評判ベースのクラウドソーシングプラットフォーム**

Ahmed Mounsf Rafik Bendada, Mouhamed Amine Bouchiha, Mourad Rabah, Yacine Ghamri-Doudane

- 現在のブロックチェーンベースの評判システムは、効率とプライバシーを両立しながらスケーラビリティを保つことが難しい
- RollupTheCrowdはzkRollupsを活用してシステムのスケーラビリティを向上しつつ、ユーザープライバシーを保護する新しいフレームワークを提案
- オフチェーンのデータストレージを採用し、ブロックチェーンの負荷を軽減することでパフォーマンスを最適化
- スマートコントラクトとゼロ知識証明を使用してガス消費を20倍削減し、実証的な結果で有効性とスケーラビリティを証明

新しい技術を使って、大規模なクラウドソーシングでも効率を高めつつプライバシーを守れるってすごいね！将来のアプリケーションがますます安全で便利になるといいな。

**Comment:** 9 pages, 8 figures, 2 tables, Paper accepted at IEEE 48th Annual   Computers, Software, and Applications Conference (COMPSAC) IEEE, Osaka, Japan   (2024)

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-02 12:51

- - -

### [Attack-Aware Noise Calibration for Differential Privacy](http://arxiv.org/abs/2407.02191)

**差分プライバシーのための攻撃感知ノイズキャリブレーション**

Bogdan Kulynych, Juan Felipe Gomez, Georgios Kaissis, Flavio du Pin Calmon, Carmela Troncoso

- 差分プライバシーは、機械学習モデルを訓練する際の情報漏洩リスクを低減
- 従来の手法はプライバシーバジェット$\epsilon$に基づくノイズスケール設定が多い
- 新手法は攻撃リスクに直接ノイズスケールを合わせ、従来より少ないノイズで高い実用性を実現
- 特定攻撃リスクに対応するノイズスケール設定により、同リスク水準でモデルの精度が向上

これは内容がすごく革新的だね！プライバシーを守りつつ、精度も良くなるなんて未来のML（機械学習）モデルが楽しみ！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, math.ST, stat.ML, stat.TH, **投稿日時:** 2024-07-02 11:49

- - -

### [Exploring Federated Learning Dynamics for Black-and-White-Box DNN Traitor Tracing](http://arxiv.org/abs/2407.02111)

**ブラックボックスとホワイトボックスのDNNトレイタートレースのための連合学習ダイナミクスの探索**

Elena Rodriguez-Lois, Fernando Perez-Gonzalez

- 連合学習（FL）は分散データ所有者間での共同モデルトレーニングを可能にするが、モデル所有権の保護と漏洩時の出所特定に課題がある
- 本論文ではFL分類器におけるブラック＆ホワイトトレイタートレースウォーターマーキングの適応を探求
- 表示されたデータとして、対策としては隠れ層のニューロン数を増加させることで対抗
- コラボレーション攻撃に対してもFLフレームワーク内で漏洩耐性のあるトレイサビリティが初期段階から可能であることが示された

FLとウォーターマーキング技術を組み合わせるのって面白そう！これからの応用でもっと安全なデータ共有が期待できるね。

**Comment:** This work has been submitted to the 2nd IEEE International Conference   on Federated Learning Technologies and Applications (FLTA 2024) for possible   publication. Copyright may be transferred without notice, after which this   version may no longer be accessible

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-02 09:54

- - -

### [Contribution Evaluation of Heterogeneous Participants in Federated Learning via Prototypical Representations](http://arxiv.org/abs/2407.02073)

**連合学習における異質な参加者の貢献評価：プロトタイプ表現を通じて**

Qi Guo, Minghao Yao, Zhen Tian, Saiyu Qi, Yong Qi, Yun Lin, Jin Song Dong

- 連合学習における貢献評価は、低品質データセットの検出やモデルの堅牢性向上、インセンティブ設計など、多領域で重要となっている
- 既存の貢献評価方法はデータ量、モデルの類似性、補助テストデータセットに依存しており、多様なシナリオで成功を収めている
- データ分布の異質性が効果を減少させるため、新たな視点である表現を用いて貢献評価を探求
- 提案手法は、\emph{Class Contribution Momentum}と呼ばれる新指標を導入し、補助テストデータセットに依存せずに効果的かつ効率的に異質な参加者の貢献評価を実現

連合学習でデータ分布のバラバラさを克服して、新しい評価方法を考えたんだね！データセットに頼らずに評価できるのは、実用性が高そうで楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-02 09:05

- - -

### [SAVE: Segment Audio-Visual Easy way using Segment Anything Model](http://arxiv.org/abs/2407.02004)

**SAVE：Segment Anythingモデルを用いた音声視覚セグメントの簡易方法**

Khanh-Binh Nguyen, Chae Jung Park

- 音声視覚セグメンテーション（AVS）は、視覚シーン内の聴覚要素を正確に特定し、ピクセルレベルでマスクを予測することを目的とする
- 事前学習されたSegment Anythingモデル（SAM）を効率的に適応させる軽量アプローチを提案
- トランスフォーマーブロックにイメージエンコーダアダプタを追加し、オーディオ特徴を疎プロンプトとしてエンコードする
- 入力解像度を1024から256ピクセルに減少させつつ、最新技術（SOTA）より高い性能を達成

視覚と音がどう絡み合うのかを軽量モデルで実現するなんて、めっちゃ気になるテーマ！これからAVSの分野もどんどん進化しそうでワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.SD, eess.AS, **投稿日時:** 2024-07-02 07:22

- - -

### [Federated Binary Matrix Factorization using Proximal Optimization](http://arxiv.org/abs/2407.01776)

**近接最適化を用いた連合バイナリマトリックス分解**

Sebastian Dalleiger, Jilles Vreeken, Michael Kamp

- バイナリデータの情報抽出は、多くの研究分野において重要である
- 現実世界のデータは分散されプライバシーを求められるため、単純なBMFの適用は困難
- 連合学習の観点からBMFを適応させ、効率的な勾配ベースの最適化を実現
- 提案手法は既存のBMFを超え、質と効果において優れた結果をもたらす

連合学習を使ってプライバシーも守りながらBMFするって、おもしろそう！実際にどんな分野やデータで使われるのか気になるね。



**トピック:** [連合学習](fl), [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-07-01 20:10

- - -

### [LLM See, LLM Do: Guiding Data Generation to Target Non-Differentiable Objectives](http://arxiv.org/abs/2407.01490)

**言語モデルを導く合成データ生成: 非微分可能な目標を達成するためのアプローチ**

Luísa Shimabucoro, Sebastian Ruder, Julia Kreutzer, Marzieh Fadaee, Sara Hooker

- 合成データの統合がモデルの内部偏向、キャリブレーション、生成されたテキスト属性や選好に与える影響を系統的に研究
- 合成データの「中立」に見えるプロンプトでもモデルが特定の属性に対して敏感であることを発見
- データ生成プロセスを利用してテスト時に意図した特性をモデルに誘導できる可能性を検討
- 情報量の高い合成データの品質向上と一般用途のモデルの出現が、新たなアプローチ「アクティブ継承」を提案するきっかけに

モデルがデータの意図から影響を受けやすくなるところが面白いよね。今後、どうやって合成データを賢く使って行くのか気になるなぁ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-07-01 17:26

- - -

### [Optimizing Age of Information in Vehicular Edge Computing with Federated Graph Neural Network Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2407.02342)

**連合グラフニューラルネットワーク多エージェント強化学習による車両エッジコンピューティングにおける情報の鮮度の最適化**

Wenhua Wang, Qiong Wu, Pingyi Fan, Nan Cheng, Wen Chen, Jiangzhou Wang, Khaled B. Letaief

- インテリジェント車両とITSの発展により、車両のセンサーが計算負荷と遅延に敏感なタスクを実行
- RSUを通じたデータ処理を行う車載エッジコンピューティング(VEC)で、情報の鮮度指標としてAoIに注目
- 情報漏洩を防ぐため、連合学習(FL)を活用し、生データではなくモデルパラメータを共有
- 初めての試みとして、道のシナリオをグラフデータ構造として構築し、GNNベースの連合学習フレームワークを提案

今、どんどん進化しているインテリジェント車両とそのための技術がとても興味深いよね！この研究が実用化されたら、車両同士が賢く通信してもっと安全で効率的な交通が実現できそうだね！

**Comment:** This paper has been submitted to IEEE Journal. The source code has   been released at:   https://github.com/qiongwu86/Optimizing-AoI-in-VEC-with-Federated-Graph-Neural-Network-Multi-Agent-Reinforcement-Learning

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.MA, cs.NI, **投稿日時:** 2024-07-01 15:37

- - -

### [Semantic-guided Adversarial Diffusion Model for Self-supervised Shadow Removal](http://arxiv.org/abs/2407.01104)

**意味ガイド型対戦的拡散モデルによる自己教師付き影除去**

Ziqi Zeng, Chen Zhao, Weiling Cai, Chenyu Dong

- 既存の未教師あり方法の課題として、不整合な対データと真実のラベル取得の手間
- GANベースのトレーニングはモード崩壊や不安定な最適化に直面
- 提案するフレームワークは、まず粗い結果を生成しサイクル一貫構造で合成データを作成
- 第二ステージでは、拡散ベースの復元モジュールでテクスチャとエッジアーティファクトを強化

自己教師付きで影を取り除くって面白そうだね！特に、サイクル一貫構造と拡散ベースの技術がどんな効果を生むのか気になるなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-01 09:14

- - -

### [FedRC: A Rapid-Converged Hierarchical Federated Learning Framework in Street Scene Semantic Understanding](http://arxiv.org/abs/2407.01103)

**FedRC: 通りの場面の意味理解における階層的連合学習フレームワークの急速収束**

Wei-Bin Kou, Qingfeng Lin, Ming Tang, Shuai Wang, Guangxu Zhu, Yik-Chung Wu

- 自動運転車のための通りの場面の意味理解（TriSU）は、都市間のドメインシフトにより一般化が難しい
- 階層的連合学習（HFL）はTriSUの一般化を改善できるが、都市間のデータ異質性による収束遅延が問題
- 本研究では、Gaussian分布を用いた重み設計によりRGBデータセットの特徴を捉えたFedRCフレームワークを提案
- 提案手法は最先端ベンチマークと比較し、mIoU、mPrecision、mRecall、mF1でそれぞれ約35-40%の収束速度向上を示した

実世界のデータの異質性を考慮しつつ、性能アップを実現するアプローチだね。将来的な自動運転車にとって、すごく重要な技術だと感じるよ！

**Comment:** This work has been accepted by 2024 IEEE/RSJ International Conference   on Intelligent Robots and Systems (IROS 2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, **投稿日時:** 2024-07-01 09:10

- - -

### [SplitLoRA: A Split Parameter-Efficient Fine-Tuning Framework for Large Language Models](http://arxiv.org/abs/2407.00952)

**SplitLoRA: 大規模言語モデルの分割パラメータ効率的ファインチューニングフレームワーク**

Zheng Lin, Xuanjie Hu, Yuxin Zhang, Zhe Chen, Zihan Fang, Xianhao Chen, Ang Li, Praneeth Vepakomma, Yue Gao

- 大規模言語モデル(LLM)は高複雑性モデルや大規模データセットの処理で成功しているが、高品質な公開データセットの枯渇が迫っている
- 連合学習(FL)によるLLMのファインチューニングは、分散プライベートデータ上で協調的に行う利点があるが、モデルの巨大さがクライアントに負担をかける
- 分割学習(SL)は、モデルの主要なトレーニング負荷をサーバにオフロードし、より小さなデータサイズで活性化/その勾配を交換する有望な解決策である
- SplitLoRAは初のSL LLMファインチューニングフレームワークとして、FLの並列トレーニングとSLのモデル分割の利点を融合し、訓練効率を大幅に向上させる

分割でモデルの負担を軽減しながら、FLの協調的な利点も活かせるなんて面白そう。お互いにデータを共有せずに訓練できるって、プライバシー保護にもなるしね！

**Comment:** 9 pages, 3 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CL, cs.DC, **投稿日時:** 2024-07-01 04:13

- - -

### [FedEx: Expediting Federated Learning over Heterogeneous Mobile Devices by Overlapping and Participant Selection](http://arxiv.org/abs/2407.00943)

**FedEx：異種モバイルデバイスにおける重複処理と参加者選択による連合学習の迅速化**

Jiaxiang Geng, Boyu Li, Xiaoqi Qin, Yixuan Li, Liang Li, Yanzhao Hou, Miao Pan

- 異種モバイルデバイスでの連合学習（FL）のトレーニング遅延を減少させる新手法を提案
- 重複処理によりメモリ消費を抑えつつ、参加者選択（PS）デザインと互換性を持たせる
- PSの有用性を重複処理による遅延減少を考慮して評価し、ストラグラー問題を解決する包括的なPSソリューションを提供
- 実験結果により、従来の設計と比較して、異種モバイルデバイスでのFLトレーニング遅延を大幅に削減しつつメモリコストを限定的に保つことを示す

重複処理と参加者選択の組み合わせで、効率的な連合学習が可能になりそう！これなら大量のデータを扱うアプリでも、もっとサクサク動くようになるかもね。

**Comment:** 21 pages, 10 figures, Submitted to Sensys2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-01 03:52

- - -

### [SecureSpectra: Safeguarding Digital Identity from Deep Fake Threats via Intelligent Signatures](http://arxiv.org/abs/2407.00913)

**SecureSpectra: インテリジェントシグネチャーによるディープフェイク脅威からのデジタルアイデンティティ保護**

Oguzhan Baser, Kaan Kale, Sandeep P. Chinchali

- DFオーディオモデルの進歩が、音声認証システムに重大な脅威をもたらし、不正アクセスや偽情報の拡散を引き起こす
- DF脅威に対処するために、オーディオに直交的かつ不可逆のシグネチャーを埋め込む防御メカニズム「SecureSpectra」を提案
- 差分プライバシーを統合し、シグネチャーのリバースエンジニアリングを防ぎつつ、セキュリティ強化とパフォーマンス低下の最小化を両立
- Mozilla Common Voice、LibriSpeech、VoxCelebデータセットでの評価で、最先端技術に比べて検出精度が最大71%向上することを実証

ディープフェイク対策として革新的！これ、研究者コミュニティのスタンダードになる予感♡

**Comment:** 5 pages, 4 figures, Proc. INTERSPEECH 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, cs.SD, eess.AS, **投稿日時:** 2024-07-01 02:36

- - -

### [Privacy-First Crowdsourcing: Blockchain and Local Differential Privacy in Crowdsourced Drone Services](http://arxiv.org/abs/2407.00873)

**プライバシー重視のクラウドソーシング: クラウドソース型ドローンサービスにおけるブロックチェーンとローカル差分プライバシー**

Junaid Akram, Ali Anaissi

- 消費者向けドローンをブッシュファイヤー管理に組み込むプライバシー保護フレームワークを導入
- ローカル差分プライバシーを利用しデータ提供者のプライバシーを保護
- ブロックチェーンに基づく解決策で、公正なデータ交換と責任追跡を実現
- 実証実験により、スケーラビリティと規模の大きいデータ収集シナリオでの可能性を示す

ブッシュファイヤーの管理にドローンとか未来感バッチリだね！プライバシーもしっかり守られてるのがめっちゃ安心できる。

**Comment:** 3 pages, 2 figures, accepted and to be published in the proceedings   of IEEE International Conference on Web Services (ICWS 2024)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-07-01 00:46

- - -

### [DroBoost: An Intelligent Score and Model Boosting Method for Drone Detection](http://arxiv.org/abs/2407.00830)

**DroBoost: ドローン検出のためのインテリジェントなスコアとモデルブースティング手法**

Ogulcan Eryuksel, Kamil Anil Ozfuttu, Fatih Cagatay Akyon, Kadir Sahin, Efe Buyukborekci, Devrim Cavusoglu, Sinan Altinuc

- ドローン検出は、視界条件や画像品質が悪く、背景が複雑で小さな物体が多いため困難である
- 前回の研究ではリアルデータと合成データ、Kalmanトラッカーを使用し検出精度を向上
- 現在の研究で多様なデータセットを使用し、基礎モデルのエラー分析から合成サンプルを選択
- オブジェクト追跡のための高度なスコアリングアルゴリズムを開発し、検出信頼度を向上

高精度なドローン検出技術により安全性が高まりそう！次のコンテストでもっと良い成果が期待できるね💕



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-30 20:49

- - -

### [Characterizing Stereotypical Bias from Privacy-preserving Pre-Training](http://arxiv.org/abs/2407.00764)

**プライバシー保護型事前訓練によるステレオタイプバイアスの特性化**

Stefan Arnold, Rene Gröbner, Annika Schreiner

- 差分プライバシーは埋め込み空間での単語の位置関係を利用して生のテキストに適用される
- プライバシー技術が言語モデルのステレオタイプバイアスに与える影響を調査
- プライバシーが強化されると一般的にバイアスが減少するが、全ての社会領域で一様にバイアスが削減されるわけではない
- バイアスがある言語モデルには診断が必要であることを指摘

バイアスが完全に取り除けないのが意外だよね。でも、これからのテクノロジーの進化でさらに改善されるといいな！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-06-30 16:54

- - -

### [A Whole-Process Certifiably Robust Aggregation Method Against Backdoor Attacks in Federated Learning](http://arxiv.org/abs/2407.00719)

**連合学習におけるバックドア攻撃に対する全プロセス保証された堅牢な集約方法**

Anqi Zhou, Yezheng Liu, Yidong Chai, Hongyi Zhu, Xinyue Ge, Yuanchun Jiang, Meng Wang

- 連合学習(FL)はバックドア攻撃の脅威にさらされており、悪意のあるアクターがトリガーを挿入
- 現存の堅牢な集約方法は、事前(ex-ante)、実行中(ex-durante)、事後(ex-post)の3タイプに分類
- 新提案のWPCRAメソッドは3つのフェーズすべてにおいて堅牢性を向上
- 提案するWGMEアルゴリズムはクライアントの重みを考慮し、幾何学的メディアンを改善

バックドア攻撃をこんなに真剣に考えてるのがすごい。新しいアルゴリズムでどれだけFLが安全になるのか楽しみだよね！

**Comment:** 14 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, cs.LG, **投稿日時:** 2024-06-30 15:00

- - -

### [A Collocation-based Method for Addressing Challenges in Word-level Metric Differential Privacy](http://arxiv.org/abs/2407.00638)

**単語レベル差分プライバシーにおける課題解決のためのコロケーションベース手法**

Stephen Meisenbacher, Maulik Chevli, Florian Matthes

- 従来の単語レベル差分プライバシーアプローチは、意味的な一貫性が失われがちである
- 本研究では単語と文章の間に位置するコロケーションを用いた新たな手法を提案
- n-グラムを摂動することで、意味的に一貫した変動長の文章を生成できるようにした
- 頻出単語群に基づいた埋め込みモデルを構築し、単語とバイグラム、トライグラムの共存を実現

文章の意味が保たれる新しい方法を提案しているのが面白そう！差分プライバシーと意味的な一致をどうやって両立させるのか、もっと知りたくなるね。

**Comment:** 13 pages, 2 figures, 9 tables. Accepted to PrivateNLP 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-30 09:37

- - -

### [DP-MLM: Differentially Private Text Rewriting Using Masked Language Models](http://arxiv.org/abs/2407.00637)

**DP-MLM: マスクされた言語モデルを利用した差分プライベートなテキスト再書き換え**

Stephen Meisenbacher, Maulik Chevli, Juraj Vladika, Florian Matthes

- 差分プライバシーを利用したテキスト再書き換えが、最近注目されている
- 従来の方法はオートレグレッシブモデルに依存し、文脈を考慮したプライバシー処理が不足
- 新たな方法DP-MLMでは、マスクされた言語モデル（MLM）を使用し、意義を維持しつつテキストを変換
- 小さなモデル使用で高い効用保存を実現し、カスタマイズも容易

DP-MLMって、際立った成果ね！これでテキストのプライバシー保護がもっと簡単になるかも。未来のアプリケーションも期待できるよね！

**Comment:** 15 pages, 2 figures, 8 tables. Accepted to ACL 2024 (Findings)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-30 09:31

- - -

### [Privacy-Preserving and Trustworthy Deep Learning for Medical Imaging](http://arxiv.org/abs/2407.00538)

**医療画像のためのプライバシー保護と信頼性の高いディープラーニング**

Kiarash Sedghighadikolaei, Attila A Yavuz

- 医療画像データのプライバシー保護がディープラジオミクスにおいて重要
- 既存のプライバシー強化技術(PET)の分類とハイブリッドなPETの提案
- PETをディープラジオミクスに統合するための技術的知見や課題の分析
- 将来の研究方向性として、PETの強化を目指すチャレンジと解決策を提示

次世代の医療に向けて大事な課題だね！PETの実際の適用がどれくらい進むのか、具体的な事例が見てみたいな。

**Comment:** This work has been submitted to the IEEE for possible publication.   Copyright may be transferred without notice, after which this version may no   longer be accessible

**トピック:** [PETs](pets), **カテゴリ:** cs.CR, cs.AI, cs.CV, eess.IV, **投稿日時:** 2024-06-29 22:26

- - -

### [Detecting and Identifying Selection Structure in Sequential Data](http://arxiv.org/abs/2407.00529)

**逐次データにおける選択構造の検出と識別**

Yujia Zheng, Zeyu Tang, Yiwen Qiu, Bernhard Schölkopf, Kun Zhang

- 実際の状況でしばしば行われるデータ点の選択的包含が、統計解析を歪める
- 選択バイアスを単なる誤りと見るのではなく、生成プロセスの深い洞察を提供する機会と捉える
- 選択構造は、パラメトリック仮定や介入実験なしで同定可能であることを示す
- 潜在的な混乱変数が存在する場合でも、適切な構造条件下で非パラメトリックな同定可能性を確立

選択構造って、なんだかデータの裏側を解き明かす探偵みたいだよね！音楽データにも応用できるなんて、それってすごく未来的でワクワクするなぁ。

**Comment:** ICML 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.SD, eess.AS, math.ST, stat.ML, stat.TH, **投稿日時:** 2024-06-29 20:56

- - -

### [MH-pFLGB: Model Heterogeneous personalized Federated Learning via Global Bypass for Medical Image Analysis](http://arxiv.org/abs/2407.00474)

**MH-pFLGB: メディカルイメージ解析のためのグローバルバイパスを用いたモデル多様な個人化連合学習**

Luyuan Xie, Manqing Lin, ChenMing Xu, Tianyu Luan, Zhipeng Zeng, Wenjun Qian, Cong Li, Yuejian Fang, Qingni Shen, Zhonghai Wu

- 医療用人工知能におけるプライバシー保護に連合学習が重要
- 医療機関間の統計的およびシステム的異質性が課題
- グローバルバイパス戦略を使用し、公的データセットへの依存を軽減
- ローカルおよびグローバルな特徴を融合することで性能を向上

医療データでこんなに工夫されてるんだね！みんなで協力してもっと良いAIが作れる未来が楽しみだな。

**Comment:** arXiv admin note: text overlap with arXiv:2405.06822

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-29 15:38

- - -

### [pFLFE: Cross-silo Personalized Federated Learning via Feature Enhancement on Medical Image Segmentation](http://arxiv.org/abs/2407.00462)

**医療画像セグメンテーションにおける特徴強調を用いたシロ間パーソナライズド連合学習 (pFLFE)**

Luyuan Xie, Manqing Lin, Siyuan Liu, ChenMing Xu, Tianyu Luan, Cong Li, Yuejian Fang, Qingni Shen, Zhonghai Wu

- 医療画像セグメンテーションで、データ不足やプライバシー問題を解決するためにシロ間パーソナライズド連合学習が人気
- 既存手法はクライアントドリフトにより一貫性がなく、訓練が遅延する問題あり
- pFLFEは特徴強調と教師あり学習の二段階でこれらの課題を解決する新しいフレームワークを提案
- 少ない通信ラウンドでセグメンテーション品質を維持しつつ、限られた通信リソースでの訓練を実現

これってめっちゃ画期的じゃない？pFLFEがもし普及したら、もっと効果的に医療データ活用できそうでワクワクするね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-06-29 15:20

- - -

### [Obtaining -differential privacy guarantees when using a Poisson mechanism to synthesize contingency tables](http://arxiv.org/abs/2407.00417)

**ポアソンメカニズムを用いたクロス集計表の合成時における$(ε,δ)$-差分プライバシー保証の取得**

James Jackson, Robin Mitra, Brian Francis, Iain Dove

- ポアソン合成メカニズムを用いることで、クロス集計表のカウント保護に差分プライバシー保証を提供できる
- ポアソン分布の累積分布関数を利用することで、$(\epsilon, \delta)$-確率的差分プライバシー保証を取得する方法を示す
- 実証実験を通じて、行政タイプの機密データベースを合成することでこれを実証
- この手法により、ポアソン分布を利用した実際のデータセットでのプライバシー保証が可能

ポアソン分布を使ってプライバシーが守れるなんて面白い！これからもっと安全なデータ解析ができるようになりそうだね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, stat.ME, **投稿日時:** 2024-06-29 11:57

- - -

### [Iterative Data Augmentation with Large Language Models for Aspect-based Sentiment Analysis](http://arxiv.org/abs/2407.00341)

**大規模言語モデルを用いた反復データ拡張によるアスペクトベース感情分析**

Haiyun Li, Qihuang Zhong, Ke Zhu, Juhua Liu, Bo Du, Dacheng Tao

- ABSAはセンテンス内の特定アスペクトに対する感情の方向性を決定するタスクである
- 現在のデータ拡張手法には、流暢さ・一貫性の不足、多様性の欠如などの問題がある
- 提案手法IterDはLLMを利用し、未監督データから流暢で多様な合成ラベルデータを生成する
- 4つのABSAベンチマークで著しい性能向上を確認、手動アノテーションデータとほぼ同等以上の性能を達成

大規模言語モデルを活用してデータ合成するなんて、すごく未来志向だよね！ABSAがさらに効果的に機能するなら、もっと楽しい分析ができそう🎉

**Comment:** Work in process

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-29 07:00

- - -

### [Mind the Gap: Analyzing Lacunae with Transformer-Based Transcription](http://arxiv.org/abs/2407.00250)

**ギャップに注意：トランスフォーマーベースの転写を用いた欠損分析**

Jaydeep Borkar, David A. Smith

- 歴史的文書の損傷やインク問題などで欠損部分が生じる
- 合成データを用いて訓練したトランスフォーマーOCRモデルの有効性を実証
- 欠損部分の検出と修復成功率は65%で、従来モデルの5%を大きく上回る
- 複雑な書体やインク問題などのエラー識別能力が学者にとって有用

歴史を感じる文書の修復ってロマンがあるよね！未来にはもっとこういう技術が進化して、昔の記録がもっと詳しく読めるようになるかも！

**Comment:** Accepted to ICDAR 2024 Workshop on Computational Paleography

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, **投稿日時:** 2024-06-28 22:52

- - -

### [Towards Secure and Efficient Data Scheduling for Vehicular Social Networks](http://arxiv.org/abs/2407.00141)

**車両ソーシャルネットワークにおけるセキュアで効率的なデータスケジューリングを目指して**

Youhua Xia, Tiehua Zhang, Jiong Jin, Ying He, Fei Yu

- 車両環境内で効率的なデータ伝送スケジューリングは高いモビリティのため困難
- 本論文は、効率とセキュリティを優先する新しい学習ベースのスケジューリングアルゴリズムを紹介
- データ処理能力を強化するために特定のニューラルネットワークを使用し、Q学習で情報交換を最適化
- 比較実験により、提案されたスケジューリングアルゴリズムが既存のアルゴリズムより優れていることが示された

この研究、特にQ学習を使った効率性の向上が未来の車両ネットワークを大きく変える可能性があるね！差分プライバシーでセキュリティも強化されている点が安心だよー。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-28 15:20

- - -

### [Generative AI for Synthetic Data Across Multiple Medical Modalities: A Systematic Review of Recent Developments and Challenges](http://arxiv.org/abs/2407.00116)

**複数の医療モダリティにおける合成データ向け生成AIの最新進展と課題に関する系統的レビュー**

Mahmoud Ibrahim, Yasmina Al Khalil, Sina Amirrajab, Chang Sun, Marcel Breeuwer, Josien Pluim, Bart Elen, Gokhan Ertaylan, Michel Dumontier

- 医療データの合成には様々な生成モデル（GAN、VAE、DM、LLM）が使用される
- 最新の研究動向を2021年1月から2023年11月までの間でデータベース（Scopus、PubMed、ArXiv）から調査
- 合成データは臨床的に有効で、多様な臨床ニーズに対応できる可能性がある
- 医療データ用の標準化評価手法の欠如が臨床応用の障害となっており、より深化した評価アプローチの必要性が強調される

最新の技術がこんなに使われてるんだね！個別化アプローチの重要性とか、どのように進化していくのかワクワクするよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-27 14:00

- - -

### [Personalized Federated Continual Learning via Multi-granularity Prompt](http://arxiv.org/abs/2407.00113)

**マルチ粒度プロンプトによるパーソナライズド連合継続学習**

Hao Yu, Xin Yang, Xin Gao, Yan Kang, Hao Wang, Junbo Zhang, Tianrui Li

- PFCLは知識の共有と個別化の課題を解決するシナリオである
- 既存手法は知識の多粒度表現を見落としており、STCF克服に役立つ
- 粗粒度なグローバルプロンプトと細粒度なローカルプロンプトを提案
- 粗粒度プロンプトは空間忘却防止、細粒度プロンプトは時間忘却防止に効果的

個別化された知識を効果的に共有するアイデアが面白そう！これって未来のAI学習法の基盤になるかもね。高校生の私たちでもすぐに使えるといいな。

**Comment:** Accepted by KDD 2024 Research Track

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-27 13:41
