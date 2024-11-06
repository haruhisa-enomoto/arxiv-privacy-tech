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

更新: 2024-11-06T04:23:56.842878

- - -

### [Concurrent Composition for Continual Mechanisms](http://arxiv.org/abs/2411.03299)

**継続的メカニズムの同時合成**

Monika Henzinger, Roodabeh Safavi, Salil Vadhan

- 非対話型差分プライベートメカニズムの合成定理を、対話型の場合に拡張
- 適応的な敵を考慮した継続的観測環境での研究の拡張
- 継続的差分プライベートメカニズムへの同時合成が可能であることを示す
- 結果は$f$-DPだけでなく、純DPや$(\epsilon, \delta)$-DPにも適用可能

オンラインデータと継続的プライバシーでのアプローチがすごく興味深いね！リアルタイムでの情報保護って未来のテクノロジーに絶対重要だし、もっといろんな応用が期待できそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, **投稿日時:** 2024-11-05 17:50

- - -

### [DiffLM: Controllable Synthetic Data Generation via Diffusion Language Models](http://arxiv.org/abs/2411.03250)

**DiffLM: 拡散言語モデルによる制御可能な合成データ生成**

Ying Zhou, Xinyao Wang, Yulei Niu, Yaojie Shen, Lexin Tang, Fan Chen, Ben He, Le Sun, Longyin Wen

- 最新の大規模言語モデルは高品質なデータ生成を促進するが、合成データ生成は難しい
- DiffLMはVAEをベースに拡散モデルを活用し、元の分布情報や形式構造を保持
- ターゲット分布の学習と生成の目的を分離、学習の柔軟性を向上
- 実データと比較して2-7%優れた結果を実現、特に構造化データでの性能向上

DiffLMって面白そう！実データ超えちゃうとかほんとすごいよね。データとコードの公開もワクワクする〜！

**Comment:** 17 pages, 8 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-11-05 16:47

- - -

### [Formal Logic-guided Robust Federated Learning against Poisoning Attacks](http://arxiv.org/abs/2411.03231)

**形式論理による毒殺攻撃に対抗する堅牢な連合学習**

Dung Thuy Nguyen, Ziyan An, Taylor T. Johnson, Meiyi Ma, Kevin Leach

- 連合学習はプライバシーを重視するも、毒殺攻撃に弱くモデル性能が低下する脅威がある
- 既存手法は主に画像認識向けで、時系列データの連合学習の課題への対応は進んでいない
- FLORALはクライアントの予測を論理的に評価し、時系列データでの毒殺攻撃を緩和する手法
- 実験で予測誤差を大幅に減少させ、時系列応用での連合学習の堅牢性向上を示した

FLORALって面白そうな防御策だね！予測誤差が93.27％も減少するなんて、とても期待できる未来だよね。連合学習の可能性がもっと広がりそう！

**Comment:** arXiv admin note: text overlap with arXiv:2305.00328 by other authors

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.DC, cs.LO, **投稿日時:** 2024-11-05 16:23

- - -

### [Local Lesion Generation is Effective for Capsule Endoscopy Image Data Augmentation in a Limited Data Setting](http://arxiv.org/abs/2411.03098)

**局所病変生成はカプセル内視鏡画像データの拡張において限られたデータ状況で効果的である**

Adrian B. Chłopowiec, Adam R. Chłopowiec, Krzysztof Galus, Wojciech Cebula, Martin Tabakov

- 医療画像データが少ないとGANの識別器が過学習しやすく、分類モデルの性能も低下。
- データを増やす合成データ増強には生成モデルの訓練が必要で、そこで局所病変生成法を提案。
- Poisson Image EditingとImage Inpainting GANを用いて、病変を合成しデータを増強。
- 提案手法は現状の最先端手法を超える成果を示し、特に内視鏡データセットで有効性を確認。

この研究って、限られたデータでも精度を上げる方法があるって感じで、すっごく面白いよね！医療現場で役立ちそうだし、新しい技術がこんなに効果的に応用されるのってワクワクする！

