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

更新: 2024-08-01T04:20:01.578069

- - -

### [ShieldGemma: Generative AI Content Moderation Based on Gemma](http://arxiv.org/abs/2407.21772)

**ShieldGemma: Generative AIによるGemmaベースのコンテンツモデレーション**

Wenjun Zeng, Yuchi Liu, Ryan Mullins, Ludovic Peran, Joe Fernandez, Hamza Harkous, Karthik Narasimhan, Drew Proud, Piyush Kumar, Bhaktipriya Radharapu, Olivia Sturman, Oscar Wahltinez

- Gemma2を利用したLLMベースの安全コンテンツモデレーションモデルを紹介
- 性的、危険な内容、嫌がらせ、ヘイトスピーチなどの主要な危険タイプに対応
- 公共および内部ベンチマークで既存モデルより優れた性能を発揮（+10.8% AU-PRC）
- 合成データを用いたモデルで高い汎化性能を実証

新しい技術で、コンテンツモデレーションがより正確になりそう！安全なオンライン空間が増えるといいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, **投稿日時:** 2024-07-31 17:48

- - -

### [A Federated Learning-Friendly Approach for Parameter-Efficient Fine-Tuning of SAM in 3D Segmentation](http://arxiv.org/abs/2407.21739)

**パラメータ効率的なSAMの3Dセグメンテーション向け連合学習フレンドリーアプローチ**

Mothilal Asokan, Joseph Geo Benjamin, Mohammad Yaqub, Karthik Nandakumar

- 自然データと医療データ間の分布シフトのため、基礎モデルのファインチューニングに多量の医療データが必要
- プライバシーの懸念があるため、特定タスク用の医療データを集中収集することが難しい
- 連合学習(FL)とパラメータ効率的なファインチューニング(PEFT)を組み合わせ、通信コストを削減しながら効果的な学習を実現
- Fed-KiTSデータセットで通信コスト約48倍削減、性能も約6%向上し、Fed-IXIおよびProstate MRIデータセットでも有効性を確認

これさ、医療データのプライバシー問題解決しつつ効率的に学習できるってめっちゃ良いね！連合学習の可能性が広がるし、3Dセグメンテーションの精度アップも期待できそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, eess.IV, **投稿日時:** 2024-07-31 16:48

- - -

### [Synthetic Simplicity: Unveiling Bias in Medical Data Augmentation](http://arxiv.org/abs/2407.21674)

**合成の簡潔性：医療データ補完におけるバイアスの解明**

Krishan Agyakari Raja Babu, Rachana Sathish, Mrunal Pattanaik, Rahul Venkataramani

- 合成データが医療画像などのデータ不足分野で用いられるが、その統計的特性が下流タスクに影響
- 実データと合成データの間の偽の相違を利用する「簡単さバイアス」が発生
- 原因として、データソース（実データvs合成データ）に依存し、表面的な特徴に過度に依存する
- デジタル分類と心臓エコー画像での数室ビュー分類の実験で、この脆弱性を実証

合成データが医療分野で増えてるけど、表面的な違いに引っかかるのは困るね。この論文はその点を具体的に実証してて、実践的なガイドラインにもなるから注目だよ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-07-31 15:14

- - -

### [Grid-Based Decompositions for Spatial Data under Local Differential Privacy](http://arxiv.org/abs/2407.21624)

**ローカル差分プライバシーにおける空間データのグリッド分解**

Berkay Kemal Balioglu, Alireza Khodaie, Ameer Taweel, Mehmet Emre Gursoy

- LDPは人気の高いプライバシー基準であり、空間データにも適用されている
- 本研究ではUG（均一グリッド）、PrivAG（適応グリッド）、AAG（高度適応グリッド）の3つのグリッド分解法を検討
- AAGは隣接セルの密度に基づき不均一なセル分割を行い、より高い効用を提供
- 実験結果では、AAGは小さなクエリにおいてUGとPrivAGを上回る

AAGという新しいアプローチがFBやインスタのデータ解析でどれだけ役立つか気になる！でも大規模なクエリはUGの方がいいってこともあるんだね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-31 14:17

- - -

### [EZSR: Event-based Zero-Shot Recognition](http://arxiv.org/abs/2407.21616)

**EZSR: イベントベースのゼロショット認識**

Yan Yang, Liyuan Pan, Dongxu Li, Liu Liu

- 既存のアプローチは、イベントデータとRGB画像の埋め込み類似性を最大化してゼロショット認識を達成
- グローバルな類似性最大化が、学習されたイベント埋め込み空間とCLIPテキスト埋め込み空間の語義の不一致を引き起こす
- セマンティックの不一致を軽減するためにスカラー正則化戦略を採用
- 静止RGB画像からイベントデータを合成するパイプラインを提案し、優れたゼロショット性能を達成

イベントベースでゼロショット認識なんて面白すぎる！実際の実装でどれだけ使えるか試してみたいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-31 14:06

- - -

### [Tabular Data Augmentation for Machine Learning: Progress and Prospects of Embracing Generative AI](http://arxiv.org/abs/2407.21523)

**機械学習のための表形式データ拡張: 生成AIの進展と展望**

Lingxi Cui, Huan Li, Ke Chen, Lidan Shou, Gang Chen

- 機械学習における高品質な表形式データの取得は大きな障害。
- 表形式データ拡張のパイプラインを3つの手順（前処理、拡張、後処理）に分類。
- 拡張方法を外部データ取得ベースと合成データ生成ベースに分け、細分化。
- 生成AIを活用した最新の表形式データ拡張の動向と未来の方向性を強調。

生成AIがこれからどう表形式データを変えていくのか、すっごく気になる！GitHubもチェックしてみたいな。

