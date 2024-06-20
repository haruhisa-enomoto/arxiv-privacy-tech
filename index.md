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

更新: 2024-06-20T04:17:54.951432

- - -

### [Synergizing Foundation Models and Federated Learning: A Survey](http://arxiv.org/abs/2406.12844)

**基盤モデルと連合学習の融合：調査**

Shenghui Li, Fanghua Ye, Meng Fang, Jiaxu Zhao, Yun-Hin Chan, Edith C. -H. Ngai, Thiemo Voigt

- 基盤モデル（大型言語モデル、視覚トランスフォーマ、マルチモーダルモデル）が学術界と産業界に大きな影響を与えている
- 小規模モデルと比較して、基盤モデルはプレトレーニングフェーズで大量のデータを必要とする
- 一般的な基盤モデルはインターネットから収集したデータでプレトレーニング可能だが、ドメイン固有の基盤モデルは専有データが必要でプライバシーの問題が発生
- 連合学習は、異なる参加者からのデータの可用性の壁を破り、プライバシーを保護しながら分散データセットを使用した基盤モデルのカスタマイズと適応を可能にする

基盤モデルと連合学習を組み合わせることで、様々なドメインに特化した強力なモデルがプライバシーを守りながら構築できるようになるんだよね。最新技術がどのようにプライバシーとデータ利用のバランスを取るか、これからの発展が楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-18 17:58

- - -

### [Neural Approximate Mirror Maps for Constrained Diffusion Models](http://arxiv.org/abs/2406.12816)

**制約付き拡散モデルのためのニューラル近似ミラーマップ**

Berthy T. Feng, Ricardo Baptista, Katherine L. Bouman

- 拡散モデルは視覚的に説得力のある画像を生成するが、データの微妙な制約を満たすのは困難
- 制約には物理ベース、幾何学的、意味的なものがあり、制約を満たすことでモデルの精度が向上する
- 現行手法は制約の柔軟性に欠けるが、ニューラル近似ミラーマップ（NAMMs）を提案
- NAMMsは学習したミラー空間と逆マップを使い、制約を満たした状態でデータを生成できる

物理ベースから意味的な制約まで柔軟に対応できるNAMMsのアプローチ、期待値高いかも！制約問題のソルバーも簡単に応用できるって、すごく使えそうだよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CV, eess.IV, **投稿日時:** 2024-06-18 17:36

- - -

### [Privacy Preserving Federated Learning in Medical Imaging with Uncertainty Estimation](http://arxiv.org/abs/2406.12815)

**医療画像における不確実性推定を伴うプライバシー保護型連合学習**

Nikolas Koutsoubis, Yasin Yilmaz, Ravi P. Ramachandran, Matthew Schabath, Ghulam Rasool

- 連合学習（FL）はプライバシー保護の下で機械学習モデルの訓練を可能にする
- 患者データのプライバシー問題が大規模な訓練データセットの構築を妨げている
- 不確実性推定がFLにおいて重要であり、データの異質性が課題となる
- 現行研究の調査とともに、プライバシー向上とノイズの多い医療画像データの課題解決の方向性を提案

医療分野での連合学習の重要性が分かるね！これからの研究がどのようにプライバシーを守りつつ精度を上げていけるのかに注目したい。

**Comment:** 31 pages, 5 figures, 3 tables, Journal preprint

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, eess.IV, stat.ML, **投稿日時:** 2024-06-18 17:35

- - -

### [In-Context Learning of Energy Functions](http://arxiv.org/abs/2406.12785)

**エネルギー関数のインコンテキスト学習**

Rylan Schaeffer, Mikail Khona, Sanmi Koyejo

- インコンテキスト学習は、最先端のAIモデルの成功を支える強力な能力
- 今回の研究で、モデルの制約なしにエネルギー関数を学習する新しい方法を提案
- 我々の手法は、合成データでの実験で実証されている
- 入力空間と出力空間が異なる場合でも機能する初の例として示唆

新しい視点でインコンテキスト学習の可能性を広げているところが面白い！これからのAIの応用範囲がますます広がりそうだね。

**Comment:** Proceedings of the 1st Workshop on In-Context Learning at the 41st   International Conference on Machine Learning, Vienna, Austria. 2024. arXiv   admin note: text overlap with arXiv:2402.10202

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-18 16:54

- - -

### [Can Large Language Models Code Like a Linguist?: A Case Study in Low Resource Sound Law Induction](http://arxiv.org/abs/2406.12725)

