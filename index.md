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

更新: 2024-11-29T04:23:19.957409

- - -

### [Task Arithmetic Through The Lens Of One-Shot Federated Learning](http://arxiv.org/abs/2411.18607)

**ワンショット連合学習を通じたタスク算術の視点**

Zhixu Tao, Ian Mason, Sanjeev Kulkarni, Xavier Boix

- タスク算術はモデルの統合技術で、複数モデルの能力を一つのモデルに統合する
- タスク算術の成功要因は不明瞭であり、データ異質性やトレーニング異質性が影響
- 連合学習のFedAvgと数学的に同等であることを示し、理論上の基盤を構築
- 連合学習のアルゴリズムを適用し、パフォーマンス向上を実証し、理論と実用性の橋渡しを行う

タスク算術と連合学習の関係を掘り下げるっておもしろそうじゃない？新しい理論的な視点も得られるし、こういう新技術が今後のAIモデル開発に役立つって期待が高まるね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-27 18:53

- - -

### [Evaluating and Improving the Effectiveness of Synthetic Chest X-Rays for Medical Image Analysis](http://arxiv.org/abs/2411.18602)

**合成胸部X線画像の医学的画像解析における有効性の評価と改善**

Eva Prakash, Jeya Maria Jose Valanarasu, Zhihong Chen, Eduardo Pontes Reis, Andrew Johnston, Anuj Pareek, Christian Bluethgen, Sergios Gatidis, Cameron Olsen, Akshay Chaudhari, Andrew Ng, Curtis Langlotz

- 合成胸部X線画像を生成し、医療画像データセットを拡張して深層学習モデルの性能を最適化する
- 潜在拡散モデルを使い、テキストプロンプトやセグメンテーションマスクに基づいて合成画像を生成
- 疾患情報や幾何変形セグメントマスクを使用し、分類とセグメンテーションの性能向上を測定
- 一尾t検定とボンフェローニ補正で合成データによる改善の統計的有意性を評価

合成データをうまく活用して医療画像解析の精度を上げるなんてすごいね！これからの医療技術がどんどん進化していくって感じでワクワクしちゃう♡



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-11-27 18:47

- - -

### [Enhancing weed detection performance by means of GenAI-based image augmentation](http://arxiv.org/abs/2411.18513)

**GenAIベースの画像拡張による雑草検出性能の強化**

Sourav Modak, Anthony Stein

- 雑草管理の効率化のために高品質なトレーニングデータが必要である
- 従来のデータ拡張技術は多様性に欠け、十分な精度が得られない
- Stable Diffusionモデルを使用し、高品質な合成画像を生成してデータセットを強化
- 合成データはYOLOモデルの精度向上に貢献し、モデルの堅牢性を高める可能性がある

AIで雑草検出の精度がグンと上がるなんて、なんだか未来を感じるね！これがどんどん普及すれば、もっと持続可能な農業が実現しそうじゃない？



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-27 17:00

- - -

### [Synthetic ECG Generation for Data Augmentation and Transfer Learning in Arrhythmia Classification](http://arxiv.org/abs/2411.18456)

**不整脈分類におけるデータ拡張と転移学習のための合成ECG生成**

José Fernando Núñez, Jamie Arjona, Javier Béjar

- ディープラーニングには十分なデータが必要であり、合成データでデータセットを拡大できる。
- ECGのデータ生成にはDiffweave、Time-Diffusion、Time-VQVAEを使用し、分類精度を向上。
- 合成データと実データを組み合わせた時に分類器の精度が向上する。
- Time-VQVAEは他の生成モデルより優れているが、実データのみの分類器には及ばない。

合成データを活用して心電図解析の精度を高めるのは面白いね！医療現場での応用が進むと安心だし、データ不足の解消に役立ちそう。興味深い成果が出てくるのを期待してる！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-27 15:46

- - -

### [Federated Learning with Uncertainty and Personalization via Efficient Second-order Optimization](http://arxiv.org/abs/2411.18385)

**不確実性とパーソナライズを考慮した連合学習：効率的な二次最適化**

Shivam Pal, Aishwarya Gupta, Saqib Sarwar, Piyush Rai

- 連合学習はデータをクライアントに留めおくため、データの分散処理に優れている
- ベイジアンアプローチにより、モデルや予測の不確実性を後部分布で把握できる
- 層状ベイジアンアプローチで個別モデルを共通の事前分布と共に学習可能
- 効率的な二次最適化で計算コストを抑えつつ精度向上を実現する方法を提案

個別データに応じてモデルをパーソナライズできて、しかも計算が効率的だなんて、面白そう！これで連合学習の弱点を克服できるかもね～



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, stat.ML, **投稿日時:** 2024-11-27 14:30

