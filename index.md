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

更新: 2024-12-08T04:22:09.182546

- - -

### [DualPM: Dual Posed-Canonical Point Maps for 3D Shape and Pose Reconstruction](http://arxiv.org/abs/2412.04464)

**DualPM: 3D形状と姿勢再構成のための二重姿勢・標準点マップ**

Ben Kaye, Tomas Jakab, Shangzhe Wu, Christian Rupprecht, Andrea Vedaldi

- データ表現の選択は幾何学的タスクの成功に影響する
- DualPMを導入し、変形可能な物体の3D形状と姿勢再構成に新たな手法を提供
- ピクセルを3D位置と静止状態の標準形に対応づける二重の点マップを用いる
- 合成データで訓練したDualPMは実画像上でも一般化し、従来法を大幅に改善

3D形状再構成のための新しい手法がリアルな応用に生かされるのってワクワクするよね！これでますますCGがリアルになって、未来の映画やゲームももっと面白くなりそうだよね。

**Comment:** First two authors contributed equally. Project page:   https://dualpm.github.io

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-05 18:59

- - -

### [Monocular Dynamic Gaussian Splatting is Fast and Brittle but Smooth Motion Helps](http://arxiv.org/abs/2412.04457)

**単眼動的ガウススプラッティングは高速で脆いがスムーズな動きが助けになる**

Yiqing Liang, Mikhail Okunev, Mikaela Angelina Uy, Runfeng Li, Leonidas Guibas, James Tompkin, Adam W. Harley

- 単眼入力データを用いた動的シーンのビュー合成は、困難な課題である
- ガウススプラッティング手法を比較し、これまで不足していた厳密な評価を提供
- 合成データセットで手法の違いを評価すると、現実データでは違いが不明瞭
- 全手法は高速レンダリングだが、最適化の脆さが課題であると結論付け

ガウススプラッティングって一体何？って思ったけど、どうやら動かすのがめっちゃ速くなるっぽい！でも最適化にくじけやすいみたいだから、これからそこがもっと強くなるかも？がんばれ〜って応援したくなっちゃうね！

**Comment:** 37 pages, 39 figures, 9 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-05 18:59

- - -

### [FedDUAL: A Dual-Strategy with Adaptive Loss and Dynamic Aggregation for Mitigating Data Heterogeneity in Federated Learning](http://arxiv.org/abs/2412.04416)

**FedDUAL: 連合学習におけるデータ異質性を緩和する適応的損失と動的集約による二重戦略**

Pranab Sahoo, Ashutosh Tripathi, Sriparna Saha, Samrat Mondal

- 連合学習はデータの中央集約を避けつつモデルを統一するが、データの不均一性により性能が劣化しがちである
- 特にラベルの偏りによる問題が深刻で、画像分類領域で顕著である
- 提案手法はクライアント側で適応型損失を採用し、ローカルとグローバル最適化のバランスを取る
- 動的集約戦略でクライアントの学習パターンに適応し、データの多様性の問題を解決する

なんかさ、データがバラバラでもちゃんと学べちゃうなんて面白そうじゃない？どんな場面で使えるのか想像するとワクワクしてくるね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CV, cs.DC, **投稿日時:** 2024-12-05 18:42

- - -

### [Providing Differential Privacy for Federated Learning Over Wireless: A Cross-layer Framework](http://arxiv.org/abs/2412.04408)

**無線通信における連合学習への差分プライバシー提供：クロスレイヤーフレームワーク**

Jiayu Mao, Tongxin Yin, Aylin Yener, Mingyan Liu

- 無線エッジネットワーク向けのOTA-FLは自然な重ね合わせ特性を活用しプライバシーを強化
- 分散型動的電力制御と協力的ジャマーにより無線PHY層で差分プライバシーを改善
- クライアント側の人工ノイズ注入不要、伝送効率を保ちつつ高レベルのプライバシーを実現
- FEMNISTデータセットでの数値結果が最先端手法を上回るプライバシーと精度の達成

