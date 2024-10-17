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

更新: 2024-10-17T04:23:04.326348

- - -

### [Vaccinating Federated Learning for Robust Modulation Classification in Distributed Wireless Networks](http://arxiv.org/abs/2410.12772)

**分散型無線ネットワークにおけるモジュレーション分類のための連合学習のワクチン化**

Hunmin Lee, Hongju Seong, Wonbin Kim, Hyeokchan Kwon, Daehee Seo

- 自動モジュレーション分類は、効率的で信頼性のある通信サービスに重要
- 既存のFLモデルは非IID環境で最適な学習収束を妨げる課題に直面
- FedVaccineはノイズ耐性を強化し過学習を軽減する新たなFLモデル
- インテグレーション困難を克服し、性能改善と信頼性の向上を実証

なるほど、連合学習にノイズを意図的に加えるなんて面白いね！今後、ノイズが多い現場でも安心して使える技術が増えそうって思った！ 😊📡



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.AI, **投稿日時:** 2024-10-16 17:48

- - -

### [StyleDistance: Stronger Content-Independent Style Embeddings with Synthetic Parallel Examples](http://arxiv.org/abs/2410.12757)

**StyleDistance: 合成並列例を用いたより強力な内容非依存のスタイル埋め込み**

Ajay Patel, Jiacheng Zhu, Justin Qiu, Zachary Horvitz, Marianna Apidianaki, Kathleen McKeown, Chris Callison-Burch

- スタイル表現は、同じライティングスタイルのテキストを近く、異なるスタイルのテキストを遠くに埋め込むことを目指す
- StyleDistanceは内容依存を排除し、強力なスタイル埋め込みを実現する新しいアプローチ
- 合成データセットを用い、40のスタイル特徴で対比学習を行い、ポジティブ・ネガティブ例を生成
- 内容非依存性を向上させ、実世界のベンチマークで優れた性能を示し、従来の手法を上回る

合成データを使ってスタイルだけを抽出するアプローチが面白いね！これで、スタイルに特化したAIがどんどん進化していく未来が楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-10-16 17:25

- - -

### [Federated Learning and Free-riding in a Competitive Market](http://arxiv.org/abs/2410.12723)

**競争市場における連合学習とフリーライディング**

Jiajun Meng, Jing Chen, Dongfang Zhao, Lin Liu

- 連合学習はプライバシーを守りつつ、競争市場で技術向上を目指す協力技術
- フリーライディング行動が企業の情報提供意欲を阻害し、連合学習の形成を困難にする可能性
- 情報量が少ない企業は常にフリーライディングが有利で、競争が過激でない場合にのみ連合学習を形成
- 連合学習が形成されると全関係者が利益を得る「全員が勝つ」状況が存在

フリーライダーの問題って、協力しようとする企業にとって大きな壁だよね。でも、この論文では「All-Win」な状況もあるってことが示されてとってもワクワク！未来の市場の在り方に超期待だね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.GT, econ.TH, **投稿日時:** 2024-10-16 16:31

- - -

### [VividMed: Vision Language Model with Versatile Visual Grounding for Medicine](http://arxiv.org/abs/2410.12694)

**VividMed: 医療における多目的な視覚的基盤のためのビジョン言語モデル**

Lingxiao Luo, Bingda Tang, Xuanzhong Chen, Rong Han, Ting Chen

- 医療領域でのVLMは個別の視覚基盤が必要で、医療画像が3Dであることが多く応用が難しい。
- VividMedは、2Dおよび3Dデータを含む多様な画像モダリティに対応し、セマンティックセグメンテーションマスクとインスタンスレベルのバウンディングボックス生成をサポートする。
- オープンデータセットとモデルを活用した3段階のトレーニングプロセスと自動データ合成パイプラインを設けている。
- 視覚的基盤能力の統合により、視覚質問応答やレポート生成などの下流タスクでの性能が向上することが実証されている。

医療分野での視覚言語モデルってすごく未来っぽい！3Dデータにも対応してるなんて、どんな風に役に立つのか興味津々。これからどんな進化を遂げるんだろうって考えるとワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, **投稿日時:** 2024-10-16 15:54

