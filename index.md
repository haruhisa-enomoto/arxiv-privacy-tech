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

更新: 2024-11-27T04:24:47.453162

- - -

### [RealSeal: Revolutionizing Media Authentication with Real-Time Realism Scoring](http://arxiv.org/abs/2411.17684)

**RealSeal: リアルタイムなリアリズムスコアリングによるメディア認証の革命**

Bhaktipriya Radharapu, Harish Krishna

- ディープフェイクや改ざんメディアの脅威に対応するため、メディア認証の再考が必要
- 現実のコンテンツにウォーターマークを施す手法を提案し、従来手法の限界を克服
- コンテンツのリアリズムをリアルタイムで評価し、信頼性を高めるため画像メタデータに埋め込む
- 人間のリアリズムに関する推論と機械学習を組み合わせることで、デジタルメディアの新たな基準を確立

本当に最先端なテクノロジーって感じでワクワクするよね。画像にスコアを組み込む発想、めっちゃ面白そうだし、将来どう普及するか楽しみ！

**Comment:** Best Paper Award, Blue Sky Track at 26th ACM International Conference   on Multimodal Interaction, Nov 2024, San Jose, Costa Rica

**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-11-26 18:48

- - -

### [Synthetic Data Generation with LLM for Improved Depression Prediction](http://arxiv.org/abs/2411.17672)

**LLMを用いた合成データ生成によるうつ病予測の改善**

Andrea Kang, Jun Yu Chen, Zoe Lee-Youngzie, Shuhao Fu

- うつ病の自動検出は心理学と機械学習の交差領域で急成長中
- データのプライバシーと不足が問題で、合成データ生成を提案
- LLMを使用し感情分析と要約生成で合成データを作成
- 合成データは予測精度を向上させ、プライバシーも保護する

うつ病の検出って重要なテーマだし、この方法ってホントに興味深いよね！合成データでここまでプライバシーと精度のバランスが取れるんなら、もっといろんな分野でも応用が広がりそう！

**Comment:** 6 pages excluding references and appendix

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-26 18:31

- - -

### [Pre-training for Action Recognition with Automatically Generated Fractal Datasets](http://arxiv.org/abs/2411.17584)

**自動生成されたフラクタルデータセットを用いた行動認識のための事前学習**

Davyd Svyezhentsev, George Retsinas, Petros Maragos

- 合成データの活用で、画像モダリティの事前学習が特定視覚タスクを支援
- フラクタル幾何学に基づき、短い合成ビデオクリップを自動で大規模生成
- 実動画の重要な特性を特定しエミュレーションし、ドメインギャップを縮小
- 提案手法は既存データセットより優れた成果を示し、一部で標準手法超える

フラクタルを使って合成ビデオを作るなんてユニークだよね！合成データの可能性をもっと深掘りして、新しい視点からの活用が期待できそうだなって思ったよ。それに、この研究が未来のデータセット作成にどう影響するか興味津々だな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-26 16:51

- - -

### [Evolving Markov Chains: Unsupervised Mode Discovery and Recognition from Data Streams](http://arxiv.org/abs/2411.17528)

**進化するマルコフ連鎖：データストリームからの教師なしモード発見と認識**

Kutalmış Coşkun, Borahan Tümer, Bjarne C. Hiller, Martin Becker

- マルコフ連鎖は時間依存プロセスをモデル化するが、実世界のプロセスは時間とともに行動を変える
- この研究は、オンラインで効率的に遷移確率を追跡し、モードを自動的に発見し、モードスイッチを検出する方法を提案
- 提案されたEMCは、任意の順序で、トラッキングウィンドウを使用しない更新スキームに基づく
- 人間の活動認識や電動機の状態モニタリング、EEG測定による眼の状態認識での評価が示される

この論文、マルコフ連鎖を実時間で進化させるって、めっちゃ面白いよね！実際のデータでの適用も広そうだし、未来のライブデータ処理がもっと進化しそうでワクワクするね！

**Comment:** 20 pages, 8 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-26 15:42

- - -

### [BESTAnP: Bi-Step Efficient and Statistically Optimal Estimator for Acoustic-n-Point Problem](http://arxiv.org/abs/2411.17521)

**BESTAnP: 音響n点問題のための2ステップ効率的かつ統計的に最適な推定器**

Wenliang Sheng, Hongxu Zhao, Lingpeng Chen, Guangyang Zeng, Yunling Shao, Yuze Hong, Chao Yang, Ziyang Hong, Junfeng Wu