ワイヤレスで差分プライバシーを改善するって未来感あるよね！協力的ジャマーでプライバシーを守るアイディアも面白い！うまくいけば伝送効率もプライバシーも両立できるかも？

**Comment:** submitted for an IEEE publication

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.IT, cs.LG, math.IT, **投稿日時:** 2024-12-05 18:27

- - -

### [Federated Automated Feature Engineering](http://arxiv.org/abs/2412.04404)

**連合学習における自動特徴エンジニアリング**

Tom Overman, Diego Klabjan

- 自動特徴エンジニアリング (AutoFE) は、人間の介入なしに新しい特徴を自動生成する手法
- 連合学習においてデータを共有しないままAutoFEを実現するアルゴリズムが乏しい
- 提案するAutoFEアルゴリズムは水平、垂直、ハイブリッド型FLに対応している
- 連合学習におけるAutoFEのモデル性能はデータが中央にある場合と同等である

この研究、すごく面白そう！データを共有せずに新しい特徴を自動生成できるなんて、プライバシーにも優しくて最高だね。これからもっと注目されそうな技術だなぁ。

**Comment:** Preliminary Work

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-12-05 18:23

- - -

### [BhashaVerse : Translation Ecosystem for Indian Subcontinent Languages](http://arxiv.org/abs/2412.04351)

**BhashaVerse: インド亜大陸言語の翻訳エコシステム**

Vandan Mujadia, Dipti Misra Sharma

- 36のインド言語における36 * 36のすべての言語ペアに必要なパラレルコーパスを開発
- スクリプトの差異、音声的な違い、構文の多様性といった課題を解決する方法を提案
- 低リソースの言語には合成データを用いてカバレッジと品質を保証する方法を提案
- 機械翻訳の評価を多次元で行い、包括的な翻訳品質向上のフレームワークを確立

多言語を扱うってめっちゃ大変そうだけど、それを一気に解決しようとしてるのがすごい！これがうまくいけば、インドのいろんな地域の人ともっと簡単にコミュニケーションが取れる未来が来るのかもってワクワクするね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-12-05 17:10

- - -

### [ALMA: Alignment with Minimal Annotation](http://arxiv.org/abs/2412.04305)

**ALMA: 最小限のアノテーションによる整合**

Michihiro Yasunaga, Leonid Shamis, Chunting Zhou, Andrew Cohen, Jason Weston, Luke Zettlemoyer, Marjan Ghazvininejad

- ALMAは9,000のラベル例で効果的な整合を実現できることを示す
- 合成データ生成に多様なプロンプト合成技術と報酬モデルの強化を活用
- Llama3ベースモデルと少数の例のみで高い整合性能を達成
- 10回の自己ブートストラップで以前の方法の限界を超える結果を得る

少量のデータでここまで高い整合性を保てるってすごいね！このアプローチがもっと普及すれば、コストも減らせて効率的にAIをトレーニングできそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-12-05 16:26

- - -

### [Methodology for Online Estimation of Rheological Parameters in Polymer Melts Using Deep Learning and Microfluidics](http://arxiv.org/abs/2412.04142)

**深層学習とマイクロ流体技術を用いたポリマー融解のレオロジー特性オンライン推定法**

Juan Sandubete-López, José L. Risco-Martín, Alexander H. McMillan, Eva Besada-Portas

- マイクロ流体デバイスは精度やサイズ、コストの課題を抱える
- 深層学習とモデリング、シミュレーションを統合した手法を開発
- 合成データで学習したモデルがマイクロ流路でレオロジー特性を推定
- この手法で設計とテストが迅速化し、物理プロトタイプに依存せず貢献

レオロジーなんて難しそうって思ったけど、深層学習でこんなこともできちゃうんだ！合成データを使って迅速に実験できるのってすごく効率的だね～。

**Comment:** 12 pages, 6 figures, Winter Simulation Conference 2024

**トピック:** [合成データ](sd), **カテゴリ:** physics.flu-dyn, cs.AI, **投稿日時:** 2024-12-05 13:11

- - -

### [Federated Learning in Mobile Networks: A Comprehensive Case Study on Traffic Forecasting](http://arxiv.org/abs/2412.04081)