- - -

### [A comparative analysis of metamodels for lumped cardiovascular models, and pipeline for sensitivity analysis, parameter estimation, and uncertainty quantification](http://arxiv.org/abs/2410.12654)

**集約化心血管モデルのメタモデルに関する比較分析、感度解析、パラメータ推定、および不確実性定量化のためのパイプライン**

John M. Hanna, Pavlos Varsos, Jérôme Kowalski, Lorenzo Sala, Roel Meiburg, Irene E. Vignon-Clementel

- 0次元心血管モデルは手術計画などで全球的血液循環を研究するための低次元モデルである
- 計算コストが低いが、パラメータ推定と不確実性定量化で多くの評価が必要で計算的に高価になる
- 感度解析、パラメータ推定、不確実性定量化のためのメタモデル構築パイプラインを提案
- ニューラルネットワークが結果品質、計算時間、推定精度で最も効率的であると判明

なんかこの研究って、0Dモデルの反復処理をもっと効率よくしてくれる道を生み出してる感じだよね！ニューラルネットワークが最強みたいだから、それを使って手術計画とか、いろんな場面で役立っちゃうかも！



**トピック:** [合成データ](sd), **カテゴリ:** math.NA, cs.NA, q-bio.TO, **投稿日時:** 2024-10-16 15:16

- - -

### [Constrained Posterior Sampling: Time Series Generation with Hard Constraints](http://arxiv.org/abs/2410.12652)

**制約付き後部サンプリング: 厳格な制約による時系列生成**

Sai Shankar Narasimhan, Shubhankar Agarwal, Litu Rout, Sanjay Shakkottai, Sandeep P. Chinchali

- 現実的な時系列サンプル生成は、合成データでユーザープライバシーを守りつつモデルのストレステストに重要。
- 工学や安全性が重要な分野では、サンプルが物理法則や自然に基づく厳格な制約を満たす必要がある。
- 従来の制約下での時系列生成法はスケーラブルでなく、サンプル品質が低下する課題があった。
- CPS法は多くの制約を考慮し拡張可能で、サンプル品質や現実性が向上することを実証。

制約下でも高品質な時系列データを作れる新しい方法って、未来の色んな応用にわくわくしちゃうよね！特に災害時の電力需要の予測とかで大活躍しそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, eess.SP, **投稿日時:** 2024-10-16 15:16

- - -

### [From Measurement Instruments to Training Data: Leveraging Theory-Driven Synthetic Training Data for Measuring Social Constructs](http://arxiv.org/abs/2410.12622)

**測定手段から訓練データへ: 社会的概念を測定するための理論駆動型合成訓練データの活用**

Lukas Birkenmaier, Matthias Roth, Indira Sen

- 合成訓練データがテキスト分類を強化する可能性を体系的に検討
- 社会科学の測定手段から合成データを生成する方法を探求
- 性差別と政治トピックの2つの研究で合成データの有効性を評価
- 理論駆動の合成データがラベル付きデータの代替として有効であることを示す

合成データを理論的に生成することで、ラベル付されたデータが少なくても精度を保てるなんて、人手の削減にもつながりそうだね！特に政治トピックでは大きな可能性がありそうで、これからの研究がどう発展するのかワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.CY, **投稿日時:** 2024-10-16 14:42

- - -

### [Evaluating Utility of Memory Efficient Medical Image Generation: A Study on Lung Nodule Segmentation](http://arxiv.org/abs/2410.12542)

**メモリ効率の良い医用画像生成の有用性評価: 肺結節セグメンテーションの研究**

Kathrin Khadra, Utku Türkbey

- 公開されている医用画像データの不足がAIモデルの発展を制限している
- メモリ効率の良いパッチ単位のDDPMで合成医用画像を生成する手法を提案
- 合成データでの訓練は、実データと同等のDiceスコアを達成
- 合成画像を実データに追加すると、セグメンテーション性能が大幅に向上

