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

更新: 2024-05-28T04:22:21.424710

- - -

### [Federating Dynamic Models using Early-Exit Architectures for Automatic Speech Recognition on Heterogeneous Clients](http://arxiv.org/abs/2405.17376)

**異種クライアントにおける自動音声認識のための早期退出アーキテクチャを用いた動的モデルの連合**

Mohamed Nabih Ali, Alessio Brutti, Daniele Falavigna

- 自動音声認識モデルの訓練には大量の音声記録が必要であり、データ収集にプライバシーの懸念がある。
- 連合学習を用いて複数クライアントでデータをローカルのまま共有モデルを学習することが可能である。
- クライアントデバイスの計算・通信資源が限られており、単一モデルの生成は最適でない。
- 効率的なアーキテクチャとして早期退出ソリューションを用いた動的モデルを提案し、様々なデバイスで利用可能であることを実証。

早期退出するモデルとか、なんかキャッチーな感じがして良いね！色々なデバイスで一つのモデルが使えちゃうなんて、未来の技術って感じがするなぁ。

**Comment:** The paper is under review in Future Generation Computer Systems   Journal

**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, **投稿日時:** 2024-05-27 17:32

- - -

### [Conditioning on Time is All You Need for Synthetic Survival Data Generation](http://arxiv.org/abs/2405.17333)

**時間に基づく条件付けが合成生存データ生成の鍵**

Mohd Ashhad, Ricardo Henao

- 生存データ生成の大きな障害は検閲（イベントの正確なタイミングが不明）
- 提案方法は、イベント時間に基づく共変量生成で既存の生成モデルを再利用可能
- 実データセットを用いた実験で提案手法が従来手法を上回る結果を示す
- 合成生存データで訓練された下流の生存モデルの性能が向上

時間に基づく条件付けで生存データが正確に生成できるなんて、シンプルで効果的！実データと比肩する合成データの性能向上が期待できるね。



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-05-27 16:34

- - -

### [Leveraging Offline Data in Linear Latent Bandits](http://arxiv.org/abs/2405.17324)

**線形潜在バンディットにおけるオフラインデータの活用**

Chinmaya Kausik, Kevin Tan, Ambuj Tewari

- 潜在バンディットは未観測の潜在状態が軌跡のモデルを決定するフレームワーク
- オフラインデータを使用して各潜在状態の複雑なモデルを学習し、オンラインで最適に行動
- 潜在空間を短いオフライントラジェクトリから学習するためのSOLDという新しい方法を提案
- LOCAL-UCBとProBALL-UCBの2つのオンライン活用方法を提示し、実験で効果を実証

この研究、潜在状態使って精度上げるの面白い！オンラインとオフラインのデータ融合って未来感あるよね。

**Comment:** 40 pages. 14 pages for main paper, 26 pages for references + appendix

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, stat.ML, **投稿日時:** 2024-05-27 16:23

- - -

### [All-day Depth Completion](http://arxiv.org/abs/2405.17315)

**全天候深度補完**

Vadim Ezhov, Hyoungseob Park, Zhaoyang Zhang, Rishi Upadhyay, Howard Zhang, Chethan Chinder Chandrappa, Achuta Kadambi, Yunhao Ba, Julie Dorsey, Alex Wong

- 異なる照明条件（昼夜）の下で深度推定を行う新しい方法を提案
- LiDARからの同期されたスパースポイントクラウドを用いてカメラ画像と融合
- 合成データを活用して、不確実性を伴うスパースから粗い密度深度マップへのマッピングを学習
- 提案手法は、ベースラインと比較して全天候で平均11.65%の改善を達成

合成データを使って深度推定の限界を突破するなんてすごいよね！ナイトモードの性能もあがるから、夜の運転支援にも役立ちそうだよ。

**Comment:** 8 pages, 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-27 16:16

- - -

### [FedHPL: Efficient Heterogeneous Federated Learning with Prompt Tuning and Logit Distillation](http://arxiv.org/abs/2405.17267)

**FedHPL: プロンプトチューニングとロジット蒸留による効率的な異種連合学習**

Yuting Ma, Lechao Cheng, Yaxiong Wang, Zhun Zhong, Xiaohua Xu, Meng Wang