**大規模言語モデルは言語学者のようにコードできるか？低リソース音声法則の導入に関するケーススタディ**

Atharva Naik, Kexun Zhang, Nathaniel Robinson, Aravind Mysore, Clayton Marr, Hong Sng Rebecca Byrnes, Anna Cai, Kalvin Chang, David Mortensen

- 歴史言語学者は、親言語の再構築された単語を子孫言語に変換するプログラムを書く
- プログラム作成はエラーが多く時間がかかるため、方法の改善が求められている
- 大規模言語モデル（LLM）を使い、音声変化例からPythonの音声法則プログラムを生成する方法を提案
- LLMの効果を評価し、既存の自動音声法則導入方法と比較すると、LLMがそれらの弱点を補うことができる

音の変化をPythonでプログラムにするなんて面白い！これから言語学もAIがどんどん手伝ってくれるようになりそうでワクワクするね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-06-18 15:46

- - -

### [GeoBench: Benchmarking and Analyzing Monocular Geometry Estimation Models](http://arxiv.org/abs/2406.12671)

**GeoBench: 単眼幾何推定モデルのベンチマークと分析**

Yongtao Ge, Guangkai Xu, Zhiyue Zhao, Libo Sun, Zheng Huang, Yanlong Sun, Hao Chen, Chunhua Shen

- 判別的な単眼幾何推定モデルは、大規模な微調整データに依存してゼロショット一般化を実現
- 生成ベースのパラダイムでは、事前学習された拡散モデルと合成トレーニングデータの微調整で見事な一般化性能を発揮
- 既存の幾何評価ベンチマークにはシーンの多様性やラベル品質の欠如などの欠点がある
- 微調整データの品質が、データスケールやモデルアーキテクチャよりも重要であることが判明

シンプルなDINOv2だけで最先端を達成できるなら、複雑な生成モデルいらないかもね？この研究、将来の幾何推定の進展に貢献しそう！

**Comment:** https://github.com/aim-uofa/GeoBench

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-18 14:44

- - -

### [Federated Learning with a Single Shared Image](http://arxiv.org/abs/2406.12658)

**連合学習における単一の共有画像の利用**

Sunny Soni, Aaqib Saeed, Yuki M. Asano

- 連合学習はプライベートなトレーニングデータ共有を避け、モデルを協同で訓練する技術
- 既存のFedDFは共通の共有データセットを使用するが、これはプライバシーやストレージの問題で困難
- 本研究では、クライアント間とサーバー間で単一の共有画像のみを使用する新たな知識蒸留法を提案
- 新しい適応型データセットプルーニングアルゴリズムにより、単一画像から最も情報価値の高い切り取り範囲を選択

一枚の画像で全体の連合学習がより効果的に行えるなんて革新的だね！異なるクライアントアーキテクチャも対応できるのはすごい未来な感じ。

**Comment:** 8 Pages, 3 Figures, Appendix 4 Pages, CVPRW 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-06-18 14:26

- - -

### [UIFV: Data Reconstruction Attack in Vertical Federated Learning](http://arxiv.org/abs/2406.12588)

**UIFV: 垂直連合学習におけるデータ再構築攻撃**

Jirui Yang, Peng Chen, Zhihui Lu, Qiang Duan, Yubing Bao

- 垂直連合学習（VFL）は、生データを共有せずに協調機械学習を行う手法である
- 既存のデータ再構築方法はモデルや勾配情報に依存し、VFL適用には限界がある
- 本研究では、UIFVという新しい方法を提案し、中間特徴データを用いて元データを再構築する
- 実験では、提案手法が最先端技術よりも高い攻撃精度を示し、VFLのプライバシーの脆弱性を明らかにした

データ共有なしで協力するのに、まだこんな抜け道があるなんてビックリ！UIFVのような新しい方法で、もっとプライバシーを守れる方法が必要だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, stat.ML, **投稿日時:** 2024-06-18 13:18

- - -

### [Low-Resource Machine Translation through the Lens of Personalized Federated Learning](http://arxiv.org/abs/2406.12564)

**パーソナライズド連合学習による低リソース機械翻訳へのアプローチ**

Viktor Moskvoretskii, Nazarii Tupitsa, Chris Biemann, Samuel Horváth, Eduard Gorbunov, Irina Nikishina

