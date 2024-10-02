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

更新: 2024-10-02T04:24:18.582922

- - -

### [Devil is in Details: Locality-Aware 3D Abdominal CT Volume Generation for Self-Supervised Organ Segmentation](http://arxiv.org/abs/2409.20332)

**細部に潜む悪魔：自己教師あり臓器セグメンテーションのための局所性認識型3D腹部CTボリューム生成**

Yuran Wang, Zhijing Wan, Yansheng Qiu, Zheng Wang

- 医療画像解析における自己教師あり学習（SSL）技術は、ラベル付けの負担を軽減するが、データ不足は依然として課題
- 腹部の複雑で微細な解剖構造が他の部位と比べてCTボリューム生成を困難にしている
- 状況認識型拡散（Lad）という新しい方法を提案し、局所性ロスと腹部事前知識を組み込むことで高品質な腹部CTを生成
- 提案手法は既存の方法を超え、自己教師あり臓器セグメンテーションタスクにおいて平均Diceスコアを向上させた

腹部への特化って面白いね！これがもっと発展すれば、医療現場でのデータ不足も解消できるかもしれないよ。私たちも医学について勉強しようかな。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-09-30 14:35

- - -

### [Fine-Tuning Personalization in Federated Learning to Mitigate Adversarial Clients](http://arxiv.org/abs/2409.20329)

**連合学習における個別化の微調整で敵対的クライアントを軽減**

Youssef Allouah, Abdellah El Mrini, Rachid Guerraoui, Nirupam Gupta, Rafael Pinot

- クライアント間のデータ分布の異質性がモデル性能に悪影響を与える
- 個別化によって各クライアントに最適なモデルを作成しつつ、他のデータも活用
- 敵対的クライアントの存在下での連合学習の一般化性能を分析
- データの異質性と許容可能な敵対的クライアントの割合に応じた協力の調整が必要

敵対的なクライアントがいる中での連合学習のパフォーマンス向上に取り組むなんて面白そう！クライアントに合わせた細かな調整が未来の鍵になるかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-09-30 14:31

- - -

### [OPONeRF: One-Point-One NeRF for Robust Neural Rendering](http://arxiv.org/abs/2409.20043)

**OPONeRF: 頑強なニューラルレンダリングのためのワンポイントワンNeRF**

Yu Zheng, Yueqi Duan, Kangfu Zheng, Hongru Yan, Jiwen Lu, Jie Zhou

- 既存のNeRFは、訓練とテスト中にシーンが変わらないという前提に基づいて設計されている
- OPONeRFは、局所のシーン変動に適応するために点ごとのパラメータを適用するアプローチを提案
- 点表現を決定論的マッピングと確率的推論に分解し、予測不可能なシーン変動をモデル化
- 実際的および合成データを用いたベンチマーク実験で、先行研究に比べて高い性能を示した

この研究、注目すべきポイント多いよね！特にリアルなシーン変動に対応するところ、すごく面白そう。もっと多様なシーンでも試してみたくなるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-30 07:49

- - -

### [Enhancing Security Using Random Binary Weights in Privacy-Preserving Federated Learning](http://arxiv.org/abs/2409.19988)

**プライバシー保護連合学習におけるランダムバイナリ重みを用いたセキュリティ強化**

Hiroto Sawada, Shoko Imaizumi, Hitoshi Kiya

- 連合学習で生のデータを収集せずに更新情報のみで学習するが、その情報からデータが推測される問題がある
- 従来の対策にはプライバシー保護と学習効率のトレードオフがあり、モデル性能が低下する
- 提案手法はランダムバイナリ重みを用い、更新情報へのデータ推測攻撃に強く、モデル性能を低下させない
- 実験で、APRIL（Attention PRIvacy Leakage）復元攻撃に対する耐性とモデル性能の有効性を確認

新しいセキュリティ技術ってすごくわくわくするよね！データのプライバシーを守りつつ高性能を保つなんて、未来の連合学習がもっと安心して使えるようになるかも。

**Comment:** 6pages, 17figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-30 06:28

- - -

### [CONTESTS: a Framework for Consistency Testing of Span Probabilities in Language Models](http://arxiv.org/abs/2409.19984)

**CONTESTS: 言語モデルにおけるスパン確率の一貫性テストのフレームワーク**

Eitan Wagner, Yuli Slavutsky, Omri Abend

