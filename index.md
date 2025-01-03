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

更新: 2025-01-04T04:20:33.869654

- - -

### [Generalizing in Net-Zero Microgrids: A Study with Federated PPO and TRPO](http://arxiv.org/abs/2412.20946)

**ネットゼロマイクログリッドにおける一般化：連合PPOとTRPOの研究**

Nicolas M Cuadrado Avila, Samuel Horváth, Martin Takáč

- プライバシーを保護する共同フレームワークでマイクログリッドのエネルギー管理を改善
- 連合学習とTRPOを統合したFedTRPO手法で分散エネルギー資源を効率管理
- CityLearn環境と合成データで複数建物のネットゼロシナリオをシミュレーション
- FedTRPOは最先端の連合強化学習手法と比較して、ハイパーパラメータ調整なしで高い性能を発揮

この研究、なんだかすごくエコでSDGsっぽい！プライバシーも守りつつ、地球に優しいエネルギー管理を実現するなんて、未来のグリーンテクノロジーって感じで楽しみだなぁ。

**Comment:** Submitted to Environmental Data Science Journal from Cambridge   University Press

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-30 13:38

- - -

### [A Tale of Two Imperatives: Privacy and Explainability](http://arxiv.org/abs/2412.20798)

**2つの命令: プライバシーと説明可能性の物語**

Supriya Manna, Niladri Sett

- 深層学習の普及が、プライバシーと説明可能性の両方を満たす枠組みを要請
- プライバシーには差分プライバシーを採用し、強力な定量的保証を提供
- 説明可能性には、モデル訓練と独立したポストホック説明が選ばれる
- 両者を高リスクな用途で効果的に統合する方法と産業ソフトウェアの例を提示

プライバシーと説明可能性の両立を実際の例で示すのがステキ！どの業界でも応用効きそうで楽しみだね。

**Comment:** Work in progress

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.CV, **投稿日時:** 2024-12-30 08:43

- - -

### [Accelerating Energy-Efficient Federated Learning in Cell-Free Networks with Adaptive Quantization](http://arxiv.org/abs/2412.20785)

**セルフリーネットワークにおける適応量子化を用いた省エネ連合学習の加速**

Afsaneh Mahmoudi, Ming Xiao, Emil Björnson

- 従来の無線ネットワークでは連合学習において遅延が課題だが、CFmMIMOがスペクトル効率を向上させる
- 省エネかつ低遅延な連合学習フレームワークを提案し、適応量子化により通信コストを削減
- FLモデル更新、ローカル反復、電力割り当ての最適化をSQPで解決し、エネルギーと遅延のバランスを実現
- 提案手法が他の方法に比べてテスト精度を最大36％向上させることを数値結果で示す

CFmMIMOを使って、たくさんのクライアントを効率よくつなげるってすごいね！エネルギーとか遅延の問題も上手に解決できそうで、未来のネットワークの可能性を感じるな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-30 08:10

- - -

### [Enhancing Privacy in Federated Learning through Quantum Teleportation Integration](http://arxiv.org/abs/2412.20762)

**連合学習におけるプライバシー強化のための量子テレポーテーション統合**

Koffka Khan

- 連合学習はデータを共有せずにモデルを訓練できるが、モデル更新の共有で情報漏洩のリスクがある。
- 量子テレポーテーションは量子状態を遠隔地に転送し、盗聴を検出できるためデータの安全性を保証する。
- 量子テレポーテーションを用いた新しいアーキテクチャで、モデルパラメータや勾配の安全な交換を実現。
- 現在の量子ネットワークの限界や量子-古典プロトコルの必要性など、実装上の課題も議論されている。 

量子テレポーテーションと連合学習を組み合わせるなんて、未来的でワクワクするよね！これが実現したら、私たちのプライバシーも守られて安心だね。



**トピック:** [連合学習](fl), **カテゴリ:** quant-ph, cs.CR, cs.CY, cs.LG, 68T07 (Primary), 68M14, 94A60 (Secondary), F.2.2; I.2.7; K.4.1; C.2.4, **投稿日時:** 2024-12-30 07:15

- - -

### [Blockchain-Empowered Cyber-Secure Federated Learning for Trustworthy Edge Computing](http://arxiv.org/abs/2412.20674)

**ブロックチェーンによって強化されたサイバーセキュアな信頼できるエッジコンピューティングのための連合学習**

Ervin Moore, Ahmed Imteaj, Md Zarif Hossain, Shabnam Rezapour, M. Hadi Amini

