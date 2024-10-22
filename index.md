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

更新: 2024-10-22T04:25:13.732374

- - -

### [A Framework for Evaluating Predictive Models Using Synthetic Image Covariates and Longitudinal Data](http://arxiv.org/abs/2410.16177)

**合成画像共変量と縦断データを用いた予測モデル評価フレームワーク**

Simon Deltadahl, Andreu Vall, Vijay Ivaturi, Niklas Korsbo

- 患者データを合成しつつ複雑な共変量と縦断的観察を組み合わせてプライバシー問題に対処
- 潜在空間での制御された関連付けにより、共変量と縦断的観察のペアを生成可能に
- 109,309のOCTスキャンを使用し、変分オートエンコーダと拡散モデルを組み合わせて画像生成モデルを訓練
- 合成データでの弱い信号の検出が可能で、ヘルスケア研究のための有用なツールを提供

複雑な患者データを守りつつ解析できるなんてすごいね！いかにして関連付けをコントロールするかがポイントで、様々な業界への応用もワクワクするよね。未来の研究にもつながりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-21 16:43

- - -

### [Sparkle: Mastering Basic Spatial Capabilities in Vision Language Models Elicits Generalization to Composite Spatial Reasoning](http://arxiv.org/abs/2410.16162)

**Sparkle: ビジョンランゲージモデルで基本的な空間能力を習得し、複合的な空間推論への一般化を実現**

Yihong Tang, Ao Qu, Zhaokai Wang, Dingyi Zhuang, Zhaofeng Wu, Wei Ma, Shenhao Wang, Yunhan Zheng, Zhan Zhao, Jinhua Zhao

- 現在のビジョンランゲージモデルは、2D環境での空間推論が苦手である
- 基本的な空間能力をマスターすることで、複雑な空間推論が向上するという仮説を立てる
- Sparkleというフレームワークを導入し、合成データ生成と目標指導によりモデルを強化
- Sparkleにより短径問題の正解率が13.5%から40.0%に向上し、複合的な課題にも一般化

空間認識って案外難しいんだね！SparkleでVLMsが進化する姿がワクワクするよね。これからもっと多様な環境でAIが役に立ちそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, **投稿日時:** 2024-10-21 16:26

- - -

### [DMM: Distributed Matrix Mechanism for Differentially-Private Federated Learning using Packed Secret Sharing](http://arxiv.org/abs/2410.16161)

**差分プライベート連合学習のための分散行列機構：パック秘密共有を用いて**

Alexander Bienstock, Ujjwal Kumar, Antigoni Polychroniadou

- 連合学習では、異なるユーザーのデータを用いてプライバシーを守ることが課題
- 中央DPとローカルDPの違いは、データのノイズ処理のタイミングと場所にある
- 分散行列機構を提案し、ローカルDPにおいてもプライバシーとユーティリティのバランスを改善
- 提案手法により、ユーザーの動的な参加に対応しつつプライバシーを向上

新しい仕組みで課題を解決できるのってすごいね！プライバシーを守りつつパフォーマンスを高めるって、これからもっといろんな分野に広がりそう！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-10-21 16:25

- - -

### [Extracting Spatiotemporal Data from Gradients with Large Language Models](http://arxiv.org/abs/2410.16121)

**大規模言語モデルを用いた勾配からの時空間データ抽出**

Lele Zheng, Yang Cao, Renhe Jiang, Kenjiro Taura, Yulong Shen, Sheng Li, Masatoshi Yoshikawa

- 連合学習では勾配更新からユーザーデータが再構築され、プライバシーが脅かされている
- 画像データでの成功事例はあるが、時空間データには直接適用できない
- ST-GIAとST-GIA+を提案、勾配からの位置再構築を成功させる
- 動的に摂動を調整した防御戦略により、プライバシーと有用性のトレードオフを改善

連合学習ってデータのプライバシーを守る技術なのに、逆に情報が漏れちゃうなんてびっくり！やっぱり、防御もちょっとした工夫でプライバシーも守りつつ学習もできるようになるんだね。そんな技術の進歩のスピード感にワクワクしちゃう！

**Comment:** arXiv admin note: substantial text overlap with arXiv:2407.08529

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-21 15:48

- - -

### [Distributed Learning for UAV Swarms](http://arxiv.org/abs/2410.15882)

**UAV群のための分散学習**

Chen Hu, Hanchi Ren, Jingjing Deng, Xianghua Xie

- 環境モニタリングや監視にUAV群を活用する場面で、連合学習がプライバシーとセキュリティの課題に対する有望な解決策となる
- UAVが収集するデータは非IIDであるため、FedAvg, FedProx, FedOpt, MOONなどの多様な集約方法を検討
- FedProxは、非IID環境下で最も安定した性能を示し、ローカル更新を正規化する重要性を確認
- ベースラインのMNISTから監視向けのCelebAまで、データセットごとに異なるアルゴリズム性能を比較