- 言語モデルの確率としての信頼性はキャリブレーションを通じて主に研究されてきたが、他の側面は見過ごされている
- ConTestSフレームワークを導入し、統計テストを使用してスコアの一貫性を評価
- 実験により、マスク言語モデル（MLM）との自己回帰モデルは不一致な予測を示した
- 大きなMLMは一貫性が高く、自己回帰モデルは一貫性が低い傾向があることが明らかに

言語モデルの出力って、確率として信じすぎちゃダメなんだね。自己回帰モデルが一貫性低いのはちょっと意外！デコード戦略の選び方にまで影響あるなんて、面白い方向に進むかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-09-30 06:24

- - -

### [Violina: Various-of-trajectories Identification of Linear Time-invariant Non-Markovian Dynamics](http://arxiv.org/abs/2409.19978)

**Violina: 線形時不変非マルコフ力学系の多軌道識別**

Ryoji Anzaki, Kazuhiro Sato

- Violinaは、新しいシステム識別法である
- 状態空間モデルとメモリカーネルの係数行列を最適化して予測を観測データに一致させる
- 合成データを用いて、Violinaが既存の動的分解法よりも一般化性能が優れていることを実証
- 事前知識に基づく制約を考慮して非マルコフ動力学系を識別可能

めっちゃ面白そう！Violinaのやり方だと、複雑なシステムももっと正確にモデリングできるかもね。しかも、一般化性能が高いっていうのは、今後さらに多くの分野で活用できそうでワクワクしちゃう。



**トピック:** [合成データ](sd), **カテゴリ:** math.OC, cs.LG, **投稿日時:** 2024-09-30 06:04

- - -

### [Comments on "Privacy-Enhanced Federated Learning Against Poisoning Adversaries"](http://arxiv.org/abs/2409.19964)

**「毒性攻撃者に対するプライバシー強化型連合学習」へのコメント**

Thomas Schneider, Ajith Suresh, Hossein Yalame

- PEFLは準同型暗号を用いて毒性行動を検出するフレームワークを提案
- PEFLはすべてのユーザーの勾配ベクトルを明らかにするため、プライバシーを維持しない
- 提案されたシステムに複数の欠陥があり、即時修正ではプライバシーを確保できない
- PEFLの問題点を認識せずに引用や採用する研究が後を絶たない

PEFLのフレームワーク、実際はプライバシー全然守れていないとか驚きだね！これからの研究にも影響大きそうだから、ちゃんとチェックしなきゃだね。

**Comment:** Published at IEEE Transactions on Information Forensics and   Security'23

**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-09-30 05:34

- - -

### [Leveraging Pre-trained Models for Robust Federated Learning for Kidney Stone Type Recognition](http://arxiv.org/abs/2409.19934)

**腎臓結石タイプ認識のための堅牢な連合学習のための事前学習モデルの活用**

Ivan Reyes-Amezcua, Michael Rojas-Ruiz, Gilberto Ochoa-Ruiz, Andres Mendez-Vazquez, Christian Daul

- 深層学習の進展が医療画像診断の精度を劇的に向上
- 巨大なデータセットの必要性とデータ交換の法的制限が障壁
- 事前学習モデルを用いた強力な連合学習フレームワークを提案
- 連合学習の堅牢性と診断精度の向上を示し、患者ケアの改善が期待できる

これ、プライバシーを守りながらも高精度な診断ができるなんて⤴絶対おもしろそうだよね。医療における新たな信頼の形になるかも💖🎵



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-30 04:23

- - -

### [HYDRA-FL: Hybrid Knowledge Distillation for Robust and Accurate Federated Learning](http://arxiv.org/abs/2409.19912)

**HYDRA-FL: ロバストかつ高精度な連合学習のためのハイブリッド知識蒸留**

Momin Ahmad Khan, Yasra Chandio, Fatima Muhammad Anwar

- 連合学習におけるデータの不均一性がグローバルモデルのパフォーマンス低下を招く
- 知識蒸留技術は高い不均一性におけるパフォーマンスを向上させるが、攻撃増幅が問題
- ハイブリッド蒸留技術HYDRA-FLを提案し、浅い層への蒸留損失の一部をオフロードすることで攻撃の影響を軽減
- FedNTDとMOONの2つのアルゴリズムに適用し、攻撃シナリオでベースラインを上回る性能を確認

