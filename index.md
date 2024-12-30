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

更新: 2024-12-30T04:22:20.622697

- - -

### [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](http://arxiv.org/abs/2412.19723)

**OS-Genesis: 逆タスク合成によるGUIエージェント軌跡構築の自動化**

Qiushi Sun, Kanzhi Cheng, Zichen Ding, Chuanyang Jin, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu

- GUIエージェントの軌跡データ収集はリソースがかかるか、データの質を保証できない
- OS-Genesisは従来のアプローチとは反対に環境を認識し、後から質の高いタスクを生成
- 軌跡報酬モデルで生成された軌跡の質を確保し、オンラインベンチマークで性能を向上
- OS-Genesisは従来の合成方法と比べて優れたデータ質と多様性を提供することを示した

GUIエージェントの学習効率を高める新しい手法って、とても革新的だよね！データの多様性と質を改善する方法がリアルタイムで実用化できたら、アプリ開発の未来がもっと面白くなるかも。

**Comment:** Work in progress

**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, cs.CV, cs.HC, **投稿日時:** 2024-12-27 16:21

- - -

### [Asymmetrical Reciprocity-based Federated Learning for Resolving Disparities in Medical Diagnosis](http://arxiv.org/abs/2412.19654)

**医療診断における格差解消のための非対称相互性に基づく連合学習**

Jiaqi Wang, Ziyi Yin, Quanzeng You, Lingjuan Lyu, Fenglong Ma

- 低・中所得国の地域的な健康格差は、限られたデータと計算資源が原因で悪化
- FedHelpという新しいフレームワークを提案し、連合学習で地域格差問題に対処
- 基礎モデルの知識をAPIで利用し、データ不足に苦しむ小規模クライアントを支援
- 非対称性を克服するため、非対称デュアル知識蒸留モジュールを導入

医療の発展が進む未来が期待できそうだね！テクノロジーで世界中の健康格差を少しでも埋められるなんて、とてもワクワクするね。

**Comment:** Jiaqi Wang and Ziyi Yin equally contributed to this paper. This paper   has been accepted by KDD 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-12-27 13:59

- - -

### [TARGA: Targeted Synthetic Data Generation for Practical Reasoning over Structured Data](http://arxiv.org/abs/2412.19544)

**ターゲット合成データ生成による構造化データの実用的推論**

Xiang Huang, Jiayu Shen, Shanshan Huang, Sitao Cheng, Xiaxia Wang, Yuzhong Qu

- セマンティックパーシングは、自然言語を論理形式に変換する技術だが、手動アノテーションが必要
- TARGAは手動アノテ不要で、高関連性の合成データを動的生成する新しいフレームワーク
- TARGAは、データセットGraiqQAとKBQA-Agentで大幅な精度向上を達成し、効率も良い
- 非独立同一分布（non-I.I.D.）でも、TARGAは高いサンプル効率と頑健性、一般化能力を持つ

論文の手動アノテationが要らないというのは、すごく便利そう！知識ベースの質問応答で成果が出てるのも好印象。やっぱり次世代の学習プロセスの進展にとてもワクワクしちゃうね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-12-27 09:16

- - -

### [Learning Radiance Fields from a Single Snapshot Compressive Image](http://arxiv.org/abs/2412.19483)

**単一ショット圧縮画像からの放射フィールド学習**

Yunhao Li, Xiang Liu, Xiaodong Wang, Xin Yuan, Peidong Liu

- 単一の圧縮画像から3Dシーン構造を復元するために、Snapshot Compressive Imaging（SCI）の技術を探る
- 低コストな2Dイメージングセンサーを用いて高次元データを1枚の画像に記録し、効率的でプライバシー保護も可能
- 神経放射フィールド（NeRF）の力を活用し、3Dシーン情報を復元する新手法SCINeRFを提案
- SCINeRFと3D Gaussian Splattingフレームワークを組み合わせるSCISplatで、シーンの再構築品質と速度を向上

シーン構造を圧縮しながらも、NeRFによって3D情報をうまく復元しちゃうのってなんかすごい！リアルタイムで高フレームレートを維持できるのも、未来の映像技術につながりそうでワクワクするね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-27 06:40

- - -

### [Federated Hybrid Training and Self-Adversarial Distillation: Towards Robust Edge Networks](http://arxiv.org/abs/2412.19354)

**連合ハイブリッド学習と自己対抗蒸留：堅牢なエッジネットワークを目指して**

Yu Qiao, Apurba Adhikary, Kitae Kim, Eui-Nam Huh, Zhu Han, Choong Seon Hong

- 連合学習は、データの生データを送信せずにプライバシーを向上させる技術である
- データの不均一性や敵対的攻撃が、エッジでのモデル執行に難しさをもたらす
- FedBATを提案し、ハイブリッド対抗学習と自己対抗蒸留を統合して堅牢性を向上
- 多様なデータセットで実験し、正確さを保ちつつロバスト性を強化した成果を示す

