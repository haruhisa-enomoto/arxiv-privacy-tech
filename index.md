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

更新: 2024-08-29T04:20:28.711985

- - -

### [ModalityMirror: Improving Audio Classification in Modality Heterogeneity Federated Learning with Multimodal Distillation](http://arxiv.org/abs/2408.15803)

**ModalityMirror: マルチモーダル蒸留でモダリティ異質性連合学習における音声分類の改善**

Tiantian Feng, Tuo Zhang, Salman Avestimehr, Shrikanth S. Narayanan

- マルチモーダル連合学習はモダリティの異質性により、特に音声認識性能が低下する課題がある
- ModalityMirrorを導入し、視聴覚連合学習モデルから知識蒸留を利用して音声モデルの性能を向上
- ModalityMirrorは、モダリティ別のエンコーダー集約と単一モーダルモデルの訓練の2段階で構成される
- 実験結果は、特に動画の欠如する視聴覚連合学習において、最新FL方法より音声分類を大幅に改善することを示した

連合学習にマルチモーダル蒸留を組み合わせるの、すごく革新的！音声データがちゃんと活かされるようになると、色々な可能性が広がりそうで楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** eess.AS, cs.AI, cs.SD, **投稿日時:** 2024-08-28 13:56

- - -

### [Efficient LLM Scheduling by Learning to Rank](http://arxiv.org/abs/2408.15792)

**ランク学習による効率的なLLMスケジューリング**

Yichao Fu, Siqi Zhu, Runlong Su, Aurick Qiao, Ion Stoica, Hao Zhang

- LLM要求の出力長は事前に不明とされ、FCFS戦略はHOLブロッキングとスループット低下を招く
- 各要求の出力長を正確に予測することは難しいが、バッチ内の相対順位を予測することは可能
- このランキング情報を使い、新しいスケジューラーを開発し、既存の方法よりSJFスケジュールを近似
- 最先端のLLMサービングシステムに統合し、チャットボットで2.8倍の低遅延、合成データ生成で6.5倍のスループット向上を実現

新しいスケジューリング方法でこんなに性能がアップするなんてすごいね！合成データ生成での大幅なスループット向上も、実際の応用が楽しみだな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-28 13:35

- - -

### [Interactive Agents: Simulating Counselor-Client Psychological Counseling via Role-Playing LLM-to-LLM Interactions](http://arxiv.org/abs/2408.15787)

**インタラクティブエージェント：ロールプレイングでLLM対LLMの相互作用によるカウンセラー-クライアント心理カウンセリングのシミュレーション**

Huachuan Qiu, Zhenzhong Lan

- 大規模言語モデル (LLM) を利用したバーチャルカウンセラーが、クライアントのメンタルヘルス支援システムを構築
- 人間によるカウンセリングの注釈は時間がかかり、コストが高く、プライバシーの保護が求められ、拡張性に欠ける
- 提案フレームワークでは、2つのLLMがカウンセラーとクライアントの役割を担い、対話をシミュレート
- LLM生成対話と人間生成対話の違いを評価し、メンタルヘルスモデルとの比較実験を実施

カウンセリングをAIで再現するって、すごく未来的！これが普及したら、多くの人が気軽に心理支援を受けられるようになりそうで楽しみだよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.IR, **投稿日時:** 2024-08-28 13:29

- - -

### [Protecting Privacy in Federated Time Series Analysis: A Pragmatic Technology Review for Application Developers](http://arxiv.org/abs/2408.15694)

**連合時系列分析におけるプライバシー保護：アプリケーション開発者のための実用技術レビュー**

Daniel Bachlechner, Ruben Hetfleisch, Stephan Krenn, Thomas Lorünser, Michael Rader

- 医療や製造業などの分野で、連合分析の潜在力が非常に高い
- 効率や信頼の要件は全同型暗号などの技術で対応可能
- 実世界のユースケースに基づく定性要件を導出し、利用可能な技術と対応付け
- 決定ツリーを提供し、開発者が最適な技術を選定できるよう支援

医療や製造業でのプライバシー技術の活用方法がわかるのが面白そう！どんな技術が将来さらに発展するのか、期待しちゃうよね。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-08-28 10:41

- - -

### [Synthetic Forehead-creases Biometric Generation for Reliable User Verification](http://arxiv.org/abs/2408.15693)

**信頼できるユーザ認証のための合成額シワ生体データ生成**

Abhishek Tandon, Geetanjali Sharma, Gaurav Jaswal, Aditya Nigam, Raghavendra Ramachandra

- 額のシワパターンは顔や虹彩、眼周囲認識の代替手段であり、特にマスク着用時に有用
- 額のデータ収集はコストと時間の制約があり、多数の高品質画像が必要
- 合成生体データはプライバシー保護と効果的な深層学習ベースの検証訓練を可能にする
- 提案されたフレームワークで合成データが検証精度の向上に寄与することを確認

これ、マスクで顔が隠れても認証できる技術って面白そう！プライバシーも守れるし、合成データでトレーニングできるのがすごいね。

**Comment:** Accepted at Generative AI for Futuristic Biometrics - IJCB'24 Special   Session

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-08-28 10:33

- - -

