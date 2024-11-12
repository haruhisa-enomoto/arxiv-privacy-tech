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

更新: 2024-11-12T04:23:34.229775

- - -

### [TempCharBERT: Keystroke Dynamics for Continuous Access Control Based on Pre-trained Language Models](http://arxiv.org/abs/2411.07224)

**TempCharBERT: 事前学習済み言語モデルに基づく継続的なアクセス制御のためのキー入力動力学**

Matheus Simão, Fabiano Prado, Omar Abdul Wahab, Anderson Avila

- デジタル環境での信頼できる認証と継続的なアクセス制御が重要。
- 個々のタイピングスタイルで個人を識別するキー入力動力学（KD）が注目される。
- 事前学習済み言語モデル（PLM）を活用し、タイピングの時間的特徴を考慮するTempCharBERTを提案。
- TempCharBERTを連合学習で訓練し、データプライバシーを向上する可能性を示した。

なんかTempCharBERTって未来感がいっぱい！タイピングの仕方で個人を特定できるなんておもしろいね。これで安全性もプライバシーも強化できるのかな。進化が待ち遠しいね💻✨

**Comment:** Accepted at WIFS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.CL, **投稿日時:** 2024-11-11 18:44

- - -

### [DLCR: A Generative Data Expansion Framework via Diffusion for Clothes-Changing Person Re-ID](http://arxiv.org/abs/2411.07205)

**DLCR: 衣服変更人物リ-IDのための拡散による生成データ拡張フレームワーク**

Nyle Siddiqui, Florinel Alin Croitoru, Gaurav Kumar Nayak, Radu Tudor Ionescu, Mubarak Shah

- 衣服変更人物再識別（CC-ReID）は、衣服を変更しても人物の識別を試みる難しい課題である
- 現在のCC-ReIDモデルは多様性が限られたデータセットにより制約を受けている
- 提案されたDLCRは、拡散モデルと大規模言語モデルを利用して多様な衣装の人物画像を生成する
- 提案手法はデータの多様性を10倍にし、先行研究と比べ精度を11.3%向上させる性能向上を達成

すごいね！衣服を変えても同じ人を認識できるようにするなんて、未来の防犯対策に使えそうでワクワクする！たくさんのデータを作って、もっと正確にできるっていう発想がかなり斬新だね！

**Comment:** Published in WACV 2025

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-11 18:28

- - -

### [Revisiting Ensembling in One-Shot Federated Learning](http://arxiv.org/abs/2411.07182)

**ワンショット連合学習におけるアンサンブルの再考**

Youssef Allouah, Akash Dhasade, Rachid Guerraoui, Nirupam Gupta, Anne-Marie Kermarrec, Rafael Pinot, Rafael Pires, Rishi Sharma

- 連合学習は生データを共有せずにモデルを訓練できるが、通信コストが高い。
- ワンショット連合学習は単一の通信ラウンドでコストを削減するが、精度にギャップがある。
- FENSは、ワンショット連合学習の通信効率を保持しながら連合学習に近い精度を達成。
- CIFAR-10データで、FENSは最新ワンショット手法より最大26.9%精度向上、通信量も低減。

このアプローチ、すごく効率的かつ精度も高めているみたいでびっくり！特にデータをあまり共有せずに高い精度を出す方法が、未来のいろんなデータを守りながら学習する時代にぴったりだよね。

**Comment:** Accepted at NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-11-11 17:58

- - -

### [Differentially-Private Collaborative Online Personalized Mean Estimation](http://arxiv.org/abs/2411.07094)

**差分プライバシーを用いた協調型オンラインパーソナライズ平均推定**

Yauhen Yakimenka, Chung-Wei Weng, Hsuan-Yin Lin, Eirik Rosnes, Jörg Kliewer

