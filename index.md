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

更新: 2024-07-18T04:20:46.953493

- - -

### [Jigsaw Game: Federated Clustering](http://arxiv.org/abs/2407.12764)

**ジグソーゲーム：連合クラスタリング**

Jinxuan Xu, Hong-You Chen, Wei-Lun Chao, Yuqian Zhang

- 連合学習は教師あり学習で注目されているが、教師なし学習問題（特にクラスタリング）は十分に探究されていない
- 連合k-meansの非凸目的関数とデータの異質性が連合フレームワークにおける課題である
- FeCA（一度きりのアルゴリズム）を提案し、クライアント上での局所解を適応的に洗練し、それらを集約することで一回でグローバル解を回収する
- FeCAのロバスト性を実証し、DeepFeCAを提案、これにより連合設定での教師なし特徴学習が可能

連合学習の世界がどんどん広がりそうでワクワクしちゃうね！新しいアルゴリズムで更なる発展が期待できるのはめっちゃ楽しみ～。

**Comment:** Accepted to TMLR

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-17 17:42

- - -

### [Comparing Federated Stochastic Gradient Descent and Federated Averaging for Predicting Hospital Length of Stay](http://arxiv.org/abs/2407.12741)

**連合確率的勾配降下法と連合平均法を用いた病院滞在期間予測の比較**

Mehmet Yigit Balik

- 病院滞在期間の予測は、病院の資源配分において重要である
- 医療機関はプライバシー規則があるため、十分で多様なデータの取得が困難である
- 連合学習を使い、データを外に出さずに複数の病院で共同モデルをトレーニングする手法を検討
- 連合確率的勾配降下法（FedSGD）と連合平均法（FedAVG）を比較し、プライバシーを守りながら正確な滞在期間予測が可能であると示した

こんな感じの研究、私たちの未来の医療にめっちゃ役立ちそうじゃない？連合学習でデータが守られてるのも安心できるよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-17 17:00

- - -

### [FlexFL: Heterogeneous Federated Learning via APoZ-Guided Flexible Pruning in Uncertain Scenarios](http://arxiv.org/abs/2407.12729)

**FlexFL：不確実なシナリオにおけるAPoZガイド柔軟剪定による異種連合学習**

Zekai Chen, Chentao Jia, Ming Hu, Xiaofei Xie, Anran Li, Mingsong Chen

- ディープラーニング技術の普及に伴い、AIoTシステムは連合学習を採用
- 既存の連合学習システムはモデル選択の問題を抱えている
- FlexFLはAPoZガイドの柔軟な剪定戦略を採用し、異種デバイスに最適なモデルを提供
- 実験結果により、FlexFLは最先端の異種連合学習方法と比較して推論精度を最大14.24%改善

FlexFLって、異なるデバイスで最適なモデルを見つけるんだって！性能が大幅アップするなんて、すごくおもしろそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-17 16:48

- - -

### [Enhancing the Utility of Privacy-Preserving Cancer Classification using Synthetic Data](http://arxiv.org/abs/2407.12669)

**合成データを用いたプライバシー保護型癌分類の有用性向上**

Richard Osuala, Daniel M. Lang, Anneliese Riess, Georgios Kaissis, Zuzanna Szafranowska, Grzegorz Skorupko, Oliver Diaz, Julia A. Schnabel, Karim Lekadir

- 深層学習は乳癌検出に有望だが、データ共有の制約がある
- 差分プライバシーSGDと合成データを生成するGANを使用
- 合成データ増強がプライバシーと有用性の両立を向上させる
- データ前処理とDP-SGD微調整で性能がさらに向上する

プライバシーを保ちつつ、乳癌検出モデルの性能を上げる新しい方法だね！これ、臨床現場にもすぐ役立ちそうでワクワクする！

**Comment:** Early Accept at MICCAI 2024 Deep-Breath Workshop

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-07-17 15:52

- - -

### [LSKV: A Confidential Distributed Datastore to Protect Critical Data in the Cloud](http://arxiv.org/abs/2407.12623)

