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

更新: 2024-07-05T04:20:31.808078

- - -

### [Correlated Privacy Mechanisms for Differentially Private Distributed Mean Estimation](http://arxiv.org/abs/2407.03289)

**差分プライベートな分散平均推定のための相関プライバシーメカニズム**

Sajani Vithana, Viveck R. Cadambe, Flavio P. Calmon, Haewon Jeong

- 差分プライバシーを保証しつつ、$d$次元ベクトルの平均を推定することが目的
- ローカル差分プライバシー（LDP）は耐性は強いが、ユーティリティの低下が問題
- 分散DPはユーティリティが高いが、通信や計算のオーバーヘッドが増加
- 提案するCorDP-DMEは、ガウスノイズを利用し、LDPと分散DPの間のバランスを実現

CorDP-DMEっていい感じだね！LDPの保護と分散DPの効率をうまいこと両立させてて、実用的なプライバシー技術だと思うな～。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.IT, cs.CR, cs.LG, math.IT, **投稿日時:** 2024-07-03 17:22

- - -

### [Bridging Model Heterogeneity in Federated Learning via Uncertainty-based Asymmetrical Reciprocity Learning](http://arxiv.org/abs/2407.03247)

**連合学習におけるモデルの不均一性を不確実性に基づく非対称相互学習で解決する方法**

Jiaqi Wang, Chenxu Zhao, Lingjuan Lyu, Quanzeng You, Mengdi Huai, Fenglong Ma

- 連合学習のモデル不均一性を解決するためのFedTypeを提案
- 小規模な同一プロキシモデルを用いて安全かつ効率的な情報交換を実現
- 公共データを一切使用せずに、クライアント間の知識移転を提案
- 包括的な実験でFedTypeの有効性と一般化能力を実証

新しい不確実性に基づく学習方法って、なんだかワクワクするよね！クライアントのプライバシーも守られるなんて、これからの連合学習の未来が楽しみだね。

**Comment:** This paper has been accepted by ICML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-03 16:23

- - -

### [Reconsidering utility: unveiling the limitations of synthetic mobility data generation algorithms in real-life scenarios](http://arxiv.org/abs/2407.03237)

**有用性の再考: 実際のシナリオにおける合成移動データ生成アルゴリズムの限界を明らかにする**

Alexandra Kapp, Helena Mihaljević

- 合成移動データ生成はプライバシーを守りつつ高い有用性と柔軟性を目指す
- 現在の有用性評価方法は実際の要求に完全には対応していない
- 5つの最新の合成アプローチを、差分プライバシー (DP) 保証有無で評価
- モデルは空間分布の維持に成功するものの、意味のあるジオロケーションのシーケンスを生成できない

リアルなシナリオを想定して評価するのは重要だね！未来の移動データ技術がどんな風に進化していくのか、興味津々だよ。

**Comment:** 12 pages, 8 figures, 31st ACM International Conference on Advances in   Geographic Information Systems (SIGSPATIAL 2023)

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-03 16:08

- - -

### [TheoremLlama: Transforming General-Purpose LLMs into Lean4 Experts](http://arxiv.org/abs/2407.03203)

**TheoremLlama: 汎用LLMをLean4の専門家に変える**

Ruida Wang, Jipeng Zhang, Yizhen Jia, Rui Pan, Shizhe Diao, Renjie Pi, Tong Zhang

- 数学定理の形式的証明を生成するためにNL-FL整合データの希少性が課題である
- TheoremLlamaフレームワークはNL-FL整合データ生成、LLMトレーニング、Lean4証明技術を統合する
- NL-FLブートストラップ法でLLMの自然言語推論能力を形式的推論に活用
- MiniF2F-ValidとTestデータセットでGPT-4を上回る精度を達成

自動で数学の定理を証明するAIとか、超面白そう！みんなで問題解けるLLMを使って、授業でもっと楽できる未来が来そうだね💕



**トピック:** [連合学習](fl), **カテゴリ:** cs.FL, cs.AI, **投稿日時:** 2024-07-03 15:36

- - -

### [Venomancer: Towards Imperceptible and Target-on-Demand Backdoor Attacks in Federated Learning](http://arxiv.org/abs/2407.03144)

**Venomancer: 連合学習における目に見えないオンデマンド型バックドア攻撃に向けて**

Son Nguyen, Thinh Nguyen, Khoa Doan, Kok-Seng Wong

- 連合学習はデータを分散して訓練することでプライバシーを保護するが、バックドア攻撃に弱い
- 従来のバックドア攻撃は事前に定義されたターゲットクラスが必要で、目に見えて検出可能
- Venomancerは、視覚的損失関数を使い元データと視覚的に識別不可能な毒データを生成
- 実験でNorm Clipping, Weak DP, Krum, Multi-Krumなど最先端防御に対する高い耐性を示す