連合学習の課題を解決しつつ、攻撃耐性も向上させるなんてすごいね！現実のデータに対する応用が楽しみだな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-09-30 03:29

- - -

### [Textual Training for the Hassle-Free Removal of Unwanted Visual Data](http://arxiv.org/abs/2409.19840)

**望まない視覚データの手間なく除去のためのテキストトレーニング**

Saehyung Lee, Jisoo Mok, Sangha Park, Yongho Shin, Dahuin Jung, Sungroh Yoon

- 視覚データセット内の不要なコンテンツを検出する方法を探究
- テキストデータのみで視覚データを適切に分割するモデルの理論分析を示す
- HFTTを提案し、合成テキストデータと事前訓練された視覚言語モデルを使用
- HFTTの新しい目的関数によりデータ注釈の必要性を大幅に削減

実験結果もふまえて、HFTTの実用性を実証しているんだね。視覚データの世界でテキストだけでここまでできるのってびっくり！やってみる価値ありそう♡

**Comment:** NeurIPS 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-30 00:46

- - -

### [Automatic debiasing of neural networks via moment-constrained learning](http://arxiv.org/abs/2409.19777)

**瞬間制約学習によるニューラルネットワークの自動デバイアス化**

Christian L. Hines, Oliver J. Hines

- 因果推論や非パラメトリック推定量の平均がバイアス推定となる問題
- 自動デバイアス化はリース表現子（RR）を直接学習して解決を試みる
- 瞬間制約学習を新たなRR学習アプローチとして提案
- ニューラルネットワークを用いた評価で、従来手法より性能向上を確認

瞬間制約学習って画期的！これでバイアス問題がもっと解決しやすくなるかもね。ニューラルネットワークと組み合わせると、さらに効果が期待できそうでワクワクする！

**Comment:** Code repository and license available at   https://github.com/crimbs/madnet

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, stat.ME, **投稿日時:** 2024-09-29 20:56

- - -

### [Balancing Cost and Effectiveness of Synthetic Data Generation Strategies for LLMs](http://arxiv.org/abs/2409.19759)

**LLM向け合成データ生成戦略のコストと効果のバランス**

Yung-Chieh Chan, George Pu, Apaar Shanker, Parth Suresh, Penn Jenks, John Heyer, Sam Denton

- 大規模言語モデル（LLM）のタスク固有データセット作成は重要だが高コスト
- 合成データやハイブリッドデータ生成方法の有効性は不明
- 質問再フレーズ、新質問など戦略によって効果が異なる
- データ量と予算に応じた最適戦略をフレームワークとして提供

LLMの合成データ生成、大変そうだけど結構おもしろそう！特に、新しい質問を作るタイミングとか気になる～！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-09-29 20:14

- - -

### [Advances in Privacy Preserving Federated Learning to Realize a Truly Learning Healthcare System](http://arxiv.org/abs/2409.19756)

**プライバシー保護型連合学習の進展により実現する真の学習型医療システム**

Ravi Madduri, Zilinghan Li, Tarak Nandi, Kibaek Kim, Minseok Ryu, Alex Rodriguez

- 学習型医療システム（LHS）は、患者ケアのデータを分析して将来の医療成果を向上させる
- データ共有とプライバシー保護の大きな課題がLHS実現の妨げとなっている
- プライバシー保護型連合学習（PPFL）は、分散データの共同学習で患者プライバシーを守る
- PPFLを医療エコシステムに統合し、IOMラウンドテーブルが定義する真のLHSを目指す

医療データの共有が進むと、より良い治療が受けられるようになりそう！患者さんのプライバシーも守られるなら安心だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-09-29 20:02

- - -

### [Tailored Federated Learning: Leveraging Direction Regulation & Knowledge Distillation](http://arxiv.org/abs/2409.19741)

**特徴的な連合学習：方向規制と知識蒸留の活用**

Huidong Tang, Chen Li, Huachong Yu, Sayaka Kamei, Yasuhiko Morimoto

- 連合学習は医療などプライバシーが重要な分野で有用だが、データや計算能力の異質性が課題
- モデルデルタ正則化、パーソナライズドモデル、連合知識蒸留、ミックスプーリングを統合したFL最適化アルゴリズムを提案
- モデルデルタ正則化は通信コストを最小限に抑えつつ、中央サーバでの効率的な更新を実現
- 実験結果では、モデルの高精度と迅速な収束を示し、多様なデータでも優れた性能を発揮

