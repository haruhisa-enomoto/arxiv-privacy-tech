---
layout: single
title: トップページ
permalink: /
author_profile: true
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

To be written.

## 最新更新分

更新: 2024-05-01T04:20:08.778088

- - -

### [Succinct arguments for QMA from standard assumptions via compiled nonlocal games](http://arxiv.org/abs/2404.19754)

**標準的な仮定からQMAのための簡潔な議論体系**

Tony Metger, Anand Natarajan, Tina Zhang

- 標準的な暗号学的仮定からQMAのための簡潔な古典的議論体系を構築
- 使用する主要な原始要素は、衝突耐性ハッシュ関数と量子準同型暗号の軽減バージョン
- 従来はポスト量子安全な不可判別性帳簿化に依存していたが、提案手法ではより弱い原始要素を使用
- 構築プロトコルは任意の量子非局所ゲームを議論体系にコンパイルする一般的変換を使用している

**Comment:** 57 pages

**トピック:** [準同型暗号](he), **カテゴリ:** quant-ph, cs.CR, **投稿日時:** 2024-04-30 17:58

- - -

### [Fairness Without Demographics in Human-Centered Federated Learning](http://arxiv.org/abs/2404.19725)

**人中心連合学習における人口統計なしの公平性**

Roy Shaily, Sharma Harshit, Salekin Asif

- 連合学習（FL）における公平性を確保するための研究ギャップが存在し、現在の公平性戦略はバイアスのある属性の知識を必要とするが、これがFLのプライバシー原則と矛盾する
- 機械学習の「人口統計なしの公平性」に触発された新しいバイアス緩和アプローチを提示し、トレーニング中にヘッシアン行列のトップ固有値を最小化することにより、FL参加者間で公平な損失風景を確保
- 新しいFLアグリゲーション方式を導入し、エラー率と損失風景の曲率属性に基づいて参加モデルを評価し、FLシステム全体に公平性を促進
- このアプローチは、単一および複数のバイアス要因を含むさまざまな現実世界のアプリケーションにおいて、公平性と効率のバランスを効果的に示し、人中心FLにおいて重要な進歩を表す



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-04-30 17:19

- - -

### [Fake it to make it: Using synthetic data to remedy the data shortage in joint multimodal speech-and-gesture synthesis](http://arxiv.org/abs/2404.19622)

**合成データを用いた音声とジェスチャーの合同多モード合成によるデータ不足の解決**

Shivam Mehta, Anna Deichler, Jim O'Regan, Birger Moëll, Jonas Beskow, Gustav Eje Henter, Simon Alexanderson

- 人間は対面会話で言葉と非言語的な動作を同時に用いるが、テキストからの音声と3Dジェスチャーの同時合成技術は新しく発展途上である
- 既存の合成モデルは大きなデータセットに依存するため、データ不足が問題となっている
- 単一モード合成モデルを用いて合成トレーニングデータを生成し、それを使用して新しい合成モデルを事前訓練する方法を提案
- 提案された新しい合成アーキテクチャは、合成された音声と動作の質を向上し、より優れたプロソディモデリングを可能にする

**Comment:** 13+1 pages, 2 figures, accepted at the Human Motion Generation   workshop (HuMoGen) at CVPR 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.HC, cs.CV, cs.GR, cs.SD, eess.AS, 68T07 (Primary), 68T42 (Secondary), I.2.7; I.2.6; H.5, **投稿日時:** 2024-04-30 15:22

- - -

### [Physical Non-inertial Poser (PNP): Modeling Non-inertial Effects in Sparse-inertial Human Motion Capture](http://arxiv.org/abs/2404.19619)

**非慣性系における人体モーションキャプチャのための物理的非慣性ポーザー（PNP）のモデリング**

Xinyu Yi, Yuxiao Zhou, Feng Xu

- ヒューマンルート座標系を非慣性系として理論的に検討し、ルートの加速や回転時に見落とされがちな慣性力をモデル化
- 自己回帰推定器を利用して慣性力を正確に補償し、ニュートンの運動法則に準じたモーションキャプチャを実現
- 加速度と体の動きの関係を学習可能にし、神経ネットワークを訓練してモーションキャプチャを改善
- 合成データを用いた神経ネットワークトレーニングとシミュレーションによるIMU合成を開発して、ハードウェアのノイズモデルを適切にモデル化し、システムのロバスト性を向上

**Comment:** Accepted by SIGGRAPH 2024 Project Page:   https://xinyu-yi.github.io/PNP/

**トピック:** [合成データ](sd), **カテゴリ:** cs.GR, **投稿日時:** 2024-04-30 15:19

- - -

### [Let's Focus: Focused Backdoor Attack against Federated Transfer Learning](http://arxiv.org/abs/2404.19420)

**集中攻撃: 連合転移学習に対する集中バックドア攻撃**

Marco Arazzi, Stefanos Koffas, Antonino Nocera, Stjepan Picek

- 連合転移学習(FTL)では特徴抽出の事前学習が一方の当事者（通常はサーバー）によって行われる
- 本研究では、連合学習フェーズにおいてクライアントの一部がXAIとデータセット蒸留を組み合わせてバックドア攻撃の脆弱性を探る
- 攻撃は、XAIを用いてトリガーの最適な局所を特定し、バックドアクラスの圧縮情報を封じ込める方法で実行される
- 提案された攻撃（FB-FTLと短縮される）は、画像分類シナリオでテストされ、平均80％の攻撃成功率を示し、既存の防御手法にも効果を持つことが確認された



