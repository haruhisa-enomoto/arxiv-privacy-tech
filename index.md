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

更新: 2024-08-14T04:20:12.994414

- - -

### [Improved Counting under Continual Observation with Pure Differential Privacy](http://arxiv.org/abs/2408.07021)

**純粋な差分プライバシーを用いた連続観察下での計数の改善**

Joel Daniel Andersson, Rasmus Pagh, Sahel Torkamani

- 差分プライバシーの連続観察下での計数問題は広く研究されている
- 従来の$\varepsilon$-差分プライバシーでの平均二乗誤差の改善はなかった
- この論文は、二項木メカニズムの新たな一般化に基づき、誤差を約4倍に削減
- 提案手法は、従来のガウスノイズを用いたメカニズムよりも$\delta$が十分に小さい場合に優れた精度を示す

この研究の新しいメカニズムはすごく興味深いね。今後の差分プライバシーの応用に大きなインパクトを与えそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DS, **投稿日時:** 2024-08-13 16:36

- - -

### [The Complexities of Differential Privacy for Survey Data](http://arxiv.org/abs/2408.07006)

**調査データにおける差分プライバシーの複雑性**

Jörg Drechsler, James Bailie

- 複数段階のデータ生成過程が差分プライバシーの実装を困難にする
- 複雑なサンプリングデザインが原因でプライバシー増幅が限られる
- 調査加重推定の影響が差分プライバシーの効力に関係
- 欠測値の代入や無回答調整の点でも課題がある

調査データに差分プライバシーを適用する難しさが伝わるね。でも、それを乗り越えたら新しい標準が生まれるかもってワクワクするよ！

**Comment:** 18 pages, 2 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ME, cs.CR, **投稿日時:** 2024-08-13 16:15

- - -

### [Faster Private Minimum Spanning Trees](http://arxiv.org/abs/2408.06997)

**高速なプライベート最小全域木**

Rasmus Pagh, Lukas Retschmeier

- クラスタリングや合成データ生成に動機づけられ、重み付き差分プライバシー下での最小全域木の公開問題を検討
- 既存の手法では、重み行列の各エントリにノイズを加えたり、特定のアルゴリズムの実行中にノイズを加える方法がある
- 新しいアルゴリズムは、従来の手法と同等の使用性で、計算時間を$O(m + n^{3/2}\log n)$に短縮を実現
- 実験結果が、利用効率または実行時間のどちらにおいても、既存のアルゴリズムを大幅に改善することを示している

差分プライバシーを保持しながらも計算効率をかなり上げられるところがすごいよね！これでクラスタリングとか合成データの生成がもっと簡単になりそう。



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, cs.LG, **投稿日時:** 2024-08-13 16:00

- - -

### [Breaking Class Barriers: Efficient Dataset Distillation via Inter-Class Feature Compensator](http://arxiv.org/abs/2408.06927)

**クラス間の壁を超えて：インタークラス特徴補償器を用いた効率的なデータセット蒸留**

Xin Zhang, Jiawei Du, Ping Liu, Joey Tianyi Zhou

- データセット蒸留は、大規模な自然データセットの情報豊富な特徴をコンパクトで合成的な形に凝縮する技法である
- クラス固有の合成パラダイムが主流であり、これが特徴凝縮の効率を制限している
- インタークラス特徴補償器（INFER）は、クラス固有のデータラベルフレームワークを超えた新しい蒸留アプローチである
- INFERは、クラス間の特徴統合を促進し、蒸留効率と一般化可能性を大幅に向上させる

この論文、面白そう！データセットのサイズを劇的に減らせるなら、将来のAIのトレーニングがもっと効率的になるかもね。INFERの効果、実際に試してみたいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-08-13 14:29

- - -

### [Heterogeneity: An Open Challenge for Federated On-board Machine Learning](http://arxiv.org/abs/2408.06903)

**異質性：連合搭載機械学習における未解決の課題**

Maria Hartmann, Grégoire Danoy, Pascal Bouvry

- 衛星ミッション設計が個別のモノリシック衛星から複数衛星の分散ミッションへとシフト
- オンボード軌道エッジコンピューティングへの関心が高まり、連合学習が有望視されている
- 異質な衛星間の即席協業における連合学習の課題を体系的にレビュー
- クロスプロバイダーのユースケースでの最先端技術の概要と問題探求のためのエントリーポイントを提供

異なるプロバイダー間の衛星協力とかカッコいい！この技術が進めば、衛星同士がもっと賢くなりそうで楽しみだね✨

**Comment:** Accepted to the ESA SPAICE conference 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.DC, cs.LG, **投稿日時:** 2024-08-13 13:56

- - -

### [Voltran: Unlocking Trust and Confidentiality in Decentralized Federated Learning Aggregation](http://arxiv.org/abs/2408.06885)

**Voltran：分散型連合学習集約での信頼性と機密性の解放**

Hao Wang, Yichen Cai, Jun Wang, Chuan Ma, Chunpeng Ge, Xiangmou Qu, Lu Zhou

- 連合学習モデルにおいて、フェデレーテッドラーニングの集約を単一のサーバーではなく分散ノードを使用
- 従来のFLが抱える中央集権サーバーの脆弱性を解消し、ブロックチェーンの信頼性と堅牢性を取り入れる
- Trusted Execution Environment (TEE)とブロックチェーン技術を組み合わせ、FLの信頼性、機密性、堅牢性を実現
- 複数のSGXパラレル実行戦略により、大規模FL作業負荷を軽減し、多様なFLシナリオでの強力なスケーラビリティを提供