- 連合学習はデータをローカルに保持しつつモデルを協調訓練するプライバシー保護パラダイム
- 異なるモデル構造やデータ分布、限られたリソースでの性能低下や収束速度の遅れが発生
- FedHPLはプロンプトチューニングとロジット蒸留を基にした統一的連合学習フレームワークを提案
- 実験で既存手法を上回る性能と少ない計算負荷、訓練ラウンドで効率的であることを確認

プロンプトチューニングとロジット蒸留が鍵になってるみたい！効率的にモデルを強化する方法が気になるね。😊

**Comment:** 35 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-05-27 15:25

- - -

### [: towards data-free Transferable Parameter Efficient Finetuning](http://arxiv.org/abs/2405.17258)

**データフリーで転送可能なパラメータ効率の良いファインチューニングに向けたTrans-LoRA**

Runqian Wang, Soumya Ghosh, David Cox, Diego Antognini, Aude Oliva, Rogerio Feris, Leonid Karlinsky

- LoRAは少ない追加パラメータでフルモデルに近いパフォーマンスを発揮するPEFT技術
- ベースモデルが変更されるとLoRAモジュールも再トレーニングが必要
- Trans-LoRAは合成データを使い、LoRAモジュールのデータフリー転送を提案
- LLamaとGemmaモデルを用いて、異なるモデル間での効果的なLoRA転送を示す

合成データでのモデル転送とか、めっちゃ未来感あるよね！どんな実用例が出てくるのか楽しみだな〜！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-27 15:15

- - -

### [LabObf: A Label Protection Scheme for Vertical Federated Learning Through Label Obfuscation](http://arxiv.org/abs/2405.17042)

**LabObf: ラベルあいまい化による垂直連合学習のためのラベル保護スキーム**

Ying He, Mingyang Niu, Jingyu Hua, Yunlong Mao, Xu Huang, Chen Li, Sheng Zhong

- 垂直連合学習におけるスプリット学習は、プライバシー保護特性のため広く利用されている
- 悪意ある参加者がアップロードされた埋め込みベクトルからラベル情報を推測し、プライバシー漏洩が懸念される
- Embedding Extension Attackを提案し、現行防御戦略を無力化する手法を扱う
- ラベルのあいまい化防御戦略「LabObf」を提案し、攻撃者の成功率をランダム推測レベルまで低減する

この研究、攻撃と防御のせめぎ合いが面白いよね！LabObfの防御戦略が今後どこまで実用化されるか興味津々だな～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-27 10:54

- - -

### [SCaRL- A Synthetic Multi-Modal Dataset for Autonomous Driving](http://arxiv.org/abs/2405.17030)

**SCaRL - 自動運転のための合成マルチモーダルデータセット**

Avinash Nittur Ramesh, Aitor Correas-Serrano, María González-Huici

- SCaRLは、自動運転ソリューションの訓練と検証を可能にする合成生成された新しいマルチモーダルデータセットである
- 既存のデータセットは完全なセンサースイートからの同期データ収集が不足しているが、SCaRLはそれを解決する
- SCaRLはRGB、セマンティック/インスタンス、深度カメラ、レーダー、LiDARからの同期データを提供する
- SCaRLは多様で動的なシナリオと交通条件を含む大量データを提供し、一部のリンクからアクセス可能である

このデータセット、未来の自動運転技術に大きな影響を与えそうだよね。シミュレーション用のデータがこんなに充実してるってすごい！

**Comment:** Accepted in International Conference on Microwaves for Intelligent   Mobility - 16.&17. April 2024 - Boppard near Koblenz, Germany

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-05-27 10:31

- - -

### [A Correlation- and Mean-Aware Loss Function and Benchmarking Framework to Improve GAN-based Tabular Data Synthesis](http://arxiv.org/abs/2405.16971)

**相関と平均を考慮した損失関数とGANベースの表形式データ合成のベンチマークフレームワーク**

Minh H. Vu, Daniel Edler, Carl Wibom, Tommy Löfstedt, Beatrice Melin, Martin Rosvall