**Comment:** 45 pages, 27 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-11-05 13:44

- - -

### [Speech Separation with Pretrained Frontend to Minimize Domain Mismatch](http://arxiv.org/abs/2411.03085)

**事前学習型フロントエンドによる音声分離のドメイン不一致最小化**

Wupeng Wang, Zexu Pan, Xinke Li, Shuai Wang, Haizhou Li

- 音声分離の目的は混合音声から個別の音声信号を分離すること
- 通常の分離モデルは、ターゲット参照データの不足から合成データで学習
- 提案するDIPフロントエンドは自己教師あり学習でリアルと合成データのドメイン差を縮小
- DIPフロントエンドを活用し、現実データに転移可能な分離モデルの開発に成功

ドメインの壁を超えて、リアルでも合成でもちゃんと分離できるようになるなんて、すごくワクワクするね！この技術で現実のパーティーシーンでも、誰が何を話しているかをクリアに聞き取れちゃうかもね。もっといろんな応用が進みそうで楽しみだよ！

**Comment:** IEEE/ACM Transactions on Audio, Speech, and Language Processing

**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.LG, cs.MM, eess.AS, **投稿日時:** 2024-11-05 13:30

- - -

### [Enhancing DP-SGD through Non-monotonous Adaptive Scaling Gradient Weight](http://arxiv.org/abs/2411.03059)

**非単調な適応スケーリング勾配重みを用いたDP-SGDの強化**

Tao Huang, Qingyu Huang, Xin Shi, Jiayang Meng, Guolong Zheng, Xu Yang, Xun Yi

- 深層学習での課題は、データ保護を維持しつつモデルの有用性を保つ点にある
- 従来のDP-SGD法は小さな勾配を軽視し、モデル精度を損なう可能性がある
- 提案手法は非単調な適応スケーリングを導入し、小さな勾配に適切な重みを割り当てる
- 理論的および実証的分析により、多様なデータセットでプライバシーを保持しつつ高性能を実証

勾配の重さを上手に管理して、より良い結果を出すってすごく面白いよね。新しいアプローチでプライバシーもちゃんと守れるなら、これからの応用範囲がぐんと広がりそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-05 12:47

- - -

### [Gradient-Guided Conditional Diffusion Models for Private Image Reconstruction: Analyzing Adversarial Impacts of Differential Privacy and Denoising](http://arxiv.org/abs/2411.03053)

**プライベート画像再構築のための勾配ガイド条件付拡散モデル：差分プライバシーとノイズ除去の敵対的影響の分析**

Tao Huang, Jiayang Meng, Hong Chen, Guolong Zheng, Xu Yang, Xun Yi, Hua Wang

- 勾配を誘導する条件付き拡散モデルで私的画像を再構築し、差分プライバシーノイズとノイズ除去の関係を分析
- 現在の方法は高解像度画像において計算の複雑さと事前知識が課題である
- 新手法は拡散モデルに最小限の修正のみ必要で、画像生成能力を活かし再構築を実現
- 理論分析でノイズ大きさと攻撃者の能力がどのように影響し合うかを明示し、実験で検証

新しい画像再構築方法ってなんかワクワクするよね！差分プライバシーの影響とか知らなかったから、より深く知れるって面白そう。プライバシーの観点からも安心してデジタルライフ楽しめるといいな。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-11-05 12:39

- - -

### [FEDLAD: Federated Evaluation of Deep Leakage Attacks and Defenses](http://arxiv.org/abs/2411.03019)

**FEDLAD: 深層リーク攻撃と防御の連合評価**

Isaac Baglin, Xiatian Zhu, Simon Hadfield

- 連合学習はプライバシーを保ちつつモデルを協調学習するが、勾配反転技術でデータ漏洩のリスクがある
- これまでの攻撃は連合学習の現実的なシナリオで評価されていないことが多い
- FEDLADフレームワークは深層リークの攻撃と防御を評価する包括的なベンチマークを提供する
- プライバシーとモデル精度のトレードオフを強調し、セキュリティの理解を進めることを目的としている