この研究めっちゃ面白そう！特に色々なデータでもうまくいくっていうのが興味深いよね。連合知識蒸留とか、次世代のプライバシー技術に期待大だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-29 15:39

- - -

### [A Systematic Review of NLP for Dementia- Tasks, Datasets and Opportunities](http://arxiv.org/abs/2409.19737)

**認知症のためのNLPの体系的レビュー - タスク、データセット、機会**

Lotem Peled-Cohen, Roi Reichart

- 認知症研究でNLPと医療の協力が進行中
- 200本以上の論文検討、主な研究領域は認知症検出や言語バイオマーカー抽出など
- 臨床データを用いた認知症検出が多く、新たな方向として合成データやデジタルツインが未踏
- 信頼性、科学的厳密性、適用可能性、クロスコミュニティ協力のギャップと機会を強調

認知症にNLPが使えるなんてすごいね！これからもっとクリエイティブなアプローチが出てくるといいなと思う。学際的なコラボも垣間見れて、ワクワクする内容だよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-09-29 15:30

- - -

### [Scrambled text: training Language Models to correct OCR errors using synthetic data](http://arxiv.org/abs/2409.19735)

**スクランブルドテキスト：合成データを使用してOCRエラーを修正するための言語モデルの訓練**

Jonathan Bourne

- OCRエラーはデジタル化された歴史的アーカイブに多く、使用性と価値に影響する
- 合成データとキャラクターレベルのマルコフ腐敗プロセスを利用し、OCRエラーを55%削減
- 少数の高品質データよりも多数の低品質データの方が訓練効果が高い
- 19世紀の新聞記事11,000件の合成データセットとpythonライブラリを提供

合成データを使って、エラーが大幅に減るなんて面白そう！Pythonライブラリもあるから試してみたいな。

**Comment:** 21 pages, 6300 words, 6 Figures, 5 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-09-29 15:20

- - -

### [Multimodal Misinformation Detection by Learning from Synthetic Data with Multimodal LLMs](http://arxiv.org/abs/2409.19656)

**合成データを用いたマルチモーダルLLMによるマルチモーダル誤情報検出**

Fengzhu Zeng, Wenqian Li, Wei Gao, Yan Pang

- マルチモーダル誤情報の検出は重要であるが、特に画像とテキストのペアが問題となる
- 高品質の実世界データセットの作成は高コストで、AI技術を用いた合成データセットが利用される
- 合成データで訓練された検出器の実世界シナリオでの一般化能力には不明点が残る
- 提案する手法は、合成データと実世界データの分布を一致させるモデル非依存のデータ選択方法により、検出性能を向上させる

これ、AIちゃんならではの工夫がいっぱいだね！実際のデータじゃなくて合成データでもこんなに成果が出るなんてビックリ！

**Comment:** EMNLP 2024 Findings

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-09-29 11:01

- - -

### [Federated Learning from Vision-Language Foundation Models: Theoretical Analysis and Method](http://arxiv.org/abs/2409.19610)

**視覚と言語の基盤モデルを用いた連合学習：理論的分析と手法**

Bikang Pan, Wei Huang, Ye Shi

- 事前訓練済みの視覚と言語基盤モデル（CLIPなど）を連合学習に統合することで多様なタスクの一般化を強化
- プロンプト学習を用いて通信および計算コストを削減するプロンプトベースの連合学習法の理論的分析が限られている
- プロンプトベースの連合学習の信号学習とノイズ記憶の進化をモニタリングし、タスク関連とタスク非関連の係数比で性能を評価
- グローバルおよびローカルのプロンプトを用いたプロンプトポートフォリオにより一般化と個別化のバランスを取り、最適な混合係数を導出

連合学習とポートフォリオ最適化のアナロジーが面白そう！信号学習とノイズ記憶の進化をどう捉えたのかも気になるな～



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CL, cs.CV, **投稿日時:** 2024-09-29 08:31

- - -

### [Infighting in the Dark: Multi-Labels Backdoor Attack in Federated Learning](http://arxiv.org/abs/2409.19601)

**暗闇で内部争い：連合学習におけるマルチラベルバックドア攻撃**

Ye Li, Yanchao Zhao, Chengcheng Zhu, Jiale Zhang

