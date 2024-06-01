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

更新: 2024-06-01T04:18:20.436304

- - -

### [Federated and Transfer Learning for Cancer Detection Based on Image Analysis](http://arxiv.org/abs/2405.20126)

**連合学習と転移学習を用いた画像解析による癌検出**

Amine Bechar, Youssef Elmir, Yassine Himeur, Rafik Medjoudj, Abbes Amira

- 連合学習（FL）は、複数のサイトに分散したデータでモデルを訓練し、中央データの共有を不要にする
- 転移学習（TL）は、一つのタスクから別のタスクへの知識の転送を可能にする
- 両方法の強みと弱点を評価し、癌検出での応用と将来の方向性を議論
- 画像ベースの癌検出におけるTLとFLの役割について詳細を提供し、追加研究の提案を行う

連合学習と転移学習での癌検出、すごい未来感あるね！これからますます精度が上がって命を救う技術になりそう💖



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-30 15:07

- - -

### [SPAM: Stochastic Proximal Point Method with Momentum Variance Reduction for Non-convex Cross-Device Federated Learning](http://arxiv.org/abs/2405.20127)

**SPAM: モーメント分散縮減を用いた非凸交差デバイス連合学習のための確率的近似点法**

Avetik Karagulyan, Egor Shulgin, Abdurakhmon Sadiev, Peter Richtárik

- 交差デバイス学習では、顧客数が数十億に達する場合があるが、標準的な手法やローカルメソッドにはクライアントドリフトやデータ類似性への鈍感性が課題となる
- 非凸損失を持つ交差デバイス連合学習に対して、新しいアルゴリズム（SPAM）を提案し、これらの問題を解決
- 提案手法は、現実の多様な機械学習問題で満たされるヘッセ行列の類似性に基づき鋭い分析を提供
- 部分参加設定でも成果が示され、顧客がサーバーと通信する際にも有効で、クライアント間のデータ類似性の恩恵を受けることが証明されている

めっちゃおもしろそう！クライアントドリフトとか解決できると連合学習がもっと使いやすくなりそうだね。どんなデバイスでもうまく連携できる未来が近づいてる感じがするよ！

**Comment:** The main part of the paper is around 9 pages. It contains the   proposed algorithms, the main theoretical results and the experimental   setting. The proofs of the main results and other technicalities are deferred   to the Appendix

**トピック:** [連合学習](fl), **カテゴリ:** math.OC, cs.LG, 90C26, **投稿日時:** 2024-05-30 15:07

- - -

### [Cross-Training with Multi-View Knowledge Fusion for Heterogenous Federated Learning](http://arxiv.org/abs/2405.20046)

**異種連合学習のための多視点知識融合による交差訓練**

Zhuang Qi, Lei Meng, Weihao He, Ruohan Zhang, Yu Wang, Xin Qi, Xiangxu Meng

- 連合学習は異なるデータソースから訓練することで一般化能力を向上
- データの異質性が以前の知識の忘却を引き起こす問題がある
- 新たな方法FedCTを提案し、個別と全体の知識を融合して性能向上を実現
- FedCTは特に知識保存と特徴空間の多様性向上に有効で、最新手法を上回る

異なるデータソースを使って知識を融合するなんて、連合学習の未来が楽しみだね！これできっともっと賢いAIが生まれるよ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, **投稿日時:** 2024-05-30 13:27

- - -

### [Applications of Generative AI (GAI) for Mobile and Wireless Networking: A Survey](http://arxiv.org/abs/2405.20024)

**モバイルおよびワイヤレスネットワーキングにおける生成AIの応用：サーベイ**

Thai-Hoc Vu, Senthil Kumar Jagatheesaperumal, Minh-Duong Nguyen, Nguyen Van Huynh, Sunghwan Kim, Quoc-Viet Pham

- AIの成功がモバイルネットワーキングとIoT時代への進化を促進
- 生成AI（GAI）は効率的に合成データを作成し、既存データを多様な形で表現
- GAIはネットワーク管理やワイヤレスセキュリティ、セマンティック通信に活用
- 既存の研究成果を総括し、GAIの課題と今後の展望を提示

