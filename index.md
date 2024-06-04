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

更新: 2024-06-04T04:18:06.294673

- - -

### [Locking Machine Learning Models into Hardware](http://arxiv.org/abs/2405.20990)

**機械学習モデルをハードウェアにロックする**

Eleanor Clifford, Adhithya Saravanan, Harry Langford, Cheng Zhang, Yiren Zhao, Robert Mullins, Ilia Shumailov, Jamie Hayes

- 機械学習モデルは高価な知的財産であり、企業の競争力はその秘密保持に依存
- 機密計算技術は未熟で広範な導入は難しい
- この研究では、特定のハードウェアでのみ利用可能な機械学習モデルロック機構を提案
- モデルロックにより、モデルの不正使用が難しくなり、オーバーヘッドがほとんどないことを実証

ハードウェアと機械学習モデルのミックス、ちょっと未来感あってワクワクしちゃうね！これで機密保持が簡単になると、どんどん新しい技術も安全に使えちゃうんじゃない？

**Comment:** 10 pages, 2 figures of main text; 14 pages, 16 figures of appendices

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-05-31 16:35

- - -

### [ACE: A Model Poisoning Attack on Contribution Evaluation Methods in Federated Learning](http://arxiv.org/abs/2405.20975)

**ACE: 連合学習における貢献評価方法へのモデルポイズニング攻撃**

Zhangchen Xu, Fengqing Jiang, Luyao Niu, Jinyuan Jia, Bo Li, Radha Poovendran

- 連合学習（FL）は、クライアントがローカルデータを共有せずにグローバルモデルを共同で訓練する手法
- ACE攻撃は、悪意のあるクライアントが自身の貢献を高く評価させるための手法
- 理論的および実証的評価により、ACEが貢献評価方法を効果的に欺くことを示す
- 提案された対策はACEへの効果が不十分であり、新たな防御策の必要性を強調

悪意のあるクライアントがシステムを欺く手法が存在するなんて驚きだよね！これからもっと強力な防御策が開発されるといいな。

**Comment:** To appear in the 33rd USENIX Security Symposium, 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-05-31 16:21

- - -

### [Navigating Tabular Data Synthesis Research: Understanding User Needs and Tool Capabilities](http://arxiv.org/abs/2405.20959)

**タブラー型データ合成研究のナビゲーション: ユーザーのニーズとツールの能力の理解**

Maria F. Davila R., Sven Groen, Fabian Panse, Wolfram Wingerath

- タブラー型データの合成は、欠損値やデータセット不均衡、多様な列タイプなどの独自の複雑な課題がある
- 元のデータセットにおける列相関や時系列依存、整合性制約の保持も求められる
- 36の人気研究ツールの評価を通じて、ユーザーのニーズに適合するツール選択のための決定ガイドを開発
- 決定ガイドにより、特定の用途に適したTDSツールを見つける際の大きな研究ギャップが判明

ユーザーのニーズに応じたデータ合成ツールがいっぱいあるけど、それぞれの特長や限界を見極めるのが鍵だね。未来のデータ駆動型社会に向けて、この研究が大きな一歩になるかも！

**Comment:** 14 pages, 3 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.DB, **投稿日時:** 2024-05-31 16:00

- - -

### [Sheaf HyperNetworks for Personalized Federated Learning](http://arxiv.org/abs/2405.20882)

**連合学習のための層ハイパーネットワーク**

Bao Nguyen, Lorenzo Sani, Xinchi Qiu, Pietro Liò, Nicholas D. Lane

- GHNsはGNNsとHNsを組み合わせたが、過剰平滑化や異種性などの問題がある
- PFLにはGHNsが直接適用できず、あらかじめクライアント関係グラフがない場合が多い
- PFLの文脈で限界を克服するため、セルラー層理論とHNsを組み合わせたSHNsを提案
- SHNsは複雑な非IIDシナリオで精度が最大2.7%、平均二乗誤差が最大5.3%改善

