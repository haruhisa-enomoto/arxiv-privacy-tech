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

更新: 2024-08-16T04:19:46.572676

- - -

### [InVAErt networks for amortized inference and identifiability analysis of lumped parameter hemodynamic models](http://arxiv.org/abs/2408.08264)

**逆方向のネットワークを用いた一括パラメータ血行モデルの推論と識別可能性分析**

Guoxiang Grayson Tong, Carlos A. Sing Long, Daniele E. Schiavazzi

- 心血管モデル推定が難しいのは識別可能性の欠如が原因
- 最適化やベイズ推論は正則化を使用し、複数解の発見を制限
- inVAErtネットワークを用いて剛性動力系のデジタルツイン分析を強化
- 合成データから実データまで、inVAErtネットワークの柔軟性と効果を実証

心臓とか血行モデルとか、健康とかのデータをもっと上手に使えるようになるっぽい～！inVAErtネットワークってなんだかSFっぽくてワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** math.NA, cs.AI, cs.CE, cs.LG, cs.NA, **投稿日時:** 2024-08-15 17:07

- - -

### [Federated Fairness Analytics: Quantifying Fairness in Federated Learning](http://arxiv.org/abs/2408.08214)

**連合フェアネス分析: 連合学習におけるフェアネスの定量化**

Oscar Dilley, Juan Marcelo Parra-Ullauri, Rasheed Hussain, Dimitra Simeonidou

- 連合学習（FL）は、中央集権的なデータ収集を回避しつつ、モデルを分散的に学習する技術である
- FLはヘルスケアや金融、個人用コンピューティングでの利用が増えているが、従来のMLと同様にフェアネスの課題が存在する
- 本研究では、フェアネスを測定するための新たな方法論「連合フェアネス分析」を提案し、XAIや協力ゲーム理論、ネットワーク工学の手法を活用する
- 実験結果から、統計的な異質性とクライアントの参加がフェアネスに影響を及ぼし、「Ditto」や「q-FedAvg」のような手法が僅かにフェアネス・パフォーマンスのトレードオフを改善することが示された

連合学習って、いろんなデータの偏りにどう対応するのか気になるところだよね。この研究、フェアネスの改善に役立つ具体的な方法を提案してくれそうで面白そう！



**トピック:** [連合学習](fl), [PETs](pets), **カテゴリ:** cs.LG, cs.AI, cs.DC, cs.GT, cs.NE, **投稿日時:** 2024-08-15 15:23

- - -

### [Communication-robust and Privacy-safe Distributed Estimation for Heterogeneous Community-level Behind-the-meter Solar Power Generation](http://arxiv.org/abs/2408.08107)

**異質なコミュニティレベルでのメーター背後の太陽光発電の通信に強くプライバシーを安全にする分散推定**

Jinglei Feng, Zhengshuo Li

- メーター背後の太陽光発電システムの増加により、配電系統計画とスケジュールが複雑になる
- 従来の連合学習方法は、異質性、通信障害、悪意のあるプライバシー攻撃などの課題に直面している
- 提案手法はマルチタスク連合学習を採用し、全コミュニティの共通および固有の特徴を学習する
- 差分プライバシーメカニズムを使用し、動的なプライバシーバジェット配分戦略を採用してプライバシー攻撃に対抗

通信もプライバシーもバッチリで、未来のエネルギー管理に貢献しそう！これが実現したら、もっと効率よく安全に電力を使えるね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-08-15 12:11

- - -

### [I-SHEEP: Self-Alignment of LLM from Scratch through an Iterative Self-Enhancement Paradigm](http://arxiv.org/abs/2408.08072)

**I-SHEEP: LLMをゼロから自動調整する反復自己強化パラダイム**

Yiming Liang, Ge Zhang, Xingwei Qu, Tianyu Zheng, Jiawei Guo, Xinrun Du, Zhenzhu Yang, Jiaheng Liu, Chenghua Lin, Lei Ma, Wenhao Huang, Jiajun Zhang