**モバイルネットワークにおける連合学習：交通予測に関する包括的ケーススタディ**

Nikolaos Pavlidis, Vasileios Perifanis, Selim F. Yilmaz, Francesc Wilhelmi, Marco Miozzo, Pavlos S. Efraimidis, Remous-Aris Koutsiamanis, Pavol Mulinka, Paolo Dini

- モバイルネットワークのリソース配分の効率化のためにリアルタイム交通予測が重要である
- 連合学習は分散型かつプライバシーを重視したソリューションとして有望である
- バルセロナの基地局データを用い、連合学習のモデル集約法や外れ値管理を検討
- 研究は予測精度と持続可能性を評価しプライバシーと環境への配慮があることを示す

連合学習が環境にも優しいなんて意外で面白いよね！モバイルネットワークでの応用が期待されるし、今後の交通管理がどう進化するか楽しみだなってワクワクするね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-05 11:32

- - -

### [BEFL: Balancing Energy Consumption in Federated Learning for Mobile Edge IoT](http://arxiv.org/abs/2412.03950)

**BEFL: モバイルエッジIoTにおける連合学習のエネルギー消費のバランス化**

Zehao Ju, Tongquan Wei, Fuke Shen

- モバイルエッジIoTでは、学習と通信がデバイスのバッテリーを消耗しやすい
- 既存研究は消費エネルギーの削減に焦点をあてるが、エネルギー不均衡を招くこともある
- 提案するBEFLはモデル精度向上とエネルギー消費の最小化、エネルギー使用のばらつきの抑制を目的とする
- BEFLは既存手法と比較し、精度を1.6%、エネルギー消費のばらつきを72.7%減、全体消費を28.2%低下させる

モバイルエッジデバイスでエネルギー消費を管理しつつ学習を進めるのって、賢いアプローチだよね！連合学習をさらに進化させることで、未来のIoTデバイスがもっと使いやすくなる予感がするなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-12-05 07:58

- - -

### [Learning Speed-Adaptive Walking Agent Using Imitation Learning with Physics-Informed Simulation](http://arxiv.org/abs/2412.03949)

**模倣学習と物理シミュレーションを用いた速度適応型歩行エージェントの学習**

Yi-Hung Chiu, Ung Hee Lee, Changseob Song, Manaen Hu, Inseung Kang

- 人間の歩行をデジタル化したバーチャルモデルは、データ収集なしで機動性を研究できる
- 課題には現実とのズレや多様な歩行条件への適応力不足がある
- 生体力学的に現実的な歩行を保ちながら、速度変動に適応する枠組みを開発し検証
- 提案するエージェントは、速度変化に対し5.24度の誤差で実データに近づき適応力を示した

歩行エージェントがどんな速度でもリアルに動けたら、リハビリとかに使えるかも！本当に面白いことができそうでワクワクするよね。

**Comment:** Currently under review

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.LG, **投稿日時:** 2024-12-05 07:55

- - -

### [Privacy-Preserving in Medical Image Analysis: A Review of Methods and Applications](http://arxiv.org/abs/2412.03924)

**医療画像解析におけるプライバシー保護技術: 手法と応用のレビュー**

Yanming Zhu, Xuefei Yin, Alan Wee-Chung Liew, Hui Tian

- AIによる医療画像の解析は診断精度を向上させるが、プライバシーの課題がある
- 暗号化や差分プライバシーなどの技術を用いてプライバシー保護が図られている
- 医療画像解析の課題と対応する解法を整理し、現場での応用に役立てる
- ゼロ知識証明や安全な多者計算などの新たなトレンドを研究

医療画像解析のプライバシー問題を解決するのってすごく重要だよね。未来の研究が進んで安心して医療を受けられる環境になるといいなって思う！



**トピック:** [連合学習](fl), [差分プライバシー](dp), [準同型暗号](he), [ゼロ知識証明](zkp), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-05 06:56

- - -

