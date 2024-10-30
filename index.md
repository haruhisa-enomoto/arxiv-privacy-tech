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

更新: 2024-10-30T04:23:11.521917

- - -

### [Understanding Synthetic Context Extension via Retrieval Heads](http://arxiv.org/abs/2410.22316)

**合成コンテキスト拡張の理解と検索ヘッド**

Xinyu Zhao, Fangcong Yin, Greg Durrett

- 長文コンテキストモデルの需要増、合成データによる拡張で対応
- 合成データの微調整がどのように長文タスク能力に貢献するかは不明
- 合成データでの訓練は実データには劣るが、特定の検索ヘッドで予測可能
- 検索ヘッドの学習がモデル性能に密接に関連、多段階実験でその重要性示す

研究で提案された検索ヘッドって、めちゃくちゃ面白そうじゃない？何かを探したりする時の重要なポイントになるみたいで、タスクの性能向上に役立ちそう！もっといろんなタスクでどれ位使えるか見てみたいなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-29 17:55

- - -

### [: One-shot Private Aggregation with Single Client Interaction and its Applications to Federated Learning](http://arxiv.org/abs/2410.22303)

**$\mathsf{OPA}$: シングルクライアントのシングルインタラクションによる一度限りのプライベート集約とその連合学習への応用**

Harish Karthikeyan, Antigoni Polychroniadou

- シングルサーバー環境でのクライアントの一度限りの発話により、安全な集約を実現
- 複数ラウンドのプロトコルに依存せず、クライアントのドロップアウトや動的参加を容易に管理
- LWRなどの手法を基に、プライバシー保護の連合学習で実用的な性能を発揮
- ロジスティック回帰やMLPで、最先端のソリューションを超える性能をデータセットで確認

クライアントが一度しか話さないなんて、未来感がすごいね！これが実用化されれば、プライバシーも守られてもっと便利な技術がたくさん使えるようになるかもね。どんな変化が起きるか、すごく楽しみだよ！

**Comment:** To appear at the NeurIPS 2024 FL@FM workshop

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, D.4.6; I.2.11; E.3; K.4.1; I.2, **投稿日時:** 2024-10-29 17:50

- - -

### [Auditing -Differential Privacy in One Run](http://arxiv.org/abs/2410.22235)

**1回の実行で行う$f$-差分プライバシーの監査**

Saeed Mahloujifar, Luca Melis, Kamalika Chaudhuri

- 経験的監査はプライバシー保持アルゴリズムの欠陥を見つける手段だが、計算効率が低い
- 提案した監査手順は効率的であり、画期的な分析によりプライバシーを効果的に評価可能
- 1回の実行だけでターゲットメカニズムのプライバシーを監査できるのが特長
- 提案手法は従来の差分プライバシーパラメータを超える精度の高いプライバシー推定を実現

プライバシーを守る方法っていつも計算が大変だけど、この論文は1回で済むのがすごいね！これならAIの活用がもっと安心してできるかも。🖥️🔒



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-29 17:02

- - -

### [Age-: Communication-Efficient Federated Learning Using Age Factor](http://arxiv.org/abs/2410.22192)

**年齢要因を用いた通信効率の高い連合学習**

Matin Mortaheb, Priyanka Kaswan, Sennur Ulukus

- 連合学習はデータの不均一性と通信オーバーヘッドが課題
- 新たなアルゴリズムが情報の年齢メトリックを用いて課題を同時に解決
- パラメータサーバーが年齢ベクトルを用いてクライアントをクラスタリング
- 高効率な学習を実現、他の通信効率戦略を超える成果を示す

情報の年齢を使って効率的に学習を進めるなんて賢いね！これでデータがバラバラでもみんなでうまく連携できそう。次の連合学習界のトレンドになるかもね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, eess.SP, math.IT, stat.ML, **投稿日時:** 2024-10-29 16:30

- - -

### [Synthetic Data Generation with Large Language Models for Personalized Community Question Answering](http://arxiv.org/abs/2410.22182)

**大規模言語モデルによる個人化コミュニティ質問応答のための合成データ生成**