- 医療データの共有を促進するために、合成データが重要だが、既存のGANは実データの複雑さを再現するのが難しい
- 連続値とカテゴリ変数を含むデータの相関や均衡を考慮した新たな損失関数を提案
- 10個の実データセットと8つの既存GANを用いて、新損失関数のベンチマークを行った
- 提案手法は下流の機械学習タスクで性能向上を示し、データ共有を容易にすることが期待できる

GANがデータの複雑な相関をもっと上手に捉えられるようになるなんて、すごくおもしろそう！これからデータサイエンスの分野がもっと進化しそうだね。

**Comment:** n.a

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-27 09:08

- - -

### [From Obstacle to Opportunity: Enhancing Semi-supervised Learning with Synthetic Data](http://arxiv.org/abs/2405.16930)

**障害から機会へ：合成データで半教師あり学習の強化**

Zerun Wang, Jiafeng Mao, Liuyu Xiang, Toshihiko Yamasaki

- 現在の半教師あり学習（SSL）は合成データをうまく活用できず、時には悪影響を受ける
- 合成データによる問題を分析し、新しいSSL法「RSMatch」を提案
- 実験結果から、RSMatchは未ラベルの画像内の合成データを有効に利用し、SSLパフォーマンスを向上
- アブレーションスタディや可視化でRSMatchの有効性をさらに確認

合成データをうまく使える方法とか未来っぽくて素敵！実際にどれだけ性能が上がるのか気になるなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-27 08:24

- - -

### [Demystifying amortized causal discovery with transformers](http://arxiv.org/abs/2405.16924)

**トランスフォーマーを用いた平準化因果発見の解明**

Francesco Montagna, Max Cairney-Leeming, Dhanya Sridhar, Francesco Locatello

- CSIvAは、合成データで訓練し実データに転移するトランスフォーマーモデルである
- トレーニングデータの分布制約がテスト観察の事前情報を暗黙に定義している
- 識別可能な因果モデルのクラスから生成されたデータセットでの訓練がテストの汎化性能を改善
- 平準化因果発見は古典的方法に従う必要がある一方で、仮定の定式化には違いがある

トランスフォーマーを使った因果発見がもっとこれから進化していくみたいで、おもしろそう！合成データから実データへの転移がどれだけうまくいくのか気になるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-05-27 08:17

- - -

### [Oblivious Monitoring for Discrete-Time STL via Fully Homomorphic Encryption](http://arxiv.org/abs/2405.16767)

**準同型暗号を用いた離散時間STLのオブリビアスモニタリング**

Masaki Waga, Kotaro Matsuoka, Takashi Suwa, Naoki Matsumoto, Ryotaro Banno, Song Bian, Kohei Suenaga

- サイバーフィジカルシステムの遠隔モニタリング時に、データの秘匿性を維持する必要がある
- 既存のオンラインLTLモニタリングプロトコルに対し、暗号化された値の算術操作を可能にする
- CKKSとTFHEの2つのFHEスキームを組み合わせ、算術述語とDFA処理を最適化
- 血糖値と車両の挙動モニタリングのケーススタディを実施し、プロトコルの実用性を示す結果を得た

この研究、めっちゃ未来っぽくない？データをバッチリ守りながらモニタリングできるんだって、すごいね！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.FL, **投稿日時:** 2024-05-27 02:32

- - -

### [Faster Sampling via Stochastic Gradient Proximal Sampler](http://arxiv.org/abs/2405.16734)

**確率的勾配近接サンプラーによる高速サンプリング**

Xunpeng Huang, Difan Zou, Yi-An Ma, Hanze Dong, Tong Zhang

- 確率的勾配がラングヴァン系手法に組み込まれ、大規模サンプリング問題の効率を向上
- 決定論的設定でラングヴァンより高速収束する近接サンプラーの確率的変種を研究
- SPSの一般的なフレームワークと収束理論を確立し、SPS-SGLDとSPS-MALAを提案
- エラー率と勾配複雑性で既存の手法より優れた結果を得て、実証的研究で性能を確認

確率的近接サンプラーって面白そう！効率がすごく改善されてるみたいだから、実用化が進むといいな。特にデータが多い場合に役立ちそう。

**Comment:** 48 pages, 2 figures, 5 tables

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-05-27 00:53

- - -

