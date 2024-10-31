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

更新: 2024-10-31T04:24:21.748626

- - -

### [(FL): Overcoming Few Labels in Federated Semi-Supervised Learning](http://arxiv.org/abs/2410.23227)

**（FL）$^2$: 連合半教師あり学習におけるラベル不足の克服**

Seungjoo Lee, Thanh-Long V. Le, Jaemin Shin, Sung-Ju Lee

- 連合学習（FL）はクライアントのプライバシーを保ちつつ、正確なグローバルモデルを訓練する方法
- 従来のFLはクライアントにラベル付きデータがあることを前提とするが、現実ではそうでないことが多い
- 提案手法（FL）$^2$は、ラベルなしクライアントのための鋭敏性意識の一貫した正則化を使用
- クライアント特有の適応的閾値設定と学習状況認識型の集約を導入し、性能を向上

ラベルが少ないときの連合学習を改善する方法って、新しいね！クライアントごとに調整できるのはすごく柔軟で役立ちそうだよね。どんなデータでも対応できそうだから、未来のデータ学習ってもっと楽しくなる予感！

**Comment:** Accepted to NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-30 17:15

- - -

### [Directional anomaly detection](http://arxiv.org/abs/2410.23158)

**方向性を考慮した異常検出**

Oliver Urs Lenz, Matthijs van Leeuwen

- 従来の異常検出は正常データと異なるものを問題視
- 特に高い値や低い値の異常に注目することがある
- ランプ距離と符号付き距離の2つの非対称距離を提案
- シミュレーションと実データでの評価で、ランプ距離が絶対距離より優れる

方向性を考慮した異常検出って新しい視点だね！特にランプ距離が実際のデータで効果を発揮するのは、実用面でも期待大だと思うよ。符号付き距離はちょっと実データには弱いけど、これからの改善、楽しみだなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-30 16:11

- - -

### [Federated Learning under Periodic Client Participation and Heterogeneous Data: A New Communication-Efficient Algorithm and Analysis](http://arxiv.org/abs/2410.23131)

**周期的なクライアント参加と異質データ下での連合学習: 新たな通信効率の良いアルゴリズムと分析**

Michael Crawshaw, Mingrui Liu

- 従来の連合学習はクライアントが常時参加する前提だが、現実では難しい
- 新アルゴリズム「Amplified SCAFFOLD」は非凸最適化で通信量とデータの差を改善
- 提案手法は通信ラウンドを減らしデータ異質性に強く、以前の手法より効率的
- 実験では合成データと現実データで、このアルゴリズムの有効性を確認

これ、連合学習の実用性を高めるポイントが満載で、すごく興味惹かれる内容だね！特に新アルゴリズムで通信が効率的になって、データの違いにも対応できるなんて、これからの技術に期待しちゃう！どんな応用が実現できるんだろう、未来が楽しみだね！

**Comment:** Neurips 2024

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-10-30 15:41

- - -

### [Why Gradient Subspace? Identifying and Mitigating LoRA's Bottlenecks in Federated Fine-Tuning of Large Language Models](http://arxiv.org/abs/2410.23111)

**なぜ勾配サブスペースか？大規模言語モデルの連合ファインチューニングにおけるLoRAのボトルネックの特定と緩和**

Navyansh Mahla, Ganesh Ramakrishnan

- 大規模言語モデルの連合学習にはプライバシー問題が伴うが、LoRAを使う従来手法では効率が限られる
- LoRAの低ランク行列における制約が、連合設定でのファインチューニングの効果を妨げる
- 従来のLoRAに比べ直接的な重み平均が優れた性能を示し、LoRAの非効率性を露呈
- GaLoreなどの低ランク勾配ベースの最適化手法がLoRAより効果的であると評価

LoRAに依存しない新しい連合学習の方法、効率よく学べそう！未来のアプリケーションでプライバシーも守れるなら安心して使えそうだね。ワクワク！

**Comment:** 24 pages, 10 figures, pre-print

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-30 15:23

- - -

### [Automated Image-Based Identification and Consistent Classification of Fire Patterns with Quantitative Shape Analysis and Spatial Location Identification](http://arxiv.org/abs/2410.23105)

**火災パターンの自動画像識別と定量的形状分析および空間位置同定による一貫した分類**

Pengkun Liu, Shuna Ni, Stanislav I. Stoliarov, Pingbo Tang

- 火災パターンの伝統的な分類は目視に頼り、主観的解釈に依存することが多い
- 提案されたフレームワークは、計算分析と専門家の知見を融合し一貫性を提供
- ランダムフォレストモデルにより、火災パターンの形状を数値的に分類する手法を用いる
- 合成データでは93%、実際のデータでは83%の精度があることが実証された

