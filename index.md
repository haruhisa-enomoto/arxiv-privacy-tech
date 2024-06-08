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

更新: 2024-06-08T04:18:54.941975

- - -

### [Everything to the Synthetic: Diffusion-driven Test-time Adaptation via Synthetic-Domain Alignment](http://arxiv.org/abs/2406.04295)

**すべて合成データへ: 合成ドメイン整合による拡散駆動テストタイム適応**

Jiayi Guo, Junhao Zhao, Chunjiang Ge, Chaoqun Du, Zanlin Ni, Shiji Song, Humphrey Shi, Gao Huang

- テストタイム適応(TTA)は、未知のターゲットドメインでソースドメインで事前学習したモデルの性能を向上させるための技術
- 既存の拡散駆動TTAメソッドは、ターゲットデータを合成データに変換し、モデルの重み調整を避ける方法で強い性能を発揮
- 本研究では、ソースモデルと合成データのドメインが一致していない問題を指摘し、Synthetic-Domain Alignment (SDA)フレームワークを提案
- 実験結果は、SDAが優れたドメイン整合を実現し、既存の拡散駆動TTAメソッドを一貫して上回ることを示している

この技術って、未知のドメインでもちゃんと動くようにできるから超便利じゃない？ハードル高そうだけど成功したら革命的だと思うな！

**Comment:** GitHub:   https://github.com/SHI-Labs/Diffusion-Driven-Test-Time-Adaptation-via-Synthetic-Domain-Alignment

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-06 17:39

- - -

### [What is Dataset Distillation Learning?](http://arxiv.org/abs/2406.04284)

**データセット蒸留学習とは何か**

William Yang, Ye Zhu, Zhiwei Deng, Olga Russakovsky

- データセット蒸留は、大規模データセットの課題を克服するために考案された戦略である
- 蒸留データは高性能なモデルを訓練するために使用できるが、情報の保存方法はまだ不明である
- 蒸留データは標準的な評価設定外での訓練時に実データの代替にはならない
- 蒸留プロセスは、実モデルの初期訓練動態に関連する情報を圧縮することで高いタスク性能を保持する

データセット蒸留についてさらに理解を深められるってワクワクするね！学習データの効率化が進めば、機械学習がもっと身近になるかも。

**Comment:** ICML 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-06 17:28

- - -

### [R-CONV: An Analytical Approach for Efficient Data Reconstruction via Convolutional Gradients](http://arxiv.org/abs/2406.04227)

**R-CONV: 畳み込み勾配を通じた効率的なデータ再構築のための分析アプローチ**

Tamer Ahmed Eltaras, Qutaibah Malluhi, Alessandro Savino, Stefano Di Carlo, Adnan Qayyum, Junaid Qadir

- 連合学習は、勾配共有を利用してプライバシーを保護しつつ分散データから学習する方法
- 畳み込み層に対しては効果が低いが、それでも勾配から入力データを再構築可能
- ReLUなどの完全な逆関数を持たない場合でも、勾配から訓練サンプルを再構築できる
- 既存の分析手法は勾配攻撃のリスク評価が不正確で、実際には報告の5%未満の制約で攻撃可能

勾配からデータが漏れちゃうことを考えると、連合学習も完全じゃないんだね。でも、新しい手法でさらに深掘りできるのは面白そう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.CV, **投稿日時:** 2024-06-06 16:28

- - -

### [Federated TrustChain: Blockchain-Enhanced LLM Training and Unlearning](http://arxiv.org/abs/2406.04076)

**連合信頼チェーン：ブロックチェーン強化されたLLM訓練と忘却**

Xuhan Zuo, Minghao Wang, Tianqing Zhu, Lefeng Zhang, Dayong Ye, Shui Yu, Wanlei Zhou

- LLMの訓練には多くの新しいデータが必要であり、公開データが枯渇する問題がある
- 連合学習が新しい解決策として登場し、プライベートデータをLLMグローバルモデルに貢献させる
- ブロックチェーン技術を利用し、貢献内容の改ざん防止記録と透明性の確保を提案する
- Hyperledger Fabricを統合し、安全性、透明性、および検証可能性を高める

連合学習とブロックチェーンってすごいね！これでLLMの透明性も確保できるし、もっと公平で便利になりそう。楽しみ～😘

**Comment:** 16 pages, 7 figures,

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-06 13:44

- - -

### [Dynamic angular synchronization under smoothness constraints](http://arxiv.org/abs/2406.04071)

**滑らかさの制約下での動的角度同期化**

Ernesto Araya, Mihai Cucuringu, Hemant Tyagi

