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

更新: 2024-12-04T04:23:01.205405

- - -

### [On Domain-Specific Post-Training for Multimodal Large Language Models](http://arxiv.org/abs/2411.19930)

**ドメイン特化型マルチモーダル大規模言語モデルのポストトレーニングについて**

Daixuan Cheng, Shaohan Huang, Ziyu Zhu, Xintong Zhang, Wayne Xin Zhao, Zhongzhi Luan, Bo Dai, Zhenliang Zhang

- アカデミックと産業用途への適応は未開拓であり、MLLMのドメイン適応を研究
- 合成データを使い、ドメイン画像キャプションから視覚タスクを効果的に生成
- 単一段階のトレーニングパイプラインを導入しタスク多様性を向上
- バイオメディカルと食品の領域でMLLMを評価し、さらに実装をオープンソース化予定

科学と食の世界で、進化したマルチモーダル言語モデルがどんなユニークな結果をもたらすのかワクワクする。特に、合成データの力でこれまでにない方法を試すなんて、ますます興味津々な未来が広がりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.CV, cs.LG, **投稿日時:** 2024-11-29 18:42

- - -

### [Rethinking the initialization of Momentum in Federated Learning with Heterogeneous Data](http://arxiv.org/abs/2411.19798)

**連合学習におけるモーメンタム初期化の再考：異種データ対応**

Chenguang Xiao, Shuo Wang

- データの異種性は連合学習の主要な課題であり、最近はモーメンタムベースの最適化手法がその緩和に効果的とされる
- 従来のモーメンタム蓄積法は連合学習環境には最適でなく、古い勾配より新しい勾配を重視するためバイアスが生じやすい
- 新手法「逆モーメンタム連合学習（RMFL）」を提案し、時間が経つにつれ勾配へ指数的に減衰する重みを与えるアプローチを採用
- 提案手法の有効性は異なる異種性レベルを持つ3つのベンチマークデータセットで評価

モーメンタムに対する新しいアプローチがどれくらいパフォーマンスを向上させるのか気になるよね！これで連合学習がもっと柔軟に異種データを扱えるようになったら嬉しいな～。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-29 16:00

- - -

### [MIMDE: Exploring the Use of Synthetic vs Human Data for Evaluating Multi-Insight Multi-Document Extraction Tasks](http://arxiv.org/abs/2411.19689)

**合成データ対人間データの使用を探る多視点多文書抽出タスク評価**

John Francis, Saba Esnaashari, Anton Poletaev, Sukankana Chakraborty, Youmna Hashem, Jonathan Bright

- 複雑なテキスト分析タスクの評価は困難で、MIMDEを定義して取り組む
- MIMDEは文書から洞察を抽出しその出典に紐づけるタスク
- ヒューマンと合成データセットを使った評価フレームワークを開発
- 合成データは完全な分析の再現が難しく、限界があることが判明

うわー、合成データと人間データを比べるなんて面白いね！課題だけど、この研究で解決策が見つかると良いなー。🌟✨



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-11-29 13:24

- - -

### [Diorama: Unleashing Zero-shot Single-view 3D Scene Modeling](http://arxiv.org/abs/2411.19492)

**ディオラマ：ゼロショットでの単一視点3Dシーンモデリングの開放**

Qirui Wu, Denys Iliash, Daniel Ritchie, Manolis Savva, Angel X. Chang

- 単一のRGB画像から3Dシーンを再構築する技術で、CADオブジェクトを利用して効率性と相互作用を維持
- 既存方法では高コストな現実世界のアノテーションや制御可能だが一般化しにくい合成データを使用
- ディオラマはゼロショットで、トレーニングやアノテーションなしで3Dシーンをモデリング可能
- 我々の手法は、アーキテクチャ再構築、3D形状取得、物体位置推定、シーン配置最適化のサブタスクで構成されている

この研究ってめっちゃ興味深いね！ゼロショットでできちゃうところが特におもしろいし、実生活の画像からシーンモデリングできる未来が楽しみ〜。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-11-29 06:19

- - -

### [Gradient Inversion Attack on Graph Neural Networks](http://arxiv.org/abs/2411.19440)

**グラフニューラルネットワークに対する勾配逆転攻撃**

Divya Anand Sinha, Yezi Liu, Ruijie Du, Yanning Shen

- グラフ連合学習は、大規模なグラフデータセットでのトレーニングに重要だがプライバシーを守る。
- 既存の研究では、悪意ある攻撃者が連合学習中にプライベート画像データを盗む可能性が指摘されている。
- グラフデータとグラフニューラルネットワークの脆弱性について研究し、新たな攻撃「GLG」を提案。
- GCNとGraphSAGEのフレームワークで理論的および実証的な検証を行い、グラフデータの漏洩を確認。

