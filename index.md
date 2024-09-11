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

更新: 2024-09-11T04:23:19.382062

- - -

### [Data Collection-free Masked Video Modeling](http://arxiv.org/abs/2409.06665)

**データ収集不要なマスクビデオモデリング**

Yuchi Ishikawa, Masayoshi Kondo, Yoshimitsu Aoki

- 動画トランスフォーマの事前学習には大量のデータが必要で、コストやプライバシー問題が課題
- 合成データのみの事前学習にも難点がある
- 静止画像から疑似モーションビデオを生成するPMFモジュールを提案
- この手法は合成画像にも適用可能で、データ収集のコストと問題を解消

PMFモジュールを使うと静止画像だけで効果的な動画学習ができるなんてすごい！今後の動画解析技術がもっと進化する予感がするね。

**Comment:** ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-10 17:34

- - -

### [Exploring Italian sentence embeddings properties through multi-tasking](http://arxiv.org/abs/2409.06622)

**マルチタスクによるイタリア語文埋め込み特性の探究**

Vivi Nastase, Giuseppe Samo, Chunyang Jiang, Paola Merlo

- 既存の大規模言語モデル(LLM)がどの程度抽象的な言語情報をイタリア語で符号化しているか調査
- 大規模な合成データを利用して、事前学習済み言語モデルが特定の統語的・意味的情報を符号化するかを研究
- 文章埋め込みを圧縮し、特定のタスクに関連する情報が含まれる表現としてモデル化を試みる
- 性能とエラー分析により、タスク間で文章埋め込みが異なる方法で符号化されていることを示唆

事前学習済みの埋め込みが必ずしも統語的や意味的な役割を適切に符号化していないってことで、使い方次第な部分が多そうで面白いよね。これからのLLMの可能性にも注目だね！

**Comment:** 9 pages, 9 figures, 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, 68T50, I.2.7, **投稿日時:** 2024-09-10 16:22

- - -

### [Exploring syntactic information in sentence embeddings through multilingual subject-verb agreement](http://arxiv.org/abs/2409.06567)

**多言語の主語-動詞一致を通じた文埋め込みにおける統語情報の探求**

Vivi Nastase, Chunyang Jiang, Giuseppe Samo, Paola Merlo

- 多言語事前学習モデルが抽象的な言語表現をどの程度捉えるかを調査
- 特定の特性を持った合成データを大規模に開発し、文の表現を研究
- Blackbird Language Matrices (BLM) を使用し、多言語間での主語-動詞一致に焦点
- 事前学習モデルには言語固有の違いがあり、統語構造が共有されないことを示す

多言語のモデルってやっぱり難しいんだね。でも、新しい分析手法で文の構造が分かるようになるなんて未来が楽しみ！

**Comment:** 11 pages, 5 tables, 5 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, 68T50, I.2.7, **投稿日時:** 2024-09-10 14:58

- - -

### [Advancing Hybrid Defense for Byzantine Attacks in Federated Learning](http://arxiv.org/abs/2409.06474)

**連合学習におけるビザンチン攻撃へのハイブリッド防御の進展**

Kai Yue, Richeng Jin, Chau-Wai Wong, Huaiyu Dai

- 連合学習は複数のクライアントがデータを共有せずに共同でグローバルモデルを訓練
- 攻撃者戦略や悪意のあるクライアント数を事前に知らないFLシナリオでの攻撃耐性を調査
- 状況に応じた防御選択により、大量の毒性更新があってもサーバーの頑強性を立証
- 新しいTrapsetter攻撃は既存のFL防御をすり抜け、モデル精度をさらに8-10%低下

新しい防御メカニズムがくしゃみしないで強力ってすごいよね！まだまだ課題はいろいろあるけど、この研究を基にもっと安全な連合学習ができるようになるかもね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-09-10 13:04

- - -

### [HexaCoder: Secure Code Generation via Oracle-Guided Synthetic Training Data](http://arxiv.org/abs/2409.06446)

