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

更新: 2024-05-15T04:19:38.637573

- - -

### [Using autoencoders and deep transfer learning to determine the stellar parameters of 286 CARMENES M dwarfs](http://arxiv.org/abs/2405.08703)

**オートエンコーダーと深層転移学習を用いた286個のCARMENES M矮星の星パラメータの決定**

P. Mas-Buitrago, A. González-Marcos, E. Solano, V. M. Passegger, M. Cortés-Contreras, J. Ordieres-Meré, A. Bello-García, J. A. Caballero, A. Schweitzer, H. M. Tabernero, D. Montes, C. Cifuentes

- M矮星の星パラメータ決定に深層学習が有望であり、転移学習が結果の不確実性を軽減する鍵となる
- オートエンコーダーを用いた特徴ベースの深層転移学習アプローチを提案し、高解像度スペクトルを用いて星パラメータを推定
- 合成PHOENIX-ACESスペクトルと観測CARMENESスペクトルを低次元空間に投影し、畳み込みニューラルネットワークを用いて星パラメータを決定
- 約3050～4300K、4.7～5.1dex、-0.53～0.25dexの範囲で整合性があり、特に3750K以上の有効温度で体系的な偏差が見られる

M矮星の特徴ってなんだか神秘的だね！未来ではもっと精密に星の性質が解明されるんだろうな。とてもワクワクする！

**Comment:** Accepted in A&A

**トピック:** [合成データ](sd), **カテゴリ:** astro-ph.SR, astro-ph.EP, astro-ph.IM, cs.LG, **投稿日時:** 2024-05-14 15:42

- - -

### [Byzantine-Resilient Secure Aggregation for Federated Learning Without Privacy Compromises](http://arxiv.org/abs/2405.08698)

**プライバシーを損なわない連合学習のためのビザンチン耐性セキュアアグリゲーション**

Yue Xia, Christoph Hofmeister, Maximilian Egger, Rawad Bitar

- 連合学習は大規模機械学習に有望ながらプライバシーとセキュリティの新たなリスクがある
- ByITFLはビザンチンユーザに対しレジリエンスを提供し、プライバシーを維持
- この手法は非プライベートなFLTrustを基にし、信頼スコアでユーザの勾配を調整
- ByITFLは情報理論的プライバシーを持つ初のビザンチン耐性スキーム

ビザンチンユーザに耐えるだけでなく、プライバシーも守れるなんてすごいね！これを使えば、大規模データの解析がもっと安全になりそう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, cs.CR, cs.DC, cs.LG, math.IT, **投稿日時:** 2024-05-14 15:37

- - -

### [Archimedes-AUEB at SemEval-2024 Task 5: LLM explains Civil Procedure](http://arxiv.org/abs/2405.08502)

**Archimedes-AUEBによるSemEval-2024タスク5: 大規模言語モデルが民事訴訟を解説する**

Odysseas S. Chlapanis, Ion Androutsopoulos, Dimitrios Galanis

- 複雑な法的概念を理解し推論するために、大規模言語モデル（LLM）が主に分類タスクで使用されている
- Powerful teacher-LLM（ChatGPT）を使用してトレーニングデータセットに説明を追加し、合成データを生成
- 新たな`mutation`メソッドで既存データを基に人工データを生成し、より優れた推論能力を提供
- このシステムはSemEval競技会で15位にランクインし、法的専門家によって人間の分析と一致する説明が確認された

この研究は、法的推論をLLMの限界を超えて発展させる面白い試みだね。特に、合成データを活用してモデルの性能をさらに高めるアプローチが未来の法技術に大きく貢献しそう！

**Comment:** To be published in SemEval-2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-05-14 11:04

- - -

### [Differentially Private Federated Learning: A Systematic Review](http://arxiv.org/abs/2405.08299)

**差分プライバシーに基づく連合学習: システマティックレビュー**

Jie Fu, Yuan Hong, Xinpeng Ling, Leixia Wang, Xun Ran, Zhiyu Sun, Wendy Hui Wang, Zhili Chen, Yang Cao