**Comment:** repository maintained at   https://github.com/SuDIS-ZJU/awesome-tabular-data-augmentation

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.DB, **投稿日時:** 2024-07-31 10:56

- - -

### [FSSC: Federated Learning of Transformer Neural Networks for Semantic Image Communication](http://arxiv.org/abs/2407.21507)

**FSSC: セマンティックイメージコミュニケーションのためのトランスフォーマーニューラルネットワークの連合学習**

Yuna Yan, Xin Zhang, Lixin Li, Wensheng Lin, Rui Li, Wenchi Cheng, Zhu Han

- Swin Transformerを用いたジョイントソースチャネルコーディング（JSCC）がセマンティック情報を効果的に抽出
- 連合学習（FL）フレームワークでローカルモデルパラメータを集約し、データの直接共有なしにグローバルモデルを共同学習
- このアプローチにより、ユーザープライバシー保護とサーバーやモバイルエッジの作業負担が軽減
- シミュレーション評価で従来のJSCCアルゴリズムや従来の分離型通信アルゴリズムよりも性能が向上し、PSNRも2dB以上向上

Swin Transformerの活用と連合学習の組み合わせが、どんな新しい可能性を見せてくれるのかとっても楽しみ！プライバシー保護しつつ性能が上がるなんて、未来の通信技術って感じがするよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, cs.LG, eess.IV, **投稿日時:** 2024-07-31 10:25

- - -

### [On the Problem of Text-To-Speech Model Selection for Synthetic Data Generation in Automatic Speech Recognition](http://arxiv.org/abs/2407.21476)

**音声認識のための合成データ生成におけるテキスト音声合成モデル選択問題について**

Nick Rossenbach, Ralf Schlüter, Sakriani Sakti

- 神経テキスト音声合成(TTS)システムの急速な進展により、音声認識(ASR)などの他の自然言語処理分野で利用が広がった。
- 多数のTTSアーキテクチャが存在し、それぞれの拡張もあり、適切なTTSシステムを選定するのは容易ではない。
- 自動回帰デコーディングは非自動回帰デコーディングよりもデータ生成において良好な性能を示した。
- 計算可能な指標とASR性能との間に明確な関係性は見られなかったが、TTSの一般化能力を定量化するアプローチを提案。

最新の音声技術の進化の速さってすごいよね！この研究が将来の自然言語処理にどれだけ影響を与えるか楽しみ♪

**Comment:** Accepted at the SynData4GenAI 2024 workshop

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.LG, cs.SD, eess.AS, **投稿日時:** 2024-07-31 09:37

- - -

### [FedBChain: A Blockchain-enabled Federated Learning Framework for Improving DeepConvLSTM with Comparative Strategy Insights](http://arxiv.org/abs/2407.21282)

**FedBChain: 生体活動認識を改善するためのブロックチェーンを使った連合学習フレームワークと比較戦略の洞察**

Gaoxuan Li, Chern Hong Lim, Qiyao Ma, Xinyu Tang, Hwa Hui Tew

- LSTM層の数を減らすと予測性能が向上するが、分散トレーニングではセキュリティとプライバシーが問題
- FedBChainは、一層のLSTMを持つDeepConvLSTMアーキテクチャに基づく連合学習フレームワーク
- 三つの異なる実データセットと五つの異なる連合学習戦略を用いて、予測性能を比較
- FedAvgが平均4.54%、FedProxが4.57%、FedTrimmedAvgが4.35%、Krumが4.18%、FedAvgMが4.46%の改善を示す

ブロックチェーンと連合学習を組み合わせるなんて、そんな新発想があるんだね！セキュリティも向上するし、この手法がもっと普及すればいいなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.HC, **投稿日時:** 2024-07-31 02:12

- - -

### [LFFR: Logistic Function For (multi-output) Regression](http://arxiv.org/abs/2407.21187)

**LFFR: 多出力回帰のためのロジスティック関数**

John Chiang

- 完全準同型暗号化方式を用いたデータで多出力回帰問題に対応
- 線形およびリッジ回帰の固定ヘシアン法を改良し、単一出力ロジスティック回帰用の新しいLFFRアルゴリズムを多出力対応に適応
- 計算効率と堅牢性を確保するために定数の簡略化されたヘシアン法を多出力文脈に精緻化
- 実世界の複数のデータセットでの評価結果は、高い予測精度を維持しながらプライバシーを保護する能力を実証

多次元のデータに対応するために、こんなに工夫しているとはすごい！セキュリティと精度のバランスを両立しているところが未来感あるよね。

**Comment:** arXiv admin note: substantial text overlap with arXiv:2407.09955

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-30 20:52

- - -

### [FL-DECO-BC: A Privacy-Preserving, Provably Secure, and Provenance-Preserving Federated Learning Framework with Decentralized Oracles on Blockchain for VANETs](http://arxiv.org/abs/2407.21141)

**FL-DECO-BC：VANET向けに分散型オラクルを用いたプライバシー保護、証明可能なセキュリティ、および起源保護の連合学習フレームワーク**

Sathwik Narkedimilli, Rayachoti Arun Kumar, N. V. Saran Kumar, Ramapathruni Praneeth Reddy, Pavan Kumar C

- VANETsにおいて従来の中央集権型アプローチではデータプライバシーとセキュリティ問題が懸念される
- FL-DECO-BCはデータを共有せずに協調的なモデル学習を可能にする連合学習フレームワークを提案する
- 分散型オラクルとブロックチェーンを活用し、外部データソースに安全にアクセスしつつデータプライバシーを保護する
- 暗号技術と形式的検証を通じて証明可能なセキュリティを保証し、データ起源と履歴を追跡できる設計を組み込んでいる

ブロックチェーンと連合学習を組み合わせてVANETsの未来を変えちゃうなんて、超ワクワク！実用化が待ち遠しいよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-30 19:09
