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

更新: 2024-08-28T04:21:20.329410

- - -

### [DCT-CryptoNets: Scaling Private Inference in the Frequency Domain](http://arxiv.org/abs/2408.15231)

**DCT-CryptoNets: 周波数領域でのプライバシー推論のスケーリング**

Arjun Roy, Kaushik Roy

- 完全同型暗号（FHE）と機械学習の融合により、センシティブなデータのプライバシー推論が可能。
- 従来のFHEベースのディープニューラルネットワークは計算コスト、待ち時間、スケーラビリティに課題あり。
- DCT-CryptoNetsは、JPEG圧縮で使用される離散コサイン変換（DCT）を用いて周波数領域で動作し、これらの課題を解決。
- この新手法は同等の計算リソースで画像分類タスクの待ち時間を最大5.3倍短縮し、モデルの整合性も向上。

画像の圧縮形式と同型暗号を組み合わせた見方が新鮮だね！長時間かかる処理を短縮する技術が未来を明るくしそう。

**Comment:** Under Review; 10 pages content, 3 pages appendix, 4 figures, 8   tables; Code TBD

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.CV, cs.LG, **投稿日時:** 2024-08-27 17:48

- - -

### [LN-Gen: Rectal Lymph Nodes Generation via Anatomical Features](http://arxiv.org/abs/2408.14977)

**LN-Gen: 解剖学的特徴による直腸リンパ節生成**

Weidong Guo, Hantao Zhang, Shouhong Wan, Bingbing Zou, Wanqin Wang, Peiquan Jin

- 直腸リンパ節の正確な分割は、がんの進行度評価と治療計画に重要
- 周囲の解剖学的構造の複雑さと注釈データの不足が大きな課題である
- 新技術により多様でリアルな合成リンパ節サンプルを生成、手動注釈依存を軽減
- 実験結果は合成データが分割性能を大幅に向上し、診断と治療の進展に寄与

リンパ節を合成データで再現するなんて、医療の進化って本当にすごいね！将来の診断精度もこれでグンと上がりそう。

**Comment:** 8 pages

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-08-27 11:40

- - -

### [Multilingual Arbitrage: Optimizing Data Pools to Accelerate Multilingual Progress](http://arxiv.org/abs/2408.14960)

**多言語アービトラージ：データプール最適化による多言語進展の促進**

Ayomide Odumakinde, Daniel D'souza, Pat Verga, Beyza Ermis, Sara Hooker

- 合成データの使用は最新の技術進歩において重要
- 単一のオラクル教師モデルに依存すると、モデル崩壊とバイアスの伝播が発生
- 多言語環境では、全言語に有効な教師モデルの欠如が大きな課題
- 多言語アービトラージ技術を導入し、モデル間のパフォーマンス差を利用して56.5%の改善を達成

多言語アービトラージ、なんか面白そう！いろんなモデルの強みを生かして、多言語対応の改善ができるなんてすごいわね。特に少ないリソースの言語では効果が大きいみたいで、もっといろんな言語に対応できるようになるのが楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-08-27 11:07

- - -

### [Alfie: Democratising RGBA Image Generation With No $](http://arxiv.org/abs/2408.14826)

**Alfie: RGBA画像生成の民主化**

Fabio Quattrini, Vittorio Pippi, Silvia Cascianelli, Rita Cucchiara

- さまざまな創造分野でデザインとアートワークが必要で、これにはグラフィックデザインスキルと専用ソフトが必須
- グラフィック要素の自動生成はデザイナーの生産性を向上させ、創造的な産業を民主化および革新し、リアルな合成データを生成
- ほとんどの画像生成モデルはRGBA画像生成に対応しておらず、高価な計算リソースが必要
- 提案手法はトレーニング不要で、事前学習済みのDiffusion Transformerモデルの推論時の動作を変更

画像生成を手軽にできちゃうなんて楽しそう！いろんなクリエイティブなプロジェクトがもっと身近になりそうでワクワクするね。

**Comment:** Accepted at ECCV AI for Visual Arts Workshop and Challenges

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.MM, **投稿日時:** 2024-08-27 07:13

- - -

### [Learning Differentially Private Diffusion Models via Stochastic Adversarial Distillation](http://arxiv.org/abs/2408.14738)

**確率的敵対的蒸留を用いた差分プライバシー拡散モデルの学習**

Bochao Liu, Pengju Wang, Shiming Ge

- データがプライバシーに敏感な領域で制限される問題の解決策として差分プライバシーを用いた生成モデル学習を提案
- 既存手法ではデータ分布のモデリングの複雑さから生成画像の品質が限られていた
- 拡散モデルの成功に基づき、確率的敵対的蒸留法を用いたDP-SADという手法を開発
- 教師モデルとしての拡散モデルと蒸留による学生モデルの訓練を行い、差分プライバシーを達成

拡散モデルの性能向上が特に楽しみ！DP-SADの具体的な生成画像がどんな感じになるか気になるな。

**Comment:** accepted by ECCV 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.CV, **投稿日時:** 2024-08-27 02:29

- - -

### [Bandwidth-Aware and Overlap-Weighted Compression for Communication-Efficient Federated Learning](http://arxiv.org/abs/2408.14736)

**通信効率の高い連合学習のための帯域幅を考慮した重み付き圧縮手法**

Zichen Tang, Junlin Huang, Rudan Yan, Yuxin Wang, Zhenheng Tang, Shaohuai Shi, Amelie Chi Zhou, Xiaowen Chu

