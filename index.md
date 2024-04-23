---
layout: single
title: トップページ
permalink: /
author_profile: true
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

To be written.

## 最新更新分

更新: 2024-04-23T04:24:15.336939

- - -

### [Poisoning Attacks on Federated Learning-based Wireless Traffic Prediction](http://arxiv.org/abs/2404.14389)

**連合学習を用いた無線トラフィック予測に対する攻撃**

Zifan Zhang, Minghong Fang, Jiayuan Huang, Yuchen Liu

- 連合学習は、基地局間でグローバル制御モデルを訓練する分散フレームワークを提供し、ローカルネットワークデータのプライバシーを侵害しない
- 連合学習を用いた無線トラフィック予測は、ネットワーク資源の最適化や交通流管理の向上、信頼性の高い通信支援アプリケーションの強化に寄与
- 提案された偽トラフィック注入（FTI）攻撃は、最小限の知識で作成されたトラフィック分布を注入することにより、システムを損なうよう設計されている
- グローバル-ローカル不整合検出（GLID）という防御メカニズムを導入し、統計方法を用いて推定された特定のパーセンタイル範囲を超える異常なモデルパラメータを戦略的に除去する

**Comment:** Accepted by IFIP/IEEE Networking 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.CR, cs.LG, C.2.1, **投稿日時:** 2024-04-22 17:50

- - -

### [Better Synthetic Data by Retrieving and Transforming Existing Datasets](http://arxiv.org/abs/2404.14361)

**既存のデータセットを活用して合成データの質を向上するための新メソッド、DataTune**

Saumya Gandhi, Ritu Gala, Vijay Viswanathan, Tongshuang Wu, Graham Neubig

- 信頼できるNLPモデルの構築には大量の高品質なトレーニングデータが必要であるが、タスク特有のデータが不足している問題に対処
- 既存のデータセットを新たなタスクに再利用可能な形に変換する機能を有するDataTuneメソッドを導入
- DataTuneを用いて言語モデルをファインチューニングすることで、従来の合成データや検索トレーニングデータを用いる方法と比べ性能が平均34%向上
- 生成されるデータの多様性と難易度が著しく向上し、広範な言語ベースのタスクにおいて有効性を示す



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-04-22 17:15

- - -

### [Machine Learning Techniques for MRI Data Processing at Expanding Scale](http://arxiv.org/abs/2404.14326)

**MRIデータ処理のための機械学習技術の拡大規模**

Taro Langner

- MRIは数万人の参加者から大規模なデータセットを生成し、人間の健康に関する情報が豊富に含まれている
- データセット間の分布の変化に対応する際、転移学習を使用する課題がある
- 連合学習を用いて、複数の機関に安全に保持された分散訓練データへの安全なアクセスを実現
- 表現学習は、マルチモーダルな入力形式で抽象的な関係を表現する埋め込みをエンコードする手法として評価される

**Comment:** Book chapter pre-print

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-04-22 16:38

- - -

### [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](http://arxiv.org/abs/2404.14219)

**Phi-3技術報告: スマートフォンで利用可能な高性能言語モデル**

Marah Abdin, Sam Ade Jacobs, Ammar Ahmad Awan, Jyoti Aneja, Ahmed Awadallah, Hany Awadalla, Nguyen Bach, Amit Bahree, Arash Bakhtiari, Harkirat Behl, Alon Benhaim, Misha Bilenko, Johan Bjorck, Sébastien Bubeck, Martin Cai, Caio César Teodoro Mendes, Weizhu Chen, Vishrav Chaudhary, Parul Chopra, Allie Del Giorno, Gustavo de Rosa, Matthew Dixon, Ronen Eldan, Dan Iter, Abhishek Goswami, Suriya Gunasekar, Emman Haider, Junheng Hao, Russell J. Hewett, Jamie Huynh, Mojan Javaheripi, Xin Jin, Piero Kauffmann, Nikos Karampatziakis, Dongwoo Kim, Mahoud Khademi, Lev Kurilenko, James R. Lee, Yin Tat Lee, Yuanzhi Li, Chen Liang, Weishung Liu, Eric Lin, Zeqi Lin, Piyush Madan, Arindam Mitra, Hardik Modi, Anh Nguyen, Brandon Norick, Barun Patra, Daniel Perez-Becker, Thomas Portet, Reid Pryzant, Heyang Qin, Marko Radmilac, Corby Rosset, Sambudha Roy, Olli Saarikivi, Amin Saied, Adil Salim, Michael Santacroce, Shital Shah, Ning Shang, Hiteshi Sharma, Xia Song, Olatunji Ruwase, Xin Wang, Rachel Ward, Guanhua Wang, Philipp Witte, Michael Wyatt, Can Xu, Jiahang Xu, Sonali Yadav, Fan Yang, Ziyi Yang, Donghan Yu, Chengruidong Zhang, Cyril Zhang, Jianwen Zhang, Li Lyna Zhang, Yi Zhang, Yunan Zhang, Xiren Zhou

