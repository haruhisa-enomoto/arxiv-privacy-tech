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

更新: 2024-12-15T04:22:11.814524

- - -

### [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](http://arxiv.org/abs/2412.09605)

**AgentTrek: ウェブチュートリアルによる経路再生ガイドによるエージェント軌跡の合成**

Yiheng Xu, Dunjie Lu, Zhennan Shen, Junli Wang, Zekun Wang, Yuchen Mao, Caiming Xiong, Tao Yu

- GUIエージェントの開発は多段階の軌跡データ不足が原因で停滞している
- AgentTrekはウェブチュートリアルを活用した大規模なデータ合成プロセスを提案
- チュートリアルテキストをリアル環境で実行するためのステップバイステップ指示に変換
- 合成された軌跡がGUIエージェントの計画と基盤性能を向上させることを実証した

この論文、すごくワクワクするね！ウェブチュートリアルを活用して、GUIエージェントがどんどん進化しそう。大規模なデータが手に入れば、もっとすごいことに挑戦できそうだよね。

**Comment:** https://agenttrek.github.io

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-12 18:59

- - -

### [A Plug-and-Play Algorithm for 3D Video Super-Resolution of Single-Photon LiDAR data](http://arxiv.org/abs/2412.09427)

**シングルフォトンLiDARデータの3Dビデオ超解像のためのプラグアンドプレイアルゴリズム**

Alice Ruget, Lewis Wilson, Jonathan Leach, Rachael Tobin, Aongus Mccarthy, Gerald S. Buller, Steve Mclaughlin, Abderrahim Halimi

- SPADデータは高ダイナミックな3D環境再構築に有用だが、動的シーンで動きぼけを引き起こす
- SPADは低解像度であり、複数測定の集約によって精度を高めるが動的シーンではぼけを招く
- 新たなアルゴリズムが提案され、動きぼけ対策と空間解像度向上を実現するプラグアンドプレイ手法を採用
- 実験で高い解像度とロバスト性を実証、室内外で動的物体の撮像に成功した

SPADと通常カメラの組み合わせで、新しい方法で高解像度な3D映像が撮れるなんてすごい！実際にどれくらいリアルな映像ができるのか、試してみたいな〜。

**Comment:** 14 pages, 10 figures

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-12-12 16:33

- - -

### [MaskTerial: A Foundation Model for Automated 2D Material Flake Detection](http://arxiv.org/abs/2412.09333)

**MaskTerial: 2D材料フレーク自動検出のための基礎モデル**

Jan-Lucas Uslu, Alexey Nekrasov, Alexander Hermans, Bernd Beschoten, Bastian Leibe, Lutz Waldecker, Christoph Stampfer

- 二次元材料フレークの検出と分類を自動化し、サンプル製造の効率化やデータ収集の拡大を可能にする。
- MaskTerialモデルはインスタンスセグメンテーションネットワークを用いて、2D材料のフレークを信頼性高く識別する。
- 合成データ生成器で生成した未ラベルの顕微鏡画像で事前訓練し、新素材には5～10枚の画像で迅速に適応できる。
- 光学的コントラストに基づく不確実性推定モデルを使用し、低コントラスト材料の検出を従来技術より改善する。

MaskTerialってめちゃ便利！少ないデータで新しい素材にすぐ対応できるのがすごく未来っぽいよね～。大規模データ収集が楽々になりそうで、これからの材料研究もワクワクするなぁ！

**Comment:** 9 pages, 5 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cond-mat.mtrl-sci, eess.IV, **投稿日時:** 2024-12-12 15:01

- - -

### [First Train to Generate, then Generate to Train: UnitedSynT5 for Few-Shot NLI](http://arxiv.org/abs/2412.09263)

**最初に生成して訓練し、その後訓練して生成：少数ショットNLIのためのUnitedSynT5**

Sourav Banerjee, Anush Mahajan, Ayushi Agarwal, Eishkaran Singh

