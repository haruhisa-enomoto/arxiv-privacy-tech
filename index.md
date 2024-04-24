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

更新: 2024-04-24T04:20:39.186779

- - -

### [Multimodal Large Language Model is a Human-Aligned Annotator for Text-to-Image Generation](http://arxiv.org/abs/2404.15100)

**多モーダル大規模言語モデルを利用した人間と整合性を持つテキストから画像への生成アノテータ**

Xun Wu, Shaohan Huang, Furu Wei

- 人間の好みのデータセットを活用してテキストから画像への生成モデルの整合性を高めることが示された
- 多様な好みの側面を捉える高品質で細かい好みのデータセットVisionPreferを構築
- VisionPreferを通じた報酬モデルVP-Scoreを訓練し、生成モデルのトレーニングに指導
- VisionPreferは画像の審美性や合成画像生成におけるテキストと画像の整合性を大幅に向上させた



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.MM, **投稿日時:** 2024-04-23 14:53

- - -

### [Leverage Variational Graph Representation For Model Poisoning on Federated Learning](http://arxiv.org/abs/2404.15042)

**連合学環境でのモデル毒物攻撃に対する変分グラフ表現の利用**

Kai Li, Xin Yuan, Jingjing Zheng, Wei Ni, Falko Dressler, Abbas Jamalipour

- 新しい型のモデル毒物（MP）攻撃が連合学習（FL）に対して提案され、この攻撃は教育データにアクセスせずに善良なローカルモデルだけを利用
- 変分グラフオートエンコーダー（VGAE）を用いて、グラフの構造情報を取得し、敵対的に悪意のあるローカルモデルを生成
- 提案されたVGAE-MP攻撃は効果的でありながら、既存の防御機構による検出が困難
- 実験により、連合学習の精度が徐々に低下し、既存の防御メカニズムでは攻撃を検出できないことが確認された

**Comment:** 12 pages, 8 figures, 2 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-04-23 13:43

- - -

### [Near-Universally-Optimal Differentially Private Minimum Spanning Trees](http://arxiv.org/abs/2404.15035)

**差分プライバシーにおけるほぼ普遍的に最適な最小全域木**

Richard Hladík, Jakub Tětek

- 差分プライバシーの目標を達成するために、滑らかな感度や提案-テスト-解放、逆感度メカニズムなどの技術が開発された
- 本研究では、差分プライバシーで初めて、最小全域木の近似リリースに対する簡単な差分プライバシー機構が、$\ell_1$ 近傍関係における普遍的最適性の観点から近似的に最適であることを実証
- 既存の機構が最悪の場合の近似最適性のみが知られていた
- さらに、$\ell_\infty$ 近傍関係においては最適ではなかったため、多項式時間で実行可能な指数メカニズムを用い、$\ell_1$ および $\ell_\infty$ 近傍関係の両方で普遍的に近似的に最適になることを示した



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, **投稿日時:** 2024-04-23 13:39

- - -

### [IPAD: Industrial Process Anomaly Detection Dataset](http://arxiv.org/abs/2404.15033)

**IPAD: 産業プロセス異常検出データセット**

Jinfan Liu, Yichao Yan, Junjie Li, Weiming Zhao, Pengzhi Chu, Xingdong Sheng, Yunhui Liu, Xiaokang Yang

- 産業シーンでのビデオ異常検出（VAD）は、プライバシーとセキュリティの問題から特化したデータセットや方法が不足している
- 新たに提案されたIPADデータセットは、産業シナリオに特化し、16種の産業機器を含む合成および実世界のビデオ6時間以上を含む
- データセットは産業プロセスの主要特徴である周期性を注釈し、周期情報を解析するための周期メモリモジュールとスライディングウィンドウ検査メカニズムを導入
- LoRAアダプターを活用して、合成データで訓練されたモデルを実世界シナリオに効果的に移行する方法を探求



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-23 13:38

- - -

### [Zero-Knowledge Location Privacy via Accurate Floating Point SNARKs](http://arxiv.org/abs/2404.14983)

**ゼロ知識位置プライバシーによる正確な浮動小数点SNARKs**

Jens Ernstberger, Chengru Zhang, Luca Ciprian, Philipp Jovanovic, Sebastian Steinhorst

- ゼロ知識位置プライバシー(ZKLP)を導入し、ユーザーが正確な位置を明かすことなく、特定の地理的領域内にいることを第三者に証明できるようにする
- ZKLPは、用途に応じて異なる粒度のカスタマイゼーションをサポート
- 浮動小数点算術のIEEE 754標準に完全準拠した初のゼロ知識証明(ZKP)回路を導入
- プライバシーを保護するピアツーピア接近度テストプロトコルを構築し、AliceとBobが他の位置情報を公開することなく距離を確認できるプロトコルを実現



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-04-23 12:38

- - -

