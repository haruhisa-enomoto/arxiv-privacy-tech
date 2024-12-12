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

更新: 2024-12-12T04:25:53.333658

- - -

### [Can We Generate Visual Programs Without Prompting LLMs?](http://arxiv.org/abs/2412.08564)

**大規模言語モデルを用いずに視覚プログラムを生成できるか？**

Michal Shlapentokh-Rothman, Yu-Xiong Wang, Derek Hoiem

- 視覚プログラミングは、視覚的なタスク用のコードを生成するための技術である
- プロンプトに頼る手法は、信頼性が低く、改善が難しく、コストがかかる
- 合成データ拡張とプログラムをテンプレートと引数に分ける方法を開発
- データ拡張により、プロンプトを使わない小さなLLMでも高速で競争力があることが示された

視覚的なタスクを効率的に解決する新しい方法ってすごく未来感あるね！データ拡張で小さくても強いモデルが増えるのかな、楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, **投稿日時:** 2024-12-11 17:32

- - -

### [Protecting Confidentiality, Privacy and Integrity in Collaborative Learning](http://arxiv.org/abs/2412.08534)

**共同学習における機密性、プライバシー、整合性の保護**

Dong Chen, Alice Dethise, Istemi Ekin Akkus, Ivica Rimac, Klaus Satzke, Antti Koskela, Marco Canini, Wei Wang, Ruichuan Chen

- データセットとモデルの所有者は、それぞれの資産の機密性とユーザープライバシーを守りたいが、現行の手法には限界がある
- Citadel++は、データセット、モデル、トレーニングコードの機密性とユーザープライバシーを同時に保護するシステムである
- 差分プライバシー技術を強化し、ユーザーデータのプライバシーを守りつつ、モデルの有用性を維持する
- 実験では、Citadel++が機密性とプライバシー要求を満たし、既存システムを大幅に凌ぐ効率と性能を示す

Citadel++の技術、すごいね！こんなに一気にパフォーマンスとプライバシーを向上させるなんて、革新的な道具になりそう。データの安全性を高めながら、モデルの実用性を維持するって、今後の技術への期待が膨らむね！



**トピック:** [差分プライバシー](dp), [TEE](tee), **カテゴリ:** cs.DC, cs.CR, cs.LG, **投稿日時:** 2024-12-11 16:48

- - -

### [Federated Learning for Traffic Flow Prediction with Synthetic Data Augmentation](http://arxiv.org/abs/2412.08460)

**連合学習を用いた合成データ拡張による交通流予測**

Fermin Orozco, Pedro Porto Buarque de Gusmão, Hongkai Wen, Johan Wahlström, Man Luo

- 交通データのプライバシーと商業的感度が連合学習の採用を促進
- データサイロ間での連携を促し、最適な交通流予測を実現
- 新しいFLフレームワークFedTPSは、拡散ベースのモデルで合成データを生成
- 提案手法FedTPSは複数のFLベースラインを上回る性能を達成

交通情報の連携が進むと、みんなの暮らしがもっと便利になりそう！合成データを活用したアプローチも最先端でワクワクするよね。

**Comment:** 11 pages, 7 figures, 6 tables, ACM format

**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.DC, I.2.1; I.2.11, **投稿日時:** 2024-12-11 15:25

- - -

### [How Does the Smoothness Approximation Method Facilitate Generalization for Federated Adversarial Learning?](http://arxiv.org/abs/2412.08282)

**スムーズネス近似法は連合敵対的学習の一般化をどのように促進するのか？**

Wenjun Ding, Ying An, Lixing Chen, Shichao Kan, Fan Wu, Zhe Qu

- 連合敵対的学習（FAL）は非平滑な損失関数により一般化が難しい
- 一般化誤差を軽減するためにスムーズネス近似を活用する
- RSAは一般化誤差を減らす最も有効な方法と特定
- データの異質性に対処するためにSFALの利用を推奨

スムーズにすることで、敵対的な問題を上手く克服するアイディアが素敵！未来の学習アルゴリズムがもっと賢くなっていくのを想像するとワクワクするね。新しいメトリクスやルールがどんな風に役立つのか楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-11 10:57

- - -

### [Generate Any Scene: Evaluating and Improving Text-to-Vision Generation with Scene Graph Programming](http://arxiv.org/abs/2412.08221)

**任意のシーン生成: シーングラフプログラミングによるテキストからビジョン生成の評価と改善**

Ziqi Gao, Weikai Huang, Jieyu Zhang, Aniruddha Kembhavi, Ranjay Krishna

- シーングラフプログラミングを用いて多様なシーンを生成するフレームワークを提案
- DiT系モデルはUNet系より入力キャプションと整合性高いが、全モデルに改良の余地あり
- 実用例1: 自己改善フレームワークで生成データを用いたモデル性能向上
- 実用例2: プロプライエタリモデルの強みをオープンソースモデルに転移するディスティレーションプロセス

この研究は、自動的に多彩なシーンを生成してテキストからビジョン化するのがおもしろいかも！将来的に、人工的なビジュアルがもっとリアルになって、映画やゲーム作りに役立ちそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-12-11 09:17

- - -