### [Alistair: Efficient On-device Budgeting for Differentially-Private Ad-Measurement Systems](http://arxiv.org/abs/2405.16719)

**Alistair：差分プライバシー広告測定システムの効率的なデバイス予算管理**

Pierre Tholoniat, Kelly Kostopoulou, Peter McNeely, Prabhpreet Singh Sodhi, Anirudh Varanasi, Benjamin Case, Asaf Cidon, Roxana Geambasu, Mathias Lécuyer

- サードパーティのクッキーが主要ブラウザから削除されるため、新しいプライバシー保護広告APIの導入が進む
- Google、Apple、Meta、Mozillaの既存のプライバシー保護広告測定APIを強化
- Alistairというアプローチで、差分プライバシーの予算管理をより効率的にし、個別のDP保証を提供
- ChromeにAlistairを組み込み、ミクロベンチマークと広告データセットで評価し、基準よりも多くの広告測定を可能に

今の広告のプライバシー問題を解決できたら、新しいビジネスが生まれそう！こういう革新があると、未来のテクノロジーはもっと安全で面白くなりそうだね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-26 23:27

- - -

### [Amortized Active Causal Induction with Deep Reinforcement Learning](http://arxiv.org/abs/2405.16718)

**ディープ強化学習を用いた費用分散型因果帰納学習**

Yashas Annadani, Panagiotis Tigas, Stefan Bauer, Adam Foster

- CAASLはリアルタイムかつ適応的に介入を選択でき、確率のアクセスを必要としない
- トランスフォーマーベースのネットワークは、設計環境のシミュレータで強化学習を通じて訓練される
- 合成データと単一細胞遺伝子発現シミュレータで、他の戦略よりも因果グラフの推定が向上することを実証した
- 訓練環境の分布に対して費用分散型の介入設計を達成しつつ、テスト環境の分布変動に対しても一般化が可能

因果推論において強化学習がどんな風に活躍するのかすっごくおもしろそう！実際の遺伝子発現データにも応用できるのかな、未来の科学ってドキドキするよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-26 23:14

- - -

### [Visualizing the Shadows: Unveiling Data Poisoning Behaviors in Federated Learning](http://arxiv.org/abs/2405.16707)

**影を可視化する：連合学習におけるデータポイズニング行動の解明**

Xueqing Zhang, Junkai Zhang, Ka-Ho Chow, Juntao Chen, Ying Mao, Mohamed Rahouti, Xiang Li, Yuchen Liu, Wenqi Wei

- 連合学習システムは、ターゲットを絞ったデータポイズニング攻撃に対して脆弱である
- ラベル反転を用いたデータポイズニング攻撃をシミュレーションし、モデル性能への影響を分析
- 五つのコンポーネントで構成されるシステムを使用し、攻撃の可視化と対策を実施
- ラベル操作、攻撃タイミング、悪意ある攻撃の可用性からの観察で、システムの脆弱性を理解

連合学習に対する攻撃の可視化って、実際にどうやって見える化するのか興味津々！未来のセキュリティ対策に役立ちそう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-26 21:58

- - -

### [A Systematic Review of Federated Generative Models](http://arxiv.org/abs/2405.16682)

**連合生成モデルの体系的レビュー**

Ashkan Vedadi Gargary, Emiliano De Cristofaro

- 連合学習（FL）と生成モデルを組み合わせることで分散システムでデータを共有せずにモデル訓練が可能
- FLと生成モデルの組み合わせは攻撃に脆弱で、最適なアーキテクチャの設計が困難
- 2019年から2024年にかけての約100本の論文を体系的に比較し、FLと生成モデルの手法、およびプライバシー考慮の点に焦点
- 最先端の進展を強調し、未解決の課題を特定することで、新参者にも理解しやすく今後の研究に洞察を提供

連合学習と生成モデルの融合って、新たなプライバシー技術の未来が見えそう！どんな技術が出てくるのかワクワクするね。

**Comment:** 24 Pages, 3 Figures, 5 Tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CL, cs.CR, **投稿日時:** 2024-05-26 20:20

- - -

### [Fair Federated Learning under Domain Skew with Local Consistency and Domain Diversity](http://arxiv.org/abs/2405.16585)

**異なるドメインにおける局所的一貫性とドメイン多様性を考慮した公平な連合学習**

