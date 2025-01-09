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

更新: 2025-01-09T04:22:56.719060

- - -

### [URSA: Understanding and Verifying Chain-of-thought Reasoning in Multimodal Mathematics](http://arxiv.org/abs/2501.04686)

**URSA: マルチモーダル数学における思考過程推論の理解と検証**

Ruilin Luo, Zhuofan Zheng, Yifan Wang, Yiyao Yu, Xinzhe Ni, Zicheng Lin, Jin Zeng, Yujiu Yang

- マルチモーダル数学の推論で、高品質な思考過程データの不足が課題
- 三つのモジュールを統合した戦略で高品質データセットMMathCoT-1Mを作成
- 新たなデータ合成戦略でDualMath-1.1Mを生成し、解釈と論理に注力
- URSA-RM-7BがURSA-7Bのテスト時パフォーマンスを向上させOの一般化も実現

思考過程推論の話って新しい感じでめちゃ興味があるなあ。マルチモーダルでの解析でどんな応用が見つかるのかな、ちょっとわくわくしてくる！

**Comment:** 27 pages, 10 tables, 17 figures. The training data has been released.   The code and model are currently undergoing internal review. They will be   made available soon. Project url: https://ursa-math.github.io

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2025-01-08 18:49

- - -

### [Towards System 2 Reasoning in LLMs: Learning How to Think With Meta Chain-of-Though](http://arxiv.org/abs/2501.04682)

**連合学習におけるムラエレクトロンのプライバシー強化**

Violet Xiang, Charlie Snell, Kanishk Gandhi, Alon Albalak, Anikait Singh, Chase Blagden, Duy Phung, Rafael Rafailov, Nathan Lile, Dakota Mahan, Louis Castricato, Jan-Philipp Franken, Nick Haber, Chelsea Finn

- Meta-CoTは伝統的なChain-of-Thoughtを拡張し、推論プロセスを明示的にモデル化
- 基礎モデルの行動を観察し、コンテキスト内検索との一貫性を示す
- Meta-CoTの生成にはプロセス監視、合成データ生成、探索アルゴリズムを活用
- 線形検索トレースと強化学習の後処理を組み込み、モデル訓練パイプラインを具体化

この方式で、AIにもっと賢くて人間っぽい考え方を身につけさせるんだって。Meta-CoTを使うと、新しい推論アルゴリズムが見つかりそうでワクワクする～！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, **投稿日時:** 2025-01-08 18:42

- - -

### [Enhancing Virtual Try-On with Synthetic Pairs and Error-Aware Noise Scheduling](http://arxiv.org/abs/2501.04666)

**合成ペアとエラー対応型ノイズスケジューリングによるバーチャル試着の強化**

Nannan Li, Kevin J. Shih, Bryan A. Plummer

- バーチャル試着には、ペアデータの少なさとテクスチャの歪みの課題がある
- 合成ペアを生成し、トレーニングデータを増強することで課題を改善
- エラー認識型の改良モデルで生成エラーを局所的に修正
- 合成データと新手法で従来の手法を上回る成果を実証し、ユーザー評価でも向上

バーチャル試着の精度がこんなに上がるんだって！今度、気になる洋服を以前より正確に試着できるかもね。ユーザーからも好評だから、いつか実装されたらワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2025-01-08 18:25

- - -

### [MedCoDi-M: A Multi-Prompt Foundation Model for Multimodal Medical Data Generation](http://arxiv.org/abs/2501.04614)

**MedCoDi-M: マルチモーダル医療データ生成のための多プロンプト基盤モデル**

Daniele Molino, Francesco Di Feola, Eliodoro Faiella, Deborah Fazzini, Domiziana Santucci, Linlin Shen, Valerio Guarrasi, Paolo Soda

- AIは医療の診断精度と提供を向上させるが、データの不足とプライバシーの制約が課題
- 合成データはプライバシーを守りつつデータ不足を緩和する有力な解決策である
- MedCoDi-Mはマルチモーダル医療データ生成モデルで、対比学習と多量データでラテント空間を構築
- 医療の匿名化やデータ不足問題の解決において、MedCoDi-Mの有効性を実証済み

この研究、マルチモーダルデータを一括で生成できるなんてすごく画期的だよね！プライバシーを守りつつデータを有効活用できるなら、医療現場でもっと革新が起きそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.LG, **投稿日時:** 2025-01-08 16:53

- - -

### [MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data](http://arxiv.org/abs/2501.04595)

