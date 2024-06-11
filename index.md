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

更新: 2024-06-11T04:21:47.032779

- - -

### [Decentralized Personalized Federated Learning](http://arxiv.org/abs/2406.06520)

**分散型個別化連合学習**

Salma Kharrat, Marco Canini, Samuel Horvath

- 分散型連合学習におけるデータの異質性と通信制限の課題に取り組む
- クライアントが適切な協力者を選ぶためのコラボレーショングラフを作成
- 資源効率を高め、通信オーバーヘッドを最小限に抑える新しい戦略を採用
- DPFLはさまざまなデータセットで優れた性能を示し、他の手法を上回る

データが異質でも効率的に協力できるなんてすごいね！将来への期待が高まるな〜。これは連合学習をさらに実用化するステップになるかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CV, cs.MA, math.OC, **投稿日時:** 2024-06-10 17:58

- - -

### [Differentially Private Best-Arm Identification](http://arxiv.org/abs/2406.06408)

**差分プライベートな最良腕同定**

Achraf Azize, Marc Jourdan, Aymen Al Marjani, Debabrota Basu

- データプライバシーを重視した最良腕同定（BAI）の課題に焦点を当てた
- バウンドの低下により、高プライバシーと低プライバシーの二つのプライバシーレジームが存在する
- 提案するCTB-TTとAdaP-TT*は、それぞれ$\epsilon$-ローカルDPと$\epsilon$-グローバルDPを満たす
- CTB-TTはランダム化応答に基づき、AdaP-TT*はラプラスノイズを追加することでプライバシーと有用性のトレードオフを実現する

プライバシーを保ちながら精度を上げる新しいアルゴリズムの提案がめっちゃ興味深いね。これでデータも安心して使えそうだから未来の研究にも期待が持てるかも！

**Comment:** arXiv admin note: substantial text overlap with arXiv:2309.02202

**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.CR, cs.LG, math.ST, stat.TH, **投稿日時:** 2024-06-10 16:02

- - -

### [Optimisation of federated learning settings under statistical heterogeneity variations](http://arxiv.org/abs/2406.06340)

**統計的不均一性変動下における連合学習設定の最適化**

Basem Suleiman, Muhammad Johan Alibasa, Rizka Widyarini Purwanto, Lewis Jeffries, Ali Anaissi, Jacky Song

- 連合学習は、中央でモデルパラメータを共有することで協力して学習
- 統計的不均一性により、デバイスごとのデータ分布が独立同分布で異なる
- データ分割戦略とメトリックを提案し、異なる統計的不均一性をシミュレート
- 最適なFLモデルとパラメータを特定し、推奨ガイドラインを提供

連合学習の最適化って、けっこうデータのばらつきに左右されるんだね。うまく使えばいろんな場面で役立ちそう！

**Comment:** 27 pages, 17 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-10 15:01

- - -

### [Statistical Inference for Privatized Data with Unknown Sample Size](http://arxiv.org/abs/2406.06231)

**未知のサンプルサイズを持つプライバタイズされたデータの統計的推論**

Jordan Awan, Andres Felipe Barrientos, Nianqiao Ju

- サンプルサイズを含むプライバタイズされたデータを解析する理論とアルゴリズムを開発
- 無限サンプルサイズで無限差分プライバシーと有限差分プライバシーの距離がゼロになることを証明
- 無限差分プライバシーにおける最大対数尤度推定が有限差分プライバシーに収束することを示す
- 有限サンプルのベイズ推論のためにリバーシブルジャンプMCMCおよびMonte Carlo EMアルゴリズムを提案

特にサンプルサイズまでプライバタイズしちゃうなんて、データの秘密保持がすごく厳しいね！研究が進めばもっと安全で信頼できるデータ分析ができそうだね。

**Comment:** 20 pages before references, 40 pages in total, 4 figures, 3 tables

**トピック:** [差分プライバシー](dp), **カテゴリ:** math.ST, cs.CR, stat.CO, stat.TH, **投稿日時:** 2024-06-10 13:03

- - -

### [Lurking in the shadows: Unveiling Stealthy Backdoor Attacks against Personalized Federated Learning](http://arxiv.org/abs/2406.06207)

**影に潜む: パーソナライズド連合学習に対するステルス性バックドア攻撃の解明**

Xiaoting Lyu, Yufei Han, Wei Wang, Jingkai Liu, Yongsheng Zhu, Guangquan Xu, Jiqiang Liu, Xiangliang Zhang