- phi-3-miniは、3.8億パラメーター、3.3兆トークンから成る言語モデルであり、Mixtral 8x7BやGPT-3.5とほぼ同等の性能を示す
- このモデルは、強化フィルタリングされたウェブデータと合成データを含む拡張データセットで訓練されている
- スマートフォンで動作するほどの小規模ながら、安全性や堅牢性そしてチャット形式での利用にも対応
- phi-3-miniよりも能力が高いphi-3-smallとphi-3-mediumモデルも紹介され、それぞれ3.8兆トークンで訓練されている

**Comment:** 12 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-04-22 14:32

- - -

### [DPTraj-PM: Differentially Private Trajectory Synthesis Using Prefix Tree and Markov Process](http://arxiv.org/abs/2404.14106)

**DPTraj-PM: 差分プライバシーを用いた軌跡データの合成技術についての解析**

Nana Wang, Mohan Kankanhalli

- DPTraj-PMは、差分プライバシーを用いて個人のプライバシーを保護しつつ、高いデータ利用価値を維持する軌跡データの合成方法を提案
- 初期の軌跡セグメントと次の位置情報を基に、トラジェクトリを隣接セルに離散化し、プレフィックスツリー構造とm次マルコフ過程を組み合わせてモデル化
- データの有用性を保持しながら差分プライバシーの下でノイズを加えた合成データセットを生成
- 実際のデータセットにおいて、既存技術よりもデータ利活用度が格段に向上していることが実証



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-04-22 11:52

- - -

### [Multi-agent Reinforcement Learning-based Joint Precoding and Phase Shift Optimization for RIS-aided Cell-Free Massive MIMO Systems](http://arxiv.org/abs/2404.14092)

**多エージェント強化学習を用いたRIS支援セルフリーマッシブMIMOシステムの共同プリコーディングと位相シフト最適化**

Yiyang Zhu, Enyu Shi, Ziheng Liu, Jiayi Zhang, Bo Ai

- セルフリーの多入出力システムでは、分散アクセスポイントを用い高いスペクトル効率を実現するが、過酷な伝播環境が通信性能を低下させる
- 再構成可能なインテリジェントサーフェス（RIS）を低コストかつ省エネルギーの手段として導入し、システム性能向上を図る
- アクセスポイントのプリコーディングマトリックスとRISの反射係数を最適化するために、多エージェント強化学習アルゴリズムとファジーロジックを組み合わせた手法を提案
- 提案したアルゴリズムはローカルチャネル情報のみを必要とし、計算複雑性を減少させながら従来手法と同様の性能を達成することをシミュレーションで確認



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, eess.SP, math.IT, **投稿日時:** 2024-04-22 11:25

- - -

### [FedTAD: Topology-aware Data-free Knowledge Distillation for Subgraph Federated Learning](http://arxiv.org/abs/2404.14061)

**FedTAD: トポロジー認識を用いたデータフリー知識蒸留によるサブグラフ連合学習**

Yinlin Zhu, Xunkai Li, Zhengyu Wu, Di Wu, Miao Hu, Rong-Hua Li

- サブグラフ連合学習は、グラフニューラルネットワークの協調トレーニングを多クライアントサブグラフで実施する新たな分散パラダイムである
- サブグラフの異質性は、ノードおよびトポロジーの変動から生じており、全体モデルの性能低下を引き起こす
- ノードやトポロジーの変動は、ラベル分布の差と構造的同質性の違いに対応することが明らかにされた
- 提案されたトポロジー認識データフリー知識蒸留技術（FedTAD）は、ローカルモデルからグローバルモデルへの信頼できる知識伝達を強化する