新しいアーキテクチャがどれだけ性能を引き上げるのかワクワクするね！応用先も広くて、交通予測や天気予報にも使えるなら未来が楽しみ！

**Comment:** 25 pages, 12 figures, 7 tables, pre-print under review

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-31 14:55

- - -

### [BackdoorIndicator: Leveraging OOD Data for Proactive Backdoor Detection in Federated Learning](http://arxiv.org/abs/2405.20862)

**BackdoorIndicator: 連合学習におけるバックドア検出のためのOODデータ活用**

Songze Li, Yanbo Dai

- 連合学習システムでは、悪意あるクライアントが毒されたモデルをアップロードしバックドアを植え付ける可能性がある
- 既存のバックドア防御はシステムや攻撃者設定によって性能が不安定である
- BackdoorIndicatorは、サーバがOODデータを用いてバックドアの存在を正確に検出する新たな検出メカニズムを提案する
- 一連の実証実験を通じて、BackdoorIndicatorは既存の防御策に比べ一貫した優れた性能と実用性を示した

バックドア検出のソリューションなんてめっちゃかっこいいじゃん！セキュリティと機械学習両方好きな人にはすごく興味深い内容だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-31 14:44

- - -

### [MegActor: Harness the Power of Raw Video for Vivid Portrait Animation](http://arxiv.org/abs/2405.20851)

**MegActor: 生動画の力を活用した鮮やかなポートレートアニメーション**

Shurong Yang, Huadong Li, Juhao Wu, Minhao Jing, Linze Li, Renhe Ji, Jiajun Liang, Haoqiang Fan

- 生動画は顔の表情情報が豊かだが、ID漏洩と背景の影響が課題
- 合成データ生成フレームワークでID漏洩を軽減し、動作と表現を維持
- 参照画像の前景と背景を分離し、CLIPで背景情報をエンコード
- スタイル転送で顔の詳細な影響を排除し、公的データセットのみでモデルを訓練

これ読んでると、オープンソースの貢献がすごいって思わない? 特に背景をCLIPで安定させる部分なんて、見てみたいな！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-31 14:33

- - -

### [Pursuing Overall Welfare in Federated Learning through Sequential Decision Making](http://arxiv.org/abs/2405.20821)

**連合学習における逐次意思決定による全体的福祉の追求**

Seok-Ju Hahn, Gi-Soo Kim, Junghye Lee

- 単一のグローバルモデルでは全クライアントに対して均等に性能を提供できない
- クライアントごとの公平性を達成するため、適応的な集約方式の導入が必要
- 既存の公平性を考慮した集約戦略はオンライン凸最適化フレームワークで統一できる
- 細分化された新手法AAggFFは既存方法よりもクライアントレベルの公平性が向上

連合学習でクライアントごとの公平性をめちゃ考えてるね。新しいAAggFFがどれだけ実用的か、コード見て試したくなっちゃう♪

**Comment:** Accepted at ICML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, stat.ML, **投稿日時:** 2024-05-31 14:15

- - -

### [Share Your Secrets for Privacy! Confidential Forecasting with Vertical Federated Learning](http://arxiv.org/abs/2405.20761)

**秘密を共有してプライバシーを守ろう！垂直連合学習での機密予測**

Aditya Shankar, Lydia Y. Chen, Jérémie Decouchant, Dimitra Gkorou, Rihan Hai

- 垂直連合学習は、予知保全と機械制御などの産業用時系列予測に有望
- データプライバシーと小規模・ノイズデータでの過学習が課題
- 秘密共有と秘密計算を用いたサーバーレス予測を提案
- 提案フレームワークは中央集権的手法と比較して予測精度が向上し、23.81%の精度向上を達成

データプライバシーを保ちながら予測精度も上げるなんて、すごく興味深いよね！セキュリティに煩わされずに産業がもっと効率的になるかも。