**LSKV: クラウドで重要なデータを保護するための機密分散データストア**

Andrew Jeffery, Julien Maffre, Heidi Howard, Richard Mortier

- クラウドへのサービス移行は、ハードウェアやソフトウェア、データアクセスにおける信頼が必要
- Kubernetesのetcdのような分散データストアが多くのサービスで重要な役割を果たしている
- LSKVは、信頼できる実行環境によりクラウドプロバイダからデータを保護しつつ、etcdに似たAPIを提供
- LSKVは、従来システムを機密実行へ移行させ、etcdと競合する性能で信頼性向上に寄与

分散データストアがクラウドの信頼性をどう変えるか楽しみだね。これが普及したら安全性も一層高まるかも！



**トピック:** [TEE](tee), **カテゴリ:** cs.DC, **投稿日時:** 2024-07-17 14:50

- - -

### [An Efficient TLS 1.3 Handshake Protocol with VC Certificate Type](http://arxiv.org/abs/2407.12536)

**効率的なTLS 1.3ハンドシェイクプロトコルとVC証明書タイプ**

Leonardo Perugini, Andrea Vesco

- トランスポートレイヤーセキュリティ(TLS)ハンドシェイクプロトコルにVerifiable Credential(VC)を導入
- TLS 1.3のセキュリティ機能を保持しつつ、RFC-8446に完全準拠した設計
- OpenSSLライブラリに最小限の変更、新たな外部プロバイダーでVCとDID関連操作を処理
- 実験結果でPKIとX.509証明書ベースのソリューションと同等のパフォーマンスを証明

すごく未来的でイノベーティブな感じ！IoTシステムでの自己主権型アイデンティティ、大規模でもコストダウン期待できそうでワクワクするね。

**Comment:** arXiv admin note: text overlap with arXiv:2311.00386

**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-17 13:18

- - -

### [Case2Code: Learning Inductive Reasoning with Synthetic Data](http://arxiv.org/abs/2407.12504)

**Case2Code: 合成データを用いた帰納的推論の学習**

Yunfan Shao, Linyang Li, Yichuan Ma, Peiji Li, Demin Song, Qinyuan Cheng, Shimin Li, Xiaonan Li, Pengyu Wang, Qipeng Guo, Hang Yan, Xipeng Qiu, Xuanjing Huang, Dahua Lin

- LLMは主に演繹的推論に優れているが、帰納的推論は難しい
- 人間が生成する帰納的データを大規模かつ多様に集めるのは困難
- コード領域でデータ合成を行い、合成された入出力変換を元にLLMがコードの実装を推論
- 実験結果から、合成データによる帰納的推論訓練がLLMの様々なコーディング能力の向上に寄与することが示された

合成データを使ってLLMがどんどん賢くなるなんてすごいね！未来のAIがもっともっといろんなことをできるようになるのが楽しみだなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-07-17 11:35

- - -

### [Non-parametric regularization for class imbalance federated medical image classification](http://arxiv.org/abs/2407.12446)

**非パラメトリック正則化によるクラス不均衡な連合学習の医療画像分類**

Jeffry Wicaksana, Zengqiang Yan, Kwang-Ting Cheng

- 限られた訓練データとクラス不均衡は、臨床的に頑健な深層学習モデルの開発に重大な課題を生じる
- 連合学習はユーザーがプライバシーセンシティブなデータを共有せずに協力して深層モデルを訓練できる
- クライアント間でクラス分布のばらつきがあるため、クラス不均衡が悪化する
- 提案するFedNPRとFedNPR-Perが特徴抽出器を正則化し、信号を向上させることで既存の手法を超える

クラス不均衡の問題を連合学習で改善するなんて、めちゃくちゃ未来的だね！医療分野への応用が増えたらもっと進歩しそう。

**Comment:** arXiv admin note: text overlap with arXiv:2305.00738

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-17 09:54

- - -

### [Proximity-based Self-Federated Learning](http://arxiv.org/abs/2407.12410)