- 角度同期化問題は、ノイズを含むペア間の測定値から未知の角度を復元するものである
- 本研究では、時間とともに変化する角度と測定グラフを考慮した動的問題を扱う
- 3つのアルゴリズムを導出し、特に1つのアルゴリズムについて非漸近的な回復保証を確立
- 測定グラフが非常に疎で不連結な場合やノイズが大きくなる場合でも条件が緩和される

動的な問題に注目してるのが面白い！特に測定ノイズが増える場合にちゃんと対処しているところ、すごいね。

**Comment:** 40 pages, 9 figures

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, math.ST, stat.TH, **投稿日時:** 2024-06-06 13:36

- - -

### [How Good is Zero-Shot MT Evaluation for Low Resource Indian Languages?](http://arxiv.org/abs/2406.03893)

**ゼロショットMT評価は低リソースのインド言語にどれだけ有効か？**

Anushka Singh, Ananya B. Sai, Raj Dabre, Ratish Puduppully, Anoop Kunchukuttan, Mitesh M Khapra

- 高リソースの言語に比べ、低リソース言語の翻訳評価への関心が最近高まっている
- アッサム語、カンナダ語、マイティリー語、パンジャブ語を対象にゼロショット評価を実施
- 人間の評価と自動評価指標のケンダールタウとピアソン相関は最大0.32と0.45
- 合成データのアプローチは混合結果となり、評価のギャップを埋めるにはまだ課題が多い

低リソース言語の評価ってまだ難しいんだね。でもこれからの技術進歩が楽しみだね。インドの多様な言語について学ぶ良い機会になりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-06 09:28

- - -

### [Lean Workbook: A large-scale Lean problem set formalized from natural language math problems](http://arxiv.org/abs/2406.03847)

**Leanワークブック：自然言語の数学問題から形式化された大規模なLean問題集**

Huaiyuan Ying, Zijian Wu, Yihan Geng, Jiayu Wang, Dahua Lin, Kai Chen

- 大規模な言語モデルは自然言語処理タスクで印象的な能力を示している
- 形式言語（Lean）での数学定理証明には苦手
- 提案された新しいパイプラインが合成データを生成し、自然言語数学問題をLean 4文に翻訳
- 最終データセットは約57Kの形式-非形式質問ペアと21の新IMO問題を含む

新しい方法で自然言語の数学問題をLean形式に変換してるんだね！これから、数学問題の解決がもっと効率的になりそうでワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-06 08:25

- - -

### [Continual Counting with Gradual Privacy Expiration](http://arxiv.org/abs/2406.03802)

**漸時的プライバシー消費における持続的カウント**

Joel Daniel Andersson, Monika Henzinger, Rasmus Pagh, Teresa Anna Steiner, Jalaj Upadhyay

- 差分プライバシーが時間と共に漸次消費されるモデルを研究
- バイナリカウント問題に対して上限と下限を提供
- アルゴリズムは多くのプライバシー消費関数に対して適用可能
- 実験結果でプライバシー消費が緩やかに増加することを確認

漸次的プライバシー消費って新しい考え方で興味深いね。これを使えば、長期間データを扱う場合にプライバシーを効果的に守れそうだね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, **投稿日時:** 2024-06-06 07:20

- - -

### [Low-Rank Similarity Mining for Multimodal Dataset Distillation](http://arxiv.org/abs/2406.03793)

**マルチモーダルデータセット蒸留のための低ランク類似性マイニング**

Yue Xu, Zhilin Lin, Yusong Qiu, Cewu Lu, Yong-Lu Li

- マルチモーダルデータ（例：画像-テキストペア）は独自の課題を抱えている
- 提案する低ランク類似性マイニング（LoRS）は効率性とスケーラビリティを兼ね備えている
- LoRSは画像-テキストペアと同時に真実の類似性行列を蒸留する
- LoRSは既存のアルゴリズムに対して著しい改善をもたらす

画像とテキストを使った類似性マイニング、めっちゃ新しいアイデアだね！効率よくデータセットを蒸留して、色んな可能性広がりそう。

**Comment:** Accepted at ICML 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-06-06 07:05

- - -

### [NAP^2: A Benchmark for Naturalness and Privacy-Preserving Text Rewriting by Learning from Human](http://arxiv.org/abs/2406.03749)

**NAP^2: 人間から学んだ自然でプライバシー保護されたテキストリライトのベンチマーク**

Shuo Huang, William MacLean, Xiaoxi Kang, Anqi Wu, Lizhen Qu, Qiongkai Xu, Zhuang Li, Xingliang Yuan, Gholamreza Haffari