- 自然言語推論（NLI）は、文対の関係を分類するタスクである
- 現在のSOTAモデルであるEFLの進展を合成データ強化で工夫
- T5ベースの生成器を使用してデータセットに新たな文対を追加
- 拡張データセットでGTR-T5-XLモデルを学習し新たな精度を達成

合成データで精度を上げるなんて発想が革新的だし面白いね。これからのNLIタスクがますます進化しそう！

**Comment:** 14 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-12-12 13:21

- - -

### [Multi-client Functional Encryption for Set Intersection with Non-monotonic Access Structures in Federated Learning](http://arxiv.org/abs/2412.09259)

**連合学習における非単調アクセス構造を持つ集合交差のためのマルチクライアント機能暗号**

Ruyuan Zhang, Jinguang Han

- 連合学習（FL）は、モデルを共有して学習する分散型機械学習フレームワークである
- 既存の機能暗号（FE）手法は複雑なアクセス制御ポリシーが表現できない
- 本研究では、非単調アクセス構造を持つマルチクライアント機能暗号（MCFE-SI-NAS）を提案
- 提案手法はセキュリティが形式的に証明され、性能分析も行われた

連合学習で他クライアントと安全にコラボできる技術が発展したら、AIの進化が加速しそう！みんなが参加できる未来がもっと広がるかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-12 13:19

- - -

### [VLMs meet UDA: Boosting Transferability of Open Vocabulary Segmentation with Unsupervised Domain Adaptation](http://arxiv.org/abs/2412.09240)

**VLMsとUDAの出会い：教師なしドメイン適応によるオープンボキャブラリセグメンテーションの転移性向上**

Roberto Alcover-Couso, Marcos Escudero-Viñolo, Juan C. SanMiguel, Jesus Bescos

- 従来のセグメンテーションモデルは訓練時のカテゴリに制約される
- VLMsの細粒度分解能力を強化するFROVSSフレームワークを提案
- 提案モデルは教師なしドメイン適応で異なる領域間の適応を可能にする
- カテゴリ共通性なしに適応を成功させる初のUDA-FROVSSフレームワーク

VLMsを強化することで、異なるドメインの壁を越えて使えるようになるの素敵！新しい視点で今後の応用も広がりそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-12-12 12:49

- - -

### [Building a Privacy Web with SPIDEr -- Secure Pipeline for Information De-Identification with End-to-End Encryption](http://arxiv.org/abs/2412.09222)

**SPIDErによるプライバシーウェブの構築 -- エンドツーエンド暗号化を用いた情報非識別化のためのセキュアパイプライン**

Novoneel Chakraborty, Anshoo Tandon, Kailash Reddy, Kaushal Kirpekar, Bryan Paul Robert, Hari Dilip Kumar, Abhilash Venkatesh, Abhay Sharma

- データの非識別化は、利用者のプライバシーを守りつつデータから洞察を得る手法
- Trusted Execution Environments（TEEs）を利用し、クラウド上で第三者を信頼せずに非識別化アプリを実行可能
- SPIDErはエンドツーエンド暗号化を実装し、多様な匿名化技術や形式的プライバシー保証を提供
- データのバッチ処理によりTEEでの差分プライバシー計算のスケーラビリティとパフォーマンス向上

この技術が普及したら、クラウドでもプライバシーをすっごくしっかり守れるようになりそうだね！データを安全に使える未来が楽しみ～。

**Comment:** 3 pages, 2 figures

**トピック:** [差分プライバシー](dp), [TEE](tee), **カテゴリ:** cs.CR, cs.IT, math.IT, **投稿日時:** 2024-12-12 12:24

- - -

### [Evaluating the Potential of In-Memory Processing to Accelerate Homomorphic Encryption](http://arxiv.org/abs/2412.09144)

**インメモリ処理の可能性を評価して準同型暗号を加速する**

Mpoki Mwaisela, Joel Hari, Peterson Yuhala, Jämes Ménétrey, Pascal Felber, Valerio Schiavoni