UAVが協力して学習する世界なんて、未来を感じちゃうよね。みんなで情報を交換しながら、それぞれのお仕事をきちんとこなしていけるなんてすごいかっこいい！FedProxの安定した性能がどんな風に活かされていくのか、これからが楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, cs.RO, **投稿日時:** 2024-10-21 11:01

- - -

### [LLM4GRN: Discovering Causal Gene Regulatory Networks with LLMs -- Evaluation through Synthetic Data Generation](http://arxiv.org/abs/2410.15828)

**LLM4GRN: LLMを用いた遺伝子調節ネットワークの発見 -- 合成データ生成による評価**

Tejumade Afonja, Ivaxi Sheth, Ruta Binkyte, Waqar Hanif, Thomas Ulas, Matthias Becker, Mario Fritz

- 遺伝子調節ネットワーク（GRNs）は転写因子とターゲット遺伝子間の因果関係を示す
- この研究は、大規模言語モデル（LLMs）が持つ生物学的知識をGRN発見に活用
- LLMsが提案するGRNsをもとに合成データを生成し、元のデータセットと比較評価
- 統計的・生物学的評価でLLMsがデータ合成や統計モデリングを支援できると示唆

遺伝子調節の因果関係を大規模言語モデルで探るなんて面白そう！合成データで評価するアプローチも未来的でワクワクするね。どんな病気の発見に役立つのか気になっちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-10-21 09:46

- - -

### [Digital Product Passport Management with Decentralised Identifiers and Verifiable Credentials](http://arxiv.org/abs/2410.15758)

**分散型識別子と検証可能な資格情報によるデジタル製品パスポート管理**

Ismael Illán García, Francesc D. Muñoz-Escoí, Jordi Arjona Aroca, F. Javier Fernández-Bravo Peñuela

- デジタル製品パスポート（DPP）は製品の再利用、修理、リサイクルを促進する仕組み
- DPPは環境への影響を減少させ、循環型経済を推進する効果を期待されている
- ESPRは製品関連データの収集と管理に特定の要件を設定している
- 分散型識別子と検証可能な資格情報を用いることで制度の拡張性と信頼性を向上

デジタルの世界で環境を守るアイディアだなんて、未来を考えるとワクワクしちゃう！分散型の管理で、情報の信頼性をキープしつつスケーラブルにするって最高じゃない？これからの製品ももっとエコになるかもね。

**Comment:** 22 pages, 8 images

**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.DC, cs.CR, **投稿日時:** 2024-10-21 08:18

- - -

### [Automated Proof Generation for Rust Code via Self-Evolution](http://arxiv.org/abs/2410.15756)

**自己進化によるRustコードの自動証明生成**

Tianyu Chen, Shuai Lu, Shan Lu, Yeyun Gong, Chenyuan Yang, Xuheng Li, Md Rakib Hossain Misu, Hao Yu, Nan Duan, Peng Cheng, Fan Yang, Shuvendu K Lahiri, Tao Xie, Lidong Zhou

- Rustコードの自動証明生成を可能にする新たなフレームワークSAFEを提案。
- SAFEはデータ合成と微調整を通じてモデル能力を向上させる自己進化サイクルを確立。
- 多数の合成された誤った証明を活用し、自己デバッグ能力をトレーニング。
- GPT-4oと比べ、効率と精度が向上し、正確性が70.50%の人間エキスパート作成ベンチマークを達成。

Rustコードの証明生成が自動化されるってすごく面白そう！自己進化が鍵になってて、今後いろんなコードでこの技術が応用されるかもね。🤔✨



**トピック:** [合成データ](sd), **カテゴリ:** cs.SE, cs.AI, **投稿日時:** 2024-10-21 08:15

- - -

### [Alchemy: Amplifying Theorem-Proving Capability through Symbolic Mutation](http://arxiv.org/abs/2410.15748)

**錬金術: 象徴的な変異による定理証明能力の増幅**

Shaonan Wu, Shuai Lu, Yeyun Gong, Nan Duan, Ping Wei

- 形式的な定理証明はデータ不足の問題があったが、Alchemyは象徴的な変異を用いて合成データを生成
- Mathlibの定理を候補として、同等の表現に置換することで定理数を11万から600万に増加
- 増強されたコーパスで大規模言語モデルを継続的に事前学習・微調整し、Leandojoベンチマークで5%の性能向上を達成
- 合成データがminiF2Fベンチマークでも2.5%の性能向上を実現し、データ構成とトレーニング法の分析も行う

この論文、すごく面白そう！特に、少ないデータからそんなに多くの定理を生成できるAlchemyの仕組みが気になるよね。未来の定理証明が一気に簡単になっちゃうかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-10-21 08:04