**Comment:** Accepted by IJCAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DB, cs.SI, **投稿日時:** 2024-04-22 10:19

- - -

### [Apodotiko: Enabling Efficient Serverless Federated Learning in Heterogeneous Environments](http://arxiv.org/abs/2404.14033)

**Apodotiko: 異質環境での効率的なサーバーレス連合学習を実現**

Mohak Chadha, Alexander Jensen, Jianfeng Gu, Osama Abboud, Michael Gerndt

- 連合学習は分散クライアント間で共有モデルの協同トレーニングを可能にし、データは分散されたまま保持される
- Apodotikoでは、クライアントのハードウェア能力とデータセットサイズを評価するスコアリングメカニズムを用いてクライアントを選定
- この戦略により、訓練プロセスを遅らせる非効率なクライアント（stragglers）の影響が最小限に抑えられる
- 実験結果では、Apodotikoは他の連合学習戦略に比べて平均2.75倍、最大7.03倍のスピードアップを達成し、サーバーレス環境での冷始動も平均で四分の一に削減

**Comment:** Accepted at IEEE/ACM CCGrid'24

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-04-22 09:50

- - -

### [Dual Model Replacement:invisible Multi-target Backdoor Attack based on Federal Learning](http://arxiv.org/abs/2404.13946)

**連合学習に基づく目に見えない多目標バックドア攻撃 - デュアルモデル置換**

Rong Wang, Guichen Zhou, Mingjun Gao, Yunpeng Xiao

- 連合学習モデルに潜むバックドアの隠蔽性を高めるため、TrojanGanステガノグラフィーモデルを用いて、特定の攻撃情報を不可視のノイズとしてエンコードし画像に挿入
- 単一バックドアトリガーの問題に対処するため、複合トリガー攻撃という画像毒性攻撃法を提案し、マルチバックドアトリガーの実現とバックドア攻撃の堅牢性を向上
- ローカルトレーニングメカニズムがバックドア攻撃の成功率を低下させる問題に対して、デュアルモデル置換バックドア攻撃アルゴリズムを設計し、連合学習の集約モデルの性能を保ちつつ攻撃成功率を向上
- 実験により、連合学習下でのバックドアの高い隠蔽性とトリガー形式の多様化、そして多目標攻撃における良好な成功率が確認された



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-04-22 07:44

- - -

### [Fair Concurrent Training of Multiple Models in Federated Learning](http://arxiv.org/abs/2404.13841)

**連合学習における複数モデルの公平な並行トレーニング**

Marie Siew, Haoran Zhang, Jong-Ik Park, Yuezhou Liu, Yichen Ruan, Lili Su, Stratis Ioannidis, Edmund Yeh, Carlee Joe-Wong

- 既存の多モデル連合学習（MMFL）アルゴリズムは、クライアントとタスクの割り当てに平均ベースの簡易手法を使用しており、難易度が異なる学習タスクに対して不公平な成果を生じさせることがある
- 大規模なモデルには多くのトレーニングラウンドとデータが必要で、資源割り当ての単純な方法では一部のタスクでトレーニング時間が過度に長くなったり、精度が低下したりすることが問題となる
- FedFairMMFLという難易度を考慮したアルゴリズムを設計し、各トレーニングラウンドでクライアントをタスクに動的に割り当てることで公平性と収束率を保証する
- 複数タスクのトレーニングにクライアントを動機づける新しいオークション設計を提案し、タスク間でのトレーニング努力の公平な分配を実現し、その影響を実データセット上で評価する



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-22 02:41

- - -

### [From LLM to NMT: Advancing Low-Resource Machine Translation with Claude](http://arxiv.org/abs/2404.13813)

**LLMからNMTへ: Claudeを用いて低リソース機械翻訳を進化させる**

Maxim Enis, Mark Hopkins

- Claude 3 Opusは、他の大規模言語モデルよりも優れた機械翻訳能力を示す
- Claudeを用いて英語への低リソース機械翻訳の効果を確認する新たなベンチマークを作成
- Claudeはリソース効率が高いことが判明し、リソースレベルに依存する翻訳モデルの品質が向上
- クロードを使用して生成した合成データにより、知識蒸留を進め、Yoruba-English翻訳で最新技術を更新

