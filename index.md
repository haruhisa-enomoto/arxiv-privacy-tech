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

更新: 2024-08-06T04:21:23.836498

- - -

### [Fair Resource Allocation For Hierarchical Federated Edge Learning in Space-Air-Ground Integrated Networks via Deep Reinforcement Learning with Hybrid Control](http://arxiv.org/abs/2408.02501)

**階層的連合エッジ学習のための公平なリソース割り当て：宇宙・空中・地上統合ネットワークにおけるハイブリッド制御を用いた深層強化学習によるアプローチ**

Chong Huang, Gaojie Chen, Pei Xiao, Jonathon A. Chambers, Wei Huang

- 宇宙・空中・地上統合ネットワーク（SAGIN）は広範なカバレッジと迅速な展開が可能で、将来の無線通信における重要な研究方向
- 階層的連合学習（HFL）とSAGINを統合し、多層集計機能を提供する新しいフレームワークを提案
- 複数の計算タスクを限られた衛星サービス時間内で公平に処理し、DSACアルゴリズムを用いてリソース割り当てを最適化
- 深層強化学習（DRL）のハイブリッド制御空間の効率性を向上させるため、新しい動的報酬関数を設計

宇宙を含むネットワークなんてSFみたいでワクワクするよね！未来の通信技術が進化して、私たちの生活ももっと便利になりそう。

**Comment:** Accepted for publication in IEEE Journal on Selected Areas in   Communications

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, eess.SP, math.IT, **投稿日時:** 2024-08-05 14:22

- - -

### [Attenuation-adjusted deep learning of pore defects in 2D radiographs of additive manufacturing powders](http://arxiv.org/abs/2408.02427)

**アディティブ製造粉の2次元X線画像における空孔欠陥の減衰調整型深層学習**

Andreas Bjerregaard, David Schumacher, Jon Sporring

- 金属供給粉末のガスポアが最終製品に大きな影響を与える
- 高精度な分割を達成するため、X線減衰モデルとUNet変異体を使用
- 提案モデルは、合成データでの事前訓練、粒子の切り取り、理想的な粒子との差分を使用
- 最速の方法では粒子の分割が平均0.014秒でF1スコア0.78、最も正確な方法では0.291秒でF1スコア0.87

高精度なポア検出がスピードアップして現場で使えるようになるなんて、未来感すごいよね。効率化が進んで、製造品質も一気に向上しそうで楽しみ！

**Comment:** Implementation on https://github.com/yhsure/porosity

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, eess.IV, 68U10 (Primary) 68T45, 68T07, 94A08 (Secondary), I.4.6; I.4.1; J.2; I.2.10; I.5.4, **投稿日時:** 2024-08-05 12:34

- - -

### [Strategic Federated Learning: Application to Smart Meter Data Clustering](http://arxiv.org/abs/2408.02384)

**戦略的連合学習: スマートメーターデータのクラスタリングへの応用**

Hassan Mohamad, Chao Zhang, Samson Lasaulce, Vineeth S Varma, Mérouane Debbah, Mounir Ghogho

- 連合学習(FL)では、複数のクライアントが各自のデータで訓練したモデルを融合センター(FC)と共有
- 従来のFLは、モデル情報(MI)の最終的な利用を無視、提案手法はMIを基にしたFCの意思決定がクライアントの効用を左右
- クライアントはMIを使って効用を最大化するが、場合によっては戦略的ノイズを加えた方が有利
- 具体例として、電力消費スケジューリング問題に適用、クライアントとFCの効用の不一致が示される

戦略的にノイズを加えて効用を上げる話って面白そう！実際の電力データでの検証も興味深いなあ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.GT, **投稿日時:** 2024-08-05 11:16

- - -

### [Operationalizing Contextual Integrity in Privacy-Conscious Assistants](http://arxiv.org/abs/2408.02373)

**プライバシー志向アシスタントにおける文脈的整合性の運用**