- - -

### [FreqX: What neural networks learn is what network designers say](http://arxiv.org/abs/2411.18343)

**FreqX: ニューラルネットワークが学ぶのは設計者の意図**

Zechen Liu

- 個別の連合学習は非公開の個人モデルを協力して訓練するが、非独立同一分布や不公平性などの課題がある
- 説明可能性への新たな要求として、低コスト、プライバシー、詳細情報が求められている
- 従来の方法ではこれらを満足できず、新たに信号処理と情報理論を用いた解釈方法FreqXを提案
- FreqXは基準方法より10倍以上速く、帰属情報と概念情報を含む説明結果を示す

新しい技術が早くて詳しい情報を得られるなんて、ほんとにすごいと思う！連合学習の課題を解決することで、個別のAIがもっと活用されそうな予感がするね。

**Comment:** 16pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-11-27 13:41

- - -

### [Hidden Data Privacy Breaches in Federated Learning](http://arxiv.org/abs/2411.18269)

**連合学習における隠れたデータプライバシー侵害**

Xueluan Gong, Yuji Wang, Shuaike Li, Mengyuan Sun, Songze Li, Qian Wang, Kwok-Yan Lam, Chen Chen

- 連合学習はデータを共有せずに機械学習を行うパラダイムであるが、最近の研究でモデル操作や勾配分析を通じたデータ盗難のリスクが示された
- 提案されたデータ再構築攻撃は、悪意のあるコード注入を用い、目立たずにパラメータ共有を通じて機密データを抽出する
- フィボナッチベースのインデックス設計により、効率的かつ構造化されたデータ回収が可能で、高解像度画像もブロック分割で処理対応可能
- 提案手法はFedAVGとFedSGDに対しても直接適用可能であり、新たな防御策の必要性を示している

連合学習ってプライバシー安心と思ってたけど、こんな裏技があるんだね。悪意ある攻撃への対策が急務って感じ！おもしろいし、ちょっと怖いね。開発者さんたち、早く新しい防御策考えてほしいなー！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.CR, **投稿日時:** 2024-11-27 12:04

- - -

### [Dependency-Aware CAV Task Scheduling via Diffusion-Based Reinforcement Learning](http://arxiv.org/abs/2411.18230)

**Diffusionベース強化学習による依存性認識CAVタスクスケジューリング**

Xiang Cheng, Zhi Mao, Ying Wang, Wen Wu

- 無人航空機が支援する自律車両(CAV)のタスクを依存性を考慮して効率的に割り当てる手法を提案
- CAVや基地局にサブタスクを割り当て、タスク完了時間を最小化する問題をマルコフ決定過程として定式化
- PickerであるSynthetic DDQNベースの拡散強化学習アルゴリズムを開発し、柔軟なタスクスケジューリングを実現
- シミュレーション結果で提案手法が従来の手法よりもタスク完了時間を短縮する効果を確認

これって、まさに未来のスマートシステムだよね！自動車たちが美しく連携して仕事をこなして、効率がグンと上がるのが想像できる！どうなるか楽しみだなぁ。

**Comment:** 6 pages, 5 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.RO, **投稿日時:** 2024-11-27 11:07

- - -

### [SharpDepth: Sharpening Metric Depth Predictions Using Diffusion Distillation](http://arxiv.org/abs/2411.18229)

**SharpDepth: 拡散蒸留を用いたメトリック深度予測の鮮明化**

Duc-Hai Pham, Tung Do, Phong Nguyen, Binh-Son Hua, Khoi Nguyen, Rang Nguyen

- SharpDepthは単眼メトリック深度推定の新手法である
- 判別法のメトリック精度と生成法の境界鮮明さを組み合わせる
- メトリック精度と境界詳細を統合し制限を克服する
- ゼロショット評価で高精度と詳細な表現力を発揮する

深度予測にこんなに進化があるなんて、すごくワクワクする！ビジュアルも鮮明で、どんなリアルな環境にも使えそうなんて、未来のアプリケーションが楽しみだなあ。

**Comment:** Uncompressed version can be found in   https://drive.google.com/file/d/1MG4-d_xDERVBCRfLDolNLnMLLuqd7qRz

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-27 11:07

- - -

### [Training Data Synthesis with Difficulty Controlled Diffusion Model](http://arxiv.org/abs/2411.18109)

**困難制御型拡散モデルによるデータ合成の訓練**

Zerun Wang, Jiafeng Mao, Xueting Wang, Toshihiko Yamasaki