**近接性に基づく自己連合学習**

Davide Domini, Gianluca Aguzzi, Nicolas Farabegoli, Mirko Viroli, Lukas Esterle

- 連合学習は分散クライアントネットワークでグローバルモデルを共同開発、ローカルデータの共有を不要とする
- 従来の連合学習は中央サーバーによる調整が必要、地理的・ローカルデータの差異を無視しがち
- 近接性ベースの自己連合学習は、地理的近接性とデータ分布に基づくクライアントの自律連携を可能に
- シミュレーションで従来の中央集権型連合学習と比較し、モデルの適応性と効果を実証

この論文、自己連合学習のアイデアがすごく新しいと思わない？ローカルデータの違いもちゃんと考慮されてて、未来のスマートネットワークにすごく役立ちそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-17 08:44

- - -

### [Private and Federated Stochastic Convex Optimization: Efficient Strategies for Centralized Systems](http://arxiv.org/abs/2407.12396)

**プライベートかつ連合的確率的凸最適化：集中型システムの効率的な戦略**

Roie Reshef, Kfir Y. Levy

- プライバシーを維持しながら連合学習（FL）に取り組む課題について検討
- 確率的凸最適化（SCO）フレームワーク内で差分プライバシー（DP）を保証する方法を考案
- ホモジニアスおよびヘテロジニアスなデータ分布に対して最適な収束率を維持する手法を提供
- 近年の確率的最適化技術を基にしたアプローチにより、計算の線形複雑性と勾配の曖昧化が低減

これはすごく面白そうだね！差分プライバシーを維持しつつ効率も高いなんて、未来の連合学習が楽しみだな～。

**Comment:** To be published in ICML 2024

**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-17 08:19

- - -

### [Cabin: Confining Untrusted Programs within Confidential VMs](http://arxiv.org/abs/2407.12334)

**Cabin: 信頼できないプログラムを機密VM内に隔離する方法**

Benshan Me, Saisai Xia, Wenhao Wang, Dongdai Lin

- 機密コンピューティングは、信頼できないクラウドから機密計算を保護するが、CVMは大規模で脆弱なOSカーネルを含むため攻撃の対象になりやすい
- ページテーブルの読書アクセスの不正確な制御により、攻撃者が脆弱性を悪用しやすくなっている
- CabinはAMD SEV-SNP技術を用いて、信頼できないプロセスをより低いVMPLのユーザースペースに隔離し、プロキシカーネルを導入して攻撃面を最小化
- 非同期転送機構と匿名メモリ管理を導入し、性能への影響を最小限に抑えつつ、NbenchとWolfSSLベンチマークで5%のオーバーヘッド 

技術的にめっちゃ新しいアイデアだね！セキュリティとパフォーマンスのバランスを取るのって本当に難しいけど、そこが面白いところかも。

**Comment:** ICICS 2024

**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-17 06:23

- - -

### [CDFL: Efficient Federated Human Activity Recognition using Contrastive Learning and Deep Clustering](http://arxiv.org/abs/2407.12287)

**CDFL: 対照学習とディープクラスタリングを用いた効率的な連合的なヒューマンアクティビティ認識**

Ensieh Khazaei, Alireza Esmaeilzehi, Bilal Taha, Dimitrios Hatzinakos

- ヒューマンアクティビティ認識(HAR)は、多様なセンサーからのデータで自動化と知能的識別が必要だが、従来の方法はメモリ集約的でプライバシー懸念がある。
- 連合学習(FL)は、データの交換ではなく、ローカルモデルパラメータを交換することでグローバルモデルを訓練する。
- 実際の環境では、センサーデータは非独立同分布(Non-IID)であり、典型的なFLフレームワークは非均質な環境では遅い収束と低パフォーマンスに苦しむ。
- CDFLは、プライバシー保護されたデータで効率的にグローバルモデルを更新し、性能、収束速度、帯域幅使用量で他の最新手法より優れていることを実証した。