### [GP-FL: Model-Based Hessian Estimation for Second-Order Over-the-Air Federated Learning](http://arxiv.org/abs/2412.03867)

**GP-FL: モデルベースのヘッセ行列推定を用いた航空通信連合学習の二次手法**

Shayan Mohajer Hamidi, Ali Bereyhi, Saba Asaad, H. Vincent Poor

- 二次法は学習アルゴリズムの収束率を向上させるために採用される
- 連合学習ではローカルなヘッセ行列共有が通信コストとして障壁となる
- 提案されたGP-FLはガウス過程を用いてノイズまじりの勾配からヘッセ行列を推定
- GP-FLは既存の一・二次オーダー手法を上回る性能を示し、線形-二次収束率を持つ

この研究、めっちゃ面白そう！無線環境でも効率よく学習できるって、これすごく画期的だと思う。データがノイズまみれでもいい感じに推定できるなんて未来っぽいし、連合学習の幅がぐっと広がりそうだよね！

**Comment:** The paper is submitted to IEEE Transactions on Signal Processing

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-05 04:27

- - -

### [FedMetaMed: Federated Meta-Learning for Personalized Medication in Distributed Healthcare Systems](http://arxiv.org/abs/2412.03851)

**FedMetaMed: 分散型医療システムにおける個別化薬物療法のための連合型メタラーニング**

Jiechao Gao, Yuangang Li

- 個別化薬物療法は患者特性に応じた医療提供を目指すが、データの多様性が障壁となる
- 連合学習はプライバシーを守りながら分散型データのモデル訓練を行うが、モデル性能低下の課題あり
- FedMetaMedは連合学習とメタラーニングを組み合わせ、多様な患者データに適応するモデルを構築
- 累積フーリエ集約と協調的転送最適化を導入し、効果的なグローバル知識の集約と個別化モデルの向上を図る

FedMetaMed、すごくおもしろそうだね！データの多様性に対応しつつ、プライバシーも守れるなんて未来の医療にぴったり。これがうまくいけば、個別化医療がもっと身近になっちゃうかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, **投稿日時:** 2024-12-05 03:36

- - -

### [CCxTrust: Confidential Computing Platform Based on TEE and TPM Collaborative Trust](http://arxiv.org/abs/2412.03842)

**CCxTrust: TEEとTPM協調による信頼のための秘密計算プラットフォーム**

Ketong Shang, Jiangnan Lin, Yu Qin, Muyan Shen, Hongzhan Ma, Wei Feng, Dengguo Feng

- 多くのクラウド環境で、単一のハードウェアの信頼の根への依存がユーザーの信頼を制限
- CCxTrustを提案し、TEEとTPMの協力による信頼フレームワークを構築
- 様々な信頼の根（RTM、RTR、RTS）の組み合わせでセキュリティを向上
- プロトタイプにより、アテステーション効率24%改善し、通常TPMと比較して16.47%性能低下

この論文の提案するCCxTrustってめっちゃいい感じ！複数のハードウェアの信頼を組み合わせて使うのはスマートだよね。これでプライバシーがもっと守られる世の中になる予感がする！

**Comment:** 23 pages, 14 figures

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, D.4.6; F.4.3, **投稿日時:** 2024-12-05 03:12

- - -

### [Diffusion in Zero-Shot Learning for Environmental Audio](http://arxiv.org/abs/2412.03771)

**環境音響向けゼロショット学習における拡散法**

Ysobel Sims, Stephan Chalup, Alexandre Mendes

- ゼロショット学習は未見クラスへの一般化を可能にするが、環境音響分野での研究は未熟で性能が低い
- コンピュータビジョンで成功した生成モデル、CADA-VAEとLisGANを適用し、クラス補助データに条件付けされた新しい拡散モデルを導入
- この拡散モデルは未見クラスの合成データを生成し、既知クラスのデータと組み合わせて分類器を訓練する
- 環境音データセットでの実験で、拡散モデルが既存の方法を25%以上上回る精度を達成

環境音のゼロショット学習って面白そう！拡散モデル使うことで、これまで難しかった未見クラスの識別がサクサク進むようになりそうだね。未来の音の研究に繋がりそうな予感！