- プライバシー制約下での協調型平均推定問題に取り組み、差分プライバシーによる手法を提案
- 仮説検定とデータ分散推定を組み合わせ、2つのプライバシー機構と分散推定手法を提案
- 提案手法は各エージェントのデータが未知でも、理論的に局所手法より高速な収束を示す
- 理想的な性能に近い収束速度を達成し、プライベートコラボレーションのメリットを確認

データが未知でも、協力することで素早く収束できるのってすごいよね。プライバシーを守りながらもスムーズに情報を共有できる仕組みが、これからのデータ社会にとって重要になりそう！

**Comment:** Presented in part at the 2023 IEEE International Symposium on   Information Theory (ISIT)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.IT, math.IT, **投稿日時:** 2024-11-11 16:14

- - -

### [Hierarchical Conditional Tabular GAN for Multi-Tabular Synthetic Data Generation](http://arxiv.org/abs/2411.07009)

**マルチタブラー合成データ生成のための階層条件タブラーGAN**

Wilhelm Ågren, Victorio Úbeda Sosa

- 合成データ生成は、実データアクセスやプライバシー規制の制約を乗り越える方法である
- 単一タブラーよりも複雑なマルチタブラー間のデータ生成研究はまだ少ない
- 提案されたHCTGANにより、複雑なマルチタブラーから効率的に大量の合成データを生成
- 大規模データにはHCTGAN、小規模データには品質重視でHMA1モデルが適すると示唆

マルチタブラーの複雑な関係を保ちながら合成データを効率的に生成できるなんてすごい！これでさらに多くの分野でプライバシーを守りつつ、安全にデータ活用が進むといいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.DB, **投稿日時:** 2024-11-11 14:09

- - -

### [Which PPML Would a User Choose? A Structured Decision Support Framework for Developers to Rank PPML Techniques Based on User Acceptance Criteria](http://arxiv.org/abs/2411.06995)

**ユーザーはどのPPMLを選ぶ？ユーザー受容基準に基づく開発者向けPPML技術ランク決定支援フレームワーク**

Sascha Löbner, Sebastian Pape, Vanessa Bracamonte, Kittiphop Phalakarn

- プライバシー強化技術（PETs）は機械学習における計算能力やデータ利用方法に影響を及ぼす。
- PETsの導入で応答遅れやデータ精度の低下などのトレードオフが発生する。
- ユーザーの技術的理解が限定的であり、PPML選択に貢献する方法がない。
- 本研究はユーザー受容基準に基づき、PPML技術を評価ランク付けする枠組みを提供する。

ユーザーの観点からPPML技術の評価をするなんて、新しい考え方だよね！開発者が選びやすくなりそうだし、サービス品質も向上しそうでとってもワクワクする。



**トピック:** [PETs](pets), **カテゴリ:** cs.AI, cs.CR, cs.LG, cs.SE, **投稿日時:** 2024-11-11 13:53

- - -

### [WassFFed: Wasserstein Fair Federated Learning](http://arxiv.org/abs/2411.06881)

**WassFFed: ワッサースタインに基づく公平な連合学習**

Zhongxuan Han, Li Zhang, Chaochao Chen, Xiaolin Zheng, Fei Zheng, Yuyuan Li, Jianwei Yin

- 連合学習では地理的に分散した多様なユーザーグループのデータを公平に扱う必要がある
- 現行の方法では代理関数で得られる公正な最適化結果と公正な分類結果の整合性が取れない
- 非独立同分布（non-IID）のデータで局所モデルの集約が全体の公正性を保証しない
- WassFFedはワッサースタイン重心を使用し、局所モデルをグローバル出力に近づけ一貫性を確保

ワッサースタイン距離を使って公平性を高めるアプローチって斬新だね！データ分散の問題が解決されれば、より多くの応用が期待できそう。興味が尽きないテーマだな～。

**Comment:** Submitted to TKDE

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-11-11 11:26

- - -

### [Maximizing domain generalization in fetal brain tissue segmentation: the role of synthetic data generation, intensity clustering and real image fine-tuning](http://arxiv.org/abs/2411.06842)

