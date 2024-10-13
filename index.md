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

更新: 2024-10-13T04:22:17.903207

- - -

### [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](http://arxiv.org/abs/2410.08196)

**MathCoder2: モデル翻訳された数学的コードの継続的プレトレーニングによるより良い数学的推論**

Zimu Lu, Aojun Zhou, Ke Wang, Houxing Ren, Weikang Shi, Junting Pan, Mingjie Zhan, Hongsheng Li

- コードは言語モデルの数学推論能力を向上させるが、従来のプレトレーニングには直接的な数学推論への焦点が欠けていた。
- 新しい手法で数学的コードと対応する推論ステップを生成する継続的プレトレーニングが導入された。
- 高品質の数学データセットをウェブデータ、パッケージコード、教科書、合成データから作成し、推論ステップと対応するコードを生成。
- 生成したデータを元に複数モデルをトレーニングし、数学的能力が有意に向上、MathCoder2ファミリーを開発。

この論文超面白そう！数学のコードと推論ステップを組み合わせて、モデルの理解を深めてるんだね。高校の数学苦手な子も試しにこのモデルで勉強したくなっちゃうかも！

**Comment:** https://github.com/mathllm/MathCoder2

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.CV, **投稿日時:** 2024-10-10 17:58

- - -

### [PP-GWAS: Privacy Preserving Multi-Site Genome-wide Association Studies](http://arxiv.org/abs/2410.08122)

**PP-GWAS: プライバシー保護型マルチサイトゲノムワイド関連解析**

Arjhun Swaminathan, Anika Hannemann, Ali Burak Ünal, Nico Pfeifer, Mete Akgün

- 多サイト間のGWASは統計的パワーを強化するが、遺伝情報共有のセンシティブさが障害となる
- 現行のプライバシー重視手法は準同型暗号や秘密計算など計算コストが高い
- PP-GWASは計算効率とスケーラビリティを向上させた新アルゴリズムを提案
- 試験で既存アルゴリズムの2倍の速度で動作し、省リソースで高いセキュリティモデルを実現

このアルゴリズム、めっちゃワクワクするね！プライバシーを守りつつバリバリ分析できるなら、未来の研究の可能性が広がりそう。効率も速さもアップして、どんどん進化していく感じが最高だね！