火災現場の解析が技術の進歩でこんなに正確になるなんてすごい！これからは事故原因究明がもっと迅速で信頼できるものになりそうでワクワクするね。それに、研究者と技術のコラボも面白いポイントだと思うな〜。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.HC, **投稿日時:** 2024-10-30 15:15

- - -

### [Private Synthetic Text Generation with Diffusion Models](http://arxiv.org/abs/2410.22971)

**拡散モデルを用いたプライベートな合成テキスト生成**

Sebastian Ochs, Ivan Habernal

- 拡散モデルは、合成テキスト生成で自己回帰型LLMs並みの性能を持つ
- 差分プライバシーを活用した合成データ生成には十分な証拠がまだない
- 既存のLLMsによる合成テキスト生成は差分プライバシー保証を破る可能性がある
- プライバシー環境下では、オープンソースLLMsが拡散モデルより優れていると判明

拡散モデルって本当すごいのかもって思ったけど、意外とLLMsの方が強かったんだね！オープンソースで、いっぱい実験してくれるのありがたいから、もっと研究進むといいな〜。



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-30 12:38

- - -

### [A Study of Secure Algorithms for Vertical Federated Learning: Take Secure Logistic Regression as an Example](http://arxiv.org/abs/2410.22960)

**縦型連合学習のための安全なアルゴリズムの研究：安全なロジスティック回帰を例に**

Huan-Chih Wang, Ja-Ling Wu

- ビッグデータ時代では、機械学習を使ったサービスが増えたが、データ収集のコストが高い
- 他社データとの連携でモデルの性能向上が可能だが、法律で制限される場合がある
- データ共有とプライバシー漏洩防止のバランスが重要な課題
- 縦型連合学習で暗号化領域での安全なモデル訓練を行い、プライバシー問題を解決

データを他社と共有しつつも安全に扱う方法ってめちゃくちゃ大事だよね！プライバシーを保護しながら、縦型連合学習でどうやって安全にモデルを訓練するのか、もっと知りたいな〜！

**Comment:** accepted by the 20th International Conference on Security &   Management (SAM 2021)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-10-30 12:17

- - -

### [CopRA: A Progressive LoRA Training Strategy](http://arxiv.org/abs/2410.22911)

**CopRA: プログレッシブなLoRAトレーニング戦略**

Zhan Zhuang, Xiequn Wang, Yulong Zhang, Wei Li, Yu Zhang, Ying Wei

- LoRAは基盤モデルを効率よくファインチューニングする技術だが、初期設定近くの局所解に収束しやすい
- 提案手法CopRAはランダムな層の除去とLoRAパラメータのShapley値最適化を組み合わせる
- パラメータの線形モード接続を示し、モデル統合の効率化を可能にすることが実験で示された
- Shapley値の最適化で、特にプルーニングタスクにおいて優れた性能を発揮する

CopRAのアイデアって面白い！ランダムな要素を取り入れて、新しい道を切り拓いてるよね。これがちゃんと機能すれば、連合学習やマルチタスク学習に革命が起きるかも！？

**Comment:** Published in UniReps Workshop (Extended Abstract Track), NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-30 11:07

- - -

### [Federated UCBVI: Communication-Efficient Federated Regret Minimization with Heterogeneous Agents](http://arxiv.org/abs/2410.22908)

**連合UCBVI: 異種エージェントによる効率的な連合後悔最小化**

Safwan Labbi, Daniil Tiapkin, Lorenzo Mancini, Paul Mangold, Eric Moulines

- Federated UCBVI（Fed-UCBVI）は、連合学習の枠組みに特化したUCBVIアルゴリズムの新しい拡張版
- Fed-UCBVIの後悔が、状態数、行動数、エピソードの長さ、エージェント数に応じてスケール
- 単一のエージェントの場合、この上限はミニマックスの下限と一致し、多エージェントでは線形的な速度向上
- 複数エージェントの方が通信複雑性が増すが、Fed-UCBVIはわずかしか増加しない

この論文、エージェント数が増えても通信量がほとんど変わらないってところがすごいよね！将来の連合学習の応用範囲が広がりそうな予感がする〜。また、異種エージェントの考え方が他の研究にも応用できそうで、面白そう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-10-30 11:05

- - -

### [Augmenting Polish Automatic Speech Recognition System With Synthetic Data](http://arxiv.org/abs/2410.22903)