**胎児脳組織セグメンテーションにおけるドメイン一般化の最大化：合成データ生成、強度クラスタリングと実画像のファインチューニングの役割**

Vladyslav Zalevskyi, Thomas Sanchez, Margaux Roulet, Hélène Lajous, Jordina Aviles Verdera, Jana Hutter, Hamza Kebiri, Meritxell Bach Cuadra

- 複数スキャナーや設定からのデータの異質性とデータ不足が課題である
- SynthSegを用いた手法は単一ソースのドメイン一般化に潜在力を持つ
- 単純なガウス混合モデルが物理情報を用いた生成よりOOD一般化に優れている
- 合成データで事前学習したモデルのファインチューニングが複数ドメインでの改善に寄与する

領域を越えて活用できるってすごいよね！胎児の脳に限らず、他の臓器やモダリティにも展開できるかもって思うとワクワクするな〜。データの異質性を克服する方法の研究って、これからの進展が楽しみだね！



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-11-11 10:17

- - -

### [Model Partition and Resource Allocation for Split Learning in Vehicular Edge Networks](http://arxiv.org/abs/2411.06773)

**車両エッジネットワークにおける分割学習のためのモデル分割とリソース割り当て**

Lu Yu, Zheng Chang, Yunjian Jia, Geyong Min

- 自動運転技術と車両ネットワークの統合はプライバシー保持や通信効率の課題を生む
- U字型分割連合学習フレームワーク (U-SFL) がプライバシーを強化し複数車両で並列処理を可能にする
- セマンティック対応オートエンコーダー (SAE) がデータ伝送効率を高め通信遅延を低減
- 深層強化学習（DRL）アルゴリズムがリソース割り当てと分割点選択のNP困難問題を解決

ふむふむ、この研究って、まるで『未来の交通』そのものだね！同時並行でめっちゃ効率的に自動運転が進んで行く未来、わたしたちの生活も楽しくなっちゃう気がするよ！

**Comment:** arXiv admin note: text overlap with arXiv:2306.12194 by other authors

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-11-11 07:59

- - -

### [Sketched Adaptive Federated Deep Learning: A Sharp Convergence Analysis](http://arxiv.org/abs/2411.06770)

**スケッチ適応型連合深層学習: 鋭い収束解析**

Zhijie Chen, Qiaobo Li, Arindam Banerjee

- 勾配圧縮と適応最適化を組み合わせることで、通信ラウンド数と通信量を削減できる。
- 線形依存で高コストだった通信量を、対数的な依存関係にする理論的収束解析を提案。
- 現在の分析とは異なり、異方性曲率を利用することでスケッチノイズを改善。
- i.i.d.環境では速い収束を示し、非i.i.d.環境でも収束の証明ができる。

理論的な根拠を実証データで裏付けているのがすごく心強いなあ。さらに、この方法が最先端と競えるレベルってのも面白いね！新しい通信効率の技術が実現する未来、楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-11 07:51

- - -

### [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](http://arxiv.org/abs/2411.06722)

**合成し、分割し、適応する：基盤モデルから多様なサンプルを引き出す方法**

Yeming Wen, Swarat Chaudhuri

- 基盤モデルで多様な応答を生成することが重要だが、精度を犠牲にせずに生成するのが難しい。
- 新しいフレームワーク「Synthesize-Partition-Adapt (SPA)」を提案し、多様な応答を生成。
- SPAは合成データを利用し、データを特徴ごとに分割し、異なるモデル適応を訓練する。
- 実験結果により、コード生成や自然言語理解タスクで高品質かつ多様な応答生成が示された。

この研究、なんだか面白そうじゃない？新しい方法でユーザー体験がもっと豊かになるかも！いろんなアプリで試してみたくなるね。きっと未来のAIとの会話も変わるんだろうな〜。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-11 05:13

- - -