- 半教師あり学習は、低コストで集めた未ラベル画像を活用しモデル性能を向上させる
- 合成画像が未ラベルデータに混入することで半教師あり学習への影響が未解明
- Real-Synthetic Hybrid SSL（RS-SSL）を導入しこれらの影響を調査
- RSMatchという新しい方法で、合成データを制約から資源へと変換可能と実証

合成画像が「障害」から「資源」に変わるのってすごい！RSMatchの活用で、合成データももっと役に立ちそうだから、新しいモデルがどんどん出てきておもしろくなりそうだね。未来のデータ活用が楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-11-27 07:42

- - -

### [CrypQ: A Database Benchmark Based on Dynamic, Ever-Evolving Ethereum Data](http://arxiv.org/abs/2411.17913)

**CrypQ: ダイナミックで進化し続けるイーサリアムデータに基づくデータベースベンチマーク**

Vincent Capol, Yuxi Liu, Haibo Xiu, Jun Yang

- 現代のデータベースシステムは時間とともに進化する動的データを扱う必要がある
- 多くのデータベースベンチマークは動的な側面の評価が不十分である
- CrypQは動的なイーサリアムブロックチェーンデータを活用し、現実的かつ高容量なデータセットを提供
- CrypQは現実の不均等性と依存関係を含むデータ分布でコストベースのクエリ最適化を評価

イーサリアムデータを使ったデータベース評価とか面白そう！動的データの扱いがこれからますます重要になりそうだね。進化し続けるから、飽きずに学べそう！

**Comment:** Accepted by Proceedings of the 2024 TPC Technology Conference on   Performance Evaluation and Benchmarking @ VLDB 2024, Guangzhou

**トピック:** [合成データ](sd), **カテゴリ:** cs.DB, **投稿日時:** 2024-11-26 22:09

- - -

### [Distributed Sign Momentum with Local Steps for Training Transformers](http://arxiv.org/abs/2411.17866)

**局所ステップを用いたトランスフォーマー訓練の分散符号モーメント**

Shuhua Yu, Ding Zhou, Cong Xie, An Xu, Zhi Zhang, Xin Liu, Soummya Kar

- トランスフォーマーモデルの事前学習はリソースを大量に消費する。
- 本研究では、効率的な分散符号モーメント手法を提案、局所更新を活用。
- 提案手法は広範な基底最適化器を許容し、符号モーメントを利用してグローバル更新。
- GPT-2モデルの学習で他の分散手法と比較し、著しい改善を確認。

分散で効率的な学習方法ができちゃうんだね！今回の方法は従来より良くなるみたいで、リソースが限られててもみんな元気に学べそう！トランスフォーマーの未来がまた楽しみになるね。

**Comment:** 23 pages, 21 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-26 20:31

- - -

### [Adaptive Client Selection with Personalization for Communication Efficient Federated Learning](http://arxiv.org/abs/2411.17833)

**パーソナライズによる通信効率的な連合学習のための適応的クライアント選択**

Allan M. de Souza, Filipe Maciel, Joahannes B. D. da Costa, Luiz F. Bittencourt, Eduardo Cerqueira, Antonio A. F. Loureiro, Leandro A. Villas

- 連合学習は通信のボトルネックとネットワークのスケーラビリティに課題がある
- ACSP-FLはクライアント数やラウンド数を動的に調整し、通信と計算のコストを削減
- モデルパーソナライズによりクライアントのパフォーマンスを向上
- 最大95%の通信削減を達成しつつ、異なるデータ分布でも良好な収束を実現

連合学習の通信効率を劇的に改善する技術みたい！データの広がりが多様な状況でもこのアプローチが使えるって、すごく便利そう。どこでも使える未来が見えてくるね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-11-26 19:20

- - -

### [Analytic Continuation by Feature Learning](http://arxiv.org/abs/2411.17728)

**特徴学習による解析接続**

Zhe Zhao, Jingping Xu, Ce Wang, Yaping Yang

- 解析接続は虚時間グリーン関数から実時間スペクトル関数を再構築するが、解決が難しい問題である
- 新しいニューラルネットワーク構造であるFL-netを提案し、従来手法よりも20%以上の精度向上を達成
- 提案されたネットワークのロバスト性を評価するための解析的手法を開発
- FL-netの隠れ次元を増やすと損失が低減されるが、ロバスト性が低下することを示した

解析接続の難題をニューラルネットで解決するのって面白いよね！効果がUPするけど、頑丈さがDOWNするのも興味深い問題だよね。

**Comment:** 8 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cond-mat.str-el, cs.LG, eess.SP, physics.comp-ph, stat.ML, **投稿日時:** 2024-11-22 05:12
