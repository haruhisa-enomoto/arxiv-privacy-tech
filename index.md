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

更新: 2024-12-19T04:24:47.642272

- - -

### [On the Robustness of Distributed Machine Learning against Transfer Attacks](http://arxiv.org/abs/2412.14080)

**分散型機械学習の転移攻撃に対する頑健性について**

Sébastien Andreina, Pascal Zimmer, Ghassan Karame

- 分散型機械学習は学習と推論の結合した頑健性をこれまで検証していなかった
- 初めて全てのモデルパラメータが異質な分散型MLモデルの頑健性を探求
- CIFAR10とFashionMNISTを用いた理論と実験で精度と頑健性の向上を示した
- Common Weakness攻撃に対し、頑健精度が40%向上し、クリーンタスク精度に最小限の影響

分散型機械学習の全体的な頑健性を強化する新しいアプローチなんだね！こういう研究って、未来の機械学習システムをさらに強力にしそうでワクワクするよね！

**Comment:** To appear in the Proceedings of the AAAI Conference on Artificial   Intelligence (AAAI) 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-12-18 17:27

- - -

### [Prompting Depth Anything for 4K Resolution Accurate Metric Depth Estimation](http://arxiv.org/abs/2412.14015)

**4K解像度で正確なメトリック深度推定を可能にする「深度すべてプロンプト」の導入**

Haotong Lin, Sida Peng, Jingxiao Chen, Songyou Peng, Jiaming Sun, Minghuan Liu, Hujun Bao, Jiashi Feng, Xiaowei Zhou, Bingyi Kang

- 言語とビジョンモデルにプロンプトを導入し、深度推定にも適用
- 低コストのLiDARをプロンプトとして使用し、4K解像度の精密深度を実現
- 合成データや擬似GT深度生成を含むスケーラブルなデータパイプラインを提案
- ARKitScenesやScanNet++で新しい成果を上げ、応用領域にも有益

これ、プロンプトが深度の世界でも活躍しちゃうんだね！めっちゃ高解像度で、しかもLiDARを使ってるなんて、最先端な感じがワクワクするね！

**Comment:** Project page: https://PromptDA.github.io/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-18 16:32

- - -

### [T-Edge: Trusted Heterogeneous Edge Computing](http://arxiv.org/abs/2412.13905)

**T-Edge: 信頼された異種エッジコンピューティング**

Jiamin Shen, Yao Chen, Weng-Fai Wong, Ee-Chien Chang

- 異種コンピューティングは効率を向上させるが、セキュリティとプライバシーへの懸念が増加
- CPUベースの信頼実行環境は成功しているが、異種コンピューティングシステムへの拡張は困難
- ARM/FPGAプラットフォーム向けの実用的な信頼実行環境を提案し、TrustZoneを利用
- セキュリティを確保するためにProVerifを使用し、Xilinx MPSoCでプロトタイプを実装

異種コンピューティングのセキュリティ、なんか課題が多そうだけどすごく重要よね！しかもTrustZoneとか、ワクワクする新技術ばかりで未来が楽しみ～！

**Comment:** 13 pages, 6 figures

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-18 14:45

- - -

### [Towards an identity management solution on Arweave](http://arxiv.org/abs/2412.13865)

**Arweave上でのアイデンティティ管理ソリューションに向けて**

Andreea Elena Dragnoiu, Ruxandra F. Olimid

- 従来の集中型アイデンティティ管理はプライバシーやデータセキュリティで問題を抱えている
- Arweaveネットワークを活用した永久保存を利用し、ユーザーに自己主権型アイデンティティを提供
- 分散型識別子と検証可能な資格証明を用いてユーザーがデジタルIDを作成・管理する
- ゼロ知識証明やBBS(+)署名スキームでプライバシー強化し、GDPRなどの法規制への準拠を支援

Arweaveを使ってアイデンティティ管理をもっと安全にできるのってすごく親切だよね。プライバシーの強化と法規制への準拠を両立させながら、デジタルIDを自分で管理できるのは未来っぽい！

**Comment:** 37 pages