**Comment:** 17 pages, 15 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-04-22 01:22

- - -

### [A Comparative Study on Enhancing Prediction in Social Network Advertisement through Data Augmentation](http://arxiv.org/abs/2404.13812)

**ソーシャルネットワーク広告における予測向上のためのデータ拡張に関する比較研究**

Qikai Yang, Panfeng Li, Xinyu Shen, Zhicheng Ding, Wenjing Zhou, Yi Nian, Xinhe Xu

- ソーシャルネットワーク広告データの生成的拡張フレームワークが提示され、試された
- 生成型敵対ネットワーク(GANs)、変分オートエンコーダー(VAEs)、ガウス混合モデル(GMMs)の3つの生成モデルを用いてデータの豊富さと多様性が向上
- データ拡張により様々な分類器の性能が定量的に改善されたことが示された
- 各データ拡張技術による相対的な性能向上を比較し、実践者がモデル性能を向上させるための適切な技術を選択するための洞察を提供



**トピック:** [合成データ](sd), **カテゴリ:** cs.SI, cs.AI, **投稿日時:** 2024-04-22 01:16

- - -

### [Adaptive Heterogeneous Client Sampling for Federated Learning over Wireless Networks](http://arxiv.org/abs/2404.13804)

**無線ネットワーク上での連合学習のための適応型異種クライアントサンプリング**

Bing Luo, Wenli Xiao, Shiqiang Wang, Jianwei Huang, Leandros Tassiulas

- 連合学習（FL）では、多数の参加者がいる状況とサーバーの通信帯域が限られている場合に、クライアントの一部だけを各ラウンドで選択する
- 提案されたアルゴリズムは、システムと統計の両方の異質性を考慮し、実時間での収束時間を最小化する
- 実用化された収束境界から、適応的な帯域幅割り当て方式を用いて学習の総時間とサンプリング確率の関係を解析的に確立
- 実験により、提案されたサンプリング方式は、収束時間を著しく短縮したことが示された

**Comment:** Published in IEEE Transactions on Mobile Computing (TMC). arXiv admin   note: substantial text overlap with arXiv:2112.11256

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, cs.NI, cs.SY, eess.SY, **投稿日時:** 2024-04-22 00:16

- - -

### [Universal Fingerprint Generation: Controllable Diffusion Model with Multimodal Conditions](http://arxiv.org/abs/2404.13791)

**ユニバーサル指紋生成: 多モーダル条件を用いた制御可能な拡散モデル**

Steven A. Grosz, Anil K. Jain

- 合成データに基づく指紋認識技術はプライバシー問題の緩和に有効だが、現在の生成手法では同じ指の異なる印象の生成に制約がある
- GenPrintは、指紋のクラス、取得タイプ、センサーデバイス、品質レベルにおいて、容易に制御可能な多様な指紋イメージを生成するフレームワークを提供
- GenPrintは既存の訓練データセットに限定されず、新たなデバイスからの新スタイルも追加のチューニングなしで生成可能
- 実データのみで訓練されたモデルと同等またはそれ以上の精度を持ち、既存のリアルな指紋データセットを拡張することで性能を向上



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-04-21 23:01

- - -

### [Bt-GAN: Generating Fair Synthetic Healthdata via Bias-transforming Generative Adversarial Networks](http://arxiv.org/abs/2404.13634)

**Bt-GAN: バイアス変換型生成敵対ネットワークを用いた公正な合成健康データ生成**

Resmi Ramachandranpillai, Md Fahim Sikder, David Bergström, Fredrik Heintz

- 電子健康記録（EHR）の合成データ生成は、リアルで非識別化されたデータの生成による有用性の向上を目指す
- 従来の研究は合成健康データの品質に注目していたが、ダウンストリームの予測における公正性が疎かにされていた
- Bt-GANは、偏りのある相関を取り除き、アルゴリズム的公正を基に正確なサブグループ表現を捉えることを目指して設計された
- 実験結果は、Bt-GANが最先端の精度を達成しつつ公正性を大幅に向上し、バイアスの増幅を最小限に抑えることを示す



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-21 12:16

- - -