生成AIがモバイルネットワーキングの未来を変えるなんてワクワクだね！どういうサービスが登場するのか、すごく楽しみ～。



**トピック:** [合成データ](sd), **カテゴリ:** cs.NI, cs.AI, **投稿日時:** 2024-05-30 13:06

- - -

### [subMFL: Compatiple subModel Generation for Federated Learning in Device Heterogenous Environment](http://arxiv.org/abs/2405.20014)

**subMFL: デバイス異種環境における連合学習のための互換性のある部分モデル生成**

Zeyneddin Oz, Ceylan Soygul Oz, Abdollah Malekjafarian, Nima Afraz, Fatemeh Golpayegani

- FLは、異なるデータ量と計算・保存容量を持つ分散型デバイスで一般的に使用される
- 資源制約のあるデバイスでの大規模モデル（DNNなど）の訓練は時間とエネルギーを大量に消費する
- 提案手法では、サーバーが密なモデルをすべてのデバイスに共有し訓練、その後徐々に圧縮
- 実験では、約50％のスパース状態でも精度を保ちつつ、資源制約デバイスの参加率を約50％向上

デバイスの性能に合わせてモデルを圧縮して使うなんて賢いよね！これを使えばもっと多くのデバイスが協力できて、データの偏りも減らせそう💡

**Comment:** 12 pages, 7 figures, European Conference on Parallel Processing, pp.   between 52 and 64, Springer, 2023

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-30 12:49

- - -

### [Robust Kernel Hypothesis Testing under Data Corruption](http://arxiv.org/abs/2405.19912)

**データ破損下でのロバストなカーネル仮説検定**

Antonin Schrab, Ilmun Kim

- 2つの一般的なロバストな置換検定の構築方法を提案
- 最小条件下での一型誤差制御と検出力の一致性を証明
- 差分プライバシーを保証し、プライベートデータ分析にも適用可能
- 提案手法がカーネルMMDとHSICメトリクスでミニマックス最適であることを示す

差分プライバシーを自然に含む検定方法とか、未来のデータ分析に超使えそうじゃない？実装も公開されてるし、試してみたいな！

**Comment:** 26 pages, 2 figures, 2 algorithms

**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-05-30 10:23

- - -

### [Federated Learning with Multi-resolution Model Broadcast](http://arxiv.org/abs/2405.19886)

**マルチ解像度モデルブロードキャストを用いた連合学習**

Henrik Rydén, Reza Moosavi, Erik G. Larsson

- 連合学習では、サーバが定期的にモデルをエージェントへブロードキャスト
- マルチ解像度コーディングと変調を用いることで、下りリンクリソースを節約
- 高SNRエージェントは正確なモデルを、低SNRエージェントは基本的なモデルを受け取る
- 提案手法の有効性をMNISTデータセットを用いた実験で検証

この手法、通信リソースを効率化しつつ、多様なエージェントに対応できるってすごくない？未来感あるよね。MNISTデータセットでちゃんと実験したってところも信頼できるし。



**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.LG, **投稿日時:** 2024-05-30 09:45

- - -

### [Learning from Random Demonstrations: Offline Reinforcement Learning with Importance-Sampled Diffusion Models](http://arxiv.org/abs/2405.19878)

**ランダムデモンストレーションからの学習: 重要サンプリングされた拡散モデルを用いたオフライントレーニング強化学習**

Zeyu Fang, Tian Lan

- 拡散モデルを用いることで合成データ生成を行い、オフライントレーニング強化学習の効果を向上
- 提案手法は、閉ループのポリシー評価とワールドモデル適応を組み合わせている
- 重要サンプリングでワールドモデルのアップデートを行い、実環境下での最適ポリシーとの差分の上限を解析
- D4RL環境での評価により、ランダムなデモンストレーションや中程度の専門知識を持つデモンストレーションがある場合、従来のベースラインよりも大幅な改善を示した