Sahra Ghalebikesabi, Eugene Bagdasaryan, Ren Yi, Itay Yona, Ilia Shumailov, Aneesh Pappu, Chongyang Shi, Laura Weidinger, Robert Stanforth, Leonard Berrada, Pushmeet Kohli, Po-Sen Huang, Borja Balle

- 高度なAIアシスタントはユーザー情報へのアクセスで劇的に有用性が向上するが、プライバシー懸念が生じる
- アシスタントが適切に情報共有するために、文脈的整合性(CI)を運用することを提案
- CIに基づいてアシスタントの行動を誘導するための複数の戦略を設計および評価
- 合成データと人間の注釈を用いた新しいフォーム入力ベンチマークで、CIベースの推論が強力な結果を示す

高度なAIとプライバシーのバランスを取る新しいアプローチが面白そう！文脈に応じた情報の流れをどう制御するか、未来のAI活用に期待が膨らむね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-08-05 10:53

- - -

### [A Lower Bound for Local Search Proportional Approval Voting](http://arxiv.org/abs/2408.02300)

**局所探索による比例承認投票の下限**

Sonja Kraiczy, Edith Elkind

- 異質な$n$人のエージェントの好みに基づいて$m$個のアイテムから$k$個を選定する問題を研究
- 和声的効用関数を用いた比例承認投票(PAV)が、効用最適化と公正な投票ルールを満たす
- PAVの当選セットを見つけることはNP困難であり、Azizらは局所探索版PAVを提案
- $\varepsilon$を非常に小さく設定した場合、アルゴリズムの実行時間が超多項式であることを証明

局所探索のアルゴリズムがどこまで効率的なのかを実験で確認しているのが面白そう！私たちの研究にも何か応用できるかもね。

**Comment:** 26 pages including appendix, accepted to ESA 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.GT, **投稿日時:** 2024-08-05 08:17

- - -

### [One-Shot Collaborative Data Distillation](http://arxiv.org/abs/2408.02266)

**ワンショット協調データ蒸留**

Rayne Holland, Chandra Thapa, Sarah Ali Siddiqui, Wei Shao, Seyit Camtepe

- 大規模な機械学習データセットを情報豊かな合成データに蒸留することで効率的なモデル学習が可能
- 合成データセットはデータ共有の通信コストを削減し、分散ネットワーク環境での機械学習アプリケーションの効率的な導入を支持
- 既存手法では各クライアントが局所的にデータ蒸留し、それをサーバーに統合するが、データ分布の異質性が品質を低下させる
- コラボレーションデータ蒸留技術「CollabDM」を提案し、クライアントとサーバー間の通信は1回のみでグローバルなデータ分布を捕捉、最先端のワンショット学習手法を上回る性能を示した

一回の通信でグローバルなデータ分布を反映できるなんてすご～い！5Gネットワークでの実用性も高そうだし、これからの分散学習が楽しみ♡



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, I.2, **投稿日時:** 2024-08-05 06:47

- - -

### [Advancing Post-OCR Correction: A Comparative Study of Synthetic Data](http://arxiv.org/abs/2408.02253)

**ポストOCR修正の進展：合成データの比較研究**

Shuhao Guan, Derek Greene

- 合成データを用いた実験で、データ量や拡張、生成方法がモデル性能に与える影響を評価
- 新しいアルゴリズムを紹介し、コンピュータビジョンの特徴検出でグリフの類似性を計算
- 複数の言語、特にリソースが少ない言語で実験を行い、手動で注釈されたデータなしでCERを減少させる
- 提案した合成データ生成方法は、特にリソースが少ない言語において従来の方法より有利であることを示した

ポストOCRって、テキストの修正を自動化するのに役立ちそう！合成データの使い方も進んでて、低リソースな言語にもいい影響が出るなんて、すごい可能性を感じるな。

**Comment:** ACL 2024 findings

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-08-05 05:56

- - -

### [Demystifying AMD SEV Performance Penalty for NFV Deployment](http://arxiv.org/abs/2408.02212)

**NFV展開におけるAMD SEVのパフォーマンスペナルティの解明**

Syafiq Al Atiiq, Aris Cahyadi Risdianto