**HexaCoder: オラクル指導合成訓練データによる安全なコード生成**

Hossein Hajipour, Lea Schönherr, Thorsten Holz, Mario Fritz

- LLMが生成するコードには深刻な脆弱性が多いという問題に対処
- HexaCoderは安全なコードを自動合成し、訓練データの準備を軽減
- オラクルが脆弱性を特定し、最先端のLLMが修正コードを生成
- 提案手法は、生成される脆弱なコードの量を最大85%削減

これ、すごく面白そうじゃない？これからもっと安全なコード生成ができるようになるなんて、未来が楽しみ！

**Comment:** 24 pages, 16 tables, 8 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.AI, cs.CL, cs.LG, cs.SE, **投稿日時:** 2024-09-10 12:01

- - -

### [A Pervasive, Efficient and Private Future: Realizing Privacy-Preserving Machine Learning Through Hybrid Homomorphic Encryption](http://arxiv.org/abs/2409.06422)

**遍在的で効率的かつプライバシー保護の未来: ハイブリッド準同型暗号を用いたプライバシー保護機械学習の実現**

Khoa Nguyen, Mindaugas Budzys, Eugene Frimpong, Tanveer Khan, Antonis Michalas

- 機械学習(ML)は近年データサイエンスで重要な分野だが、プライバシーリスクが懸念される
- プライバシー保護機械学習(PPML)として準同型暗号(HE)が用いられるも非効率で課題
- ハイブリッド準同型暗号(HHE)が代替手法として提案され、HEの非効率性を克服
- HHEを用いたPPMLプロトコルを提案し、心臓病分類への応用で実証

これ、心臓病の分類にHHEを使うとかすごいね！エッジデバイスで効率的にプライバシー保護するなんてこれからもっと注目されそう！

**Comment:** Accepted in The 22nd IEEE International Conference on Dependable,   Autonomic and Secure Computing (DASC 2024)

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-10 11:04

- - -

### [Compute-Update Federated Learning: A Lattice Coding Approach](http://arxiv.org/abs/2409.06343)

**計算更新連合学習：格子符号化アプローチ**

Seyed Mohammad Azimi-Abarghouyi, Lav R. Varshney

- 無線通信を介した計算を可能にする新たな連合学習フレームワークを提案
- 格子符号を使い、モデルパラメータを量子化してデバイス間の干渉を活用
- サーバー上で量子化モデルパラメータの整数の組み合わせを格子点として集約する受信構造を提案
- 提案手法がさまざまなパラメータで一貫した学習精度を提供し、他の無線通信手法を上回ることを実証

格子符号化を使ってエラー訂正しながら連合学習するなんて、面白そう！通信状態が変わっても一貫して精度がいいってすごいね！

**Comment:** Extended version of the preprint available at arXiv:2403.01023

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, cs.AI, cs.LG, math.IT, **投稿日時:** 2024-09-10 08:52

- - -

### [Rate-Constrained Quantization for Communication-Efficient Federated Learning](http://arxiv.org/abs/2409.06319)

**通信効率の高い連合学習のためのレート制約付き量子化**

Shayan Mohajer Hamidi, Ali Bereyhi

- 連合学習の通信コストを軽減するために量子化を使用する
- 量子化されたローカルパラメータはヒュフマン符号などのエントロピー符号化技術でさらに圧縮
- 新たな量子化FLフレームワーク「RC-FED」を提案し、信号忠実度とデータレートの両方を制約
- RC-FEDは、最適化を通じて量子化歪みを最小化しつつ通信コスト目標を下回ることを実現

量子化フレームワークであるRC-FEDの提案とか、通信コストを最適化しつつ精度も保つのめっちゃ面白そう！他の手法と比較してもパフォーマンスが良いなら期待できるよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-09-10 08:22

- - -

### [The Black-Box Simulation Barrier Persists in a Fully Quantum World](http://arxiv.org/abs/2409.06317)