**トピック:** [連合学習](fl), [連合転移学習](ftl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-04-30 10:11

- - -

### [Deep Learning Forecasts Caldera Collapse Events at Kīlauea Volcano](http://arxiv.org/abs/2404.19351)

**Kīlauea火山のカルデラ崩壊イベントの深層学習予測**

Ian W. McBrearty, Paul Segall

- 2018年のハワイ、キラウェア火山の3ヶ月間の噴火中に、既存の火口カルデラが60回以上の準周期的な崩壊イベントを経験
- 崩壊イベントの最後の40回は、マグニチュード5以上の非常に長い周期(VLP)の地震を引き起こし、イベント間の時間は0.8日から2.2日だった
- 深層学習を用いたグラフニューラルネットワーク(GNN)を訓練して、カルデラ崩壊イベントの時間までを予測し、初期のデータの一部分だけを用いて数時間以内に予測
- 高SNRの傾斜計データを使用した時の予測が最も正確であり、合成データで教育されたGNNはほぼ一定のストレス閾値で崩壊を予測し、カルデラ崩壊の物理的要因を感知していることを示す



**トピック:** [合成データ](sd), **カテゴリ:** physics.geo-ph, cs.LG, **投稿日時:** 2024-04-30 08:28

- - -

### [C2FDrone: Coarse-to-Fine Drone-to-Drone Detection using Vision Transformer Networks](http://arxiv.org/abs/2404.19276)

**C2FDrone: 粗大から細かいまでのドローン間検出のためのビジョントランスフォーマーネットワーク**

Sairam VC Rebbapragada, Pranoy Panda, Vineeth N Balasubramanian

- ドローン同士の検出は衝突回避や敵対的ドローンの対処、捜索救助活動に不可欠
- 小さな対象物のサイズや歪み、遮蔽、リアルタイム処理が挑戦的な問題点とされる
- 新たに提案された粗大から細かいまでの検出戦略はビジョントランスフォーマーに基づく
- 提案モデルはFL-Drones、AOT、NPS-DronesデータセットでF1スコアをそれぞれ7%、3%、1%向上し、エッジコンピューティングデバイスでのリアルタイム処理が可能

**Comment:** Accepted at ICRA 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-30 05:51

- - -

### [Zero Knowledge Proof for Multiple Sequence Alignment](http://arxiv.org/abs/2404.19064)

**多重配列アライメントのためのゼロ知識証明**

Worasait Suwannik

- 多重配列アライメント（MSA）は生物情報学における基本的なアルゴリズムである
- 入力配列やアライメントスコアは公開されるが、アライメント自体は保護される必要がある場面でゼロ知識証明が利用される
- 入力配列、アライメント、アライメントスコアの一貫性を検証するバリデータがCircom言語で記述される
- zkSNARKというゼロ知識証明システムを用いて、回路とその入力に対して暗号論的証明が生成され、実際のアライメントを明かすことなくすべての入力が一貫していることを示す



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-04-29 19:11

- - -

### [An Aggregation-Free Federated Learning for Tackling Data Heterogeneity](http://arxiv.org/abs/2404.18962)

**データの不均一性に対処するための集約フリー連合学習**

Yuan Wang, Huazhu Fu, Renuga Kanagavelu, Qingsong Wei, Yong Liu, Rick Siow Mong Goh

- 従来の連合学習では、サーバーが集約したグローバルモデルを元にローカルモデルを更新するが、クライアント間のデータの不均一性がこのプロセスのパフォーマンスを低下させる
- 新しいアルゴリズムFedAFは、集約を行わずクライアント間で知識を共有し、より効果的なデータの凝縮を行うことでクライアントのドリフト問題を解決
- FedAFはデータの不均一性が大きい環境でも高品質な凝縮データを生成し、グローバルモデルのパフォーマンスと収束速度を向上
- 数多くのベンチマークデータセットでの数値実験により、FedAFは特にラベルの偏りや特徴の偏りがあるデータの不均一性に対処する能力が高いことが示された

**Comment:** Accepted to CVPR 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-04-29 05:55

- - -

### [Decoder Decomposition for the Analysis of the Latent Space of Nonlinear Autoencoders With Wind-Tunnel Experimental Data](http://arxiv.org/abs/2404.19660)

**非線形オートエンコーダの潜在空間解析のためのデコーダ分解：風洞実験データを用いた研究**

Yaxin Mo, Tullio Traverso, Luca Magri

- オートエンコーダの解釈性を向上させるために、デコーダ分解という後処理方法を提案
- 潜在変数を流れの整合性のある構造に関連付けるデコーダ分解を二次元非定常ウェイクデータに適用し、潜在空間の次元が自動エンコーダの解釈可能性に重要な影響を与えることを発見
- 三次元乱流ウェイクデータに対してデコーダ分解を適用し、潜在空間の次元とデコーダのサイズが再構成誤差に影響し、相関関係があることを示示
- デコーダ分解を用いて、整合性のある構造を表す潜在変数をランク付けし、望ましくないまたは不適切な潜在変数をフィルタリングするための有用性を示した



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, physics.flu-dyn, **投稿日時:** 2024-04-25 10:09

- - -

### [Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data](http://arxiv.org/abs/2404.01413)

**モデルの崩壊は避けられないのか？リアル・合成データの蓄積による再帰の呪いの打破**

Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, Sanmi Koyejo

- 生成モデルが自身の生成した出力で訓練された場合、モデル-データのフィードバックループにより「モデル崩壊」と呼ばれる現象が発生することが示唆されている
- 単一世代の合成データによる既存実データの置換はモデル崩壊を促進することが確認された
- 複数世代の合成データと元の実データを蓄積することでモデル崩壊を避けることが可能で、この結果は様々なモデルサイズやアーキテクチャで一貫している
- データが蓄積される場合、テストエラーは反復回数に依存せず有限上限を持つため、モデル崩壊は発生しないことが証明された



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, cs.ET, stat.ML, **投稿日時:** 2024-04-01 18:31