- LLMは従来の学習方法では受動的な情報貯蔵庫として扱われるが、能動的学習と自己調整の可能性がある
- I-SHEEPは人間のようにゼロから連続的に自己調整するパラダイムを導入
- Dromedary法と比較して、QwenとLlamaモデルで最大78.2%の相対的改善を達成
- 標準ベンチマーク生成タスクでもベースモデルを上回り、平均24.77%の改善を実現

人間みたいに自己改善できるLLMなんてワクワクしちゃう！将来のAI学習方法がどんどん進化していきそうで楽しみ～。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-08-15 10:44

- - -

### [Reliable Communication in Hybrid Authentication and Trust Models](http://arxiv.org/abs/2408.08060)

**ハイブリッド認証と信頼モデルにおける確実な通信**

Rowdy Chotkan, Bart Cox, Vincent Rahli, Jérémie Decouchant

- 信頼できる通信は、ネットワーク全体の強力な通信プリミティブの基礎
- 既存の認証モデルを用いた2つのプロトコルが未知かつ十分に接続されたネットワークで信頼できる通信を実現
- ハイブリッドシステムモデルでは、認証リンクと認証プロセスを組み合わせ、信頼できるノードやコンポーネントを活用
- 新提案のDualRCアルゴリズムは、拡散経路とデジタル署名を操作し、ネットワークゲートウェイやIntel SGX enclavesなど信頼できるノードを活用

新しく提案されたアルゴリズムが、今までよりも強力で信頼性のある通信を可能にするのがすごく興味深い！ネットワークセキュリティの進化が楽しみだね。



**トピック:** [TEE](tee), **カテゴリ:** cs.DC, **投稿日時:** 2024-08-15 10:01

- - -

### [Practical Privacy-Preserving Identity Verification using Third-Party Cloud Services and FHE (Role of Data Encoding in Circuit Depth Management)](http://arxiv.org/abs/2408.08002)

**第三者クラウドサービスとFHEを用いた実用的なプライバシー保護型の身分証明確認（回路深度管理におけるデータエンコーディングの役割）**

Deep Inder Mohan, Srinivas Vivek

- 発展途上国でのデジタル身分証明システムのコスト削減と技術的課題がある
- 提案したプロトコルは、単一鍵の完全準同型暗号（FHE）を使用してデータを暗号化して処理
- データエンコーディング方式は、多様なID確認クエリを少ない暗号文で処理可能
- 認証機関による計算負担を最小限にし、「拡張」復号のみを行う設計

ID確認を完全準同型暗号でやっちゃうなんて未来的だし、本当に安全な感じだよね。これ、広まれば色々な国が採用しそうで楽しみ！

**Comment:** This work was presented (without proceedings) at the Turing   Trustworthy Digital Identity International Conference 2022 at The Alan Turing   Institute, London, UK, on Sep. 16, 2022

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-15 08:12

- - -

### [Polaris: Open-ended Interactive Robotic Manipulation via Syn2Real Visual Grounding and Large Language Models](http://arxiv.org/abs/2408.07975)

**Polaris: Syn2Real視覚グラウンドと大規模言語モデルによるオープンエンドのインタラクティブロボットマニピュレーション**

Tianyu Wang, Haitao Lin, Junqiu Yu, Yanwei Fu

- オープンエンドなインタラクティブロボットマニピュレーションに関する研究
- LLMsはユーザー指示理解を助力も視覚グラウンド欠如が物理的操作を制限
- PolarisフレームワークはGPT-4と視覚モデルの統合で精密な操作を実現
- Syn2Realポーズ推定パイプラインで合成データから実世界タスクへの適応を行う

視覚と言語を合体させることで、ロボットがもっと賢く動けるようになるなんてワクワクするよね！未来には、家庭でロボットが普通になってくれたら便利だなぁって思う。

**Comment:** Accepted by IROS 2024. 8 pages, 5 figures. See   https://star-uu-wang.github.io/Polaris/

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.CL, cs.CV, **投稿日時:** 2024-08-15 06:40