### [DiffSR: Learning Radar Reflectivity Synthesis via Diffusion Model from Satellite Observations](http://arxiv.org/abs/2411.06714)

**DiffSR: 衛星観測からの拡散モデルによるレーダー反射率合成の学習**

Xuming He, Zhiwang Zhou, Wenlong Zhang, Xiangyu Zhao, Hao Chen, Shiqi Chen, Lei Bai

- 天気レーダーデータの合成は、地上観測が不足している領域のデータを補完することが目的。
- 既存手法は再構築ベースで過剰に平滑化され、高周波数や高値観測区域の生成が困難。
- 提案手法DiffSRは二段階拡散法で、レーダー推定と衛星データを条件に合成。
- 実験は最先端の結果を示し、高周波数と高値エリア生成の能力を証明。

天気予測がより正確になりそうで、災害対策にも役立ちそう！まさに技術の力で未来を変えるって感じでワクワクするね。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.AI, cs.CV, cs.LG, **投稿日時:** 2024-11-11 04:50

- - -

### [What Should Baby Models Read? Exploring Sample-Efficient Data Composition on Model Performance](http://arxiv.org/abs/2411.06672)

**赤ちゃんモデルは何を読むべきか？モデル性能におけるサンプル効率の良いデータ構成の探求**

Hong Meng Yam, Nathan J Paek

- 小規模な言語モデルには、複雑で豊かなGutenbergのようなデータセットが効果的
- CHILDESやTinyStoriesで訓練したモデルは、あらゆるモデルサイズで劣っていた
- サンプル効率的な訓練には、データセット構成とモデル容量の両方を考慮する必要がある
- データセットの選択はモデルサイズに依存し、子供向けスピーチと簡易な物語は常に最適ではない

赤ちゃんモデルに読ませるものって重要なんだね！サイズに合ったデータ選びの知識が、言語モデルの進化に欠かせないのかも。今後こうした研究が、もっと効率的なモデルを生み出すのに役立ちそうでワクワクするね！

**Comment:** 8 pages, 6 figures, CoNLL 2024 (Shared Task) Accepted Paper

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-11-11 02:37

- - -

### [Using Diffusion Models as Generative Replay in Continual Federated Learning -- What will Happen?](http://arxiv.org/abs/2411.06618)

**連続連合学習における生成的リプレイとしての拡散モデルの使用 -- 何が起こるか？**

Yongsheng Mei, Liangqi Yuan, Dong-Jun Han, Kevin S. Chan, Christopher G. Brinton, Tian Lan

- 連合学習ではデータ分布が動的に変化するため、継続的学習の問題が発生する
- 主な課題は壊滅的忘却と非IIDな入力データで、従来の解決策は履歴データのリプレイかGANを使用
- 新しい枠組みDCFLは条件付き拡散モデルで合成データを生成し、動的データ分布のずれを軽減
- 提案手法は収束境界を提供し、複数データセットでの効果的な性能を実証

条件付き拡散モデルを使って連合学習を改善するなんて、めっちゃ斬新じゃない？どんなデータセットでもうまくいくようになるかも、未来が楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-11-10 22:48

- - -

### [Protection against Source Inference Attacks in Federated Learning using Unary Encoding and Shuffling](http://arxiv.org/abs/2411.06458)

**連合学習におけるユニコードとシャッフルを用いたソース推論攻撃からの保護**

Andreas Athanasiou, Kangsoo Jung, Catuscia Palamidessi

- 連合学習（FL）では、データを公開せずにクライアントがモデルを共同で訓練
- ソース推論攻撃（SIA）では中央サーバーが特定データの所有クライアントを特定可能
- ユニコードとシャッフルを用い中央サーバーからの情報推論を防止
- 定量化を導入し、通信コストを抑えつつSIAの精度を低下させた

シャッフルすることで攻撃を防ぐなんて発想が面白いね！これがうまくいくなら、もっとプライバシーが守られる未来がくるかも！

