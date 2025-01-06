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

更新: 2025-01-06T04:24:45.200621

- - -

### [Mingling with the Good to Backdoor Federated Learning](http://arxiv.org/abs/2501.01913)

**善良な者と混じり合う: 連合学習にバックドアを仕掛ける**

Nuno Neves

- 連合学習はデータセットのプライバシーを保ちながらモデルを共同訓練する技術
- バックドアの攻撃手法MIGOは、正当なモデル更新と巧妙に混ざり、長期間仕掛ける
- MIGOは5つのデータセットで高精度なバックドアを実装し、主要タスクのユーティリティを維持
- 他の攻撃手法を超え、最小0.1%のクライアントでの攻撃成功を示す

この研究、なんかエキサイティングだと思わない？連合学習の新たな脅威として、攻撃手法と防御の駆け引きがこれからどんな展開を見せるのか、ちょっとワクワクしちゃうかも！

**Comment:** 13 pages, 9 figures, under submission

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.DC, D.4.6; I.2, **投稿日時:** 2025-01-03 17:30

- - -

### [LCFed: An Efficient Clustered Federated Learning Framework for Heterogeneous Data](http://arxiv.org/abs/2501.01850)

**LCFed: 異質なデータに対する効率的なクラスタード連合学習フレームワーク**

Yuxin Zhang, Haoyu Chen, Zheng Lin, Zhe Chen, Jin Zhao

- クラスタード連合学習は、データの異質性による性能問題に対処し、類似データのデバイスをクラスタ化して協調モデル訓練を行う。
- 既存の方法ではクラスター内での知識共有に限定され、グローバルな知識統合が欠如し、最適性能に達しない。
- 提案するLCFedはモデル分割とサブモデルごとの集約戦略を取り入れ、より広範な知識統合を実現し、最適な訓練を達成。
- LCFedは低ランクモデルに基づく効率的なモデル類似度計測法を使用し、リアルタイムのクラスター更新を低コストで実現。

異質なデータの連合学習をさらに効率化する仕組みって何かおもしろそう！クラスタごとに特化しつつ、しっかり全体の知識も共有する感じだから、将来のアプリケーションの性能が期待できるなって思う。

**Comment:** 6 pages, 3 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2025-01-03 14:59

- - -

### [Time Series Language Model for Descriptive Caption Generation](http://arxiv.org/abs/2501.01832)

**時系列データの記述的キャプション生成のための言語モデル**

Mohamed Trabelsi, Aidan Boyd, Jin Cao, Huseyin Uzunalioglu

- 時系列データの自然言語による自動記述生成が分析を簡潔にし解釈性を向上
- 既存の基盤モデルはNLPやCVで進展も、時系列解析はデータ不足で難航
- 新モデルTSLMは、時系列データの微細なパターンを捉え、精確な説明文生成が可能
- TSLMは合成データ生成とデータノイズ除去によりデータ不足を克服

時系列データの分析がもっとわかりやすくなりそうで面白そう！いろんな分野で応用できるかもね、期待しちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2025-01-03 14:34

- - -

### [Age-Based Device Selection and Transmit Power Optimization in Over-the-Air Federated Learning](http://arxiv.org/abs/2501.01828)

**年齢ベースデバイス選択と送信電力最適化によるオーバーザエア連合学習**

Jingyuan Liu, Zheng Chang, Ying-Chang Liang

- オーバーザエア連合学習は通信効率を向上させるが、デバイス選択と信号集約の誤差が性能を制限
- 制限を改善するため、デバイス選択と送信電力を最適化し、遅延デバイスの公平な参加を実現
- 年齢ベースのデバイス選択で収束の上限を理論的に分析し、デバイス優先順位を計算
- 実験でMSEを低減し、モデルの公平性と効率を保ちながら安定した性能を保証

デバイス選択と電力調整で効率よく学習するのが面白そう！最新技術でさらなるモデル精度アップが期待できるね。ますます連合学習の世界が広がる予感！



**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, cs.LG, **投稿日時:** 2025-01-03 14:27

- - -

### [Uncertainty-Aware Label Refinement on Hypergraphs for Personalized Federated Facial Expression Recognition](http://arxiv.org/abs/2501.01816)

**不確実性を考慮したハイパーグラフによる個別化された連合学習対応の表情認識のラベル改良**

Hu Ding, Yan Yan, Yang Lu, Jing-Hao Xue, Hanzi Wang