目に見えないバックドア攻撃とか、今までになかった攻め方って感じ？連合学習の未来にどんな影響があるのか楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-03 14:22

- - -

### [Effective Heterogeneous Federated Learning via Efficient Hypernetwork-based Weight Generation](http://arxiv.org/abs/2407.03086)

**効率的なハイパーネットワークベースの重み生成を用いた効果的な異種連合学習**

Yujin Shin, Kichang Lee, Sungmin Lee, You Rim Choi, Hyung-Sin Kim, JeongGil Ko

- 連合学習は分散クライアントリソースを利用するが、異質なクライアント能力のため困難が伴う
- HypeMeFedという新しい連合学習フレームワークを提案し、マルチエグジットネットワークとハイパーネットワークベースの重み生成を組み合わせ
- 低ランク因子分解アプローチを採用し、ハイパーネットワークの計算とメモリのオーバーヘッドを最小化
- 実際の異質デバイスで評価し、FedAvgよりも精度が5.12%向上、メモリ要求を98.22%削減、動作速度を1.86倍に加速

この内容めっちゃ面白そう！異質なクライアントでも効率的な学習ができるなんて、未来の連合学習が楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-07-03 13:15

- - -

### [Artificial Inductive Bias for Synthetic Tabular Data Generation in Data-Scarce Scenarios](http://arxiv.org/abs/2407.03080)

**データ不足なシナリオにおける合成タブラデータ生成のための人工的帰納バイアス**

Patricia A. Apellániz, Ana Jiménez, Borja Arroyo Galende, Juan Parras, Santiago Zazo

- 深層生成モデル（DGM）はデータ不足とプライバシー問題を解決するが、十分な訓練データが必要
- 提案された方法では、転移学習とメタ学習を通じてDGMに人工帰納バイアスを生成
- 転移学習のプリトレーニングやモデル平均化がメタ学習より優れると比較実証
- 実験で変分オートエンコーダーと生成的敵対ネットワークを使用し、生成データの質が最大50%向上

制約が多い中で良質な合成データを作るアイデア、すごく面白そう！特に医療や金融分野での応用が楽しみだね。

**Comment:** 19 pages, 6 Figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, I.2.0, **投稿日時:** 2024-07-03 12:53

- - -

### [Federated Learning for Zero-Day Attack Detection in 5G and Beyond V2X Networks](http://arxiv.org/abs/2407.03070)

**5Gおよび次世代V2Xネットワークにおけるゼロデイ攻撃検出のための連合学習**

Abdelaziz Amara korba, Abdelwahab Boualouache, Bouziane Brik, Rabah Rahal, Yacine Ghamri-Doudane, Sidi Mohammed Senouci

- 5G上の接続・自動運転車はセキュリティとプライバシー攻撃に脆弱
- 従来の手法は新しい攻撃（ゼロデイ攻撃）を検出する能力に限界がある
- 深層オートエンコーダーを用い、善良なネットワークトラフィックパターンのみで攻撃検出を行う新手法を提案
- 連合学習を用いて、プライバシーを保持しつつ多様な善良なデータでモデルを訓練、高い検出率と低い誤検出率を実現

ゼロデイ攻撃を連合学習で検出するってすごい！5Gの自動運転車の安全性がさらに向上しそうだね。将来のセキュリティ対策にも期待大だな〜。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-07-03 12:42

- - -

### [On the Client Preference of LLM Fine-tuning in Federated Learning](http://arxiv.org/abs/2407.03038)

**連合学習における大規模言語モデル微調整のクライアントの好みに関する研究**

Feijie Wu, Xiaoze Liu, Haoyu Wang, Xingchen Wang, Jing Gao

- 人間のフィードバックを用いる強化学習（RLHF）で、事前学習済み大規模言語モデル（LLM）を人間の好みデータセットで微調整
- プライバシーの懸念から、様々なクライアントによって保持される好みデータセットを共有せずにRLHFを実装する必要がある
- クライアントが協力してバイナリセレクターを訓練する枠組み「FedBis」を提案し、それを用いてLLMの生成を改善
- クライアントを好みに基づいてバランスよく分割したクラスターで複数のセレクターを訓練する新アルゴリズム「FedBiscuit」を提案し、これが従来の手法を上回る性能を示した

クライアントのプライバシーを守りつつ、好みに応じたデータを活用する方法が面白そう！プライバシーとパフォーマンスを両立する技術、これからもっと注目されそうだね。

**Comment:** Work in progress

**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.DC, cs.LG, **投稿日時:** 2024-07-03 12:02

- - -

