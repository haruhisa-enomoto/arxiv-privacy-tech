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

更新: 2024-06-06T04:19:33.012168

- - -

### [How to Construct Quantum FHE, Generically](http://arxiv.org/abs/2406.03379)

**量子完全準同型暗号の一般的構築方法**

Aparna Gupte, Vinod Vaikuntanathan

- 古典的な完全準同型暗号から量子完全準同型暗号（QFHE）を構築
- 従来の研究と異なり、非ブラックボックスの使用を避ける方法を提供
- 二重モードトラップドア関数を利用し、クライアントを古典的に変換
- 群作用からの新しい二重モードトラップドア関数を示す

量子暗号の進展が一般的にも適用できたら未来がすごく楽しみになるね！こんな技術がもっと広がると、セキュリティがもっと強くなり全然違う世界が見えそう！



**トピック:** [準同型暗号](he), **カテゴリ:** quant-ph, cs.CR, **投稿日時:** 2024-06-05 15:32

- - -

### [Tiny models from tiny data: Textual and null-text inversion for few-shot distillation](http://arxiv.org/abs/2406.03146)

**小さなデータから小さなモデルへ: 少数ショット蒸留のためのテキストおよびヌルテキスト反転**

Erik Landolsi, Fredrik Kahl

- 少数ショット画像分類は、非常に少ない訓練例で画像を分類するもので、多くのデータが必要
- 本研究では、新しい拡散モデル反転技術（TINT）を提案。この方法は、テキスト反転の多様性とヌルテキスト反転の特異性を組み合わせたもの
- 少数ショット蒸留パイプラインにおいて、TINTを使用することで、小さな学生モデルがおいて最先端の精度を実現
- 合成データ生成を用いる手法は計算負荷が高いため、エピソード数とクエリ例数が精度推定の分散にどう影響するかを理論的に分析し、評価の計算負荷を削減

少数のデータで高精度なモデルが作れるなんて超クール！合成データの生成がいかに役に立つか、もっと知りたくなっちゃう。

**Comment:** 21 pages (9 main pages + references and appendix)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, I.4.0; I.2.6; I.2.10, **投稿日時:** 2024-06-05 11:01

- - -

### [Learning Solutions of Stochastic Optimization Problems with Bayesian Neural Networks](http://arxiv.org/abs/2406.03082)

**ベイジアンニューラルネットワークを用いた確率最適化問題の学習**

Alan A. Lahoud, Erik Schaffernicht, Johannes A. Stork

- 現実世界の設定では、多くのパラメータが未知または不確実なことが多い
- 予測の不確実性をモデル化するためにベイジアンニューラルネットワーク(BNN)を利用
- BNNと数理ソルバーの微分可能な性質を活用し、2つの学習方法を提案
- 提案手法は合成データと実データの評価で決定リグレットが低い（良好である）ことを示す

ベイジアンニューラルネットワークで予測の不確実性を取り入れるなんて、斬新じゃん？実データで評価してるから、現実に応用できそうってとこもいいよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-05 09:11

- - -

### [Towards Federated Domain Unlearning: Verification Methodologies and Challenges](http://arxiv.org/abs/2406.03078)

**連合ドメイン消去に向けて：検証手法と課題**

Kahou Tam, Kewei Xu, Li Li, Huazhu Fu

- 連合学習は共同モデルトレーニングのための強力なツールであるが、RTBFの導入は新たな課題を生む
- 従来の連合学習の消去方法は、多ドメインシナリオでは不十分で、モデルの精度を低下させる
- 既存の方法は、ドメイン固有データの影響を無視するため、特に深層層での学習内容が消去される
- 新たな評価方法を提案し、ドメイン固有データの消去を正確に検証し、モデルの整合性と性能を維持

RTBFってどんなんだろう？必要だよね～。でも、複数の分野で使うなら、一筋縄ではいかないんだな。この論文、そこに挑戦するのめっちゃ面白そう！

**Comment:** 16 pages, 12 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-05 09:05

- - -

### [PrE-Text: Training Language Models on Private Federated Data in the Age of LLMs](http://arxiv.org/abs/2406.02958)

**PrE-Text: LLM時代におけるプライベートな連合データでの言語モデルのトレーニング**

Charlie Hou, Akshat Shrivastava, Hongyuan Zhan, Rylan Conway, Trang Le, Adithya Sagar, Giulia Fanti, Daniel Lazar