- MeritFedアルゴリズムに基づく新しいアプローチを提案
- 低リソース機械翻訳のタスクに適用し、その有効性を検証
- 訓練に使用する各言語の影響を追跡できるため、MeritFedは非常に解釈可能
- ターゲットデータセットのサイズ、関連性のない言語の影響、および補助最適化パラメータの効果を分析

MeritFedって、低リソース言語の機械翻訳にも使えるんだね！異なる言語の影響を追跡できるって、かなり役立ちそう💡

**Comment:** 18 pages, 7 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-06-18 12:50

- - -

### [Update Selective Parameters: Federated Machine Unlearning Based on Model Explanation](http://arxiv.org/abs/2406.12516)

**更新選択パラメータ: モデル説明に基づく連合機械学習のアンラーニング**

Heng Xu, Tianqing Zhu, Lefeng Zhang, Wanlei Zhou, Philip S. Yu

- 機械アンラーニングが必要な理由は、特定のトレーニングデータの影響をモデルから除去するため
- 現行の中央集権的なアンラーニング手法では連合学習に不向きであり、全データへのアクセスが前提となる
- 新たな手法はモデル説明に基づき、重要なチャネルのみを調整してデータの影響を削減
- 提案手法は計算コストと通信コストを削減しつつ、モデルの性能を維持することを実験で実証

この論文は連合学習の新しいアプローチだね！モデル説明を活用するアイデア、とってもクールじゃない？

**Comment:** Accepted by IEEE Transactions on Big Data

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, cs.LG, **投稿日時:** 2024-06-18 11:43

- - -

### [The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions](http://arxiv.org/abs/2406.12480)

**オンライン政治討論における立場検出のためのLLM生成の合成データの力**

Stefan Sylvius Wagner, Maike Behrendt, Marc Ziegele, Stefan Harmeling

- 立場検出は議論の要約、誤情報の検出、意見分布の評価に有用
- トランスフォーマーモデルは多くのデータを必要とするが、オンライン討論の多様性がデータ収集を難しくする
- Mistral-7Bモデルで生成した合成データで立場検出エージェントのパフォーマンスを向上
- 合成データと未ラベルデータの最も情報量豊富なサンプルを組み合わせることで、ラベリング労力を軽減しベースラインモデルを超える成果を達成

LLMによる合成データでラベリングの手間が減ってパフォーマンスも向上するなんて、すごく画期的じゃない？特に多様な議論の場では大きな助けになるね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-06-18 10:36

- - -

### [Federated Learning with Limited Node Labels](http://arxiv.org/abs/2406.12435)

**ラベルの限定されたノードを持つ連合学習**

Bisheng Tang, Xiaojun Chen, Shaopu Wang, Yuexin Xuan, Zhendong Zhao

- 分散グラフ構造データを扱うための手法として、サブグラフ連合学習（SFL）が注目を集めている
- SFLの一部モデルは、サブグラフ間の欠落エッジの重要性を見落とし、ローカルGNNがグローバル表現を他のパーティのGNNに渡せなくなる
- 既存のSFLモデルは多くのラベル付きデータを必要とし、実用性を制限している
- 提案する新たなSFLフレームワークFedMpaは、少量のデータでMLPモデルを訓練し、連合特徴をローカル構造に伝播

新しいSFLフレームワークが実用性を高める方法についての研究なんて面白そうだね！将来的にもっと現実の応用が増えるかもって感じだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-06-18 09:30

- - -

### [Deep Temporal Deaggregation: Large-Scale Spatio-Temporal Generative Models](http://arxiv.org/abs/2406.12423)

**深層時系列デアグリゲーション: 大規模時空間生成モデル**

David Bergström, Mattias Tiger, Fredrik Heintz

- 時系列データはセンサーや取引システムから生成され、プライバシーとビジネス感受性が課題
- 従来の方法は短いシーケンスと小規模なデータに限られ、大規模データには不向き
- 本研究では、TDDPMというトランスフォーマーベースの拡散モデルを提案し、性能とスケーラビリティを向上
- 新たな包括的ベンチマークで評価し、事前の空間占有周波数情報に基づくモビリティデータ生成を実現

大規模な時系列データを活用して、都市の動きがシミュレートされるの楽しそう！特に、未知の環境でも適応できるなんてすごいね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-18 09:16

- - -

### [Unveiling the Flaws: Exploring Imperfections in Synthetic Data and Mitigation Strategies for Large Language Models](http://arxiv.org/abs/2406.12397)

**欠点の解明：合成データの不完全性と大規模言語モデルの緩和戦略の探求**