### [FedMPQ: Secure and Communication-Efficient Federated Learning with Multi-codebook Product Quantization](http://arxiv.org/abs/2404.13575)

**FedMPQ: 連合学習における安全かつ通信効率の良い多コードブック積量子化**

Xu Yang, Jiapeng Zhang, Qifeng Zhang, Zhuo Tang

- 連合学習における安全な集約は悪意のあるアグリゲーターからの推論攻撃を効果的に防ぐが、追加的な通信オーバーヘッドが必要であり、グローバルモデルの収束率を妨げる場合がある
- 無線ネットワーク環境において帯域幅が非常に限られているため、安全な集約の下で効率的な通信圧縮を実現することは高度に困難であり貴重な課題である
- 本研究では、複数共有コードブック積量子化に基づく新しい連合学習のためのアップリンク通信圧縮方法であるFedMPQを提案し、前回の更新から堅牢なコードブックを生成し、TEEまたはTTPを用いて安全な集約を実現
- LEAFデータセットにおける実験では、提案方法がベースラインの最終精度の99%を達成しつつ、アップリンク通信量を90-95%削減することを示した



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-04-21 08:27

- - -

### [FedTrans: Efficient Federated Learning Over Heterogeneous Clients via Model Transformation](http://arxiv.org/abs/2404.13515)

**FedTrans: 異種クライアントにおける効率的な連合学習のためのモデル変換**

Yuxuan Zhu, Jiachen Liu, Mosharaf Chowdhury, Fan Lai

- 連合学習は、クライアントのデータやデバイスの異種性により個別モデル開発に課題が多い
- FedTransはグローバルモデルから始まり、精度のボトルネックを特定し、モデル変換で新たなモデルを導出
- マルチモデル更新のソフト集約を用いて個別クライアントに適したモデルを割り当て
- 実際の設定に基づく評価では、FedTransが個々のクライアントモデルの精度を14% - 72%向上させ、訓練コストを1.6X - 20X削減



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-04-21 03:31

- - -

### [MultiConfederated Learning: Inclusive Non-IID Data handling with Decentralized Federated Learning](http://arxiv.org/abs/2404.13421)

**マルチ連合学習: 分散連合学習による包括的な非独立同一分布データ処理**

Michael Duchesne, Kaiwen Zhang, Chamseddine Talhi

- 連合学習は、プライバシーを保持しながらグローバルモデルの訓練を可能にするが、単一の集約サーバが障害の原因となることがある
- 非独立同一分布（non-IID）データの存在は、モデルの性能を最大50%低下させる
- 提案されたマルチ連合学習は、複数のモデルを並行して維持し、非独立同一分布データにおける収束を支援する
- 転移学習を用いて、学習者は少数のモデルに収束することができ、柔軟性の向上のためにどの更新を集約するかを選択できる



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-20 16:38

- - -

### [DNA: Differentially private Neural Augmentation for contact tracing](http://arxiv.org/abs/2404.13381)

**差分プライバシーを実装したニューラルネットワークによる接触追跡の改善**

Rob Romijnders, Christos Louizos, Yuki M. Asano, Max Welling

- COVID19パンデミックは経済や社会への大きな影響をもたらした
- 従来の接触追跡はプライバシーの懸念から広く採用されなかった
- 新たにニューラルネットワークを用いて学習し、差分プライバシーを満たすことで、個人のプライバシー保護を強化
- この技術をCOVID19のシミュレータに適用することで、感染者の特定と感染率の低減が可能になった

**Comment:** Privacy Regulation and Protection in Machine Learning Workshop at   ICLR 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.MA, q-bio.PE, **投稿日時:** 2024-04-20 13:43

- - -

### [Breaking the Memory Wall for Heterogeneous Federated Learning with Progressive Training](http://arxiv.org/abs/2404.13349)

**連合学習のための進行型トレーニングによるメモリ制約の克服**

Yebo Wu, Li Li, Chunlin Tian, Chengzhong Xu

- ProFLは、連合学習モデルをブロックに分割し、各ブロックを順番にトレーニングすることによりメモリ消費を削減
- トレーニングは2段階で行われ、「進行型モデル縮小」と「進行型モデル成長」に分けられ各ブロックが期待される特徴表現を学習できるよう設計
- 各ブロックの学習状況を評価し次のトレーニングを触発する新しいスカラー指標を提案
- ProFLはピークメモリ使用量を最大57.4%削済み、モデル精度を最大82.4%向上させることが実証された



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-04-20 11:08