- 中央集権的な学習で行われる表情認識にはプライバシーの懸念がありデータ収集が困難
- 個別化された連合学習を使い実現する分散設定が実用的と考え、新しいAMY手法を開発
- 各ローカルモデルは不確実性推定ブロックと表情分類ブロックで構成される
- ハイパーグラフを用いた不確実性推定とラベル伝播で、精度の高い個人化された表情認識モデルを構築

AMY手法めっちゃおもしろそう！ハイパーグラフとか、ちょっと難しそうだけど、うまく活用すれば顔認識の精度がグンと上がりそうだね！公開されるコードも試してみたい！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-03 13:59

- - -

### [Creating Artificial Students that Never Existed: Leveraging Large Language Models and CTGANs for Synthetic Data Generation](http://arxiv.org/abs/2501.01793)

**存在しない人工学生の創出：大規模言語モデルとCTGANを活用した合成データ生成**

Mohammad Khalil, Farhad Vadiee, Ronas Shakya, Qinyi Liu

- 教育データのプライバシー保護が課題であり、合成データが有望な解決策となる
- CTGANと3つのLLMを使用して、学生の合成データを生成
- 合成データの統計的および予測性能を検証し、モデル間の比較を実施
- 学習分析研究のための新たなデータ生成手法の基盤を提供

AIを使って架空の学生データを作るなんて、面白いアイデアだね。プライバシーを守りつつ学習分析が進むと、もっと個別最適な教育ができそうでワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-03 12:52

- - -

### [Advancing privacy in learning analytics using differential privacy](http://arxiv.org/abs/2501.01786)

**差分プライバシーを用いた学習分析におけるプライバシーの向上**

Qinyi Liu, Ronas Shakya, Mohammad Khalil, Jelena Jovanovic

- 学習分析でデータプライバシーと利用のバランスを模索
- 差分プライバシーを適用した新たな枠組みを提案
- DPを用いた実験でデータプライバシーの保護を検証
- データプライバシーと有用性のトレードオフを探求

法律とかデジタル時代の流れってすごく速いよね。この新しいDPフレームワークが広まれば、デジタル教育がもっと安心して使えるものになるかも！めっちゃ面白そうで、未来の学習がどんなふうに変わっていくのか楽しみ！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2025-01-03 12:36

- - -

### [Can Synthetic Data be Fair and Private? A Comparative Study of Synthetic Data Generation and Fairness Algorithms](http://arxiv.org/abs/2501.01785)

**合成データは公平でプライベートになりうるか？合成データ生成と公平性アルゴリズムの比較研究**

Qinyi Liu, Oscar Deho, Farhad Vadiee, Mohammad Khalil, Srecko Joksimovic, George Siemens

- 機械学習の多用により、公平性とプライバシーの懸念が高まっている
- 合成データはプライバシーと公平性向上を目的に登場
- DECAFアルゴリズムはプライバシーと公平性の最適なバランスを実現
- 合成データに公平性の前処理を施すと、リアルデータ以上に公平性が改善

合成データを使った公平でプライベートな世界が近づいてるって思うとワクワクするね！特に、合成データの方がリアルデータよりも効果的に公平性を改善できるなんて、すごい発見だと思うよ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CY, **投稿日時:** 2025-01-03 12:35

- - -

### [Denoising and Adaptive Online Vertical Federated Learning for Sequential Multi-Sensor Data in Industrial Internet of Things](http://arxiv.org/abs/2501.01693)

**産業用IoTにおける逐次マルチセンサーデータのためのノイズ除去と適応的オンライン垂直連合学習**

Heqiang Wang, Xiaoxiong Zhong, Kang Liu, Fangming Liu, Weizhe Zhang

- インテリジェントセンサーの計算能力向上で、データ収集から複雑な計算処理まで可能になっている
- 集中型学習の通信負荷とプライバシー問題を解決するため、DAO-VFLアルゴリズムを提案
- DAO-VFLは連続データストリームを管理し、学習目標の変化に適応可能である
- 実験結果から、DAO-VFLがベンチマークアルゴリズムよりも優れた性能を示している

産業用IoTのセンサーが賢くなって、データだけじゃなくっていろいろ計算もできるようになったなんてすごいよね！DAO-VFLがその力を活かして、よりよい学習ができるようになるのが面白いポイントだと思うな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.NI, **投稿日時:** 2025-01-03 08:22

- - -

### [Practical Secure Inference Algorithm for Fine-tuned Large Language Model Based on Fully Homomorphic Encryption](http://arxiv.org/abs/2501.01672)