- クラウド導入がプライバシーとセキュリティ問題を引き起こす
- 準同型暗号は計算機上の暗号データを保護するが計算負荷が大きい
- インメモリ処理(PIM)でプロセッサ-メモリ間のデータ移動を減らす
- 2つのHEライブラリを用いたPIMの実践研究が有益な見解を提供

この研究、クラウドの未来を見据えた新しい作業方法みたいでおもしろいよね！便利で安全な暗号化がもっと手軽になると、さらにみんなの生活が変わりそう。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AR, cs.DC, cs.PF, **投稿日時:** 2024-12-12 10:28

- - -

### [The Utility and Complexity of In- and Out-of-Distribution Machine Unlearning](http://arxiv.org/abs/2412.09119)

**イン・アウト・オブ・ディストリビューション機械学習解除の効用と複雑性**

Youssef Allouah, Joshua Kazdan, Rachid Guerraoui, Sanmi Koyejo

- 機械学習解除はプライバシーと知識ギャップへの対応に重要だが、既存手法は形式的保証が不足
- 類似データの解除では、リスク最小化と出力摂動により有効なトレードオフが可能
- 異なるデータの解除は時間複雑性が再学習を超え、既存手法が不適切
- 新しい頑健なノイズ付き勾配法で時間複雑性を低減しつつ効用を維持

機械学習モデルの記憶を取り除く「解除」って、知る人ぞ知ることだよね！既存手法の弱点を補完する新たな勾配法が登場したのかぁ、使い方広がりそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, math.OC, **投稿日時:** 2024-12-12 09:54

- - -

### [Deep Learning Model Security: Threats and Defenses](http://arxiv.org/abs/2412.08969)

**ディープラーニングモデルのセキュリティ：脅威と防御策**

Tianyang Wang, Ziqian Bi, Yichao Zhang, Ming Liu, Weiche Hsieh, Pohsun Feng, Lawrence K. Q. Yan, Yizhu Wen, Benji Peng, Junyu Liu, Keyu Chen, Sen Zhang, Ming Li, Chuanqi Jiang, Xinyuan Song, Junjie Yang, Bowen Jing, Jintao Ren, Junhao Song, Hong-Ming Tseng, Silin Chen, Yunze Wang, Chia Xin Liang, Jiawei Xu, Xuanhe Pan, Jinlang Wang, Qian Niu

- ディープラーニングはAIを進化させたが、攻撃やデータの毒性、モデル盗難、プライバシー漏洩などの課題に直面している
- 敵対的訓練や差分プライバシー、連合学習を使った防御策の強みと限界を調査
- 対比学習や自己教師付き学習が堅牢性向上に役立つ方法として紹介されている
- 将来の方向性として、自動化された防御やゼロトラストアーキテクチャ、AIモデルのセキュリティ課題が示されている

未来のディープラーニングって、単に賢いだけじゃなくて、安全性もしっかり考えてるのがすごいよね！ゼロトラストアーキテクチャとか、新しい概念聞くだけでワクワクしちゃう。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, cs.SE, **投稿日時:** 2024-12-12 06:04

- - -

### [BA-ORABE: Blockchain-Based Auditable Registered Attribute-Based Encryption With Reliable Outsourced Decryption](http://arxiv.org/abs/2412.08957)

**BA-ORABE: 信頼性のある外部委任復号機能を持つブロックチェーンベースの監査可能な登録属性ベース暗号化**

Dongliang Cai, Borui Chen, Liang Zhang, Haibin Kan

- ABEはクラウドでの細粒度のアクセス制御を可能にするが、従来の方式は中央集権的な認証機関を必要とする。
- 本研究で提案するBA-ORABEは、ユーザーが自らの公開鍵と属性を登録し、監査可能な登録方法を用いることで、中央機関を排除。
- 復号化負担を軽減するためのデータのデコンシーリングを信頼できるデコードクラウドサービスにアウトソースする技術を採用。
- 公正性と利害の守護を実現し、ブロックチェーンを使うことで全てのプロセスが透明で完全に監査可能。

