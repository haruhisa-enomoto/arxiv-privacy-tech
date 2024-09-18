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

更新: 2024-09-18T04:21:41.751496

- - -

### [Federated Learning with Integrated Sensing, Communication, and Computation: Frameworks and Performance Analysis](http://arxiv.org/abs/2409.11240)

**連合学習のための統合センシング、通信、および計算：フレームワークと性能解析**

Yipeng Liang, Qimei Chen, Hao Jiang

- サンプル収集と通信エラーがアルゴリズムの性能に悪影響を与えるため、FL-ISCCの設計が重要
- FedAVG-ISCCはIIDデータ下で複数のローカルアップデートによる利点からFedSGD-ISCCより良好な性能を示す
- 非IIDデータでは、FedSGD-ISCCがFedAVG-ISCCよりもロバストで性能が維持される
- FedSGD-ISCCは通信エラーに対してFedAVG-ISCCよりもレジリエントである

6G時代に向けた新しい連合学習のアプローチだね。エラーに強いアルゴリズムの話、これからの技術革新に期待が高まるね！

**Comment:** due to the limitation The abstract field cannot be longer than 1,920   characters", the abstract appearing here is slightly shorter than that in the   PDF file

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-09-17 14:42

- - -

### [Score Forgetting Distillation: A Swift, Data-Free Method for Machine Unlearning in Diffusion Models](http://arxiv.org/abs/2409.11219)

**スコア忘却蒸留: 拡散モデルにおける機械学習のための迅速かつデータ不要の手法**

Tianqi Chen, Shujian Zhang, Mingyuan Zhou

- 機械学習では信頼性と安全性を重視し、機械忘却（MU）は重要な土台である
- 伝統的なMU手法は厳しい前提に固執し、実データを必要とするものが多い
- スコア忘却蒸留（SFD）は不要な情報を「安全」なクラスに整合させる革新的手法
- 実験で目標クラスを迅速に忘れ、他の生成品質を保持しながら生成速度も向上

この研究、すごく未来感があるね！拡散モデルにおける安全性の改善だけじゃなくて、生成速度も上げちゃうのとか、まさに一石二鳥って感じ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-09-17 14:12

- - -

### [Synthetic data augmentation for robotic mobility aids to support blind and low vision people](http://arxiv.org/abs/2409.11164)

**盲目および低視力者を支援するロボティックモビリティ支援のための合成データ拡張**

Hochul Hwang, Krisha Adhikari, Satya Shodhaka, Donghyun Kim

- ロボティックモビリティ支援は深層学習ベースの視覚モデルに依存している
- 実世界データセットの収集が難しく、多様なタスクに対するデータが不足している
- Unreal Engine 4で生成された合成データがモデル性能向上に寄与することを発見
- 生成した合成データセットを公開し、BLV支援技術の研究を促進

ロボット使った盲目の人たちの支援ってもうすぐ実現するのかな？データセット公開ってありがたいね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-09-17 13:17

- - -

### [Large Language Models are Good Multi-lingual Learners : When LLMs Meet Cross-lingual Prompts](http://arxiv.org/abs/2409.11056)

**大規模言語モデルは優れた多言語学習者である：クロスリンガルプロンプトとの出会い**

Teng Wang, Zhenqi He, Wing-Yin Yu, Xiaojin Fu, Xiongwei Han

- 大規模言語モデル（LLM）はルールベースのデータ生成が容易
- 自然言語の曖昧さとルールの複雑性でLLMはしばしばルールを守れない
- 長く複雑な文脈に対して新たな多言語プロンプト（MLPrompt）戦略を提案
- MLPromptは最新のプロンプト方法を上回る性能を実証、自動チェック機構との統合も提案

クロスリンガルでプロンプトを使うなんて面白いよね！これでさらに精度が上がったら、よりスムーズに多言語対応できるんじゃないかなってワクワクする！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-09-17 10:33

- - -

### [Enhanced segmentation of femoral bone metastasis in CT scans of patients using synthetic data generation with 3D diffusion models](http://arxiv.org/abs/2409.11011)

**3D拡散モデルを使用した合成データ生成による患者のCTスキャンにおける大腿骨転移の強化セグメンテーション**

Emile Saillard, Aurélie Levillain, David Mitton, Jean-Baptiste Pialat, Cyrille Confavreux, Hélène Follet, Thomas Grenier

- 大腿骨転移のセグメンテーションは手動では時間がかかり、オペレーターのばらつきもある
- 3D DDPMを使用して、29個の転移病変と26個の健康な大腿骨を基に新たな合成データを生成
- 合成データを使用した3D U-Netセグメンテーションモデルは、実データのみを使用したモデルより優れた性能を発揮
- 特にオペレーターのばらつきを考慮した場合において、合成データを使用したモデルの効果が顕著

面白そうな研究だね！セグメンテーションの精度が上がると、患者さんのQOLもグッと上がりそう〜データ生成のアイデアも新しいし、もっと深掘りしたくなるね！

**Comment:** 14 pages, 5 figures 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.AI, cs.CV, **投稿日時:** 2024-09-17 09:21

- - -

### [Benchmarking Sim2Real Gap: High-fidelity Digital Twinning of Agile Manufacturing](http://arxiv.org/abs/2409.10784)

**Sim2Realギャップのベンチマーク：アジャイル製造のための高精度デジタルツイン**

Sunny Katyara, Suchita Sharma, Praveen Damacharla, Carlos Garcia Santiago, Lubina Dhirani, Bhawani Shankar Chowdhry