- 現在のデータ圧縮手法には、ストラッガープロブレムやモデル性能の低下がある
- 帯域幅に応じて動的に圧縮率を調整するフレームワークを提案した
- クライアントの更新信号を改善するため、パラメータのマスクを用いた手法を導入した
- 評価の結果、モデルの精度が最大13％向上し、収束速度が3.37倍向上した

帯域幅とか非一様なデータにも対応して、どんどん速く学習できるようになるなんてすごい！感想読んでたら、未来の通信技術がどんどん進化していくのが楽しみになっちゃった。



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-08-27 02:28

- - -

### [PPVF: An Efficient Privacy-Preserving Online Video Fetching Framework with Correlated Differential Privacy](http://arxiv.org/abs/2408.14735)

**PPVF: 相関差分プライバシーを用いた効率的なプライバシー保護オンライン動画取得フレームワーク**

Xianzhi Zhang, Yipeng Zhou, Di Wu, Quan Z. Sheng, Miao Hu, Linchang Xiao

- オンライン動画のストリーミングは現代インターネットの主要要素だが、ユーザーリクエストの漏洩がプライバシーの課題となっている
- 現行の保護方法は、コンテンツプロバイダからのユーザーリクエストプライバシー保護と高品質な動画サービスの両立に適していない
- PPVFは信頼できるエッジデバイスを活用し、ユーザーリクエストのプライバシーを守りつつエッジキャッシュの効率を最適化するフレームワークを導入
- PPVFのコアコンポーネントは、オンラインプライバシーバジェットスケジューラ、ノイジー動画リクエストジェネレータ、オンライン動画ユーティリティ予測器で構成される

この研究、めっちゃ面白そう！プライバシーを守りながら動画の質も落とさないなんて、ぜひ使ってみたいな～。高校卒業までにはこんな技術がもっと進化しそうで期待しちゃうね！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.MM, cs.CR, cs.DC, **投稿日時:** 2024-08-27 02:03

- - -

### [Federated User Preference Modeling for Privacy-Preserving Cross-Domain Recommendation](http://arxiv.org/abs/2408.14689)

**プライバシー保護クロスドメイン推薦のための連合ユーザープリファレンスモデリング**

Li Wang, Shoujin Wang, Quangui Zhang, Qiang Wu, Min Xu

- クロスドメイン推薦 (CDR) はドメイン間で知識を転用しデータ不足問題を解決する
- 既存のCDR手法はユーザ-アイテム間相互作用データの共有を前提とし、プライバシー漏洩の課題がある
- 提案されたFUPMは相互作用データとレビュー文などから包括的プリファレンスを学習しプライバシーを強化
- 実験でFUPMが最先端手法より優れていることをアマゾンとDoubanデータセットで確認

新しいプライバシー保護の方法が提案されていて、実際のデータセットで効果が検証されているのが面白いよね。これからの推薦システムの進化が楽しみ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, **投稿日時:** 2024-08-26 23:29

- - -

### [ParTEETor: A System for Partial Deployments of TEEs within Tor](http://arxiv.org/abs/2408.14646)

**ParTEETor: Tor内での部分展開TEEシステム**

Rachel King, Quinn Burke, Yohan Beugin, Blaine Hoak, Kunyang Li, Eric Pauley, Ryan Sheatsley, Patrick McDaniel

- Torネットワークは匿名性を提供するが、特定の攻撃に弱い
- TEEをすべてのリレーに導入するのは非現実的である
- ParTEETorは部分的なTEE展開で既知の攻撃を防ぐシステム
- 小規模なTEE展開でも性能を維持しつつ、二つの攻撃に対する保護を保証

部分展開でこんなに効果が出るなんてびっくり！これ、今後もっと活用されそうだよね。興味深すぎる〜！



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-26 21:23

- - -

### [Securing Biometric Data: Fully Homomorphic Encryption in Multimodal Iris and Face Recognition](http://arxiv.org/abs/2408.14609)

**生体データの保護: マルチモーダル虹彩および顔認証における準同型暗号の活用**

Surendra Singh, Lambert Igene, Stephanie Schuckers

- 虹彩と顔の特徴ベクトルを融合し、データベースを保護する手法を探求
- 準同型暗号を使用して暗号化されたテンプレートでのマッチング操作を実施
- QFIRE-Iデータベースでの評価により、高精度とユーザープライバシーの両立を実証
- 理論と実験を通じて、96.41%の虹彩認識TAR、81.19%の顔認識TAR、100%の虹彩顔融合TARを達成

完全性を保ちながらユーザープライバシーを守る技術って凄いね！虹彩と顔の融合が全然漏れないって感動的だなぁ。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-26 20:05

- - -

### [Exploring the Potential of Synthetic Data to Replace Real Data](http://arxiv.org/abs/2408.14559)

**合成データによる実データ代替の可能性の探求**

Hyungtae Lee, Yan Zhang, Heesung Kwon, Shuvra S. Bhattacharrya

- 合成データがデータを多く必要とするAIにおいて重要である
- 合成データと少量の他のドメインの実画像を併用することで、トレーニング効果が増す
- 評価基準に新たな指標、train2test距離と$\text{AP}_\text{t2t}$を導入
- 合成データがトレーニング性能に与える影響を深く解析し、興味深いダイナミクスを発見

合成データがもっと広く使われるようになるといいなって思う！特に、トレーニング性能の向上が狙えるのがすごく魅力的だよね。

**Comment:** ICIP 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-08-26 18:20