### [Analyzing and Improving Model Collapse in Rectified Flow Models](http://arxiv.org/abs/2412.08175)

**修正フローモデルにおけるモデル崩壊の解析と改善**

Huminhao Zhu, Fangyikang Wang, Tianyu Ding, Qing Qu, Zhihui Zhu

- 自己生成データによる学習反復で、モデル崩壊が発生することがある
- 修正フローモデルのモデル崩壊を、脱ノイズオートエンコーダーの文脈で理論的に分析
- 小さなノイズ分散の再帰生成データで訓練すると生成品質が低下
- 現実のデータを効果的に使用する手法で崩壊を防ぎ、サンプリング効率も向上

モデル崩壊を防ぐために、どうやって現実のデータに再焦点を当てるかが面白そうだね！また、品質向上とプロセスの効率化が両立できるなんてワクワクだよね〜。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-12-11 08:05

- - -

### [A Survey on Private Transformer Inference](http://arxiv.org/abs/2412.08145)

**プライベートトランスフォーマー推論に関する調査**

Yang Li, Xinyu Zhou, Yitong Wang, Liangxin Qian, Jun Zhao

- トランスフォーマーモデルがAIの応用を革新した一方で、MLaaSではプライバシーの懸念が高まる
- プライベートトランスフォーマー推論（PTI）は、MPCや準同型暗号を用いてプライバシー問題に対処
- 最新のPTI技術を分析し、最先端のソリューションの課題と潜在的な改善点も評価
- リソース効率とプライバシー保証を評価するためのガイドラインを提案し、性能とプライバシーの両立を目指す

トランスフォーマーってよく聞くけど、そのプライバシー問題にこういう解決策があると安心だね！技術的にもすごく興味深いし、実際の応用が楽しみだなー。

**Comment:** The manuscript is still being revised and will be continuously   updated in the future

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-12-11 07:05

- - -

### [Learn How to Query from Unlabeled Data Streams in Federated Learning](http://arxiv.org/abs/2412.08138)

**連合学習におけるラベルなしデータストリームからのクエリ習得**

Yuchang Sun, Xinran Li, Tao Lin, Jun Zhang

- 連合学習はプライバシー保護しつつ分散クライアントの共同学習を可能にする
- 現実ではクライアントにはストリーミング形式でラベルなしデータが到着する
- 提案するLeaDQはマルチエージェント強化学習でデータ選択問題を解決
- LeaDQでグローバルモデル精度を向上しベンチマークアルゴリズムを凌駕

ラベルなしデータの扱い、連合学習の課題を解くって面白そう！LeaDQの効果でどこまで精度が向上するのかワクワクするね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-12-11 06:51

- - -

### [Generative Zoo](http://arxiv.org/abs/2412.08101)

**生成的動物園**

Tomasz Niewiadomski, Anastasios Yiannakidis, Hanz Cuevas-Velasquez, Soubhik Sanyal, Michael J. Black, Silvia Zuffi, Peter Kulits

- 3D動物の姿勢と形状をモデル化するために、大量の正確なラベル付き画像データが必要とされる
- 現実世界の画像を手動で2Dアノテーションし3Dパラメータを最適化する手法もあるが、非現実的な場合がある
- ゲームエンジンを用いた合成データ生成も視覚的リアルさに欠け、新しい種や環境に適応するために多くの手作業が必要
- 提案されたコンディショナル画像生成モデルを用いた新たな合成データ生成手法「GenZoo」はリアルな画像を生成

動物の姿勢や形状をリアルに把握できることってすごくクールだよね！GenZooは合成データだけで現実世界のベンチマークを超えるなんて、どんな動物でも研究できちゃう未来が楽しみだな～！

**Comment:** 12 pages; project page: https://genzoo.is.tue.mpg.de

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-12-11 04:57

- - -

### [THUD++: Large-Scale Dynamic Indoor Scene Dataset and Benchmark for Mobile Robots](http://arxiv.org/abs/2412.08096)

**THUD++: モバイルロボット向け大規模動的屋内シーンデータセットとベンチマーク**

Zeshun Li, Fuhao Li, Wanting Zhang, Zijie Zheng, Xueping Liu, Yongjin Liu, Long Zeng

- 静的シーンが主だった既存のモバイルロボット用データセットの限界に着目
- THUD++を提案し、実世界と合成データを組み合わせた13の動的シナリオを提供
- RGB-Dデータセットに90K以上の画像フレームと2D/3D境界ボックス、カメラの位置情報を含む
- Unity3Dベースのシミュレーションで制御された環境でのカスタムシーンとアルゴリズムテストが可能

ロボットの動的環境での課題を解決するためのデータセットが登場って感じかな。大規模な動的シーンがこれからのロボット開発を一気に加速させそう！未来が楽しみだね。

**Comment:** arXiv admin note: substantial text overlap with arXiv:2406.19791

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-12-11 04:37

- - -

### [A Tutorial of Personalized Federated Recommender Systems: Recent Advances and Future Directions](http://arxiv.org/abs/2412.08071)

**個別化連合推薦システムのチュートリアル: 最近の進展と今後の方向性**