- 連合学習はバックドア攻撃に脆弱であると示されている
- ほとんどの研究が単一ラベルバックドア攻撃（SBA）に焦点を当てている
- 本研究は、既存の手法がマルチラベルバックドア攻撃（MBA）には効果がないことを示す
- 新手法M2Mは異なるトリガーパターンを適応させ、目標クラスの分布に基づいてバックドアを起動

攻撃手法がどんどん野心的になっていてびっくり。研究が進めば、連合学習の安全性がどう改善されるか楽しみだね。

**Comment:** 10 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-29 07:37

- - -

### [Fast-Convergent and Communication-Alleviated Heterogeneous Hierarchical Federated Learning in Autonomous Driving](http://arxiv.org/abs/2409.19560)

**自律走行における高速収束および通信負荷軽減の異種階層型連合学習**

Wei-Bin Kou, Qingfeng Lin, Ming Tang, Rongguang Ye, Shuai Wang, Guangxu Zhu, Yik-Chung Wu

- 自律走行のためのストリートシーンセマンティック理解は、地域ごとのデータの偏りで一般化が困難
- 提案されたFedGauアルゴリズムにより、異なる統計特性を持つ都市データの収束速度が35.5%-40.6%向上
- FedGauがRGB画像とデータセットをガウス分布としてモデル化し、統計特性に基づく集約を行う
- AdapRSポリシーが通信リソースを29.65%節約し、パフォーマンスをほぼ維持

全然新しい手法で連合学習の課題を解決するんだね！収束速度も改善するし、通信量も減らせるって、めっちゃ未来型！

**Comment:** 16 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.RO, **投稿日時:** 2024-09-29 05:27

- - -

### [Convergence-aware Clustered Federated Graph Learning Framework for Collaborative Inter-company Labor Market Forecasting](http://arxiv.org/abs/2409.19545)

**収束意識を持つクラスタ化連合グラフ学習フレームワークによる企業間協働の労働市場予測**

Zhuoning Guo, Hao Liu, Le Zhang, Qi Zhang, Hengshu Zhu, Hui Xiong

- 人材需要と供給の変動を予測するために、企業間の需要供給シーケンスの相互連結性が重要
- 企業は競争優位性やセキュリティの懸念からプライベートな人事データを積極的に共有したがらない
- Meta-personalized Convergence-aware Clustered Federated Learning（MPCAC-FL）によりプライバシー保護をしながら精度を高める手法を提案
- 実験でMPCAC-FLは既存の最新モデルを上回り、97%以上の精度を達成しつつ、データのプライバシーも確保

これはすっごく面白そう！企業間でも協力できるなんて、これからの働き方が大きく変わりそうだね。プライバシーも守られてるのが安心できる！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-09-29 04:11

- - -

### [One Node Per User: Node-Level Federated Learning for Graph Neural Networks](http://arxiv.org/abs/2409.19513)

**ユーザーごとに1ノード: グラフニューラルネットワークのためのノードレベルの連合学習**

Zhidong Gao, Yuanxiong Guo, Yanmin Gong

- グラフニューラルネットワークの訓練には生データ収集が必要で、プライバシーの懸念がある
- 連合学習により、生データ共有せずに協調的なモデル訓練が可能
- 提案手法は、メッセージパッシングと特徴ベクトル変換をユーザデバイスとクラウドサーバで分離して実行する
- 特徴ベクトルの潜在表現に基づくグラフラプラシアン項を導入し、ユーザ側モデル更新の調整を行う

ユーザーのデータを守りながら精度も上がるならめっちゃ便利そう！どんな分野で使われるのか気になるよね。

**Comment:** 16 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-09-29 02:16

- - -

### [Heterogeneity-Aware Resource Allocation and Topology Design for Hierarchical Federated Edge Learning](http://arxiv.org/abs/2409.19509)

**異質性を考慮した階層型連合エッジ学習のためのリソース配分およびトポロジー設計**

Zhidong Gao, Yu Zhang, Yanmin Gong, Yuanxiong Guo

- 連合学習はモバイルエッジデバイス上でプライバシーを保護して機械学習モデルを訓練する手法である
- 階層型連合エッジ学習（HFEL）はエッジサーバーを中継してモデル集約を行い、通信負荷を軽減する
- HFELは効率的だが、システムとデータの異質性で収束率が低く、リソース消費が高いという課題がある
- 提案手法はリソース配分とピアツーピア接続調整でトレーニング遅延を最小化し、効率的な大規模FLを実現