このFedBATって面白そうね！敵対的攻撃から守りつつ、みんなのデータに偏りが出ないようにするなんて、本当にエッジネットワークにうってつけだと思う。これが広まったら、もっと安全なネット社会になりそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-12-26 21:32

- - -

### [Swarm Contract: A Multi-Sovereign Agent Consensus Mechanism](http://arxiv.org/abs/2412.19256)

**スウォームコントラクト: マルチ・ソブリンエージェントによる合意形成メカニズム**

Haowei Yang

- 従来のスマートコントラクトはオンチェーンでの決定論的なロジック実行に優れているが、オフチェーンでの大規模データ処理や動的なワークフローには課題がある。
- スウォームコントラクトは、複数のデジタルライフフォームまたはソブリンエージェントが、信頼された実行環境で複雑なタスクを処理する新たなメカニズム。
- 多重署名によるオンチェーンウォレットを活用することで、論理をオフチェーンに移動し、中央集権的コントロールを回避。
- この方法はDAOガバナンスやクロスチェーン互換性の向上、マルチモーダルデータ処理の支援に貢献できる可能性がある。

分散型で信頼が不要な仕組みが増えるなんてワクワクしちゃうね！DAOとかNFTにもっと応用できたら、未来の可能性は無限大だよね。

**Comment:** 7 pages, 1 figure

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, C.2.4; D.4.6, **投稿日時:** 2024-12-26 15:46

- - -

### [Mask Factory: Towards High-quality Synthetic Data Generation for Dichotomous Image Segmentation](http://arxiv.org/abs/2412.19080)

**マスクファクトリー: 2値画像セグメンテーションのための高品質な合成データ生成に向けて**

Haotian Qian, YD Chen, Shengtao Lou, Fahad Shahbaz Khan, Xiaogang Jin, Deng-Ping Fan

- 2値画像セグメンテーションは精密な注釈が必要で、従来のデータセット作成は大変で専門知識が必要
- 合成データを用いるとこれらの課題を解決できるが、既存の生成モデルではシーンのずれやノイズ、サンプルの多様性に課題がある
- 新手法\ourmodel{}は多様で精密なデータセットを低コストで生成し、準備時間を大幅に短縮
- 実験では、DIS5Kデータセットベンチマークで既存手法より高品質で効率的な性能を示す

このアプローチめちゃ賢そうじゃない？合成データ生成がもっと簡単にできたら、画像解析の未来がさらに広がる予感☆



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-26 06:37

- - -

### [Effective and secure federated online learning to rank](http://arxiv.org/abs/2412.19069)

**効果的かつ安全な連合オンラインランク学習**

Shuyi Wang

- OLTRはクリックなどのユーザーフィードバックを用いてランキングモデルを最適化
- 人間の注釈コストやユーザープリファレンスと人間の判断のミスマッチを解消
- OLTRはユーザーデータの収集が必要でプライバシーの懸念がある
- FOLTRは連合学習を活用しプライバシーを強化するが、ランキングの効果やセキュリティが課題

連合学習を使ってみんなのデータを安全に守りながら効率的にランキングを最適化するなんて、未来の技術って感じがするよね！なのに今のFOLTRにはまだまだ課題があるみたい。改善されたらもっとすごいことに使えるかも〜。

**Comment:** PhD Thesis

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.IR, **投稿日時:** 2024-12-26 05:53

- - -

### [Optimal Federated Learning for Functional Mean Estimation under Heterogeneous Privacy Constraints](http://arxiv.org/abs/2412.18992)

**異なるプライバシー制約下での機能平均推定のための最適な連合学習**

Tony Cai, Abhinav Chakraborty, Lasse Vuursteen

- 連合学習はデータプライバシーを保つための分散機械学習技術である
- 人数や測定数、プライバシーパラメータが異なる環境で平均推定誤差を解析
- 共通設計と個別設計の設定で、設計点の違いによる推定誤差の境界を確立
- プライバシーと精度の最適なバランスを実現するアルゴリズムを提案

この論文、異なるプライバシー条件での最適性とか、共通設計と個別設計の違いが興味深いよね！プライバシーと精度のバランスをどうやって取ってるのか、実際に応用されたらめっちゃ便利そう～。



**トピック:** [連合学習](fl), **カテゴリ:** math.ST, cs.LG, stat.TH, 62G08, 62G20, **投稿日時:** 2024-12-25 22:06

- - -

### [FedCFA: Alleviating Simpson's Paradox in Model Aggregation with Counterfactual Federated Learning](http://arxiv.org/abs/2412.18904)

**FedCFA: 反事実連合学習によるモデル集約のシンプソンのパラドックス緩和**