- デジタルツイン技術が製造資産をデジタル再現し、プロセス最適化や予知保全を実現
- シミュレーション環境から実世界への政策転移にドメインランダム化、カリキュラム学習を活用
- 産業自動化シナリオにおけるデジタルツインの性能を実データ遅延や適応速度で評価
- アジャイル製造に特化したデジタルツイン技術により、カスタマイズやプロトタイピングを迅速化

最新の融合技術を使って現実と仮想を行き来するデジタルツイン、未来の製造業にワクワクしちゃう！これが本格的に導入されたら、カスタマイズとかあっという間になるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, **投稿日時:** 2024-09-16 23:36

- - -

### [Federated Learning for Smart Grid: A Survey on Applications and Potential Vulnerabilities](http://arxiv.org/abs/2409.10764)

**スマートグリッドの連合学習: 応用と潜在的脆弱性に関する調査**

Zikai Zhang, Suman Rath, Jiaohao Xu, Tingsong Xiao

- スマートグリッド（SG）はリアルタイムの電力使用データを収集し、未来のエネルギー需要を予測するインフラ
- データセキュリティとプライバシー懸念から、連合学習（FL）がプライバシー、効率、精度のバランスを提供
- 世代、送電・配電、消費の三段階でのFL活用の進展と、潜在的な脆弱性を徹底的にレビュー
- FLに基づくSGシステムの攻撃防御戦略や堅牢なインフラ構築の必要性を強調し、将来の研究方向を提案

サマリーを読んでワクワクしてくるよね！FLがSGの将来をどう安全にしながら発展させるか、すごく面白そう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, C.2.4, **投稿日時:** 2024-09-16 22:42

- - -

### [Using Generative Models to Produce Realistic Populations of the United Kingdom Windstorms](http://arxiv.org/abs/2409.10696)

**生成モデルを用いたイギリスのリアルな風ストーム人口の生成**

Etron Yee Chun Tsoi

- イギリスの風ストームは物的被害や社会の混乱を引き起こし、命の危険を伴うこともある
- 観測データの不足が包括的分析と保険モデルの課題となっている
- 標準GAN、WGAN-GP、U-net拡散モデルを用いて風マップを生成し評価
- 生成モデルは保険業界のリスク評価と災害モデリングに有用である可能性を示唆

生成モデルって、保険とかの現実世界で役立ちそう！風ストームのリスク評価がもっと正確になるって良さそうだね。

**Comment:** 86 pages, 28 figures

**トピック:** [合成データ](sd), **カテゴリ:** physics.ao-ph, cs.LG, **投稿日時:** 2024-09-16 19:53

- - -

### [Benchmarking Secure Sampling Protocols for Differential Privacy](http://arxiv.org/abs/2409.10667)

**差分プライバシーのための安全なサンプリングプロトコルのベンチマーク**

Yucheng Fu, Tianhao Wang

- 差分プライバシーの中央モデルとローカルモデルについて述べる
- 多者間計算 (MPC) を用いた分散モデル提案、高い有用性とプライバシーの両立
- ノイズの効率的サンプリングが課題、多様なセキュリティ仮定と理論分析
- サンプリングプロトコルの包括的評価とパフォーマンス比較を実施

ふむふむ、分散モデルでのプライバシー守りつつ効率も求めるのとか、めちゃ挑戦的！実験データが参考にできたら色んな応用が期待できるね！

**Comment:** This is the full version (18 pages) of the paper Benchmarking Secure   Sampling Protocols for Differential Privacy published at CCS'2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-09-16 19:04

- - -

### [CaBaGe: Data-Free Model Extraction using ClAss BAlanced Generator Ensemble](http://arxiv.org/abs/2409.10643)

**CaBaGe: クラスバランス生成器アンサンブルを用いたデータフリーモデル抽出**

Jonathan Rosenthal, Shanchao Liang, Kevin Zhang, Lin Tan

- 機械学習サービス(MLaaS)はブラックボックスシステムのためモデル結果の再現や検証が困難
- データフリーモデル抽出を対象に、少ない問い合わせ数で高精度を達成
- 経験再生、生成器アンサンブル、多様な合成データ生成と選択的フィルタリングによる手法を提案
- クラス数を事前に知らない設定でクラス数を動的に学習し、高い精度と問い合わせ数の削減を実現

この研究って超面白そうじゃない？自分でデータなしにモデルを作り出せるって、未来感ハンパないね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CR, cs.LG, **投稿日時:** 2024-09-16 18:19

- - -

### [MAISI: Medical AI for Synthetic Imaging](http://arxiv.org/abs/2409.11169)

**MAISI: 合成画像のための医療AI**

Pengfei Guo, Can Zhao, Dong Yang, Ziyue Xu, Vishwesh Nath, Yucheng Tang, Benjamin Simon, Mason Belue, Stephanie Harmon, Baris Turkbey, Daguang Xu

- 医療画像解析はデータ不足、高い注釈コスト、プライバシー問題を抱えている
- MAISIは拡散モデルを用いて合成3D CT画像を生成し、これらの課題を解決
- 基盤ボリューム圧縮ネットワークと潜在拡散モデルを駆使し、柔軟なボリューム寸法とボクセル間隔で高解像度CT画像を生成
- ControlNetを組み込むことで、127の解剖学的構造の臓器セグメンテーションを条件に、正確に注釈された合成画像を生成可能

そのアイディア、すっごいね！合成データでここまでリアルな画像作れちゃう未来、ワクワクしない？



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.AI, cs.CV, **投稿日時:** 2024-09-13 18:15