グラフデータが漏洩するなんてちょっとびっくり。未来のデータプライバシーがちゃんと守られるように、新しい対策が生まれるといいね。連合学習の世界もまだまだ進化しそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-29 02:42

- - -

### [PEFT-as-an-Attack! Jailbreaking Language Models during Federated Parameter-Efficient Fine-Tuning](http://arxiv.org/abs/2411.19335)

**連合パラメータ効率的ファインチューニング中の言語モデルの脱獄**

Shenghui Li, Edith C. -H. Ngai, Fanghua Ye, Thiemo Voigt

- 連合パラメータ効率的ファインチューニング（FedPEFT）は、プライバシーを保護しつつ効率的なモデル適応を実現する。
- FedPEFTはデータを分散化し、ローデータがユーザーのデバイスを離れないようにすることでデータプライバシーを保護する。
- 本論文はPEFTが攻撃のベクトルとして利用される新たなセキュリティ脅威、PEFT-as-an-Attackを紹介する。
- 防御策として、ロバスト・アグリゲーション・スキームやポストPEFT安全性調整を調査するも、効果には限界がある。

プライバシーを守るための工夫が悪用されちゃうなんてドキドキ！効果的な防御策ができたら、もっと安全に連合学習を活用できそうで楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-11-28 19:05

- - -

### [Controlling Participation in Federated Learning with Feedback](http://arxiv.org/abs/2411.19242)

**フィードバックによる連合学習への参加管理**

Michael Cummins, Guner Dilsad Er, Michael Muehlebach

- 従来の連合学習はクライアントのランダム選択を行うが、FedBackは異なる
- FedBackは制御理論を用い、クライアント参加をADMMベースで管理する
- クライアント参加を離散時間動的システムとしてモデル化し、フィードバック制御を行う
- 画像分類実験でFedBackにより通信と計算効率が50％改善される

FedBackってすごい！制御理論で参加率を最適化するなんて、なんだか学校の通知表みたい。しかも効率が50％もアップするなんて、これからの連合学習がもっと実用的になるのが楽しみ～✨



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, math.OC, **投稿日時:** 2024-11-28 16:26

- - -

### [Parallel and Mini-Batch Stable Matching for Large-Scale Reciprocal Recommender Systems](http://arxiv.org/abs/2411.19214)

**大規模相互レコメンダーシステムのための並列およびミニバッチ安定マッチング**

Kento Nakada, Kazuki Kawamura, Ryosuke Furukawa

- 二者間マッチングプラットフォームで推奨が偏り、全体のマッチ数が減少する問題
- 伝達可能効用を持つ安定マッチング理論が適用されるが、計算コストとメモリの効率の課題
- 並列計算とミニバッチ法を用い、計算時間と空間効率を改善する新手法を提案
- 実験で提案手法が計算速度を向上させ、大規模データ処理が可能であることを確認

この研究は、マッチングの理論を巧妙に使って効率をめっちゃ上げてる感じだね！大規模データを処理できるなんて、これからのオンラインマッチングサービスがどんどん進化しそうでワクワクするよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.IR, **投稿日時:** 2024-11-28 15:36

- - -

### [Personalized Federated Fine-Tuning for LLMs via Data-Driven Heterogeneous Model Architectures](http://arxiv.org/abs/2411.19128)

**LLMのためのデータ駆動型異種モデルアーキテクチャを用いたパーソナルな連合微調整**

Yicheng Zhang, Zhen Qin, Zhaomin Wu, Shuiguang Deng

- 分散学習はデータ共有せずに協力的微調整が可能だが、データ量や分布の異質性が問題
- 一様なモデル構造や事前定義のアーキテクチャでは性能が最適でない
- FedAMoLEはデータ駆動型で異種モデル構造を活用し、効果的な微調整を実現
- RSEA戦略により専門家が最適なクライアントを選び、高い精度とスケーラビリティを達成

データに合わせたモデル選びで性能がアップするなんて、面白いよね！この研究、現場での適用例なんかも見てみたいなって思ったよ。

**Comment:** On going work. Codes are released at   https://github.com/zyc140345/FedAMoLE

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-28 13:20

- - -

### [Swarm Intelligence-Driven Client Selection for Federated Learning in Cybersecurity applications](http://arxiv.org/abs/2411.18877)

**サイバーセキュリティアプリケーションにおける連合学習のための群知能駆動クライアント選択**

Koffka Khan, Wayne Goodridge