異質性に対応したルート設計とか、まるで迷路をナビゲートするみたいで面白そう！しかも、従来の方法より効率が良くなるってところがワクワクするね。

**Comment:** 12 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-09-29 01:48

- - -

### [Subject Data Auditing via Source Inference Attack in Cross-Silo Federated Learning](http://arxiv.org/abs/2409.19417)

**クロスサイロ連合学習におけるソース推論攻撃を用いた主体データ監査**

Jiaxin Li, Marco Arazzi, Antonino Nocera, Mauro Conti

- 連合学習のソース推論攻撃（SIA）は、特定のデータポイントを使用したクライアントを特定
- クロスサイロ連合学習では複数の主体からデータ収集し、情報漏えいのリスクが高まる
- 提案するSLSIAは、既存の制約を取り除き、対象データ使用のクライアントを正確に検出
- 差分プライバシー機構を用いて、SLSIAに対する防御策を提案

クライアントのデータ使用をチェックする攻撃で、連合学習の新しい視点が広がるのめっちゃ面白そう。確かに情報漏えいは怖いから、防御策とセットで考えるのが重要だね！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-09-28 17:27

- - -

### [Efficient Federated Intrusion Detection in 5G ecosystem using optimized BERT-based model](http://arxiv.org/abs/2409.19390)

**最適化されたBERTベースモデルを用いた5Gエコシステムにおける効率的な連合侵入検知**

Frederic Adjewa, Moez Esseghir, Leila Merghem-Boulahia

- 5Gの進化に伴い、IoTを通じたアプリケーションが進化し、セキュリティ上の課題が増加
- 提案された侵入検知システムは、連合学習とBERTを組み合わせて悪意あるネットワークフローを検出
- BERTの性能をエッジデバイスでも最適化し、中央集権的・連邦学習の文脈で実験
- 線形量子化を活用してモデル圧縮を行い、0.02%の精度減少で28.74%のサイズ削減を実現

BERTをエッジデバイスでも使えるように最適化したなんてすごく面白そう！これでIoT環境でも効率的に動作するから、セキュリティレベルがもう一段上がりそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-09-28 15:56

- - -

### [Quantum delegated and federated learning via quantum homomorphic encryption](http://arxiv.org/abs/2409.19359)

**量子準同型暗号を用いた量子委任学習と連合学習**

Weikang Li, Dong-Ling Deng

- 量子学習モデルは古典的な領域よりも計算上の利点を持つ可能性がある
- 量子準同型暗号を用いた一般的なフレームワークを提案し、データのプライバシーを保証
- 提案されたフレームワークでは、通信の複雑さが従来の方法よりも大幅に低減
- サーバーが暗号化された量子データを操作するため、クライアント側の計算負担が軽減

量子技術でのプライバシー保護がすっごく進んでる！これからのクラウドサービスにも大きな影響がありそうね。未来の安全な学習モデルってどんな感じになるんだろう？ワクワクしちゃう！

**Comment:** 5 pages, 1 figure, 1 table

**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** quant-ph, cs.CR, cs.LG, **投稿日時:** 2024-09-28 14:13

- - -

### [Leveraging MTD to Mitigate Poisoning Attacks in Decentralized FL with Non-IID Data](http://arxiv.org/abs/2409.19302)

**非IIDデータを持つ分散型FLにおけるポイズニング攻撃を緩和するためのMTDの活用**

Chao Feng, Alberto Huertas Celdrán, Zien Zeng, Zi Ye, Jan von der Assen, Gerome Bovet, Burkhard Stiller

- 分散型連合学習（DFL）はプライバシーを保護しながら大規模データを管理できるが、ポイズニング攻撃に脆弱である
- 現行の防御方法はIIDデータを前提としており、現実での適用が難しい
- 本論文は、MTD（Moving Target Defense）を活用してDFLモデルの堅牢性を強化するフレームワークを提案
- 実験評価により、このMTDベースのメカニズムが様々なポイズニング攻撃を効果的に緩和することを示した

マジで面白そうな研究！実際のデータでの応用が、もっと安心できる連合学習の未来に繋がりそう。チェックしなきゃね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-09-28 10:09