- 音響n点問題（AnP）は、2D前方視ソナーの姿勢を推定する課題
- 提案手法BESTAnPは平行移動と回転の推定を分離して行うアルゴリズム
- 距離のみの計測を用い平行移動、方位のみの計測と固有値分解で回転を推定
- シミュレーション実験で最先端モデル比で10倍速く、リアルタイム性能を保持

この手法って、速いだけじゃなくて、リソースが限られた環境でも使えるって凄いよね。ソナーベースのオドメトリーに組み込めるところも、実際の応用先が広がって面白そう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, **投稿日時:** 2024-11-26 15:30

- - -

### [RealTraj: Towards Real-World Pedestrian Trajectory Forecasting](http://arxiv.org/abs/2411.17376)

**RealTraj：実世界の歩行者軌跡予測に向けて**

Ryo Fujii, Hideo Saito, Ryo Hachiuma

- 従来の歩行者軌跡予測の課題は、認識エラーやデータ収集コスト、高価なID注釈にある
- RealTrajは、合成データで自己教師あり学習し実データで微調整して適用性を強化
- Det2TrajFormerにより追跡ノイズに不変で検出データに基づき予測性能を向上
- 高価なID注釈を減らし、限られた実データでモデルを微調整して最先端手法を上回る成果を示す

歩行者軌跡って日常にも関わってるから面白いね！RealTrajで未来のスマートシティがどんな風に変わるのかワクワクするなぁ。人の動きをうまく予測できれば、安全面の向上や新しいサービスにもつながりそうで、今後の展開が気になる！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-26 12:35

- - -

### [Knowledge-aware Evolutionary Graph Neural Architecture Search](http://arxiv.org/abs/2411.17339)

**知識対応進化的グラフニューラルネットワークアーキテクチャ探索**

Chao Wang, Jiaxuan Zhao, Lingling Li, Licheng Jiao, Fang Liu, Xu Liu, Shuyuan Yang

- 既存のGNASはゼロ知識から開始し、知識を活用せずに効率性に欠ける
- 本研究は既存知識を活用して新たなデータセットの探索を加速するKEGNASを提案
- KEGNASはナレッジモデルと深層多出力ガウスプロセスを用いて転送アーキテクチャを迅速に生成
- 実証研究ではKEGNASが他の進化的手法より精度を高めることを実証

この研究ってGNASの効率をすごく上げてるんだね！知識を使って最初から良いスタートを切るなんて賢い方法だよ～。かなり実用的でいろんな場面で使われそう！

**Comment:** This work has been accepted by Knowledge-Based Systems

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.NE, cs.AI, cs.LG, **投稿日時:** 2024-11-26 11:32

- - -

### [On the Generalization of Handwritten Text Recognition Models](http://arxiv.org/abs/2411.17332)

**手書き文字認識モデルの一般化に関する研究**

Carlos Garrido-Munoz, Jorge Calvo-Zaragoza

- 手書き文字認識（HTR）は、同分布内での誤りを減らすが、現実世界では前提が成り立たない
- ドメイン一般化の設定で、事前アクセスなしで未知データに一般化することを探求
- 336のケースを分析し、合成データの活用でモデルの一般化を研究
- テキストのドメイン間の差異が一般化の最も重要な要因で、誤差は70％のケースで10ポイント以下

手書き文字認識って奥が深いんだね！ドメインの違いを乗り越えて、現実世界での適用がもっと広がる未来が楽しみだな。合成データを使うアイデアも革新的で、どんな風に進化していくのかワクワクするね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-26 11:20

- - -

### [LHPF: Look back the History and Plan for the Future in Autonomous Driving](http://arxiv.org/abs/2411.17253)

**LHPF: 自動運転における過去を振り返り未来を計画する手法**

Sheng Wang, Yao Tian, Xiaodong Mei, Ge Sun, Jie Cheng, Fulong Ma, Pedro V. Sander, Junwei Liang

- 自動運転の意思決定と計画は安全性を反映し、効果的な計画が不可欠
- 現在の手法は過去と現在の計画を独立して評価し、計画の不連続性とエラー累積が課題
- LHPFは歴史的な計画情報を統合する模倣学習計画アルゴリズムを提案
- 実験でLHPFは既存の手法を上回り純粋な学習ベースで専門家を超えた性能を示す

この論文、過去の意図を活用する方法が興味深いね。将来の自動運転車がもっと人間らしい運転をするなんて、ちょっとワクワクしちゃうなー！



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.CV, **投稿日時:** 2024-11-26 09:30