- 連合学習は分散型の機械学習で、データはデバイス上に保存され、ローカルモデルのみが転送される
- 悪意ある参加者による攻撃、特に毒性攻撃により、連合学習の品質が損なわれる可能性がある
- 信頼性構築のために、貢献度に基づく評価モデルとアウトライアー検出で悪質な参加者を排除
- 各デバイスにはトークンを生成し、ブロックチェーンに記録して参加者の信頼度を評価する仕組みを提案

ブロックチェーンと連合学習の組み合わせってすごいよね！信頼できる学習環境を構築するのに最適だと思う。それに、悪質な攻撃まで防げるとか、本当に未来的で安心感があるなぁって感じるよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.CR, cs.LG, **投稿日時:** 2024-12-30 02:58

- - -

### [SafeSynthDP: Leveraging Large Language Models for Privacy-Preserving Synthetic Data Generation Using Differential Privacy](http://arxiv.org/abs/2412.20641)

**SafeSynthDP: 差分プライバシーを用いたプライバシー保護型合成データ生成のための大規模言語モデル活用**

Md Mahadi Hasan Nahid, Sadid Bin Hasan

- 機械学習モデルは個人情報を含むデータに依存し、プライバシー問題を引き起こす
- 大規模言語モデルを用いて差分プライバシー付きの合成データセットを生成する手法を提案
- ラプラスやガウス分布によるノイズ注入でデータのプライバシー保持を確保
- 実験では、差分プライバシー機構を組み込んだ合成データがプライバシーとデータ利用性のバランスを実現

大規模言語モデルがプライバシーを守りながらデータを生成できるなんてかっこいい！これが普及すれば、安心して研究や開発ができそうだよね。未来の技術がどんどん進化していくのが楽しみ！

**Comment:** 15 pages, 1 figure, 5 tables

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-30 01:10

- - -

### [A Multiparty Homomorphic Encryption Approach to Confidential Federated Kaplan Meier Survival Analysis](http://arxiv.org/abs/2412.20495)

**機密連合カプラン・マイヤー生存分析のためのマルチパーティ準同型暗号アプローチ**

Narasimha Raghavan Veeraragavan, Svetlana Boudko, Jan Franz Nygård

- 医療データの増加により共同研究が活発だが、プライバシー規制が患者記録の共有を妨げている。
- マルチパーティ準同型暗号を用いて、プライバシーを守りつつ生存分析を実現。
- 合成データなどでの実験では、暗号化された生存曲線も非暗号化とほぼ一致する正確さを示す。
- 複数の提供者による連合では復元攻撃の脆弱性があるが、暗号によって機密性が向上。

これってすごく未来っぽい感じだよね！マルチパーティで進めるって、普通の人には意味不明に感じるかもだけど、秘密を守りつつ分析するなんて最高じゃない？みんなでデータを共有できるなんて、医療の進歩がますます加速しそう！

**Comment:** 40 pages

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AI, cs.LG, cs.MS, stat.ML, **投稿日時:** 2024-12-29 15:17

- - -

### [Sub-optimal Learning in Meta-Classifier Attacks: A Study of Membership Inference on Differentially Private Location Aggregates](http://arxiv.org/abs/2412.20456)

**メタ分類器攻撃における最適でない学習：差分プライバシーによる位置情報集計に対するメンバーシップ推論の研究**

Yuhan Liu, Florent Guepin, Igor Shilov, Yves-Alexandre De Montjoye

- 差分プライバシーを用いた位置情報の集計でも、プライバシーリスクが過小評価される可能性がある。
- 新たに1つの閾値攻撃と2つの閾値攻撃の2つのメトリック基準のMIAsを提案し、異なるデータ分布での効果を調査。
- MLPベースの攻撃はラプラスノイズ下で最適でなく、プライバシーリスクを過小評価することがわかった。
- 差分プライバシー付きデータ集合全般にも応用可能であり、合成データ生成や事前学習が複雑なルール学習を促進可能。

位置情報だけでなく、他のデータにも使えるって面白そう！実際のプライバシーリスクがもっと正確にわかったら、安心感が増すかもね。あと、合成データとか事前学習で進化したMLPがどんな結果をもたらすのか、未来が楽しみだね。



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-29 12:51

- - -

### [Election of Collaborators via Reinforcement Learning for Federated Brain Tumor Segmentation](http://arxiv.org/abs/2412.20253)

**連合脳腫瘍セグメンテーションのための強化学習による協力者選定**

Muhammad Irfan Khan, Elina Kontio, Suleiman A. Khan, Mojtaba Jafaritadi