連合学習の実際の課題に対処したこの研究は、未来のプライバシー技術に大きく貢献しそうで楽しみだね。ちょっと難しそうだけど、この新しいアプローチが世の中にどんな良い影響を与えるのかワクワクするよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-07-17 03:17

- - -

### [Individualized Federated Learning for Traffic Prediction with Error Driven Aggregation](http://arxiv.org/abs/2407.12226)

**交通予測のための誤差駆動型集約を用いた個別化連合学習**

Hang Chen, Collin Meese, Mark Nejad, Chien-Chung Shen

- スマートシティの交通管理において、低レイテンシの交通予測が重要
- 現在の連合学習フレームワークはリアルタイムのモデル更新が不足している
- NeighborFLという個別化されたリアルタイム連合学習手法を提案
- シミュレーションでは、他の三つのベースラインモデルよりもリアルタイム予測精度が向上

NeighborFLの提案、すごく面白そう！リアルタイム更新と個別化で、もっと賢い交通システムが実現できるかも。これが実用化されたら、私たちの生活も便利になるね！

**Comment:** 16 pages, 4 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-17 00:42

- - -

### [Monocular pose estimation of articulated surgical instruments in open surgery](http://arxiv.org/abs/2407.12138)

**開腹手術における細長い外科器具のモノキュラ姿勢推定**

Robert Spektor, Tom Friedman, Itay Or, Gil Bolotin, Shlomi Laufer

- 細長い外科器具のモノキュラ 6D 姿勢推定の新規手法を提案
- 3Dモデリングと物理ベースのレンダリングを用いた合成データ生成
- オブジェクト検出とポーズ推定を組み合わせたハイブリッドジオメトリ融合戦略
- 合成データと実世界の未注釈データを利用し、ドメイン適応による擬似ラベル生成

外科手術の未来が見えるかもね！広がる医療の可能性って感じでワクワクするよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, cs.RO, **投稿日時:** 2024-07-16 19:47

- - -

### [LLMs-in-the-loop Part-1: Expert Small AI Models for Bio-Medical Text Translation](http://arxiv.org/abs/2407.12126)

**LLMsインザループ・パート1：バイオメディカルテキスト翻訳のための専門小型AIモデル**

Bunyamin Keles, Murat Gunay, Serdar I. Caglar

- 医療翻訳における難解な医学用語の翻訳品質向上のため、「LLMs-in-the-loop」アプローチを提案
- 高品質な合成データを用いて訓練された小型モデルが大規模なLLMを凌駕する結果を示す
- 六つの言語で専門的な並列コーパスを作成し、新しい医療翻訳テストデータセットを導入
- BLEUやBERTスコアにより、Google翻訳やDeepL、GPT-4-Turboより高評価を獲得

しっかりした医療データに特化したことで、小型モデルがめっちゃ強いの驚きだよね！次のパートも楽しみだし、医療AIがもっと進化しそうでワクワクしちゃう。

**Comment:** 14 pages, 2 figures, 9 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, 68T35, **投稿日時:** 2024-07-16 19:32

- - -

### [Private prediction for large-scale synthetic text generation](http://arxiv.org/abs/2407.12108)

**大規模合成テキスト生成のためのプライベート予測**

Kareem Amin, Alex Bie, Weiwei Kong, Alexey Kurakin, Natalia Ponomareva, Umar Syed, Andreas Terzis, Sergei Vassilvitskii

- LLMを使用して差分プライバシーを保証する合成テキストを生成する手法を提案
- 提案手法はトレーニングしないが、ソースデータを用いて次のトークン予測を行う
- 既存研究では10以下の例しか生成できなかったが、提案手法は数千のデータ生成が可能
- プライバシー解析とプライベート選択メカニズムを改善し、柔軟なデータ予測を実現

これって、差分プライバシーを活かしてもっとたくさんのデータを作れる方法だね！大規模データでも安全に活用できるようになるのが楽しみ😆

**Comment:** 12 pages main text + 15 pages appendix

**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CL, cs.CR, **投稿日時:** 2024-07-16 18:28