プライバシーと精度のトレードオフって難しいね。でも、こういうフレームワークがあれば、もっと安全で良いモデルが作れるといいよね！コラボレーションが進むと面白い発見が増えそうだし、ワクワクするね。

**Comment:** 9 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.CV, I.2.11; I.4.5, **投稿日時:** 2024-11-05 11:42

- - -

### [Rozproszone Wykrywanie Zajętości Widma Oparte na Uczeniu Federacyjnym](http://arxiv.org/abs/2411.03017)

**連合学習に基づく分散型スペクトル占有検出**

Łukasz Kułacz, Adrian Kliks

- スペクトル占有検出は動的スペクトルアクセスの鍵で、機械学習を用いて検出を改善
- ラベル付きデータの不足が教師あり学習モデルの主な課題
- センサが学習データにアクセスできない場合でも解決するため、連合学習を提案
- DVB-T信号検出でのハードウェア実験での結果を議論

連合学習を使うことで、データへの直接アクセスが不要になるってすごく便利！センサーのデータをより活用できる未来が楽しみだね。

**Comment:** 4 pages, in Polish language, 10 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, **投稿日時:** 2024-11-05 11:41

- - -

### [Controlling for Unobserved Confounding with Large Language Model Classification of Patient Smoking Status](http://arxiv.org/abs/2411.03004)

**観察不能な交絡因子の制御: 患者の喫煙状況に対する大規模言語モデルの分類の利用**

Samuel Lee, Zach Wood-Doughty

- 医学の因果推論は観察データから治療効果を推定するが、未観察の交絡因子が課題となる
- 機械学習を活用し、未観察変数を補完して分類器の誤差を補正し因果効果を推定する手法がある
- これまでは合成データや単純な分類器、二値変数のみに限定されていた
- 提案された手法は、大規模言語モデルを使用して喫煙状況を予測し、MIMICデータで心エコーの死亡率への影響を推定

因果推論の新しい方法か〜！大規模言語モデルで未観察の交絡因子を扱えるなんてすごいね。医療のデータ分析がもっと正確になる未来が楽しみ！

**Comment:** Advancements In Medical Foundation Models: Explainability,   Robustness, Security, and Beyond (AIM-FM) at NeurIPS 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-05 11:05

- - -

### [IMUDiffusion: A Diffusion Model for Multivariate Time Series Synthetisation for Inertial Motion Capturing Systems](http://arxiv.org/abs/2411.02954)

**IMUDiffusion: 慣性モーションキャプチャシステムのための多変量時系列合成のための拡散モデル**

Heiko Oppel, Michael Munz

- キネマティックセンサーは空間制約がなく使いやすいが、動作データの生成とラベリングは手間とコストがかかる
- データ不足では複雑な動作パターンの認識が難しいため、合成データで多様性を拡張
- IMUDiffusionは多変量時系列生成のための確率的拡散モデルで、人間活動の動態を精度高く再現可能
- 合成データを使用することで、ヒューマンアクティビティ分類器の性能が大幅に向上し、最大でF1スコアが30%改善

IMUDiffusionって名前が可愛くて気になるよね！部活での動きとかもっと詳しく分析できたら、体育の授業とかもレベルアップしそうで楽しそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-05 09:53

- - -

### [Privacy-Preserving Graph-Based Machine Learning with Fully Homomorphic Encryption for Collaborative Anti-Money Laundering](http://arxiv.org/abs/2411.02926)

**共同マネーロンダリング防止のための完全準同型暗号を用いたプライバシー保護グラフベース機械学習**

Fabrianne Effendi, Anupam Chattopadhyay

- サイバー犯罪の増加でマネーロンダリング対策が複雑化し、データサイロが協力を制限している。
- 完全準同型暗号（FHE）を使い、安全に機関間でデータを共有し、プライバシーと規制を遵守。
- プライバシー保護のグラフニューラルネットワーク（GNN）とグラフベースのXGBoostパイプラインを提案。
- 実験結果では、XGBoostモデルが99%を超える精度を示し、グラフ特徴が不均衡データにおけるF1スコアを8%向上。