Marco Braga, Pranav Kasela, Alessandro Raganato, Gabriella Pasi

- 個人化情報検索の大規模評価にはデータセットが不足しているが、収集やプライバシーの課題がある
- 大規模言語モデルを用いて合成データを生成し、低リソースタスクのデータ不足問題の解決を目指す
- 合成データセットSy-SE-PQAを作成し、StackExchangeの質問をもとに合成回答を生成
- 合成データはユーザーに最適化でき、人間によるデータを置き換える可能性があるが、誤情報のリスクも

合成データがこんなに役立つとはって感じだね！しかも、プライバシー対策とかコスト削減で利点もいっぱいだし、未来のコミュニティにどんどん活用されそうじゃない？楽しみ～！

**Comment:** Accepted in WI-IAT '24

**トピック:** [合成データ](sd), **カテゴリ:** cs.IR, **投稿日時:** 2024-10-29 16:19

- - -

### [Data Generation for Hardware-Friendly Post-Training Quantization](http://arxiv.org/abs/2410.22110)

**ハードウェアフレンドリーな後処理量子化のためのデータ生成**

Lior Dikstein, Ariel Lapid, Arnon Netzer, Hai Victor Habi

- 零ショット量子化は合成データを使用し、プライバシー制約下で後処理量子化を行う
- 現存手法は全モデル層を量子化するのに適したデータ生成に苦労
- 提案するDGHは生成画像を一括最適化し、データ拡張不足を補い自然画像の特性を利用
- DGHは新たな損失関数を用い、真のデータと合成データの特徴分布を一致させ性能向上

この論文すごく面白そう！ハードウェア全体を使って、プライバシーも守りつつ画像認識をもっと効率良くできるなんて、未来の技術って感じがするよね。生成したデータが本物と同じくらい凄い結果を出すなんて、もっとたくさんの分野で応用が広がりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-29 15:08

- - -

### [A Machine Learning-Based Secure Face Verification Scheme and Its Applications to Digital Surveillance](http://arxiv.org/abs/2410.21993)

**機械学習に基づく安全な顔認証方式とデジタル監視への応用**

Huan-Chih Wang, Ja-Ling Wu

- 顔認証は個人認識で広く使用されるが、プライバシー保護が重要視されていない
- DeepID2とEMアルゴリズムを組み合わせ、顔画像の特徴を抽出し問題を解決
- プライバシー保護のため、準同型暗号を用い暗号化されたデータ上で演算を実施
- プライバシーレベルに応じた3つの監視用顔認証システムを開発し、その実用性を示す

顔認証のプライバシーを守るための技術、めちゃくちゃ重要だね。データを暗号化したまま処理できるなんて、未来の技術って感じでワクワクする！不正アクセスからも守れるし、もっと多くの場面で活用できるといいな。

**Comment:** accepted by International Conference on Digital Image and Signal   Processing (DISP) 2019

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CV, cs.CR, cs.LG, **投稿日時:** 2024-10-29 12:25

- - -

### [Cognitive Semantic Augmentation LEO Satellite Networks for Earth Observation](http://arxiv.org/abs/2410.21916)

**地球観測のための認知的セマンティック拡張LEO衛星ネットワーク**

Hong-fu Chou, Vu Nguyen Ha, Prabhu Thiruvasagam, Thanh-Dung Le, Geoffrey Eappen, Ti Ti Nguyen, Duc Dung Tran, Luis M. Garces-Socarras, Juan Carlos Merlano-Duncan, Symeon Chatzinotas

- 地球観測システムは膨大なデータ処理と送信に苦戦している
- 提案されたフレームワークは、認知処理技術を用いたデータ伝送効率向上を目指す
- DT-JSCCとSAを組み合わせた認知セマンティック処理で性能改善を図る
- 6Gを支える次世代衛星ネットワークにおいて大幅な改善を実現

地球観測って大事だけどデータが大変なんだね。でも、新しい技術で改善できるのかも！次世代の衛星ネットワークって聞くだけでワクワクしちゃう。

