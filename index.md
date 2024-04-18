---
layout: single
title: トップページ
permalink: /
author_profile: true
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

To be written.

## 最新更新分

更新: 2024-04-18 02:16

- - -

### [MiniCheck: Efficient Fact-Checking of LLMs on Grounding Documents](http://arxiv.org/abs/2404.10774)

**MiniCheck: LLMの根拠文書に基づく効率的なファクトチェック**

Liyan Tang, Philippe Laban, Greg Durrett

- LLMの出力が証拠に基づいているかどうかを認識するのは、NLP内の多くの任務で中心的である
- 現在のファクトチェックの方法は計算コストが高く、一つの応答をチェックするために多数のLLM呼出しが必要である
- 本研究では、GPT-4で生成された合成データを用いて、400倍低コストでGPT-4レベルの性能を持つ小型モデルの構築方法を示す
- 提案システムMiniCheck-FT5は比較可能なサイズの全システムを上回り、GPT-4の精度に達する

**Comment:** LLM-AggreFact benchmark, MiniCheck models, data generation code at   https://github.com/Liyan06/MiniCheck

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-04-16 17:59

- - -

### [Confidential Federated Computations](http://arxiv.org/abs/2404.10764)

**機密性を高めた連合学習と分析のためのシステム**

Hubert Eichner, Daniel Ramage, Kallista Bonawitz, Dzmitry Huba, Tiziano Santoro, Brett McLarnon, Timon Van Overveldt, Nova Fallen, Peter Kairouz, Albert Cheu, Katharine Daly, Adria Gascon, Marco Gruteser, Brendan McMahan

- 連合学習と分析（FLA）は敏感なデバイス上のデータ処理に広く採用されているが、プライバシーに対する制限がある
- 差分プライバシー（DP）をFLAシステムに追加する現行方法は、デバイスごとの更新に過剰なノイズを加えるか、誠実なサービスプロバイダーを前提としている
- 秘密計算（SMPC）に基づく気づかれないアグリゲーションを導入することでサービスプロバイダーからの個別ユーザー更新情報へのアクセスを制限できるが、スケーラビリティの課題とシビル攻撃の脆弱性がある
- この論文では、信頼性のある実行環境（TEE）とオープンソーシングを活用してサーバー側の計算の機密性を保証し、外部から検証可能なプライバシー特性を提供する新しいシステムアーキテクチャを紹介する



**トピック:** [連合学習](fl), [差分プライバシー](dp), [秘密計算](mpc), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-04-16 17:47