- - -

### [Addressing Skewed Heterogeneity via Federated Prototype Rectification with Personalization](http://arxiv.org/abs/2408.07966)

**個別化による連合プロトタイプ補正で偏った異質性に対処する**

Shunxin Guo, Hongsong Wang, Shuxia Lin, Zhiqiang Kou, Xin Geng

- 連合学習の課題として、偏ったプライベートデータの分布が存在する
- この論文では、より実用的かつ挑戦的な「Skewed Heterogeneous Federated Learning (SHFL)」を定義
- 提案手法は「連合個別化」と「連合プロトタイプ補正」で構成され、クラス間とクラス内の差異を活用
- 3つのベンチマーク実験で、提案手法が現行の最先端手法を上回り、個別化と一般化の両面でバランスの取れた性能を実現

新しい学習方法でデータ偏り問題を解決できるのはすごいね！連合学習を使うのってちょっと未来っぽいし、これからのAIモデルにめっちゃ役立ちそう💡



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-08-15 06:26

- - -

### [Time-Dependent VAE for Building Latent Factor from Visual Neural Activity with Complex Dynamics](http://arxiv.org/abs/2408.07908)

**複雑な動態を持つ視覚神経活動から潜在因子を構築するための時間依存VAE**

Liwei Huang, ZhengYu Ma, Liutao Yu, Huihui Zhou, Yonghong Tian

- 神経活動と行動や感覚刺激の内在的な相関を明らかにするため、質の高い神経潜在表現の探索が重要
- 従来のモデルは行動情報に依存し固定時間スケールに制約されるため、自由視聴の視覚神経活動では困難
- Time-Dependent SwapVAEを提案し、内容とスタイル空間を分離させ時間依存の状態変数を導入
- 自己教師付きコントラスト学習を利用し、任意の長さの神経活動シーケンスから複雑な動態を効果的に解析

視覚神経活動から直接的に有用な情報を引き出すこの方法、かなり革新的かも！神経活動データをこんな形で使えるなんて、面白そうだよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.NE, q-bio.NC, **投稿日時:** 2024-08-15 03:27

- - -

### [Enhancing Equitable Access to AI in Housing and Homelessness System of Care through Federated Learning](http://arxiv.org/abs/2408.07845)

**連合学習による住宅およびホームレス支援システムにおける公平なAIアクセスの強化**

Musa Taib, Jiajun Wu, Steve Drew, Geoffrey G. Messier

- 住宅およびホームレス支援システム（HHSC）の主要目標はホームレス状態の人々を支援住宅に繋げること
- 各機関のITプラットフォームは異なり、データが孤立しているため、データの共有が困難
- 連合学習（FL）によって、全機関がセンシティブなデータを共有せずに予測モデルを協力してトレーニングできる
- カルガリーの実データを用いた実験結果は、データを完全に共有した理想的なシナリオと同等の性能を示す

連合学習って、各機関がデータを共有しなくても協力できるんだね。これってすごく未来感あるし、プライバシーも守れるから安心だね！

**Comment:** Accepted at the 2024 AAAI/ACM Conference on AI, Ethics, and Society   (AIES)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CY, **投稿日時:** 2024-08-14 23:01

- - -

### [Graph neural network surrogate for strategic transport planning](http://arxiv.org/abs/2408.07726)

**戦略的交通計画のためのグラフニューラルネットワーク代理モデル**

Nikita Makarov, Santhanakrishnan Narayanan, Constantinos Antoniou

- 都市環境の複雑化に伴い、交通システムのモデリングが困難に
- GCNに基づく既存のモデルとGATを比較分析
- 新しいGATのバリアント（GATv3）を提案し、過平滑化問題に対応
- 合成データ生成でトレーニングデータを増やし、GCNの性能向上を実証

グラフニューラルネットワークで交通計画をもっとスマートにできる未来、楽しみ！新しいGATv3の提案も面白そうで、実現すれば大きな変革が期待できそうだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-08-14 14:18