**微調整された大規模言語モデルのための完全準同型暗号に基づく実用的な安全推論アルゴリズム**

Zhang Ruoyan, Zheng Zhongxiang, Bao Wankang

- 大規模言語モデルはプライバシー漏洩のリスクがあるが、準同型暗号とPEFTで安全性を向上
- モデルを公開部分と秘密部分に分け、計算負荷を削減しながらプライバシーを守るアプローチを採用
- Private Linear Layerを導入し、モデル抽出攻撃から守りつつ、本来の機能を維持
- 提案手法はチャットモデルChatGLM2-6Bを基にし、実験で1.61秒/トークンの効率を達成

完全準同型暗号ってなんだか魔法みたいじゃない？モデルの秘密を守りながらも効率的な推論ができるなんてワクワクする！これからどんな応用が可能になるのか、すごく楽しみだね。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2025-01-03 07:19

- - -

### [Look Back for More: Harnessing Historical Sequential Updates for Personalized Federated Adapter Tuning](http://arxiv.org/abs/2501.01653)

**もっと見るための振り返り: 個別化された連合アダプターチューニングのための歴史的逐次更新の活用**

Danni Peng, Yuan Wang, Huazhu Fu, Jinpeng Jiang, Yong Liu, Rick Siow Mong Goh, Qingsong Wei

- 既存の連合学習は最新モデルに依存し、過去の更新を無視しがちで最適化が不十分
- 新たに提案されたpFedSeqは、過去の更新を利用することで個別アダプターを最適化
- pFedSeqは選択的状態空間モデルを採用し、隠れた関連性をキャプチャする
- 4つのベンチマークデータセットで最先端の個別連合学習手法より優れていることを実証

過去のデータの活用でより個別化されたモデルができるなんて面白そう！連合学習の進化を感じるね。次の実験や応用が待ち遠しいなぁ！

**Comment:** Accepted by AAAI 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2025-01-03 06:10

- - -

### [Stackelberg Game Based Performance Optimization in Digital Twin Assisted Federated Learning over NOMA Networks](http://arxiv.org/abs/2501.01584)

**デジタルツインを活用したNOMAネットワークにおける連合学習のスタッケルベルクゲームによる性能最適化**

Bibo Wu, Fang Fang, Xianbin Wang

- フェデレーテッドラーニングはデータプライバシーを守るが、計算資源と通信環境の制約で課題あり
- デジタルツインが分散資源を模倣し、ストラグラー問題を軽減する可能性を持つ
- クライアント選択において信頼性を考慮し、モデル更新の攻撃リスクを緩和する手法を提案
- スタッケルベルクゲームを用いて遅延とエネルギー消費を最小化し、優れた性能を証明

デジタルツインでフェデレーテッドラーニングって新しい試みだね！どういう風に影響するか追ってみると面白そうだなあ。未来のネットワーク技術になりそうでワクワクしちゃう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.GT, cs.NI, **投稿日時:** 2025-01-03 00:43

- - -

### [OmniChat: Enhancing Spoken Dialogue Systems with Scalable Synthetic Data for Diverse Scenarios](http://arxiv.org/abs/2501.01384)

**OmniChat: 多様なシナリオ向けにスケーラブルな合成データを活用した対話システムの強化**

Xize Cheng, Dongjie Fu, Xiaoda Yang, Minghui Fang, Ruofan Hu, Jingyu Lu, Bai Jionghao, Zehan Wang, Shengpeng Ji, Rongjie Huang, Linjun Li, Yu Chen, Tao Jin, Zhou Zhao

- 現在の対話データセットは規模とシナリオの多様性が制約で、複雑な会話に対応しづらい
- 多様なシナリオをカバーする合成データを利用し、ShareChatXデータセットを提案
- OmniChatは異なる対話コンテキストで機能を最適化する多段階対話システム
- 合成と実データの最適なバランスを見つけ、DailyTalkデータセットで最高性能を達成

対話システムって、いろんな会話に対応できるのがこれから重要になってくるよね！合成データを使って性能を上げつつ、リアルな対話感を求めていくアプローチが面白いねー。どんなシチュエーションでも話せるって、会話AIの未来がすごく楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.HC, cs.SD, eess.AS, **投稿日時:** 2025-01-02 17:58

- - -

### [TabTreeFormer: Tabular Data Generation Using Hybrid Tree-Transformer](http://arxiv.org/abs/2501.01216)