**モバイルH2R: スケーラブルかつ多様な合成データのみから学習する、汎用的な人からモバイルロボットへの受け渡し**

Zifan Wang, Ziqing Chen, Junyu Chen, Jilong Wang, Yuxin Yang, Yunze Liu, Xueyi Liu, He Wang, Li Yi

- 合成データを用いることで、実世界のデモに依存せずに汎用的な受け渡しスキルをシミュレーターで開発
- 多様な合成人体動作データ生成のためのスケーラブルなパイプラインを提案し、安全かつ模倣しやすいデモを実現
- 大規模なデモを基にした4次元模倣学習により、基底とアームの協調による閉ループポリシー生成を効率化
- 実験では、ベースラインに対し少なくとも15%の成功率向上、合成データの効果を実証

モバイルロボットがこんなにスムーズに物を受け取れるなんて、未来感が強すぎる！合成データだけでこんなに進化できるのが信じられないけど、ほんとにロボ研究の最前線って感じだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2025-01-08 16:23

- - -

### [Gradient Purification: Defense Against Poisoning Attack in Decentralized Federated Learning](http://arxiv.org/abs/2501.04453)

**勾配浄化: 分散型連合学習における毒攻撃防御**

Bin Li, Xiaoye Miao, Yongheng Shang, Xinkui Zhao, Shuiguang Deng, Jianwei Yin

- 分散型連合学習は毒攻撃の影響を受けやすく、悪意のあるクライアントからの勾配が問題。
- 提案する勾配浄化技術は、既存の連合学習と統合して毒攻撃を防ぐ新しい手法。
- 悪意のある隣接クライアントを検出し、悪影響を歴史的に一貫したチェックで軽減する。
- 3つのデータセットでの実験結果、提案手法は最先端よりも高い精度で毒攻撃を防ぐ。

勾配浄化っていう新しいアプローチで、従来捨てられてた有用な部分を活かせるようにしてるんだね！これで毒攻撃への対策がさらに進んだら、もっと安全なモデルができて、連合学習の未来はもっと明るくなりそうだよね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2025-01-08 12:14

- - -

### [Revisiting LocalSGD and SCAFFOLD: Improved Rates and Missing Analysis](http://arxiv.org/abs/2501.04443)

**LocalSGDとSCAFFOLDの再検討: 改善された速度と不足していた分析**

Ruichen Luo, Sebastian U Stich, Samuel Horváth, Martin Takáč

- LocalSGDとSCAFFOLDは連合学習で広く使用されるが、理論的優位性の証明が難しい
- LocalSGDは弱凸関数においてMbSGDより速い収束を示し、強い勾配類似の仮定が不要
- LocalSGDは高次の類似性と滑らかさから大きな利益を得る
- SCAFFOLDは非二次関数の広範なクラスでMbSGDよりも速い収束を実現する

LocalSGDとSCAFFOLDの利点が明確に示されてて、この技術を使った新しいことができそう！効果的な分散最適化の可能性がありそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** math.OC, cs.DC, cs.LG, **投稿日時:** 2025-01-08 11:52

- - -

### [Federated Fine-Tuning of LLMs: Framework Comparison and Research Directions](http://arxiv.org/abs/2501.04436)

**LLMの連合微調整：フレームワーク比較と研究の方向性**

Na Yan, Yang Su, Yansha Deng, Robert Schober

- 連合学習により、データプライバシーを保ちながらLLMをタスクに特化させる
- LLMの微調整は通信と計算コストが高く、リソース制約のある環境で困難
- 各フレームワークの評価はモデル精度、通信負荷、クライアント側の計算負荷に基づく
- フレームワークごとの最適化の機会や実世界への適用における課題を示す

これって、連合学習を活用してデータを守りながらも、モデルを上手く調整するための研究なんだね。高性能ながら省エネな方法が大事だから、これからの技術進化が楽しみ！みんなで効率よくAIを使える未来が来るかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2025-01-08 11:37

- - -

### [User Simulation in the Era of Generative AI: User Modeling, Synthetic Data Generation, and System Evaluation](http://arxiv.org/abs/2501.04410)

**生成AI時代におけるユーザーシミュレーション: ユーザーモデリング、合成データ生成、システム評価**

Krisztian Balog, ChengXiang Zhai