### [Fin-Fed-OD: Federated Outlier Detection on Financial Tabular Data](http://arxiv.org/abs/2404.14933)

**Fin-Fed-OD: 金融表データにおけるフェデレーション型外れ値検出**

Dayananda Herurkar, Sebastian Palacio, Ahmed Anwar, Joern Hees, Andreas Dengel

- 実世界の動的かつ未知の異常分布による課題を克服するために、開かれた世界を前提とした堅牢な方法が求められている
- この研究では、データの機密性を損なうことなく個々の組織内での外れ値検出を向上させる方法を提案している
- 提案手法は表現学習と連合学習技術を活用し、未知の異常の検出を改善している
- モデルのパラメータのみが組織間で共有されるため、データプライバシーが保護される



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-23 11:22

- - -

### [Bathymetric Surveying with Imaging Sonar Using Neural Volume Rendering](http://arxiv.org/abs/2404.14819)

**神経体積レンダリングを使用したイメージングソナーによる水深測量**

Yiping Xie, Giancarlo Troni, Nils Bore, John Folkesson

- 従来の教師あり学習やラムバート反射に基づく表面レンダリングを超越した自己教師ありフレームワークを提案
- 高解像度な海底ハイトマップを神経パラメトリック多解像度ハッシュ符号化スキームで表現し、階層的サンプリング技術を用いてボリュームレンダリング
- 水平および垂直のビームパターンをモデル化し、それを水深測定と共に推定
- シミュレーションおよびリモート操作型潜水艇(ROV)による現場データで評価し、従来手法よりも優れた成績を示す



**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, **投稿日時:** 2024-04-23 08:13

- - -

### [FLARE: A New Federated Learning Framework with Adjustable Learning Rates over Resource-Constrained Wireless Networks](http://arxiv.org/abs/2404.14811)

**FLARE: リソース制約のある無線ネットワーク上で学習率を調整可能な新しい連合学習フレームワーク**

Bingnan Xiao, Jingjing Zhang, Wei Ni, Xin Wang

- FLAREフレームワークでは、各デバイスが瞬間的な計算力に応じて個々の学習率とローカルトレーニングの反復回数を調整可能
- 非i.i.d.データセットと計算能力の不均衡が存在する一般的な設定の下で、非凸モデルに対するFLAREの収束上界が厳格に確立された
- チャネルの異質性を活用するために、FLAREのスケジューリングを最適化し、新たな貪欲法によるデバイスの選択とバイナリサーチを用いた帯域幅の割り当てが行われる
- 提案されたスケジューリングポリシーにより、FLAREはテスト精度でベースラインを上回り、収束が大幅に速くなることが実験で示された



**トピック:** [連合学習](fl), **カテゴリ:** eess.SP, cs.LG, **投稿日時:** 2024-04-23 07:48

- - -

### [Simulating Task-Oriented Dialogues with State Transition Graphs and Large Language Models](http://arxiv.org/abs/2404.14772)

**状態遷移グラフと大規模言語モデルを用いたタスク指向対話のシミュレーション**

Chris Samarinas, Pracha Promthaw, Atharva Nijasure, Hansi Zeng, Julian Killingback, Hamed Zamani

- SynTODは、意図分類、スロット充填、対話型質問応答等の複雑なタスクを扱うタスク指向対話システムの開発のための新しい合成データ生成手法である
- 状態遷移グラフを使用してTODシステムの望ましい振る舞いを定義し、大規模言語モデルを使用したランダムウォークと応答シミュレーションにより構造化された多様な会話を生成
- グラフ誘導の応答シミュレーションは、意図分類とスロット充填、応答の関連性において大幅な改善をもたらす
- 研究用にデータセット、モデル、コードを公開し、特定のドメインのTODシステムの迅速な開発と評価への道を開く



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-04-23 06:23

- - -

### [Skip the Benchmark: Generating System-Level High-Level Synthesis Data using Generative Machine Learning](http://arxiv.org/abs/2404.14754)

**ベンチマークを飛ばして、生成機械学習を使ったシステムレベルの高水準合成データを生成する**

Yuchao Liao, Tosiron Adegbija, Roman Lysecky, Ravi Tandon

- 高水準合成（HLS）設計空間探索（DSE）は、HLSプロセス中のパレート最適なハードウェアソリューションを効率的に探るために広く受け入れられている手法である
- 既存のHLSベンチマークを使ったデータ生成は専門知識と時間が必要であり、実行が困難である
- 本論文では、バリエーショナルオートエンコーダと生成敵対ネットワークを用いた新しいアプローチ「Vaegan」を提案し、それにより合成データを生成する
- Vaeganは効果的に合成HLSデータを生成し、そのデータは元のデータの分布に密接に一致することが示された

**Comment:** Accepted at Great Lakes Symposium on VLSI 2024 (GLSVLSI 24)

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.AR, **投稿日時:** 2024-04-23 05:32

- - -