**Comment:** CCS 2024 - The ACM Conference on Computer and Communications   Security, ACM, Oct 2024, Salt Lake City, United States

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-11-10 13:17

- - -

### [Client Contribution Normalization for Enhanced Federated Learning](http://arxiv.org/abs/2411.06352)

**強化された連合学習のためのクライアント寄与標準化**

Mayank Kumar Kundalwal, Anurag Saraswat, Ishan Mishra, Deepak Mishra

- スマートフォンなどのモバイルデバイスのデータは分散的かつ異質で、従来の集中型機械学習に課題を与える。
- 連合学習（FL）は、データ共有なしで分散デバイス間でグローバルモデルを協力的に訓練できる。
- 本研究は、クライアント間の統計的不均一性をデータ依存の視点で捉え平均潜在表現で寄与を正規化する手法を提案。
- 多様なデータセットで実験を行い、モデルの精度と一貫性の大幅な向上を確認し、FLの信頼性を改善。

技術者さんたちは、連合学習の進化を追求しているんだね！クライアントのデータのばらつきを平均化することで、もっと正確なモデルが作れるようになるなんて、ほんとスゴイよね。未来の機械学習の発展が楽しみ♪

**Comment:** Accepted at IEEE INDICON 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-10 04:03

- - -

### [AMAZE: Accelerated MiMC Hardware Architecture for Zero-Knowledge Applications on the Edge](http://arxiv.org/abs/2411.06350)

**AMAZE: エッジでのゼロ知識アプリケーションのためのMiMCハードウェアアーキテクチャの加速**

Anees Ahmed, Nojan Sheybani, Davi Moreno, Nges Brian Njungle, Tengkai Gong, Michel Kinsy, Farinaz Koushanfar

- ゼロ知識証明(ZKP)では、SHA2などのCRH関数が非効率である
- ZKフレンドリーなMiMCハッシュは、ZKPに適したブロック暗号とハッシュを提供
- MiMCをハードウェアで効率的に組み込むことが重要な課題である
- AMAZEはMiMCのハードウェア最適化を行い、CPU性能を13倍以上上回る

エッジデバイスでのZKフレンドリーな技術をハードウェアでこんなに効率化しちゃうなんてすごいよね！ゼロ知識証明の応用がどんどん広がっていきそうで、未来のおもしろい技術が楽しみ♪

**Comment:** Accepted to ICCAD 2024

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.AR, **投稿日時:** 2024-11-10 03:55

- - -

### [CRTRE: Causal Rule Generation with Target Trial Emulation Framework](http://arxiv.org/abs/2411.06338)

**CRTRE: ターゲット試行エミュレーションフレームワークによる因果ルール生成**

Junda Wang, Weijian Li, Han Wang, Hanjia Lyu, Caroline P. Thirukumaran, Addisu Mesfin, Hong Yu, Jiebo Luo

- 医療分野における因果推論とモデル解釈可能性が注目されている
- CRTREはランダム化試行設計の原理を用い、因果効果を推定する新しい方法
- 6つの医療データセットで実験を行い、他のモデルを上回る性能を達成
- 実データセットでの予測精度とICDコード予測タスクでの優れたAUCスコアを記録

因果推論と医療データ解析の融合って、まさに未来の医学そのものかも！この技術が進化すると、より正確な病気の予測ができちゃうかもね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-10 02:40

- - -

### [TinyML NLP Approach for Semantic Wireless Sentiment Classification](http://arxiv.org/abs/2411.06291)

**セマンティックワイヤレス感情分類のためのTinyML NLPアプローチ**

Ahmed Y. Radwan, Mohammad Shehab, Mohamed-Slim Alouini

- NLPはユーザープライバシーを侵害しがちで、デバイス負荷が大きい
- 連合学習はプライバシー保護が強いがエネルギー消費が高い
- 分割学習はエネルギー効率が良く、プライバシーを守るTinyML手法として注目
- 分割学習は高精度を維持しながら処理電力とCO2排出を削減