この論文って、本物の医用画像が少なくてもAIを鍛えるための合成画像がちゃんと役立つってことだよね！技術が進んで、もっと沢山のケースに使われるようになるといいなって思う！



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, cs.LG, **投稿日時:** 2024-10-16 13:20

- - -

### [Disentangling data distribution for Federated Learning](http://arxiv.org/abs/2410.12530)

**連合学習のためのデータ分布の解きほぐし**

Xinyuan Zhao, Hanlin Gu, Lixin Fan, Qiang Yang, Yuxing Han

- 連合学習は、データプライバシーを損なわずに分散クライアントのプライベートデータを用いてグローバルモデルを共同訓練する技術
- クライアント間のデータ分布の絡まりが広範な適用の妨げとなっている
- データ分布を解きほぐすことで、1回のコミュニケーションラウンドで分散システムと同等の効率が実現可能と示す
- FedDistrアルゴリズムを提案し、データ分布を安定して分離・復元し、従来の方法を上回るモデル効率を実証

新しい連合学習のアプローチが効率を劇的に改善しちゃうなんて！これって分散型AIの時代がもっと早く来る予感がする。すごくエキサイティングでワクワクしちゃうね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-10-16 13:10

- - -

### [Retrieval-Reasoning Large Language Model-based Synthetic Clinical Trial Generation](http://arxiv.org/abs/2410.12476)

**検索-推論型大規模言語モデルによる合成臨床試験生成**

Zerui Xu, Fang Wu, Tianfan Fu, Yue Zhao

- 機械学習は臨床領域で期待されるが、データ不足と倫理の制約がある
- LLMsの可能性は十分に探求されていないため、新たに少数ショットフレームワークを提案
- 合成データが実際の臨床試験データセットを効果的に補強できると実験で示した
- 合成データで微調整したモデルにより試験結果予測のトレーニングが向上する

これってすごくない？合成データで本物の臨床試験を補えるなんて、もっと効率的な研究ができそう！倫理的にも安心だし、夢が広がるよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-10-16 11:46

- - -

### [Reconstruction of Differentially Private Text Sanitization via Large Language Models](http://arxiv.org/abs/2410.12443)

**大規模言語モデルによる差分プライバシー文書の復元**

Shuchao Pang, Zhigang Lu, Haichen Wang, Peng Fu, Yongbin Zhou, Minhui Xue, Bo Li

- 差分プライバシーが適用された文書がLLMによって復元可能であると発見
- ブラックボックスとホワイトボックスの2つの攻撃手法を提案
- 実験では特にChatGPT-4oやClaude-3.5で高い復元率を確認
- LLMが差分プライバシー文書の新たなセキュリティリスクとなる可能性を指摘

これ、すごく興味深いよね！差分プライバシーが完璧じゃないって感じがちょっと怖いけど、新しい視点で考えたら、これを改善する技術の進歩が期待できるかも！LLMでのプライバシーって、本当にまだまだ深いなぁ。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-10-16 10:41

- - -

### [TPFL: A Trustworthy Personalized Federated Learning Framework via Subjective Logic](http://arxiv.org/abs/2410.12316)

**信頼できる個人化連合学習フレームワーク: 主観論理を用いたアプローチ**

Jinqian Chen, Jihua Zhu

- 連合学習はデータのプライバシーを守りつつ共同でモデルを訓練する技術
- TPFLフレームワークは主観論理を用いて信頼性を向上させる
- データの不均一性を軽減して、安全で信頼性のある学習を実現
- 悪意ある攻撃やドメインシフトに対する耐性を持ち、高ステークな状況でも信頼性を示す

連合学習って便利だけど、データの信頼性も大事なんだね。TPFLフレームワークで信頼性が上がるなら、もっと安心して使える未来が来るかも！安全と信頼性の確保は重要だし、これからもどんな展開があるか楽しみだね。

**Comment:** 17 Pages with Appendix

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, 68T05, **投稿日時:** 2024-10-16 07:33

- - -

### [Advancing Healthcare: Innovative ML Approaches for Improved Medical Imaging in Data-Constrained Environments](http://arxiv.org/abs/2410.12245)