**ブラックボックスシミュレーションの障壁は完全な量子世界でも持続する**

Nai-Hui Chia, Kai-Min Chung, Xiao Liang, Jiahui Liu

- ゼロ知識プロトコル(ZK)は基本的な重要性と多様性のために広く研究されている
- ポスト量子設定で常時ラウンドのブラックボックスZKはNPがBQPに含まれない限り不可能
- 量子通信は約束と対話的議論のラウンド圧縮を可能にしてきた
- 対象言語がBQPに含まれる場合のみ常時ラウンドの完全量子BBZKが許容されると証明

量子コンピューティングがZKプロトコル全体を根本的に変える可能性が面白そうだよね。さらに、この研究が新しい量子プロトコルのデザインに役立ちそうでワクワクする！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** quant-ph, cs.CR, **投稿日時:** 2024-09-10 08:17

- - -

### [On Applying Bandit Algorithm to Fault Localization Techniques](http://arxiv.org/abs/2409.06268)

**バンディットアルゴリズムの故障位置特定技術への適用について**

Masato Nakao, Kensei Hamamoto, Masateru Tsunoda, Amjed Tahir, Koji Toda, Akito Monden, Keitaro Nakasai, Kenichi Matsumoto

- 開発者は高性能な故障位置特定（FL）技術を選ぶ必要がある
- 伝統的な方法はデバッグ前に一つのFL技術を選ぶこと
- 本研究はデバッグ中に動的により良いFL技術を選択する新しい方法を提案
- 新しいアプローチは動的選択により性能向上が期待される

バンディットアルゴリズム使うのってなんかゲームみたいで面白そうじゃない？この新しいアプローチでデバッグがもっと楽になるといいね！

**Comment:** 2 pages, 2 figures, 1 table

**トピック:** [連合学習](fl), **カテゴリ:** cs.SE, **投稿日時:** 2024-09-10 07:15

- - -

### [Test-Time Certifiable Self-Supervision to Bridge the Sim2Real Gap in Event-Based Satellite Pose Estimation](http://arxiv.org/abs/2409.06240)

**イベントベースの衛星姿勢推定におけるSim2Realギャップを埋めるためのテスト時認証可能な自己教師システム**

Mohsi Jawaid, Rajat Talak, Yasir Latif, Luca Carlone, Tat-Jun Chin

- データが不足しているため、合成データで訓練する必要がありSim2Realギャップが発生する
- 照明条件の変化が大きな原因であり、商用イベントセンサーにはノイズや不均一なイベント密度が生じる
- 論文では、テスト時に自己教師付きと認証モジュールを活用したスキームを提案
- 提案手法が確立されたテスト時適応スキームを上回る成果を示している

自己教師付きの方法で姿勢推定が改善するのってすごくない！？宇宙空間での実応用がどこまで進むのか、これからが楽しみだね。

**Comment:** This work has been accepted for publication at IEEE/RSJ International   Conference on Intelligent Robots and Systems (IROS 2024). Copyright may be   transferred without notice, after which this version may no longer be   accessible

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.RO, **投稿日時:** 2024-09-10 06:17

- - -

### [Conditional Encryption with Applications to Secure Personalized Password Typo Correction](http://arxiv.org/abs/2409.06128)

**条件付き暗号化と安全なパーソナライズドパスワードタイポ修正への応用**

Mohammad Hassan Ameri, Jeremiah Blocki

- 条件付き暗号化スキームは公開鍵暗号に追加する概念である
- 条件付き暗号化の具体的で効率的な構築を提案し、パスワードタイポ修正に利用
- Paillier部分準同型暗号とShamir Secret Sharingを使用した実用的な構築
- C++ライブラリを実装し、TypTopシステムのセキュリティを向上させ性能を評価

条件付き暗号化でパスワードタイポ修正がもっと安心になりそうだね。TypTopの更新展開も楽しみ！

**Comment:** Full version of CCS 2024 paper with the same title

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-10 00:49

