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

更新: 2024-06-26T04:20:58.596079

- - -

### [FedBiOT: LLM Local Fine-tuning in Federated Learning without Full Model](http://arxiv.org/abs/2406.17706)

**FedBiOT: 連合学習におけるフルモデルなしのLLMローカルファインチューニング**

Feijie Wu, Zitao Li, Yaliang Li, Bolin Ding, Jing Gao

- 大規模言語モデル（LLM）は適切なデータでファインチューニングするとドメイン特有のタスクで優れた性能を発揮する
- ドメイン特有のデータは複数の所有者間で分散しており、連合学習（FL）の文脈でLLMのファインチューニングを行う方法に関心が集まっている
- FLのクライアントは計算能力と通信容量が限られているため、LLMの効果的なファインチューニングが困難である
- FedBiOTでは圧縮LLMを生成し、それを用いてクライアントが軽量なアダプターをファインチューニングすることで、リソース消費を大幅に削減できる

FedBiOTめっちゃ素敵じゃない？軽量なアダプターだけで効果を維持しつつリソース削減とか、ほんとに現実的な解決策だと思う！連合学習の新しい時代が来るかもね！

**Comment:** KDD 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CL, cs.DC, **投稿日時:** 2024-06-25 16:45

- - -

### [Protecting the 'Stop Using My Data' Right through Blockchain-assisted Evidence Generation](http://arxiv.org/abs/2406.17694)

**ブロックチェーンを利用した「データ使用停止権」の保護**

Fan Zhang, Peng Liu

- 個人データの利用停止要求は基本的な権利であるが、既存の対策（例：暗号化データ消去、差分プライバシー）では対応が不十分
- データ取得後の権利侵害を防ぐための証拠生成フレームワークを初めて開発
- 「データ使用停止権」の問題を定式化し、ブロックチェーンを用いた証拠生成システムを設計・実装
- 証拠生成プロトコルの有効性を検証し、99%以上の成功率を達成

ブロックチェーンで証拠を作るなんてすごい技術！これが普及すれば、もっとプライバシーが守られる世の中になるかも♡



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-25 16:32

- - -

### [Robust Gray Codes Approaching the Optimal Rate](http://arxiv.org/abs/2406.17689)

**最適レートに迫るロバストなグレイコード**

Roni Con, Dorsa Fathollahi, Ryan Gabrys, Mary Wootters, Eitan Yaakobi

- ロバストなグレイコードは、ノイズが含まれても元の整数に近い値を復元できる
- この研究では、レート$1 - H_2(p) - \varepsilon$の近最適な構造を提案
- 提案されたコードは効率的にエンコード可能であり、高いノイズ耐性を持つ
- 効率的なデコードアルゴリズムにより推定誤差が小さいことが証明された

ロバストなグレイコードはプライバシー技術としても重要だね！ノイズに強いのってすごく未来を感じるよ。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.IT, cs.DS, math.IT, **投稿日時:** 2024-06-25 16:28

- - -

### [Capacity-Achieving Gray Codes](http://arxiv.org/abs/2406.17669)

**容量達成グレイコード**

Venkatesan Guruswami, Hsin-Po Wang

- 差分プライバシーのために整数をラプラスノイズかBSCノイズで曖昧にする方法を紹介
- BSCノイズを利用して整数をバイナリ文字列に変換する方法が柔軟である
- 提案された実装は、BSCの容量を正の誤り指数で達成する
- 古い実装に比べ、提案された「コーディドグレイコード」が誤り訂正機能を追加

誤り訂正機能付きグレイコードの実装って、すごく未来感あるよね！これからのプライバシー技術がもっと強くなりそうってワクワクする～。

**Comment:** 10 pages, 3 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.IT, cs.DS, math.IT, **投稿日時:** 2024-06-25 15:58

- - -

### [Privacy Preserving Reinforcement Learning for Population Processes](http://arxiv.org/abs/2406.17649)

**人口過程におけるプライバシー保護強化学習**

Samuel Yang-Zhao, Kee Siong Ng

- 動的に相互作用する大規模な人口を対象とするRLアルゴリズムにおけるプライバシー保護の問題を考察
- ベイズ的セマンティクスを通じて、相関データを含む人口過程に対する差分プライバシーの分析を実施
- 任意のRLアルゴリズムを差分プライバシー対応とするメタアルゴリズムを提案、各時点での状態および報酬信号をプライバタイズ
- 理論的に、プライベート化した状態に対する価値関数近似誤差が、人口サイズおよびプライバシー予算の増加に伴い迅速に減少することを証明

人口過程におけるプライバシー保護の問題って、実生活に応用できる可能性が豊富でワクワクするね。この技術が進歩すると、安全にデータを使用してより良い社会が期待できそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-25 15:41

- - -