Jing Jiang, Chunxu Zhang, Honglei Zhang, Zhiwei Li, Yidong Li, Bo Yang

- パーソナライズは推薦システムの要で、無駄な情報を省き個別サービスを提供する
- Cloud型推薦システムは中心化されたデータ収集が必要で、プライバシーリスクがある
- 連合推薦システム（FedRecSys）はデータをローカルに保持し、モデルパラメータのみを共有する
- 駆動要因、クライアント・サーバーの適応、通信効率、プライバシー保護が重要な研究領域

プライバシーに気をつけつつ、個人化された体験を提供できるシステムの進展ってワクワクするよね！ますます便利になっていきそうで、どんな未来が待っているのか楽しみだな〜。

**Comment:** A technical tutorial will appear at The Web Conference 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, **投稿日時:** 2024-12-11 03:33

- - -

### [Federated In-Context LLM Agent Learning](http://arxiv.org/abs/2412.08054)

**連合インコンテキストLLMエージェント学習**

Panlong Wu, Kangshuo Li, Junbao Nan, Fangxin Wang

- 大規模言語モデル(LLM)は論理推論や道具の利用を可能にしたが、高品質データの希少性が発展を妨げている
- 連合学習(FL)はプライベートデータを保護しつつ分散LLMを協調訓練可能だが、帯域幅や計算負荷が大きい
- FICALアルゴリズムは新しいプライバシー保護手法で、知識集大成を使ってLLMエージェントをFLで訓練
- 実験結果ではFICALが他の最先端ベースラインと比較し、通信コストを3.33×10^5倍削減しつつ競争力ある性能を示す

FICALすごい！どんどん効率よくデータをやりとりできるってことなのかな？これで色んなサービスももっと安全で早くなるといいよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CL, cs.CR, **投稿日時:** 2024-12-11 03:00

- - -

### [dsLassoCov: a federated machine learning approach incorporating covariate control](http://arxiv.org/abs/2412.07991)

**dsLassoCov: 共変量制御を取り入れた連合機械学習アプローチ**

Han Cao, Augusto Anguita, Charline Warembourg, Xavier Escriba-Montagut, Martine Vrijheid, Juan R. Gonzalez, Tim Cadman, Verena Schneider-Lindner, Daniel Durstewitz, Xavier Basagana, Emanuel Schwarz

- 機械学習は生物医学研究で広く採用されているが、異なる機関間のデータ統合は法的制約がある
- 連合学習は地理的に分散したデータセットを用いてプライバシーを守ったモデル訓練を可能にする
- 通常の共変量制御法は高次元データでの通信コストが高く、連合学習には不適
- dsLassoCovは共変量効果を管理し、連合学習で効率的なバイオマーカー選択を実現する

dsLassoCovで、もっと楽で効率的に医学研究が進むってデータ革命じゃん！法律やデータ管理の厄介ごとも、これで解決できちゃうなんてすごい！もっとたくさんの研究にどんどん使ってほしいな〜。

**Comment:** 17 pages, 5 figures

**トピック:** [連合学習](fl), **カテゴリ:** q-bio.QM, cs.LG, **投稿日時:** 2024-12-11 00:03

- - -

### [Mayfly: Private Aggregate Insights from Ephemeral Streams of On-Device User Data](http://arxiv.org/abs/2412.07962)

**Mayfly: デバイス上のユーザーデータの一時的なストリームからプライベートな集計インサイトを得る手法**

Christopher Bian, Albert Cheu, Stanislav Chiknavaryan, Zoe Gong, Marco Gruteser, Oliver Guinan, Yannis Guzman, Peter Kairouz, Artem Lagzdin, Ryan McKenna, Grace Ni, Edo Roth, Maya Spivak, Timon Van Overveldt, Ren Yi

- Mayflyは、端末上のデータを中央に保持せずに集計クエリを可能にする連合分析手法
- 一時的なデータ窓口とSQLプログラムでデータ量を最小化し、ストリーミング差分プライバシーで匿名化
- プライベートな集計のみを即座にメモリにてサーバーで集約し、データアナリストに開示する
- 新たな差分プライバシー機構を設計し、交通炭素排出量の推定で実用化し、他領域にも適用可能

Mayflyって未来を感じるね。データを蓄積しないで分析できるなんて画期的！これがもっと広まったら、プライバシーの心配が少なくなるんじゃないかな？

**Comment:** 22 pages, 7 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DB, H.2.8; K.4.1; H.4, **投稿日時:** 2024-12-10 22:58

- - -

### [MOFHEI: Model Optimizing Framework for Fast and Efficient Homomorphically Encrypted Neural Network Inference](http://arxiv.org/abs/2412.07954)

**MOFHEI: 高速で効率的な準同型暗号ニューラルネットワーク推論のためのモデル最適化フレームワーク**

Parsa Ghazvinian, Robert Podschwadt, Prajwal Panzade, Mohammad H. Rafiei, Daniel Takabi