- ユーザーシミュレーションは、ユーザーの行動を模倣する知能エージェントを創造する技術である。
- 合成データ生成のためにユーザー行動をモデリングし、AIシステムを効果的に評価する。
- 多様な分野に影響を与え、汎用人工知能の追求において重要な役割を担う。
- 重要性が増すこの技術の応用や学際的な関連を概観し、未来の研究方向性を示す。

ユーザーシミュレーションなんて未来っぽくてワクワクするね！これが進化したら、AIはもっと人間らしくなって、私たちと感情を持って接してくれるようになるのかな？それに、いろんな分野に応用できそうで夢が膨らむね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.HC, cs.IR, cs.LG, **投稿日時:** 2025-01-08 10:49

- - -

### [Lossless Privacy-Preserving Aggregation for Decentralized Federated Learning](http://arxiv.org/abs/2501.04409)

**分散型連合学習のための無損失プライバシー保護集約法**

Xiaoye Miao, Bin Li, Yangyang Wu, Meng Xi, Xinkui Zhao, Jianwei Yin

- 連合学習は勾配を集約するが、依然としてデータ漏洩のリスクがある
- 提案手法LPPAは、勾配にノイズ差を注入しプライバシーを守る
- ノイズフロー保存理論を用いて、ノイズの影響を無効化する
- LPPAは従来法より精度を13%改善し、データ保護を実現

この研究、すごく面白そう！データ保護しながらも精度を上げるなんて素敵すぎる。このアイデアが進化したら、もっと安心して連合学習を活用できそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2025-01-08 10:49

- - -

### [AutoDFL: A Scalable and Automated Reputation-Aware Decentralized Federated Learning](http://arxiv.org/abs/2501.04331)

**AutoDFL: スケーラブルで自動化された評判対応型分散連合学習**

Meryem Malak Dif, Mouhamed Amine Bouchiha, Mourad Rabah, Yacine Ghamri-Doudane

- 連合学習とブロックチェーンを組み合わせてプライバシーとセキュリティを強化するBFLは、スケーラビリティとコストの問題がある
- 評判を考慮したBFLではブロックチェーンの混雑と性能低下が起こりやすく、これがさらに複雑さを増す
- AutoDFLはzk-Rollupsを活用し、スケーラビリティを改善しつつレイヤー1と同等のセキュリティを維持
- 平均3000TPSを超えるスループットを達成し、最大20倍のガス削減を実現

AutoDFLってすごいじゃない？スケーラビリティも改善しちゃうなんて夢のようだよね！ブロックチェーンの混雑を避けつつ、高速な処理を目指すこの技術、ちょっと目が離せないね！

**Comment:** Paper accepted at NOMS'2025 (pages 9, figures 5)

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.CR, cs.ET, cs.LG, **投稿日時:** 2025-01-08 08:05

- - -

### [VerifBFL: Leveraging zk-SNARKs for A Verifiable Blockchained Federated Learning](http://arxiv.org/abs/2501.04319)

**VerifBFL: zk-SNARKsを活用した検証可能なブロックチェーン連合学習**

Ahmed Ayoub Bellachia, Mouhamed Amine Bouchiha, Yacine Ghamri-Doudane, Mourad Rabah

- 連合学習は中央サーバーを必要とせず、プライバシーを保護するが、攻撃の脆弱性がある
- VerifBFLはブロックチェーンと暗号技術を組み合わせた、信頼不要の検証可能な連合学習
- zk-SNARKsにより、ローカルトレーニングと集約の検証性を確保し、オンチェーンで監査可能にする
- 差分プライバシーを用いて学習データを保護し、プロトタイプで効率を実証

ブロックチェーンと連合学習の組み合わせ、めっちゃ革新的じゃない！検証も速くて、実用化が楽しみだね。

**Comment:** Paper accepted at NOMS'25 (9 pages, 6 Figures)