- - -

### [Fault Localization from the Semantic Code Search Perspective](http://arxiv.org/abs/2411.17230)

**セマンティックコード検索視点からのフォールトローカリゼーション**

Yihao Qin, Shangwen Wang, Yan Lei, Zhuo Zhang, Bo Lin, Xin Peng, Liqian Chen, Xiaoguang Mao

- ソフトウェア開発は連続的な実装とデバッグの反復で、コード検索とフォールトローカリゼーションが重要
- コード検索は自然言語クエリによる精度が高く、フォールトローカリゼーションを改善できる可能性
- 提案されたCosFLは、問題の機能を自然言語で表現し、コード検索で関連プログラムを特定する手法
- CosFLはコード分析とLLMの能力を活用し、マルチグラニュラリティ戦略で精度を向上させる

ソフトウェアのバグ修正の未来がちょっと見えてきちゃうね！CosFLでバグの特定がすっごく効率的になりそうで、日本のエンジニアもこれに夢中になっちゃったりして～💕彼らの開発速度、めちゃくちゃ上がる予感！



**トピック:** [連合学習](fl), **カテゴリ:** cs.SE, **投稿日時:** 2024-11-26 08:52

- - -

### [Software Fault Localization Based on Multi-objective Feature Fusion and Deep Learning](http://arxiv.org/abs/2411.17101)

**多目的特徴融合とディープラーニングに基づくソフトウェア障害局在化**

Xiaolei Hu, Dongcheng Li, W. Eric Wong, Ya Zou

- ソフトウェア障害局在化は従来の方法では特徴の多様性が少なく精度が低い。
- マルチオブジェクト最適化とディープラーニングを組み合わせ、精度と効率を改善する新たな手法を提案。
- スペクトラム、変異、およびテキストベースの特徴を融合し、MLPとGRNを用いて局在化の精度と一般化性を向上。
- Defects4Jデータセットでの実験では、時間が78.2%短縮され、従来手法よりも94.2%精度向上。

提案された手法が処理時間を大幅に削減しつつも高精度を達成した点がすごいね！ディープラーニングと最適化でソフトウェアのバグ特定がさらに進化するなんて、未来の技術が楽しみだし、将来的にどんな応用が出てくるかワクワクするね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.SE, **投稿日時:** 2024-11-26 04:37

- - -

### [HOPE: Homomorphic Order-Preserving Encryption for Outsourced Databases -- A Stateless Approach](http://arxiv.org/abs/2411.17009)

**HOPE: 外部委託データベースのための準同型順序保存暗号 - 無状態アプローチ**

Baiqiang Wang, Dongfang Zhao

- 既存の順序保存暗号は状態を必要とするため、クライアント側に保存負担が発生
- HOPEは準同型暗号の加法的特性を活用し、クライアント側の保存や通信を不要にした
- 比較キー機構を導入し、暗号文の比較をランダム化した差分計算に変換して安全な範囲クエリが可能
- IND-OCPAモデル下でのセキュリティを証明し、他の先端技術と比較しても競争力のある実行性能を持つ

HOPEって名前もかわいいし、なんか革新的だよね！クライアントの負担軽減とセキュリティのバランスを取るのは、これからのデータベース管理にもっと必要になりそう。

**Comment:** arXiv admin note: substantial text overlap with arXiv:2406.03559

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-11-26 00:38

- - -

### [Towards Efficient Model-Heterogeneity Federated Learning for Large Models](http://arxiv.org/abs/2411.16796)

**大規模モデルのための効率的なモデル異質性連合学習に向けて**

Ruofan Jia, Weiying Xie, Jie Lei, Haonan Qin, Jitao Ma, Leyuan Fang

- エッジコンピューティングにおける大規模モデルの連合学習は重要だが、リソース制約とクライアントの異質性が課題。
- モデル異質性連合学習（MHFL）のための革新的なファインチューニングフレームワーク、HeteroTuneを導入。
- FedAdapterという多枝クロスモデルアグリゲーターを用いた新しいパラメーター効率的なファインチューニング（PEFT）構造を提案。
- 提案手法は計算と通信のオーバーヘッドを大幅に削減し、幅広い大規模モデルのファインチューニングに適用可能。

この研究、とっても面白そう！いろんな異質なモデルを賢くつなぐって、AI界のバーテンダーみたいじゃない？これがうまくいったら、もっと多様なAIが早く動かせるし、未来の可能性を感じるよね。