### [Convergent Differential Privacy Analysis for General Federated Learning: the f-DP Perspective](http://arxiv.org/abs/2408.15621)

**一般的な連合学習のための収束差分プライバシー分析：f-DPの視点**

Yan Sun, Li Shen, Dacheng Tao

- 連合学習(FL)と差分プライバシー(DP)の協力が大規模なプライベートクライアントのための有望な学習フレームワークを提供する
- ノイズ付与によるDPアルゴリズムが多く研究され、FL-DPに広く適用されるが、長期のコミュニケーションラウンドではプライバシー漏洩の定量化が難しくなる
- Noisy-FedAvgメソッドの最悪のプライバシーは、シフテッドインターポレーション技術の助けを借りて、厳密な収束下限を達成する
- Noisy-FedProxメソッドでは、プロキシ項の正則化により、最悪のプライバシーが安定した定数下限を持つ

長期的なプライバシー保護の信頼性が問題になることを考えると、この研究の革新性とその実用性には興味がわくね！特に2つのメソッドの違いがどれだけ効果的かもっと知りたくなるよね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-08-28 08:22

- - -

### [On the Benefits of Visual Stabilization for Frame- and Event-based Perception](http://arxiv.org/abs/2408.15602)

**フレームベースおよびイベントベースの視覚安定化の利点について**

Juan Pablo Rodriguez-Gomez, Jose Ramiro Martinez-de Dios, Anibal Ollero, Guillermo Gallego

- ロボットの用途での大きな方位変化は視覚システムの性能に影響を与える
- カメラ回転を補償するための機械的安定装置の統合は困難な場合がある
- 本研究は、フレームとイベントの両方でカメラ回転を補償する処理ベースの手法を提案
- 安定化により特徴追跡精度が27.37%、カメラ自動運動推定精度が34.82%向上し、処理時間も25%以上短縮される

視覚システムの精度と効率がここまで変わるなんてすごいよね！ロボットの未来がもっと面白くなりそうだよ。ぜひこの技術が実際に使われるところを見てみたいな。

**Comment:** 8 pages, 4 figures, 4 tables,   https://github.com/tub-rip/visual_stabilization

**トピック:** [合成データ](sd), **カテゴリ:** cs.RO, cs.CV, eess.IV, **投稿日時:** 2024-08-28 07:49

- - -

### [Exploring Selective Layer Fine-Tuning in Federated Learning](http://arxiv.org/abs/2408.15600)

**連合学習における選択的階層微調整の探求**

Yuchang Sun, Yuexiang Xie, Bolin Ding, Yaliang Li, Jun Zhang

- 連合学習では分散データを用いることでプライバシーを保護しつつ基礎モデルを微調整する
- 限られたリソース下では、クライアントがタスクに合わせた特定の層を選んで調整する方が実用的
- 選択する層の重要性とクライアント間の異質な選択がモデルの収束に大きな影響を与えることを理論的に示す
- 提案する戦略的層選択方法はローカル勾配を利用し、クライアント間の層選択を制御する

選択的な層の調整が、連合学習の成功のカギになりそう！どの層を微調整するかで効果が全然違うんだって。これでリソースが少ない環境でも効率よく学習できそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-08-28 07:48

- - -

### [VFLIP: A Backdoor Defense for Vertical Federated Learning via Identification and Purification](http://arxiv.org/abs/2408.15591)

**VFLIP: 縦型連合学習におけるバックドア攻撃防御手法の識別と浄化による新提案**

Yungi Cho, Woorim Han, Miseon Yu, Ho Bae, Yunheung Paek

- VFL（縦型連合学習）は垂直に分割されたデータを扱い、バックドア攻撃の脆弱性がある
- 従来の防御機構はHFL（水平型連合学習）向けでありVFLには効果が薄い
- VFLIPは初のVFL専用バックドア防御であり、識別と浄化の技術を用いて攻撃対策を強化
- CIFAR10やBankMarketingなどの実験で、VFLIPがバックドア攻撃を効果的に緩和することを実証

VFLIPって、縦型連合学習に特化した初めてのバックドア防御法なんだって。これで新しい攻撃にも強くなりそうね！

**Comment:** Accepted by 29th European Symposium on Research in Computer Security   (ESORICS 2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-08-28 07:31

- - -

### [Examining the Interplay Between Privacy and Fairness for Speech Processing: A Review and Perspective](http://arxiv.org/abs/2408.15391)

**音声処理におけるプライバシーと公平性の相互作用の検討: レビューと展望**

Anna Leschanowsky, Sneha Das

- 個人のプライバシーを保護しつつ、すべてのユーザーに対して信頼性を保つ必要がある
- 音声処理のモデル開発中に共存するバイアスやプライバシーの問題を検討
- プライバシー強化技術がバイアスを増やす可能性があり、それに対する対策がプライバシーを減じる可能性を指摘
- 音声技術におけるプライバシーと公平性のトレードオフの包括的評価を提唱

プライバシーと公平性って両立するのが難しいんだね。これからの音声技術の進化が楽しみ！



**トピック:** [PETs](pets), **カテゴリ:** eess.AS, cs.SD, **投稿日時:** 2024-08-27 20:32