### [Laminator: Verifiable ML Property Cards using Hardware-assisted Attestations](http://arxiv.org/abs/2406.17548)

**Laminator: ハードウェア支援アテステーションを用いた検証可能な機械学習プロパティカード**

Vasisht Duddu, Oskari Järvinen, Lachlan J Gunn, N Asokan

- 規制が機械学習モデルのトレーニングデータやプロセスに対する保証を求めており、各企業は透明性を高めるためにモデルカードやデータシートを使用
- 悪意のあるモデル提供者が誤情報を含む可能性があり、検証可能なプロパティカードの必要性がある
- ハードウェア支援の信頼実行環境（TEE）が高効率なアテステーションを提供し、検証可能なプロパティカードの実現が可能に
- Laminatorを提案し、複数の検証者にスケールし、モデルの構成に依存しない効率的なアテステーションを提供

新しい技術で透明性を追求するなんて未来っぽくてわくわくするね！Laminatorがどれだけ実際の運用に役立つか期待しちゃう。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-25 13:36

- - -

### [Dynamic Scheduling for Vehicle-to-Vehicle Communications Enhanced Federated Learning](http://arxiv.org/abs/2406.17470)

**車両間通信を強化するための動的スケジューリングと連合学習**

Jintao Yan, Tan Chen, Yuxuan Sun, Zhaojun Nan, Sheng Zhou, Zhisheng Niu

- 車両の計算能力とセンサ能力を活用して、連合学習をエッジトレーニングに適用
- V2V通信を強化する動的スケジューリング（VEDS）アルゴリズムを提案
- 長期的な確率最適化問題をオンライン混合整数非線形プログラミング問題に変換
- 提案したアルゴリズムは画像分類精度と軌道予測誤差を大幅に改善

新しい車両ネットワークの連合学習、とっても面白そうだね！移動しながらでも学習が進むなんて、未来の交通システムがますます楽しみだね！

**Comment:** Submitted to IEEE for possible publication

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, cs.IT, math.IT, **投稿日時:** 2024-06-25 11:15

- - -

### [Improving Grammatical Error Correction via Contextual Data Augmentation](http://arxiv.org/abs/2406.17456)

**文法誤り訂正の改善のためのコンテキストデータ増強**

Yixuan Wang, Baoxin Wang, Yijun Liu, Qingfu Zhu, Dayong Wu, Wanxiang Che

- 合成データを利用したデータ拡張が、文法誤り訂正（GEC）におけるデータ不足の問題を軽減する
- 合成データは主に事前学習フェーズに使用され、微調整フェーズではエラーディストリビューションが不一致で雑音が多い
- コンテキスト的データ増強に基づく合成データ構築方法を提案し、一貫したエラーディストリビューションを確保
- 生成モデルを利用してエラーパターンのリッチなコンテキストを生成、ラベルのノイズを軽減するリラベリング手法も提案

提案された方法の実験結果が強いベースラインを一貫して上回り、特に少量の合成データで状態最先端レベルを達成するところが面白いね。データ不足の課題を解決する新しいアプローチ、かなり期待できるかも。

**Comment:** Accepted as Findings of ACL 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-06-25 10:49

- - -

### [Towards Efficient and Scalable Training of Differentially Private Deep Learning](http://arxiv.org/abs/2406.17298)

**差分プライバシー深層学習の効率的かつスケーラブルな訓練に向けて**

Sebastian Rodriguez Beltran, Marlon Tobaben, Niki Loppi, Antti Honkela

- 差分プライバシー確保のための確率的勾配降下法（DP-SGD）の利便性低下が従来から問題視されている
- 実用面でのもう一つの大きな問題として、DP-SGDの計算コストの高さがある
- 本研究ではDP下で深層学習モデルを訓練する際の計算コストを定量的に評価し、低減方法を評価
- 効率的なDP-SGD実装や低精度での訓練、最大80GPUを用いたスケーリング挙動を研究

DP深層学習って、よりプライベートにするためのコストがすごく高いんだね！でも、もっと効率的な方法を探るってワクワクするし、80GPUまでスケールできると想像するとすごい😳💡

**Comment:** 15 pages, 12 figures, Accepted to the Workshop on Advancing Neural   Network Training at International Conference on Machine Learning (WANT@ICML   2024)

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-06-25 06:04

- - -

### [Task-Agnostic Federated Learning](http://arxiv.org/abs/2406.17235)

**タスク非依存型連合学習**

Zhengtao Yao, Hong Nguyen, Ajitesh Srivastava, Jose Luis Ambite