- パーソナライズド連合学習（PFL）は各クライアントが個別のローカルモデルを作成できるように設計されている
- PFLの個別化プロセスがバックドア中毒効果を希釈することができ、防御機構を使用して強化可能
- 提案された\textit{PFedBA}攻撃戦略は、主学習タスクとバックドア学習タスクを巧妙に一致させる
- \textit{PFedBA}は10種の最新PFLアルゴリズム全てで高い攻撃性能を示し、6種の既存防御を突破

PFLは連合学習の次のステップみたいだけど、それでもまだまだ安全性に課題がいっぱいだね〜。\textit{PFedBA}のやり方、すごく巧妙だけどちょっと怖いかも！

**Comment:** Accepted by Usenix Security 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-10 12:14

- - -

### [Federated learning in food research](http://arxiv.org/abs/2406.06202)

**フードリサーチにおける連合学習**

Zuzanna Fendor, Bas H. M. van der Velden, Xinxin Wang, Andrea Jr. Carnoli, Osman Mutlu, Ali Hürriyetoğlu

- フードリサーチはデータ共有の障害（データ所有、プライバシー、規制）により制約されやすい
- データ共有の障害を軽減するために、ローカルデータを使いモデルをトレーニングする連合学習が提案されている
- 水とミルクの品質評価、サイバーセキュリティ、農薬リスク分析、雑草検出、不正検出の例が含まれる
- 知識ギャップとして縦型/転送連合学習と分散アーキテクチャの不足が指摘されている

フードリサーチに連合学習を取り入れることで、より多くのデータを活用できる可能性が熱いね！技術の進展が楽しみだなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-10 11:58

- - -

### [DiffInject: Revisiting Debias via Synthetic Data Generation using Diffusion-based Style Injection](http://arxiv.org/abs/2406.06134)

**DiffInject: 拡散ベースのスタイル注入を用いた合成データ生成によるバイアス除去の再考**

Donggeun Ko, Sangwoo Jo, Dongjun Lee, Namjun Park, Jaekwang Kim

- データセットバイアスは機械学習の重大な課題であり、特定の属性（例：画像のテクスチャや色）が意図せず学習され、性能が低下する
- これまでのバイアス除去には新しいアルゴリズムの開発や合成データ生成が試みられてきたが、バイアス特定のサンプルが少なすぎるという問題があった
- DiffInjectは、事前学習済みの拡散モデルを使用して合成バイアスコンフリクトサンプルを増強するシンプルだが強力な方法である
- 提案手法はバイアスの種類やラベリングの明示的な知識を必要とせず、完全に教師なしの設定でデータセットバイアスの効果的な削減を実現する

この方法って、事前知識なくバイアスを取り除けるなんてすごいね！実際のデータセットのバイアス問題解決がもっと簡単になりそう。

**Comment:** 10 pages (including supplementary), 3 figures, SynData4CV@CVPR 24   (Workshop)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-06-10 09:45

- - -

### [ProcessPainter: Learn Painting Process from Sequence Data](http://arxiv.org/abs/2406.06062)

**ProcessPainter: シーケンスデータから絵画プロセスを学ぶ**

Yiren Song, Shijie Huang, Chen Yao, Xiaojun Ye, Hai Ci, Jiaming Liu, Yuxuan Zhang, Mike Zheng Shou

- 画家の絵画プロセスは段階的であり、画家やスタイルによって大きく異なる
- 従来の描画方法では、アーティストの本物のプロセスを再現するのに限界がある
- ProcessPainterはテキストから絵画プロセスを生成する初の試みである
- Artwork Replication Networkは、任意のフレーム入力を受け付けることで制御可能な絵画プロセス生成を実現する

絵画プロセスをテキストから生成するなんてすごい！これが美術教育にどう役立つか、もっと知りたいな。未来のアーティストには、新しい創作の道具になるかも！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-06-10 07:18

- - -

### [Contrastive Learning from Synthetic Audio Doppelgangers](http://arxiv.org/abs/2406.05923)

**合成音声ドッペルゲンガーによる対照学習**

Manuel Cherep, Nikhil Singh

- 現実世界の音声データセットの代わりに合成音声を使い、堅牢な音声表現を学習
- 音声シンセサイザーのパラメータをランダムに変更して合成音声のペアを生成
- 合成音声の変動により豊富な対照情報を提供し、実データ並みの性能を達成
- 軽量でデータ保存が不要、単一のハイパーパラメータのみを使用

面白そうなポイントは、合成音声を使うことでデータ収集の負担が減るところ。リアルな音声データなくても高い精度が出せるなら、環境にも優しいかもね！