- NFVは通信ネットワークをより適応可能なソフトウェアソリューションに移行させたが、新たなセキュリティ懸念が発生。
- IntelのSGXは潜在的な解決策だが、複雑なアプリケーション適応が必要。
- AMDのSEVはVMメモリを暗号化し、アプリケーションの変更なしにハイパーバイザレベルの脅威から保護。
- SEV-SNPでSnort NFを実行し、20%の平均パフォーマンスペナルティを示すが、多くのNFV展開にとって許容範囲と考えられる。

SEV-SNPが複雑なセキュリティ対策なしで一定のパフォーマンスを保ちつつ使えるなんて未来的！セキュリティとパフォーマンスのバランスが求められる今、役立ちそう〜。



**トピック:** [TEE](tee), **カテゴリ:** cs.NI, **投稿日時:** 2024-08-05 03:26

- - -

### [CodeACT: Code Adaptive Compute-efficient Tuning Framework for Code LLMs](http://arxiv.org/abs/2408.02193)

**CodeACT: コードLLMsのためのコード適応型効率的チューニングフレームワーク**

Weijie Lv, Xuan Xia, Sheng-Jun Huang

- CodeACTは、複雑性と多様性に基づいて高品質なトレーニングデータを選択するCDASを導入
- Dynamic Packパディング戦略により、トレーニング中のパディングトークンを最小化し、計算資源の使用を削減
- CodeACT-DeepSeek-Coder-6.7Bは、EVOL-Instructデータの40%の微調整のみで、HumanEvalで8.6%の性能向上を実現
- トレーニング時間を78%短縮し、ピークGPUメモリ使用量を27%削減

効率的なデータ選択とトレーニングにより、オープンソースのモデル性能を大きく向上させるCodeACT、すごく革新的だと思うな。これからリソース効率と性能の両立がもっと進むかもしれないね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-08-05 02:38

- - -

### [VidModEx: Interpretable and Efficient Black Box Model Extraction for High-Dimensional Spaces](http://arxiv.org/abs/2408.02140)

**VidModEx: 高次元空間に向けた解釈可能かつ効率的なブラックボックスモデル抽出**

Somnath Sendhil Kumar, Yuvaraj Govindarajulu, Pavan Kulkarni, Manojkumar Parmar

- 従来の方法は高次元入力空間でのスケーリングに苦戦し、多くの相互依存クラスの複雑性を管理するのが難しい
- SHAPを用いて合成データ生成を強化し、それにより特徴ごとの出力への寄与度を量化する
- エネルギーベースのGANを最適化することで画像分類モデルの精度を16.45%向上
- 動画分類モデルではUCF11、UCF101、Kinetics 400、Kinetics 600、Something-Something V2で最大33.36%の改善を達成

SHAPの使い方がすごく新しいね！動画も含む複雑なデータで大幅なパフォーマンスアップとか、これ未来あるよね。やっぱりデータの力って偉大だなーって感じる。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-08-04 20:38

- - -

### [Model Hijacking Attack in Federated Learning](http://arxiv.org/abs/2408.02131)

**連合学習におけるモデルハイジャック攻撃**

Zheng Li, Siyuan Wu, Ruichuan Chen, Paarijaat Aditya, Istemi Ekin Akkus, Manohar Vanga, Min Zhang, Hao Li, Yang Zhang

- モデルハイジャック攻撃により、MLモデルが元のタスクと異なるタスクを実行
- ハイジャックFLは連合学習における初のグローバルモデルハイジャック攻撃を提案
- 攻撃者はピクセルレベルの摂動を利用し、元のタスクとハイジャックタスクを一致させる
- 実験により、他のベースラインを上回る攻撃性能を実証し、防御方法も議論

モデルが巧妙にハイジャックされるなんて、連合学習の信頼性が問われるよね。防御策がうまく機能するかがこれからの鍵だね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-08-04 20:02

- - -

### [MedSyn: LLM-based Synthetic Medical Text Generation Framework](http://arxiv.org/abs/2408.02056)