- - -

### [Collaborative Visual Place Recognition through Federated Learning](http://arxiv.org/abs/2404.13324)

**共同視覚位置認識における連合学習の導入**

Mattia Dutto, Gabriele Berton, Debora Caldarola, Eros Fanì, Gabriele Trivigno, Carlo Masone

- 視覚位置認識(VPR)は画像から位置を特定する問題で、画像内のグローバル表現（ディスクリプタ）を抽出する
- 伝統的にVPRのトレーニングは中央集権的に行われていたが、この研究では連合学習(FL)を通じて分散化を試みる
- VPRのデータは明確なクラスがなく、対照学習により中央データベースでのデータマイニングが必要
- 提案されたFedVPRフレームワークは連合学習による画像検索任務を実現し、新たな課題を提起する

**Comment:** 13 pages, 7 figures, CVPR - The 3rd International Workshop on   Federated Learning for Computer Vision (FedVision-2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-20 08:48

- - -

### [EHRFL: Federated Learning Framework for Heterogeneous EHRs and Precision-guided Selection of Participating Clients](http://arxiv.org/abs/2404.13318)

**EHRFL: 各異なるEHRを持つ医療機関間での連合学習フレームワークと参加クライアントの精密誘導選択**

Jiyoun Kim, Junu Kim, Kyunghoon Hur, Edward Choi

- EHRFLは、異なる医療コーディングシステムとデータベーススキーマを持つ医療機関間で連合学習を可能にするフレームワークとして提案された
- 経費削減を目的として、適切な参加クライアント数の最適化に関する新しい精密ベースの方法が提示された
- 手法はデータの潜在特性を利用して、その病院に適した参加者を特定する
- 実験結果により、EHRFLは異なるEHRシステムを持つ病院間での連合学習を効果的に支援し、運営コストを削減しつつモデル性能を損なうことなくクライアント数を減少させることが確認された



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-04-20 08:23

- - -

### [PoseINN: Realtime Visual-based Pose Regression and Localization with Invertible Neural Networks](http://arxiv.org/abs/2404.13288)

**PoseINN: リアルタイム映像ベースのポーズ推定とローカライゼーションにおける可逆ニューラルネットワークの活用**

Zirui Zang, Ahmad Amine, Rahul Mangharam

- カメラから自己位置推定を行うことはロボティクスや拡張現実にとって重要な課題
- 可逆ニューラルネットワーク(INN)を利用して画像の潜在空間とポーズとのマッピングを行うことを提案
- 提案モデルは既存の最先端モデルと同等のパフォーマンスを有しつつ、訓練速度が速く、低解像度の合成データのオフラインレンダリングにのみ依存
- 正規化フローを用いることで出力の不確実性の推定も提供



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.CV, **投稿日時:** 2024-04-20 06:25

- - -

### [Federated Transfer Learning with Task Personalization for Condition Monitoring in Ultrasonic Metal Welding](http://arxiv.org/abs/2404.13278)

**超音波金属溶接における条件モニタリングのための連合学習とタスク個別化**

Ahmadreza Eslaminia, Yuquan Meng, Klara Nahrstedt, Chenhui Shao

- 超音波金属溶接(UMW)には、プロセスの異常が結合品質を大きく低下させるため、条件モニタリング(CM)が必要
- データのプライバシー保護と高コストの問題を解決するために、タスク個別化を伴う連合転送学習(FTL-TP)フレームワークを提案
- FTL-TPは客の関連タスク間でCMモデルを適応させ、性能と適応性を向上
- 実際のエッジ-クラウドアーキテクチャ上で実装し、UMWの異なる2つのCMタスクにおいて従来のFLアルゴリズムよりも5.35%から8.08%の精度向上を実証

**Comment:** 37 pages, 8 figures

**トピック:** [連合学習](fl), [連合転移学習](ftl), **カテゴリ:** cs.LG, cs.AI, cs.DC, eess.SP, **投稿日時:** 2024-04-20 05:31

- - -

### [Intelligent Agents for Auction-based Federated Learning: A Survey](http://arxiv.org/abs/2404.13244)

**オークションベースの連合学習における知能エージェント: 総説**

Xiaoli Tang, Han Yu, Xiaoxiao Li, Sarit Kraus

- オークションベースの連合学習は、データ所有者を公平かつ効率的にモチベートする新しいインセンティブ設計
- 知能エージェント利用により、オークションの意思決定サポートを効率化
- 関連文献の既存研究を利害関係者、採用されるオークション方式、エージェントの目標別に分類し多角的に整理
- 既存のアプローチの限界を分析し、性能評価メトリクスを要約し、今後の有望な研究方向を議論



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.GT, **投稿日時:** 2024-04-20 03:05

- - -

### [Personalized Wireless Federated Learning for Large Language Models](http://arxiv.org/abs/2404.13238)

**個別化無線連合学習を用いた大規模言語モデル**

Feibo Jiang, Li Dong, Siwei Tu, Yubo Peng, Kezhi Wang, Kun Yang, Cunhua Pan, Dusit Niyato

- 大規模言語モデルは自然言語処理で革新をもたらしたが、無線ネットワークでの導入にはプライバシーやセキュリティの課題がある
- 連合学習はこれらの課題に対処する有望なアプローチだが、データの不均一性やリソース集約的なトレーニング、高い通信オーバーヘッドに悩まされている
- 個別化無線連合学習のために、通信オーバーヘッドが低い二つの微調整方法、個別化連合手続き調整と個別化連合タスク調整を導入
- 提案方法の効果をシミュレーションで実証し、未解決の課題について詳細に議論している

**Comment:** 8 pages, 5 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-04-20 02:30

- - -

### [PAFedFV: Personalized and Asynchronous Federated Learning for Finger Vein Recognition](http://arxiv.org/abs/2404.13237)

**PAFedFV: 個別化および非同期連合学習による指静脈認識**

Hengyu Mu, Jian Guo, Chong Han, Lijuan Sun

- 指静脈データの異質性と非IIDの問題を解決するため、個別化されたモデル集約方法を設計
- クライアントがサーバーからモデルを返却されるのを待つ時間を有効活用するための非同期訓練モジュールを導入
- 6つの指静脈データセットに関する広範な実験を実施し、非IIDデータが連合学習の性能に与える影響を分析
- PAFedFVは精度と堅牢性の点での優位性を示す



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-20 02:25

- - -

### [DISC: Latent Diffusion Models with Self-Distillation from Separated Conditions for Prostate Cancer Grading](http://arxiv.org/abs/2404.13097)

**DISC: 前立腺がんグレーディングのための分離条件からの自己蒸留を用いた潜在拡散モデル**

Man M. Ho, Elham Ghelichkhan, Yosep Chong, Yufei Zhou, Beatrice Knudsen, Tolga Tasdizen

- 潜在拡散モデル(LDM)を用いて、複数のグリーソン等級(GG)を含む合成画像タイルの生成を行った
- GGパターンを生成するために新しいフレームワーク「自己蒸留から分離条件(DISC)」を導入
- 合成タイルは、特に珍しいGG5の症例において前立腺がんグレーディングのモデルの一般化を大幅に改善
- この研究は、生成モデルがデータが限られている場合にがんグレーディングを向上させる可能性を示した

**Comment:** Abstract accepted for ISBI 2024. Extended version to be presented at   SynData4CV @ CVPR 2024. See more at https://minhmanho.github.io/disc/

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, cs.LG, q-bio.QM, **投稿日時:** 2024-04-19 06:52

- - -

### [Intellecta Cognitiva: A Comprehensive Dataset for Advancing Academic Knowledge and Machine Reasoning](http://arxiv.org/abs/2404.13065)

**Intellecta Cognitiva: 学術知識と機械推論の進歩のための包括的データセット**

Ajmal PS, Ditto PS, Jithin VG

- Intellectaは合成データと教科書データを組み合わせた11.53億トークンから成る革新的なデータセット
- 言語モデルの認知処理能力を高めるために設計されている
- Mixtral-8x7B-Instruct-v0.1モデルを活用して複雑な思考プロセスと詳細な教科書スタイルの説明生成を促進
- 合成データの潜在力を示し、AIの限界を拡張する大規模で多様なリポジトリを提供



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-04-13 06:11