Yuhang Chen, Wenke Huang, Mang Ye

- ドメインスキュー下での連合学習（FL）は偏りがあり、公平性の問題が二つある
- パラメータアップデートの矛盾があり、不一致なアップデート方向が発生
- モデルの集約バイアスがあり、不公平な重み配分とドメイン多様性の無視が問題
- 提案手法は不要なパラメータアップデートを選択的に破棄し、公平な集約目標を設定

この研究、実践的なリアルな問題を解決しようとしてて、けっこうおもしろい！公平性を保つための工夫、現場にどう役立つか気になる〜。

**Comment:** Accepted by CVPR2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-26 14:29

- - -

### [Memory-efficient High-resolution OCT Volume Synthesis with Cascaded Amortized Latent Diffusion Models](http://arxiv.org/abs/2405.16516)

**メモリ効率の高い高解像度OCTボリューム合成：カスケード型アンモータイズド潜在拡散モデル**

Kun Huang, Xiao Ma, Yuhan Zhang, Na Su, Songtao Yuan, Yong Liu, Qiang Chen, Huazhu Fu

- 眼科領域で重要なOCT画像解析は大規模データセットが必要であるが、一部のタスクで入手が困難
- 深層生成モデルを用いたリアルなデータ作成が有望だが、高解像度OCTボリュームの合成はハードウェア資源の制約が問題
- 提案したCA-LDMは、非ホリスティックオートエンコーダを用いて高解像度ボリューム空間と低解像度潜在空間の双方向マッピングを実現
- 公開データセットでの実験により、既存手法を上回るリアルな高解像度データを生成し、微細なセグメンテーションタスクでも性能向上を確認

高解像度のOCT画像をメモリ効率よく生成するなんてスゴイね！医療画像の解析がもっと簡単に正確にできるようになりそうで、未来が楽しみ♡

**Comment:** Provisionally accepted for medical image computing and   computer-assisted intervention (MICCAI) 2024

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-05-26 10:58

- - -

### [Differentiable Proximal Graph Matching](http://arxiv.org/abs/2405.16479)

**微分可能な近接グラフマッチング**

Haoru Tan, Chuang Wang, Xu-Yao Zhang, Cheng-Lin Liu

- グラフマッチングを近接作用素に基づいてリラックスし、凸最適化問題の連続として分解
- 提案手法はグラフの親和性行列からノード対応予測への微分可能な写像として機能
- エンドツーエンドのディープラーニングフレームワークに統合し、特徴表現と親和性行列を同時学習
- 提案手法が安定点に収束する理論的保証を提供し、既存アルゴリズムを様々なデータセットで上回る

これめっちゃ面白そう！特にディープラーニングと統合できるところが未来的だよね。こんな技術がもっと広がったら、もっと便利なアプリが出てきそうでワクワクするよ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-26 08:17

- - -

### [KiNETGAN: Enabling Distributed Network Intrusion Detection through Knowledge-Infused Synthetic Data Generation](http://arxiv.org/abs/2405.16476)

**KiNETGAN: 知識を活用した合成データ生成による分散型ネットワーク侵入検知の実現**

Anantaa Kotal, Brandon Luton, Anupam Joshi

- IoT/CPSシステムにおける伝統的な侵入検知方法では、ネットワークトラフィックの分析が必要であり、プライバシーの問題がある
- 合成データはデータプライバシーを保護しながら、リアルなネットワーク行動を模倣する可能性がある
- Generative Adversarial Networks (GANs)は合成データを生成するが、有限なトレーニングデータで現実的なデータ生成が難しい
- 提案されたKiNETGANは、知識を取り入れたGANでリアルなネットワーク活動データを生成し、プライバシーとユーティリティのバランスを確保している

知識を取り入れたGANがどれだけリアルなデータを作るのか、ワクワクするね！IoT環境でのセキュリティ向上、すごく気になる～✨



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-05-26 08:02

- - -

### [Multi-Level Additive Modeling for Structured Non-IID Federated Learning](http://arxiv.org/abs/2405.16472)

**非独立同分布な連合学習のための多層加法モデリング**

Shutong Chen, Tianyi Zhou, Guodong Long, Jie Ma, Jing Jiang, Chengqi Zhang