**MedSyn: LLMベースの合成医療テキスト生成フレームワーク**

Gleb Kumichev, Pavel Blinov, Yulia Kuzkina, Vasily Goncharov, Galina Zubkova, Nikolai Zenovkin, Aleksei Goncharov, Andrey Savchenko

- 合成テキスト生成は医療などのプライバシーセンシティブな領域でのデータ不足の課題を解決
- MedSynは大規模言語モデルと医療知識グラフ(MKG)を統合した新しいフレームワーク
- GPT-4やLLaMAモデルを使用して合成臨床ノートを生成し、ICDコード予測タスクで評価
- 合成データを用いることで分類精度が最大17.8%向上し、ロシア語の最大規模のオープンソース合成データセットも提供

医療データの合成ってすごく面白いね！ロシア語のデータも手に入るから、国際的な研究が進みそうだよ。

**Comment:** 16 pages, accepted to ECML PKDD 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-08-04 15:07

- - -

### [LEGO: Self-Supervised Representation Learning for Scene Text Images](http://arxiv.org/abs/2408.02036)

**LEGO: 自己教師あり表現学習によるシーンテキスト画像認識**

Yujin Ren, Jiaxin Zhang, Lianwen Jin

- データ駆動型のシーンテキスト認識は進展しているが、実世界の注釈付きデータ不足が課題
- 合成データと実データの分布ギャップが実世界での性能向上を制約
- シーケンシャルな特性を考慮した新しい自己教師あり学習法LEGOを提案
- LEGOは他のテキスト関連タスクでも優れた性能を発揮し、6つのベンチマークで高評価

LEGOって名前がかわいい！自己教師あり学習がどんな風にテキスト認識を向上させるのか気になるね。他のテキスト関連タスクにも応用できるってのもめっちゃ未来を感じるなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-04 14:07

- - -

### [Personalized Federated Learning on Heterogeneous and Long-Tailed Data via Expert Collaborative Learning](http://arxiv.org/abs/2408.02019)

**異質かつロングテールデータに対する専門家協調学習による個別化連合学習**

Fengling Lv, Xinyi Shang, Yang Zhou, Yiqun Zhang, Mengke Li, Yang Lu

- 個別化連合学習（PFL）は各クライアントのデータを公開せずにカスタマイズされたモデルを取得することを目指す
- 現実のデータはしばしばロングテール分布に従い、これはPFLモデルの性能を低下させる要因になる
- クライアントごとの異質なデータ環境も連合学習の古典的な課題であり、その対応策が必要
- 専門家協調学習（ECL）を提案し、複数の専門家が異なるトレーニングサブセットを担うことで少数クラスを含む全クラスを十分に学習

ロングテールデータに対しても効果的に対応できるなんて、めちゃ興味深いね！私たちもこんな技術使ってデータ分析してみたら、びっくりするような新発見ができるかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-04 13:11

- - -

### [ENeRF: Efficient Event-Enhanced Neural Radiance Fields from Blurry Images](http://arxiv.org/abs/2408.01840)

**E$^3$NeRF: ぼやけた画像から効率的なイベント強化型ニューラル放射フィールドの生成**

Yunshan Qi, Jia Li, Yifan Zhao, Yu Zhang, Lin Zhu

- NeRFは異なる視点からの複数の画像を用いてボリューム3D表現を学習し、高いレンダリング性能を発揮
- ぼやけた入力から鋭いNeRFを再構築するのが難しい問題を解決するためにRGB画像とイベントストリームを組み合わせた新しい効率的なイベント強化型NeRF（E$^3$NeRF）を提案
- イベントストリームをニューラルボリューム表現学習に効果的に導入するために、イベント強化型ぼかしレンダリング損失とイベントレンダリング損失を提案
- E$^3$NeRFは異常な動きや低照度のシーンでも鋭いNeRFを効果的に学習できることを実証

イベントが画像のぼかしをどうやって消してくれちゃうのか気になるね！カメラの精度がもっと良くなる未来が見えるよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-03 18:47

- - -