### [Automated Verification of Higher-Order Probabilistic Programs via a Dependent Refinement Type System](http://arxiv.org/abs/2407.02975)

**依存型洗練型システムによる高次確率プログラムの自動検証**

Satoshi Kura, Hiroshi Unno

- 高次確率プログラムの検証は困難であるが、本研究では複数の量的特性をサポートする方法を提案
- 提案手法は既存のツールの互換性を損なわず、最小限の変更で量的特性を扱える
- 依存型洗練型システムと高次固定点論理を用いることで、連続分布や条件付きの量的特性を考慮可能
- 既存のCHCソルバーを小さな変更で拡張し、具体例の検証能力を実証

新しい手法で既存ツールを活用できるってほんと便利だよね！最小限の変更で高次確率プログラムも楽々検証できるようになりそうでワクワクしちゃう。

**Comment:** 60 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LO, **投稿日時:** 2024-07-03 10:17

- - -

### [Zero-X: A Blockchain-Enabled Open-Set Federated Learning Framework for Zero-Day Attack Detection in IoV](http://arxiv.org/abs/2407.02969)

**Zero-X: ブロックチェーンを活用したIoVにおけるゼロデイ攻撃検知のためのオープンセット連合学習フレームワーク**

Abdelaziz Amara korba, Abdelwahab Boualouache, Yacine Ghamri-Doudane

- IoV(インターネット・オブ・ビークル)は、ITS（インテリジェント輸送システム）において重要な技術である
- Zero-Xフレームワークは深層ニューラルネットワークとオープンセット認識を組み合わせ、0-dayおよびN-day攻撃を検知
- ブロックチェーン技術を用いた信頼性の高い分散型連合学習を導入し、プライバシー保護を優先
- 実験結果では高い検知率と低い誤検知率を達成し、関連する既存の解決策を上回る性能を示す

IoVの進化ってすごい！未来の交通システムが安全に保たれるんだね。Zero-Xがどんな風に現実に役立つのか見てみたいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-07-03 10:06

- - -

### [ObfuscaTune: Obfuscated Offsite Fine-tuning and Inference of Proprietary LLMs on Private Datasets](http://arxiv.org/abs/2407.02960)

**ObfuscaTune: プライベートデータセットでプロプライエタリLLMのオフサイト微調整と推論のための秘匿化技術**

Ahmed Frikha, Nassim Walha, Ricardo Mendes, Krishna Kanth Nakka, Xue Jiang, Xuebing Zhou

- この研究は、モデル提供者とデータ所有者間での秘密保持を保証しながら、プロプライエタリ言語モデルの推論と微調整を行う問題を解決する
- 提案するObfuscaTuneは、単純かつ効果的な秘匿化技術と秘密計算の効率的な使用を組み合わせたアプローチである
- ObfuscaTuneはGPT-2モデルを使用した実証により、その有効性を四つのNLPベンチマークデータセットで検証
- ナイーブアプローチと比較し、乱数行列を使用することで秘匿化によるエラーを軽減し、精度を向上させる必要性を示した

第三者クラウド上での微調整なんて、未来の技術って感じでワクワクするね！秘匿化しても精度が落ちないなんて、すごいなぁ。

**Comment:** Preprint

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.AI, cs.CL, cs.LG, **投稿日時:** 2024-07-03 09:54

- - -

### [Federated Fine-Tuning for Pre-Trained Foundation Models Over Wireless Networks](http://arxiv.org/abs/2407.02924)

**無線ネットワーク上での事前学習基盤モデルの連合ファインチューニング**

Zixin Wang, Yong Zhou, Yuanming Shi, Khaled. B. Letaief

- 事前学習基盤モデル(Foundation Models)を個別化するのに大量のタスク固有のデータと計算資源が必要
- 連合ファインチューニング(FedFT)は、低ランク適応(LoRA)と連合学習(FL)の統合により、個別化を達成しつつ生データプライバシーを保護
- エッジデバイスの限られた無線リソースと計算能力が、無線ネットワーク上での連合LoRAの展開を困難にする
- 提案する分割連合LoRAフレームワークは、エッジサーバーに計算集約型エンコーダを配置し、エッジデバイスに埋め込みとタスクモジュールを保持、学習性能向上を実証

分割連合LoRAフレームワークは、限られたリソースを効率的に活用するための新しいアプローチだね。オンラインアルゴリズムの効果をシミュレーションで見たら、期待できそうでワクワクした！



**トピック:** [連合学習](fl), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-07-03 08:56

- - -

### [Joint Optimization of Resource Allocation and Data Selection for Fast and Cost-Efficient Federated Edge Learning](http://arxiv.org/abs/2407.02888)

**高速でコスト効率の高い連合エッジ学習のためのリソース配分およびデータ選択の共同最適化**