- - -

### [Geographical Node Clustering and Grouping to Guarantee Data IIDness in Federated Learning](http://arxiv.org/abs/2410.15693)

**連合学習におけるデータIID性を保証する地理的ノードクラスタリングとグルーピング**

Minkwon Lee, Hyoil Kim, Changhee Joo

- 連合学習では非IIDデータセット問題が大きな課題で、多くの試みが行われている
- 本論文は、地理的特徴を用いたIoTノードのクラスタリングとグルーピングを提案
- Dynamic ClusteringとPartial-Steady GroupingアルゴリズムでデータセットのIID性を改善
- 提案手法は、離脱デバイス数と各グループの均一性におけるコストを既存手法より110倍以上改善

IoTデバイスの地理情報を使ってデータの特性を改善するアイデアが新しいよね！これでたくさんのデバイスが集まっても効率的に学習できちゃうのがすごいかも。これからもっとスマートに連携していけそうだね。

**Comment:** 10 pages, 7 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, cs.NI, **投稿日時:** 2024-10-21 07:03

- - -

### [Federated Learning with MMD-based Early Stopping for Adaptive GNSS Interference Classification](http://arxiv.org/abs/2410.15681)

**適応的GNSS干渉分類のためのMMDベース早期停止を用いた連合学習**

Nishant S. Gaikwad, Lucas Heublein, Nisha L. Raichur, Tobias Feigl, Christopher Mutschler, Felix Ott

- 連合学習は複数デバイスでグローバルモデルを共同訓練するが、データの偏りが課題
- 提案手法は少数ショット学習とモデル重みのグローバルサーバーでの集約を組み合わせる
- ローカルとグローバルモデル間の特徴埋め込みの最大平均差異を利用し動的早期停止を導入
- 提案手法は最新技術を上回り、新規の干渉クラスやマルチパスシナリオに適応可能と判明

連合学習が新しいデータに対してどう適応するのかを工夫していて面白そう！親しみやすい具体例もあって、実際の応用がイメージできるね。個々のデバイスでの偏りを解決するアイデアが魅力的だと思うなあ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, 62P30, 68T30, 68T05, 68T37, G.3; I.2.4; I.2.6, **投稿日時:** 2024-10-21 06:43

- - -

### [Accounting for Missing Covariates in Heterogeneous Treatment Estimation](http://arxiv.org/abs/2410.15655)

**異なる共変量を持つ個別化治療効果推定のための欠落共変量の考慮**

Khurram Yamin, Vibhhu Sharma, Ed Kennedy, Bryan Wilder

- 元の研究で観察されなかった共変量が新たにターゲット集団で観察された場合について研究
- 新たに観察された共変量で条件付けした異質な治療効果の最狭境界を推定することを目指す
- 既存の共変量に絞った場合も正しく周辺化されるような部分的識別戦略を導入
- バイアス修正推定量の導入により、迅速な収束率と統計的保証を実現

探してたらやっと新しい方法を見つけたって感じだよね！共変量が異なる実験の結果を活かせたら、もっといろんな場面で役立てることができそう♪



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ME, **投稿日時:** 2024-10-21 05:47

- - -

### [ZK-DPPS: A Zero-Knowledge Decentralised Data Sharing and Processing Middleware](http://arxiv.org/abs/2410.15568)

**ZK-DPPS: ゼロ知識の分散型データ共有と処理ミドルウェア**

Amir Jabbari, Gowri Ramachandran, Sidra Malik, Raja Jurdak

- IoT駆動のサプライチェーンは複雑化し、データ共有と処理が重要
- ブロックチェーンは信頼性や透明性を促進するが、データプライバシーに懸念
- ZK-DPPSは通常のゼロ知識証明を使わず、プライバシーを保持する手法を提案
- 完全準同型暗号と秘密計算で効率よくプライバシーを保つシステムを実現

この研究はめっちゃおもしろそう！ゼロ知識証明の代わりに完全準同型暗号を使って、プライバシーを守りつつデータを安全に処理するなんてちょっと驚きだよね。サプライチェーンの未来が見えてきて、ワクワクしちゃう！