**Comment:** 17 pages, 6 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.LG, eess.AS, **投稿日時:** 2024-06-09 21:44

- - -

### [Comments on "Federated Learning with Differential Privacy: Algorithms and Performance Analysis"](http://arxiv.org/abs/2406.05858)

**「連合学習と差分プライバシー：アルゴリズムとパフォーマンス分析」に関するコメント**

Mahtab Talaei, Iman Izadi

- Weiらの論文における連合学習の差分プライバシーアルゴリズムの収束性能が対象
- 提案された差分プライバシーアルゴリズムはNoising before Model Aggregation FL (NbAFL)と呼ばれる
- 元の論文のNbAFLの収束上限（定理2）が誤っていると指摘
- 正しい収束上限をこのコメントで提示することが目的

収束性能の上限が修正されて正確になったみたい。これでNbAFLがもっと効果的に使えるようになるから、注目されそうだね！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.DC, cs.CR, cs.PF, **投稿日時:** 2024-06-09 17:03

- - -

### [Heterogeneous Treatment Effects in Panel Data](http://arxiv.org/abs/2406.05633)

**パネルデータにおける不均一な処置効果**

Retsef Levi, Elisabeth Paulson, Georgia Perakis, Emily Zhang

- パネルデータの構造を活用しない既存手法や処置パターンに制限がある
- 観察データを同様の処置効果を持つクラスタに分割する新手法を提案
- パネルデータの低ランク構造を活用してクラスタごとの平均処置効果を推定
- セミ合成データでの実験で精度が向上、回帰木のリーフ数は40以下

パネルデータっていろいろなところで使えるから、この手法って結構応用範囲広そう！セミ合成データでの実験だけど、実際に使うのが楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, econ.EM, **投稿日時:** 2024-06-09 04:02

- - -

### [CCSI: Continual Class-Specific Impression for Data-free Class Incremental Learning](http://arxiv.org/abs/2406.05631)

**CCSI: データ不要のクラス増加学習のための継続的クラス特定インプレッション**

Sana Ayromlou, Teresa Tsang, Purang Abolmaesumi, Xiaoxiao Li

- 従来の深層学習は全ての疾病クラスサンプルを要し、新規疾病の診断が困難
- クラス増加学習は既存モデルに新疾病を適応させるが、昔のクラスのパフォーマンスが低下
- 提案手法は合成データを使用しデータ保存不要とし、プライバシー・ストレージ問題を解決
- 合成データと新疾病データの組み合わせ、多様な損失関数導入でバランス悪化を防止

データ不要で新しい疾病に対応できるなんてすごい！医療現場にも大きな影響がありそうだね。未来の技術がこんなに進んでいるってワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2024-06-09 03:52

- - -

### [Privacy-Preserving Optimal Parameter Selection for Collaborative Clustering](http://arxiv.org/abs/2406.05545)

**プライバシー保護を目的とした協調クラスタリングの最適パラメータ選択**

Maryam Ghasemian, Erman Ayday

- 協調クラスタリングの最適パラメータ選択をデータプライバシーを確保しつつ探求
- 複数のデータ所有者がデータを結合し、半信頼サーバが最適アルゴリズムとパラメータを推薦
- プライバシーパラメータ($\epsilon$)が推薦に与える影響は少ないが、$\epsilon$が高いほどメンバーシップ推測攻撃のリスク増加
- 差分プライバシー技術（特にランダム化応答技法）を使用しデータ保護、クラスター品質は高維持

協調クラスタリングしながらプライバシーを守るっていうアプローチすごく気になるね。データをシェアしつつ安全性高めるテクニックはこれからの研究に大事だよね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-08 18:21

- - -

### [Blockchain Integrated Federated Learning in Edge-Fog-Cloud Systems for IoT based Healthcare Applications A Survey](http://arxiv.org/abs/2406.05517)

**IoTベースのヘルスケアアプリケーションにおけるエッジ-フォグ-クラウドシステムに統合されたブロックチェーン連合学習の調査**

Shinu M. Rajagopal, Supriya M., Rajkumar Buyya

- IoTアプリケーションは大量のデータを生成するが、データのサイロ化とユーザープライバシー法が利用を制約する
- 連合学習は分散型パラダイムであり、プライバシーを保ちながらの共同学習を可能にする理想的な手法である
- 暗号技術を使用することで、IoTシステムはデータを安全に保管・送信し、一貫性を保証できる
- ヘルスケアのような機密データの処理における連合学習とブロックチェーンの統合は特に有益である

連合学習とブロックチェーンがヘルスケアデータの処理でどう役立つか、とっても面白そう！エッジ-フォグ-クラウドの説明も知りたいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-08 16:36