Jie Chen, Yupeng Zhang, Bingning Wang, Wayne Xin Zhao, Ji-Rong Wen, Weipeng Chen

- 高品質データの不足を補うため、合成データが提案されている
- 合成データはモデルの性能を改善するが、パターンオーバーフィッティングの課題あり
- Q-Aペアに関連する特定の欠点を解析し、アンラーニング技術を提案
- 提案手法は、低コストで性能を維持しつつ、指示追従問題を緩和

合成データを使うとこういう困ったがあるんだね。でも新しい手法で改善できるなら、試してみる価値ありそう！未来のAIがもっと賢くなりそう～。

**Comment:** 15 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-18 08:38

- - -

### [Security and Privacy of 6G Federated Learning-enabled Dynamic Spectrum Sharing](http://arxiv.org/abs/2406.12330)

**6G連合学習対応動的スペクトル共有のセキュリティとプライバシー**

Viet Vo, Thusitha Dayaratne, Blake Haydon, Xingliang Yuan, Shangqi Lai, Sharif Abuadbba, Hajime Suzuki, Carsten Rudolph

- 6G無線通信における動的スペクトル共有が重要
- 連合学習によるスペクトルセンシング技術が注目を集める
- 協調トレーニングの整合性とローカルユーザのスペクトル情報のプライバシーが未解決
- 実践的な攻撃ベクトルと防御の指針を提示

連合学習でプライバシーを保ちながら6Gの通信をより効率的にするなんて、未来のネットワークがもっと便利になりそうでワクワクする！新しいテクノロジーでどんな日常が来るのか、楽しみだね。

**Comment:** 7 pages, 5 figures. The paper is submitted to IEEE Networks for   review

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, cs.ET, cs.LG, cs.NI, **投稿日時:** 2024-06-18 06:54

- - -

### [BadSampler: Harnessing the Power of Catastrophic Forgetting to Poison Byzantine-robust Federated Learning](http://arxiv.org/abs/2406.12222)

**BadSampler: カタストロフィックフォゲッティングの力を利用したビザンチン耐性連合学習の毒殺攻撃**

Yi Liu, Cong Wang, Xingliang Yuan

- ビザンチン耐性の連合学習における毒殺攻撃の研究がほとんど行われていない
- 本論文では、カタストロフィックフォゲッティングを利用した新たな攻撃BadSamplerを提案
- Clean-labelデータのみを使用し、モデルの一般化誤差を最大化するように訓練データを選択
- 提案手法の有効性と性能を二つの実データセットで評価し、効率的な攻撃が可能であることを示した

これ、めっちゃ興味深いね！毒殺攻撃とか、まるでスパイ映画みたいだし、連合学習がもっと強くなるかもってワクワクするね。