**医療の進展: データ制約下における革新的な医療画像のための機械学習アプローチ**

Al Amin, Kamrul Hasan, Saleh Zein-Sabatto, Liang Hong, Sachin Shetty, Imtiaz Ahmed, Tariqul Islam

- 医療分野では、希少疾患のサンプルが少ないため合成データが倫理やプライバシー問題を引き起こす
- CAT-U-Netフレームワークは少ないデータで医療画像の特徴抽出を強化し、患者プライバシーを保護
- フレームワークに追加された結合層とダウンサンプリングで、データ制約における学習能力が向上
- COVID-19や脳腫瘍、手首骨折のデータセットで98%の再構成精度と0.946に近いDice係数を達成

新しいCAT-U-Netが希少データ環境でこれだけ高い精度を叩き出せるって、すごくワクワクしない？珍しい病気でも正確に診断してくれる未来がもうすぐそこにありそう！

**Comment:** 7 pages, 7 figures

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-10-16 05:16

- - -

### [On A Scale From 1 to 5: Quantifying Hallucination in Faithfulness Evaluation](http://arxiv.org/abs/2410.12222)

**1から5のスケール：忠実性評価におけるハルシネーションの定量化**

Xiaonan Jing, Srinivas Billa, Danny Godbout

- 自然言語生成でのハルシネーションは、データ品質の低下や利用者の信頼喪失を招く問題である
- 大規模言語モデルを用いて生成物を定量化する信頼性評価の自動化を探求した
- 合成データ生成とハルシネーションの定量化手法を開発し、忠実性の評価に役立てた
- GPT-4が事実の一貫性において正確な判断と説明を提供し、NLIモデルの調整は性能向上に寄与する

自動で生成物の信頼性を評価するのって、未来のAIアプリこうなりそう！特にGPT-4がこんなに頼りにされているのは驚きだよね。ってことは、もっとAIを自由に正しい方法で使える時代が来るかも？

**Comment:** 14 pages, 13 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-10-16 04:36

- - -

### [fAmulet: Finding Finalization Failure Bugs in Polygon zkRollup](http://arxiv.org/abs/2410.12210)

**fAmulet: Polygon zkRollupにおける確定失敗バグの発見**

Zihao Li, Xinghao Peng, Zheyuan He, Xiapu Luo, Ting Chen

- ゼロ知識レイヤー2プロトコルはブロックチェーンのスケーラビリティ問題を解消する手法として注目。
- 本研究では初めて、ゼロ知識レイヤー2プロトコルの確定失敗バグを体系的に検討し、2つのバグを定義。
- fAmuletはPolygon zkRollup上でのバグ検出ツールで、ファジングテストを活用し効果的にバグを発見。
- fAmuletは12のゼロデイバグを検出し、Scroll zkRollupでもバグを特定、全て修正済み。

fAmuletって、バグを発見するための新しいツールなのがすごいな！しかも、複数のzkRollupプロトコルで使えるなんて、なんか万能な感じする～。もっと他のプロジェクトにも活用される未来が見えるね！

**Comment:** This submission serves as our full paper version with the appendix

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-10-16 04:06

- - -

### [Ranking with Multiple Objectives](http://arxiv.org/abs/2410.12139)

**複数の目的を持つランキング**

Nikhil R. Devanur, Sivakanth Gopi

- 検索や広告のランキングでは、複数の目的を同時に最大化する必要がある
- 各結果には目的に応じた異なるスコアが割り当てられる
- 結果をランキング順に重み付け集計し、任意の凹関数で最大化する手法を考案
- アルゴリズムは最適解と同等の結果を得るため、目的のバランスをとる助けとなる

この研究、目的のバランス取りが上手くできるってすごく興味深いよね！現実のデータで試行された結果が、LinkedInで実際に役立っているっていうのも面白そう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.DS, cs.DM, **投稿日時:** 2024-10-16 01:01

- - -

### [Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning](http://arxiv.org/abs/2410.12085)

**データ適応型差分プライベートプロンプト合成によるコンテキスト内学習**