分割学習が注目されているのはおもしろいね！プライバシーも環境も守れるなんて、未来の技術だなって思う！違う手法をうまく組み合わせて、より良いソリューションが開発されるのが楽しみ！

**Comment:** Submitted for WCNC-2025, Under Review

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.IT, math.IT, 68T50, 94A12, I.2.7; C.2.1, **投稿日時:** 2024-11-09 21:26

- - -

### [Federated Split Learning for Human Activity Recognition with Differential Privacy](http://arxiv.org/abs/2411.06263)

**連合スプリット学習による差分プライバシーを活用した人の行動認識**

Josue Ndeko, Shaba Shaon, Aubrey Beal, Avimanyu Sahoo, Dinh C. Nguyen

- 新たなFSL-DPフレームワークにより、人の行動認識精度が向上
- 従来の連合学習に比べ、FSLフレームワークが精度と損失面で優れている
- プライバシー保証とモデル精度のバランスを探るため、DPメカニズムのデータ設定を調査
- FSLフレームワークは通信時間が短く、効率性と効果的な性能を示す

この技術が進化すれば、私たちのデバイスはもっと賢くなるかもね！実生活のデータでテストされたっていうのも頼もしいな。連合スプリット学習…響きからしてなにかすごそう！

**Comment:** Accepted to IEEE Consumer Communications and Networking Conference   (CCNC), 6 pages

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-11-09 19:32

- - -

### [A Sharded Blockchain-Based Secure Federated Learning Framework for LEO Satellite Networks](http://arxiv.org/abs/2411.06137)

**LEO衛星ネットワーク向けのシャードブロックチェーンを用いた安全な連合学習フレームワーク**

Wenbo Wu, Cheng Tan, Kangcheng Yang, Zhishu Shen, Qiushi Zheng, Jiong Jin

- LEO衛星ネットワークは宇宙ベースのAIアプリケーションに必須だが、サイバー攻撃リスクが高まっている
- 従来のモデルでは、地上ステーションへの送信に注力し、衛星特有のセキュリティ問題を見過ごしがち
- SBFL-LEOはシャードブロックチェーン技術を活用、衛星に特定の役割を割り振り通信信頼性を向上
- 新手法はモデル精度やエネルギー効率を向上し、攻撃耐性を強化する実験結果が示された

ブロックチェーンと連合学習を組み合わせて、衛星間通信の安全性をアップするなんてすごい！これからの宇宙AI時代に欠かせない技術になりそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-11-09 10:22

- - -

### [Behavior-Aware Efficient Detection of Malicious EVs in V2G Systems](http://arxiv.org/abs/2411.06113)

**行動認識に基づくV2Gシステムにおける悪意のあるEV検出の効率化**

Ruixiang Wu, Xudong Wang, Tongxin Li

- 電気自動車とV2G技術の進展で悪意のあるユーザー検出が重要に
- 機械学習で非協力的な行動パターンを予測するも、予測の信頼性が低い
- 新手法\ouralgを提案し、確率的グループテストとML予測、組合せグループテストを組み合わせる
- 実験で\ouralgの効果を確認し、エネルギー・輸送分野でのアルゴリズム決定への貢献を示す

この研究って面白そう！実際のEVデータも使って、非協力な運転手を効率的に探し出すんだって。未来のスマートグリッドには欠かせない技術に思えるよね！



**トピック:** [合成データ](sd), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-11-09 08:31

- - -

### [Personalized Hierarchical Split Federated Learning in Wireless Networks](http://arxiv.org/abs/2411.06042)

**ワイヤレスネットワークにおける個別化された階層型分割連合学習**

Md-Ferdous Pervej, Andreas F. Molisch

