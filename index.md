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

更新: 2024-11-14T04:22:38.092465

- - -

### [Locally Private Sampling with Public Data](http://arxiv.org/abs/2411.08791)

**公開データを用いた局所的なプライバシーサンプリング**

Behnoosh Zamanlooy, Mario Diaz, Shahab Asoodeh

- ローカル差分プライバシーは、ユーザーデータを保護する機械学習で使用されるが、データ記録が単一であるという制約がある。
- ユーザーのプライベートデータセットとパブリックデータセットの両方を活用する、局所的なプライバシーサンプリングの枠組みを提案。
- プライベートなサンプルを生成しつつ、パブリックデータセットを保持するメカニズムを設計することを目的とする。
- 一般的な$f$-分岐を用いた最小最大最適メカニズムを具体化し、実験で最先端のサンプラーと比較して効果を確認。

ユーザーのデータを守りながらも、今あるデータをうまく活用しようってアイデアがめっちゃ新しい！これが広まったら、もっと安全にオープンデータを活用できる世の中になりそうでワクワクするね。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-13 17:17

- - -

### [FedSub: Introducing class-aware Subnetworks Fusion to Enhance Personalized Federated Learning in Ubiquitous Systems](http://arxiv.org/abs/2411.08699)

**FedSub: ユビキタスシステムにおけるパーソナライズ連合学習向上のためのクラス認識サブネットワーク融合の導入**

Mattia Giovanni Campana, Franca Delmastro

- ユビキタスシステムでは、プライバシーを守りつつユーザの多様な行動に適応するモデルが重要である。
- 既存の手法は、パーソナライズと一般化のバランスが取れず、グローバルモデルに依存しがちである。
- FedSubは、クラス認識プロトタイプとサブネットワークを用いて個別化を強化する新手法である。
- FedSubは、実験によりリアルなシナリオでのデータヘテロ性に対処し、最高精度を達成した。

FedSubってすごくない？個々の特性を活かしたパーソナライズされたモデルって、未来の技術でめっちゃ期待できる！これからのウェアラブルデバイスとか、どんどんユーザーに合ったサービスになっていくんだろうなぁ。

**Comment:** Submitted to Proceedings of the ACM on Interactive, Mobile, Wearable   and Ubiquitous Technologies (IMWUT)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-13 15:42

- - -

### [Generalized Pose Space Embeddings for Training In-the-Wild using Anaylis-by-Synthesis](http://arxiv.org/abs/2411.08603)

**自然環境における解析合成を用いた一般化ポーズ空間埋め込みの訓練**

Dominik Borer, Jakob Buhmann, Martin Guay

- 大規模な手動ラベル付きデータに依存せず、ポーズ推定を行うための手法を提案
- 単純な骨格表現が精度の低下を引き起こす問題を改善する新たな表現を開発
- 合成データを用いて新しい表現を訓練し、ポーズの正確な予測を実現
- 提案した手法は標準ベンチマークで従来の分析合成モデルを上回る性能を示す

ポーズをレンダリングするってすごいよね！これで正確なポーズ推定がもっと簡単になりそうだね。手動のラベリングが減るのも嬉しいし、新しい骨格表現がどんなものか見てみたいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.HC, **投稿日時:** 2024-11-13 13:40

- - -

### [CorrSynth -- A Correlated Sampling Method for Diverse Dataset Generation from LLMs](http://arxiv.org/abs/2411.08553)

**CorrSynth -- LLMから多様なデータセットを生成するための相関サンプリング手法**

Suhas S Kowshik, Abhishek Divekar, Vijit Malik

- LLMを用いたデータ生成は多様性不足やバイアス問題がある
- CorrSynthを提案し、相関サンプリング戦略で多様で忠実なデータ生成を実現
- 提案手法は他のガイダンス技術よりも複雑さを克服
- 実験によりCorrSynthが多様性と性能向上に効果的であることを確認

LLMからのデータ生成をもっと多様で良い感じにする新しい手法の話だね！相関サンプリングって面白そう、色んなデータが簡単にいっぱい作れるようになりそう〜。どうやってバイアスなくすのかなってこれからも気になるな。

**Comment:** Published as a main conference paper at EMNLP 2024; First two authors   contributed equally

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-11-13 12:09

- - -

### [Dynamic Thresholding Algorithm with Memory for Linear Inverse Problems](http://arxiv.org/abs/2411.08284)

**メモリを用いた線形逆問題のための動的しきい値アルゴリズム**

Zhong-Feng Sun, Yun-Bin Zhao, Jin-Chuan Zhou, Zheng-Hai Huang

- ROTPは小中規模の線形逆問題を解決するが、大規模問題では計算コストが高い。
- マージした最適$k$-しきい値技術と反復法によりDTAMアルゴリズムを提案。
- DTAMは低計算複雑性で線形逆問題の解を見つけられる。
- DTAMは合成データや音声・画像処理で高速かつ競争力のある動作を実証。

しきい値アルゴリズムって工夫次第でこんなに速くできるんだね！実用性も高そうだから楽しみ～。実際にいろんなデータセットで試してみる価値がありそうだわ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.IT, cs.NA, math.IT, math.NA, **投稿日時:** 2024-11-13 01:50

- - -

### [SynapsNet: Enhancing Neuronal Population Dynamics Modeling via Learning Functional Connectivity](http://arxiv.org/abs/2411.08221)

**SynapsNet: 機能的接続学習によるニューロン集団ダイナミクスモデルの強化**

Parsa Delavari, Ipek Oruc, Timothy H Murphy

- 大規模ニューロンデータは新たなモデリング技術を必要としている
- SynapsNetはニューロン間の動的相互作用を効果的にモデル化する
- 各ニューロンは潜在埋め込みに基づき電流を送受信する
- 実験ではSynapsNetが既存モデルを上回る性能を示した

そんなに難しくて専門的なことをやってるんだね！ニューロンの相互作用が理解できると、脳の仕組みがもっとよく分かるかも？将来の脳研究にすごく役立ちそうな技術だね！



**トピック:** [合成データ](sd), **カテゴリ:** q-bio.NC, cs.LG, **投稿日時:** 2024-11-12 22:25

- - -

### [Large Language Models Can Self-Improve in Long-context Reasoning](http://arxiv.org/abs/2411.08147)

**大規模言語モデルは長文推論で自己改善できる**

Siheng Li, Cheng Yang, Zesen Cheng, Lemao Liu, Mo Yu, Yujiu Yang, Wai Lam

- 大規模言語モデル(LLM)は長文処理で進展しているが、長文推論が苦手
- 現在の手法は合成データで微調整するが、専門家の注釈に依存し限界がある
- 新手法\oursを提案し、質問の複数出力に基づく微調整で改善を図る
- 実験で他手法を上回る成果を示し、新たな自己改善技術の可能性を開く

長い文脈の推論って難しいけど、モデル自身が改善しちゃうってすごいね！これが広がると、もっと賢いAIがどんどん生まれてくるんじゃないかな。興味津々！

**Comment:** Project Page: https://github.com/SihengLi99/SEALONG

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-11-12 19:53