**Comment:** This work has been submitted to the IEEE for possible publication

**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.LG, eess.AS, **投稿日時:** 2024-12-04 23:18

- - -

### [End to End Collaborative Synthetic Data Generation](http://arxiv.org/abs/2412.03766)

**エンドツーエンドの協調合成データ生成**

Sikha Pentyala, Geetha Sitaraman, Trae Claar, Martine De Cock

- AIの成功はデータの入手可能性に依存しているが、単一の保有者で十分なデータを持つことはまれ
- 現行の連合合成データ生成アルゴリズムは、プライバシーを考慮したデータ共有を目指す
- 既存技術は合成器の訓練に集中し、前処理済みデータを前提とするが、新たなフレームワークを提案
- 提案フレームワークで秘密計算プロトコルを実装し、白血病の合成ゲノムデータで評価

合成データの共有におけるプライバシーを重視しつつ、エンドツーエンドの形で解決する技術って面白いね！秘密計算を使って、協力をしながらデータを守れるって未来的でワクワクするね。



**トピック:** [合成データ](sd), [秘密計算](mpc), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-12-04 23:10

- - -

### [Beyond Local Sharpness: Communication-Efficient Global Sharpness-aware Minimization for Federated Learning](http://arxiv.org/abs/2412.03752)

**局所的鋭さを超えて: 連合学習のための通信効率の良いグローバル鋭さ認識最小化**

Debora Caldarola, Pietro Cagnasso, Barbara Caputo, Marco Ciccone

- データの異質性により連合学習では鋭い最小値に収束しがちで、汎化性能に悪影響
- 従来の手法はクライアント側での鋭さ最小化を利用するが、局所的で効果が限られる
- 本研究はFedGloSSを提案し、サーバー側でのグローバル鋭さ最適化を重視
- 評価結果によるとFedGloSSはより平坦な最小値と高い性能を達成

新しい手法でFL環境下での性能が上がるの、本当にすごいね〜！データの多様性に対応できると、さらに未来が広がりそう。

**Comment:** Preprint, 26 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, **投稿日時:** 2024-12-04 22:46

- - -

### [Evaluating Language Models as Synthetic Data Generators](http://arxiv.org/abs/2412.03679)

**言語モデルの合成データ生成能力の評価**

Seungone Kim, Juyoung Suk, Xiang Yue, Vijay Viswanathan, Seongyun Lee, Yizhong Wang, Kiril Gashteovski, Carolin Lawrence, Sean Welleck, Graham Neubig

- 合成データが重要視され、言語モデルのデータ生成能力が直接解決能力と同等に重要視されている
- 既存の研究では効果的なデータ生成方法の開発に注力しているが、統一された設定での比較は不足している
- AgoraBenchというベンチマークを提案し、LMのデータ生成能力を標準化された設定と指標で評価
- データ生成能力は問題解決能力と必ずしも相関せず、品質などの特徴が指標となる

言語モデルのデータ生成の奥深い側面が探れるのが超面白そう！しかも、戦略次第で生成の効果が全然変わるなんて、未来の技術が広がっていく予感がするね。

**Comment:** Work in Progress

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-04 19:20

- - -

### [MIDI: Multi-Instance Diffusion for Single Image to 3D Scene Generation](http://arxiv.org/abs/2412.03558)

**MIDI: 単一画像からの3Dシーン生成のための多インスタンス拡散**

Zehuan Huang, Yuan-Chen Guo, Xingqiao An, Yunhan Yang, Yangguang Li, Zi-Xin Zou, Ding Liang, Xihui Liu, Yan-Pei Cao, Lu Sheng

- MIDIは新しい多インスタンス拡散モデルにより、単一画像から3Dシーンを生成する手法を提案
- 特徴的なマルチインスタンス注意メカニズムを用いて、オブジェクト間の相互作用と空間的整合性を効果的に捉える
- 部分的なオブジェクト画像とグローバルなシーンコンテキストを使用し、3D生成中のオブジェクト完成を直接モデリング
- シーンレベルデータと単一オブジェクトデータを組み合わせ、学習時に効果的な監督を行いつつ既存の一般化能力を保持