- 連合学習の主要な課題は、クライアント間の非独立同分布（Non-IID）をモデル化すること
- 非IIDに対応するため、マルチレベル加法モデル（MAM）を用いて知識共有を改善
- 各クライアントは任意のレベルの1つのモデルに割り当てられ、個別の予測はモデルの出力を統合して算出
- FeMAMは既存のクラスタFLおよび個別FL手法を上回り、非IID環境で優れた性能を発揮することを実証

異なるクライアント間での知識共有を効率化するなんて、面白そう！普遍的なモデルと個別モデルを組み合わせるアプローチにワクワクするなぁ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-26 07:54

- - -

### [Machine learning in business process management: A systematic literature review](http://arxiv.org/abs/2405.16396)

**ビジネスプロセスマネジメントにおける機械学習: 系統的文献レビュー**

Sven Weinzierl, Sandra Zilker, Sebastian Dunzer, Martin Matzner

- 機械学習はプログラムを明示的にコーディングせずにデータに基づいて作成するアルゴリズムを提供
- BPMにおける機械学習の用途は、意思決定支援、正確なプロセスモデルの発見、リソース配分の改善に多様
- 研究はBPMタスクをプロセスのライフサイクルのフェーズごとに整理し、機械学習がそのタスクにどう寄与するかを解説
- 結論として、今後の研究の方向性や新しい機械学習概念の適用に関する研究アジェンダを提供

機械学習とビジネスプロセスを一緒にするなんて、超面白そうじゃない！？今後の研究の方向性も提示されてて、革新的なアイデアが次々に生まれそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-26 01:12

- - -

### [Federated Unsupervised Domain Generalization using Global and Local Alignment of Gradients](http://arxiv.org/abs/2405.16304)

**連合学習を用いた教師なしドメイン一般化のための全球および局所の勾配整合**

Farhad Pourpanah, Mahdiyar Molahasani, Milad Soltany, Michael Greenspan, Ali Etemad

- 連合学習におけるドメインシフトと勾配整合の関連性を理論的に確立
- 新手法「FedGaLA」を提案し、クライアントとサーバーでの勾配整合を実施
- PACS、OfficeHome、DomainNet、TerraIncのデータセットで実験し、手法の有効性を検証
- 各コンポーネントとパラメータの影響を調査するためのアブレーション研究と感度分析を実施

勾配整合で新しいドメインに対応できるモデルを作るのすごいね！これって色んなデータセットで試してみてもうまくいくってことなら、めっちゃ注目されそう♪

**Comment:** 23 pages, 4 figure

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-25 17:12

- - -

### [Generation of synthetic data using breast cancer dataset and classification with resnet18](http://arxiv.org/abs/2405.16286)

**乳がんデータセットを用いた合成データ生成とResNet18による分類**

Dilsat Berin Aytar, Semra Gunduc

- 現代の情報社会ではデータが重要な資源であり、収集・管理・分析が成功の鍵
- 合成データは、実データの制約やラベル付けデータ収集の費用、プライバシー問題などに対処するために必要
- 病理学データセットを用いてMSG-GANで悪性と非悪性の合成画像を生成し、がん識別を支援
- 生成された合成データと実データをResNet18モデルで分類し、合成画像が実データと同様の機能を示すか調査

合成データが実際の医療データの代わりになるなら、患者情報のプライバシーを守りながら研究が進むよね。未来の医療技術の発展に期待大かも！

**Comment:** 17 pages, 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-25 15:53

- - -

### [FastQuery: Communication-efficient Embedding Table Query for Private LLM Inference](http://arxiv.org/abs/2405.16241)

**FastQuery: 秘密LLM推論のための通信効率の良い埋め込みテーブルクエリ**

Chenqi Lin, Tianshi Xu, Zebin Yang, Runsheng Wang, Ru Huang, Meng Li