こういうの本当にすごい！✨ 自分たちのデータがもっと安心安全に使えるようになるって、未来が楽しみだね。技術の進歩ってホントにわくわくしちゃう！



**トピック:** [連合学習](fl), [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-13 13:33

- - -

### [CRISP: Confidentiality, Rollback, and Integrity Storage Protection for Confidential Cloud-Native Computing](http://arxiv.org/abs/2408.06822)

**CRISP：機密性、ロールバック、および整合性保護のためのクラウドネイティブコンピューティング**

Ardhi Putra Pratama Hartono, Andrey Brito, Christof Fetzer

- TEEは実行中のコードと関連データの機密性と整合性を保護
- しかし、TEEの整合性保護はディスクに保存された状態には及ばない
- CRISPはIntel SGXを使用してロールバックを防ぐメカニズムを提案
- CRISP使用によるリソース増加はあるが、パフォーマンス低下は小さい

マジで興味深いね！クラウド環境でのロールバック攻撃を防ぐ手段って、クリティカルなセキュリティ対策になるよね。私たちが使ってるアプリもこんな技術で守られたら安心だね～



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, cs.OS, **投稿日時:** 2024-08-13 11:29

- - -

### [Prioritizing Modalities: Flexible Importance Scheduling in Federated Multimodal Learning](http://arxiv.org/abs/2408.06549)

**モダリティの優先順位付け: 連合型マルチモーダル学習における柔軟な重要度スケジューリング**

Jieming Bian, Lei Wang, Jie Xu

- 連合学習はユーザープライバシーを確保した機械学習手法であるが、現実のデータには適用が難しい
- マルチモーダル連合学習が登場し、多様なデータに対するモダリティ特化のエンコーダモデルを使用
- 既存の方法はモダリティ毎に均等に計算資源を割り当てるが、IoTデバイスでは非効率
- FlexModはモダリティの重要度とトレーニング要件に基づいて計算資源を適応的に割り当て、パフォーマンスを最適化

モダリティごとにリソースを賢く配分するのがカギになるね！データの多様性に対応しているので、幅広いデバイスで効率的に活用できるんじゃないかなぁ。

**Comment:** Submitted to IEEE TMC, under review

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-08-13 01:14

- - -

### [Evaluating Privacy Measures for Load Hiding](http://arxiv.org/abs/2408.06460)

**負荷隠蔽のためのプライバシー対策の評価**

Vadim Arzamasov, Klemens Böhm

- スマートメーターによる電力消費測定がプライバシー問題を引き起こす
- 様々な負荷隠蔽アルゴリズムが設計され、異なるプライバシー対策が提案されている
- 25の対策のうち20は効果がないと判明
- 相互情報量の変種が「家電使用」秘密に対して最も有効であることを発見

スマートグリッドの世界すごく進んでるね！どのプライバシー対策が実際には有効なのか、実験で特定したところが面白いなあ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.IT, math.IT, 94A60, 93A14, K.6.5; H.3.5, **投稿日時:** 2024-08-12 19:21

- - -

### [FedRobo: Federated Learning Driven Autonomous Inter Robots Communication For Optimal Chemical Sprays](http://arxiv.org/abs/2408.06382)

**FedRobo: 連合学習駆動の自律型ロボット通信による最適な化学噴霧**

Jannatul Ferdaus, Sameera Pisupati, Mahedi Hasan, Sathwick Paladugu

- 連合学習により、ロボットが中央データに依存せず互いの経験から学習可能
- 個々のロボットが作物状態と化学噴霧効果を保持し定期的に共有
- 作物状態や天候などの情報交換を通じて化学噴霧を最適化する通信プロトコルを設計
- 提案されたクラスタベースの連合学習アプローチは、グローバルサーバーの計算負荷とクライアント間の通信オーバーヘッドを効果的に軽減

農業の未来がこんなに進化するなんてワクワクするよね！連合学習を駆使したスマートなロボットたちがどんな成果を示すのか楽しみ♡

**Comment:** This research article is going to be submitted to a best-fit   conference. We are looking for a conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, cs.DC, cs.RO, **投稿日時:** 2024-08-10 00:32

- - -

### [Verifiable Decentralized IPFS Cluster: Unlocking Trustworthy Data Permanency for Off-Chain Storage](http://arxiv.org/abs/2408.07023)

**検証可能な分散型IPFSクラスター：オフチェーンストレージの信頼性を解き放つ**

Sid Lamichhane, Patrick Herbke

- オフチェーンストレージとしてIPFSがブロックチェーンの制限を克服する
- IPFSでのデータ保持はピン止めに依存し、信頼性の問題や単一点障害が存在
- VDIC(検証可能な分散型IPFSクラスター)を導入し、検証可能なデータ永続性を保証
- VDICは従来のピン止めサービスに匹敵する性能を持ち、実用ケースでの有用性も確認

分散型アプリのオフチェーンストレージ、ちょっとワクワクしない？新技術で信頼できるデータ保持が実現できるなんてすごいよね、どんな可能性が広がるのか楽しみだな。



**トピック:** [SSI/DID/VC](ssi), **カテゴリ:** cs.DC, cs.CR, **投稿日時:** 2024-08-09 08:26