この論文、ブロックチェーンの技術でセキュリティを強化しているのが面白いよね。未来的なAEBシステムでクラウド利用の安全性がどこまで上がるのかワクワクしちゃう！

**Comment:** 16pages

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-12 05:38

- - -

### [Predicting Quality of Video Gaming Experience Using Global-Scale Telemetry Data and Federated Learning](http://arxiv.org/abs/2412.08950)

**グローバル規模のテレメトリーデータと連合学習を用いたビデオゲーム体験の品質予測**

Zhongyang Zhang, Jinhe Wen, Zixi Chen, Dara Arbab, Sruti Sahani, Bijan Arbab, Haojian Jin, Tauhidur Rahman

- ゲーム体験におけるFPSの重要性を認識し、購入前に正確なFPS予測を提供する意義を示す
- グローバルデータセットを用いて、プレイヤー・ゲーム側の特性や国の経済統計がFPSに及ぼす影響を分析
- プライバシーを考慮し連合学習モデルを提案し、独自な知識カーネルで精度向上を図る
- 新たな学習・予測スキームでコールドスタート問題に対処し、従来の手法を上回る性能を実現

連合学習でFPSを予測する方法ってすごく興味深いね！特にプライバシー保護しながら予測精度を上げるアイデアが今後のゲーム体験を変えそうでワクワクするよね。

**Comment:** 22 pages, 11 figures, 6 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.HC, cs.AI, cs.IR, **投稿日時:** 2024-12-12 05:28

- - -

### [Federated Foundation Models on Heterogeneous Time Series](http://arxiv.org/abs/2412.08906)

**異種時系列データにおける連合基盤モデル**

Shengchao Chen, Guodong Long, Jing Jiang, Chengqi Zhang

- 時系列基盤モデルの訓練は多様なアプリケーションでの一般化が課題
- クロスドメインのデータ統合で共有部分を抽出しモデルを訓練
- 時系列データに対し連合学習アプローチFFTSを提案し各組織を独立したクライアントとする
- 提案手法は予測や欠損値補完、異常検知で優れた一般化能力を発揮

この論文、おもしろそう！時系列データの連合学習って、どこでも使えるモデルが作れるかも！スゴく未来が明るくなりそうだよね！

**Comment:** Accepted by Main Track in AAAI'25

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-12 03:38

- - -

### [Phi-4 Technical Report](http://arxiv.org/abs/2412.08905)

**Phi-4テクニカルレポート**

Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien Bubeck, Ronen Eldan, Suriya Gunasekar, Michael Harrison, Russell J. Hewett, Mojan Javaheripi, Piero Kauffmann, James R. Lee, Yin Tat Lee, Yuanzhi Li, Weishung Liu, Caio C. T. Mendes, Anh Nguyen, Eric Price, Gustavo de Rosa, Olli Saarikivi, Adil Salim, Shital Shah, Xin Wang, Rachel Ward, Yue Wu, Dingli Yu, Cyril Zhang, Yi Zhang

- phi-4は14億パラメータの言語モデルで、データ品質を重視して開発された。
- 有機データではなく合成データを戦略的に利用してトレーニングしている。
- STEM中心のQA能力で、教師モデルのGPT-4を超える成果を示している。
- phi-3と比べてアーキテクチャ変更は少ないが、データとトレーニングで性能を向上。

合成データがこんなに効果的だなんてちょっと驚き！STEMとか難しい分野でも成果出しちゃうの、すごいなぁって思う。やっぱりデータの質と戦略が鍵なのかもね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-12-12 03:37

- - -

### [A Graph-Based Synthetic Data Pipeline for Scaling High-Quality Reasoning Instructions](http://arxiv.org/abs/2412.08864)

**高品質推論命令の拡張のためのグラフベースの合成データパイプライン**