**トピック:** [SSI/DID/VC](ssi), [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, cs.ET, **投稿日時:** 2024-12-18 14:01

- - -

### [Domain-adaptative Continual Learning for Low-resource Tasks: Evaluation on Nepali](http://arxiv.org/abs/2412.13860)

**低リソースタスクにおけるドメイン適応継続学習: ネパール語での評価**

Sharad Duwal, Suraj Prasai, Suresh Manandhar

- 継続学習は、新しいデータが得られた際に巨大な言語モデルを再訓練することが困難なため、注目される研究分野である
- ドメイン適応事前学習（DAPT）では、もともと訓練されていなかった領域に適応させるために、事前学習済みの言語モデルの継続的な学習を行う
- 合成データを使ってLLama 3 8Bを4ビットQLoRA設定でネパール語に適応し、忘却や知識獲得などを性能評価した
- 驚いたことに、評価中のショット数を増やすと、基礎モデルと比べて大きな性能向上（最大19.29%）が見られ、潜在的な保持があると示唆される

継続学習って面白いよね、新しいデータを手に入れるたびに再訓練しなくていいなんて。大規模モデルの適応ができたら低リソースの言語ももっとサポートできそうでワクワクする！

**Comment:** 10 pages, 2 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-12-18 13:53

- - -

### [Fed-AugMix: Balancing Privacy and Utility via Data Augmentation](http://arxiv.org/abs/2412.13818)

**Fed-AugMix: データ拡張によるプライバシーと有用性のバランス調整**

Haoyang Li, Wei Chen, Xiaojin Zhang

- 連合学習のプライバシーが勾配漏洩攻撃により脅かされている
- 歪みベースの保護は効果的だが、モデル性能は低下する
- クライアントレベルのAugMixアルゴリズムでプライバシーと性能向上を両立
- JSダイバージェンスで、プライバシーを守りつつモデルの一貫性を促進

この研究、データの守り方と性能の両立を目指してる感じでおもしろそう！ちゃんと効果あるって実験結果も出てるから、これからの連合学習での応用が楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-18 13:05

- - -

### [Differentially Private Substring and Document Counting](http://arxiv.org/abs/2412.13813)

**差分プライバシーを用いた部分文字列と文書のカウント**

Giulia Bernardini, Philip Bille, Inge Li Gørtz, Teresa Anna Steiner

- 差分プライバシーを活用した部分文字列カウントと文書カウントを理論的に研究
- 全パターンに対して最適な誤差で問題解決可能なデータ構造を提案
- ドキュメントカウントは誤差をさらに改善し、データ構造は効率的
- 提案手法で頻出部分文字列やq-グラムのプライベートマイニングのアルゴリズムを改善

理論的でちょっと難しそうだけど、部分文字列をプライバシー守りながら数えるってすごいね！q-グラムの効率化も興味深くて、いろんな応用が浮かぶ！

**Comment:** 33 pages

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, **投稿日時:** 2024-12-18 13:00

- - -

### [Rehearsal-Free Continual Federated Learning with Synergistic Regularization](http://arxiv.org/abs/2412.13779)

**リハーサルなし協調正則化による継続的連合学習**

Yichen Li, Yuying Wang, Tianzhe Xiao, Haozhao Wang, Yining Qi, Ruixuan Li

- 継続的連合学習は、以前のタスクを忘れずに絶えず変化するデータから新たな概念を学ぶ技術である
- 既存の継続的連合学習はリハーサルによる記憶コストやプライバシー侵害の懸念がある
- 課題解決のために、サンプルキャッシュが不要な正則化技術を連合学習に適用する
- FedSSIはデータの異質性を考慮し、計算負担を軽減しつつも高性能を実現する

この論文面白そう！特にリハーサルを省略しつつ、異質なデータに対応できる新技術って画期的だよね。これが成功すれば、もっと効率的な分散学習が実現しそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-12-18 12:16

- - -

### [Federated Source-free Domain Adaptation for Classification: Weighted Cluster Aggregation for Unlabeled Data](http://arxiv.org/abs/2412.13757)

**連合ソースフリードメイン適応による分類：ラベルなしデータのための重み付きクラスター集約**

Junki Mori, Kosuke Kihara, Taiki Miyagawa, Akinori F. Ebihara, Isamu Teranishi, Hisashi Kashima

- 連合学習ではラベル付きデータが前提であるが、実際にはコストとプライバシーの問題がある
- ソースデータなしでのドメイン適応で、予め訓練されたモデルを用いる手法を提案
- FedWCAは重み付きクラスター集約でドメインシフトとプライバシー問題を解決
- 実験結果よりFFREEDAで既存手法を上回る効果を示し、その実効性を証明

連合学習の新しいアプローチだね！ラベルなしデータだけでドメイン適応をするなんて、すごく面白そう。これが実用化されたら、もっと安心してデータを共有できるかもしれないよね。

**Comment:** Accepted by WACV 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-18 11:47

- - -

### [Text2Relight: Creative Portrait Relighting with Text Guidance](http://arxiv.org/abs/2412.13734)

**Text2Relight: テキストガイドによる創造的なポートレート再照明**

Junuk Cha, Mengwei Ren, Krishna Kumar Singh, He Zhang, Yannick Hold-Geoffroy, Seunghyun Yoon, HyunJoon Jung, Jae Shin Yoon, Seungryul Baek

- ポートレート画像とテキストを使用して1枚の画像を再照明する技術を提案
- テキストの創造性を利用し、光源を温度、感情、匂い、時間によって表現可能
- 大規模なテキストと再照明のデータがないため、そのようなマッピングのモデル化が難しい
- 生成モデルを用いて、テキストに基づく多様で創造的な照明画像を自動生成し学習

この研究、テキストから感覚的なことまで表現できるなんて面白そう！AIがどんな情景を再現するのか想像が膨らむね。また、景色だけじゃなくて感情まで表現に組み込めるなんて、本当に未来的な技術だと思うな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-18 11:12

- - -

### [Federated Learning and RAG Integration: A Scalable Approach for Medical Large Language Models](http://arxiv.org/abs/2412.13720)

**連合学習とRAG統合: 医療向け大規模言語モデルの拡張可能なアプローチ**

Jincheol Jung, Hongju Jeong, Eui-Nam Huh

- 医療分野のLLM性能を向上のためにRAGを連合学習へ統合
- 連合学習によりデータプライバシーと分散コンピュテーションの利点を活用
- RAG統合で、さまざまなクライアント構成下のモデル性能が向上
- 結果は非統合モデルよりも一貫して優れた評価指標を示す

連合学習とRAGを組み合わせることで、医療分野の大規模言語モデルがどこまで進化するのかワクワクする！プライバシーを守りつつ、性能向上できるのはまさに未来の技術だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-12-18 11:00

- - -

### [NPC: Neural Predictive Control for Fuel-Efficient Autonomous Trucks](http://arxiv.org/abs/2412.13618)

**NPC: 燃料効率の良い自動運転トラックのためのニューラル予測制御**

Jiaping Ren, Jiahao Xiang, Hongfei Gao, Jinchuan Zhang, Yiming Ren, Yuexin Ma, Yi Wu, Ruigang Yang, Wei Li

- 燃料効率はコスト削減と炭素排出削減に重要である
- NPCは物理モデルを使わない純粋なデータ駆動型手法である
- NVFormerは注意メカニズムを用いて関係性をモデル化する
- NPCは従来手法を上回り、シミュレーションと実地試験で燃料節約を実現

自動運転トラックの燃料効率すごく上がりそう！これで環境にも優しいトラックの未来が期待できるね。実際の道路でのテスト結果が良好ってところもポイント高い！

**Comment:** 7 pages, 6 figures, for associated mpeg file, see   https://www.youtube.com/watch?v=hqgpj7LhiL4

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.AI, **投稿日時:** 2024-12-18 08:57

- - -

### [SemiDFL: A Semi-Supervised Paradigm for Decentralized Federated Learning](http://arxiv.org/abs/2412.13589)

**SemiDFL: 分散型連合学習のための半教師ありパラダイム**

Xinyang Liu, Pengchao Han, Xuan Li, Bo Liu

- 分散型連合学習(DFL)は、中央サーバーに依存せず、通信のボトルネックと単一障害点を解消する
- 現実世界の多くのデータがラベルなしであるため、半教師あり学習(SSL)シナリオを考慮
- SemiDFLは、データとモデル空間でのコンセンサスを確立し、性能を向上させる初の半教師ありDFL方法
- 提案手法は、擬似ラベル付けと合成データ生成を活用し、適応的な集約により精度を向上

このアプローチってすごく実用的かも！ラベルなしデータが多い現実のシナリオで重要な役割を果たしそう。未来のAIシステムがもっと賢くなれそうだね！

**Comment:** Accepted by AAAI 2025

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-12-18 08:12

- - -

### [Large Language Model Federated Learning with Blockchain and Unlearning for Cross-Organizational Collaboration](http://arxiv.org/abs/2412.13551)

**ブロックチェーンと学習解除を用いたクロスオーガニゼーション協力における大規模言語モデル連合学習**

Xuhan Zuo, Minghao Wang, Tianqing Zhu, Shui Yu, Wanlei Zhou

- 異なる組織間での大規模言語モデルの利用が難しく、データ共有にためらいがある
- 組織間競争が信頼問題を生み、新しいプライバシー法がデータ削除を要求
- 既存の連合学習は信頼とデータ削除問題に対応しておらず限界がある
- 公開・個人チェーンを用いたハイブリッド学習で信頼とプライバシーを両立

これってすごいよね！異なる企業が協力して技術を磨くために、安全にデータを扱えるなんて未来感満載。組織が共有しつつ守られる方法、もっと探ってみたいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-18 06:56

- - -

### [Hybrid Data-Free Knowledge Distillation](http://arxiv.org/abs/2412.13525)

**ハイブリッドデータフリー知識蒸留**

Jialiang Tang, Shuo Chen, Chen Gong

- データフリー知識蒸留は、元の教師ネットワークのトレーニングデータを使わずに小型の生徒ネットワークを学習する方法である
- 既存の方法は実際の例を集めるか合成例を生成するが、現実的にはデータ収集やエミュレーションに困難がある
- HiDFDは少量の収集データと十分な合成データを組み合わせて生徒ネットワークを訓練する
- HiDFDは教師ガイド生成と生徒蒸留の2つのモジュールで構成され、従来の方法より120倍少ないデータでの性能を実証した

これって、省エネで効率的なAI教育を目指すストーリーみたいでワクワクするよね！少ないデータで優秀なAIを作るって、ますます未来の技術が身近になりそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-12-18 05:52

- - -

### [Privacy-Preserving Cyberattack Detection in Blockchain-Based IoT Systems Using AI and Homomorphic Encryption](http://arxiv.org/abs/2412.13522)

**AIと準同型暗号を用いたブロックチェーンIoTシステムにおけるプライバシー保護サイバー攻撃検出**

Bui Duc Manh, Chi-Hieu Nguyen, Dinh Thai Hoang, Diep N. Nguyen, Ming Zeng, Quoc-Viet Pham

- ブロックチェーンノードにAIを用いた検出モジュールを配置し、リアルタイムでの攻撃検出を実現
- プライバシー保護のため、準同型暗号を利用してクラウドサービスプロバイダで学習を行う
- SIMD形式のパッキングアルゴリズムを導入し、効率的に暗号化データでのモデル学習を可能に
- FedAvgアルゴリズムに基づく分散学習手法を提案し、計算時間を短縮しつつ高精度を維持

この研究はブロックチェーンとAIの素敵な融合が見どころかも！プライバシーを守りつつ、サイバー攻撃を素早く検出する未来のIoTシステムに大きく貢献しそう！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-18 05:46

- - -

### [Federated t-SNE and UMAP for Distributed Data Visualization](http://arxiv.org/abs/2412.13495)

**連合学習を用いた分散データ可視化のためのt-SNEとUMAP**

Dong Qiao, Xinxian Ma, Jicong Fan

- 高次元データの可視化はビッグデータ時代において重要だが、データが複数のセンターに分散されていることによるセキュリティとプライバシーの懸念がある
- 標準的なt-SNEとUMAPを改善するため、連合学習を使ったFed-tSNEとFed-UMAPを提案し、データを交換せずに可視化を実現
- 更なるプライバシー保護のためにFed-tSNE+とFed-UMAP+を提案し、分散クラスタリングのアルゴリズムも開発
- 提案手法は最適化の収束や距離・類似度推定、差分プライバシーに関する理論的保証を提供し、実験で精度の低下が少ないことを確認

連合学習とデータ可視化が合わさるなんて、新しいね！プライバシーも守りながら高次元データを可視化できるのは素晴らしい進化だと思うな。

**Comment:** The paper was accepted by AAAI 2025

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-12-18 04:33

- - -

### [Federated Unlearning Model Recovery in Data with Skewed Label Distributions](http://arxiv.org/abs/2412.13466)

**データの偏ったラベル分布における連合学習のモデル復元**

Xinrui Yu, Wenbin Pei, Bing Xue, Qiang Zhang

- 連合学習において、データ提供を撤回する連合アンラーニングは重要
- ラベルが偏ったデータでのアンラーニングは、バイアスがかかりやすくサービスの質を下げる
- 提案手法は深層学習を用いたオーバーサンプリングでデータセットを補完し、回復を支援
- ノイズを取り除く密度ベースの手法でデータ品質を向上し、モデル性能回復を実現

この手法、データの偏りをうまく補正してモデルをちゃんと回復できるとかすごいよね！連合学習の新しい可能性が広がりそうで、いろんな分野で役立ちそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-12-18 03:25

- - -

### [TETRIS: Composing FHE Techniques for Private Functional Exploration Over Large Datasets](http://arxiv.org/abs/2412.13269)

**TETRIS: 大規模データセットでのプライベート機能探索のためのFHE技術の組み合わせ**

Malika Izabachène, Jean-Philippe Bossuat

- 大規模なデータセットを対象に効率的なプライベート解析手法を設計する問題に取り組む。
- 準同型暗号の技術を組み合わせることで、プライベートな機能評価としきい値処理を実現。
- 患者記録を保持するサーバーに対し、統計基準を非公開にしたまま探索できるシステムTETRISを設計。
- 1スレッドで数十万のデータを数分で解析し、1データあたりの所要時間は2ms未満を実現。

TETRISってシステム名がゲームみたいでおしゃれ！秘密を守りながらデータを分析するなんて、すごく未来的だね。これからの医療研究に役立ちそうで楽しみ！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-12-17 19:04