- 群知能最適化を用いた連合学習のクライアント選択に関する文献のギャップを考察
- パーティクル群最適化やグレイウルフ最適化など9つのアルゴリズムを4つの実験シナリオで評価
- 特にGWOが適応性と堅牢性で最高の精度を達成し、PSOとカッコウ検索も好成績
- サイバーセキュリティへの応用で、群知能アルゴリズムがスケーラブルかつ堅牢な解決策を提供可能

群知能アルゴリズムがサイバーセキュリティにどう活かせるかワクワクしちゃうね！特にGWOが強いって知れて、未来の技術革新が楽しみになる～。

**Comment:** 21 pages, 1 figure, 15 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, 68T20, 68M25, I.2.8; C.2.0; K.6.5, **投稿日時:** 2024-11-28 03:05

- - -

### [Reconstructing Animals and the Wild](http://arxiv.org/abs/2411.18807)

**動物と自然の再構築**

Peter Kulits, Michael J. Black, Silvia Zuffi

- 3D復元はコンピュータビジョンの基礎であり、2D観察から構造を推測するための強い事前情報が必要
- 従来の研究は動物の再構築に偏っていたが、環境の文脈を無視することで有用性が限定される
- 本研究は、CLIP埋め込みと自己回帰モデルを使って動物と自然を包含するシーンを再構成する方法を提案
- 合成データセットのトレーニングにより、実際の画像でも動物と環境の再構築が可能

動物とその周りの環境を一緒に再構成できるなんて、すごく便利になりそう！リアルなシーンの分析がもっと進むってことかな？新しいデータセットの公開も楽しみだよね！

**Comment:** 12 pages; project page: https://raw.is.tue.mpg.de/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, **投稿日時:** 2024-11-27 23:24

- - -

### [Locally Differentially Private Online Federated Learning With Correlated Noise](http://arxiv.org/abs/2411.18752)

**時間相関のあるノイズを用いた局所的差分プライバシーのオンライン連合学習**

Jiaojiao Zhang, Linglingzhi Zhu, Dominik Fay, Mikael Johansson

- 局所的差分プライバシー(LDP)アルゴリズムを提案し、時間相関ノイズでプライバシーを保護しつつ効用を向上。
- 相関ノイズと非IIDデータに対抗するため、ノイズの影響を制御するための摂動反復解析を行う。
- 非凸損失関数のいくつかのクラスで、ローカル更新によるドリフト誤差を効果的に管理する方法を示す。
- 数値実験により提案アルゴリズムの有効性が確認され、学習効果への影響を動的後悔境界で評価する。

新しいノイズの取り扱い方法が個々のユーザーのデータを守りながら学習パフォーマンス向上につながるのは面白いね！これからのプライバシー研究が楽しみだな。

**Comment:** arXiv admin note: text overlap with arXiv:2403.16542

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, stat.ML, **投稿日時:** 2024-11-27 20:56

- - -

### [Inference Privacy: Properties and Mechanisms](http://arxiv.org/abs/2411.18746)

**推論プライバシー：特性とメカニズム**

Fengwei Tian, Ravi Tandon

- 公開モデルの出力からユーザーのプライベート入力を復元されるリスクがある
- 推論段階でのデータのプライバシーを保証する、推論プライバシー(IP)を提案
- 推論プライバシー(IP)の基本的な特性を導き出し、LDPとの違いを示す
- ユーザーカスタマイズ可能な入力・出力摂動でプライバシーと有用性のトレードオフを調査

推論プライバシーって、新しい考え方で面白いかも！自分でプライバシーをコントロールできるのがいいね。今後もっと研究が進んで、身近なサービスにも取り入れられたらいいなって思った。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.IT, cs.LG, math.IT, **投稿日時:** 2024-11-27 20:47

- - -

### [RoMo: Robust Motion Segmentation Improves Structure from Motion](http://arxiv.org/abs/2411.18650)

**RoMo: 頑強な動作分割が構造から運動を改善する**

Lily Goli, Sara Sabour, Mark Matthews, Marcus Brubaker, Dmitry Lagun, Alec Jacobson, David J. Fleet, Saurabh Saxena, Andrea Tagliasacchi

- 4Dシーンの生成には構造から運動への技術が必要で、動と静の分割が重要
- RoMoは光の流れとエピポーラキューを用いる効果的な方法を提案
- 合成データで学習した手法や非教師あり手法を性能で上回る
- 動的なコンテンツを含むシーンで、新しいカメラ校正精度を実現

この研究、すごく面白そう！特に、動的なシーンでのカメラ校正が大幅に向上するなんて、映画やゲームの品質がもっとアップしそう！楽しみね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-27 01:09