- ワイヤレスネットワークでは、リソース制約で分散クライアントによる大規模MLが難しい。
- 分割連合学習により、クライアント側のブロックのみでモデルを訓練し負荷を軽減。
- 個々のタスクに適した個別モデルが必要で、パーソナライズされた学習アルゴリズムを提案。
- 分割モデルの影響を理論的に分析し、クライアントごとに微調整したモデルで精度が向上。

ワイヤレスネットワークって大変そうだけど、みんなに合ったやり方を見つけていくのすごく面白そう！未来はもっと個々に最適化されたネットワーク環境になりそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.NI, cs.SY, eess.SY, **投稿日時:** 2024-11-09 02:41

- - -

### [A novel study on the MUSIC-type imaging of small electromagnetic inhomogeneities in the limited-aperture inverse scattering problem](http://arxiv.org/abs/2411.06030)

**限られた開口逆散乱問題における小さな電磁的不均一性のMUSIC型イメージングに関する新しい研究**

Won-Kwang Park

- MUSICアルゴリズムを逆散乱問題に適用し、不均一性の位置を再構築
- 伝統的な手法ではノイズ部分空間への射影が難しいため、代替の射影演算子を定義
- イメージング関数の表現に整数階の第一種ベッセル関数を用いる
- 数値シミュレーションで設計したMUSICアルゴリズムの有効性を実証

MUSICアルゴリズムでの不均一性を特定する新しい方法なんだね！小さい違いを見つけるのが得意そうで楽しみ！研究が進めば、将来どんな新しい技術が生まれるのかワクワクしちゃうね。

**Comment:** 26 pages, 10 figures

**トピック:** [合成データ](sd), **カテゴリ:** math.NA, cs.NA, 78A46, **投稿日時:** 2024-11-09 01:25

- - -

### [DNAMite: Interpretable Calibrated Survival Analysis with Discretized Additive Models](http://arxiv.org/abs/2411.05923)

**DNAMite: 離散化加法モデルによる解釈可能な適合的生存分析**

Mike Van Ness, Billy Block, Madeleine Udell

- 生存分析の多くの機械学習モデルはブラックボックスであり、医療分野で解釈可能性が重要。
- 近年ではガラスボックスモデルが登場し、予測性能と解釈可能性を両立するものもある。
- 新提案のDNAMiteは特徴の離散化とカーネルスムージングを用いて柔軟な形状関数を学習。
- DNAMiteは合成データで真の形状関数に近いものを生成し、既存モデルより良好なキャリブレーションを実現。

この研究、医療分野にとってすごく役立ちそうだね！ガラスボックスモデルだから、ドクターたちも安心して使えちゃう。そしてDNAMiteがどんなふうに未来の予測をもっと正確にしてくれるか、ワクワクしちゃうな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-11-08 19:13

- - -

### [Interplay between Federated Learning and Explainable Artificial Intelligence: a Scoping Review](http://arxiv.org/abs/2411.05874)

**連合学習と説明可能な人工知能の相互作用：スコーピングレビュー**

Luis M. Lopez-Ramos, Florian Leiser, Aditya Rastogi, Steven Hicks, Inga Strümke, Vince I. Madai, Tobias Budig, Ali Sunyaev, Adam Hilbert

- 連合学習と説明可能なAIは、プライバシーを守りながら分散データからモデルを学習し、内部構造を説明可能にする。
- 多くの研究が特徴の関連性を重視した説明手法に焦点を当てており、アルゴリズムの透明性に関する解釈可能性は少ない。
- 水平方向の連合学習セットアップで、10以下のデータセンターを使用したシミュレーションが主流。
- 連合学習がモデルの説明に及ぼす影響を定量的に分析した研究はほとんどなく、特にFLノード間の解釈可能性の集約が課題。

連合学習と説明可能AIの組み合わせって面白いよね。これからもっと研究が進んで、どう活用されるのか期待しちゃう！特にデータセンターにおける実世界の応用と具体的な成果が早く知りたいな〜。

