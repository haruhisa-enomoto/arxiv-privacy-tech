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

更新: 2024-07-20T04:20:23.205054

- - -

### [MaRINeR: Enhancing Novel Views by Matching Rendered Images with Nearby References](http://arxiv.org/abs/2407.13745)

**MaRINeR: 近傍の参照画像と一致することで新しい視点を強化する手法**

Lukas Bösiger, Mihai Dusmanu, Marc Pollefeys, Zuria Bauer

- 3D再構築からの現実的なイメージレンダリングは、混合現実や自律エージェントの訓練に重要
- 従来の手法はノイズや欠損による不完全な再構築の影響を受けやすい
- MaRINeRは近隣のマッピング画像の情報を活用しターゲット視点のレンダリングを改善
- 定量的指標と定性的な例での改善が示され、合成データの強化や詳細復元に有効

視点を変えるだけで新しい世界が見えるなんてワクワクするね！これを利用して映像作品とかゲームがもっとリアルになる未来が楽しみだな☺️

**Comment:** Accepted to ECCV 2024; Project Page: see   https://boelukas.github.io/mariner/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, I.4.3, **投稿日時:** 2024-07-18 17:50

- - -

### [Differential Privacy Mechanisms in Neural Tangent Kernel Regression](http://arxiv.org/abs/2407.13621)

**差分プライバシーを用いたニューラルタンジェントカーネル回帰のメカニズム**

Jiuxiang Gu, Yingyu Liang, Zhizhou Sha, Zhenmei Shi, Zhao Song

- 学習データプライバシーは、顔認識や推薦システムなど多くのAIアプリケーションで重要な課題
- ニューラルタンジェントカーネル (NTK) 回帰で差分プライバシー (DP) の有効性を検証
- 差分プライバシーとテスト精度の両方に対して証明可能な保証を示す
- CIFAR10データセットでの実験により、適度なプライバシーバジェット下でも高精度を維持することを確認

差分プライバシーとNTKの組み合わせが新鮮だよね！AIのプライバシー問題、これからどんどん進化しそうでワクワクしちゃう〜



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-07-18 15:57

- - -

### [SecScale: A Scalable and Secure Trusted Execution Environment for Servers](http://arxiv.org/abs/2407.13572)

**SecScale: サーバ向けのスケーラブルで安全な信頼実行環境**

Ani Sunny, Nivedita Shrivastava, Smruti R. Sarangi

- 信頼実行環境（TEE）は現代の安全なプロセッサの一部であり、アプリケーションとコードの機密性や改ざん防止を担保する
- 2021年にIntelはSGXの非推奨を発表、その理由は256MBを超える拡張が困難でハードウェアの負荷が大きかったため
- 他の競合解決策はスケーラブルだが、リプレイ攻撃防止など多くの重要なセキュリティ保証を提供していない
- SecScaleは、投機実行、MACの森、完全なメモリ暗号化を使い、競合他社より10%速い

完全なメモリ暗号化とか投機実行のアイデア、すごくない？リプレイ攻撃も防げるなら実用性高そうだよね。未来のプロセッサの標準になっちゃうかも！



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.AR, **投稿日時:** 2024-07-18 15:14

- - -

### [EnergyDiff: Universal Time-Series Energy Data Generation using Diffusion Models](http://arxiv.org/abs/2407.13538)

**EnergyDiff: 拡散モデルを使用した時系列エネルギーデータの汎用生成**

Nan Lin, Peter Palensky, Pedro P. Vergara

- 電力や暖房システムなどのエネルギーシステムには高解像度の時系列データが必要
- データ収集コストとプライバシーの懸念から、必要なデータが不足する問題がある
- EnergyDiffは高解像度時系列データ生成のための新しい枠組みを提案
- 提案手法は従来の方法と比べて時空間依存性と周辺分布のキャプチャにおいて大幅な改善を実現

拡散モデルを使ってデータ生成するなんて、新しい技術っぽくてワクワクするね！これが普及すれば、データが足りない問題が解決できそう。

**Comment:** 10 pages, 8 figures

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.SY, eess.SY, **投稿日時:** 2024-07-18 14:10

- - -

### [PriPL-Tree: Accurate Range Query for Arbitrary Distribution under Local Differential Privacy](http://arxiv.org/abs/2407.13532)

**PriPL-Tree: ローカル差分プライバシー下で任意の分布に対する正確な範囲クエリ**

Leixia Wang, Qingqing Ye, Haibo Hu, Xiaofeng Meng

- 既存のLDPソリューションは、ドメインパーティション内のデータが均一であると仮定し、不正確な推定を招く
- PriPL-Treeは、階層的な木構造と区分線形関数を組み合わせてデータ分布を正確にモデル化
- データに基づいた適応型グリッドを用いて、多次元ケースにも対応
- 実データと合成データの実験で、最新のソリューションに比べて優れた性能を示す

PriPL-Treeがどうやって適応型グリッドを使うのか気になる！これがもっと実際のデータ分析に貢献しそうで楽しみ！

**Comment:** To appear in VLDB 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-07-18 14:05

- - -

### [Cheddar: A Swift Fully Homomorphic Encryption Library for CUDA GPUs](http://arxiv.org/abs/2407.13055)

**Cheddar: CUDA GPU用の高速な完全同型暗号ライブラリ**

Jongmin Kim, Wonseok Choi, Jung Ho Ahn

- 完全同型暗号（FHE）はクラウドコンピューティングのセキュリティとプライバシー問題を解決する技術
- FHEは処理が暗号化されるため計算負荷が非常に大きく、処理速度が2〜6桁遅くなる
- CheddarはCUDA GPU用のFHEライブラリで、従来のGPU実装と比較して大幅な性能向上を実現
- 32ビットの小さいワードサイズを用いた効率的なカーネル設計を採用し、具体的なFHEワークロードで2.9〜25.6倍の性能アップを達成