- オンデバイス学習は多くの課題があり、大型モデルの学習には適していない
- PrE-Textは差分プライバシー合成データを用いてこれらの課題を解決
- 小型モデルをPrE-Textで学習させると、オンデバイスよりも高性能
- 大型モデルの微調整もプライベートデータで改善されることが示された

PrE-Textは差分プライバシーを駆使して、通信量や計算量を大幅に削減してるんだって！これからのプライバシー技術にとって超期待できるよね。

**Comment:** ICML 2024 (Oral)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, cs.CR, cs.DC, **投稿日時:** 2024-06-05 05:27

- - -

### [FedStaleWeight: Buffered Asynchronous Federated Learning with Fair Aggregation via Staleness Reweighting](http://arxiv.org/abs/2406.02877)

**FedStaleWeight: 停滞の重み付けによるフェアな集約を実現するバッファード非同期連合学習**

Jeffrey Ma, Alan Tu, Yiling Chen, Vijay Janapa Reddi

- FLはプライバシーを保ちつつ分散データを活用するが、性能やスケーラビリティの課題がある
- 非同期FLはアプローチとして有望だが、収束保証や計算異質性に関する公平性が課題
- FedStaleWeightは平均停滞時間を利用して、非同期クライアント更新の公平な重み付けを実現
- 理論的収束保証を提供し、FedBuffと比較して公平性と収束速度の面で優れていることを実証

公平性と収束速度を両立させる新しい方法、気になるよね。FedStaleWeightの実践検証も楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-05 02:52

- - -

### [Auditing Privacy Mechanisms via Label Inference Attacks](http://arxiv.org/abs/2406.02797)

**ラベル推論攻撃によるプライバシー機構の監査**

Róbert István Busa-Fekete, Travis Dick, Claudio Gentile, Andrés Muñoz Medina, Adam Smith, Marika Swanberg

- 再構築優位性測度を提案し、ラベルのプライバシー保護機構を監査する
- 再構築優位性測度は攻撃者が真のラベルを推測する能力の増加を定量化する
- この測度は理論的モデルと実験による評価で効果を確認
- 実験では差分プライバシー手法が他のアプローチより優位に立つ

これめっちゃ面白そう！差分プライバシーの手法がやっぱり強いんだね。新しいプライバシー技術の進化に期待しちゃうよね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-04 21:48

- - -

### [PriME: Privacy-aware Membership profile Estimation in networks](http://arxiv.org/abs/2406.02794)

**PriME: ネットワークにおけるプライバシー考慮のメンバーシッププロファイル推定**

Abhinav Chakraborty, Sayak Chatterjee, Sagnik Nandy

- 個々のエッジのプライバシーを保持しながら、ネットワークの頂点のコミュニティメンバーシップ確率を推定する新しい手法を提案
- $\varepsilon$-エッジローカル差分プライバシーフレームワークに基づき、対称的なエッジフリップ機構とスペクトルクラスタリングを用いた最適なプライベートアルゴリズムを導入
- 推定リスクの包括的な分析を行い、プライバシー制約下での手法の最適性を最小最大リスクの下限値で示す
- 数値シミュレーションと実データを使って方法の性能を検証することで、実際の適用性を明らかに

個々のエッジのプライバシーを保ちながらネットワーク解析するの面白そう！実データでの検証もしてるから、本当に使えそうだね。どこで実践されるか楽しみだな～



**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ME, cs.SI, math.ST, stat.TH, **投稿日時:** 2024-06-04 21:43

- - -

### [Private Stochastic Convex Optimization with Heavy Tails: Near-Optimality from Simple Reductions](http://arxiv.org/abs/2406.02789)

**重い尾を持つプライベート確率凸最適化: 単純な削減からのほぼ最適性**

Hilal Asi, Daogao Liu, Kevin Tian

- 重い尾を持つ勾配で差分プライベートな確率凸最適化（DP-SCO）を研究
- 新しい削減ベースのアプローチで重い尾の設定で最初の最適レートを達成
- 既知のリプシッツ定数の仮定下で最適アルゴリズムを提案
- 平滑関数のためにほぼ線形時間のアルゴリズムも提示

重い尾を持つデータを使っても差分プライバシーを確保できる方法を探るなんて面白そう！しかも、効率的なアルゴリズムを取り入れてるのがすごいね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, cs.LG, stat.ML, **投稿日時:** 2024-06-04 21:26

- - -

### [Synthetic Data Outliers: Navigating Identity Disclosure](http://arxiv.org/abs/2406.02736)