- - -

### [Contrastive Federated Learning with Tabular Data Silos](http://arxiv.org/abs/2409.06123)

**タブラー形式データサイロを用いた対照的連合学習**

Achmad Ginanjar, Xue Li, Wen Hua

- データサイロからの学習は、ラベル無し、独立非同分布(NIID)、垂直分割等の課題がある
- プライバシー保護が課題を複雑化し、協力的な作業の意欲を阻害
- 対照学習を用いてラベルコスト問題に対処するが、タブラー形式には適用困難
- 半教師付き対照的連合学習(CFL)を提案し、精度面での改善を実証

対照的連合学習がこれまでの方法より効果的だなんて、未来のデータ解析がもっと楽しみになるね！クライアント環境の複雑さも克服できるところがポイント高いね。

**Comment:** 18 Pages. Was submitted on Artificial Intelligence Journal, Jan 29,   2024, ARTINT-D-24-00098

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, 68A00, I.1.1, **投稿日時:** 2024-09-10 00:24

- - -

### [MLLM-FL: Multimodal Large Language Model Assisted Federated Learning on Heterogeneous and Long-tailed Data](http://arxiv.org/abs/2409.06067)

**MLLM-FL: 異質で長尾分布データにおけるマルチモーダル大規模言語モデルを活用した連合学習**

Jianyi Zhang, Hao Frank Yang, Ang Li, Xin Guo, Pu Wang, Haiming Wang, Yiran Chen, Hai Li

- 異なるクライアント間のデータの異質性により発生するパフォーマンス低下に焦点
- MLLMをサーバー側に導入し、異質性や長尾分布の課題に対応
- オープンソースデータと強力なサーバー計算資源を活用し、プライバシー漏洩や端末負担増加を回避
- 実験評価により、データの異質性や長尾分布下でのパフォーマンス向上を確認

MLLM使うとかめっちゃ面白そう！データ多様でもちゃんと学習できるってすごいなぁ。実際のアプリケーションでどう活かせるんだろうね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, **投稿日時:** 2024-09-09 21:04

- - -

### [Analyzing Tumors by Synthesis](http://arxiv.org/abs/2409.06035)

**合成による腫瘍の解析**

Qi Chen, Yuxiang Lai, Xiaoxi Chen, Qixin Hu, Alan Yuille, Zongwei Zhou

- CTスキャンの腫瘍データの希少性がAI開発の障害となる
- 腫瘍合成はAI訓練のための合成腫瘍を生成し、この問題を解決する
- モデリングベースと学習ベースの2つの合成データアプローチが存在する
- 合成腫瘍を使用したAIは、リアルデータを使用したAIと同等かそれ以上の性能を達成

腫瘍合成が進むことで、AIが本当に医療現場で活躍しそう！患者のプライバシーも守りつつ、信頼性が高いAIがどんどん広がるね。

**Comment:** Accepted as a chapter in the Springer Book: "Generative Machine   Learning Models in Medical Image Computing."

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-09-09 19:51

- - -

### [FLoRA: Federated Fine-Tuning Large Language Models with Heterogeneous Low-Rank Adaptations](http://arxiv.org/abs/2409.05976)

**FLoRA: 異質な低ランク適応による連合型大規模言語モデルの微調整**

Ziyao Wang, Zheyu Shen, Yexiao He, Guoheng Sun, Hongyi Wang, Lingjuan Lyu, Ang Li

- LLMの急速な発展がAIの進歩を促進し、連合学習によりプライバシーを保護しながら微調整を可能に
- クライアントのリソースに制約があるため、既存の低ランク適応手法は効果が低下
- FLORAという新しいアプローチを提案、スタッキングベースの集約方法で異質なLoRAアダプタ対応を実現
- 実験により、同質および異質の設定の両方で既存手法を上回る性能を示す

FLORAって、何だか未来的でワクワクするよね！プライバシーと効率性を両立できるなんて素敵✨



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-09-09 18:21