**Comment:** 8 Pages, 5 figures, Magazine. arXiv admin note: substantial text   overlap with arXiv:2409.15246

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, **投稿日時:** 2024-10-29 10:15

- - -

### [Optimized Homomorphic Vector Permutation From New Decomposition Techniques](http://arxiv.org/abs/2410.21840)

**新しい分解技術による最適化された準同型ベクトル置換**

Xirong Ma, Junling Fang, Steven Duong, Yali Jiang, Chunpeng Ge

- 準同型置換は、ワード単位の準同型暗号に基づくプライバシー保護計算に不可欠
- 深さ1の理想的な置換分解を提案し、特定の準同型行列転置や乗算で速度と回転キーを改善
- 任意の置換を準同型的に計算する新戦略を開発し、理想的な分解性能の限界に近づく
- 既存技術を超える性能で、最小限の回転キーで速度が最大2.27倍に向上

新しい分解技術で準同型暗号の計算がもっと早くなるかもってワクワクするよね！プライバシーを重視しながら処理速度が上がるのって、とても未来的で素敵なことだと思うな～。

**Comment:** First Submission on 29/10/2024

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-29 08:07

- - -

### [Secure numerical simulations using fully homomorphic encryption](http://arxiv.org/abs/2410.21824)

**完全準同型暗号を用いた安全な数値シミュレーション**

Arseniy Kholod, Yuriy Polyakov, Michael Schlottke-Lakemper

- データプライバシーは現代の多くの環境で重要な懸念事項であり、特にクラウドコンピューティングでの処理が不安定な環境で深刻
- 完全準同型暗号（FHE）は、暗号化されたデータ上で安全な計算を可能にしプライバシー保護に有望な解決策
- CKKSスキームと呼ばれるFHE手法を利用し、Julia言語のOpenFHE.jlとSecureArithmetic.jlパッケージを導入
- FHEを用いた数値シミュレーションは可能だが誤差や効率を慎重に考慮する必要がある

完全準同型暗号って、暗号化したまま計算できちゃうんだね！プライバシーが守られるし、クラウドでの計算も安心感増しそう。数値シミュレーションにも適用できるなんて、技術の進化ってすごいなー！



**トピック:** [準同型暗号](he), **カテゴリ:** math.NA, cs.CR, cs.NA, physics.comp-ph, 65-04, 65M06, 65Y99, **投稿日時:** 2024-10-29 07:47

- - -

### [Online Mirror Descent for Tchebycheff Scalarization in Multi-Objective Optimization](http://arxiv.org/abs/2410.21764)

**多目的最適化におけるチェビシェフ尺度化のオンラインミラーディセント法**

Meitong Liu, Xiaoyuan Zhang, Chulin Xie, Kate Donahue, Han Zhao

- 多目的最適化では、複数の潜在的に対立する目標学習を行う
- 線形尺度化は非凸領域を捉えにくく、パレート最適解の完全回収が難しい
- 本研究では、最悪な場合でも最適化を図るチェビシェフ尺度化を提案
- 提案手法OMD-TCHは合成データと連合学習で最先端の効果を発揮

この論文って、なんか未来のAIがもっと賢く物事を判断できるようになるって感じだよね！フェアネス重視するっていいことだよねー、これからのAI技術にワクワク♪

**Comment:** 27 pages, 7 figures, 2 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-29 05:58

- - -

### [Generating Realistic Tabular Data with Large Language Models](http://arxiv.org/abs/2410.21717)

**大規模言語モデルを用いた現実的な表形式データの生成**

Dang Nguyen, Sunil Gupta, Kien Do, Thin Nguyen, Svetha Venkatesh

- これまでの生成モデルは画像データに強みがあるが、表形式データ生成は少ない
- 大規模言語モデルの成功から表形式データ生成への応用が試みられている
- 提案手法は新たな順列戦略と特徴条件付きサンプリングを用いて相関を捉える
- 生成合成データは高品質かつ多様で、元データと同等の分類器性能を示す

わぁ、大規模言語モデルがますますいろんなデータ生成に使えるなんて素敵っ！合成データが本物みたいに使えるなら、今後の研究の幅広がりそう！みんなも試してみたら面白そうだね～。