**Comment:** Submitted to the 27TH EUROPEAN CONFERENCE ON ARTIFICIAL INTELLIGENCE   (ECAI 2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-05-31 12:27

- - -

### [GANcrop: A Contrastive Defense Against Backdoor Attacks in Federated Learning](http://arxiv.org/abs/2405.20727)

**GANcrop: 連合学習におけるバックドア攻撃に対するコントラスト防御**

Xiaoyun Gan, Shanyu Gan, Taizhi Su, Peng Liu

- 連合学習はデータプライバシー保護のために注目されているが、バックドア攻撃の機会も提供する
- GANcropはコントラスト学習を用いて悪意あるモデルと善良なモデルの違いを探る新たな防御機構を提案
- GANを使用してバックドアトリガーを回収し、ターゲットを絞った緩和戦略を実施する
- 実験結果では、特に非独立同分布（non-IID）シナリオで、バックドア攻撃から効果的に保護しつつ、高いモデル精度を維持することが示された

連合学習のバックドア攻撃を防ぐ新手法って、めちゃ楽しそう！GANを使ってうまく対処してるってみたいだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.DC, **投稿日時:** 2024-05-31 09:33

- - -

### [GI-NAS: Boosting Gradient Inversion Attacks through Adaptive Neural Architecture Search](http://arxiv.org/abs/2405.20725)

**GI-NAS: 適応的ニューラルアーキテクチャ検索による勾配逆転攻撃の強化**

Wenbo Yu, Hao Fang, Bin Chen, Xiaohang Sui, Chuan Chen, Hao Wu, Shu-Tao Xia, Ke Xu

- 連合学習システムで勾配を逆転し、ローカルクライアントの機微データを再構築する手法
- 多くの手法は明示的な事前知識（例: 事前訓練済み生成モデル）に依存しているが、これは現実シナリオでは入手困難
- 提案手法GI-NASはニューラルアーキテクチャ検索を通じて暗黙的な事前知識を活用し、ネットワークを自動検索
- 高解像度画像や大きなバッチサイズ、先進的な防御戦略など、より実用的な設定でも優れた攻撃性能を示した

適応的にニューラルアーキテクチャを探索することで、従来の手法では難しかったシナリオでも成功するって、めっちゃ興味深い！今後のプライバシー技術にとって重要なステップになりそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, cs.CV, **投稿日時:** 2024-05-31 09:29

- - -

### [GenMix: Combining Generative and Mixture Data Augmentation for Medical Image Classification](http://arxiv.org/abs/2405.20650)

**GenMix: 医用画像分類のための生成および混合データ増強の組み合わせ**

Hansang Lee, Haeil Lee, Helen Hong

- GenMixは生成モデルと混合モデルの強みを組み合わせてデータ拡張を行う手法
- 生成モデルは新しいデータパターンを生成するが、GANのモード崩壊や、拡散モデルの訓練困難がある
- 混合モデルはクラス境界を強化するが、クラス不均衡のシナリオで主要クラスを優遇する
- GenMixは合成データと実データを混合し、CT画像中の肝病変分類のパフォーマンスを向上させる

生成と混合の二段構えで強化するって面白いね！医用画像の精度が上がるなら、もっといろんな病気も早期発見できるようになるかもね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-31 07:32

- - -

### [Prune at the Clients, Not the Server: Accelerated Sparse Training in Federated Learning](http://arxiv.org/abs/2405.20623)

**クライアントで剪定を行う: 連合学習における加速スパーストレーニング**

Georg Meinhardt, Kai Yi, Laurent Condat, Peter Richtárik

- 連合学習（FL）は複数のクライアントがローカルデータを保持しながら共有モデルを訓練する方式
- クライアントのリソース制限と通信コストが大規模モデルの訓練において主要な問題
- サーバー側でのスパーストレーニングと加速は失敗し、クライアント側で適切に実行する新手法を提案
- Sparse-ProxSkipは、非凸設定でのスパーストレーニングと加速を組み合わせ、実験でも良好な性能を示す

クライアント側で剪定を行うとか、新しい発想だね！これで連合学習の効率がもっと上がるかも。試してみたくなるね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, math.OC, **投稿日時:** 2024-05-31 05:21

- - -

### [Masked Language Modeling Becomes Conditional Density Estimation for Tabular Data Synthesis](http://arxiv.org/abs/2405.20602)

**マスクドランゲージモデルが表形式データ生成のための条件付き密度推定に変わる**

Seunghwan An, Gyeongdong Woo, Jaesung Lim, ChangHyun Kim, Sungchul Hong, Jong-June Jeon

- 異質な表形式データセットのため、高い機械学習有用性（MLu）を持つ合成データを生成を目指す
- MaCoDEという新しい合成データ生成法を提案し、マスクドランゲージモデル（MLM）を条件付き密度推定に転用
- 提案手法は任意の目標変数と条件変数の組み合わせ間の条件密度推定を可能にする
- 理論的ギャップを埋めることを示し、実世界のデータセットで有効性を実証

これってさ、データを生成するだけじゃなくてプライバシーもコントロールできるのがすごいよね！MLMの応用がこんなに広がるなんて未来が楽しみ〜。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CL, **投稿日時:** 2024-05-31 03:26

- - -

### [Selective Knowledge Sharing for Personalized Federated Learning Under Capacity Heterogeneity](http://arxiv.org/abs/2405.20589)

**キャパシティ不均一性におけるパーソナライズされた連合学習のための選択的知識共有**

Zheng Wang, Zheng Wang, Zhaopeng Peng, Zihui Wang, Cheng Wang

- 連合学習は低キャパシティデバイスからのプライベートデータと計算力を利用可能
- クライアント特有のデータに基づくモデルのパーソナライズが不十分で、効率に課題
- Pa3dFLはレイヤーを一般パラメータと個別パラメータに分けて、効率的な知識の共有を実現
- 実験結果では、Pa3dFLがベースライン法を性能面で一貫して上回り、通信・計算効率も良好

Pa3dFL、すごく面白いね！低キャパシティデバイスの活用が進むと、もっと多様なデバイスでの学習ができるかもね。今後の連合学習がどう発展するか楽しみだな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-31 02:59

- - -

### [Federated Graph Analytics with Differential Privacy](http://arxiv.org/abs/2405.20576)

**差分プライバシーによる連合グラフ分析**

Shang Liu, Yang Cao, Takao Murakami, Weiran Liu, Seng Pei Liew, Tsubasa Takahashi, Jinfei Liu, Masatoshi Yoshikawa

- 連合グラフ分析は差分プライバシーの下での新たな課題である
- プライバシーと有用性のバランスが課題である現状を改善
- 個人のプライバシーを保ちながら任意のグラフ統計を可能にするFEATフレームワークを提案
- FEAT+は真のローカルサブグラフを活用することで全体の有用性を向上

差分プライバシーを確保しながら、めっちゃ使えるグラフ統計ができるなんてすごいよね! みんなでデータ解析してもプライバシーが守られる未来が楽しみだな〜。

**Comment:** 13 pages

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-31 02:09

- - -

### [Hiding Your Awful Online Choices Made More Efficient and Secure: A New Privacy-Aware Recommender System](http://arxiv.org/abs/2405.20483)

**もっと効率的かつ安全に悪いオンライン選択を隠す: 新しいプライバシー対応レコメンダーシステム**

Shibam Mukherjee, Roman Walch, Fredrik Meisingseth, Elisabeth Lex, Christian Rechberger

- プライバシー対応のレコメンダーシステムは、従来のシステムと比較して精度をほぼ維持しながらユーザーデータを保護する
- 現在のシステムは、プライバシーと計算効率の間で大きなトレードオフがある
- 新提案は、機械学習アルゴリズムと準同型暗号や多党計算などの暗号技術を組み合わせている
- 標準ベンチマークに対する実験で、時間とメモリの効率が三桁向上し、低電力のSOCデバイスでも大規模データセットの処理が可能

暗号技術と機械学習の組み合わせで、効率良くプライバシーを守るシステムが実現するなんてすごいね！この研究が進めば、私たちのデータも安心して管理できそう。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-30 21:08

- - -

### [Is Synthetic Data all We Need? Benchmarking the Robustness of Models Trained with Synthetic Images](http://arxiv.org/abs/2405.20469)

**合成データだけで十分か？合成画像で訓練されたモデルの堅牢性のベンチマーク**

Krishnakant Singh, Thanush Navaratnam, Jannik Holmer, Simone Schaub-Meyer, Stefan Roth

- 合成データで訓練されたモデルが注釈のボトルネックを克服する可能性を示した
- 既存の合成自己教師あり・多モーダルモデルが最先端の実画像ベースラインを上回る
- 合成モデルは敵対的および現実世界のノイズに対して実データよりも脆弱である
- 実データと合成データの組み合わせがモデルの堅牢性をさらに向上させる

合成データと実データをうまく組み合わせれば、もっと頑丈なモデルが作れちゃうかも？リアルワールドの応用が楽しみだね！

**Comment:** Accepted at CVPR 2024 Workshop: SyntaGen-Harnessing Generative Models   for Synthetic Visual Datasets. Project page at   https://synbenchmark.github.io/SynCloneBenchmark

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-30 20:37

- - -

### [Exploring the Practicality of Federated Learning: A Survey Towards the Communication Perspective](http://arxiv.org/abs/2405.20431)

**連合学習の実践可能性の探求: 通信の観点からの調査**

Khiem Le, Nhan Luong-Ha, Manh Nguyen-Duc, Danh Le-Phuoc, Cuong Do, Kok-Seng Wong

- 連合学習（FL）はプライバシー保護型の分散学習を実現するが、通信のオーバーヘッドが大きな課題である
- 効果的な通信効率のFLを実現するための戦略と進展を調査し、分類してレビューしている
- 通信非効率の原因を分析し、最新の通信効率化手法を詳細に取り上げている
- 将来の研究課題として、より効果的な通信効率化の方向性を提案している

FLがもっと広く使われたら、イノベーションが進みそうだよね。特にIoTやヘルスケア分野で大きな影響をもたらしそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-05-30 19:21

- - -

### [Enhancing Performance for Highly Imbalanced Medical Data via Data Regularization in a Federated Learning Setting](http://arxiv.org/abs/2405.20430)

**データ正則化による連合学習環境での高度に不均衡な医療データの性能向上**

Georgios Tsoumplekas, Ilias Siniosoglou, Vasileios Argyriou, Ioannis D. Moscholios, Panagiotis Sarigiannidis

- 医療データは複数の提供者間で小規模かつ散在しており、高度なクラス不均衡と厳しいプライバシー制約がある
- 本研究は高度なクラス不均衡下で学習可能なデータ正則化アルゴリズムを提案し、連合学習環境で適用
- 提案手法は、複数ノード間で患者データを使用しプライバシーを保護しつつ心血管疾患予測モデルの性能を向上
- 四つの異なる心血管疾患予測データセットで評価し、ハイパーパラメータ設定やリソース配分シナリオに適応する堅牢性を確認

連合学習でプライバシーを守りながら予測精度を上げるなんてすごいね！他の疾患にもこの技術が応用できたら、もっと医療が進むかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-30 19:15

- - -

### [Gradient Inversion of Federated Diffusion Models](http://arxiv.org/abs/2405.20380)

**連合拡散モデルの勾配反転**

Jiyue Huang, Chi Hong, Lydia Y. Chen, Stefanie Roos

- 拡散モデルは高解像度の画像データを生成するが、大量の実データが必要
- 連合学習でデータの勾配を共有し、モデルを共同訓練するが、プライバシー漏洩のリスクが存在
- GIDMを設計し、生成モデル自体を事前知識として利用して画像をほぼ復元できる
- GIDM+は未知のデータ、ノイズ、サンプリングステップの最適化を行い、さらに高品質の画像復元が可能 

勾配を共有するだけでもこんなにリスクがあるんだ！GIDM+でどうやってその課題を克服するのか、興味津々だよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, cs.CR, cs.CV, **投稿日時:** 2024-05-30 18:00

- - -

### [Learning 3D Robotics Perception using Inductive Priors](http://arxiv.org/abs/2405.20364)

**帰納的事前知識を用いた3Dロボティクス認識の学習**

Muhammad Zubair Irshad

- 帰納的事前知識とバイアスを用いて、原理中心のインテリジェンスを解放する手法やアルゴリズムを設計
- この論文では、過去の経験や世界の動作に関する仮定などの事前知識の使用法を3つのロボティクス認識問題で実証
- 合成データからのジオメトリと外観、モジュール性とセマンティックマップ、セマンティック、構造、および文脈の三つの事前知識を提案
- ロボティクスエージェントが新しいシミュレーションや現実世界の未見環境で動的かつ複雑なシーンを理解するために必要な現実世界データを最小化

事前知識でロボットに賢く動いてもらうなんて面白そう！あまりデータがいらないから、コスト的にもエコフレンドリーかもね。

**Comment:** Georgia Tech Ph.D. Thesis, December 2023. For more details:   https://zubairirshad.com/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.RO, **投稿日時:** 2024-05-30 17:59

- - -

### [Universal Exact Compression of Differentially Private Mechanisms](http://arxiv.org/abs/2405.20782)

**差分プライバシー機構のためのユニバーサルな正確な圧縮**

Yanxiao Liu, Wei-Ning Chen, Ayfer Özgür, Cheuk Ting Li

- 差分プライバシー手法の通信コストを削減するため、Poisson private representation (PPR)を提案
- PPRは、元のランダム化機構のデータと出力の結合分布を正確に保存
- 元のプライバシー機構と同じ統計特性を保持し、理論的な下限に近い圧縮サイズを達成
- 実験結果で、通信、精度、中央とローカル差分プライバシーの間のトレードオフが改善

新しい圧縮手法で差分プライバシーの効率をめっちゃ向上できそう！データの分布をしっかり守りつつ省エネになるって、ホントすごいと思う！

**Comment:** 30 pages, 3 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.IT, math.IT, stat.ML, **投稿日時:** 2024-05-28 23:54

- - -

### [Federated Learning with Blockchain-Enhanced Machine Unlearning: A Trustworthy Approach](http://arxiv.org/abs/2405.20776)

**ブロックチェーン強化による機械アンラーニングを用いた連合学習: 信頼できるアプローチ**

Xuhan Zuo, Minghao Wang, Tianqing Zhu, Lefeng Zhang, Shui Yu, Wanlei Zhou

- プライバシー規制対応とユーザーデータ削除要求に対処するための機械アンラーニングの必要性
- 従来のアンラーニング方法は検証可能なメカニズムが欠如しており、信頼性の確立が困難
- ブロックチェーンを連合学習に統合し、不変性、透明性、強固なセキュリティでアンラーニングプロセスを強化
- フレームワークがアンラーニング要求とアクションの不変記録を確立し、IoT環境での効率とセキュリティの課題に対処

IoT時代には、こういう信頼性の高い技術ってほんとに必要だよね。ブロックチェーンでアンラーニングを強化する発想、とても新鮮で面白そう！

**Comment:** 13 pages, 25 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.DC, cs.LG, **投稿日時:** 2024-05-27 04:35