Fengyu Gao, Ruida Zhou, Tianhao Wang, Cong Shen, Jing Yang

- LLMはコンテキスト情報に依存し、プライバシー漏洩のリスクを軽減する必要がある
- AdaDPSynは合成データ生成でプライバシーを守りつつ高いICL精度を実現
- データの統計的特性に応じてノイズレベルを調整し、差分プライバシーを保証
- Precision-Focused Iterative Radius Reductionでノイズを最小限に抑えつつ精度を維持

プライバシーを守りつつ高性能を維持するための技術ってすごくない？AIがもっと安心して使えるようになる未来が見えてわくわくしちゃうね！



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-10-15 22:06

- - -

### [WeatherDG: LLM-assisted Procedural Weather Generation for Domain-Generalized Semantic Segmentation](http://arxiv.org/abs/2410.12075)

**WeatherDG: 領域一般化セマンティックセグメンテーションのためのLLM支援手続型天気生成**

Chenghao Qian, Yuhu Guo, Yuhong Mo, Wenjing Li

- WeatherDGはStable Diffusionと大規模言語モデルを用いて多様な天候の運転画面画像を生成する
- LLMベースの手続型プロンプト生成法でシナリオ説明を豊かにし、詳細で多様な画像を自動生成
- バランス生成戦略により、さまざまな天候下で希少クラスの高品質オブジェクト生成を促進
- 合成データ適応により、既存のセグメンテーションモデルの一般化能力を向上させることが可能

WeatherDGってすごいよね！LLMとSDの協力で詳細な天候画像が生成されるなんて、運転シミュレーションとかの応用がさらに広がりそう！デモ見てみたいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-10-15 21:29

- - -

### [Differential Privacy on Trust Graphs](http://arxiv.org/abs/2410.12045)

**信頼グラフにおける差分プライバシー**

Badih Ghazi, Ravi Kumar, Pasin Manurangsi, Serena Wang

- 差分プライバシーを複数の参加者間で適用する研究で、各参加者は他の特定の参加者のみを信頼する設定に基づいている
- 信頼グラフを用いることで、従来のローカルモデルよりも優れたプライバシーとユーティリティのトレードオフを実現するアルゴリズムを提案
- さらに、知られていない最大$t$の隣接者に信頼を置かないロバストなバリアントについても研究し、そのためのアルゴリズムを提供
- プライベートな学習や分析タスクに関連する影響も議論し、提案するアルゴリズムを下限で補完

信頼ってめっちゃ大事だよね。でもデータをどう守るかも重要！この論文、まだまだ広がりそうで楽しみだな。プライバシーとトレードオフで良い解決方法がどんどん増えていくといいな～。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, cs.LG, cs.SI, **投稿日時:** 2024-10-15 20:31

- - -

### [A Survey on Deep Tabular Learning](http://arxiv.org/abs/2410.12034)

**深層タブラー学習の調査**

Shriyank Somvanshi, Subasish Das, Syed Aaqib Javed, Gian Antariksa, Ahmed Hossain

- タブラーデータは異質的で空間構造に欠けるため、深層学習の挑戦が続く。
- SAINTやTabNetなどの先進的モデルは、注意機構を駆使して性能と計算効率を両立。
- ハイブリッド構造であるTabTransformerは、カテゴリ・数値データを処理可能にする。
- グラフベースや拡散モデルはデータの過少を補完し、特徴表現を向上させる。

タブラー学習って地味なイメージだけど、いろんなモデルが工夫されてて面白そうに感じる。新しいテクノロジーで進化してるこの分野、私たちも勉強続けてついていかなきゃね！

**Comment:** 43 pages, 18 figures, 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-10-15 20:08

- - -

### [EmotionCaps: Enhancing Audio Captioning Through Emotion-Augmented Data Generation](http://arxiv.org/abs/2410.12028)

**EmotionCaps: 感情強化データ生成による音声キャプションの強化**

Mithun Manivannan, Vignesh Nethrapalli, Mark Cartwright