- 連合学習はデータプライバシーを保持しつつ、共同でモデルを訓練する技術である
- 動的なFL環境では協力者の選定が難しく、強化学習とsimAggで改善策を提案
- バランスの取れた協力者の選定により、多様なデータセットで効率的な訓練が可能
- シミュレーション実験でUCBがEGを上回り、より高いDiceスコアを達成した

強化学習のおかげで、協力者の選び方がもっと賢くなるっていうのが面白かった！これからの脳腫瘍の研究がもっと進む予感がするね。技術の進歩で医療がもっと良くなるといいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-12-28 19:54

- - -

### [Recommender Engine Driven Client Selection in Federated Brain Tumor Segmentation](http://arxiv.org/abs/2412.20250)

**フェデレーテッド脳腫瘍セグメンテーションにおけるレコメンダーエンジン主導のクライアント選択**

Muhammad Irfan Khan, Elina Kontio, Suleiman A. Khan, Mojtaba Jafaritadi

- フェデレーテッドラーニングのための最適なクライアント選択プロトコルを提案
- レコメンダーエンジンにより、非活性な協力者選択問題を改善
- 調和類似度加重集約によりモデルパラメータの自動適応を実現
- 脳腫瘍セグメンテーションにおいて高精度な結果を達成

この論文すごく面白そうじゃない？特に、専門性に基づいて協力者を選ぶことで、フェデレーテッドラーニングの効率が上がるってところが、エレガントで素敵なアイディアだと思う！ 🎓✨



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-12-28 19:49

- - -

### [Federated Unlearning with Gradient Descent and Conflict Mitigation](http://arxiv.org/abs/2412.20200)

**勾配降下と対立緩和による連合消去**

Zibin Pan, Zhichao Wang, Chi Li, Kaiyan Zheng, Boqi Wang, Xiaoying Tang, Junhua Zhao

- 連合学習ではグローバルモデルがクライアントのデータを覚えてしまう問題がある
- 連合消去はデータ削除を再トレーニングなしで行う手法として期待されるが課題もある
- 本研究は、対象クライアントの勾配に近い非衝突の勾配を計算する新手法を提案
- 提案手法は既存手法よりも消去性能とモデルの実用性を両立していると示された

連合消去って面白そうだよね！忘れられる権利がちゃんと守られるってことだし、技術的にもすごく挑戦的なことをやってる感じがするから、これからに期待だね。

**Comment:** To be published in the Proceedings of the 39th AAAI Conference on   Artificial Intelligence (AAAI-25)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-12-28 16:23

- - -

### [Enhancing Marine Debris Acoustic Monitoring by Optical Flow-Based Motion Vector Analysis](http://arxiv.org/abs/2412.20085)

**海洋ゴミ音響モニタリングの光フロー解析による強化**

Xiaoteng Zhou, Katsunori Mizuno

- 海洋ゴミ問題は人間活動により増加し、海洋生態系に深刻な影響を与えている。
- 従来の光学センサーでは低視認性の水中や海底でのモニタリングに限界がある。
- 音響カメラは水の濁りや暗闇に影響されず、ゴミ監視に有用だが課題も多い。
- 新たな光フローベースの方法で、先行ラベルなしにゴミの分布モニタリングが可能になる。

海の中のゴミをもっと正確に見つけるために、音響と光の技術を掛け合わせたなんて未来的でワクワクするよね。これが広まれば海の環境もきっと良くなって、私たちの住む地球がもっと綺麗になるんじゃないかな♪

**Comment:** 8 pages, conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-28 08:55

- - -

### [Calibre: Towards Fair and Accurate Personalized Federated Learning with Self-Supervised Learning](http://arxiv.org/abs/2412.20020)

**Calibre: 自己教師あり学習による公平で正確な個別連合学習に向けて**

Sijia Chen, Ningxin Su, Baochun Li

- 自己教師あり学習を用いても、異質なデータ間では高品質な個別モデルが学習できない。
- SSLのままではクラス境界が曖昧になり、低精度な個別モデルが生成される。
- Calibreは一般性と顧客特化性をバランスした表現を校正するために設計された。
- 実験結果により、Calibreが精度と公平性で最先端の性能を発揮することが示された。

自己教師あり学習を連合学習に活かす工夫が興味深いね！データの偏りがあっても公平に学習できるのはポイント高いなー。どんな使われ方するのか楽しみ！

**Comment:** ICDCS camera-ready paper, Code repo:   https://github.com/TL-System/plato/tree/main/examples/ssl/calibre

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-12-28 04:43

- - -

### [A Robust Federated Learning Framework for Undependable Devices at Scale](http://arxiv.org/abs/2412.19991)

**スケールの大きい信頼できないデバイス向けのロバストな連合学習フレームワーク**

