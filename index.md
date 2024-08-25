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

更新: 2024-08-25T04:19:46.673219

- - -

### [Sharper Bounds for Chebyshev Moment Matching with Applications to Differential Privacy and Beyond](http://arxiv.org/abs/2408.12385)

**チェビシェフモーメントマッチングの鋭い境界と差分プライバシーへの応用**

Cameron Musco, Christopher Musco, Lucas Rosenblatt, Apoorv Vikram Singh

- ノイズを含んだチェビシェフ多項式モーメントから確率分布を回復する問題を研究
- ウォッシャースタイン距離で正確な回復を、以前よりも多くのノイズで達成
- 差分プライバシーを持つ合成データ分布を構築するシンプルな「線形クエリ」アルゴリズムを提案
- 対称行列のスペクトル密度を推定するための高速アルゴリズムも提案

一見難しそうだけど、差分プライバシーへの応用が身近になった感じがするね！よりノイズが多い状況でも精度を保てるって、実用性がすごく広がりそう。



**トピック:** [合成データ](sd), **カテゴリ:** cs.DS, cs.LG, **投稿日時:** 2024-08-22 13:26

- - -

### [Tackling Data Heterogeneity in Federated Learning via Loss Decomposition](http://arxiv.org/abs/2408.12300)

**連合学習におけるデータ異質性への対処: 損失分解を通じて**

Shuang Zeng, Pengxin Guo, Shuai Wang, Jianbo Wang, Yuyin Zhou, Liangqiong Qu

- データ異質性があると、ローカルモデルが発散し最適なグローバルモデルを得にくい
- 損失をローカル損失、分布シフト損失、集約損失に分解しそれぞれの影響を分析
- 提案する新手法FedLDは全ての損失項を同時に減少させるアプローチ
- 提案手法は異なるデータ異質性環境下で既存手法よりも優れたパフォーマンスを達成

この研究すごく興味深いね！データ異質性への対策がしっかりしてて、新しい手法も試してみたくなるな。連合学習がもっと進化しそう！

**Comment:** Accepted at MICCAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-22 11:18

- - -

### [Subsurface Scattering for 3D Gaussian Splatting](http://arxiv.org/abs/2408.12282)

**3Dガウススプラッティングによるサブサーフェス散乱**

Jan-Niklas Dihlmann, Arjun Majumdar, Andreas Engelhardt, Raphael Braun, Hendrik P. A. Lensch

- 散乱材料で構成される物体の3D再構成と再照明は、複雑な光の運搬のため困難
- 3Dガウススプラッティングは高品質な新しい視点合成をリアルタイムで実現
- 提案手法は3Dガウス表現と散乱成分の暗黙的な体積表現を用いてシーンを再構成
- すべてのパラメータをレイトレーシングによる微分レンダリングで最適化

最近のCG技術ってほんとにすごいよね！これなら3Dモデルの素材編集とかも超簡単そう。試してみたくなるよね！

**Comment:** Project page: https://sss.jdihlmann.com/

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.GR, **投稿日時:** 2024-08-22 10:34

- - -

### [Weight Scope Alignment: A Frustratingly Easy Method for Model Merging](http://arxiv.org/abs/2408.12237)

**重みスコープアライメント: モデル統合のための驚くほど簡単な手法**

Yichu Xu, Xin-Chun Li, Le Gan, De-Chuan Zhan

- トレーニングのランダム性や非独立同分布 (Non-I.I.D) データが、平均ベースのモデル融合に大きな課題をもたらす
- 重みスコープの変動がモデル統合の効果に大きく影響することを明らかにする
- 各層のパラメータが基本的にガウス分布に従うことから、新しい簡単な正則化手法「重みスコープアライメント (WSA)」を提案する
- WSAは、ターゲット重みスコープを用いた訓練と複数モデルの重みスコープの統一という二つの主要なコンポーネントを持つ

WSAって意外とシンプルなのにめっちゃ効果的かも！連合学習とかいろんなシナリオにも使えるから、これからの研究が超楽しみだよね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.AI, cs.LG, **投稿日時:** 2024-08-22 09:13

- - -

### [Empowering Over-the-Air Personalized Federated Learning via RIS](http://arxiv.org/abs/2408.12162)

**RISを活用した個別化FLのオーバー・ザ・エア促進**

Wei Shi, Jiacheng Yao, Jindan Xu, Wei Xu, Lexi Xu, Chunming Zhao