**Comment:** In Proceedings of the 30th ACM SIGKDD Conference on Knowledge   Discovery and Data Mining (KDD' 24), August 25-29, 2024, Barcelona, Spain

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-06-18 02:43

- - -

### [SFedCA: Credit Assignment-Based Active Client Selection Strategy for Spiking Federated Learning](http://arxiv.org/abs/2406.12200)

**SFedCA: スパイキング連合学習のための信用配分に基づくアクティブクライアント選択戦略**

Qiugang Zhan, Jinbo Cao, Xiurui Xie, Malu Zhang, Huajin Tang, Guisong Liu

- スパイキング連合学習は、デバイスが局所データを交換せず低消費電力で協力して学習する
- プライバシー保護機能とエネルギー効率を兼ね備え、マルチメディアデータ処理に革命をもたらす可能性
- 既存手法はクライアントの無作為選択に依存し、統計的異質性がグローバルモデルの収束や精度に影響
- SFedCAは閾値に基づきクライアントを選定し、データ分布のバランスを維持。また、通信ラウンド数を減らすことに成功

この技術で低消費電力で効率的に学習できるとか、未来のガジェットがすごくスマートになりそう！早く実用化されるといいね。

**Comment:** 9 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.ET, cs.MM, cs.NE, **投稿日時:** 2024-06-18 01:56

- - -

### [LLMs Are Prone to Fallacies in Causal Inference](http://arxiv.org/abs/2406.12158)

**LLMは因果推論において誤謬を犯しやすい**

Nitish Joshi, Abulhair Saparov, Yixin Wang, He He

- LLMは事前学習データから因果関係を抽出できるが、記憶に依存する可能性がある
- 合成データを用いて因果関係の推論能力を検証した結果、LLMはテキスト中の順序から因果関係を推論しがち
- 時系列関係（XがYの前に発生）でも同様の誤謬を示すことが多い
- 反事実的な関係から因果関係を推論するのが困難であり、因果性の理解に疑問が残る

LLMって便利だけど、因果関係の推論はまだまだ課題が多いみたい。テンプレから外れた状況でも柔軟に対応できるようになるといいな！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-06-18 00:14

- - -

### [ChatEMG: Synthetic Data Generation to Control a Robotic Hand Orthosis for Stroke](http://arxiv.org/abs/2406.12123)

**ChatEMG：脳卒中の手の装具を制御するための合成データ生成**

Jingxi Xu, Runsheng Wang, Siqi Shang, Ava Chen, Lauren Winterbottom, To-Liang Hsu, Wenxi Chen, Khondoker Ahmed, Pedro Leandro La Rotta, Xinyue Zhu, Dawn M. Nilsen, Joel Stein, Matei Ciocarlie

- 障害を持つ被験者からのデータ収集の困難さにより、手の装具での意図推定が困難
- EMG信号は条件、セッション、被験者ごとに大きな変動があり、分類器の一般化が難しい
- ChatEMGはプロンプトに基づいて合成EMG信号を生成し、少量のデータを拡張
- 合成データは分類器に依存せず、意図推定精度を向上させ、機能的な装具支援作業に利用可能

合成データで意図推定をサポートするのってすごくない？新しい被験者でもすぐに活用できちゃうとか、未来のリハビリは明るい感じがするなぁ！

**Comment:** 8 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.AI, cs.LG, **投稿日時:** 2024-06-17 22:04

- - -

### [Centering Policy and Practice: Research Gaps around Usable Differential Privacy](http://arxiv.org/abs/2406.12103)

**政策と実践の中心化：使いやすい差分プライバシーに関する研究のギャップ**

Rachel Cummings, Jayshree Sarathy

- 差分プライバシーは理論的に非常に強力だが、実践には大きな課題がある
- 実世界での利用可能性を向上させるためには、研究者と実務家の協力が必要
- ユーザーのニーズに合わせたリスクフレームワークの開発が提案されている
- ユーザーインターフェースの投資やアルゴリズム監査が重要な改善点である

理論だけじゃなくて実践も大事って視点が新鮮！みんなのための差分プライバシーが早く実現するといいな。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.CY, cs.HC, **投稿日時:** 2024-06-17 21:32

- - -

### [Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts](http://arxiv.org/abs/2406.12034)

**Self-MoE: 自己特化型専門家を備えた構成可能な大規模言語モデルに向けて**

Junmo Kang, Leonid Karlinsky, Hongyin Luo, Zhen Wang, Jacob Hansen, James Glass, David Cox, Rameswar Panda, Rogerio Feris, Alan Ritter

- モノリシックなLLMを自己特化型専門家によるモジュールシステムに変換するアプローチであるSelf-MoEを提案
- 自己生成の合成データを用いて専門家モジュールを構築し、自己最適化ルーティングを組み込む
- 人間のラベル付けデータや追加パラメータなしで、動的かつ能力特化型のタスク処理が可能
- 多様なベンチマークで基盤LLMを上回る性能を示し、モジュール性と自己改善の重要性を示す

自己改善のアイデアがすごくおもしろそう！もっと効率的で柔軟なAIシステムが実現できる可能性、大きいよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-06-17 19:06

- - -

### [P3GNN: A Privacy-Preserving Provenance Graph-Based Model for APT Detection in Software Defined Networking](http://arxiv.org/abs/2406.12003)

**P3GNN: ソフトウェア定義ネットワーキングにおけるAPT検出のためのプライバシー保護型プロベナンスグラフベースモデル**

Hedyeh Nazari, Abbas Yazdinejad, Ali Dehghantanha, Fattane Zarrinkalam, Gautam Srivastava

- SDNはネットワーク管理に進展をもたらしたが、APTやゼロデイ攻撃の脅威も増加
- 既存の対策は新しい脅威の検出や共同学習中のデータプライバシーの問題に不十分
- P3GNNは連合学習と準同型暗号を組み合わせ、データ機密性と勾配の整合性を強化
- 無監督学習で攻撃を検知し、DARPA TCE3データセットで高い精度と低い誤検知率を実現

連合学習と準同型暗号の組み合わせってすごいね！これなら新しい脅威にも対応できるから安心じゃん？



**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-17 18:14