- 機械学習の幅広い応用とデータプライバシーの必要性から、プライバシー保護機械学習が注目されている。
- 準同型暗号を用いることで暗号化されたデータ上で機械学習を行うが、計算は未だに遅くメモリを多く消費する。
- MOFHEIはHEを用いたニューラルネットワーク推論を高速化し効率化するために、モデルを最適化するフレームワークを提案する。
- LeNetで最大98%のパラメータ削減を達成し、HE操作を最大93%削減、遅延とメモリ消費も大幅に削減。

この研究、面白そうだなーと思うのは、同じパフォーマンスを保ちながら、どれだけ速く効率的にできるのか挑戦するところ！準同型暗号でのニューラルネットって普段あまり聞かない話題だけど、これが実用化されたらすごく未来っぽくない？

**Comment:** 10 pages, 5 Figures, IEEE International Conference on Trust, Privacy   and Security in Intelligent Systems, and Applications 2024

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-10 22:44

- - -

### [Mitigating exponential concentration in covariant quantum kernels for subspace and real-world data](http://arxiv.org/abs/2412.07915)

**共変量量子カーネルにおける指数的濃度の軽減：部分空間および実世界データに対する研究**

Gabriele Agliardi, Giorgio Cortiana, Anton Dekusar, Kumar Ghosh, Naeimeh Mohseni, Corey O'Meara, Víctor Valls, Kavitha Yogaraj, Sergiy Zhuk

- データ内の群構造を活用する共変量フィデリティカーネルは、分類タスクで量子的優位性を示す
- 実世界データにおける群構造の不明瞭さと100量子ビット以上のスケーリングによる指数的濃度が課題
- 新しい誤差緩和戦略「Bit Flip Tolerance (BFT)」を提案し、指数的濃度を抑制
- 156量子ビットまでの実験で、BFT導入時には80％の精度、クラシカルモデルとほぼ同等の成果を達成

量子機械学習の最前線って感じでワクワクするね！特にBFTの効果で、クラシカルと同等の精度が出るなんて、早く実生活で活かされるところを見てみたいな。



**トピック:** [合成データ](sd), **カテゴリ:** quant-ph, cs.LG, **投稿日時:** 2024-12-10 20:53

- - -

### [Evaluating the Potential of Federated Learning for Maize Leaf Disease Prediction](http://arxiv.org/abs/2412.07872)

**トウモロコシ葉病予測における連合学習の可能性を評価**

Thalita Mendonça Antico, Larissa F. Rodrigues Moreira, Rodrigo Moreira

- 作物の病気診断に機械学習を導入するも、データプライバシーに問題がある
- 連合学習（FL）は分散型学習により、集中型の欠点を克服する
- トウモロコシ病にFLを初適用し、5つのCNNを比較評価
- FLは異質な領域でデータプライバシーを強化する可能性が示された

連合学習をトウモロコシ病に応用するなんておもしろいね！データプライバシーを守りながら精度も高められるなら、他の農作物にも広がりそう。未来に期待しちゃうな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-10 19:19

- - -

### [GASP: Gaussian Avatars with Synthetic Priors](http://arxiv.org/abs/2412.07739)

**GASP: 合成事前情報によるガウスアバター**

Jack Saunders, Charlie Hewitt, Yanan Jian, Marek Kowalski, Tadas Baltrusaitis, Yiye Chen, Darren Cosker, Virginia Estellers, Nicholas Gyde, Vinay P. Namboodiri, Benjamin E Lundell

- Gaussian Splattingはリアルタイムのフォトリアリスティックレンダリングに革新をもたらした技術である
- 既存技術は高品位なフリービューアバター生成には高価な多カメラ設備が必要か、固定視点に限定される
- GASPは合成データを用いて個別の写真やビデオから高品質な360度アバターを生成可能にする手法を提案
- アバターは限られたデータから生成され、商用ハードウェアで70fpsでアニメーション化およびレンダリング可能

ここまでリアルなアバターを作れるなんてすごく未来的！手持ちのPCでも簡単に楽しめそうで、これからの利用シーンが楽しみになっちゃうね。

**Comment:** Project page: https://microsoft.github.io/GASP/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.GR, **投稿日時:** 2024-12-10 18:36

- - -

### [Granite Guardian](http://arxiv.org/abs/2412.07724)

**グラニット・ガーディアン**

Inkit Padhi, Manish Nagireddy, Giandomenico Cornacchia, Subhajit Chaudhury, Tejaswini Pedapati, Pierre Dognin, Keerthiram Murugesan, Erik Miehling, Martín Santillán Cooper, Kieran Fraser, Giulio Zizzo, Muhammad Zaid Hameed, Mark Purcell, Michael Desmond, Qian Pan, Inge Vejsbjerg, Elizabeth M. Daly, Michael Hind, Werner Geyer, Ambrish Rawat, Kush R. Varshney, Prasanna Sattigeri

- グラニット・ガーディアンは、多様なリスクの検出を提供する保護モデル群である
- 社会的偏見や不適切発言、暴力、性表現、不倫理、脱獄、幻覚リスクなどをカバー
- 人間による注釈と合成データを組み合わせた独自データセットで訓練されている
- 開かれたソースとして、責任あるAI開発を促進することを目指している

「グラニット・ガーディアン」ってなんか強そうでかっこいい！いろんな問題に対処できるって心強いね。みんなが安心して新しい技術を使えるようになったらいいな～。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-10 18:17

