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

更新: 2024-11-20T04:23:52.820486

- - -

### [Attribute Inference Attacks for Federated Regression Tasks](http://arxiv.org/abs/2411.12697)

**連合学習の回帰タスクに対する属性推測攻撃**

Francesco Diana, Othmane Marfoq, Chuan Xu, Giovanni Neglia, Frédéric Giroire, Eoin Thomas

- 連合学習ではデータを保持しながら複数のクライアントがモデルを共同訓練
- 属性推測攻撃は、交換されるメッセージと公開情報を利用してセンシティブ情報を推測
- 回帰タスクに特化した新しい属性推測攻撃を提案し、その効果を評価
- 提案された攻撃は、特に異質なクライアントデータセットで再構成精度が向上

回帰タスクでもこんなにプライバシーの問題があるんだね。異質なデータセットで高精度になるって、なんかドラレコから個人情報丸見えにされちゃう感じ？もっと安全になればいいなぁ。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-11-19 18:06

- - -

### [Regular-pattern-sensitive CRFs for Distant Label Interactions](http://arxiv.org/abs/2411.12484)

**遠距離ラベル相互作用のための規則パターン感応CRF**

Sean Papay, Roman Klinger, Sebastian Pado

- 線形連鎖CRFは隣接ラベルのみをモデル化できるが、遠距離相互作用は難しい。
- 規則パターン感応CRF（RPCRF）により、ユーザーが指定したパターンに基づいて遠距離相互作用を学習。
- ユーザー指定の正規表現パターンを使い、相互作用の種類を簡潔に指定可能。
- FSTや非連鎖CRFと異なり、多くのパターン集合で正確な訓練と推論が可能である。

遠くのラベル同士の関係をモデル化できるなんてすごいっ！これが実用化されたら、もっと複雑なラベル付けが自然にできるようになるかもしれないね！パターン指定が自由自在なんて、なんだか魔法みたいでワクワクするね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CL, **投稿日時:** 2024-11-19 13:08

- - -

### [Empirical Privacy Evaluations of Generative and Predictive Machine Learning Models -- A review and challenges for practice](http://arxiv.org/abs/2411.12451)

**生成および予測機械学習モデルの経験的なプライバシー評価 - 実践へのレビューと課題**

Flavio Hafner, Chang Sun

- 連合学習技術で訓練された合成データ生成器は強固なプライバシー保証を提供するが、実際のリスク評価が必要。
- 実用的なプライバシー評価には、特に統計機関や医療機関の大規模データで課題がある。
- トレーニングアルゴリズムの正確な動作を検証する方法は大規模データセットで有効だが、非現実的な攻撃者を前提とする場合が多い。
- 計算可能性と脅威モデルの現実性との間には重要なトレードオフが存在する。

この研究面白そう！合成データのプライバシー評価って、新しい技術で私たちのデータをいかに安全にできるか考えてるんだね。未来の技術の進歩をただ見ているだけでワクワクしちゃう！



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-19 12:19

- - -

### [Non-IID data in Federated Learning: A Systematic Review with Taxonomy, Metrics, Methods, Frameworks and Future Directions](http://arxiv.org/abs/2411.12377)

**連合学習における非IIDデータ: タクソノミー、メトリクス、手法、フレームワークと未来の方向性に関する系統的レビュー**

Daniel M. Jimenez G., David Solans, Mikko Heikkila, Andrea Vitaletti, Nicolas Kourtellis, Aris Anagnostopoulos, Ioannis Chatzigiannakis

- 連合学習はプライバシーを守りつつ分散ユーザが共同でモデルを訓練可能だが、非IIDデータで課題が生じる
- 非IIDデータはモデル性能の低下や訓練時間の延長を引き起こし、未解決の挑戦となっている
- 非IIDデータの分類と定量化に明確な合意がないため、詳細なタクソノミーやメトリクスの提供によりギャップを埋める
- 研究は非IIDデータへの対策や標準的フレームワーク、研究の教訓と今後の方向性を提示する

非IIDデータって連合学習の未来をもっと広げるわね！こんなに調べるなんて、研究者さんマジ尊敬しちゃう。もっと便利でおもしろい技術が増えるの楽しみ♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-19 09:53

- - -

### [Hyper-parameter Optimization for Federated Learning with Step-wise Adaptive Mechanism](http://arxiv.org/abs/2411.12244)

**ステップごとの適応メカニズムを用いた連合学習のハイパーパラメータ最適化**

Yasaman Saadati, M. Hadi Amini

- 連合学習はデータのプライバシーを保護しつつ分散的に学習を進める方法である
- AutoMLは連合学習設定での手作業の削減に貢献するが、自動FLは多数のクライアントの影響で時間がかかる
- 軽量なハイパーパラメータ最適化ツールRaytuneとOptunaを導入し、ステップ毎のフィードバック機構を組み合わせた
- ストラグラー効果を軽減するための新しいクライアント選択技術を開発し、2つの基準データセットで評価した