**Comment:** To appear at ICDM 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-29 04:14

- - -

### [BF-Meta: Secure Blockchain-enhanced Privacy-preserving Federated Learning for Metaverse](http://arxiv.org/abs/2410.21675)

**BF-Meta: メタバースのためのブロックチェーン強化によるプライバシー保護連合学習**

Wenbo Liu, Handi Chen, Edith C. H. Ngai

- メタバースは仮想サービスを提供するが、セキュリティとプライバシーの課題も存在
- 連合学習はウェアラブルデバイスでユーザープライバシーを保ちながらモデルをトレーニング
- 従来の連合学習は単一障害点の外部攻撃に弱く、インセンティブ不足も問題
- BF-Metaは分散型モデル集約で安全な仮想サービスを提供し、インセンティブ機構も設計

ブロックチェーンと連合学習のタッグがメタバースのプライバシー問題を解決しちゃうんだね！新しい技術をいっぱい取り入れて実験で効果も示してるし、何かとってもワクワクするよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-10-29 02:52

- - -

### [Personalized Federated Learning with Mixture of Models for Adaptive Prediction and Model Fine-Tuning](http://arxiv.org/abs/2410.21547)

**適応予測とモデル微調整のためのモデル混合によるパーソナライズド連合学習**

Pouya M. Ghari, Yanning Shen

- 連合学習はデータのプライバシーを保持しつつ分散モデルを訓練する技術。
- 従来は静的データを仮定していたが、ストリーミングデータ対応が課題。
- クライアントはモデルをオンラインで微調整し、動的環境に適応可能になる。
- 提案手法は個別モデルと連合モデルの混合で予測と微調整を効果的に実現。

クライアントごとに個別対応する連合学習って、今まで以上に個々のデータを尊重しつつ予測精度も上がるなんてすごく良いよね！私たちもこんな技術でますます未来への期待が高まっちゃう！

**Comment:** Accepted to NeurIPS 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-28 21:20

- - -

### [Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](http://arxiv.org/abs/2410.21526)

**全てのLLM生成データが等しいわけではない: テキスト分類におけるデータ重み付けの再考**

Hsun-Yu Kuo, Yin-Hsiang Liao, Yu-Chieh Chao, Wei-Yun Ma, Pu-Jen Cheng

- 大規模言語モデルによる合成データ増強は、現実データが不足するときに下流タスクの性能を向上させる。
- 生成データと実データの不一致は、モデルの応用時に不十分な結果をもたらす。
- 高品質かつ多様な生成データを強調する重み付け手法を提案し、少量の実データを利用。
- BERTレベルモデルの評価では、標準的なクロスエントロピーや他の手法を上回る結果を示した。

同じLLMのデータでも重み付け次第で性能違うんだって。少しの実データを活かして効率アップできるかも？今後色んなデータ生成にも活かせそうでワクワクするね！

**Comment:** 12 pages, 7 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CL, **投稿日時:** 2024-10-28 20:53

- - -

### [Large Language Model Benchmarks in Medical Tasks](http://arxiv.org/abs/2410.21348)

**医療タスクにおける大規模言語モデルのベンチマーク**

Lawrence K. Q. Yan, Ming Li, Yichao Zhang, Caitlyn Heqi Yin, Cheng Fei, Benji Peng, Ziqian Bi, Pohsun Feng, Keyu Chen, Junyu Liu, Qian Niu

- 医療分野での大規模言語モデル（LLM）使用が増加し、ベンチマークデータセットでの評価が重要に
- 論文はLLM医療タスクに用いられる多様なベンチマークデータセットを総合的に調査し分類
- 各データセットはテキスト、画像、マルチモーダルと多様で、診断やレポート生成に関係
- 多言語データセットや革新的な合成手法が求められ、医療AIの進化に貢献する基盤を提供

医療AIってこれからめっちゃ実用化されそうでワクワクするよね！もっと多様なデータとか集まったら、色んな国でもっと活躍しちゃうかも！

**Comment:** 25 pages, 5 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-10-28 11:07