**ポーランド語の音声認識システムを合成データで拡張する**

Łukasz Bondaruk, Jakub Kubiak, Mateusz Czyżnikiewicz

- 合成データを利用してポーランド語音声認識システムを改善する研究
- Voiceboxを基にした音声合成パイプラインを使用
- ConformerとWhisperモデルを合成データで強化
- 合成音声を追加することで認識結果が大幅に向上することを確認

ポーランド語の音声認識を合成データで改善しちゃうなんてすごいよね！技術の組み合わせで性能がアップする話が面白いし、これから音声AIの可能性がどんどん広がっていきそうだね！



**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.SD, **投稿日時:** 2024-10-30 11:02

- - -

### [Towards Robust and Efficient Federated Low-Rank Adaptation with Heterogeneous Clients](http://arxiv.org/abs/2410.22815)

**異質なクライアントに対するロバストで効率的なフェデレーテッド低ランク適応の実現に向けて**

Jabin Koo, Minwoo Jang, Jungseul Ok

- 連合学習で大規模言語モデルのファインチューニングの通信オーバーヘッドが課題
- LoRAは低ランク適応策だが、連合学習での集約の不一致で複雑化
- LoRA-A2を導入し、低ランクとデータ異質性の中でも性能を維持することを実証
- 通信効率を向上させ、資源が限られた環境での大規模言語モデルの実用的な展開を可能に

LoRA-A2ってすごいじゃん！異種データでのパフォーマンス維持ってホントに大変そうだけど、それを実現できるなんて感動しちゃう。しかも通信が軽く済むとか、これどんどん使っていい感じ♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-10-30 08:48

- - -

### [Universality of the  Pathway in Avoiding Model Collapse](http://arxiv.org/abs/2410.22812)

**モデル崩壊を避ける$π^2/6$経路の普遍性**

Apratim Dey, David Donoho

- モデル崩壊とは、合成データで訓練したモデルが劣化する現象である
- 実データを使用し続ける増強ワークフローでモデル崩壊を回避可能
- 古典的な線形回帰でのテストリスクが$π^2/6$で境界づけされることを示した
- 提案する枠組みで多様なワークフローを比較評価可能

「モデル崩壊」を避けるアイディアが数学的にしっかり証明されてるのがすごいね！これを応用すれば、今後もっといっぱいのモデルに適用できちゃうかも！？びっくりだよね～シンプルなガウス過程で評価できるなんて便利だし、面白そう！

**Comment:** 30 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.ET, math.ST, stat.ML, stat.TH, **投稿日時:** 2024-10-30 08:44

- - -

### [Analysis of Classifier Training on Synthetic Data for Cross-Domain Datasets](http://arxiv.org/abs/2410.22748)

**合成データを用いたクロスドメインデータセットの分類器訓練の分析**

Andoni Cortés, Clemente Rodríguez, Gorka Velez, Javier Barandiarán, Marcos Nieto

- ディープラーニングには大量の学習データが必要で、その収集は時間・労力がかかる。
- 合成データの利用により、多様な検出器のトレーニングを効果的に行える。
- 本研究では合成データによるカメラベースの交通標識認識システムを検証。
- 合成データによるアプローチは、多くの場合実データに比べ10%の精度向上を示す。

合成データを使った訓練っておもしろいよね！写真を集める手間が減るから、もっといろんな分野で活用される未来が見えるよ。運転支援システムにも役立ちそうでワクワクするなぁ。

**Comment:** 10 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-30 07:11

- - -

### [Exactly Minimax-Optimal Locally Differentially Private Sampling](http://arxiv.org/abs/2410.22699)

**ローカル差分プライバシーにおけるサンプリング問題の厳密なミニマックス最適化**

Hyun-Young Park, Shahab Asoodeh, Si-Hyeon Lee

- ローカル差分プライバシーの下でのサンプリング問題は生成モデルへの応用が期待される
- f-ダイバージェンスを用いてプライバシー-ユーティリティトレードオフ（PUT）をミニマックス的に定義
- 有限および連続データ空間におけるPUTを正確に特徴付け、すべてのf-ダイバージェンスに対して最適なサンプリングメカニズムを提案
- 数値実験により、理論的および実証的なユーティリティの面で提案手法がベースラインを上回ることを示した

プライバシーを保ちながらも、実用的な性能を最大限引き出そうとするアプローチが興味深いね！こんな技術、関係する分野でどんなふうに花開くのかな？ワクワクするね！

**Comment:** 32 pages and 7 figures. Accepted by NeurIPS 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-30 05:13

- - -