Yunjian Jia, Zhen Huang, Jiping Yan, Yulu Zhang, Kun Luo, Wanli Wen

- 連合エッジ学習（FEEL）は通信リソースの制約と誤ラベルデータの影響を受けやすい
- リソース配分やデータ選択が不適切だと収束速度が遅くなり、訓練コストが増加
- 本研究はリソース配分とデータ選択の共同最適化問題を変数変換して解決
- 提案手法の優位性を数値結果で確認、低複雑なサブ最適アルゴリズムを開発

リソースとデータの最適化でこんなに効率が上がるんだね！未来のデータ処理がもっと速くて安くなるの楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-03 08:03

- - -

### [FedPot: A Quality-Aware Collaborative and Incentivized Honeypot-Based Detector for Smart Grid Networks](http://arxiv.org/abs/2407.02845)

**FedPot：スマートグリッドネットワークのための品質認識型共同・インセンティブ付きハニーポットベース検出器**

Abdullatif Albaseer, Nima Abdi, Mohamed Abdallah, Marwa Qaraqe, Saif Alkuwari

- ハニーポット技術は産業用IoTのセキュリティを強化し、特に高度計測インフラストラクチャの安全性を向上させる。
- 小規模電力供給業者がハニーポットの実装とデータ共有に参加し、伝統的な電力小売業者がインセンティブを提供する。
- 連合学習を利用して、セキュリティ防御モデルとインセンティブシステムの機能強化を図る。
- 提案されたFedAvgアルゴリズムとFedPotモデルが、セキュリティ強化と公平な報酬分配で最先端技術を上回る成果を示す。

ハニーポットと連合学習の組み合わせって、新しいアプローチだよね。電力網のセキュリティ向上とインセンティブの両立って、未来に向けて期待が持てる内容だと思うな！

**Comment:** Accepted for IEEE TNSM

**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, **投稿日時:** 2024-07-03 06:47

- - -

### [Large language models, physics-based modeling, experimental measurements: the trinity of data-scarce learning of polymer properties](http://arxiv.org/abs/2407.02770)

**大規模言語モデル、物理ベースモデル、実験測定：高分子特性のデータ不足を解決する三位一体**

Ning Liu, Siavash Jafarzadeh, Brian Y. Lattimer, Shuna Ni, Jim Lua, Yue Yu

- 大規模言語モデル(LLM)は、高速で正確な材料モデリング手法として有望
- データ不足を克服するために、物理ベースのトレーニングパイプラインを提案
- 合成データを用いた物理ベースのモデリングで初期状態を整え、実験データで微調整する二段階訓練戦略を採用
- 高分子の燃焼性測定指標の学習において、有効性を実証

大規模言語モデルを材料科学に応用するなんて、めっちゃ面白そう！実験データが少なくても、こうやって精度を上げられるのは画期的だね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CE, **投稿日時:** 2024-07-03 02:57

- - -

### [Towards Federated Learning with On-device Training and Communication in 8-bit Floating Point](http://arxiv.org/abs/2407.02610)

**8ビット浮動小数点によるデバイス上での訓練と通信を用いた連合学習の実現に向けて**

Bokun Wang, Axel Berg, Durmus Alp Emre Acar, Chuteng Zhou

- FP8での訓練は、FP32/FP16に比べて計算コストが低い
- 連合学習でFP8訓練を使用、クライアントサーバー間の通信コストも削減
- FP8クライアント訓練とグローバルFP32サーバーモデルを組み合わせる新手法を提案
- 実験により、FP32ベースラインと比較して通信が最低でも2.9倍削減

8ビット浮動小数点を使ったコスト削減と効率がとても気になる！連合学習の未来がさらに広がりそうでワクワクだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-07-02 18:55

- - -

### [Diffusion Models for Tabular Data Imputation and Synthetic Data Generation](http://arxiv.org/abs/2407.02549)

**表形式データの補完および合成データ生成のための拡散モデル**

Mario Villaizán-Vallelado, Matteo Salvatori, Carlos Segura, Ioannis Arapakis

- 拡散モデルは、画像や音声など複雑なデータ分布を生成する強力なモデルとして登場
- この論文は、表形式データに特化した拡散モデルを提案し、3つの重要な改良を行った
- 提案するモデルの評価は、機械学習効率、統計的類似性、プライバシーリスク軽減の3つの基準に焦点
- 提案手法は、欠損データの補完および合成データ生成において既存技術と比較して性能を検証

表形式データの補完と生成で拡散モデル使うんだ！医療や金融データの扱いがもっと簡単になりそうで期待が持てるね。

**Comment:** 25 pages, 7 figures, 6 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-02 15:27