- - -

### [SimVS: Simulating World Inconsistencies for Robust View Synthesis](http://arxiv.org/abs/2412.07696)

**SimVS: 頑健なビュー合成のための世界の不整合のシミュレーション**

Alex Trevithick, Roni Paiss, Philipp Henzler, Dor Verbin, Rundi Wu, Hadi Alzayer, Ruiqi Gao, Ben Poole, Jonathan T. Barron, Aleksander Holynski, Ravi Ramamoorthi, Pratul P. Srinivasan

- 静的シーンの新しいビュー合成技術は、カジュアルなキャプチャ設定中の不整合で苦労する
- 照明の変化やシーンの動きなどの不整合を生成ビデオモデルでシミュレーションする手法を提案
- 既存のマルチビューデータセットと合成データを使用し、不整合を解決するマルチビュー調和ネットワークを構築
- 提案手法は従来の方法を超え、多様な不整合を克服する高精度の3D再構築を実現

この研究って、日常的なキャプチャでも3Dシーンをきれいに再現できるようになりそう！生成ビデオモデルを使ってもっとリアルなシミュレーションに挑むところがワクワクするね。

**Comment:** Project page: https://alextrevithick.github.io/simvs

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.GR, cs.LG, **投稿日時:** 2024-12-10 17:35

- - -

### [Privacy-Preserving Customer Support: A Framework for Secure and Scalable Interactions](http://arxiv.org/abs/2412.07687)

**プライバシーを保護したカスタマーサポート: 安全でスケーラブルなやり取りのためのフレームワーク**

Anant Prakash Awasthi, Chandraketu Singh, Rakshit Varma, Sanchit Sharma

- 従来の機械学習はデータプライバシーのリスクと法規制の課題がある
- PP-ZSLは事前学習済みの大規模言語モデルを使い、センシティブなデータのローカルトレーニングを回避
- フレームワークにはリアルタイムデータ匿名化と、特定ドメインのクエリ解決の手法を組み込む
- 精度を保ちながらコストと複雑性を低減し、様々な業界での活用が期待される

AIが進化すると、裏で活躍するこういうフレームワークが重要になりそうだよね！顧客情報をしっかり守りつつ効率よく対応できるなら、みんな安心して使えそうで嬉しいな。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, stat.AP, **投稿日時:** 2024-12-10 17:20

- - -

### [Bayesian Data Augmentation and Training for Perception DNN in Autonomous Aerial Vehicles](http://arxiv.org/abs/2412.07655)

**自律航空機における認識DNNのためのベイジアンデータ拡張と学習**

Ashik E Rasul, Humaira Tasnim, Hyung-Jin Yoon, Ayoosh Bansal, Duo Wang, Naira Hovakimyan, Lui Sha, Petros Voulgaris

- 自律システムにはDNNが不可欠だが、実用条件との不一致が事故原因になる
- 合成データ生成技術は多様なシナリオを探索できるが、航空機用は不足
- 写実的シミュレーションを活用し、安全着陸の課題に焦点を当てたフレームワークを提案
- ベイジアン最適化によりデータ拡張パラメータを最適化し、認識モデルの成功率を20%以上向上

これって、空飛ぶタクシーがもっと安全になる手助けになるかも！着陸がうまくいくと、利用者も安心だよね。未来の移動が楽しみになっちゃうな〜！

**Comment:** To be published in AIAA SciTech 2025 Forum

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.CV, cs.LG, I.2.9; I.2.10; I.6.3, **投稿日時:** 2024-12-10 16:41

- - -

### [SurvBETA: Ensemble-Based Survival Models Using Beran Estimators and Several Attention Mechanisms](http://arxiv.org/abs/2412.07638)

**SurvBETA: Beran推定量と複数のアテンション機構を用いたアンサンブルベース生存モデル**

Lev V. Utkin, Semen P. Khomets, Vlada A. Efremenko, Andrei V. Konstantinov

- 生存分析の既存アンサンブルモデルに対し、Beran推定量を弱学習器とするSurvBETAを提案
- アテンション機構を用い、条件付き生存関数を距離に基づき統合
- Beran推定量の実装、ブートストラップサンプルの特定、予測統合に3回アテンション機構を適用
- 数値実験で合成データと実データを用い特性を示し、他モデルと比較

タイトルの「SurvBETA」がいかにも強そうな雰囲気を醸し出してるし、このアプローチは生存分析の新しい可能性を感じるよね。しかも実際に使ってみることができるコードも公開されてるなんて、もっと探求してみたくなっちゃう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-10 16:17

- - -

### [Tazza: Shuffling Neural Network Parameters for Secure and Private Federated Learning](http://arxiv.org/abs/2412.07454)

**Tazza: セキュアでプライベートな連合学習のためのニューラルネットワークパラメータのシャッフル**

Kichang Lee, Jaeho Jin, JaeYeon Park, JeongGil Ko

- 連合学習はデータプライバシーを保護するが、勾配逆推定やモデル毒性攻撃に脆い
- 既存の解決策はセキュリティかモデル精度のどちらかを犠牲にすることが多い
- Tazzaは重みシャッフルを活用し、毒性攻撃に対して強化しつつデータ機密性と高精度を実現
- Tazzaは最大6.7倍の計算効率を向上させ、パフォーマンスを損なわない堅牢な防御を達成