### [Byzantine-Robust Federated Learning: An Overview With Focus on Developing Sybil-based Attacks to Backdoor Augmented Secure Aggregation Protocols](http://arxiv.org/abs/2410.22680)

**ビザンチン耐性連合学習:シビル攻撃によるバックドア増強セキュア集約プロトコルの概要**

Atharv Deshmukh

- 連合学習は複数のクライアントが協力してプライベートデータでモデルを訓練するが、ビザンチン攻撃に弱い。
- 既存の防御手法を網羅的に整理し、連合学習の耐性あるプロトコルRoFLの解析を行う。
- シビル攻撃を利用したRoFLの脆弱性を突く新たな攻撃手法を提案。
- 攻撃実装の詳細とRoFL及び耐ビザンチンフレームワーク改善の方向性を示す。

ビザンチン攻撃とか、なんだかかっこいい名前だよね！でも、そのせいでちょっと怖い部分もあるけど、この論文がどんな改善をもたらすのか楽しみ。連合学習を安全にするなんて、未来の機械学習をもっとワクワクするものにしてくれそうだね！

**Comment:** 16 pages, 4 figures, 1 appendix

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-30 04:20

- - -

### [Calibrating Practical Privacy Risks for Differentially Private Machine Learning](http://arxiv.org/abs/2410.22673)

**差分プライバシー機械学習における実用的プライバシーリスクの調整**

Yuechun Gu, Keke Chen

- 差分プライバシーの理論的指標$\epsilon$は、モデルやデータセットによって実用的解釈が複雑である。
- LiRA攻撃成功率(ASR)は、$\epsilon$設定が同じでもデータセットやモデルにより変動し実世界のリスク指標となる。
- プライバシーに敏感な特徴を抑えることでASRを低下させ、データ有用性を損なわずに柔軟なプライバシー設定が可能に。
- SHAPとLIMEを使い特徴感度を評価し、特徴をマスクする戦略がデータセットのプライバシーリスクを軽減。

プライバシーリスクをこんなにしっかり考えてるなんて、すごいなぁ。データの便利さと安全性を両立させる方法が、未来の技術の鍵かもね！高校のレポートにも使える知識かもしれないから、詳しく見てみたいな。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-30 03:52

- - -

### [FT-PrivacyScore: Personalized Privacy Scoring Service for Machine Learning Participation](http://arxiv.org/abs/2410.22651)

**FT-PrivacyScore: 機械学習参加のための個別化プライバシースコアサービス**

Yuechun Gu, Jiajie He, Keke Chen

- プライバシー損失を定量化する手法は精度に影響を与える
- 多くの業界や研究では制御されたデータアクセスが主流
- 個別のプライバシーリスクを事前評価する定量的手段がない
- FT-PrivacyScoreで効率的にプライバシーリスクを推定可能

プライバシーを守りつつ機械学習に参加できるなんてすごいね！もしこれがもっと広まったら、みんなのデータ活用がもっと安全に行えそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-30 02:41

- - -

### [FISC: Federated Domain Generalization via Interpolative Style Transfer and Contrastive Learning](http://arxiv.org/abs/2410.22622)

**FISC: 連合的なドメイン一般化を中間的スタイル転送と対比学習で実現**

Dung Thuy Nguyen, Taylor T. Johnson, Kevin Leach

- 連合学習はプライバシーを保ちつつ共同学習を可能にするが、ドメインシフトが課題
- FISCという新手法が複雑なドメイン分布を考慮し中間的スタイル転送と対比学習を活用
- クライアント間の多ドメイン表現と公平な収束目標を実現
- PACSやOffice-Home、IWildCamでの実験で精度が3.64%から57.22%向上

この研究面白そうだね！中間的スタイル転送ってどんな感じなのかな？クライアントと協力していろんなドメインに強くなるのって、なんか解決策の連携っぽくてワクワクしちゃうね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, cs.DC, **投稿日時:** 2024-10-30 00:50

- - -

### [Vertical Federated Learning with Missing Features During Training and Inference](http://arxiv.org/abs/2410.22564)

**トレーニングと推論中の欠損特徴を持つ垂直連合学習**

Pedro Valdeira, Shiqiang Wang, Yuejie Chi

- 垂直連合学習は特徴で分割されたデータセットでモデルを訓練するが、特徴欠損が課題
- 不完全なサンプルを利用しないと一般化能力が低下し、推論時の制約がある
- LASER-VFLという手法を提案し、特徴の欠損にも柔軟に対応可能なモデルを訓練
- 数値実験でベースラインを超える性能を示し、特徴欠損があっても精度向上を達成