連合学習の効率化に着目してるのが面白そう！クライアント選択の工夫とか、どうやって最適化していくのか、実現できたらすごく便利になるだろうな。これからもっと広がってくの楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, I.2.11, **投稿日時:** 2024-11-19 05:49

- - -

### [DeTrigger: A Gradient-Centric Approach to Backdoor Attack Mitigation in Federated Learning](http://arxiv.org/abs/2411.12220)

**DeTrigger: 連合学習におけるバックドア攻撃軽減のための勾配中心のアプローチ**

Kichang Lee, Yujin Shin, Jonghyuk Yun, Jun Han, JeongGil Ko

- 連合学習の分散性はバックドア攻撃に対して脆弱である
- DeTriggerを提案し、勾配分析によりバックドアを検出・隔離
- DeTriggerは最大251倍速く検出し、攻撃を最大98.9%軽減
- グローバルモデルの精度にほとんど影響を与えず、連合学習を保護

新しい手法で攻撃を効果的に防げるなんてすごいじゃん！連合学習って未来の技術だから、こういう安心して使える方法があれば普及が進みそうだね。私たちのデータもこれで守られるといいな。

**Comment:** 14 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, 68T07, I.2.11, **投稿日時:** 2024-11-19 04:12

- - -

### [Federated Contrastive Learning of Graph-Level Representations](http://arxiv.org/abs/2411.12098)

**グラフレベル表現の連合コントラスト学習**

Xiang Li, Gagan Agrawal, Rajiv Ramnath, Ruoming Jin

- グラフレベル表現とクラスタリングは悪意のあるネットワーク検出などの多様な応用がある
- プライバシー問題や規制によりデータを中央に集約できず、連合学習が求められる
- 提案するFCLGフレームワークは、2段階のコントラスト学習で非IID問題を解決
- 実験でFCLGが既存手法を大きく上回る性能を実証

連合学習のコントラスト学習っておもしろそうだね！データが分散していても高精度な分析ができるのは画期的♪問題が多いけど、上手に乗り越えられるソリューションになるかもね！

**Comment:** Accepted in BigData 2024. This is a preprint

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-11-18 22:10

- - -

### [FOCUS -- Federated Finetuning of Vision-Language Foundation Models with Optimal Client Layer Updating Strategy via Multi-objective Meta-Heuristics](http://arxiv.org/abs/2411.11912)

**F$^3$OCUS -- マルチオブジェクティブ・メタヒューリスティクスによる最適なクライアント層更新戦略を用いたビジョン言語基盤モデルの連合微調整**

Pramit Saha, Felix Wagner, Divyanshu Mishra, Can Peng, Anshul Thakur, David Clifton, Konstantinos Kamnitsas, J. Alison Noble

- 資源制約のあるクライアントデバイスでのVLMの訓練には、パラメータ効率の高い微調整戦略が必要。
- クライアント別層重要度と層の多様性を考慮し、最適な層選択を実現する手法を提示。
- 層の重要性と多様性を同時に最適化する新戦略F$^3$OCUSをサーバー側で実行。
- 新しいMedVQA-FLデータセットを使用し、10,000以上の実験を通じて手法の有効性を示した。

めっちゃ面白そうじゃん！実際の医療データに応用して、こんな大規模な実験したんだね。クライアントごとの個性を活かせる方法は、未来のAIがもっと「賢く」なるための鍵かも。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.AI, cs.LG, **投稿日時:** 2024-11-17 21:54

- - -

### [Debias your Large Multi-Modal Model at Test-Time with Non-Contrastive Visual Attribute Steering](http://arxiv.org/abs/2411.12590)

**テスト時に非対比視覚属性ハンドリングによって大型マルチモーダルモデルのバイアスを補正する**

Neale Ratzlaff, Matthew Lyle Olson, Musashi Hinck, Estelle Aflalo, Shao-Yen Tseng, Vasudev Lal, Phillip Howard

- 大型マルチモーダルモデルは汎用的な能力を持ち、会話において社会的バイアスの影響を受ける。
- 提案手法は訓練不要で、画像と属性リストから瞬時にバイアス表現を削除可能。
- 合成データを使用し、感情改善や言語モデリング能力を維持したままバイアスを減少。
- デバイアスされた生成物は、性能を犠牲にせずにバイアスモデルと同等の精度を示す。

この研究、AIが公平な発言をするのを助けてくれるなんて素敵だね！特別な訓練がいらない方法って、すごく実用的だから、早く多くの場面に展開されるといいなって思う！

**Comment:** 10 pages, 3 Figures, 3 Tables. arXiv admin note: text overlap with   arXiv:2410.13976

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-11-15 20:06