**トピック:** [合成データ](sd), [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-10 17:07

- - -

### [Private Language Models via Truncated Laplacian Mechanism](http://arxiv.org/abs/2410.08027)

**切断ラプラス機構を用いたプライベート言語モデル**

Tianhao Huang, Tao Yang, Ivan Habernal, Lijie Hu, Di Wang

- 深層学習モデルはプライバシー攻撃に弱く、既存手法はプライバシー強度の限界がある
- 切断ラプラス機構を高次元に拡張し、プライベートな単語埋め込み手法を提案
- 提案手法は既存手法よりも分散が低く、理論的に優れていると示される
- 実験で高プライバシー状況でも非プライベートな場合と比較して性能低下を最小限に抑えた

新しいプライベートな手法ってすごいね！異次元のアイディアで、これからもっと安心してAIを使える時代がくるかもってワクワクする。

**Comment:** Accepted by EMNLP 2024, Main Track

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-10-10 15:25

- - -

### [Disease Entity Recognition and Normalization is Improved with Large Language Model Derived Synthetic Normalized Mentions](http://arxiv.org/abs/2410.07951)

**病気エンティティ認識と正規化は大規模言語モデルで生成された合成正規化メンションによって改善される**

Kuleen Sasse, Shinjitha Vadlakonda, Richard E. Kennedy, John D. Osborne

- 病気のエンティティ認識（DER）と正規化（DEN）において、頻度の低い概念は教育用の例が少ない
- 大規模言語モデル（LLM）を用いて合成データを生成し、DERとDENの性能を向上させる
- 合成データにより、特に病気エンティティ正規化では精度が3-9ポイント、分布外データで20-55ポイント向上
- 病気エンティティ認識の改善は限られており、合成データの効果は主に正規化で顕著

合成データを活用して性能を向上させるなんてすごいね！病気の理解がもっと進むといいな。でも、認識の方ももっと改善できるといいのになー。

**Comment:** 21 pages, 3 figures, 7 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, I.2.7; J.3, **投稿日時:** 2024-10-10 14:18

- - -

### [Identifying latent disease factors differently expressed in patient subgroups using group factor analysis](http://arxiv.org/abs/2410.07890)

**患者サブグループにおける潜在的な病因要素をグループ因子分析で特定する**

Fabio S. Ferreira, John Ashburner, Arabella Bouzigues, Chatrin Suksasilp, Lucy L. Russell, Phoebe H. Foster, Eve Ferry-Bolder, John C. van Swieten, Lize C. Jiskoot, Harro Seelaar, Raquel Sanchez-Valle, Robert Laforce, Caroline Graff, Daniela Galimberti, Rik Vandenberghe, Alexandre de Mendonca, Pietro Tiraboschi, Isabel Santana, Alexander Gerhard, Johannes Levin, Sandro Sorbi, Markus Otto, Florence Pasquier, Simon Ducharme, Chris R. Butler, Isabelle Le Ber, Elizabeth Finger, Maria C. Tartaglia, Mario Masellis, James B. Rowe, Matthis Synofzik, Fermin Moreno, Barbara Borroni, Samuel Kaski, Jonathan D. Rohrer, Janaina Mourao-Miranda

- 異質性が病理解明や治療開発を妨げる神経・精神障害に対し、新手法を提案
- 提案手法は多様なデータモダリティ間の関連をサブグループ別に発見可能
- フロントトラル認知症で特定の潜在因子をサブグループ間で見分けることに成功
- 提案手法により病気特徴の解明や患者の細分化が期待される

新しい手法で病気を深掘りしたら、きっと治療法ももっと良くなるよね！脳の謎にさらに近づくみたいで、なんかワクワクしちゃう！

**Comment:** 38 pages, 14 figures

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-10-10 13:12

- - -

### [A Comprehensive Survey on Joint Resource Allocation Strategies in Federated Edge Learning](http://arxiv.org/abs/2410.07881)

**連合エッジ学習における共同資源配分戦略の包括的調査**

Jingbo Zhang, Qiong Wu, Pingyi Fan, Qiang Fan

- 連合エッジ学習は分散環境でユーザープライバシーを保ちながらモデルを訓練する手法である
- IoTやスマートアースの発展により、従来の資源配分では計算と通信の需要に対応できない
- この論文は、計算、データ、通信、ネットワークトポロジーの資源を共同で最適化する戦略を調査
- 結果としてシステム効率の向上、遅延の削減、資源利用の改善、そしてセキュリティ向上を示唆

未来の技術の基盤を作っていく感じがワクワクするよね！こういう共同戦略がもっと進化すれば、安心して便利な生活が増えていくんだろうなって思えてくる。

**Comment:** This paper has been submitted to CMC-Computers Materials & Continua

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-10 13:02

- - -

### [Unsupervised Data Validation Methods for Efficient Model Training](http://arxiv.org/abs/2410.07880)

**効率的なモデル訓練のための教師なしデータ検証方法**

Yurii Paniv

- NLPやTTSなどの先端モデルは大規模データに依存するが、低リソース言語では不足が深刻
- データの質を定義し、適切なデータ生成方法を開発、そして訓練アクセス性を向上させることを探求
- データ拡張や多言語転移学習、合成データ生成選択技術の進展と限界を包括的にレビュー
- 研究の課題を整理し、データ効率化やデータ量の削減とモデル性能維持のための枠組みを提供

データが少ない言語にも優しい機械学習を目指しているんだね！身近な問題が解決すると、もっと便利なツールやサービスが増えていきそうでワクワクするね。どんな可能性が広がるのか、未来が楽しみ～って感じだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-10-10 13:00

- - -

### [Enhancing Federated Domain Adaptation with Multi-Domain Prototype-Based Federated Fine-Tuning](http://arxiv.org/abs/2410.07738)

**マルチドメインプロトタイプによる連合学習適応の強化**

Jingyuan Zhang, Yiyang Duan, Shuaicheng Niu, Yang Cao, Wei Yang Bryan Lim

- 連合ドメイン適応は異なるデータドメインでの学習が課題で、データの異質性が原因で勾配更新が分散しがち
- 新しいフレームワークMPFTを提案し、カテゴリ固有のデータから得た情報で事前学習モデルを微調整
- サーバー側での有効な学習を通じプライバシーを守りつつ、クライアントへ最適化されたアダプタを配布
- MPFTは単一通信ラウンドで収束し、計算と通信コストを削減しつつ高い精度を実現

この研究なんだか面白そう！MPFTって方法で、効率よくプライバシーもバッチリ守りつつ性能を向上させてるのいい感じ。プロトタイプを使った攻撃の検証も含めて、AI担当者には助かる技術になるかもね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-10 09:15

- - -

### [FedEP: Tailoring Attention to Heterogeneous Data Distribution with Entropy Pooling for Decentralized Federated Learning](http://arxiv.org/abs/2410.07678)

**FedEP: エントロピー・プーリングを用いた非集中型連合学習における異種データ分布への適応**

Chao Feng, Hongjie Guan, Alberto Huertas Celdrán, Jan von der Assen, Gérôme Bovet, Burkhard Stiller

- 連合学習の性能はクライアント間のデータ分布に大きく影響され、非IIDデータは収束遅延とモデル劣化を引き起こす
- 従来の非IID問題解決アルゴリズムは中央集権型FLに依存しており、分散型FLではノードが全体視野を欠く
- 本研究はFedEPという新たな分散型FL集約アルゴリズムを提案し、ローカル分布の統計特性を考慮してクライアントドリフト問題を軽減する
- FedEPは実験結果により、最新手法より高速な収束と高いテスト性能を実現することが示された

エントロピー・プーリングとか、かっこよくて頭良さそうな感じする！連合学習の新技術だから、これからのデータプライバシーにも役立ちそうだね。進化する技術を使って、新しい未来が作られていくのってワクワクするよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-10 07:39

- - -

### [Scalable and Resource-Efficient Second-Order Federated Learning via Over-the-Air Aggregation](http://arxiv.org/abs/2410.07662)

**エア集約によるリソース効率の良いスケーラブルな第二オーダー連合学習**

Abdulmomen Ghalkha, Chaouki Ben Issaid, Mehdi Bennis

- 第二オーダー連合学習は、曲率情報を利用して収束速度を向上させるが計算と記憶コストが高い
- 大規模モデルでは通信オーバーヘッドが課題となり、デジタル伝送がボトルネックを引き起こす
- スパースヘシアン推定とエア集約を用いることでスケーラブルな第二オーダーFLアルゴリズムを提案
- シミュレーション結果では通信リソースとエネルギーを67％以上節約できた

第二オーダーFLをもっと効率的にできるなんてすごく面白そう！エア集約で大規模モデルの課題を解決するなんて、未来の通信技術に期待しちゃうな。

**Comment:** 5 pages, 1 figure, 4 subfigures, letter

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-10 07:12

- - -

### [Theoretical limits of descending  sparse-regression ML algorithms](http://arxiv.org/abs/2410.07651)

**降下型$\ell_0$スパース回帰機械学習アルゴリズムの理論的限界**

Mihailo Stojnic

- $\ell_0$最適化アルゴリズムが、古典的な圧縮センシングやスパース回帰問題を解く際の理論的限界を研究
- 最大尤度（ML）デコーディングの性能を、残差の二乗平均平方根誤差（RMSE）を用いて解析的に評価
- フェイズトランジション（PT）現象を捉えることで、成功・失敗を分けるシステムの次元の曲線を特定
- 数値実験によって、降下型$\ell_0$アルゴリズムの実用的な性能が理論予測に正確に一致することを確認

理論的な予測と小さな次元でのシミュレーション結果がピッタリ一致とか超おもしろいよね！わたしも圧縮センシングを使って、データ処理する機会が増えるかも。これからの技術の発展が楽しみだな！



**トピック:** [連合学習](fl), **カテゴリ:** stat.ML, cs.IT, cs.LG, math.IT, math.ST, stat.TH, **投稿日時:** 2024-10-10 06:33

- - -

### [RealVul: Can We Detect Vulnerabilities in Web Applications with LLM?](http://arxiv.org/abs/2410.07573)

**RealVul: LLMでWebアプリケーションの脆弱性を検出できるか？**

Di Cao, Yong Liao, Xiuwei Shang

- 大規模言語モデルの進展によりソフトウェア脆弱性検出への関心が高まっている
- PHP言語の脆弱性に特化した研究が不足し、サンプル採取と処理の課題がある
- RealVulというLLMベースのフレームワークを開発し、脆弱性候補検出とコード正規化で課題を解決
- 180のPHPプロジェクトで評価を行い、既存手法に対し効果と一般化の向上を実証

PHPの脆弱性に特化したLLMの研究なんて、待ってました！コードセキュリティもどんどんLLMで進化しそうで、この分野がどんな革新をもたらすのか気になるなぁ。PHPを使ってるサービスの安全性もぐっと高くなりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.CL, **投稿日時:** 2024-10-10 03:16

- - -

### [Adaptive Batch Size for Privately Finding Second-Order Stationary Points](http://arxiv.org/abs/2410.07502)

**プライバシーを考慮した二次定常点の適応バッチサイズの発見**

Daogao Liu, Kunal Talwar

- 差分プライバシー制約下でFOSPとSOSPの間にはギャップがある
- 既存研究により、$\alpha$-SOSPの発見に関する具体的なアルゴリズムが示されている
- SpiderBoostアルゴリズムを基に適応バッチサイズとバイナリツリーメカニズムを提案
- 提案手法によりFOSPの状態に匹敵するコストでSOSPを発見可能に

差分プライバシーを守りながら二次定常点を見つけるなんて、すごくチャレンジングな問題に挑んでるね！この研究が進むと、もっと安全で効率的なイノベーションができるようになるかも！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DS, stat.ML, **投稿日時:** 2024-10-10 00:34

- - -

### [Generalizing Segmentation Foundation Model Under Sim-to-real Domain-shift for Guidewire Segmentation in X-ray Fluoroscopy](http://arxiv.org/abs/2410.07460)

**X線透視画像におけるガイドワイヤー分割のためのシミュレーションから現実へのドメインシフトにおけるセグメンテーション基盤モデルの一般化**

Yuxuan Wen, Evgenia Roussinova, Olivier Brina, Paolo Machi, Mohamed Bouri

- 血管内手技のガイドワイヤー分割は手技の正確さを大幅に向上させる可能性がある
- シミュレーションの合成データを活用することで、高価な専門家によるラベル付けを回避できる
- 提案されたフレームワークは、注釈なしでX線透視画像に対してセグメントエニシング（SAM）を適応させる
- 手法を検証した結果、最先端技術を大幅に上回る性能を確認

医療用画像の領域で、データ生成と適応の方法が発展すると、医療現場での画像解析がもっとスムーズになりそうだね！データセットも公開されるみたいだから、他の研究者とも気軽にシェアできそうで楽しみだよー。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-09 21:59

- - -

### [Bayes-Nash Generative Privacy Protection Against Membership Inference Attacks](http://arxiv.org/abs/2410.07414)

**Bayes-Nash生成的プライバシー保護：メンバーシップ推論攻撃に対抗するために**

Tao Zhang, Rajagopal Venkatesaraman, Rajat K. De, Bradley A. Malin, Yevgeniy Vorobeychik

- データ共有は重要だが、個人の参加が重要視されメンバーシップ推論攻撃がプライバシーを脅かす。
- プライバシー保護のためにベイズゲームモデルを提案し、それにより期待効用とプライバシー損失を最小化する。
- Bayes-Nash生成的プライバシーとリスクを導入し、攻撃者の異なる好みにも強いプライバシーと効用のバランスを図る。
- 理論および実証的に、自分たちの方法が要約統計のプライバシー保護において最新の方法を上回ることを示す。

ベイズゲームでプライバシーを守ろうとする発想が面白いね！攻撃者の動きに応じた戦略が練られてるとは、データの世界での駆け引きみたい！将来こういった技術がもっと普及すれば、より安心して情報を共有できる社会が訪れるのかも。

**Comment:** arXiv admin note: substantial text overlap with arXiv:2406.01811

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-09 20:29

- - -

### [Siamese networks for Poincaré embeddings and the reconstruction of evolutionary trees](http://arxiv.org/abs/2410.07387)

**ポアンカレ埋め込みと進化系統樹の再構築のためのシアミーズネットワーク**

Ciro Carvallo, Hernán Bocaccio, Gabriel B. Mindlin, Pablo Groisman

- 高次元データから進化系統樹を再構築する手法を提案
- ポアンカレ埋め込みを用いて次元削減と距離計算を行う
- 葉ノードのサンプルのみから埋め込みを学習するためにシアミーズネットワークを活用
- 合成データとフィンチ6種のスペクトログラムで手法の有効性を実証

進化系統樹を作るのって大変そうだけど、これなら鳥の声からもできちゃうんだね。未来にはもっと多くの生物の進化が明らかになったりして、ワクワクしてくる！

**Comment:** 17 pages, 10 figures

**トピック:** [合成データ](sd), **カテゴリ:** q-bio.PE, cs.LG, **投稿日時:** 2024-10-09 19:10

- - -

### [Benchmarking Data Heterogeneity Evaluation Approaches for Personalized Federated Learning](http://arxiv.org/abs/2410.07286)

**個別化連合学習のためのデータ異質性評価手法のベンチマーク**

Zhilong Li, Xiaohu Wu, Xiaoli Tang, Tiantian He, Yew-Soon Ong, Mengmeng Chen, Qiqi Liu, Qicheng Lao, Xiaoxiao Li, Han Yu

- クライアントのローカルデータセットの統計的異質性を測定する研究が増加中
- 統一されたベンチマークが不足し、手法間での公平な比較が困難
- 新しいベンチマークフレームワークで、異なる非IID FL設定で手法を比較
- データ分散の評価手法の適性に関するガイダンスを提供

データの異質性って興味深いよね。これを使って、PFLの仕組みや適用方法をもっと理解できる感じ。今後、フェアなトレーニングの進化が期待できそう！

**Comment:** Accepted to FL@FM-NeurIPS'24

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-09 13:16

- - -

### [Mitigation of gender bias in automatic facial non-verbal behaviors generation](http://arxiv.org/abs/2410.07274)

**顔面非言語行動生成におけるジェンダーバイアスの軽減**

Alice Delbosc, Magalie Ochs, Nicolas Sabouret, Brian Ravenet, Stephane Ayache

- 非言語行動の生成研究は信憑性や同期に重きを置くが、学習データのバイアスが偏在する
- ジェンダーが顔面非言語行動に与える影響を検討し、特に視線、頭の動き、表情に着目
- スピーカーのジェンダーを非言語行動から識別する分類器を開発、高精度を実現
- FairGenderGenモデルを導入し、音声特徴からジェンダー感受性を緩和した行動生成を達成

ジェンダーバイアスを意識して、顔の非言語行動の公正さを向上させるアプローチって、斬新で時代のニーズにぴったりだね！非言語コミュニケーションの分野で公平なAIが広がれば、新しい社会交流の可能性が生まれそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.HC, cs.LG, cs.NE, **投稿日時:** 2024-10-09 06:41

- - -

### [Boosting the Performance of Decentralized Federated Learning via Catalyst Acceleration](http://arxiv.org/abs/2410.07272)

**カタリスト加速を用いた分散型連合学習の性能向上**

Qinglun Li, Miao Zhang, Yingqi Liu, Quanjun Yin, Li Shen, Xiaochun Cao

- 分散型連合学習は中央集権型よりも学習速度が速く、プライバシー保護と通信負荷が軽減される
- データの不均等性が原因で集中型と比べてモデルの収束が遅く、汎化性能が低下する問題がある
- カタリスト加速としてMoreauエンベロープとNesterovの外挿ステップの2つを導入し解決を図る
- 提案アルゴリズムはCIFAR10/100での実験により収束速度と汎化性能の向上を示している

分散型でパフォーマンスを上げるってワクワクするよね！理論と実験を両立させてるところが頼もしいし、未来の技術に貢献できそうで素敵だなって思う。

**Comment:** arXiv admin note: text overlap with arXiv:2410.06482

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-09 06:17