- 第三者提供のNLPモデルで敏感なテキストを処理する際のプライバシー漏洩が問題
- 人間の削除と抽象化戦略を用いて敏感な表現を消去・隠蔽し、プライバシーを保護
- クラウドソーシングと大型言語モデル（LLM）を用いて新たなコーパスNAP^2を作成
- 差分プライバシーに基づく従来手法より、自然なリライトと情報有用性のバランスが向上

新しいリライト方法で、もっと自然で便利なテキストを作れるかも！実験結果とかも興味深いね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-06 05:07

- - -

### [FACOS: Enabling Privacy Protection Through Fine-Grained Access Control with On-chain and Off-chain System](http://arxiv.org/abs/2406.03695)

**FACOS：オンチェーンとオフチェーンシステムによる細粒度アクセス制御でのプライバシー保護の実現**

Chao Liu, Cankun Hou, Tianyu Jiang, Jianting Ning, Hui Qiao, Yusen Wu

- データ主導の環境における情報の連続生成は、セキュアな保存と効率的な伝達、および細粒度アクセス制御を必要とする
- ブロックチェーン技術は非中央集権的な保存を提供し、データのセキュリティとアクセシビリティを維持
- 提案したFACOSは、クライアント認証や許可を必要とするオンチェーンとオフチェーンのプライバシー保護を提供
- 評価結果は、他の最新設計と比較してFACOSが優れたスケーラビリティと実用性を提供することを示す

細粒度アクセス制御をブロックチェーンで実現するなんて、未来のデータ社会を見据えてる感じがする！他のシステムと比較して実用的だって部分も信頼できるよね。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-06 02:23

- - -

### [Bidding in Uniform Price Auctions for Value Maximizing Buyers](http://arxiv.org/abs/2406.03674)

**価値最大化バイヤーのための均一価格オークション入札**

Negin Golrezaei, Sourav Sahoo

- 実用で広く使われる均一価格オークションの入札問題を研究
- 行動モデルの仮定が理論と実際の差異の要因として分析
- ROI制約内で累積価値を最大化するために、一般化された$m$均一入札形式を提案
- 数値シミュレーションにより、UF入札ポリシーが理論的な境界を超えて高い効果を示す

この研究、面白そう！オークション戦略に新しい視点が入って、今後の入札方式がもっと進化しそうだね。

**Comment:** 43 pages, 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.DS, cs.GT, **投稿日時:** 2024-06-06 01:29

- - -

### [Synthetic Oversampling: Theory and A Practical Approach Using LLMs to Address Data Imbalance](http://arxiv.org/abs/2406.03628)

**合成オーバーサンプリング：データ不均衡に対処するための理論とLLMを用いた実践的アプローチ**

Ryumei Nakada, Yichen Xu, Lexin Li, Linjun Zhang

- データ不均衡と偽相関は機械学習とデータサイエンスの一般的な課題
- オーバーサンプリングは、少数派クラスのインスタンス数を人工的に増やす手法
- OPALは大規模言語モデル（LLM）の能力を活用して少数派のための高品質な合成データを生成
- 理論的に合成データの利点を示し、変数とラベル両方で高品質なデータ生成を実証

合成データを使ってデータ不均衡を解決する新しい方法、すごく興味あるよ！実際にどうやって高品質なデータを作れるのか知りたいな～。

**Comment:** 59 pages, 7 figures

**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-06-05 21:24

- - -

### [FedPylot: Navigating Federated Learning for Real-Time Object Detection in Internet of Vehicles](http://arxiv.org/abs/2406.03611)

**FedPylot: インターネット・オブ・ビークルズにおけるリアルタイム物体検出のための連合学習のナビゲーション**

Cyprien Quéméneur, Soumaya Cherkaoui

- 自動運転車は機械学習に依存しており、エッジで生成される膨大なセンシングデータが有益
- 連合学習により道路利用者のプライバシーを保護し、通信負荷を軽減可能
- YOLOv7モデルを用いて、データの不均衡やコンセプトドリフトなどの問題に対処
- FedPylotは、ハイブリッド暗号化でサーバーとクライアントの通信を保護するプロトタイプ

新しい研究ってワクワクするよね！特に、IoVでの連合学習がこんなに実用的に使えるなんて、本当に未来の技術って感じるな。これは絶対に注目だよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, cs.DC, **投稿日時:** 2024-06-05 20:06

- - -

### [Fantastyc: Blockchain-based Federated Learning Made Secure and Practical](http://arxiv.org/abs/2406.03608)

**Fantastyc: ブロックチェーンに基づいた連合学習のセキュアかつ実用的な実現**

William Boitier, Antonella Del Pozzo, Álvaro García-Pérez, Stephane Gazut, Pierre Jobic, Alexis Lemaire, Erwan Mahe, Aurelien Mayoue, Maxence Perion, Deepika Singh, Tuanir Franca Rezende, Sara Tucci-Piergiovanni