**TabTreeFormer: ハイブリッドな木-トランスフォーマーによる表形式データ生成**

Jiayu Li, Bingyin Zhao, Zilong Zhao, Kevin Yee, Uzair Javaid, Yingjie Lao, Biplab Sikdar

- トランスフォーマーは表形式データ生成で成功しているが、ドメイン特有の帰納バイアスが欠如している。
- 新たに提案したTabTreeFormerは、木ベースモデルで非平滑で低相関のパターンを捉え、合成データの忠実度を向上。
- デュアル量子化トークナイザーにより多様な連続分布を捉え、数値データの学習を促進した。
- 実験でTabTreeFormerはデータ合成の忠実度、効用、プライバシー、効率で優れ、ベースラインの1/16サイズで40%の効用向上。

TabTreeFormerって面白いね！新しいアプローチで表形式データの問題に挑んでいるのがカッコいいなぁ。しかも効率と精度を両立しているところが、データ処理を効率化する未来を感じちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2025-01-02 11:57

- - -

### [Vulnerability-Aware Spatio-Temporal Learning for Generalizable and Interpretable Deepfake Video Detection](http://arxiv.org/abs/2501.01184)

**脆弱性対応時空間学習による汎用的かつ解釈可能なディープフェイク動画検出**

Dat Nguyen, Marcella Astrid, Anis Kacem, Enjie Ghorbel, Djamila Aouada

- ディープフェイク動画は時空間アーティファクトが複雑に絡み合うため、検出が難しい
- 従来の方法は本質的なアーティファクトに焦点を当てづらく、汎用性や解釈性に欠ける
- FakeSTormerはマルチタスク学習フレームワークを用い、アーティファクトを強調し解釈性を向上
- 動画データの合成手法で微細なアーティファクトを持つ偽動画を生成し、モデルの精度を向上

FakeSTormerって名前がカッコいい！偽動画を合成して検出力を上げるなんて、すごく新しいアイデアだね。技術でディープフェイクを見破る未来が楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-02 10:21

- - -

### [Ultrasound Lung Aeration Map via Physics-Aware Neural Operators](http://arxiv.org/abs/2501.01157)

**物理に基づくニューラルオペレーターによる超音波肺エアレーションマップ**

Jiayun Wang, Oleksii Ostras, Masashi Sode, Bahareh Tolooshams, Zongyi Li, Kamyar Azizzadenesheli, Gianmarco Pinton, Anima Anandkumar

- 肺超音波は解釈が複雑で、専門家の技量が求められる
- LUNAというAIモデルで直接エアレーションマップを再構築
- 合成データと実データの両方でLUNAの性能を高めた
- 9％のエアレーション誤差で信頼性のある診断を実現

肺の状態を短時間で把握できるってすごくない？これならもっと多くの医療現場で使われそうだね！技術は進化してるんだなって実感するよ。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.LG, physics.med-ph, **投稿日時:** 2025-01-02 09:24

- - -

### [Communication-and-Computation Efficient Split Federated Learning: Gradient Aggregation and Resource Management](http://arxiv.org/abs/2501.01078)

**通信と計算効率の良い分割連合学習: 勾配集約とリソース管理**

Yipeng Liang, Qimei Chen, Guangxu Zhu, Muhammad Kaleem Awan, Hao Jiang

- 大規模学習モデルの普及に伴い、分割連合学習（SFL）が注目を集めている
- 従来のSFLは通信オーバーヘッドが大きい問題がある
- 提案手法はモデル分割と勾配集約を効率化し、通信効率を向上させる
- 理論解析と実験により、優れた収束性能と通信効率を示す

通信効率を考慮した連合学習、とても実用的な提案だと思う！特に、ダイナミックなモデル分割が実現できるなら、さらに効率的なシステムが構築できそうでワクワクするね。

**Comment:** 13 pages,8 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2025-01-02 05:53

- - -

### [FAPL-DM-BC: A Secure and Scalable FL Framework with Adaptive Privacy and Dynamic Masking, Blockchain, and XAI for the IoVs](http://arxiv.org/abs/2501.01063)

**FAPL-DM-BC: 適応的プライバシーと動的マスキング、ブロックチェーン、説明可能AIを備えた安全でスケーラブルなIoV向けFLフレームワーク**

Sathwik Narkedimilli, Amballa Venkata Sriram, Sujith Makam, MSVPJ Sathvik, Sai Prashanth Mallellu