Cheddarって名前がかわいい！未来のクラウドセキュリティもこれで安心かもって感じだね〜。しかも、暗号技術がこんなに進化したら、もっといろいろなことが安全にできるようになるのが楽しみだな。

**Comment:** 12 pages, 5 figures

**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.PF, **投稿日時:** 2024-07-17 23:49

- - -

### [INTELLECT: Adapting Cyber Threat Detection to Heterogeneous Computing Environments](http://arxiv.org/abs/2407.13043)

**INTELLECT: 異種コンピューティング環境へのサイバー脅威検出の適応**

Simone Magnani, Liubov Nedoshivina, Roberto Doriguzzi-Corin, Stefano Braghin, Domenico Siracusa

- クラウド、エッジ、IoTの普及で異種デバイスが増加し攻撃対象が広がる
- 連合学習を用いて異なる組織間でデータを統合、MLベースのIDSを開発
- INTELLECTは特徴選択、モデルプルーニング、微調整でMLモデルを動的に適応
- 知識蒸留技術を取り入れ、局所ネットワークパターンに適応しつつ歴史的知識を保持

異なるデバイスや環境に対する柔軟なアプローチが面白そう。サイバー脅威検出の精度向上に期待できるかも！

**Comment:** 14 pages, 10 figures, 4 tables, 3 algorithms, submitted to Elsevier   Computers and Security

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-17 22:34

- - -

### [Proof-of-Collaborative-Learning: A Multi-winner Federated Learning Consensus Algorithm](http://arxiv.org/abs/2407.13018)

**協調学習の証明: 複数の連合学習者によるコンセンサスアルゴリズム**

Amirreza Sokhankhosh, Sara Rouhani

- ブロックチェーンは取引の検証やネットワークの同期のためにコンセンサス機構が必要
- PoWは大量のエネルギーを消費するが生産的な出力がない
- PoCLはブロックチェーンの計算力を連合学習モデルの訓練に転用する機構を提案
- 新しい評価機構と報酬分配システムにより効率と公平性を保証

PoCLのアイディアってすごくエコだし、未来のブロックチェーンの姿が見えそう！エネルギーを賢く使うなんて、ちょっとヒーロー的じゃない？💫

**Comment:** \c{opyright} 2024 IEEE. Personal use of this material is permitted.   Permission from IEEE must be obtained for all other uses, in any current or   future media, including reprinting/republishing this material for advertising   or promotional purposes, creating new collective works, for resale or   redistribution to servers or lists, or reuse of any copyrighted component of   this work in other works

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-07-17 21:14

- - -

### [High-Quality Tabular Data Generation using Post-Selected VAE](http://arxiv.org/abs/2407.13016)

**高品質な表形式データ生成のためのポストセレクションVAEの活用**

Volodymyr Shulakov

- データプライバシーの懸念が高まる中、合成表形式データが必要
- 従来の技術は複雑なデータセットに対応できないか、実行時間が劣る
- PSVAEは単純なモデルで、短い実行時間で高品質な合成データを生成
- 損失最適化とポストセレクションの2つのキーアイデアを組み込み、現代の活性化関数Mishを用いる

PSVAEが短時間で高品質なデータ生成を可能にする点、すごく興味深いよね。将来、データプライバシーの懸念がもっと増えるから、こういう技術がもっと重要になりそうだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.SE, G.3, **投稿日時:** 2024-07-17 21:07

- - -

### [Novel Deep Neural Network Classifier Characterization Metrics with Applications to Dataless Evaluation](http://arxiv.org/abs/2407.13000)

**新規深層ニューラルネットワーク分類器の特徴評価メトリクスと無データ評価への応用**

Nathaniel Dean, Dilip Sarkar

- DNN分類器の訓練品質を例示データセットなしで評価
- 分類器の品質は重みベクトルを用いて推定
- 合成データを入力とする特徴ベクトルを用いた2つのメトリクスで特徴抽出器を評価
- ResNet18をCAFIR10とCAFIR100データセットで訓練した実証研究で、無データ評価の可能性を確認

これはめっちゃ面白そう！データがなくてもDNNの性能を評価できるって、新しい可能性がひろがる感じ。技術がもっと広まったら、いろんな分野で応用できちゃいそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.NE, **投稿日時:** 2024-07-17 20:40

- - -

### [A Framework for testing Federated Learning algorithms using an edge-like environment](http://arxiv.org/abs/2407.12980)

**エッジに近い環境を用いた連合学習アルゴリズムテストの枠組み**

Felipe Machado Schwanck, Marcos Tomazzoli Leipnitz, Joel Luís Carbonera, Juliano Araujo Wickboldt

- 連合学習（FL）は多くのクライアントがデータを非集中化しつつ中央集権的モデルを共同で訓練する機械学習のパラダイム
- FLはエッジコンピューティングでよく使われ、データの発生現場近くで計算を行うことで応答時間短縮やデータプライバシー向上を実現
- クライアントのデータ分布が異なるため、局所モデルの貢献度の正確な評価が難しいという課題がある
- 本研究はFLアルゴリズムをより簡単かつスケーラブルに評価するための枠組みを提案し、Kubernetesを用いた分散エッジ環境で評価

連合学習ってめっちゃ未来っぽい！エッジコンピューティングの活用で、データも安全かつ効率的に扱えそうだよね。Flutterでアプリ作りながら、私たちもこんな技術に触れてみたいな～。

**Comment:** Article submitted to Future Generation Computer Systems (Elsevier)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, cs.NI, C.2.4; I.2.11, **投稿日時:** 2024-07-17 19:52