- 差分プライバシーは連合学習におけるプライバシー保護の標準である
- 既存の分類は、連合学習の対象およびプライバシー保護レベルの考慮が不足
- 新しい分類法を提案し、定義と保証に基づく保護オブジェクトを明示
- 連合学習シナリオにおける差分プライバシーの応用と今後の研究方向を示唆

差分プライバシーと連合学習の組み合わせって、めっちゃ面白くなりそう！未来のプライバシー技術が一歩進んだ感じがするね。

**Comment:** 37pages

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-05-14 03:49

- - -

### [Towards Energy-Aware Federated Learning via MARL: A Dual-Selection Approach for Model and Client](http://arxiv.org/abs/2405.08183)

**エネルギー対応連合学習に向けたMARL: モデルとクライアントのデュアル選択アプローチ**

Jun Xia, Yiyu Shi

- 連合学習は異種AIoTデバイス間の知識共有に有望だが、バッテリー駆動のシナリオで制約が多い
- 「木桶の原理」で、同質モデルと異種デバイス能力の不一致が原因でトレーニングが効率的に行えない
- DR-FLというエネルギー対応FLフレームワークを提案し、マルチエージェント強化学習に基づくデュアル選択を採用
- DR-FLはエネルギー制約下で知識共有を最大化し、各異種デバイスのモデル性能も向上させる

DF-FLのアイディア、新しいアプローチでめちゃ楽しそう！エネルギー難しい問題解決に貢献しそうでワクワクするよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-13 21:02

- - -

### [PrivFED -- A Framework for Privacy-Preserving Federated Learning in Enhanced Breast Cancer Diagnosis](http://arxiv.org/abs/2405.08084)

**PrivFED -- 強化型乳がん診断におけるプライバシー保護連合学習フレームワーク**

Maithili Jha, S. Maitri, M. Lohithdakshan, Shiny Duela J, K. Raja

- 医療機関でのPIIデータ交換が多く、サイバーセキュリティ脅威が存在
- データ欠乏と不均衡を軽減するため、連合学習フレームワークを導入
- SMOTEとIsolation Forestsを使用し、モデルの堅牢性を強化
- PCAとCatboostを活用し、エッジデバイスで99.95%、サーバーで98%の平均精度を達成

連合学習でのプライバシー保護は特に医療分野でめっちゃ重要だよね！しかも、99.95%の精度って本当にすごいよ。

**Comment:** Presented in ICIITB 2024 organized by Modern College of Business and   Science, Oman

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-13 18:01

- - -

### [Mitigating federated learning contribution allocation instability through randomized aggregation](http://arxiv.org/abs/2405.08044)

**ランダム化集約による連合学習貢献配分の不安定性の緩和**

Arno Geimer, Beltran Fiz, Radu State

- 連合学習はプライバシーを保ちながら堅牢なモデルを作成する新しい枠組み
- 貢献配分の不公平が参加者の信頼を損ね、未来の参加意欲を低下させる可能性
- Shapley値を用いた勾配ベースのモデル再構築技術で、既存の集約技術が不安定
- FedRandomという新しい集約技術を提案し、公正かつ正確な貢献評価を実現

貢献の配分が公平になると、参加者ももっと安心して取り組めるよね。この技術が広まればデータももっと活用されそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-13 13:55

- - -

### [HRNet: Differentially Private Hierarchical and Multi-Resolution Network for Human Mobility Data Synthesization](http://arxiv.org/abs/2405.08043)

**HRNet: 人間の移動データ生成のための階層的かつ多解像度の差分プライバシーネットワーク**

Shun Takagi, Li Xiong, Fumiyuki Kato, Yang Cao, Masatoshi Yoshikawa

- 人間の移動データは都市計画やパンデミック対応に貢献するが、プライバシー問題がある
- HRNetは、差分プライバシーを保証しつつリアルな移動データを生成するために設計された新しいモデル
- 階層的な位置エンコーディング、多解像度でのマルチタスク学習、プライベートな事前トレーニングを統合
- 現実のデータセットを用いた徹底比較実験で、既存手法に対する有用性とプライバシーのバランスを改善

人間の移動データを大事にしつつ使えるってすごいよね！これからの都市計画にワクワクしそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-05-13 12:56