- - -

### [Baking Symmetry into GFlowNets](http://arxiv.org/abs/2406.05426)

**GFlowNetに対する対称性の組み込み**

George Ma, Emmanuel Bengio, Yoshua Bengio, Dinghuai Zhang

- GFlowNetは高い報酬を持つ多様な候補を生成するが、同型の行動を考慮していない
- 対称性の欠如はトレーニングサンプルの増加と効率の低下を引き起こす
- 研究の目標は、生成プロセス中に同等の行動を識別して対称性を組み込むこと
- 合成データを用いた実験結果で提案手法の有望な性能を示す

対称性を取り入れることで、さらに効率が良くなりそう。これ、実際どうやって同型の行動を見つけるんだろう？



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-08 10:11

- - -

### [PTF-FSR: A Parameter Transmission-Free Federated Sequential Recommender System](http://arxiv.org/abs/2406.05387)

**PTF-FSR: パラメータ送信不要な連合逐次推薦システム**

Wei Yuan, Chaoqun Yang, Liang Qu, Quoc Viet Hung Nguyen, Guanhua Ye, Hongzhi Yin

- 従来の連合逐次推薦システムは共有モデルの必要性があり、知的財産の懸念がある
- 高い通信コストが問題で、大規模言語モデルの時代には適用困難
- PTF-FSRはモデルとデータのプライバシーを保護し、複雑で大規模なモデルに対応可能
- 実験結果は、PTF-FSRの有効性と汎用性を示し、多様なデータセットとモデルで検証

モデルの知的財産を守りつつ、プライバシー保護も実現できるなんて新しいアプローチだね！これで連合学習がもっと広まるかも、早く試してみたい！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, **投稿日時:** 2024-06-08 07:45

- - -

### [Efficient Differentially Private Fine-Tuning of Diffusion Models](http://arxiv.org/abs/2406.05257)

**効率的な差分プライバシーを用いた拡散モデルの微調整**

Jing Liu, Andrew Lowy, Toshiaki Koike-Akino, Kieran Parsons, Ye Wang

- 拡散モデルは高品質な合成データを生成可能
- 差分プライバシーを用いて微調整したモデルは優れたプライバシー・効用バランスを達成
- メモリと計算資源の負担が大きいが、低次元適応を用いて効率化を図った
- 提案手法はMNISTとCIFAR-10データセットで評価され、有用な合成サンプル生成を確認

効率的にプライバシーを守りながら拡散モデルを使えるなんて、未来のプライバシー技術はもっと進化しそう！配布予定のソースコードも楽しみだね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-07 21:00

- - -

### [Federated LoRA with Sparse Communication](http://arxiv.org/abs/2406.05233)

**スパース通信を用いた連合LoRA**

Kevin Kuo, Arian Raje, Kousik Rajesh, Virginia Smith

- LoRAは通信制約のある機械学習設定での微調整に自然な方法である
- 中央集権型MLの手法でのLoRAの効率改善は連合設定では効果が低い
- 代わりに、通信中にスパース化を適用するFLASCを提案し、局所的微調整を可能にした
- 4つの連合学習タスクで、通信量を10倍削減しつつLoRAの性能を維持することを実証

この論文、連合学習での通信効率ってめっちゃ重要なんだね！性能維持しつつ通信量減らせるなんて、未来のネットワーク環境でも大活躍しそう♡

**Comment:** 12 pages (excluding references), 8 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-06-07 19:42

- - -

### [The Unmet Promise of Synthetic Training Images: Using Retrieved Real Images Performs Better](http://arxiv.org/abs/2406.05184)

**合成トレーニング画像の未達成の約束：取得した実画像の方が優れる**

Scott Geng, Cheng-Yu Hsieh, Vivek Ramanujan, Matthew Wallingford, Chun-Liang Li, Pang Wei Koh, Ranjay Krishna

- Stable Diffusionで生成された合成データは、LAION-2Bデータセットから直接取得した実画像に匹敵するか負ける
- 合成画像は下流タスクに利益をもたらす可能性があるが、生成器のアーティファクトと不正確な視覚詳細が問題
- 提案された比較ベースラインでは、合成データよりも実データが一貫して優れていることが示された
- 合成データを使う際には、まず実データの取得を試みることが重要である

合成画像に頼りがちだけど、やっぱり実データにかなわないんだね。これからは、データゲットの方法も考えなきゃ！

**Comment:** Correspondence to sgeng@cs.washington.edu. RK and PWK equally advised   the project

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-07 18:04