この研究、めっちゃ実践的で興味深いね！従来の問題をクリアしつつ性能も向上するなんて、将来のAIの現場適用に超期待できる感じがする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.DS, math.OC, **投稿日時:** 2024-10-29 22:09

- - -

### [Unpicking Data at the Seams: VAEs, Disentanglement and Independent Components](http://arxiv.org/abs/2410.22559)

**データの解体: VAE、解きほぐしと独立成分**

Carl Allen

- 解きほぐしとは、データの重要な統計的に独立した要因を識別する技術である
- 解きほぐしは合成データ生成や頑健な特徴分類、効率的なエンコーディングに有用
- 変分オートエンコーダー(VAE)での解きほぐしが特に進展している
- VAEの目的がデータを解きほぐし、独立成分を識別する過程を明らかにした

解きほぐしって、データの裏側を理解するためのカギみたい！VAEが進化することで、次世代の合成データがもっとパワフルになりそうでワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, stat.ML, **投稿日時:** 2024-10-29 21:54

- - -

### [Adaptive Aggregation Weights for Federated Segmentation of Pancreas MRI](http://arxiv.org/abs/2410.22530)

**膵臓MRIの連合学習における適応型集約重み**

Hongyi Pan, Gorkem Durak, Zheyuan Zhang, Yavuz Taktak, Elif Keles, Halil Ertugrul Aktas, Alpay Medetalibeyoglu, Yury Velichko, Concetto Spampinato, Ivo Schoots, Marco J. Bruno, Rajesh N. Keswani, Pallavi Tiwari, Candice Bolan, Tamas Gonda, Michael G. Goggins, Michael B. Wallace, Ziyue Xu, Ulas Bagci

- 連合学習はデータを共有せずに共同モデル学習を可能にし、医療画像に最適
- 伝統的な連合平均法はドメイン間での一般化が困難であり、膵臓MRIで顕著
- 適応型重みの導入により、クライアントの貢献度を動的に調整し汎化性を向上
- 複数病院で有意な改善を示し、ドメインシフトの影響を低減しつつプライバシーを維持

膵臓MRIなんてすごく重要そう！この技術がもっと発展すれば、病院同士でのデータ共有の不安も減りそうだよね。みんなの命を救う手助けができるかも！



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, cs.DC, **投稿日時:** 2024-10-29 20:53

- - -

### [Evaluating utility in synthetic banking microdata applications](http://arxiv.org/abs/2410.22519)

**合成銀行ミクロデータ利用の有用性評価**

Hugo E. Caceres, Ben Moews

- 中央銀行は詳細な銀行ミクロデータを収集するが、銀行機密法によりアクセス制限がある
- 合成データ生成技術が登場したが、銀行の課題に焦点を当てた評価枠組みは欠けている
- 提案した枠組みを用い、パラグアイ中央銀行のデータから初の合成銀行ミクロデータを生成
- 頻度表に基づく推論手法が適しており、生成モデルより優れていることを示した

合成データを使って秘密を守りながらもデータの本質をつかむなんて、めっちゃ未来的！銀行のデータがもっとオープンになったら、新しい金融サービスを考えるきっかけになりそうだよね。それに、研究が色んなとこに広まったら面白いことがたくさんありそう！

**Comment:** 28 pages, 4 figures

**トピック:** [合成データ](sd), [PETs](pets), **カテゴリ:** q-fin.CP, cs.LG, 90B90, 91B82, 62P20, **投稿日時:** 2024-10-29 20:20

- - -

### [Privacy-Preserving Dynamic Assortment Selection](http://arxiv.org/abs/2410.22488)

**プライバシー保護の動的アソートメント選択**

Young Hyun Cho, Will Wei Sun

- プライバシー保護の必要性が増大する中、MNLバンディットモデルを用いた新たなフレームワークを提案。
- 摂動されたアッパーコンフィデンスバウンド法を用いて、ユーザーの効用推定にノイズを加え探索と活用のバランスを確保。
- 提案手法は動的環境に適した共同差分プライバシーを満たし、推論攻撃のリスクを効果的に軽減。
- 提案手法の理論的な後悔境界を導出し、Expediaホテルデータセットを使用したシミュレーションで性能向上を実証。

この研究、めっちゃおもしろい！プライバシーを守りながらも個人に最適なレコメンデーションとか、未来のサービスって感じでワクワクするよね。実用化されたら旅行とかもっと楽しくなりそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.AI, cs.CR, cs.LG, **投稿日時:** 2024-10-29 19:28