Zhonghua Jiang, Jimin Xu, Shengyu Zhang, Tao Shen, Jiwei Li, Kun Kuang, Haibin Cai, Fei Wu

- 連合学習はデータの不均衡と異質性に苦しむ
- シンプソンのパラドックスでのパフォーマンスが課題
- FedCFAは反事実学習を用いてパラドックスを緩和
- 要因をデコレートするFDC損失でサンプルの品質を改善

連合学習に新たな視点を持ち込んで、パラドックス問題を解決しようとしているところが面白いね。効率よく精度を上げる手法が見つかると、実用化も夢じゃないかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-25 13:35

- - -

### [Bootstrap Your Own Context Length](http://arxiv.org/abs/2412.18860)

**自身のコンテキスト長をブートストラップする**

Liang Wang, Nan Yang, Xingxing Zhang, Xiaolong Huang, Furu Wei

- 短いコンテキスト能力を使い、長コンテキスト言語モデルを訓練するブートストラップ法を紹介
- 手動のデータ収集・注釈を排除し、合成データで多様な長コンテキストの指示チューニングを可能に
- データの合成は短コンテキストの言語モデル、テキストリトリーバー、文書コレクションで実現
- Llama-3モデルを用い、コンテキスト長を1Mトークンまで拡張し高性能を達成

長コンテキスト化がめっちゃ面白そう！どんどん便利になっていくLanguage Modelの未来が楽しみだね。特に手作業がいらないの、まさにAIの進化って感じ！

**Comment:** 18 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.IR, **投稿日時:** 2024-12-25 10:08

- - -

### [Federated Learning with Partially Labeled Data: A Conditional Distillation Approach](http://arxiv.org/abs/2412.18833)

**部分ラベルデータを用いた連合学習：条件付き蒸留アプローチ**

Pochuan Wang, Chen Shen, Masahiro Oda, Chiou-Shann Fuh, Kensaku Mori, Weichung Wang, Holger R. Roth

- 医療画像の汎用的なセグメンテーションモデルにおいて重要なのは、多数の器官と病変に対応することである。
- 既存の連合学習は部分ラベルに弱く、モデルの分岐や忘却が問題となる。
- ConDistFLは条件付き蒸留を組み込むことで、部分ラベルデータから効果的な学習を可能にする。
- 実験でConDistFLは一般化能力を発揮し、見たことのないコントラスト位相にも適応可能と示された。

この研究、医療の分野でプライバシーを守りつつも画像技術を進化させる感じがするね。未来の病気診断が迅速かつ確実になるなんて、なんだかワクワクしちゃうな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-25 08:40

- - -

### [The Impact of Input Order Bias on Large Language Models for Software Fault Localization](http://arxiv.org/abs/2412.18750)

**ソフトウェア障害の局所化における大規模言語モデルへの入力順序バイアスの影響**

Md Nakhla Rafi, Dong Jae Kim, Tse-Hsun Chen, Shaowei Wang

- 大規模言語モデルはソフトウェア障害の局所化や自動プログラム修正で有望
- 入力順とコンテキストサイズが性能に与える影響を調査
- コード順を逆にするとTop-1精度が57%から20%に減少
- 小さなコンテキストに分けることでバイアスを軽減しパフォーマンス差を1%に縮小

入力順序がこんなに重要なんだー！学習の工夫次第でパフォーマンスが大きく変わりそうで面白いね。これ、具体的な障害箇所特定にめっちゃ役立ちそうじゃない？



**トピック:** [連合学習](fl), **カテゴリ:** cs.SE, cs.AI, cs.LG, **投稿日時:** 2024-12-25 02:48

- - -

### [Edge-AI for Agriculture: Lightweight Vision Models for Disease Detection in Resource-Limited Settings](http://arxiv.org/abs/2412.18635)

**農業のためのエッジAI: 資源制限環境における病気検出のための軽量ビジョンモデル**

Harsh Joshi

- 軽量かつ効率的なコンピュータビジョンのパイプラインを開発し、農家がオレンジの病気を検出できるように支援。
- リソース制限環境での動作を保証するために、エッジデバイスに最適化されたオブジェクト検出、分類、セグメンテーションモデルを統合。
- 最新のビジョントランスフォーマーモデルはオレンジの分類で96の精度を達成し、YOLOv8-Sは低計算負荷で優れた物体検出性能を示した。
- モデルの複雑さと実用性のバランスが重要で、多様な農業コンテクストでの適用を広げるためにデータセット拡大やモデル圧縮、連合学習を探求予定。

エッジAIを使って農業がより効率化されるなんて、未来の農業っぽくてワクワクしちゃう！これで持続可能な農業がもっと身近になるといいなー。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.CY, **投稿日時:** 2024-12-23 06:48