- 大規模言語モデル(LLMs)の進化に伴い、ユーザークエリには機密情報が含まれる可能性がありプライバシーの懸念がある
- 準同型暗号(HE)に基づくプライベート推論が提案されているが、埋め込みテーブルクエリはHEベースの行列ベクトル乗算問題となり計算と通信の負担が大きい
- そこで、通信対応の埋め込みテーブル量子化アルゴリズムと1ホット対応の密集パッキングアルゴリズムを特徴とする最適化フレームワークFastQueryを提案した
- FastQueryは、先行研究のHEベースフレームワーク(Cheetah, Iron, Bumblebee)と比較して、計算遅延が最大4.3倍、通信量が最大75.7倍削減される

FastQueryの効率性を持ってLLMのプライバシー保護も改善だから、実用化が楽しみかも！プライバシーに敏感な時代だし、これは絶対注目だね。

**Comment:** 6 pages, DAC2024

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-05-25 13:58

- - -

### [Analytic Federated Learning](http://arxiv.org/abs/2405.16240)

**解析的連合学習**

Huiping Zhuang, Run He, Kai Tong, Di Fang, Han Sun, Haoran Li, Tianyi Chen, Ziqian Zeng

- AFL（解析的連合学習）は、連合学習に解析的（閉形式）ソリューションを導入する新たなトレーニングパラダイム
- ローカルクライアントのトレーニングステージでは、1エポックでのトレーニングを実現し、多エポック更新不要
- 集約ステージで絶対集約法（AA法）を導出し、単一ラウンドの集約を可能にし、複数ラウンド集約が不要
- データ異質性やクライアント数に影響されず、AFLは競争力を持ちながら絶対収束し、初のハイパーパラメータフリーメソッド

解析的なアプローチで連合学習がどこまで進化するか楽しみね。クライアント数が多くても影響を受けないなんて、本当だったらすごく面白いかも。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-25 13:58

- - -

### [Client2Vec: Improving Federated Learning by Distribution Shifts Aware Client Indexing](http://arxiv.org/abs/2405.16233)

**Client2Vec: 分布シフトに対応したクライアントインデックスによる連合学習の改善**

Yongxin Guo, Lin Wang, Xiaoying Tang, Tao Lin

- 連合学習はプライバシー保護の分散型機械学習だが、クライアント間の大きな分布シフトが課題である
- Client2Vecという機構を導入し、FLトレーニング開始前にクライアントごとの固有のインデックスを生成
- 生成されたクライアントインデックスを利用して、クライアントサンプリング、モデル集約、ローカルトレーニングを改善
- 多様なデータセットとモデルアーキテクチャにおいて、Client2Vecが効率的に機能することを実験で検証

この研究では事前準備としてクライアントインデックスを使うことで、より効率的な学習ができるみたい。クライアントごとの個性を活かすって斬新だよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-25 13:49

- - -

### [An Experimental Study of Different Aggregation Schemes in Semi-Asynchronous Federated Learning](http://arxiv.org/abs/2405.16086)

**半非同期連合学習における異なる集約方式の実験的研究**

Yunbo Li, Jiaping Gui, Yue Wu

- 連合学習は分散環境での高性能計算とデータプライバシーの保護が特徴
- 半非同期連合学習（SAFL）ではリソースの異質性に対応
- FedSGDとFedAvgの2つのモードを比較、前者は精度高く収束が速いが精度の揺れが大きい
- 後者はストラグラー問題に強いが収束遅く、精度が低い

SAFLの特性を理解して使い分けることがキーだね。精度重視か安定性重視か、どっちが大事か考えるのが面白そう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.PF, **投稿日時:** 2024-05-25 06:33

- - -

### [FedSheafHN: Personalized Federated Learning on Graph-structured Data](http://arxiv.org/abs/2405.16056)

**FedSheafHN: グラフ構造データにおけるパーソナライズ連合学習**

Wenfei Liang, Yanan Zhao, Rui She, Yiming Li, Wee Peng Tay

- グラフニューラルネットワーク（GNN）のカスタマイズによりクライアントごとのニーズに対応する
- FedSheafHNは協力グラフ埋め込みと効率的なパーソナルモデル生成を提案
- シーフ拡散を用いてクライアントの特性を学び、複雑なクライアント特徴の統合と解釈を改善
- エンピリカル評価で他の既存手法より優れ、モデル収束が速く新しいクライアントへの対応も効果的

この研究、めっちゃ面白そう！特に複雑なクライアント特性をシーフ拡散で改善するところ、すごく未来的だよね。今後この技術が普及したら、いろんなデータに対応できちゃうかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-25 04:51