- FAPL-DM-BCは、連合学習を活用しプライバシーやセキュリティ、スケーラビリティを最適化するソリューション。
- 動的マスキングを使用し、データ感度に応じて適応的にプライバシーポリシーを切り替える。
- ブロックチェーンを活用しロギングと検証を行い、安全な分散検証を確立。
- 説明可能AIを利用し、効率的な連合学習を実現し、IoVにおける多様な応用が見込まれる。

IoVの未来が見えるね！自動運転車とかスマートシティとか実現したらワクワクしちゃう。安全性もばっちりで心強いね。

**Comment:** 1 table, 1 figure

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2025-01-02 05:21

- - -

### [Fides: Scalable Censorship-Resistant DAG Consensus via Trusted Components](http://arxiv.org/abs/2501.01062)

**Fides: 信頼されたコンポーネントによるスケーラブルな検閲抵抗DAGコンセンサス**

Shaokang Xie, Dakai Kang, Hanzheng Lyu, Jianyu Niu, Mohammad Sadoghi

- FidesはDAGベースのBFTコンセンサスでTEEを活用し、スケーラビリティとセキュリティの課題に対処する
- 既存プロトコルが直面する課題は大規模クオーラムや通信コスト、検閲耐性の低さなど
- 信頼できるコンポーネントとして信頼できるブロードキャストや取引開示を採用し、効率化を図る
- 実験結果では最先端プロトコルより優れた性能を示し、現実のブロックチェーンシステムでの有用性を証明

ブロックチェーンの世界で検閲耐性とか、なんだか日々の自由を守る騎士みたいでかっこいい！Fidesなら、これからもっと広がるネットワークの未来を安心して頼れるかもね。



**トピック:** [TEE](tee), **カテゴリ:** cs.DC, cs.DB, **投稿日時:** 2025-01-02 05:13

- - -

### [KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model](http://arxiv.org/abs/2501.01028)

**KaLM-Embedding: 優れた訓練データによる強力な埋め込みモデル**

Xinshuo Hu, Zifei Shan, Xinping Zhao, Zetian Sun, Zhenyu Liu, Dongfang Li, Shaolin Ye, Xinyuan Wei, Qian Chen, Baotian Hu, Min Zhang

- 埋め込みモデルは、生成強化型モデルで重要性が増している
- KaLM-Embeddingは多言語対応し、多様な質の高いデータを活用
- 技術的には、多様化と効率性向上の工夫を取り入れている
- MTEBベンチマークで、同サイズのモデルを超える性能を発揮

新しい埋め込みモデルが、品質の高い訓練データでどれだけ強化されるか、すごく気になる！多言語対応だし、他のモデルとの比較も魅力的だよね。

**Comment:** Technical Report. 23 pages, 6 figures, 10 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2025-01-02 03:17

- - -

### [Enhancing Early Diabetic Retinopathy Detection through Synthetic DR1 Image Generation: A StyleGAN3 Approach](http://arxiv.org/abs/2501.00954)

**合成DR1画像生成による糖尿病性網膜症早期検出の向上：StyleGAN3アプローチ**

Sagarnil Das, Pradeep Walia

- 糖尿病性網膜症は視力を奪う重大な病気で、早期発見が重要だが、良質なデータが不足
- StyleGAN3を用いて微細血管瘤を含む高精度で多様な合成画像を生成し、データ不足を補う試み
- 2,602枚のDR1画像を使用しトレーニング、定量・質的に評価し実現度を確認
- 合成画像は高リアリズムを示しつつ、境界部に軽微なアーティファクトが見られるが、現実のデータセットを補完

医療分野での合成データ活用が進歩すると、診断の精度が上がってみんな安心して暮らせるようになりそうだね。微細血管瘤の表現なんて、検出精度がかなり向上するはず。応用範囲がもっと広がったら他の病気の早期発見にもつながるかも！

**Comment:** 13 pages, 11 figures

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.AI, cs.CV, **投稿日時:** 2025-01-01 21:00

- - -

### [Population Aware Diffusion for Time Series Generation](http://arxiv.org/abs/2501.00910)

**時系列生成のための人口意識拡散**

Yang Li, Han Meng, Zhenyu Bi, Ingolv T. Urnes, Haipeng Chen

- 従来の拡散モデルは個別レベルのデータの真実性に重点を置き、集団レベルの特性を軽視している
- 集団レベルの特性には、クロスコリレーションなどの値の分布や依存関係の分布が含まれる
- 提案するPaD-TSは、人口レベルの特性保存を組み込んだ新しいトレーニング手法を挙げる
- ベンチマークで本来と合成データのCC分布シフトスコアを5.9倍改善しつつ個別レベルの性能も維持