- - -

### [Privacy Attack in Federated Learning is Not Easy: An Experimental Study](http://arxiv.org/abs/2409.19301)

**連合学習におけるプライバシー攻撃は簡単ではない: 実験的研究**

Hangyu Zhu, Liyuan Huang, Zhenping Xie

- 連合学習はデータを公開せずにモデルを共同でトレーニングし、プライバシーリスクを削減
- しかし、モデル勾配を介してプライベートデータを抽出する攻撃の可能性が示唆されている
- 既存の攻撃アルゴリズムは単一ステップの勾配からデータ再構築を試みているが、実用環境での有効性は不明
- 実験結果は、最新の攻撃アルゴリズムが現実の連合学習環境でプライバシーを効果的に侵害できないことを示唆

連合学習ってプライバシー守れると思ってたけど、やっぱり難しいんだね。でも現実の環境ではまだ安全みたいで安心！これからの研究がどう進化するか楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-09-28 10:06

- - -

### [Confidential Prompting: Protecting User Prompts from Cloud LLM Providers](http://arxiv.org/abs/2409.19134)

**機密プロンプティング: クラウドLLMプロバイダからユーザープロンプトを保護する**

In Gim, Caihua Li, Lin Zhong

- ユーザー入力を保護しつつ、出力の一貫性やモデルの機密性、計算効率を確保
- 機密コンピューティングを活用し、ユーザープロンプトを信頼できる実行環境（CVM）に限定するSMDを導入
- SMDに対する再構築攻撃に対抗するために、プロンプト難読化（PO）という新しい暗号化方式を提案
- 提案手法は、機密情報を取り扱うクラウドLLMサービスにおいてプライバシー保持と効率性を両立

これ、めっちゃ興味深い！クラウドのLLMサービスがもっと安全になる未来、どんな感じか楽しみ♡



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.CL, **投稿日時:** 2024-09-27 20:32

- - -

### [TRACES: TEE-based Runtime Auditing for Commodity Embedded Systems](http://arxiv.org/abs/2409.19125)

**TRACES: コモディティ組み込みシステム向けのTEEベースのランタイム監査**

Adam Caulfield, Antonio Joia Neto, Norrathep Rattanavipanon, Ivan De Oliveira Nunes

- CFAは、リモートデバイスの制御フローのハイジャック攻撃を検出し、実行時の信頼性を確認する技術である
- TRACESは、妥協されたデバイスでも定期的なランタイムレポートの確実な配信を保証する
- ARM TrustZone-M TEEを活用し、カスタムハードウェアの変更なしにこれを実現
- プロトタイプをARM Cortex-M33で実装・評価し、オープンソースとして提供

これは今後のIoTセキュリティにめっちゃ貢献しそう！普通のハードウェアで動くのもポイント高いよね。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-27 20:10

- - -

### [Secure Multiparty Generative AI](http://arxiv.org/abs/2409.19120)

**安全なマルチパーティ生成AI**

Manil Shrestha, Yashodha Ravichandran, Edward Kim

- 生成AIツールの普及により、センシティブな情報がモデルや提供者に露出するリスクがある
- 本研究は、第三者のAI提供者にセンシティブなデータを公開せずに生成AIを使用する方法を提案
- トランスフォーマーのような生成AIアルゴリズムを修正し、機密性と検証可能なマルチパーティ計算を導入
- シャーディングプロセスで計算負荷を分散し、分散ネットワークでセキュアかつ検証可能な計算を実現

分散ネットワークで計算のセキュリティが保たれるなんてすごすぎる！実際にどうやってシャーディングを効率よく行うのか、もっと知りたいな。



**トピック:** [秘密計算](mpc), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-09-27 19:55

- - -

### [Federated Online Prediction from Experts with Differential Privacy: Separations and Regret Speed-ups](http://arxiv.org/abs/2409.19092)

**差分プライバシーによる連合型専門家のオンライン予測：分離と後悔のスピードアップ**

Fengyu Gao, Ruiquan Huang, Jing Yang

- 確率的な敵に対してFed-DP-OPE-Stochアルゴリズムを提案。クライアントごとの後悔が$\sqrt{m}$倍速で改善される。
- 通信コストは対数的に抑えつつ、純粋DPと近似DPの制約下で有効に機能。
- 一般的な無視する敵に対するクライアントの協力は後悔のスピードアップに寄与しないことを示す下限を確立。
- 低損失専門家の特殊ケースでは、Fed-SVTアルゴリズムが$m$倍の後悔スピードアップを達成し、実験による有効性も確認。