タイトルから新しいアイデアが感じられる！3Dシーン生成に革命を起こしそうな予感がするね。一枚の画像からこんなクールな世界が広がるなんて、まるで未来の技術を先取りしてるみたいでワクワクするよ！

**Comment:** Project page: https://huanngzh.github.io/MIDI-Page/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-04 18:52

- - -

### [Teaching an Old Dog New Tricks: Verifiable FHE Using Commodity Hardware](http://arxiv.org/abs/2412.03550)

**古い技術に新しいトリックを教える：商用ハードウェアを用いた検証可能な準同型暗号**

Jules Drean, Fisher Jepsen, Edward Suh, Srini Devadas, Aamer Jaleel, Gururaj Saileshwar

- Argosは信頼できるハードウェアを用いて、準同型暗号に検証可能性を追加する手法を提案
- 秘密をCPUやメモリ階層から排除することで、マイクロアーキテクチャのサイドチャネル攻撃を完全に回避
- ハードウェアの拡張が必要なく、2008年以降の商用プロセッサで利用可能
- プロトタイプ実装でFHE評価に6%のオーバーヘッド、複雑なプロトコルでも8%のオーバーヘッド

Argosがあれば、高度な暗号技術を実用化に近づけるんじゃないかな。これでプライバシー技術ももっと身近になるといいね！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-04 18:47

- - -

### [Adaptive Personalized Over-the-Air Federated Learning with Reflecting Intelligent Surfaces](http://arxiv.org/abs/2412.03514)

**適応的なパーソナライズオーバー・ジ・エア連合学習の反射インテリジェントサーフェイス利用**

Jiayu Mao, Aylin Yener

- OTA-FLは通信とモデル集約を統一し、同時伝送で効率的な学習を可能にする
- ユーザー資源やデータセット分布が異なるエッジユーザーによるネットワークを強化
- 可調整なインテリジェントサーフェイスを活用し、学習性能を向上するアルゴリズムを提案
- 提案手法は雑音や推定ミスを考慮しつつ、個別学習を実現し、最先端手法より優れている

この研究、まさに次世代の学習って感じでワクワクする！特にRISを取り入れて、速さと正確さを両立できるのはすごく面白そう。これが普及すれば、もっとパーソナライズされた学習が手軽にできそうだね！

**Comment:** submitted for an IEEE publication; Nov 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, eess.SP, math.IT, **投稿日時:** 2024-12-04 17:57

- - -

### [DiffuPT: Class Imbalance Mitigation for Glaucoma Detection via Diffusion Based Generation and Model Pretraining](http://arxiv.org/abs/2412.03629)

**DiffuPT: 拡散ベースの生成とモデル事前訓練による緑内障検出のためのクラス不均衡緩和**

Youssof Nawar, Nouran Soliman, Moustafa Wassel, Mohamed ElHabebe, Noha Adly, Marwan Torki, Ahmed Elmassry, Islam Ahmed

- 緑内障は進行性の視神経障害で、早期発見が視力の喪失防止に重要
- 医療データセットはクラス不均衡が多く、深層学習での検出が難しい
- 拡散モデルと事前訓練を活用し、合成データ生成で分類器の性能向上
- 提案手法により、識別性能指標で改善が見られ、他手法と比較も実施

新しい手法で緑内障検出がかなり進化しそう！視力を守るための技術が進歩するのはすごく心強いね。こんな研究がますます医療に貢献して、多くの人たちに役立てるといいなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, q-bio.QM, **投稿日時:** 2024-12-04 17:39

- - -

### [Reactive Orchestration for Hierarchical Federated Learning Under a Communication Cost Budget](http://arxiv.org/abs/2412.03385)

**通信コスト予算下での階層型連合学習のリアクティブオーケストレーション**

Ivan Čilić, Anna Lackinger, Pantelis Frangoudis, Ivana Podnar Žarko, Alireza Furutanpey, Ilir Murturi, Schahram Dustdar