### [Employing Layerwised Unsupervised Learning to Lessen Data and Loss Requirements in Forward-Forward Algorithms](http://arxiv.org/abs/2404.14664)

**レイヤーごとの教師なし学習を利用して、フォワード-フォワードアルゴリズムのデータと損失の要件を軽減する**

Taewook Hwang, Hyein Seo, Sangkeun Jung

- 従来のバックプロパゲーションを使用したディープラーニングモデルの制約を克服するため、フォワード-フォワードアルゴリズムが使用されている
- フォワード-フォワードアルゴリズムは特殊な入力と損失関数を要求するが、教師なし学習モデルを用いることでこれらの制限が克服される
- 教師なしのフォワード-フォワードアルゴリズムにより、さまざまなデータセットやタスクでの安定した学習と活用が可能となる
- 連合学習のような分散学習環境でも、このアプローチにより実用的な応用が期待される

**Comment:** 8 pages, 6 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-23 01:49

- - -

### [UPose3D: Uncertainty-Aware 3D Human Pose Estimation with Cross-View and Temporal Cues](http://arxiv.org/abs/2404.14634)

**UPose3D: 確信度を考慮した3次元人間ポーズ推定のためのクロスビューと時間的手がかりの活用**

Vandad Davoodnia, Saeed Ghorbani, Marc-André Carbonneau, Alexandre Messier, Ali Etemad

- UPose3Dは、直接的な3Dアノテーションを必要とせず、既存のポーズ推定フレームワークのロバストさと柔軟性を向上させる
- 一枚の画像からの2Dキーポイント推定器の予測を時間的およびクロスビュー情報を活用して精細化するポーズコンパイラモジュールを核とする
- 新しいクロスビュー融合戦略は任意のカメラ数に拡張可能であり、合成データ生成戦略により多様なアクター、シーン、視点でも一般化を実現
- 2Dキーポイント推定器とポーズコンパイラモジュールの予測確信度を活用して、異常値やノイズデータに強いロバスト性を提供し、分布外設定での最先端のパフォーマンスを実現

**Comment:** 18 pages, 12 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-04-23 00:18

- - -

### [Align Your Steps: Optimizing Sampling Schedules in Diffusion Models](http://arxiv.org/abs/2404.14507)

**サンプリングスケジュールを最適化：拡散モデルにおけるステップの調整**

Amirmojtaba Sabour, Sanja Fidler, Karsten Kreis

- 拡散モデル（DM）は視覚領域で最先端の生成モデルとして確立しているが、サンプリング速度が遅いという問題がある
- 本研究では初めて、DMのサンプリングスケジュールを最適化する一般的かつ原理的な方法「Align Your Steps」を提案
- 非同期計算を活用して、異なるソルバー、訓練済みDM、データセットに特化した最適なスケジュールを見つける
- 提案手法は、画像、動画、2Dおもちゃデータの合成ベンチマークで評価され、従来の手作りスケジュールをほぼ全ての実験で上回る成果を示す

**Comment:** Project page:   https://research.nvidia.com/labs/toronto-ai/AlignYourSteps/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-04-22 18:18

- - -

### [A Multi-Faceted Evaluation Framework for Assessing Synthetic Data Generated by Large Language Models](http://arxiv.org/abs/2404.14445)

**大規模言語モデルにより生成された合成データを評価する多面的評価フレームワーク**

Yefeng Yuan, Yuhong Liu, Liang Cheng

- 大規模言語モデルの発展により、特に製品レビューなどの構造化された表形式で合成データの生産が進展
- 合成データの生成においてプライバシー漏洩の懸念が存在し、評価フレームワークの欠如が指摘されている
- SynEvalというオープンソースの評価フレームワークを新たに導入し、合成データの忠実度、有用性、プライバシー保護を評価
- ChatGPT、Claude、Llamaにより生成された合成製品レビューデータにSynEvalを適用し、評価指標間のトレードオフを明らかにする

**Comment:** 10 pages, 1 figure, 4 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, **投稿日時:** 2024-04-20 08:08

- - -

### [FLoRA: Enhancing Vision-Language Models with Parameter-Efficient Federated Learning](http://arxiv.org/abs/2404.15182)

**FLoRA: 機械学習を用いた視覚言語モデルの改良**

Duy Phuong Nguyen, J. Pablo Munoz, Ali Jannesari

- CLIPモデルを含む視覚言語モデル（VLM）は、画像キャプションから多様な検索エンジンへと幅広い応用範囲を持つ
- VLMの従来のトレーニングは巨大なデータセットを必要とし、プライバシー保護とデータガバナンスの問題がある
- 本稿では連合学習とパラメータ効率の良い LoRA(低ランク適応)を利用してVLMをトレーニングする新たな手法を提案
- 提案された方法は、トレーニング時間を最大34.72倍高速化し、メモリ使用量を2.47倍削減する

**Comment:** 10 pages, 11 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-04-12 00:36