**合成データ外れ値：アイデンティティ開示の航路**

Carolina Trindade, Luís Antunes, Tânia Carvalho, Nuno Moniz

- 深層学習モデルが合成データ生成において主導的役割を果たす
- 合成データが元のデータに酷似しているため、個人情報保護の問題が生じる
- 再同定リスクの影響を無視しがちで、特に外れ値のプライバシーに関する研究が少ない
- 差分プライバシーなどの追加対策は再同定を防ぐが、データの有用性が減少する

外れ値にも気を配るの、大事なんだね。個人情報の保護とデータの有用性のバランスってすごく難しいみたい。でも、未来のプライバシー技術に期待が持てる内容だったよ！



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-04 19:35

- - -

### [Differentially private exact recovery for stochastic block models](http://arxiv.org/abs/2406.02644)

**確率ブロックモデルにおける差分プライバシーを用いた正確なコミュニティ復元**

Dung Nguyen, Anil Vullikanti

- 確率ブロックモデル（SBM）はコミュニティ検出アルゴリズムで広く研究されている
- SBMのコミュニティ構造をプライバシー保護下で復元する問題に焦点を当てる
- 非対称SBM、一般構造SBM、検閲SBMの3つのバージョンについて条件を導出
- 提案するプライベートアルゴリズムは多項式時間で、非プライベートな設定に匹敵する復元閾値を持つ

差分プライバシーを保持しつつ、効率的にコミュニティ復元ができるなんて、未来のネットワーク解析に期待大！これで安心してデータ使えるかもね！

**Comment:** Accepted by ICML 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.DS, **投稿日時:** 2024-06-04 12:38

- - -

### [Mixed-Precision Over-The-Air Federated Learning via Approximated Computing](http://arxiv.org/abs/2406.03402)

**近似計算による混合精度の無線連合学習**

Jinsheng Yuan, Zhuangkun Wei, Weisi Guo

- 既存のOTA-FL研究は均一なクライアント計算精度を前提としている課題がある
- エネルギー効率と計算効率のためにビット精度を調整する近似計算（AxC）を利用する提案
- サーバとクライアントの量子化性能を最適化し、異なるエッジコンピューティング能力に対応する
- 物理層のOTA集約と互換性のある異種の勾配解像度のOTA-FL変調スキームを開発

この研究すごーい！エネルギー効率を考えた新しいアプローチで、クライアントの性能を最大限に活かす未来が見えるね。早く試してみたいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-04 09:07

- - -

### [ST-DPGAN: A Privacy-preserving Framework for Spatiotemporal Data Generation](http://arxiv.org/abs/2406.03404)

**ST-DPGAN: 時空間データ生成のためのプライバシー保護フレームワーク**

Wei Shao, Rongyi Zhu, Cai Yang, Chandra Thapa, Muhammad Ejaz Ahmed, Seyit Camtepe, Rui Zhang, DuYong Kim, Hamid Menouar, Flora D. Salim

- 時空間データは個人通信や金融取引などに多く存在し、しばしば機密情報を含む
- 提案手法はGraph-GANベースのモデルで、時空間データをプライバシー保護しつつ生成
- 空間と時間のアテンションブロックや時空間デコンボリューション構造を統合し、差分プライバシーを実現
- 実験では提案手法が3つの実データセットで効果を示し、データの有用性を保ちながら予測モデルの性能を維持

この手法を使えば、プライバシーをしっかり守りつつデータの有用性も維持できちゃうんだね！未来の技術がどんどん身近に感じられてワクワクする！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-06-04 04:43

- - -

### [ACCO: Accumulate while you Communicate, Hiding Communications in Distributed LLM Training](http://arxiv.org/abs/2406.02613)

**ACCO：通信中の集積、分散LLMトレーニングにおける通信の隠蔽**

Adel Nabli, Louis Fournier, Pierre Erbacher, Louis Serrano, Eugene Belilovsky, Edouard Oyallon

- 大規模言語モデル（LLM）のトレーニングは分散実装に依存し、多数のGPUが並行して確率的勾配を計算
- データ並列設定での勾配同期は通信オーバーヘッドを引き起こし、効果的な並列化を妨げる
- 提案するACCOは、ワーカー間の通信を隠しながらオプティマイザの状態を分散させ、メモリ効率を向上
- ACCOは勾配計算と通信を重ね合わせ、通信遅延を軽減し従来の分散最適化に比べて高速収束を実現