- 階層型連合学習は、中間集約ノードを使いグローバルサーバーとクライアントをつなぐ必要がある
- コミュニケーションコストとモデル精度のバランスをとるため、適応型オーケストレーションフレームワークを提案
- フレームワークはモデルの精度やリソースの可用性を基に再構成アクションを評価し適応
- Kubernetesの拡張により変化に迅速に対応し、通信コストと性能を効果的にバランス

この研究、未来の連合学習を支える礎になりそう！予算内での工夫のしかたとか、現実世界でも役立ちそうでみんなが興味持ちそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, cs.NI, **投稿日時:** 2024-12-04 15:12

- - -

### [Domain-Agnostic Stroke Lesion Segmentation Using Physics-Constrained Synthetic Data](http://arxiv.org/abs/2412.03318)

**物理制約付き合成データを用いた領域非依存の脳卒中病変セグメンテーション**

Liam Chalcroft, Jenny Crinion, Cathy J. Price, John Ashburner

- MRIにおける脳卒中病変のセグメンテーションは、さまざまな臨床画像ドメインが原因で困難。
- 合成定量的MRI(qMRI)を用いた2つの新規物理制約アプローチを提案。
- qMRI推定モデルをMPRAGE画像から予測し、多様なMRIシーケンスを模擬したセグメンテーション訓練。
- 提案手法はベースラインnnUNetより向上し、第2アプローチは以前の方法を上回る。

この研究、すごく面白そう！物理制約を利用して画像処理の一般化を目指してるなんて、今後どんな応用ができるのか気になるよね！



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, physics.med-ph, **投稿日時:** 2024-12-04 13:52

- - -

### [Semi-decentralized Training of Spatio-Temporal Graph Neural Networks for Traffic Prediction](http://arxiv.org/abs/2412.03188)

**交通予測のための時空間グラフニューラルネットワークの半分散型トレーニング**

Ivan Kralj, Lodovico Giaretta, Gordan Ježić, Ivana Podnar Žarko, Šarūnas Girdzijauskas

- スマートモビリティでの従来の集中型アプローチは拡張性の課題に直面している
- センサをクラウドレットに分け、ローカルモデルの訓練とモデル更新の交換を行う
- 半分散型セットアップは性能指標で集中型に近く、拡張性と障害耐性で優位
- 地域特有の交通パターンの影響や、GNNの大規模受容場から来る通信コストを指摘

これからのスマート交通の新しい形を考える時代が来た感じだね！ほら、車がまるで自分たちで賢く運転してるみたいに、ネットワークも進化してるし、センサとAIの力でどんどん便利になる未来が見えてきたよ！

**Comment:** 8 pages, 4 figures, 3 tables, conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-12-04 10:20

- - -

### [Surveying the Effects of Quality, Diversity, and Complexity in Synthetic Data From Large Language Models](http://arxiv.org/abs/2412.02980)

**大規模言語モデルから生成された合成データの品質、多様性、複雑性の影響に関する調査**

Alex Havrilla, Andrew Dai, Laura O'Mahony, Koen Oostermeijer, Vera Zisler, Alon Albalak, Fabrizio Milo, Sharath Chandra Raparthy, Kanishk Gandhi, Baber Abbasi, Duy Phung, Maia Iyer, Dakota Mahan, Chase Blagden, Srishti Gureja, Mohammed Hamdy, Wen-Ding Li, Giovanni Paolini, Pawan Sasanka Ammanamanchi, Elliot Meyerson

- 大規模言語モデルによる合成データは、自然データを無限に拡張する有望な手法である
- データ生成アルゴリズムの評価は品質、多様性、複雑性の特性で行う
- 品質は分布内、多様性は分布外、複雑性は両方の一般化に重要である
- 品質-多様性のトレードオフがモデルとデータ生成に影響を与える

合成データのQDC（品質・多様性・複雑性）バランスが未来の自己改善アルゴのキーなんだね。面白そう！これからのモデルはもっと多様な対応ができちゃうかも！🌟



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-12-04 02:47