**トピック:** [準同型暗号](he), [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-21 01:23

- - -

### [Generating Tabular Data Using Heterogeneous Sequential Feature Forest Flow Matching](http://arxiv.org/abs/2410.15516)

**異種連続特徴森林フロー・マッチングによる表形式データ生成**

Ange-Clément Akazan, Alexia Jolicoeur-Martineau, Ioannis Mitliagkas

- プライバシーと規制の制約があり、現実のデータセットに依存しないデータ生成が必要
- 既存のFF法はパフォーマンスが良いが、カテゴリ変数の扱いやODEの初期条件に敏感
- 新たなHS3F法は、連続データ生成とマルチノミアルサンプリングにより生成速度を向上
- 25のデータセットでHS3Fの方が高品質で多様なデータを生成し、FFより21-27倍速く生成

データ生成がめちゃ速くなったってすごいよね！プライバシーを守りつつ高品質なデータが作れるなんて未来的でワクワクするよ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-20 21:55

- - -

### [Bayesian data fusion for distributed learning](http://arxiv.org/abs/2410.15473)

**分散学習のためのベイジアンデータ融合**

Peng Wu, Tales Imbiriba, Pau Closas

- 連合学習の課題は、クライアント間のデータ分布の不均等性による非独立かつ非同一分布データの処理
- 知識共有とモデルの個別化が重要で、クライアントを同様のデータ分布でクラスタ化する方法を提案
- 本研究では、クライアントをクラスタに関連付けるベイジアンフレームワークを提案し、実際のアルゴリズムを提供
- 提案フレームワークは一意のクライアント-クラスタ関連付けを不要にし、モデルの性能が向上

この論文、クライアントごとに異なるデータをうまく扱おうとしていて、すごくおもしろそう！クラスターごとにモデルを改善していく方法は、他の分野にも応用できそうだね。未来にわくわくしちゃう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, stat.ML, **投稿日時:** 2024-10-20 19:11

- - -

### [Data Augmentation via Diffusion Model to Enhance AI Fairness](http://arxiv.org/abs/2410.15470)

**拡散モデルによるデータ拡張でAIの公平性を向上させる**

Christina Hastings Blow, Lijun Qian, Camille Gibson, Pamela Obiomon, Xishuang Dong

- AIの公平性はユーザーの利益を反映する結果の透明性を求めている
- 拡散モデルを用いた合成データ生成がデータ不足の解決策として注目
- Tab-DDPMは様々な特徴を持つ表形式データの合成生成に適応可能
- 合成データを用いた実験で二値分類の公平性が向上

拡散モデルで表形式データを生成してAIの公平性を向上させるんだね！実験での効果も確認されているので、もっと研究が進むとAIがもっと公正に進化していきそうでワクワクするね。

**Comment:** arXiv admin note: text overlap with arXiv:2312.12560

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CY, **投稿日時:** 2024-10-20 18:52

- - -

### [Formalization of Differential Privacy in Isabelle/HOL](http://arxiv.org/abs/2410.15386)

**Isabelle/HOLにおける差分プライバシーの形式化**

Tetsuya Sato, Yasuhiko Minamide

- 差分プライバシーは理解しやすいが、データベースにおける適用は複雑
- 小さなプログラム変更が差分プライバシーを破壊することがあるため、形式的検証が重要
- この研究では、Isabelle/HOLライブラリを用いて差分プライバシーを形式化
- 連続確率分布をサポートする差分プライバシーの初の形式化を達成

差分プライバシーの形式化、すごい！これでデータの安全性が保証されるから、新しいアプリ開発もグッと進みそうだよね。やっぱりデータを扱うのって奥が深いなーって、改めて感心しちゃった。

**Comment:** Draft version

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.PL, cs.CR, **投稿日時:** 2024-10-20 13:06

- - -

### [Synthetic Data Generation for Residential Load Patterns via Recurrent GAN and Ensemble Method](http://arxiv.org/abs/2410.15379)

**住居負荷パターンの合成データ生成：再帰的GANとアンサンブル法による手法**

Xinyu Liang, Ziheng Wang, Hao Wang

- 合成データは、真の電力消費パターンを忠実に再現するために重要
- 本研究のERGANは、再帰的GANを用いたアンサンブルを活用
- ERGANは住宅ごとの多様な負荷パターンを捕捉し、データの現実味と多様性を向上
- 解析の結果、既存のベンチマークに対して優れた性能を示すことが確認された

エネルギー業界における合成データ利用の可能性が広がりそうだね。負荷パターンが細かく再現されると、いろんなシミュレーションや計画に役立ちそうでワクワクするな。

**Comment:** 12 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-20 12:33

- - -

### [Hybrid Memory Replay: Blending Real and Distilled Data for Class Incremental Learning](http://arxiv.org/abs/2410.15372)

**ハイブリッドメモリリプレイ: クラス増分学習のための実データと蒸留データの融合**

Jiangtao Kong, Jiacheng Shi, Ashley Gao, Shaohan Hu, Tianyi Zhou, Huajie Shao

- 連続学習では新たなタスクの知識を学習しつつ既存タスクの知識を保持するが、記憶容量に制限がある。
- データ蒸留は情報効率の良い合成データを生成し、バッファのサイズ削減に役立つが、効果が徐々に薄れる。
- 実データと合成データを混ぜたハイブリッドメモリにより、それぞれの弱点を補完し破滅的忘却を軽減する。
- 提案手法は既存のリプレイベースのクラス増分学習モデルに簡単に統合可能で、効果的に性能を向上する。

この研究、会話っぽくて面白いよね！実データと合成データのいいとこ取りで賢く学習するって、なんか新しい発想だよね。限られた容量でもしっかり学習できる未来がワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-20 12:13

- - -

### [Tighter Performance Theory of FedExProx](http://arxiv.org/abs/2410.15368)

**FedExProxの強化パフォーマンス理論**

Wojciech Anyszka, Kaja Gruntkowska, Alexander Tyurin, Peter Richtárik

- FedExProxの理論的保証が従来の勾配降下法と同水準なのが発覚
- 新たな解析で非強凸二次問題に対する収束率を改善
- 計算・通信コストを考慮し、部分参加シナリオでもFedExProxが優位
- 一般関数での適用性を拡大し、従来の強凸解析を超える成果を発揮

FedExProxが最初の評価を覆してかなり役立ちそうな技法に変貌したのが面白い！これを使った連合学習の新たな可能性がどんどん広がりそうでワクワクするね。

**Comment:** 43 pages, 4 figures

**トピック:** [連合学習](fl), **カテゴリ:** math.OC, cs.LG, stat.ML, **投稿日時:** 2024-10-20 11:53

- - -

### [BERTtime Stories: Investigating the Role of Synthetic Story Data in Language pre-training](http://arxiv.org/abs/2410.15365)

**BERTtime物語: 言語事前学習における合成ストーリーデータの役割を調査**

Nikitas Theodoropoulos, Giorgos Filandrianos, Vassilis Lyberatos, Maria Lymperaiou, Giorgos Stamou

- 人間の発達に基づくデータ制約下での効率的な事前学習を目指す
- 合成ストーリーデータTinyStoriesを用いて、ストーリーの補完と言語知識習得を検証
- 合成データは、時折メリットがあるが、全体として言語理解にはマイナスの影響を与えることがわかった
- リソースが限られる中でのストーリーデータの合成に関する初期研究を提供し、データ制約下でのモデリングの強化の可能性を示唆する

TinyStoriesって、小さな話でも立派に言語モデルを育てられるか試してる感じかな？合成データの限界もわかるなんて、面白いね。公開されたモデルを試してみたくなっちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-20 11:47

- - -

### [Amortized Probabilistic Conditioning for Optimization, Simulation and Inference](http://arxiv.org/abs/2410.15320)

**最適化、シミュレーション、推論のためのアモータイズド確率条件付け**

Paul E. Chang, Nasrulloh Loka, Daolang Huang, Ulpu Remes, Samuel Kaski, Luigi Acerbi

- 既存のモデルでは実行時に確率的な潜在情報を柔軟に操作できない
- 新しいメタラーニングモデルとしてACEを導入、潜在変数を明示的に表現
- ACEは観測データと解釈可能な潜在変数での条件付けを可能にする
- 画像補完やベイズ最適化、シミュレーションベース推論で性能を発揮

ACEってすごく便利そう！潜在情報を活用することで、もっとリアルな予測ができそう。画像の補完や分類にも役立つのがすごく魅力的だね。

**Comment:** 33 pages, 21 figures

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-10-20 07:22

- - -

### [BRIEF: Bridging Retrieval and Inference for Multi-hop Reasoning via Compression](http://arxiv.org/abs/2410.15277)

**圧縮を通じた多段推論のための検索と推論の架け橋**

Yuankai Li, Jia-Chen Gu, Di Wu, Kai-Wei Chang, Nanyun Peng

- 大規模言語モデルの検索補完により推論を加速し、長文理解の劣化を軽減
- BRIEFは圧縮されたテキスト要約を用いて多段推論を統合し、効率を向上
- 合成データを活用し、独自の圧縮モデルで優れた要約生成を実現
- HotpotQAで高性能を示し、既存手法を越えた高いQA精度を達成

BRIEFのって、多段推論を扱うっておもしろいな！効率良く賢く答えを出すって、まるでハイスペックな知的アシスタントになれる感じじゃない？今後のプライバシー技術にどう役立てるか考えるとワクワクする！

**Comment:** Project page: https://jasonforjoy.github.io/BRIEF/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-20 04:24

- - -

### [Physically Guided Deep Unsupervised Inversion for 1D Magnetotelluric Models](http://arxiv.org/abs/2410.15274)

**物理に基づく1Dマグネトテルリックモデルの深層教師なし逆変換**

Paul Goyes-Peñafiel, Umair bin Waheed, Henry Arguello

- 地下の抵抗分布を把握するために、マグネトテルリック逆変換が必要
- 従来の方法は多くのパラメータ調整が必要で、時間がかかる
- 新しい方法では物理に基づく教師なし深層学習を用いる
- 提案手法は最新技術よりも精度の高い抵抗モデルを示す

物理に基づいた教師なしのアプローチって新しいね！これで地下の資源探しももっと効率的になるかも！？今後のエネルギー探査の可能性が広がりそうでワクワクする！

**Comment:** 5 pages, 6 figures, github repository, submitted to IEEE-GRSL

**トピック:** [合成データ](sd), **カテゴリ:** physics.geo-ph, cs.LG, physics.app-ph, **投稿日時:** 2024-10-20 04:17

- - -

### [Fastrack: Fast IO for Secure ML using GPU TEEs](http://arxiv.org/abs/2410.15240)

**Fastrack: GPU TEEを用いたセキュアな機械学習のための高速IO**

Yongqin Wang, Rachit Rajat, Jonghyun Lee, Tingting Tang, Murali Annavaram

- クラウド上でのMLにはデータの安全性が重要であり、GPUベースの信頼実行環境（TEE）が高性能で安全なソリューションとなる。
- しかし、CPUからGPUへの通信オーバーヘッドが大きく、TEEシステムではパフォーマンスが遅延し、非TEEシステムに比べコストが12.69から33.53倍増加する。
- Nvidia H100 TEEプロトコルの課題として再暗号化、並列認証の制限、不要な処理の直列化が挙げられる。
- 提案するFastrackは、直接通信、認証の並列化、PCI-e転送との同時復号化によってランタイムを最大84.6%短縮する。

この論文、めっちゃ興味深い！GPUでの高速セキュリティ強化とか、未来のテクノロジーの可能性を感じるね。これが普及したら、みんなが安心してクラウド上で機械学習できそうなのが楽しみ！



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.AR, **投稿日時:** 2024-10-20 01:00

- - -

### [Bias Amplification: Language Models as Increasingly Biased Media](http://arxiv.org/abs/2410.15234)

**偏見増幅: メディアとしての言語モデルの偏向拡大**

Ze Wang, Zekun Wu, Jeremy Zhang, Navya Jain, Xin Guan, Adriano Koshiyama

- 大規模言語モデルが社会に広がる中、モデルの訓練データが合成的であるため、偏見増幅が問題に
- 偏見増幅を理論的に定義し、モデル崩壊と独立して起こる現象であることを示すフレームワークを提案
- GPT-2を用いた実験で、開放型政治的偏向における偏見増幅の実例を提示し、反復的な微調整で偏向が増大
- 偏見増幅を緩和する戦略として、保存と蓄積が効果的であることを示し、異なるニューロンの作用であることを実証

偏見がどんどん増えちゃうって怖いね。でも、この研究でどうやって緩和するかがわかるのは嬉しい！未来のAIがもっと公正であるために大事な一歩かもね！

**Comment:** Submitted to ARR Roling Review October

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-10-19 22:53

- - -

### [On the Diversity of Synthetic Data and its Impact on Training Large Language Models](http://arxiv.org/abs/2410.15226)

**合成データの多様性と大型言語モデルの学習への影響について**

Hao Chen, Abdul Waheed, Xiang Li, Yidong Wang, Jindong Wang, Bhiksha Raj, Marah I. Abdin

- 大型言語モデル（LLM）は多様で高品質な事前学習データが必要であり、合成データがデータ不足解決策として浮上
- 合成データの多様性を測定する新たな指標「LLMクラスターエージェント」を導入し、LLMの性能への影響を探る
- 合成データ多様性のスコアは事前学習と教師あり微調整の性能に正の相関があると実験で示される
- 合成データの事前学習における多様性は、小規模モデルでも教師あり微調整への影響がより大きいことが判明

合成データがLLMにどう役立つかの研究だなんて面白そう！データ生成プロセスがもっと効率的になる方法が見えてくるといいよね。合成データが秘める可能性にワクワクしちゃうなー。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-19 22:14

- - -

### [DataSeal: Ensuring the Verifiability of Private Computation on Encrypted Data](http://arxiv.org/abs/2410.15215)

**DataSeal: 暗号化データ上の秘密計算の検証可能性の保証**

Muhammad Husni Santriaji, Jiaqi Xue, Qian Lou, Yan Solihin

- FHEはデータを復号せずに計算できる技術で、医療や金融での利用が期待されている
- FHEを用いたクラウド計算において計算の完全性や正確性への懸念が存在する
- DataSealはABFT技法をFHEに組み合わせ、高効率かつ検証可能性を実現
- 問題サイズが大きくなるほどDataSealのオーバーヘッドはほぼ無視できるレベルまで減少する

データが暗号化されたまま計算できるってすごいよね！DataSealの技術で安全性も確保しつつオーバーヘッドも減らせるから、これからプライバシー重視の分野での応用がどんどん広がりそう。

**Comment:** Accepted by IEEE S&P 2025 (Oakland). 17 pages, 7 figures

**トピック:** [準同型暗号](he), [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-19 21:19

- - -

### [DPVS-Shapley:Faster and Universal Contribution Evaluation Component in Federated Learning](http://arxiv.org/abs/2410.15093)

**DPVS-Shapley:連合学習における高速かつ汎用的な貢献評価コンポーネント**

Ketin Yin, Zonghao Guo, ZhengHan Qin

- 連合学習はデータプライバシーとシステムの拡張性を向上させる新しい学習方法。
- 公平な貢献評価は連合学習における参加者の動機づけに不可欠な要素。
- 動的プルーニングにより評価プロセスを高速化し、精度を損なわない解法を提案。
- DPVS-Shapleyは難易度の高い例を識別できる参加者により高い貢献スコアを付与可能。

参加者の貢献度に対して公平で早い評価を提供する技術って、すごく大切だよね！DPVS-Shapleyのアプローチが色々な領域で役立ちそうで楽しみ！どんな結果をもたらすか気になるね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, cs.GT, **投稿日時:** 2024-10-19 13:01

- - -

### [Personalized Federated Learning with Adaptive Feature Aggregation and Knowledge Transfer](http://arxiv.org/abs/2410.15073)

**適応的特徴集約と知識伝達による個別化連合学習**

Keting Yin, Jiayi Mao

- 非独立同分布（Non-IID）データでのパーソナライズモデル向けに提案された新手法
- Global modelの知識を活用し、パーソナライゼーションと汎化のバランスを向上
- 三つのデータセットで多数のベンチマークを超える優れた性能を実証
- 適応的特徴集約と知識伝達を駆使し、統計的異質性問題に対処

この研究は、個別対応の機械学習の未来を変える可能性があるね！自分だけのモデルを持つなんて、ちょっと特別な感じで素敵！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-10-19 11:32

- - -

### [Adanonymizer: Interactively Navigating and Balancing the Duality of Privacy and Output Performance in Human-LLM Interaction](http://arxiv.org/abs/2410.15044)

**Adanonymizer: 人間とLLMの対話におけるプライバシーと出力性能の二面性を対話的にナビゲートしバランスを取る**

Shuning Zhang, Xin Yi, Haobin Xing, Lyumanshan Ye, Yongquan Hu, Hewu Li

- LLMは個別の相談においてプライバシーと出力性能のバランスを取るのが難しい
- Adanonymizerは匿名化プラグインであり、ユーザーがプライバシーと性能のトレードオフを操作可能にする
- このプラグインは2Dカラーパレットを用いてプライバシーとユーティリティのバランスを視覚的に調整可能
- 評価結果では、Adanonymizerが他の手法よりも修正時間を短縮し、ユーザーの満足度が高かった

人間とLLMの対話って面白そうだよね！私もプライバシー気にしながら自由に話せるなんて素敵って思う。Adanonymizerが助けてくれるなら、もっと安心してLLMを活用できるかもしれないね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.HC, **投稿日時:** 2024-10-19 09:04

- - -

### [DynaMO: Protecting Mobile DL Models through Coupling Obfuscated DL Operators](http://arxiv.org/abs/2410.15033)

**DynaMO: DLモデルを秘匿化したDLオペレーターの結合によるモバイルDLモデルの保護**

Mingyi Zhou, Xiang Gao, Xiao Chen, Chunyang Chen, John Grundy, Li Li

- モバイルアプリ上のDLモデルは逆コンパイルされやすく、知財や攻撃リスクがある
- 従来のモデル秘匿化方法は完全保護が難しく、動的分析による情報漏えいが懸念
- 演算ツールDLModelExplorerで現行秘匿化戦略の脆弱性を検証し、攻撃効果が高いことを確認
- 提案するDynaMOは準同型暗号に類似し、動的な全体秘匿化戦略であり、モデルの安全性を向上

モバイル上のDLモデル、攻撃されないようにするの大変なんだね！でもDynaMOなら軽い負荷で安全強化ってすごくない？今後早く普及されるといいな！

**Comment:** Published on Proceedings of the 39th IEEE/ACM International   Conference on Automated Software Engineering (ASE'24)

**トピック:** [準同型暗号](he), **カテゴリ:** cs.SE, **投稿日時:** 2024-10-19 08:30

- - -

### [On the Influence of Shape, Texture and Color for Learning Semantic Segmentation](http://arxiv.org/abs/2410.14878)

**形状、テクスチャ、色がセマンティックセグメンテーションの学習に与える影響について**

Annika Mütze, Natalie Grabowsky, Edgar Heinert, Matthias Rottmann, Hanno Gottschalk

- 形状とテクスチャの影響を持つDNN分類モデルが多く研究されてきたが、この論文では新たな視点から問いを立てる
- 形状、テクスチャ、色それぞれがDNNの学習にどの程度寄与するのか、また各要素の組み合わせがどのように影響するのかを分析
- CityscapesやPASCAL Contextデータセットを使用し、単一の要素または要素の組み合わせで再構築したデータセットで学習
- 形状と色の組み合わせがテクスチャを含まない場合に強力な結果を示し、畳み込み型とトランスフォーマー型バックボーンの両方に適用可能

この研究での発見って面白いね！形と色の組み合わせで効果が上がるなんてちょっとびっくり。DNNにおける学習のカギを握る要素がこんなに違うんだね、ますますAIの可能性が広がる予感がする～。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-10-18 21:52

- - -

### [FedSpaLLM: Federated Pruning of Large Language Models](http://arxiv.org/abs/2410.14852)

**FedSpaLLM: 大規模言語モデルの連合プルーニング**

Guangji Bai, Yijiang Li, Zilinghan Li, Liang Zhao, Kibaek Kim

- 大規模言語モデルは高性能だが計算負荷やストレージ需要が課題
- プライバシーに配慮し、FedSpaLLMがモデルをローカルでプルーニング
- 独自の$\ell_0$-ノルム集約関数で重要なモデルパラメータ保持を実現
- レイヤーサンプリングにより通信オーバーヘッド削減とプライニングのカスタマイズを推進

連合学習を使ってプライバシーを守りながら、効率よくモデルを軽量化する技術を提案してるみたい。データのプライバシーを守りつつ計算コストも減らせるなんて、すごく実用的で面白そう！これが広まると、もっと便利になりそうだね。

**Comment:** Preprint

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-18 20:33

- - -

### [SYNOSIS: Image synthesis pipeline for machine vision in metal surface inspection](http://arxiv.org/abs/2410.14844)

**SYNOSIS: 金属表面検査における機械視覚のための画像合成パイプライン**

Juraj Fulir, Natascha Jeziorski, Lovro Bosnar, Hans Hagen, Claudia Redenbach, Petra Gospodnetić, Tobias Herrfurth, Marcus Trost, Thomas Gischkat

- 機械学習による視覚検査システムは有望だが、データの量と多様性に依存する
- 誤差や費用、高頻度の欠陥や製品面の多様さが課題
- パラメトリック合成データセット生成で、データ取得の問題を回避
- 実データと合成データを用いた欠陥検出モデルの訓練で成果を示す

合成データを使って、金属の表面検査がもっと簡単になるならすごいよね！これが普及すれば、品質管理もどんどん進化しそうでワクワクする。

**Comment:** Initial preprint, 21 pages, 21 figures, 6 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CE, cs.GR, I.2.1; I.2.10; I.4.6; I.4.9; I.4.7; I.3.8; I.3.6; I.3.5; I.3.7;
  I.5.4; J.6; J.7, **投稿日時:** 2024-10-18 19:46

- - -

### [Differentially Private Covariate Balancing Causal Inference](http://arxiv.org/abs/2410.14789)

**差分プライバシーによる共変量バランスの因果推論**

Yuki Ohnishi, Jordan Awan

- 差分プライバシーはプライバシー保護のための主要な枠組みであり、個人情報の漏洩を防ぐ
- 観察データでの因果推論は、治療群の共変量バランスが必要だが、情報の漏洩を防ぐため確認が困難
- 本研究では、観察データから因果効果を推測する差分プライバシー対応の二段階共変量バランス重み推定器を提案
- アルゴリズムは、プライバシー予算下で一貫性や速度最適性などの統計的保証を持つ推定器を生成

個人情報を守りつつ、因果関係を正確に推論するなんて革新的だよね！安全性を保障しつつデータを解析できる未来には可能性が広がりそうで、わくわくしちゃう！

**Comment:** 30 pages

**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ME, cs.CR, cs.LG, **投稿日時:** 2024-10-18 18:02

- - -

### [What's New in My Data? Novelty Exploration via Contrastive Generation](http://arxiv.org/abs/2410.14765)

**私のデータに何が新しいのか？対比生成による新規性の探索**

Masaru Isonuma, Ivan Titov

- 微調整データセットの新規性を発見するため、生成例を用いて特性を特定するタスクを提案
- 対比生成探索 (CGE) により既存モデルと微調整後モデルを比較し、新規特性を明らかに
- 同様の例の生成を改善するため、反復プロセスを導入し、生成物の多様性を促進
- 差分プライバシー技術を用いて微調整した場合でもCGEは効果的で、新言語や毒性言語も検出

データの新しさを発見するって面白い！特に、差分プライバシーの技術を活用して新しい内容を見つける方法、未来に活かせそうだよね。なんか便利そうだし、これからの活用の可能性にワクワクする！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-10-18 15:24