Shilong Wang, Jianchun Liu, Hongli Xu, Chunming Qiao, Huarong Deng, Qiuye Zheng, Jiantao Gong

- 連合学習では、スマートフォンなどがしばしば不安定でトレーニングが困難である
- 障害に対応するために、端末の履歴に基づき依存性を評価し、高依存性のデバイスを選択する
- モデルキャッシュを利用し、中断されたトレーニングの再開を支援しリソース浪費を防ぐ
- 実験結果で、FLUDEが不安定な環境でも効率的なモデル性能の向上を実現することが示された

この研究、とっても面白いね！普段のスマホの使い方が直接活かせるなんて、未来が楽しみだな～。不安定な環境でも効率よく動くって、何かすごく自分たちの暮らしに近い感じがするよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-12-28 03:28

- - -

### [Caesar: A Low-deviation Compression Approach for Efficient Federated Learning](http://arxiv.org/abs/2412.19989)

**Caesar: 効率的な連合学習のための低偏差圧縮アプローチ**

Jiaming Yan, Jianchun Liu, Hongli Xu, Liusheng Huang, Jiantao Gong, Xudong Liu, Kun Hou

- 圧縮は連合学習の通信オーバーヘッドを軽減するが、情報損失がモデルや勾配の偏差を引き起こす
- Caesarはモデル精度とトラフィックコストのバランスをとる低偏差圧縮を提案
- ローカルモデルの不鮮明度に基づき圧縮率を最適化し、精密な初期モデルでのトレーニングを実現
- Caesarはトラフィックコストを25.54%～37.88%削減し、精度劣化はわずか0.68%にとどまる

圧縮しながらトラフィックを抑えつつ精度も維持するなんて、すっごく良さそう！特に実際のデバイスで実験してるところが、現実的な貢献を感じるよね。将来の連合学習がますます楽しみ！

**Comment:** 12 pages, 27 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-12-28 03:20

- - -

### [Delayed Random Partial Gradient Averaging for Federated Learning](http://arxiv.org/abs/2412.19987)

**遅延ランダム部分勾配平均化による連合学習の強化**

Xinyi Hu

- 連合学習における通信ボトルネックは帯域幅制限と高レイテンシーによる
- 遅延ランダム部分勾配平均化(DPGA)を提案し、通信効率を改善
- クライアントは部分的なローカルモデルの勾配のみを共有し更新率で調整
- DPGAにより通信と計算が並行処理されるため、システム実行時間を短縮

通信ボトルネックのせいでスムーズに学習が進まないこともあるんだね！DPGAを使えばもっと効率的にモデルを共有できるってすごくスマートじゃん。これからどんどん進化していきそうで楽しみだなー！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-28 03:14

- - -

### [Hades: Homomorphic Augmented Decryption for Efficient Symbol-comparison -- A Database's Perspective](http://arxiv.org/abs/2412.19980)

**Hades: 効率的なシンボル比較のための準同型増強復号 - データベース視点から**

Dongfang Zhao

- 完全準同型暗号（FHE）を用いたクラウド上のデータベースは、セキュアなデータ処理を可能にする
- FHEで暗号化されたデータの比較は重要であり、従来の手法では実用的な展開が難しい
- 新たな暗号フレームワークHADESはFHE暗号文での効率的な比較を可能にする
- HADESは実データセットで実用的な性能を示し、既存の手法を上回る

HADESって、FHEの限界を突破するかも！クラウドなんてまさに信頼できない場所だからこそ、これは大事かもね。それにデータベースって本当になんでも依存するから、こういう進歩ってすごいワクワクするよね。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.DB, cs.CR, **投稿日時:** 2024-12-28 02:47

- - -

### [Explainable Semantic Federated Learning Enabled Industrial Edge Network for Fire Surveillance](http://arxiv.org/abs/2412.19979)

**説明可能なセマンティック連合学習による工業エッジネットワークの火災監視**

Li Dong, Yubo Peng, Feibo Jiang, Kezhi Wang, Kun Yang

- 工業用IoTデバイスは大量の監視データを送信し、スペクトラム資源を消費している
- セマンティック通信を使用し、データのプライバシーとセキュリティを確保するXSFLを提案
- 異種デバイス向けに適応的なクライアント訓練戦略によりモデルの適応性を向上
- セマンティクスと監視データの関係をleakyReLUで説明するESCメカニズムを設計

火災監視のために工業用IoTデバイスが大量のデータを効率よく処理するのって面白い！説明可能なこれらの技術が、もっと安全で高度な監視システムを実現する未来に貢献しそうだね。

**Comment:** 9 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.IT, math.IT, **投稿日時:** 2024-12-28 02:45