**Comment:** 8pages, 5figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, 68T07, I.2.11, **投稿日時:** 2024-11-25 09:58

- - -

### [Revisiting DDIM Inversion for Controlling Defect Generation by Disentangling the Background](http://arxiv.org/abs/2411.16767)

**DDIM反転を再訪して背景を分離することで欠陥生成を制御する**

Youngjae Cho, Gwangyeol Kim, Sirojbek Safarov, Seongdeok Bang, Jaewoo Park

- 異常検知では正常データに比べ異常データが希少で、深層学習の特徴抽出が困難
- 合成データ利用はデータ不均衡を解消できるが、背景と欠陥の関連を考慮していない
- 本研究では背景と欠陥の関係をモデル化し、背景が欠陥に影響しないよう分離を提案
- 本手法で背景が不変な状態で欠陥生成が理論的に可能であり、実験で効果を実証

異常データが少ないのって大変だけど、背景と欠陥をうまく分けられたらめちゃくちゃ役立ちそうだね！実験で効果を示せたのもすごいから、これからもっと研究が進むといいな。

**Comment:** 10 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-11-25 04:05

- - -

### [AnySynth: Harnessing the Power of Image Synthetic Data Generation for Generalized Vision-Language Tasks](http://arxiv.org/abs/2411.16749)

**AnySynth: 汎用ビジョン・ラングイッジ課題のための画像合成データ生成の活用**

You Li, Fan Ma, Yi Yang

- 合成データは、手動データ収集を減らし、モデルの一般化を改善
- AnySynthは、柔軟で制御可能な合成データ生成フレームワークを提案
- タスク固有のレイアウト生成と統一制御型画像生成モジュールを統合
- 各種タスクでの性能改善を確認し、汎用性と効果を実証

合成データの力を活かすAnySynth、すごく面白いね！ジョブごとにデータ整えなくてもいいって、研究者にとって画期的だなぁ。どんな未来のアプリが誕生するのか、とっても楽しみだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-24 04:49

- - -

### [Federated Learning in Chemical Engineering: A Tutorial on a Framework for Privacy-Preserving Collaboration Across Distributed Data Sources](http://arxiv.org/abs/2411.16737)

**化学工学における連合学習: 分散データソース間のプライバシーを保護したコラボレーションのフレームワークに関するチュートリアル**

Siddhant Dutta, Iago Leal de Freitas, Pedro Maciel Xavier, Claudio Miceli de Farias, David Esteban Bernal Neira

- 連合学習はデータプライバシーを守りつつモデルを共同トレーニングする手法として注目
- 化学工学での応用例は製造最適化、マルチモーダルデータ統合、薬発見などに及ぶ
- チュートリアルでは$\texttt{Flower}$と$\texttt{TensorFlow Federated}$を使用し、実践的手法を紹介
- 連合学習は中央集権的学習と比較して複雑で異質なデータでも性能を維持または改善

うわー、化学工学でも連合学習が活かせるんだね！プライバシーを守りつつ、色々なデータを使えるのが未来っぽいし、すごくワクワクするね。今後の化学産業がどう発展するか楽しみ～！

**Comment:** 46 Pages, 8 figures, Under review in ACS Industrial & Engineering   Chemistry Research Journal

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.NE, **投稿日時:** 2024-11-23 13:16

- - -

### [Learn2Synth: Learning Optimal Data Synthesis Using Hypergradients](http://arxiv.org/abs/2411.16719)

**Learn2Synth: ハイパーグラデントを用いた最適なデータ合成学習**

Xiaoling Hu, Oula Puonti, Juan Eugenio Iglesias, Bruce Fischl, Yael Balbastre

- 合成によるドメインランダム化は、入力画像のドメインに対して偏りのないネットワークを訓練する強力な戦略
- 手動で合成画像のパラメータ調整を行う代わりに、Learn2Synthでは少量のラベル付き実データを用いて合成パラメータを学習
- 本手法は実データを用いずに、合成データとネットワークの最適なラベルマップを確保
- 合成画像のパラメトリックおよびノンパラメトリックな拡張により、セグメンテーション性能を向上

合成データを使って実データの影響を抑えつつ、性能を高めるってすごく画期的だよね！実験で効果が示されたのも興味深いな～。どんなデータセットでも応用できそうだから、実生活での活用が楽しみ！

**Comment:** 14 pages, 5 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-11-23 00:52