- - -

### [Federated Learning for Non-factorizable Models using Deep Generative Prior Approximations](http://arxiv.org/abs/2405.16055)

**非因数分解モデルのための連合学習：深層生成事前分布近似の利用**

Conor Hassan, Joshua J Bon, Elizaveta Semenova, Antonietta Mira, Kerrie Mengersen

- 連合学習（FL）はデータの共有を避けることでプライバシーを保ちながら分散型クライアント間で協調モデルを訓練可能である
- 現在のFL手法はクライアントモデル間の条件付き独立を仮定し、依存を捉える事前分布の使用を制限する
- SIGMA事前分布は深層生成モデルの近似を用いてクライアント間での非因数分解モデルのFLを可能にする
- SIGMA事前分布の有効性は合成データで示され、オーストラリアの空間データFLの実例で実用性が立証された

SIGMA事前分布を使うことで、空間統計や疫学など依存関係をモデル化するのが重要な分野でFLが可能になるんだね。新しい応用分野が広がりそうでワクワクする！

**Comment:** 25 pages, 7 figures, 2 tables

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, stat.CO, stat.ME, **投稿日時:** 2024-05-25 04:44

- - -

### [ComFace: Facial Representation Learning with Synthetic Data for Comparing Faces](http://arxiv.org/abs/2405.16016)

**ComFace: 合成データを用いた顔比較のための顔表現学習**

Yusuke Akamatsu, Terumi Umematsu, Hitoshi Imaoka, Shizuko Gomi, Hideo Tsurushima

- 健康や感情状態と関連した個人内の顔変化の監視は、医療や感情認識分野に有用だが、時系列的な顔画像の収集が困難で未探究
- 合成顔画像を使用して個人内の顔変化を捉える顔表現学習法「ComFace」を提案
- ComFaceは、個人間の顔の違いと個人内の顔変化の2つの特徴表現を習得し、顔比較の3つの下流タスク（表情変化、体重変化、年齢変化）に転用
- 合成データのみで訓練されたComFaceは、実画像を使用した一般的な事前訓練や最新の表現学習方法と同等またはそれ以上の転用性能を実現

これめっちゃ面白そう！リアルな顔画像の収集って大変だけど、合成データだけでこんなに有効なモデルを作れるなんて、将来の医療や感情認識がもっと進化しそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, eess.IV, **投稿日時:** 2024-05-25 02:44

- - -

### [Diversifying Human Pose in Synthetic Data for Aerial-view Human Detection](http://arxiv.org/abs/2405.15939)

**空撮人検出用合成データにおける人体ポーズの多様化**

Yi-Ting Shen, Hyungtae Lee, Heesung Kwon, Shuvra S. Bhattacharyya

- ポーズ生成器を用いて新しいポーズを作成し、既存データセットの画像を変換
- 新しいポーズに対応する画像はトレーニングに含まれないため、類似ポーズのみを適用
- ダイクストラアルゴリズムで近接配置するようにターゲットポーズを選択
- ポーズ多様化した合成データセットを使うことで、少数ショットでの精度が向上

合成データでこんなに精度が上がるなんて、すごく魅力的！実際の空撮技術に応用されたら面白そう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-24 21:08

- - -

### [Achieving Dimension-Free Communication in Federated Learning via Zeroth-Order Optimization](http://arxiv.org/abs/2405.15861)

**連合学習におけるゼロ次最適化を通じた次元依存のない通信の実現**

Zhe Li, Bicheng Ying, Zidong Liu, Haibo Yang

- 連合学習は分散データソース間で協働的かつプライバシー保護型機械学習を提供する
- 大規模モデルでの通信コストが次元に比例し、効率性の大きな障害となっている
- 新しいアルゴリズム「FedDisco」により、各通信ラウンドでスカラー値のみを送信
- 実証結果として、従来の連合学習アプローチと比較して通信オーバーヘッドが大幅に削減される

次元に依存しない通信で連合学習がもっとスムーズになるなんて、すごく未来がラクになりそうだね。FedDiscoの名前もディスコみたいでちょっと楽しい気がする。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-24 18:07