すごーく面白そう！特に、クライアント協力の限界や特殊ケースで劇的に改善できるところが斬新。発展的な研究が期待されるね。

**Comment:** Accepted to NeurIPS 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-09-27 18:43

- - -

### [Differential privacy for protecting patient data in speech disorder detection using deep learning](http://arxiv.org/abs/2409.19078)

**深層学習を用いた発話障害検出における患者データ保護のための差分プライバシー**

Soroosh Tayebi Arasteh, Mahshad Lotfinia, Paula Andrea Perez-Toro, Tomas Arias-Vergara, Juan Rafael Orozco-Arroyave, Maria Schuster, Andreas Maier, Seung Hee Yang

- 発話障害の診断にはプライバシーの重要性がある
- 差分プライバシー（DP）の適用で最大3.85%の診断精度低下を観測
- 大規模データでの事前訓練によりDPでも診断精度を維持・向上可能
- 年齢による不公平が残るも、性別に対する重大なバイアスは発生しない

DPが発話障害検出でも効果的なんだね！年齢の不公平さはちょっとだけ問題だけど、この技術って本当に未来の医療を支えそうで楽しみだよね。いますぐクラスで発表したくなる内容じゃない？



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, cs.SD, eess.AS, **投稿日時:** 2024-09-27 18:25

- - -

### [CURATE: Scaling-up Differentially Private Causal Graph Discovery](http://arxiv.org/abs/2409.19060)

**CURATE：差分プライバシーをスケールアップした因果グラフ発見**

Payel Bhattacharjee, Ravi Tandon

- 因果グラフ発見（CGD）は、データセットの特徴間の結合分布を表す確率グラフモデルを推定するプロセス
- CGDアルゴリズムは2つに分類され、制約ベースアルゴリズムとスコアベースアルゴリズムが存在する
- 差分プライバシー（DP）は観測データのプライバシー保護のために採用されているが、同じ量のノイズを加えると予測性能に影響を与える
- CURATEは、適応的なプライバシー予算配分を行うことで、精度を保ちながらプライバシー漏洩を抑えた新しいDP-CGDフレームワークである

CURATEが実際にどれくらい効果があるのか気になる！これが普及したらもっと安全にデータ解析が進みそうだよね。どんな結果になるのか期待！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.IT, cs.LG, math.IT, stat.ME, **投稿日時:** 2024-09-27 18:00

- - -

### [A Systematisation of Knowledge: Connecting European Digital Identities with Web3](http://arxiv.org/abs/2409.19032)

**知識の体系化: ヨーロッパのデジタルアイデンティティとWeb3の連携**

Ben Biedermann, Matthew Scerri, Victoria Kozlova, Joshua Ellul

- セルフソブリンアイデンティティ (SSI) と分散型アイデンティティの違いを明確化
- eIDAS 2.0の実装へ至る技術的発展の体系化を目指す
- OIDCパラダイムとブロックチェーンによる分散型アイデンティティの台頭を検証
- 公共許可なし台帳とeIDAS 2.0起源データのデジタルアイデンティティ橋の必要性を提案

これってすごく興味深いテーマだね！特にeIDAS 2.0とWeb3の接続部分がもっと探求されて、将来どんな風に変わっていくか楽しみ！

**Comment:** Conference paper

**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-09-26 22:35

- - -

### [DiaSynth -- Synthetic Dialogue Generation Framework](http://arxiv.org/abs/2409.19020)

**DiaSynth -- 合成対話生成フレームワーク**

Sathya Krishnan Suresh, Wu Mengjun, Tushar Pranav, Eng Siong Chng

- 専門分野ごとの対話データセットの欠如が対話システム開発の障壁
- DiaSynthは多様な分野の高品質で文脈豊かな対話を生成
- 大規模言語モデルと連鎖思考推論を用いてリアルな対話をエミュレート
- 合成データで微調整したモデルはベースモデルを16.47%上回る性能

対話データセットが乏しい状況を解決するための新しいアプローチだね。DiaSynthがどれだけリアルな会話を生成できるのか、試してみたいな！

**Comment:** 13 pages, 1 figure

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-09-25 07:03