**Comment:** 16 pages, 11 figures, submitted in IEEE Trans. Knowledge and Data   Engineering

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-07 22:44

- - -

### [Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data](http://arxiv.org/abs/2411.05869)

**大規模データに対する正確なガウス過程を計算するためのコンパクトにサポートされた非定常カーネル**

Mark D. Risser, Marcus M. Noack, Hengrui Luo, Ronald Pandolfi

- Gaussian process（GP）は不確実性を含むため、科学技術分野で有用
- 従来のGPは非定常性を扱えず、データセットの規模が制限される
- 提案手法は新たなカーネルを導入し、巨大データの解析を実現
- 地球科学で最先端を上回る結果を示し、GPの競争力向上を立証

大規模データでもGPがもっと自由に使えるようになるって、すごくワクワクするよね！これが進めば、いろんな分野でガウス過程がもっと活躍しそう！✨



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, stat.AP, stat.CO, stat.ME, **投稿日時:** 2024-11-07 20:07

- - -

### [Multivariate Data Augmentation for Predictive Maintenance using Diffusion](http://arxiv.org/abs/2411.05848)

**拡散モデルを用いた予知保全のための多変量データ拡張**

Andrew Thompson, Alexander Sommers, Alicia Russell-Gilbert, Logan Cummins, Sudip Mittal, Shahram Rahimi, Maria Seale, Joseph Jaboure, Thomas Arnold, Joshua Church

- 予知保全は異常検知能力に依存し、システム故障が少ないため訓練データが不足しがち
- 新規システムには故障データがなく、実データとの関係学習が困難
- 拡散モデルを用いることで、高度な合成故障データを生成し性能を向上
- 本研究は失敗経験のない新システム向けに役立つ多変量合成データを生成する方法を示す

合成データの生成技術って、未来の予測に役立ちそうでワクワクする！新しいシステムでもデータ不足の心配なしにどんどん発展できるようになったらすごいよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-06 16:57

- - -

### [Federated Data-Driven Kalman Filtering for State Estimation](http://arxiv.org/abs/2411.05847)

**連合データ駆動カルマンフィルタによる状態推定**

Nikos Piperigkos, Alexandros Gkillas, Christos Anagnostopoulos, Aris S. Lalos

- 自動運転車の高精度な位置特定のための連合学習ベースの新しい枠組みを提案
- KalmanNetを基にFedKalmanNetを開発し、車両グループが分散トレーニングを実施
- V2X通信なしで位置特定可能、システム不確実性行列を推定して自己局在化を実現
- CARLAシミュレータでの実験で、従来手法を超える性能を確認

この研究、すごくワクワクするよね！連合学習を活用して自分で自己位置を特定できるようになるとか、未来の自動運転がもっと身近に感じられるよね。リアルタイム通信が要らないってことは、より効率的に安全に走れるかもしれないね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, cs.AI, **投稿日時:** 2024-11-06 16:18

- - -

### [Navigating Distribution Shifts in Medical Image Analysis: A Survey](http://arxiv.org/abs/2411.05824)

**医療画像解析における分布シフトのナビゲーション: サーベイ**

Zixian Su, Jingwei Guo, Xi Yang, Qiufeng Wang, Frans Coenen, Kaizhu Huang

- 医療画像解析はディープラーニングで進展するが、分布シフトにより性能低下の課題がある
- データのアクセス性やプライバシー問題に応じた技術カテゴリで分布シフト問題の研究を分類
- 共同トレーニング、連合学習、ファインチューニング、ドメイン一般化の手法を説明
- 研究者に向けて、医療機関の制約下での画像解析の適応力と堅牢性向上を指針として提供

医療画像解析がこんなに進化してるなんてワクワクするよね！これからもっとリアルな現場で活用されて、患者さんにも優しい技術が広がっていくといいな。次世代の医療が待ち遠しい！



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, cs.LG, **投稿日時:** 2024-11-05 08:01