「Tazza」って名前がカッコイイ！それに、計算効率が上がったのにパフォーマンスを落とさないのはすごいね！

**Comment:** 14 pages, 14 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, 68T07, I.2.11, **投稿日時:** 2024-12-10 12:20

- - -

### [Causal World Representation in the GPT Model](http://arxiv.org/abs/2412.07446)

**GPTモデルにおける因果的世界表現**

Raanan Y. Rohekar, Yaniv Gurwicz, Sungduk Yu, Vasudev Lal

- GPTモデルは次のトークンを予測するだけでなく、因果的な世界モデルを暗黙的に学習する可能性
- 注意メカニズムの因果解釈から生じる因果的世界モデルを提案
- 推論時に、GPTがゼロショットで因果構造を学習できると示唆
- オセロゲームを使った実験で、ゲームルールに沿った因果構造が高い確信を持って生成されることを確認

この研究って、GPTの内側で何が起こってるのかを垣間見れる感じがめっちゃワクワクするよね！オセロのルールに沿って生成されるってことは、どんな応用ができるのか想像するだけで楽しいね。

**Comment:** NeurIPS 2024 Workshop on Causality and Large Models (CaLM)

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, cs.LG, stat.ML, **投稿日時:** 2024-12-10 12:05

- - -

### [When UAV Meets Federated Learning: Latency Minimization via Joint Trajectory Design and Resource Allocation](http://arxiv.org/abs/2412.07428)

**UAVが連合学習と出会った時: 軌道設計とリソース配分による遅延最小化**

Xuhui Zhang, Wenchao Liu, Jinke Ren, Huijun Xing, Gui Gui, Yanyan Shen, Shuguang Cui

- 連合学習はIoTデバイスに有用だが通信品質が制約となる
- UAVを用いて通信用に強い視通サービスを提供、通信容量を向上
- 帯域幅、計算周波数、送信電力、UAV軌道を最適化し遅延最小化を目指す
- 提案手法は既存のベンチマークより優れた遅延と理想的な訓練効率に近づく

ドローンを使ってIoTデバイスと連携するのは未来的だと思う！軌道を設計して最適化するなんて、まるでSF映画みたいな話だね。どうなるのかワクワクする～！

**Comment:** This manuscript has been submitted to IEEE

**トピック:** [連合学習](fl), **カテゴリ:** eess.SP, cs.LG, **投稿日時:** 2024-12-10 11:39

- - -

### [AppGen: Mobility-aware App Usage Behavior Generation for Mobile Users](http://arxiv.org/abs/2412.07267)

**AppGen: モバイルユーザーの行動パターンを考慮したアプリ使用行動生成**

Zihan Huang, Tong Li, Yong Li

- モバイルアプリの使用行動はコストがかかり、プライバシー問題もあるためデータ収集が困難
- AppGenはユーザーの移動経路に基づきアプリ使用行動を生成し、データセットのアクセスと質を向上
- 確率的拡散モデルと自己回帰構造を使用し、アプリ使用の複雑な順序関係を効果的にキャプチャ
- 実験の結果、先進的な基準を12%以上超え、生成データセットが実際のシナリオやタスクでも高い精度を維持

AppGenでアプリの使われ方が簡単にわかるようになるなんて、すごく便利になりそう！プライバシーを守りながらもデータが使える新しい方法、ワクワクするね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.HC, **投稿日時:** 2024-12-10 07:48

- - -

### [Game-Theoretic Joint Incentive and Cut Layer Selection Mechanism in Split Federated Learning](http://arxiv.org/abs/2412.07813)

**連合学習におけるゲーム理論的インセンティブと階層選択メカニズム**

Joohyung Lee, Jungchan Cho, Wonjun Lee, Mohamed Seif, H. Vincent Poor

- 分割連合学習は連合学習の負担軽減と収束速度向上を目指す
- 分割連合学習のモデル所有者が階層を選び、サーバとクライアント間の負担を調整
- インセンティブによりクライアント参加を促し、データ提供量やエネルギー消費を最適化
- ゲーム理論でクライアントの均衡を証明し、モデル所有者とクライアントの利益を最大化する

分割連合学習って、連合学習と特徴が組み合わさってるっぽいね！ゲーム理論的アプローチが活かされているところが、なんか新しい感じでワクワクしちゃうな。プライバシーと効率性が両立できるのか、これからも注目したいな～。

**Comment:** 10 pages, 8 figures

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.GT, cs.AI, cs.LG, **投稿日時:** 2024-12-10 06:24

- - -

### [Learnable Sparse Customization in Heterogeneous Edge Computing](http://arxiv.org/abs/2412.07216)

**異種エッジコンピューティングにおける学習可能なスパースカスタマイズ**

Jingjing Xue, Sheng Sun, Min Liu, Yuwei Wang, Zhuotao Liu, Jingyuan Wang