**トピック:** [連合学習](fl), [差分プライバシー](dp), [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.DC, cs.ET, cs.LG, **投稿日時:** 2025-01-08 07:32

- - -

### [HiCoCS: High Concurrency Cross-Sharding on Permissioned Blockchains](http://arxiv.org/abs/2501.04265)

**HiCoCS: 許可型ブロックチェーンにおける高並行クロスシャーディング**

Lingxiao Yang, Xuewen Dong, Zhiguo Wan, Di Lu, Yushu Zhang, Yulong Shen

- ブロックチェーンのスケーラビリティに対する需要が増加している
- 高並行クロスシャード取引が今まで十分に解決されていない課題である
- 独自のバーチャルサブブローカーにより競合のない取引処理が可能
- 準同型暗号を用いてプライバシー保護を強化し、スループットを大幅に改善

この論文、シャーディングとか仮想ブローカーとか、新しい技術アイデアがいっぱいでワクワクするね！特に、プライバシーを守りつつ効率化するってところがすごく魅力的だと思ったな～。これからのブロックチェーン技術の進化が楽しみだな！

**Comment:** Major Revised in IEEE TC

**トピック:** [準同型暗号](he), **カテゴリ:** cs.DC, **投稿日時:** 2025-01-08 04:19

- - -

### [Splicer: Secure Hub Placement and Deadlock-Free Routing for Payment Channel Network Scalability](http://arxiv.org/abs/2501.04236)

**Splicer$^{+}$: 支払いチャネルネットワークのスケーラビリティのための安全なハブ配置とデッドロックフリールーティング**

Lingxiao Yang, Xuewen Dong, Wei Wang, Sheng Gao, Qiang Qu, Wensheng Tian, Yulong Shen

- 現行の支払いチャネルハブは要求分布を考慮せず負荷不均衡を生む
- Splicer$^{+}$は信頼実行環境を用いて高スケーラビリティを実現する
- デッドロックを回避するためのルーティングプロトコルを設計
- トランザクション成功率やスループットで従来技術を大幅に上回る効果を示す

支払いチャネルの効率をこんなに改善できるなんてスゴイね！未来の支払いシステムがもっと使いやすくなるのかなってワクワクしちゃう。

**Comment:** Extended version of ICDCS 2023 (arXiv:2305.19182)

**トピック:** [TEE](tee), **カテゴリ:** cs.DC, **投稿日時:** 2025-01-08 02:30

- - -

### [Privacy-Preserving Distributed Online Mirror Descent for Nonconvex Optimization](http://arxiv.org/abs/2501.04222)

**プライバシー保護分散オンラインミラーディセントによる非凸最適化**

Yingjie Zhou, Tao Li

- 非凸関数の最適化問題を差分プライバシーで分散的に解く手法を検討
- ミラーディセントとラプラス差分プライバシー機構を使用してプライバシーを保護
- 非凸のコスト関数を許容し、適切なステップサイズで$\epsilon$-差分プライバシーを保証
- 局所コスト関数が滑らかであれば、後悔が時間の平方根に比例して増加

新しいプライバシー保護の最適化手法、すごい！未来の分散ネットワークの問題解決にもつながりそうでワクワクするね。実際の数値シミュレーションも効果的だったみたい！



**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2025-01-08 01:39

- - -

### [FedKD-hybrid: Federated Hybrid Knowledge Distillation for Lithography Hotspot Detection](http://arxiv.org/abs/2501.04066)

**FedKD-hybrid: リソグラフィーホットスポット検出のための連合ハイブリッド知識蒸留**

Yuqi Li, Xingyou Lin, Kai Zhang, Chuanguang Yang, Zhongliang Guo, Jianping Gou, Yanli Li

- 連合学習は分散環境でリソグラフィーホットスポット検出に新たな解決策を提供する
- 現在の方法は情報の完全な活用と転送がされておらず、潜在力が十分に探索されていない
- FedKD-hybridは、複数クライアントが公開データセットを使用しグローバルな合意を達成する手法を提案
- 実験結果ではFedKD-hybridが最新手法より優れた性能を示す

リソグラフィーって、私もちょっと気になる！FedKD-hybridで性能がアップするなんて面白そう！これから技術が進んでくのに役立ちそう♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AR, **投稿日時:** 2025-01-07 12:12

- - -

### [Homomorphic Encryption in Healthcare Industry Applications for Protecting Data Privacy](http://arxiv.org/abs/2501.04058)

**医療産業におけるデータプライバシー保護のための準同型暗号応用**

J. S. Rauthan

- 医療診断におけるニューラルネットワークと品質管理手法に準同型暗号を適用
- 準同型暗号のツールの進歩と実用アプリケーション間のギャップを検討
- 具体的なケーススタディと信頼モデルを基にリソースとパフォーマンス要件を評価
- 複雑なニューラルネットワークモデルと単純な品質管理アルゴリズムでの効果とリソース消費を示す

準同型暗号の医療分野への応用って新しい！理論から実践への進展がもっと加速するかもね。これからの医療データの安全な利用に期待大だよ！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.DC, cs.CR, **投稿日時:** 2025-01-07 07:42