- オーバー・ザ・エア計算はタスク指向の計算と通信効率を統合する技術
- 単一のグローバルモデルでは、独立同分布でないローカルデータセットの問題を解決できない
- RIS技術を用いて、異なるクラスタ間の統計的干渉を排除し個別化FLを実現
- 提案した二つの個別化集約手法により、FLの収束性能が既存手法より優れることを数値結果が示した

RISを使ってローカルデータの不均一性に対応するなんてカッコいい！個別化が進むともっと使いやすくなりそう！

**Comment:** Accepted by SCIENCE CHINA Information Sciences

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, eess.SP, math.IT, **投稿日時:** 2024-08-22 07:10

- - -

### [Understanding Data Reconstruction Leakage in Federated Learning from a Theoretical Perspective](http://arxiv.org/abs/2408.12119)

**理論的観点から見た連合学習におけるデータ再構築漏洩の理解**

Zifan Wang, Binghui Zhang, Meng Pang, Yuan Hong, Binghui Wang

- 連合学習はデータプライバシーを保護するための新しい協調学習パラダイムである
- 近年の研究で、連合学習アルゴリズムはデータ再構築攻撃に脆弱であることが示されている
- 既存研究には、デバイスのデータ再構築の程度を理論的に説明する基盤が欠け、攻撃の効果比較が困難である
- 提案する理論的枠組みで、既存の攻撃の効果を理論的に比較し、iDLG攻撃がDLG攻撃よりも優れていることを検証した

データ再構築攻撃が実際にどれくらい効果的なのか、理論的に分かるようになるってことかな？連合学習の安全性がもっと高くなるといいなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-08-22 04:20

- - -

### [Federated Diabetes Prediction in Canadian Adults Using Real-world Cross-Province Primary Care Data](http://arxiv.org/abs/2408.12029)

**連合学習を用いたカナダ成人の糖尿病予測：実世界の州間プライマリケアデータを利用して**

Guojun Tang, Jason E. Black, Tyler S. Williamson, Steve H. Drew

- 電子健康記録と機械学習の統合で糖尿病予測の精度を向上
- 連合学習を導入し中央集権的なデータ管理を避けることでプライバシー問題を解決
- 連合MLPモデルは中央集権方式と同等以上の性能を示し、連合ロジスティック回帰モデルは劣る結果に
- ダウンサンプリング技術でクラス不均衡問題に対処し、省単位および中央集権的モデルと比較

新しいアプローチで糖尿病予測が改善されるなんて、本当に未来的だね！特にプライバシーを守りながら精度を保つ技術の進展にワクワクするなあ。

**Comment:** 10 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.CE, cs.AI, **投稿日時:** 2024-08-21 22:47

- - -

### [Confounding Privacy and Inverse Composition](http://arxiv.org/abs/2408.12010)

**プライバシーと逆合成の混同**

Tao Zhang, Bradley A. Malin, Netanel Raviv, Yevgeniy Vorobeychik

- ($\epsilon, \delta$)-混同プライバシーという新しいプライバシー概念を導入
- 差分プライバシーとPufferfishプライバシーを一般化するもので、因果関係を考慮
- 独立した混同プライバシーメカニズムの合成でプライバシー損失を過小評価する問題を明示
- 新しいコプラ-摂動法を提案し、最適化問題を解くことでグローバルなプライバシーを実現

新しいプライバシーの概念が具体的にどう活用されるか楽しみだよね。これが普及したら、もっと安心してデータを扱えそう！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-21 21:45

- - -

### [Parameter-Efficient Transfer Learning under Federated Learning for Automatic Speech Recognition](http://arxiv.org/abs/2408.11873)

**連合学習下での自動音声認識におけるパラメータ効率の良い転移学習**

Xuan Kan, Yonghui Xiao, Tien-Ju Yang, Nanxin Chen, Rajiv Mathews

- 自動音声認識（ASR）モデルの性能をユーザー固有のドメインで向上させることが課題
- 連合学習とパラメータ効率の良いドメイン適応法を使用
- データの大量要件と通信コストの問題を解決
- 適切なアダプターを用いることで集中型と同等の性能を実現

連合学習を使って、ユーザープライバシーを守りながらASRモデルの性能を高められるなんて鼻血でそう！未来のプライバシー保護サービスに期待が膨らむね。



**トピック:** [連合学習](fl), **カテゴリ:** eess.AS, cs.CR, cs.LG, **投稿日時:** 2024-08-19 22:28