Jiankang Wang, Jianjun Xu, Xiaorui Wang, Yuxin Wang, Mengting Xing, Shancheng Fang, Zhineng Chen, Hongtao Xie, Yongdong Zhang

- 高品質の推論データ合成は大規模言語モデルの性能を向上させるが、コストが高くスケーラビリティが低い問題がある
- 本研究では、経済的かつスケーラブルなグラフベースの合成データパイプライン（GSDP）を提案
- 知識グラフに着想を得て知識点を抽出し、その関係性をグラフで表現することでデータを255倍に拡張
- GSDPを用いた数学的推論タスクで、コストを抑えつつ高い精度を達成し、関連データセットも公開予定

データをめちゃくちゃ増やせるのにコストも抑えられてるってすごいよね！特に数学的な推論に効くっていうのも理系には嬉しいニュース！業界の人たちがどんどん取り入れて、もっと面白いことができるようになりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-12-12 01:52

- - -

### [Exploring Large Language Models on Cross-Cultural Values in Connection with Training Methodology](http://arxiv.org/abs/2412.08846)

**トレーニング手法と関連した異文化価値観における大規模言語モデルの探求**

Minsang Kim, Seungjun Baek

- LLMは人間社会の文化的価値を判断するが、社会制度や進歩については精度が低い
- LLMは西洋文化に偏った判断をする傾向があり、多言語コーパスでの訓練で改善可能
- モデルサイズを増加させると社会的価値の理解が向上し、合成データで小さなモデルが強化可能
- 設計手法と文化価値の理解の関係において重要な知見を提供する

文化の異なる価値観を理解するってすごく挑戦的だよね！多言語コーパスを活用したら、もっとグローバルな視点が持てるLLMになるのかな、楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-12-12 00:52

- - -

### [Euclid: Supercharging Multimodal LLMs with Synthetic High-Fidelity Visual Descriptions](http://arxiv.org/abs/2412.08737)

**Euclid: 合成高精度視覚記述でマルチモーダル大規模言語モデルを強化**

Jiarui Zhang, Ollie Liu, Tianyu Yu, Jinyi Hu, Willie Neiswanger

- 現行のマルチモーダル大規模言語モデルは低レベル視覚認識が苦手である
- Geoperceptionというベンチマークを提案し、視覚情報の幾何学的詳細を評価
- 合成データとデータカリキュラムの多段階トレーニングが有効と判明
- Euclidは合成データで訓練され、幾何学的認識で他モデルを平均10.65%上回る

視覚のハイレベルなことに挑むEuclidが超えちゃったんだね！未来のAIにはもっと多くの可能性が潜んでいそうでワクワクしちゃう。何だか技術がどんどん進化しちゃって置いてかれそう！？

**Comment:** 33 pages, 22 figures, 5 tables, 7 algorithms

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.CL, **投稿日時:** 2024-12-11 19:12

- - -

### [Coherent3D: Coherent 3D Portrait Video Reconstruction via Triplane Fusion](http://arxiv.org/abs/2412.08684)

**Coherent3D: Triplane Fusionによるコヒーレントな3Dポートレートビデオ再構築**

Shengze Wang, Xueting Li, Chao Liu, Matthew Chan, Michael Stengel, Henry Fuchs, Shalini De Mello, Koki Nagano

- 1枚の画像から3Dポートレートビデオを再構築する技術が発展し、遠隔存在システムを可能にした
- フレームごとの3D再構築は時間的に不安定で、ユーザーの見た目を忘れることがある
- 新手法は3D基本データとフレームごとの動きを融合し、リアルな見た目を再現
- 合成データで訓練し、最新の3D再構築と時間的一貫性を両立した結果を達成

未来の通信って感じでワクワクするよね！この技術が進化したら、もっとリアルな自己表現ができるようになるんじゃないかな～。

**Comment:** arXiv admin note: substantial text overlap with arXiv:2405.00794

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, eess.IV, **投稿日時:** 2024-12-11 18:57