- - -

### [MACAW: A Causal Generative Model for Medical Imaging](http://arxiv.org/abs/2412.02900)

**MACAW: 医療画像のための因果生成モデル**

Vibujithan Vigneshwaran, Erik Ohara, Matthias Wilms, Nils Forkert

- 医療画像で深層学習は研究では有望だが、臨床ではまだ広く使われていない
- 因果関係を重視せず、相関に依存するモデルには説明能力の低下などの問題がある
- MACAWは複雑な因果構造を正規化フローに統合する新しいアプローチを提案する
- 提案手法は、被験者のMRIから年齢を予測し、異なる値での新しいサンプル生成が可能

因果関係を考慮した医療画像の生成モデルってなんか未来っぽくて素敵！脳の老化とかってどうしても気になるし、これで健康に役立つことが期待されるね。実際に観察できないケースの予測とかも面白そう！

**Comment:** 27 pages

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.LG, **投稿日時:** 2024-12-03 23:05

- - -

### [Proximal Control of UAVs with Federated Learning for Human-Robot Collaborative Domains](http://arxiv.org/abs/2412.02863)

**連合学習を用いた人間とロボットの協調領域におけるUAVの近接制御**

Lucas Nogueira Nobrega, Ewerton de Oliveira, Martin Saska, Tiago Nascimento

- 人間とロボットの相互作用における行動分類は未解決の問題である
- 神経ネットワークを用いた行動検出には、隠蔽による問題が存在する
- 提案手法は連合学習を組み込み、データへのアクセスなしでの分散訓練を可能にする
- 実験で96%以上の精度を達成し、隠蔽状況を防ぐ効果を確認した

ラボから飛び出して未来のロボットサービスがもっと身近になりそうだよね。ドローンがもっと賢くなって、人の意図をキャッチしやすくなるなんて、映画みたいな世界が待ってる気がする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, cs.AI, cs.LG, **投稿日時:** 2024-12-03 21:57

- - -

### [Unpaired Modality Translation for Pseudo Labeling of Histology Images](http://arxiv.org/abs/2412.02858)

**組み合わせがないモダリティ翻訳による組織学画像の擬似ラベリング**

Arthur Boschet, Armand Collin, Nishka Katoch, Julien Cohen-Adad

- 組織画像のセグメンテーションは医療応用に重要だが、アノテーションデータの不足が課題
- 教師なしの画像翻訳を用いた擬似ラベリングパイプラインを提案、ターゲット領域の事前アノテーション不要
- 3つの異なる画像領域で2つの擬似ラベリング戦略を評価し、有効性を実証
- 教育パスを通じてSEMデータセットで平均Diceスコア0.736を達成、アノテーションプロセスを加速

難しいデータラベリングもこの方法で楽になるかも！画像の世界ってほんと奥深いよね。AIが手助けしてくれる時代が来るなんてワクワクするな～。



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.AI, cs.CV, **投稿日時:** 2024-12-03 21:45

- - -

### [Methods with Local Steps and Random Reshuffling for Generally Smooth Non-Convex Federated Optimization](http://arxiv.org/abs/2412.02781)

**一般的にスムーズな非凸連合最適化のための局所ステップとランダムリシャッフルの手法**

Yury Demidovich, Petr Ostroukhov, Grigory Malinovsky, Samuel Horváth, Martin Takáč, Peter Richtárik, Eduard Gorbunov

- 非凸の機械学習問題は標準的なスムーズネスの仮定に従わないことが多い
- 本研究では、クライアントの部分参加とランダムリシャッフルを用いた新手法を提案
- 提案手法では、クライアントとサーバーのステップサイズや勾配クリッピングを適切に調整
- Polyak-Łojasiewicz条件下で初の解析を行い、理論と実験結果が一致

連合学習の中で非凸問題に取り組んでるのが興味深いね！新しい手法がどう現実世界で使われるか、ちょっと楽しみ。



**トピック:** [連合学習](fl), **カテゴリ:** math.OC, cs.LG, **投稿日時:** 2024-12-03 19:20