### [A Deep CNN Model for Ringing Effect Attenuation of Vibroseis Data](http://arxiv.org/abs/2408.01831)

**振動検層データの鳴り響き効果を減衰させるための深層CNNモデル**

Zhuang Jia, Wenkai Lu

- 振動検層データ処理において、「鳴り響き効果」が性能を低下させる
- 深層CNNを用いた新しい鳴り響き減衰モデルを提案
- 実際のデータを合成して訓練し、モデルの学習を進める
- 深層CNNモデルが鳴り響き効果を効果的に減衰させることを実験で確認

深層学習と地球物理学の組み合わせってわくわくするね！データの詳細を保ちながらノイズを減らす方法、すごく面白そう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, physics.geo-ph, **投稿日時:** 2024-08-03 17:50

- - -

### [Joint Model Pruning and Resource Allocation for Wireless Time-triggered Federated Learning](http://arxiv.org/abs/2408.01765)

**無線時間発火連合学習のためのモデル剪定とリソース割当の同時最適化**

Xinlu Zhang, Yansha Deng, Toktam Mahmoodi

- 時間発火型連合学習は、ユーザーを固定時間間隔で階層に分ける
- デバイス増加と無線帯域幅の制約により遅延や通信オーバーヘッドが増加
- モデル剪定を適用し、剪定比率と帯域幅割当を最適化して訓練損失を最小化
- シミュレーション実験では、提案手法TT-Pruneが通信コストを40%削減しつつモデル収束を維持

時間発火型の連合学習にモデル剪定を組み合わせるなんて面白そう！これで効率的に学習できるなら、将来のIoTデバイスとかにも応用できそうだね。

**Comment:** Accepted in IEEE Global Communications Conference 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, math.IT, **投稿日時:** 2024-08-03 12:19

- - -

### [TreeCSS: An Efficient Framework for Vertical Federated Learning](http://arxiv.org/abs/2408.01691)

**TreeCSS: 垂直連合学習のための効率的なフレームワーク**

Qinbo Zhang, Xiao Yan, Yukai Ding, Quanqing Xu, Chuang Hu, Xiaokai Zhou, Jiawei Jiang

- 垂直連合学習は、データサンプルの特徴が異なる参加者間で分割されている状況を対象とする
- 主要なステップは共通データサンプルの特定（アライメント）と、これを用いたモデルのトレーニングである
- 提案したTreeCSSは、ツリーベースのMPSIプロトコルとコアセット選択を用いてこの二つのステップを加速
- TreeCSSはバニラVFLと比較して最大2.93倍のトレーニング速度を実現し、同等のモデル精度を達成

データの特徴が異なる参加者同士での学習を効率化するために、ツリーベースの手法を取り入れているって面白いね！未来の垂直連合学習の可能性が広がりそう。

**Comment:** 16 pages, 7 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-03 07:11

- - -

### [Fed-RD: Privacy-Preserving Federated Learning for Financial Crime Detection](http://arxiv.org/abs/2408.01609)

**Fed-RD: 金融犯罪検出のためのプライバシー保護連合学習**

Md. Saikat Islam Khan, Aparna Gupta, Oshani Seneviratne, Stacy Patterson

- Fed-RDは、金融取引データセットの垂直および水平に分割されたデータに特化して開発された連合学習アルゴリズムである
- 差分プライバシーと安全なマルチパーティ計算を戦略的に使用し、トレーニングデータのプライバシーを保証する
- トレーニングアルゴリズムのエンドツーエンドのプライバシーに関する理論的分析を提供
- 実験結果は、プライバシーが増加しても高いモデル精度を維持し、ベンチマーク結果を一貫して上回ることを示している

連合学習を使って、今まで以上にプライバシーを守りながら金融犯罪を防止できるなんてすごくない？プライバシーと精度の両立が期待できて未来が楽しみ！



**トピック:** [連合学習](fl), [差分プライバシー](dp), [秘密計算](mpc), **カテゴリ:** cs.CE, **投稿日時:** 2024-08-03 00:07

- - -