この研究、なんか未来のデータ処理の面で役立ちそう！集団レベルの特性を意識して時系列データを生成するなんて、凄く新しいアプローチだよね。PaD-TSの方法がどんな風に実社会に影響を与えるのか楽しみかも！

**Comment:** Accepted for publication at AAAI-2025, 8 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-01 17:53

- - -

### [A Survey of Secure Semantic Communications](http://arxiv.org/abs/2501.00842)

**安全なセマンティック通信の調査**

Rui Meng, Song Gao, Dayu Fan, Haixiao Gao, Yining Wang, Xiaodong Xu, Bizhu Wang, Suyu Lv, Zhidi Zhang, Mengying Sun, Shujun Han, Chen Dong, Xiaofeng Tao, Ping Zhang

- セマンティック通信は6G技術の一環で冗長情報を省きデータの核を抽出
- セマンティック通信はデータ伝送の負担軽減や効率的な資源配分が特徴
- モデル移行や情報伝送においてセキュリティやプライバシーの問題が懸念
- セキュリティ対策としてデータクリーニング、秘密計算、差分プライバシーなどの技術を列挙

セマンティック通信って凄い！効率化しながら安全性もバッチリ考えられてるなんて、未来を感じるね。こんな技術が進化すれば、通信がもっと便利で安心になるかも！

**Comment:** 123 pages, 27 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, eess.IV, eess.SP, **投稿日時:** 2025-01-01 13:46

- - -

### [VoiceRestore: Flow-Matching Transformers for Speech Recording Quality Restoration](http://arxiv.org/abs/2501.00794)

**VoiceRestore: 音声録音品質の復元のためのフローマッチングトランスフォーマー**

Stanislav Kirdey

- 自己教師あり学習を用いた音声録音の品質復元手法を提案
- 背景雑音やリバーブなど多岐にわたる劣化を単一モデルで対処可能
- パラレルなデータセット不要で高品質へのマッピングを実現
- モデルの汎用性を実証し、短文から長文までの復元が可能

この技術があれば、過去の大事な会話とかもクリアになるのかな？リアルな環境での適応も意識してるところが期待大だね。どう変わっていくか楽しみだなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.SD, **投稿日時:** 2025-01-01 10:13

- - -

### [Beyond Static Datasets: A Behavior-Driven Entity-Specific Simulation to Overcome Data Scarcity and Train Effective Crypto Anti-Money Laundering Models](http://arxiv.org/abs/2501.00757)

**静的データセットを超えて: データ不足を克服し効果的な暗号マネーロンダリング防止モデルを訓練する振る舞い駆動のエンティティ特化型シミュレーション**

Dinesh Srivasthav P, Manoj Apte

- 暗号通貨は分散化特性やプライバシー強化で悪用されやすく、多くの不正活動に利用されている。
- マネーロンダリングの検出は困難で、層状化戦略や進化する手法が障害となっている。
- 現存のデータセットは静的で不均等、機械学習モデルの訓練に不向きである。
- 行動を埋め込んだエンティティ特化型シミュレーションで合成データを生成し、実際のマネーロンダリングを効果的に見つける。

シミュレーションで様々な形のトランザクションをモデル化できるんだね！実際の犯罪にも適用できそうな予感、これからの展開が楽しみだな～。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2025-01-01 06:58

- - -

### [Gradient Compression and Correlation Driven Federated Learning for Wireless Traffic Prediction](http://arxiv.org/abs/2501.00732)

**無線トラフィック予測のための勾配圧縮と相関駆動型連合学習**

Chuanting Zhang, Haixia Zhang, Shuping Dang, Basem Shihada, Mohamed-Slim Alouini

- 無線トラフィック予測では連合学習が注目されるが、データ送信量が多いのが課題。
- 勾配圧縮を用いてデータ圧縮を行いながら予測精度を保つ新しいアルゴリズムを提案。
- エラーフィードバックと勾配追跡を用いて圧縮による性能劣化を緩和する。
- 提案手法は通信効率を向上させつつ予測精度を維持し、最先端手法を上回る成果を示す。

通信の効率がめちゃくちゃ良くなるのがすごいよね！プライバシーも守られたままで、未来の通信がもっとスムーズになりそう！📶✨