並列処理の通信オーバーヘッドをどう減らすかってすごく重要だよね！ACCOみたいな新技術で効率が上がれば、もっと大規模なモデルもお手軽に扱えるようになりそう。未来のAIには期待が高まるね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-03 08:23

- - -

### [PPINtonus: Early Detection of Parkinson's Disease Using Deep-Learning Tonal Analysis](http://arxiv.org/abs/2406.02608)

**PPINtonus: 深層学習を用いたパーキンソン病早期検出のためのトーン解析**

Varun Reddy

- PPINtonusは、深層学習によるトーン解析を用いたパーキンソン病の早期検出システム
- 条件付き生成対向ネットワークで合成データを生成し、データセットを強化
- 120秒の音声テストとPRAAT音声学ソフトを組み合わせ、92.5%の高精度を達成
- 非侵襲かつ効率的な方法で、発展途上国での早期診断と生活の質向上に寄与

この技術、発展途上国でも使えたらすごくイイと思わない？患者さんが元気に生活できるようになったら、嬉しいよね。



**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.AI, cs.LG, **投稿日時:** 2024-06-03 01:07

- - -

### [A Novel Defense Against Poisoning Attacks on Federated Learning: LayerCAM Augmented with Autoencoder](http://arxiv.org/abs/2406.02605)

**連合学習に対する毒性攻撃防御策の新手法：オートエンコーダを用いたLayerCAM**

Jingjing Zheng, Xin Yuan, Kai Li, Wei Ni, Eduardo Tovar, Jon Crowcroft

- 連合学習（FL）における毒性攻撃を防ぐため、LayerCAMとオートエンコーダ（AE）を統合した新防御戦略LayerCAM-AEを提案。
- LayerCAM-AEは各ローカルモデル更新のヒートマップを生成し、よりコンパクトな視覚形式に変換することで検出能力を向上。
- 誤検出リスクを軽減するため、複数回の通信ラウンドでヒートマップが一貫して疑わしい場合にマリシャスモデルとみなす投票アルゴリズムを開発。
- SVHNおよびCIFAR-100データセットでの実験結果、LayerCAM-AEはResNet-50およびREGNETY-800MFよりも高い検出率とテスト精度を示し、FL性能を向上させる。

この研究は連合学習における毒性攻撃の検出精度を大幅に向上できるなんてすごく未来が明るいね！これからのセキュリティ対策がどう進化していくのか、ワクワクしちゃうな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.CV, cs.LG, **投稿日時:** 2024-06-02 12:37

- - -

### [Privacy-Aware Randomized Quantization via Linear Programming](http://arxiv.org/abs/2406.02599)

**線形プログラミングによるプライバシー対応ランダム化量子化**

Zhongteng Cai, Xueru Zhang, Mohammad Mahdi Khalili

- 差分プライバシー機構は個人情報保護に広く使われるが、主に連続出力向けに設計されている
- 離散値が必要なシナリオでは、既存の量子化機構はバイアスがあるか、精度-プライバシートレードオフが劣る
- 本研究ではバイアスがなく差分プライバシーを提供する新しい量子化機構を提案する
- 提案する量子化機構は高い自由度があり、既存の機構を特別なケースとして含むことができる

新しい量子化機構が提案されてて、ほんとに効果あるのか実験で見せてくれるの、わくわくするよね！私たちもデータを使うときにもっと安心できる道が増えるかも♪



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-06-01 18:40

- - -

### [Capturing Climatic Variability: Using Deep Learning for Stochastic Downscaling](http://arxiv.org/abs/2406.02587)

**気候変動の捉え方：確率的ダウンスケーリングにおける深層学習の利用**

Kiri Daust, Adam Monahan

- 気候変動に対応するためには、正確な地域気候情報が必要であり、計算が難しい問題である
- 生成的敵対ネットワーク（GAN）が気候変数の効率的なダウンスケーリングに利用されている
- GANの確率的キャリブレーションを改善するため、ネットワーク内のノイズ注入、学習プロセスの調整、確率的損失メトリックの使用を提案
- 最良のモデルは、全バリエーションを捉える能力が向上し、極端な気象イベントの特定に優れる

GANを使って気候の微妙な変動も捉えられるんだって！どんどん精度が上がって、将来の気候予測がもっと正確になりそうね。気候変動への適応策もこれからさらに進みそうでワクワクするね！

**Comment:** Submitted to Artificial Intelligence for the Earth Systems AMS   Journal

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-05-31 03:04