- 連合学習はエッジデバイスの多様性や非IIDデータの統計的不均一性に直面
- 提案手法FedLPSは、重要度に基づくパターンで異種スパースモデルを学習可能
- FedLPSは非IID環境下で個別データ特性を正確に抽出するスパース化を実現
- 連合学習の精度を向上させつつ実行時間を68.80%以上短縮する実験結果が得られた

エッジデバイスの多様性に対応する新しい手法なんてすごく興味深いかも！リアルタイムでの適応ができるって、未来のエッジコンピューティングの可能性を広げそうだね。

**Comment:** There are some things to modify so we decided to withdraw first

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-12-10 06:14

- - -

### [Hierarchical Split Federated Learning: Convergence Analysis and System Optimization](http://arxiv.org/abs/2412.07197)

**階層的分割連合学習: 収束解析とシステム最適化**

Zheng Lin, Wei Wei, Zhe Chen, Chan-Tong Lam, Xianhao Chen, Yue Gao, Jun Luo

- AIモデルの大規模化により、リソース制約のあるエッジデバイスでの連合学習が困難
- モデル分割による負荷軽減を目指し、分割連合学習（SFL）が注目されている
- 階層的SFL（HSFL）フレームワークとその収束境界を提案し、理論を基に性能を最適化
- モデル分割と集約の最適化問題を分解し、反復降下アルゴリズムで効率的に解決

これ、すごく新しいアイデアじゃない？階層的なアプローチで、どんなシステムでも最適化できるのが魅力的だよね。未来の連合学習がもっと広がりそう！

**Comment:** 15 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, cs.NI, **投稿日時:** 2024-12-10 05:20

- - -

### [A New Federated Learning Framework Against Gradient Inversion Attacks](http://arxiv.org/abs/2412.07187)

**新しい連合学習フレームワークでの勾配反転攻撃への対抗策**

Pengxin Guo, Shuang Zeng, Wenhao Chen, Xiaodan Zhang, Weihong Ren, Yuyin Zhou, Liangqiong Qu

- 連合学習はデータプライバシーを守るが、勾配反転攻撃に弱点がある
- 秘密計算や準同型暗号、差分プライバシーが対策として使われるが、プライバシーと有用性のトレードオフが課題
- 提案するHyperFLはハイパーネットワークを利用し、共有パラメータとプライベートデータの直接的な関係を断つ
- 理論解析と実験結果から、HyperFLのプライバシー保護能力とパフォーマンスの高さが示されている

新しい視点から問題を捉えて、ハイパーネットワークを活用したアプローチって面白そう！データの安全性を守りつつ性能も維持できるなんて、未来を考えるとワクワクするね。リンクのGitHubも覗いてみたい！

**Comment:** Accepted at AAAI 2025

**トピック:** [連合学習](fl), [差分プライバシー](dp), [準同型暗号](he), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-10 04:53

- - -

### [Rate-In: Information-Driven Adaptive Dropout Rates for Improved Inference-Time Uncertainty Estimation](http://arxiv.org/abs/2412.07169)

**Rate-In: 改善された推論時不確かさ推定のための情報駆動型適応ドロップアウト率**

Tal Zeevi, Ravid Shwartz-Ziv, Yann LeCun, Lawrence H. Staib, John A. Onofrey

- 推論時の静的なドロップアウト率は最適でない不確かさ推定を招く
- Rate-Inは推論中の情報損失に基づきドロップアウト率を動的に調整
- Ground truthラベルなしで各層と入力ごとにドロップアウト率を適応
- 合成データおよび医療画像タスクでの研究で校正改善と不確かさ推定の精緻化を実証

AIがリアルタイムで最適な推論をするなんて、未来を感じちゃうね！医療診断で超役立ちそうだし、今後の活躍が楽しみ💡

**Comment:** Updated author affiliation

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, stat.ML, **投稿日時:** 2024-12-10 04:03

- - -

### [Streaming Private Continual Counting via Binning](http://arxiv.org/abs/2412.07093)

**ビニングによるストリーミングでのプライベート連続カウント**

Joel Daniel Andersson, Rasmus Pagh

- 連続的な観察はデータセットが逐次公開される状況での問題を指し、差分プライバシーを維持しつつ良好な近似を提供するのが課題である
- 継続的なカウントではバイナリ入力要素の合計を近似することを目指し、これは差分プライベート確率的勾配降下法の実装で重要
- ビニングを用いて行列乗算をサブリニア空間で維持し、低空間での因子化メカニズムの近似を実現する新手法を提案
- 動的状況に対応した因子化メカニズムと比べても非常に低空間でも高性能を維持、類似方法との比較で柔軟性に優れている

このアプローチ、新しい手法でリソース節約しつつ精度を高められるのがいいよね！連続観察って、未来のプライバシー技術にどう影響をもたらすか興味津々だなぁ。私たちの未来がもっと安全に守られるといいね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DS, **投稿日時:** 2024-12-10 01:21

- - -

### [Enhancing radioisotope identification in gamma spectra with transfer learning](http://arxiv.org/abs/2412.07069)

**転移学習によるガンマスペクトルにおける放射性同位体識別の強化**

Peter Lalor