**Comment:** This paper has been accepted for publication by IEEE Transactions on   Cognitive Communications and Networking (2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2025-01-01 05:28

- - -

### [Cost and Reward Infused Metric Elicitation](http://arxiv.org/abs/2501.00696)

**コストと報酬を組み込んだメトリックの発見**

Chethan Bhateja, Joseph O'Brien, Afnaan Hashmi, Eva Prakash

- 機械学習のメトリック発見は、個人の暗黙的な好みに基づく評価指標の選択を指す
- 現行の発見方法は混同行列に基づく正確度しか考慮していない
- 新しく提案された方法は、追加のコストや報酬を考慮したメトリック発見を可能にする
- 合成データで行った実験により、提案手法の高精度な収束を確認した

この研究、面白そう！コストや報酬を考慮してメトリック選びができるなんて、実際のビジネスにも使えそうだよね。それに合成データでの実験結果も、説得力があると思うな。

**Comment:** Accompanying code at https://github.com/chethus/metric

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, I.2.6, **投稿日時:** 2025-01-01 01:36

- - -

### [Beyond Model Scale Limits: End-Edge-Cloud Federated Learning with Self-Rectified Knowledge Agglomeration](http://arxiv.org/abs/2501.00693)

**モデル規模の限界を超えて: 自己修正された知識アグリゲーションを用いたエンド・エッジ・クラウド連合学習**

Zhiyuan Wu, Sheng Sun, Yuwei Wang, Min Liu, Ke Xu, Quyang Pan, Bo Gao, Tian Wen

- エンド・エッジ・クラウドのコラボレーションは信頼性向上と遅延削減を提供する新たなAIモデル学習手法
- 階層型連合学習は分散型ノード間のモデル集約を可能にするが、不均質性や動的環境により制約がある
- 提案手法FedEECは、エンド、エッジ、クラウドでモデルを成長させ、一般化能力を強化する枠組み
- BSBODPとSKRにより、ノード間の知識転送を最適化し、異種環境で移動性と接続性を保つ

スマホからクラウドまでのAIモデルがどんどん賢くなるって！知識の橋渡しする技術、すごく未来っぽくて面白いかもね。どんな風に進化していくのか、ちょっとワクワクしちゃう♪

**Comment:** 16 pages, 7 tables, 6 figures. arXiv admin note: text overlap with   arXiv:2312.11489

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2025-01-01 01:11

- - -

### [Addressing Challenges in Data Quality and Model Generalization for Malaria Detection](http://arxiv.org/abs/2501.00464)

**データ品質とモデル汎用性の課題を解決するマラリア検出**

Kiswendsida Kisito Kabore, Desire Guel

- マラリア診断の効果は、データ品質とモデル汎用性の問題に制約される
- GANベースの拡張により、データクラスのバランスを調整し精度が15-20%向上
- ドメイン適応技術で感度が最大25%向上し、領域間のロバスト性が改善
- 多様なグローバルデータセットとデータ共有フレームワークが重要である

マラリア診断の進歩って、すごく大事だよね！特にリソースが限られてる地域で、この技術がどんどん役立っていくのってワクワクしちゃう。あとは、GANとか使ってるって、AIの技術が本当に革新的で頼もしいなって思った！

**Comment:** 22 pages, 17 figures, 17 tables, In: Journal of Sensor Networks and   Data Communications (JSNDC). ISSN: 2994-6433. DOI: 10.33140/JSNDC.04.03.09

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-12-31 14:25

- - -

### [Unleashing Text-to-Image Diffusion Prior for Zero-Shot Image Captioning](http://arxiv.org/abs/2501.00437)

**ゼロショット画像キャプション生成のためのテキストから画像への拡散優先度の解放**

Jianjie Luo, Jingwen Chen, Yehao Li, Yingwei Pan, Jianlin Feng, Hongyang Chao, Ting Yao

- テキストデータのみでゼロショット画像キャプションが注目されている
- 合成画像とキャプション間の意味の整合性の問題を解決するために新しい機構を提案
- 顕著な視覚概念を識別し、テキスト特徴と融合することで欠陥を軽減
- 合成データでより高品質なペアを重視する新しいクロスエントロピー損失を開発

この研究、合成データを使ってうまくゼロショット画像キャプションを生成するのがすごく興味深い！画像とテキストの整合性を取るための新しい手法、どんな結果を生み出すのかワクワクするね。

**Comment:** ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, cs.LG, cs.MM, **投稿日時:** 2024-12-31 13:39

- - -

### [Federated Dropout: Convergence Analysis and Resource Allocation](http://arxiv.org/abs/2501.00379)

**連合ドロップアウト: 収束解析とリソース割り当て**

Sijing Xie, Dingzhu Wen, Xiaonan Liu, Changsheng You, Tharmalingam Ratnarajah, Kaibin Huang

- 連合ドロップアウトは、通信と計算のボトルネックを克服する効率的な技術
- 各訓練ラウンドでサブモデルのみを更新・伝送し遅延を低減
- ドロップアウト率が大きいほど収束速度が遅くなることを理論的に示す
- 数値的実験で提案アルゴリズムの有効性を検証

連合ドロップアウトは通信や計算リソースの節約に役立つ技術みたい。理論と実験の両方でしっかりと効果が確認されているのがすごく安心感あるよね。効率的に連合学習を進められるって未来への可能性が広がるよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, math.IT, **投稿日時:** 2024-12-31 10:24

- - -

### [Federated Deep Subspace Clustering](http://arxiv.org/abs/2501.00230)

**連合深部部分空間クラスタリング**

Yupei Zhang, Ruojia Feng, Yifei Wang, Xuequn Shang

- 連合学習を活用したプライバシー保護の部分空間クラスタリング手法を提案
- 各クライアントはエンコード・自己表現・デコードのネットワークで構成
- エンコードネットワークをサーバーで他のクライアントと通信し、学習結果を共有
- 地域的な関係も保ちながら優れたクラスタリング性能を実現

連合学習でプライバシーを保ちつつ、クラスタリング性能を高める方法ってすごく新しいよね！これ、データを安全にやり取りしつつ活用できるって、めちゃくちゃ未来志向だと思うんだ。

**Comment:** 8pages,4 figures, 4 Tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, 68T07, I.5.3, **投稿日時:** 2024-12-31 02:46

- - -

### [FedCod: An Efficient Communication Protocol for Cross-Silo Federated Learning with Coding](http://arxiv.org/abs/2501.00216)

**FedCod: コーディングを用いたクロスサイロ連合学習のための効率的な通信プロトコル**

Peishen Yan, Jun Li, Hao Wang, Tao Song, Yang Hua, Lu Peng, Haihui Zhou, Haibing Guan

- 連合学習はデータのプライバシーを保ちながらモデルを共同で訓練できるパラダイムである
- クロスサイロFLは、地理的に分散したサイロ間の通信効率が課題である
- FedCodというプロトコルを提案し、コーディング機構でアイドル帯域を有効活用
- 実験で通信時間を最大62%短縮しつつ、トレーニング性能を維持する効果を確認

FedCodって、連合学習の通信効率を上げる新技術なんだって。62%も効率が上がるなんてすごいよね！私もその「FL」とやらをやってみたいな〜。最新技術ってワクワクするね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-12-31 02:05

- - -

### [Federated Learning with Workload Reduction through Partial Training of Client Models and Entropy-Based Data Selection](http://arxiv.org/abs/2501.00170)

**部分的クライアントモデルのトレーニングとエントロピーに基づくデータ選択による負荷軽減を実現した連合学習**

Hongrui Shi, Valentin Radu, Po Yang

- エッジデバイスの計算資源に応じた訓練負荷削減が必要である
- FedFT-EDSは部分モデルのファインチューニングと情報量重視のデータ選択を活用
- ユーザーデータ全てが有益ではないことを示し、データを半分に減少
- CIFAR-10/100で訓練時間を1/3に短縮しつつモデル性能が向上

デバイスの負担を減らしつつ性能を上げるってすごくね？エッジデバイス活用の新しい方法が広まりそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-12-30 22:47

- - -

### [Steppability-informed Quadrupedal Contact Planning through Deep Visual Search Heuristics](http://arxiv.org/abs/2501.00112)

**四足歩行ロボットの接触計画を深層視覚探索ヒューリスティックで情報化**

Max Asselmeier, Ye Zhao, Patricio A. Vela

- 足を置く場所の可否を画像空間で予測する方法を提案
- 合成データを活用し、多様で幾何学的なシミュレーションシーンを生成
- 既存のフットステッププランナーに統合し、複雑な環境での計画を改善
- オフライン・オンラインともに計画性能を実験的に検証

ロボットがどんな不安定な地形でもスイスイ歩けるようになるなんて、すごくカッコよくない？未来のロボットはまさに忍者みたいだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-12-30 19:19