政策の評価方法が新しい発想だから、学習効率がすごく上がってるかも！ランダムなデモからもこうやっていい結果が出せるのは、もっといろいろ応用できそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.GT, **投稿日時:** 2024-05-30 09:34

- - -

### [On Vessel Location Forecasting and the Effect of Federated Learning](http://arxiv.org/abs/2405.19870)

**船舶位置予測と連合学習の影響について**

Andreas Tritsarolis, Nikos Pelekis, Konstantina Bereta, Dimitris Zissis, Yannis Theodoridis

- 船舶位置予測（VLF）は海上認識のために重要であるが、海上交通の複雑性と動的性質により困難
- プライバシー問題とデータの断片化が進み、分散データベースによる学習モデルの質が低下
- 中央集権型（Nautilus）と連合学習型（FedNautilus）の2種類のLSTMニューラルネットワークを提案
- 中央集権型アプローチが現行技術に対して優れていることを示し、連合学習の利点と欠点を議論

船舶の動きってすっごい複雑なんだね～。連合学習のアイディア、もっと発展したら面白そう♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-30 09:23

- - -

### [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](http://arxiv.org/abs/2405.19846)

**Quest: 大規模言語モデルの長コンテキスト拡張のためのクエリ中心データ合成アプローチ**

Chaochen Gao, Xing Wu, Qi Fu, Songlin Hu

- 大規模言語モデルは限られた文脈長で事前訓練されている
- 長文データの不足と不均一な分布が課題
- Questは類似クエリで取得した文書を用いて長文データを合成
- Questは128kの長文データを合成し、他の方法を大幅に上回る

長文データをうまく合成するのってすごいよね！これからの言語モデル、もっと賢くなるかもしれないね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-05-30 08:50

- - -

### [Just Rewrite It Again: A Post-Processing Method for Enhanced Semantic Similarity and Privacy Preservation of Differentially Private Rewritten Text](http://arxiv.org/abs/2405.19831)

**もう一度書き直そう：差分プライバシーによる再書き換え法の意味的類似性とプライバシー保護の強化**

Stephen Meisenbacher, Florian Matthes

- 差分プライバシー（DP）でテキストをプライバタイズするタスクは、再書き換えタスクと見なされる
- 敏感な情報を隠すために、再書き換えテキストと元のテキストの整合性を高める後処理法を提案
- 提案手法により、意味的にオリジナルに近い出力と、高いプライバシー評価が達成できる
- DPの再書き換え手法の評価基準を引き上げ、悪意のある攻撃者に対する追加の保護を提供する

新しい後処理法ってのがどうやって元のテキストとの整合性を高めるのか気になるね！DPの質も上がるなら、色んな応用が考えられそう！

**Comment:** 10 pages, 2 figures, 2 tables. Accepted to ARES 2024 (IWAPS)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, **投稿日時:** 2024-05-30 08:41

- - -

### [Improving Object Detector Training on Synthetic Data by Starting With a Strong Baseline Methodology](http://arxiv.org/abs/2405.19822)

**強力なベースライン手法で合成データによる物体検出器のトレーニングを改善**

Frank A. Ruis, Alma M. Liezenga, Friso G. Heslinga, Luca Ballan, Thijs A. Eker, Richard J. M. den Hollander, Martin C. van Leeuwen, Judith Dijk, Wyke Huizinga

- 現実データの収集と注釈は時間と費用がかかり、軍事分野では危険や不可能
- 合成データによるトレーニングは制限された現実データの代替手段
- 合成データと現実データのギャップを埋めることが課題であり、従来の方法はリアルデータでの良好な性能を基本に構築
- 提案手法は、前訓練済みモデルの特徴を活かしつつ、合成データからの鍵情報を抽出し、データ拡張とTransformerバックボーンを活用

合成データによる物体検知って未来的でワクワクするよね！軍事用途って聞くとちょっと難しそうだけど、これがもっと多くの分野に広がったら面白そうだな〜。

**Comment:** Submitted to and presented at SPIE Defense + Commercial Sensing 2024,   13 pages, 4 figures, 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.ET, **投稿日時:** 2024-05-30 08:31

- - -