### [THOR2: Leveraging Topological Soft Clustering of Color Space for Human-Inspired Object Recognition in Unseen Environments](http://arxiv.org/abs/2408.01579)

**THOR2: 見知らぬ環境での人間のような物体認識のための色空間の位相ソフトクラスタリングの活用**

Ekta U. Samani, Ashis G. Banerjee

- 未知の乱雑な屋内環境での視覚的物体認識はモバイルロボットにとって困難
- 3D形状と色ベースの記述子TOPS2を用い、RGB-Dイメージから生成されるポイントクラウドを識別
- トポロジーソフトクラスタリング手法「Mapperアルゴリズム」を用い人間の色知覚に類似した色領域を分類
- 合成データで訓練したTHOR2は、THORや他の深層学習ネットワークよりも高い認識精度を実現

ベンチマークデータセットでこれだけ高性能が証明されてるのってすごくない？ 安価なロボットでの実用化、めちゃくちゃ楽しみだよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-02 21:24

- - -

### [Accelerating Domain-Aware Electron Microscopy Analysis Using Deep Learning Models with Synthetic Data and Image-Wide Confidence Scoring](http://arxiv.org/abs/2408.01558)

**合成データと画像全体の信頼スコアを用いたドメイン認識型高速電子顕微鏡解析のためのディープラーニングモデル**

Matthew J. Lynch, Ryan Jacobs, Gabriella Bruno, Priyam Patki, Dane Morgan, Kevin G. Field

- 合成画像とデータ生成器を作成し、物理に基づいたデータを提供
- 人間がラベル付けしたデータと同等の精度と予測能力を持つ機械学習モデルを実現
- 特徴予測の信頼スコアを用いて曖昧な画像を排除し、性能を5-30%向上
- 合成データの利用により、人間の依存を排除し多くの特徴検出が求められる場合でもドメイン認識を提供

すごい！合成データでこんなに性能が向上するんだね。人間の手間が減るのもありがたいし、実用性の高い研究だと思う！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cond-mat.mtrl-sci, **投稿日時:** 2024-08-02 20:15

- - -

### [Robot-Enabled Machine Learning-Based Diagnosis of Gastric Cancer Polyps Using Partial Surface Tactile Imaging](http://arxiv.org/abs/2408.01554)

**ロボットを使った触感イメージングによる胃がんポリープの機械学習診断**

Siddhartha Kapuria, Jeff Bonyun, Yash Kulkarni, Naruhiko Ikoma, Sandeep Chinchali, Farshid Alambeigi

- 従来の内視鏡診断の限界を克服するため、視覚ベースの触覚センサー（VTS）を利用
- 腫瘍のテクスチャ特徴を分類するための機械学習アルゴリズムも提案
- 7自由度のロボットとリアルな胃がん腫瘍ファントムを用いてデータ収集の自動化を実演
- 合成データで訓練された機械学習モデルが、従来のモデルと比較し評価結果が良好

新しい触覚センサーで胃がんの診断ってすごく先進的だよね！データ取りの問題も解決できちゃいそうで、未来の医療が変わるかも？！



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.AI, cs.CV, cs.LG, **投稿日時:** 2024-08-02 20:01

- - -

### [NeuralFactors: A Novel Factor Learning Approach to Generative Modeling of Equities](http://arxiv.org/abs/2408.01499)

**NeuralFactors: 株式の生成モデリングに対する新しい因子学習アプローチ**

Achintya Gopal

- ディープ生成モデリングを用いて古典的な因子モデルを強化することを探求
- NeuralFactorsを導入し、ニューラルネットワークが因子のエクスポージャーとリターンを出力
- ログ尤度性能と計算効率の両面で従来アプローチより優れていることを示す
- リスク分析やポートフォリオ最適化でも実用的で、合成データ生成や共分散推定においても競争力を持つ

ディープラーニングで株価予測の精度が上がるなんてスゴイ！ポートフォリオのリスク分析も簡単になるし、未来が楽しみだね。

**Comment:** 9 pages, 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** q-fin.ST, cs.LG, **投稿日時:** 2024-08-02 18:01