- ガンマ分光法での機械学習は、未知の放射性サンプルをリアルタイムで分類可能
- 実験データは収集が高コストで難しく、合成データだけでは一般化が困難
- 合成データで事前学習しターゲット領域で微調整、物理原理を組み込みデータ要件を軽減
- 複数のMLアーキテクチャで微調整モデルが優れた性能を示し、データ制約ある場合に有効性を確認

現実に即したデータが少ない時でもうまく学習できちゃうなんてすごくない？このアプローチがいろんな分野に応用できたら夢が広がるよね。学習がどんどん便利になってくれて嬉しいな〜！

**Comment:** 11 pages and 4 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, nucl-th, **投稿日時:** 2024-12-10 00:21

- - -

### [Optimizing Personalized Federated Learning through Adaptive Layer-Wise Learning](http://arxiv.org/abs/2412.07062)

**適応層別学習によるパーソナライズ連合学習の最適化**

Weihang Chen, Jie Ren, Zhiqiang Li, Ling Gao, Zheng Wang

- 連合学習は非IIDデータで性能低下、パーソナライズにより改善を図る
- FLAYERは層ごとの学習方法で個別モデル最適化を追求
- 必要に応じてグローバル情報を取り入れつつ、レイヤーごとに学習率を調整
- FLAYERは既存手法と比べ平均5.42%精度改善、最大14.29%向上

このFLAYERっていう方法、ニューラルネットワークの層の学習能力をうまく活用してるんだね！これだけの改善ができるんだったら、他の分野でも使われるかも！やっぱりAIの進化ってすごいなー。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-10 00:10

- - -

### [Data Augmentation with Variational Autoencoder for Imbalanced Dataset](http://arxiv.org/abs/2412.07039)

**変動オートエンコーダを用いた不均衡データセットのデータ拡張**

Samuel Stocksieker, Denys Pommeret, Arthur Charpentier

- 不均衡な分布からの学習は予測モデルの性能低下を引き起こす
- 分類問題に焦点を当てたアプローチが多く、回帰問題は限られている
- 不均衡回帰の課題を解決するために変動オートエンコーダを提案
- VAEと平滑化ブートストラップを組み合わせて、効果を数値的に調査

不均衡なデータセットでも、VAEを使えばバランスよく学習が進むかもしれないよね。新しい方法だから、どんな結果が出るのかワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-09 22:59

- - -

### [FM2DS: Few-Shot Multimodal Multihop Data Synthesis with Knowledge Distillation for Question Answering](http://arxiv.org/abs/2412.07030)

**FM2DS: 質問応答のための知識蒸留を用いた少量データでのマルチモーダルマルチホップデータ合成**

Amirhossein Abaskohi, Spandana Gella, Giuseppe Carenini, Issam H. Laradji

- マルチモーダルマルチホップ質問応答は、画像やテキストなど複数の情報源を用いて推論が必要
- 現在の手法はシングルモーダルで単一ホップに集中し、現実的なシナリオには適さない
- 本研究は高品質なデータセット作成のための初のフレームワークを提案、Wikipediaから資料取得
- 合成データでのモデル訓練が人間収集データよりも1.9ポイント優れた性能を示す

少ないデータで正確に学習できるなんてすごいね！マルチモーダルで科学的研究を解釈できるようになると、もっと面白い発見ができそうじゃん！

**Comment:** 20 pages, 11 figures, 10 tables, Submitted to CVPR 2025

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.CV, cs.IR, cs.LG, **投稿日時:** 2024-12-09 22:35

- - -

### [Sequential Compression Layers for Efficient Federated Learning in Foundational Models](http://arxiv.org/abs/2412.07021)

**基盤モデルにおける効率的な連合学習のための逐次圧縮層**

Navyansh Mahla, Sunny Gupta, Amit Sethi

- 連合学習が人気上昇、各ノードがプライベートデータ持つLLMの微調整に使用
- LoRAは採用されるも連合学習では性能が不十分とされる
- LoRAに頼らず効果的な新しいパラメータ効率の良い微調整法を提案
- 提案手法はLLMとビジョンエンコーダの性能向上を実証した

新しいアプローチがどんな技術なのかすごく気になるね！これで連合学習がもっと賢くなって、効率がどんどん良くなっていくといいなー！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-09 22:06

- - -

### [Variable Selection for Comparing High-dimensional Time-Series Data](http://arxiv.org/abs/2412.06870)

**高次元時系列データを比較するための変数選択**

Kensuke Mitsuzawa, Margherita Grossi, Stefano Bortoli, Motonobu Kanagawa

- マルチ変量時系列データの特定の変数と時間間隔を選択する方法を提案
- コンピュータシミュレータと実データを比較し、正当性を検証可能
- 提案手法は時系列を複数の部分に分け、変数の選択と二標本検定を行う
- 合成データ実験で検証され、粒子流体シミュレータと交通シミュレータでの有用性を実証

高次元データを効率的に扱うこの手法って、シミュレーションの精度を高めるのに役立ちそう！複雑なデータでも新たな視点で比較できるのが面白そうだね。



**トピック:** [合成データ](sd), **カテゴリ:** stat.ME, cs.LG, stat.ML, **投稿日時:** 2024-12-09 12:08