### [Dynamic feature selection in medical predictive monitoring by reinforcement learning](http://arxiv.org/abs/2405.19729)

**強化学習による医療予測モニタリングにおける動的特徴選択**

Yutong Chen, Jiandong Gao, Ji Wu

- 時系列情報を効果的に活用できない既存の特徴選択手法の限界を解決
- 各患者に対して時変特徴サブセットを選択する手法を強化学習で最適化
- 合成データを用いて予測モデルを更新し、非微分可能な予測モデルにも適用可能
- 大規模な臨床データセットで実験結果を評価し、コスト制約下で強いベースライン手法を上回る性能を示す

臨床データで強化学習を使って時変動的にアプローチするの、すごく新しい感じ！これが普及したら医療現場がもっと効率的になりそうだね。

**Comment:** preview version

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-30 06:21

- - -

### [Leveraging Open-Source Large Language Models for encoding Social Determinants of Health using an Intelligent Router](http://arxiv.org/abs/2405.19631)

**オープンソースの大規模言語モデルを活用した健康の社会的決定要因のエンコーディングに関するインテリジェントルーターの活用**

Akul Goel, Surya Narayanan Hari, Belinda Waltman, Matt Thomson

- 健康の社会的決定要因（SDOH）は、患者の健康結果に重要な役割を果たすが、患者の電子健康記録（EHR）にはあまり記載されていないことが多い
- 大規模言語モデル（LLM）はEHRからの非構造化データ抽出に有望だが、多くのモデルがあり選択が難しい
- 商業ベンダーの閉鎖型モデルの使用が難しいため、オープンソースのLLMで高性能を示すものが求められている
- 97.4%の精度を示すインテリジェントルーターシステムを導入し、訓練データの拡大に合成データ生成と検証パラダイムを使用した

合成データでプライバシーを守りつつ高精度な解析ができるなんて、未来の医療はもっと広がりそう！実際に医療機関で使われる頃が楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-05-30 02:33

- - -

### [Leveraging Generative AI for Smart City Digital Twins: A Survey on the Autonomous Generation of Data, Scenarios, 3D City Models, and Urban Designs](http://arxiv.org/abs/2405.19464)

**スマートシティのデジタルツインにおける生成AIの活用: データ、シナリオ、3D都市モデル、都市設計の自律生成に関する調査**

Haowen Xu, Femi Omitaomu, Soheil Sabri, Xiao Li, Yongze Song

- スマートシティは効率的で持続可能な都市管理を目的とし、大量のデータが必要
- 生成AIモデルがデータ生成やコード生成で特異な価値を持つことが証明されている
- 調査は生成AI技術を用いたデータ拡張やシナリオ生成、3Dモデリング、都市設計の事例をレビュー
- 次世代の都市デジタルツインに生成AIを統合することで、信頼性や規模、自動化が向上する可能性を議論

生成AIがスマートシティのデジタルツインと一緒にどんなシナジーを生むのか、すごく興味深いよね。これからの都市づくりがどんな風に進化するのか、想像するだけでワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-05-29 19:23

- - -

### [Optimizing Split Points for Error-Resilient SplitFed Learning](http://arxiv.org/abs/2405.19453)

**エラーに強いスプリットポイントを最適化するためのSplitFed学習**

Chamani Shiranthika, Parvaneh Saeedi, Ivan V. Bajić

- 連合学習 (FL) や分割学習 (SL)、SplitFed などの分散学習が進展している
- SplitFed はFLの計算負担軽減とSLの並列化を目指し、プライバシーを維持
- SplitFedのモデル分割ポイントのパケット損失に対するレジリエンスを調査
- 人間胚画像セグメンテーションタスクでの実験により、深い分割ポイントが有意に有利と判明

SplitFedってプライバシーを意識しながら計算負担を減らせるなんて、面白そう！画像セグメンテーションとか多くの場面で役立ちそうだね。

**Comment:** Accepted for poster presentation at the Women in Computer Vision   (WiCV) workshop in CVPR 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, **投稿日時:** 2024-05-29 19:03