- 連合学習は、複数のクライアントが中央サーバの調整の下で協力して機械学習モデルを訓練する分散型フレームワークである
- ブロックチェーンベースの連合学習アプローチは完全な分散型解決策と追跡性を保証するが、依然として整合性、機密性、スケーラビリティにおける課題がある
- Fantastycはこれらの課題を同時に解決するために設計されたものである
- 本研究では、これらの未解決の課題に取り組む新しいソリューションを提案する

Fantastycがどんな風に実際の課題を解決するのか気になる！今後の実用化が楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, **投稿日時:** 2024-06-05 20:01

- - -

### [Hi5: 2D Hand Pose Estimation with Zero Human Annotation](http://arxiv.org/abs/2406.03599)

**Hi5: 人間のアノテーションが不要な2Dハンドポーズ推定**

Masum Hasan, Cengiz Ozel, Nina Long, Alexander Martin, Samuel Potter, Tariq Adnan, Sangwu Lee, Amir Zadeh, Ehsan Hoque

- 新たな合成データセットHi5を提案し、人間のアノテーションや検証が不要な方法を開発
- パイプラインは高忠実度の3Dハンドモデルと動的環境、カメラ動作を用いてデータ多様性を制御
- 単一のPCで58万3千枚の画像を生成し、リアルな変化を反映した正確なポーズアノテーションを付与
- Hi5で訓練したモデルは、被遮蔽や撹乱に対して実データで訓練したモデルを上回る性能を示す

この研究、すごいね！バリエーションに強いモデルを手軽に作れるようになるなんて、未来の技術が楽しみだよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.GR, cs.LG, **投稿日時:** 2024-06-05 19:45

- - -

### [Stateless and Non-Interactive Order-Preserving Encryption for Outsourced Databases through Subtractive Homomorphism](http://arxiv.org/abs/2406.03559)

**アウトソーシングされたデータベースのための減算準同型によるステートレスかつ非対話型の順序保持暗号**

Dongfang Zhao

- 順序保持暗号（OPE）は、暗号化されたタプルをソートしてインデックスを作成し範囲クエリを完了させるための重要な技術である
- 現行のOPEスキームは、クライアントが平文と暗号文のマッピングを管理する必要があり、クエリ中にクライアントとサーバーの相互作用も必要としている
- 提案された新しいOPEスキームはステートレスクライアントに適しており、クエリ中にクライアントサーバー間の相互作用を必要としない
- 提案されたプロトコルは、準同型暗号の加法特性を活用して、評価キーを用いた代数操作により二つの平文間の差の符号を明らかにする

ステートレスで相互作用なしってめっちゃ便利！データベースの管理が楽になる未来が見えてきたね。クライアントがアクセスできないときでも機能するってのがとても頼もしい感じ！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-06-05 18:14

- - -

### [Noise-Aware Algorithm for Heterogeneous Differentially Private Federated Learning](http://arxiv.org/abs/2406.03519)

**異種差分プライバシー連合学習のためのノイズ対応アルゴリズム**

Saber Malekmohammadi, Yaoliang Yu, Yang Cao

- 連合学習システムは高効用と厳密なデータプライバシーを目指している
- クライアント毎に異なるプライバシー要件があると、効用が低下する問題がある
- 提案されたRobust-HDPは、クライアントのモデル更新における真のノイズレベルを効果的に推定し、集約モデルのノイズレベルを大幅に低減する
- Extensiveな実験結果と理論解析により、Robust-HDPの効果が確認された

クライアントに信頼をおかなくて済むのっておもしろいよね。さまざまなデータ量でも適応できるのすごく未来志向だよ！

**Comment:** Proceedings of the 41 st International Conference on Machine   Learning, Vienna, Austria. PMLR 235, 2024

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-06-05 17:41

- - -

### [Buffered Asynchronous Secure Aggregation for Cross-Device Federated Learning](http://arxiv.org/abs/2406.03516)

**クロスデバイス連合学習のためのバッファード非同期セキュアアグリゲーション**

Kun Wang, Yi-Rui Yang, Wu-Jun Li

- 非同期連合学習（AFL）はデバイスの異質性に対処する有効な方法である
- 従来のセキュアアグリゲーションプロトコルは同期アグリゲーションに基づいており、AFLと互換性がない
- 提案するBASAは、各ユーザーがサーバーと1回の非同期通信でセキュアアグリゲーションを実現できる
- BASAを用いたAFLは、追加のハードウェア要件なしでトレーニング効率とスケーラビリティが向上する

この研究、画期的だね！特にユーザーの負担を最小限に抑えつつ、効率を上げられるところがすごく魅力的💡



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-06-05 16:39