この研究、おもしろそう！データサイロを乗り越えて、協力ができる技術の進展ってワクワクするよね。未来の金融の安全性が、プライバシーを守りつつ確保できるなんて最高だと思う！

**Comment:** 14th International Conference on Security, Privacy, and Applied   Cryptographic Engineering (SPACE) 2024

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-11-05 09:13

- - -

### [Photon: Federated LLM Pre-Training](http://arxiv.org/abs/2411.02908)

**Photon: 連合LLMの事前学習**

Lorenzo Sani, Alex Iacob, Zeyu Cao, Royson Lee, Bill Marino, Yan Gao, Dongqi Cai, Zexi Li, Wanru Zhao, Xinchi Qiu, Nicholas D. Lane

- 大規模言語モデル(LLM)の拡張には膨大なデータと計算資源が必要で、従来はデータセンターに依存していた
- Photonは、連合学習(FL)を利用して低通信量で国際規模のLLMの事前学習を可能にする初のシステム
- Photonにより最大7Bサイズのモデルが連合方式で訓練でき、中央集権方式より低い困惑度を達成
- 従来の分散訓練方法よりも35%の時間短縮を達成し、極めて高い学習率で高速収束を実現する

Photonって、連合学習使ってLLMを低通信で事前学習できちゃうってすごいね！これで、個々のコンピュータの力を合わせて、大規模モデルをもっと効率的に育てられるようになるのは、未来のチームワークが広がりそうでワクワクするね。影響力のある技術になりそう！

**Comment:** 13 pages, 9 appendix pages, 10 figures, 3 algorithms, 8 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-11-05 08:48

- - -

### [Query-Efficient Adversarial Attack Against Vertical Federated Graph Learning](http://arxiv.org/abs/2411.02809)

**垂直連合グラフ学習に対するクエリ効率の高い敵対的攻撃**

Jinyin Chen, Wenbo Mu, Luxin Zhang, Guohan Huang, Haibin Zheng, Yao Cheng

- グラフニューラルネットワークは、グラフ構造データの表現学習で注目される
- 垂直連合学習により分散グラフデータ処理が可能になるが、敵対的攻撃の耐性は未検討
- NA2というハイブリッド攻撃フレームワークが新提案され、手間をかけずに攻撃性能を向上
- 実験でNA2の効果を示し、最先端の性能を適応防御下でも発揮可能

攻撃の効率を劇的に上げるフレームワークが登場するなんてワクワク！技術発展でセキュリティも進化して面白いことにいっぱい挑戦できそうだね。攻撃と防御の知恵比べが、これからどう展開されるのか楽しみ～！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-05 04:52

- - -

### [FedBlock: A Blockchain Approach to Federated Learning against Backdoor Attacks](http://arxiv.org/abs/2411.02773)

**FedBlock: 分散学習におけるバックドア攻撃に対抗するブロックチェーンアプローチ**

Duong H. Nguyen, Phi L. Nguyen, Truong T. Nguyen, Hieu H. Pham, Duc A. Tran

- 連合学習はプライベートデータを集約せずに分散機で学習する方法だが、セキュリティリスクがある
- 中央サーバへの依存が問題で、サーバが攻撃の単一障害点となる可能性がある
- バックドア攻撃ではクライアントがローカルモデルを汚染し、学習精度を低下させる
- FedBlockはスマートコントラクトを使った新たなブロックチェーンベースのフレームワークで、サーバとクライアント両方のリスクに対応

FedBlockってすごく新しい発想だよね！スマートコントラクトだけで動くなんて、どこでも使えるのがいいな。連合学習の安全性が気になる人にはめちゃくちゃ役立ちそう。

**Comment:** This paper has been accepted as a full paper for the IEEE Special   Session Federated Learning on Big Data 2024 (IEEE BigData 2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.CV, **投稿日時:** 2024-11-05 03:34