- 音声キャプション生成で合成データの使用が進展しているが、音の感情情報の活用は未開拓。
- 感情認識情報を用いたEmotionCapsデータセットを構築し、感情強化キャプションを生成。
- 音声の感情トーンに合わせた高品質なキャプションを提供し、モデルの性能向上を狙う。
- EmotionCapsを用いたモデルと基準モデルを比較し、キャプションモデル開発に新方向を提示。

感情情報を取り入れた音声キャプションって、すごくリアルな記述になりそうでワクワクしちゃう！技術がどんどん感情にも優しい方向に進化していくの、楽しい未来が待ってそうだよね！🌟



**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.LG, eess.AS, eess.SP, **投稿日時:** 2024-10-15 19:57

- - -

### [Age-of-Gradient Updates for Federated Learning over Random Access Channels](http://arxiv.org/abs/2410.11986)

**ランダムアクセスチャネル上の連合学習のための勾配更新年齢**

Yu Heng Wu, Houman Asgari, Stefano Rini, Andrea Munari

- ランダムアクセスチャネルで深層ニューラルネットワークの訓練を連合学習で行う問題を研究
- 勾配更新の新しいポリシー「勾配の鮮度」が提案され、informationの年齢に類似した解釈
- トップ-Kスパーシフィケーションとメモリー蓄積を用いた勾配圧縮と誤差修正戦略を設計
- 数値シミュレーションで、新ポリシー「Age-of-Gradient」が他のポリシーに比べて優れた性能

このアプローチ、勾配の「鮮度」っていうアイデア、面白そう！やっぱり通信とか連合学習って難しいけど、みんなが使いやすくなるといいなって思うよね。どんなふうに実際に役立つのか、ちょっと気になる！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-10-15 18:49

- - -

### [Integrating Artificial Intelligence Models and Synthetic Image Data for Enhanced Asset Inspection and Defect Identification](http://arxiv.org/abs/2410.11967)

**人工知能モデルと合成画像データを統合した資産検査と欠陥識別の強化**

Reddy Mandati, Vladyslav Anderson, Po-chen Chen, Ankush Agarwal, Tatjana Dokic, David Barnard, Michael Finn, Jesse Cromer, Andrew Mccauley, Clay Tutaj, Neha Dave, Bobby Besharati, Jamie Barnett, Timothy Krall

- 従来は現場での検査に依存していたが、最近はドローンによる検査が主流に
- 合成欠陥画像と手動ラベル付きドローン画像を組み合わせた新しいソリューションを提案
- 合成画像が、現実のまれな欠陥のリアルな再現と検査精度の向上を可能に
- データセットの複合で、欠陥検出の精度73%、資産検出モデルの精度92%を達成

この研究、すごく面白そう！現場で見つけづらいまれな欠陥も検出できちゃうなんて、ドローンと合成データの力やばいね。画像の精度も上がって、めっちゃ効率的になりそう。もっと詳しく知りたいなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-10-15 18:14

- - -

### [CtrlSynth: Controllable Image Text Synthesis for Data-Efficient Multimodal Learning](http://arxiv.org/abs/2410.11963)

**CtrlSynth: データ効率の良いマルチモーダル学習のための制御可能な画像テキスト合成**

Qingqing Cao, Mahyar Najibi, Sachin Mehta

- マルチモーダル基盤モデルの事前学習には大規模なデータセットが必要だが、これにはノイズや誤ったデータが含まれる可能性がある。
- 以前の研究では合成サンプルを生成してデータセットを拡張するが、特定のドメインに限定され多様性が低い。
- CtrlSynthは、画像の視覚的意味を基本要素に分解して操作し、画像やテキストを合成する制御可能なパイプラインを設計。
- 31種類のデータセットによる実験で、CtrlSynthがゼロショット分類や画像テキスト検索などでCLIPモデルの性能を向上させると示された。

CtrlSynthは未来のマルチモーダル学習によさそう！基本要素を自由に操れるなんて、もっと楽しく勉強できそうだよね！これが普及したら私たちももっと多様な教材で学べるかも。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-10-15 18:06