- 医療画像の分野では、大規模データセットの共有がプライバシーの懸念により困難
- 連合学習（FL）はプライバシーを保護しつつ協調学習を可能にするが、タスクやデータの異質性、ラベルの不足などの課題がある
- Vision Transformer（ViT）を利用して自己教師型FLフレームワークを採用し、初期ラベルなしで効果的な表現学習を実現
- 実世界の非同一分布医療画像データセットでの評価により、中央集約アプローチの5％のデータで90％のF1精度を維持し、アウトオブディストリビューションタスクへの適応も優れる

プライバシー保護しながらみんなで学べるとかすごいね！未来の医療がどんどん進む感じがしてわくわくする!



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.DC, **投稿日時:** 2024-06-25 02:53

- - -

### [Robust Zero Trust Architecture: Joint Blockchain based Federated learning and Anomaly Detection based Framework](http://arxiv.org/abs/2406.17172)

**堅牢なゼロトラストアーキテクチャ：ブロックチェーンベースの連合学習と異常検出に基づく枠組み**

Shiva Raj Pokhrel, Luxing Yang, Sutharshan Rajasegarar, Gang Li

- IoTネットワークにおける効率的なリモートワークと協力を目指し、分散システム用の堅牢なゼロトラストアーキテクチャを提案。
- 悪意あるクライアントからの更新を防ぐため、ブロックチェーンベースの連合学習原則を使用した堅牢な集約メカニズムを開発。
- 異常検出と信頼計算を統合し、無監視クラスタリング技術でゼロデイ攻撃のような新たな異常を検出、デバイス間の安全な協力を実現。
- スケーラビリティ向上、ディリクレ過程による先進的異常検出、量子暗号技術の統合を含む将来的な方向性を提示。

IoTでも安全にリモートワークできるなんて、すごいね！これからは量子コンピュータにも負けない時代になりそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.DC, cs.LG, **投稿日時:** 2024-06-24 23:15

- - -

### [Vastextures: Vast repository of textures and PBR materials extracted from real-world images using unsupervised methods](http://arxiv.org/abs/2406.17146)

**Vastextures: 実世界画像から抽出されたテクスチャとPBRマテリアルの大規模リポジトリ**

Sagi Eppel

- Vastexturesは、実世界画像から無監督で抽出された50万のテクスチャとPBRマテリアルを含むリポジトリ
- テクスチャは多様だが既存のリポジトリと比べて精緻さに欠ける
- 2Dテクスチャを自然画像から切り取り、そこからSVBRDF/PBRマテリアルを生成
- 大量の多様なアセットを必要とするAIシステムトレーニングに適している

実世界のパターンが多様に収集されているのがすごく面白そう！AIのトレーニング用データがこんなにたくさん手に入るなんて、未来が楽しみだね！

**Comment:** Vastexture was published as part of Learning Zero-Shot Material   States Segmentation, by Implanting Natural Image Patterns in Synthetic Data,   refer to this work in citations. This document gives a more detailed and   technical discussion of this repository

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-24 21:36

- - -

### [Achieving Fairness Across Local and Global Models in Federated Learning](http://arxiv.org/abs/2406.17102)

**連合学習におけるローカルおよびグローバルモデル間の公正性の実現**

Disha Makhija, Xing Han, Joydeep Ghosh, Yejin Kim

- FL（連合学習）ではデータの異質性やクライアントのプライベートデータの機密属性へのアクセス困難が公正性の課題
- \texttt{EquiFL}は、新たな公正性の用語をローカルの最適化目標に組み込み、公正性とローカル性能のバランスを取るアプローチ
- この協調メカニズムにより、クライアント間のコラボレーションフェーズでのバイアス伝播を防止
- 実験結果から、\texttt{EquiFL}はクライアントごとの正確性と公正性のバランスを実現し、均一な性能分布を保証することが示された

わぁ、この\texttt{EquiFL}っていうの、本当に皆に優しい感じで素敵だね！医療分野でそんな風に使われてるなんて感動的、もっと調べてみたくなっちゃうね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CY, **投稿日時:** 2024-06-24 19:42

- - -

### [Lomas: A Platform for Confidential Analysis of Private Data](http://arxiv.org/abs/2406.17087)

**Lomas: プライベートデータの機密解析のためのプラットフォーム**

Damien Aymon, Dan-Thuy Lam, Lancelot Marti, Pauline Maury-Laribière, Christine Choirat, Raphaël de Fondeville

- 公共サービスが収集する大量のデータが未活用である状況を解決するために、Lomasを提案
- データに直接アクセスせずに承認された研究者や政府アナリストがプライベートデータセット上でアルゴリズムを実行可能
- 差分プライバシーで結果を保護し、識別可能な情報抽出を無効化
- プライバシーを維持しながら公共サービスのデータから価値ある洞察を得られるようにする

データの保護と有効活用、両方を同時に達成するなんてすごいね！この技術、公衆衛生の改善にも役立ちそうで、未来が楽しみだよね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-24 19:16
