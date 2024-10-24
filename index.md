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

更新: 2024-10-24T04:22:29.681581

- - -

### [ProFL: Performative Robust Optimal Federated Learning](http://arxiv.org/abs/2410.18075)

**ProFL: パフォーマティブなロバスト最適連合学習**

Xue Zheng, Tian Xie, Xuwei Tan, Aylin Yener, Xueru Zhang, Ali Payani, Myungjin Lee

- パフォーマティブ予測は、モデルの配備による学習中のデータ分布の変化を捉える枠組み
- 連合学習におけるモデル誘発型の分布シフトの影響はまだ未解明
- 提案手法ProFLは、ノイズがあり汚染されたデータから最適点を見つける
- 非凸目的関数下での収束解析と広範な実験により効率性を実証

これすごく必要そう！どんなに複雑でノイズだらけのデータでも、最適な解を見つけるなんて魔法みたい。未来のAIがもっと賢くなるために、こういう技術がどんどん進化していくといいな。それに、どんなシフトがあっても対応できるって頼もしいよね。

**Comment:** 27 pages with Appendix, 18 figures. The paper has been submitted and   is currently under review

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.IT, math.IT, **投稿日時:** 2024-10-23 17:57

- - -

### [Federated Transformer: Multi-Party Vertical Federated Learning on Practical Fuzzily Linked Data](http://arxiv.org/abs/2410.17986)

**連合トランスフォーマー: 実用的に曖昧にリンクされたデータにおけるマルチパーティ縦連合学習**

Zhaomin Wu, Junyi Hou, Yiqun Diao, Bingsheng He

- 縦連合学習は異なる組織が異なる特徴を提供し協力してモデルを訓練する方式
- プラグマティックマルチパーティフジー VFL では性能低下とプライバシー維持費用が課題
- 新たにフェデレーテッドトランスフォーマー（FeT）を開発し、改良技術で性能向上を図る
- 作成したプライバシーフレームワークで、差分プライバシーと秘密計算を融合し、性能とプライバシーを向上

多くの組織で協力しながらプライバシーも守れるってすごいよね！FeTがどんなふうに幅広く活用されていくのか、とっても楽しみ♪



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-10-23 16:00

- - -

### [Together We Can: Multilingual Automatic Post-Editing for Low-Resource Languages](http://arxiv.org/abs/2410.17973)

**一緒にできる：低資源言語のための多言語自動後編集**

Sourabh Deoghare, Diptesh Kanojia, Pushpak Bhattacharyya

- 多言語自動後編集（APE）システムが低資源のインド・アーリア語系言語の翻訳品質向上に役立つかを探る
- 英語-マラーティー語、英語-ヒンディー語の類似性を活用し、多言語APEモデルを開発
- ヒンディー語-マラーティー語とその逆の合成データを生成し、品質推定（QE）との多タスク学習を組み合わせる
- 多言語APEモデルは各単言語ペアモデルを上回り、多タスク学習やドメイン適応で更なる改善が見られる

異なる言語間の翻訳の質を向上させるなんて、多言語の壁を破ってく感じね！さらに、公開データでみんなが試せるのもめっちゃ素敵だよね。どんな応用が出てくるか楽しみ～！

**Comment:** Accepted at Findings of EMNLP 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-10-23 15:37

- - -

### [Multi-Continental Healthcare Modelling Using Blockchain-Enabled Federated Learning](http://arxiv.org/abs/2410.17933)

**ブロックチェーン対応連合学習を用いた多大陸健康モデル**

Rui Sun, Zhipeng Wang, Hengrui Zhang, Ming Jiang, Yizhe Wen, Jiqun Zhang, Jiahao Sun, Shuoying Zhang, Erwu Liu, Kezhi Li

- 医療データの共有は難しく、従来のモデル構築が非常に困難
- 提案フレームワークは多大陸のデータを使い、データを共有せずにモデル構築
- ブロックチェーン対応連合学習により、データのプライバシーと安全性を確保
- 提案手法は精度も高く、国際的な医療プロジェクト連携を支援

これって、データを共有しないでこんなにいい結果が出るってすごくない？世界中のデータを使って、もっとかっこいいことができそうだよね。まさに未来の医療って感じ！

**Comment:** Accepted by IEEE Global Blockchain Conference

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-10-23 14:55

- - -

### [ELAICHI: Enhancing Low-resource TTS by Addressing Infrequent and Low-frequency Character Bigrams](http://arxiv.org/abs/2410.17901)

**ELAICHI: 低リソースTTSを稀少かつ低頻度な文字ビグラムの課題に取り組むことで強化**

Srija Anand, Praveen Srinivasa Varadhan, Mehak Singal, Mitesh M. Khapra

- 英語以外では大規模かつ高品質なデータ不足がTTSの知覚性を低下させる
- 言語や地理的に関連する高品質データを利用し対象言語のTTSを改善
- 非スタジオ環境でのASRデータを雑音除去や音声強化で改善し利用
- 大規模モデルからの知識蒸留と合成データを用いた出力の強化

この研究は、特に低リソース言語においてTTSの質を向上させる方法を提供するね！データ不足でも他言語と資源を共有することで新しいアプローチができそう。そんな未来を想像するとワクワクしちゃうね。

**Comment:** 11 pages, 1 figure, 3 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, eess.AS, **投稿日時:** 2024-10-23 14:18

- - -

### [Enhancing Federated Learning Convergence with Dynamic Data Queue and Data Entropy-driven Participant Selection](http://arxiv.org/abs/2410.17792)

**動的データキューとデータエントロピー駆動の参加者選択による連合学習の収束性向上**

Charuka Herath, Xiaolan Liu, Sangarapillai Lambotharan, Yogachandran Rahulamathavan

- 連合学習は非中央集権的でプライバシー保護や規制遵守に優れたモデル訓練方法
- デバイス間でデータが不均一に分布する場合の統計複雑性に焦点を当てる
- 動的データキューを用いてデバイスにデータを配布し収束性を改善する方法を提案
- 提案手法はSOTAアルゴリズムより高精度で、MNISTやCIFARデータセットで最大20%の精度向上を実現

へー！連合学習ってそんなにデータの分布がばらつくと難しいんだね。でもこの方法なら、ちゃんと収束しやすくなって精度もアップしちゃうなんてスゴイじゃん！みんなもこうやって連携してどんどん良くなるっていいねー！

**Comment:** The Journal is submitted to IEEE Transactions in the Internet of   Things

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, 14J60 (Primary), I.2.11; I.5.1; I.5.4, **投稿日時:** 2024-10-23 11:47

- - -

### [Beware of Calibration Data for Pruning Large Language Models](http://arxiv.org/abs/2410.17711)

**大規模言語モデルのプルーニングにおけるキャリブレーションデータへの警鐘**

Yixin Ji, Yang Xiang, Juntao Li, Qingrong Xia, Ping Li, Xinyu Duan, Zhefeng Wang, Min Zhang

- 大規模言語モデルの圧縮には、コスト削減と推論効率向上が重要な要素である
- キャリブレーションデータが高度なプルーニング戦略よりも性能に影響を与えることがある
- トレーニングデータに類似したキャリブレーションデータは、より良い結果をもたらす
- 自己生成キャリブレーションデータ合成戦略が、強力なプルーニング手法を強化

キャリブレーションデータがプルーニング性能にこんなに影響するなんて面白いね！合成データの戦略も活用していけば、これからの言語モデルの効率化がもっと進むかもって思うよ。

**Comment:** under review

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-10-23 09:36

- - -

### [Towards Active Participant-Centric Vertical Federated Learning: Some Representations May Be All You Need](http://arxiv.org/abs/2410.17648)

**能動的参加者中心の垂直連合学習に向けて: 一部の表現が全ての鍵かもしれない**

Jon Irureta, Jon Imaz, Aizea Lojo, Marco González, Iñigo Perona

- 垂直連合学習は異なる参加者間での共同モデル学習を可能にするが、高通信コストなどで課題がある
- 新しい方法「能動的参加者中心の垂直連合学習（APC-VFL）」を提案し、参加者間の通信を1ラウンドに削減した
- 無監督表現学習と知識蒸留を組み合わせ、古典的な方法と同等の精度を実現し通信ラウンドを最大4200倍削減
- 提案手法は非連合的なローカルモデルや他の連合学習提案とも比較し効率的かつ柔軟であることを示した

参加者同士の通信ラウンドが1回で済むの、めっちゃ効率的じゃない！？しかも精度を維持しつつ柔軟性があるなんて、今後の連合学習のプラットフォームのありかたがガラリと変わっちゃうかも！🌟



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-10-23 08:07

- - -

### [Towards Effective Data-Free Knowledge Distillation via Diverse Diffusion Augmentation](http://arxiv.org/abs/2410.17606)

**効果的なデータフリー知識蒸留のための多様な拡散拡張技術に向けて**

Muquan Li, Dongyang Zhang, Tao He, Xiurui Xie, Yuan-Fang Li, Ke Qin

- データフリー知識蒸留はモデル圧縮において重要であるが、合成データの多様性不足と分布不一致が課題。
- 本研究は多様な拡散拡張技術（DDA）を提案し、自己監督型の拡張を用いてデータサンプルの多様性を確保。
- コサイン類似性に基づく画像フィルタリングで埋め込み空間の過剰な逸脱を抑え、知識蒸留の忠実度を維持。
- CIFAR-10、CIFAR-100、Tiny-ImageNetでの実験で、提案手法が最新技術を上回る性能を示す。

データなしで知識を移せるなんてすごくエコな技術だね！合成データの多様性不足って難しそうな問題を、新しい拡散技術でうまく解決しててワクワクする。ぜひ試してみたいなぁ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, **投稿日時:** 2024-10-23 07:01

- - -

### [Securing Federated Learning Against Novel and Classic Backdoor Threats During Foundation Model Integration](http://arxiv.org/abs/2410.17573)

**基盤モデル統合中の新しいおよび古典的なバックドア脅威に対抗する連合学習のセキュリティ確保**

Xiaohuan Bi, Xi Li

- 基盤モデルを連合学習に統合することで、新たなバックドア攻撃のメカニズムが生じている。
- 攻撃者は、合成データを利用してバックドアを埋め込むことで、クライアントモデルを感染させる。
- 提案された防御策はデータなしで隠れた特徴空間の異常活動を制約し、モデル性能への影響を最小限に抑える。
- 提案手法は、新旧のバックドア攻撃に対して効果的で、既存の防御よりも優れることを実証。

連合学習と基盤モデルの統合で、新たな問題も生まれちゃったんだね。でも、この論文はその対策をうまく考えてるみたい！未来のプライバシー技術がもっと進化しそう🌟



**トピック:** [連合学習](fl), [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-10-23 05:54

- - -

### [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](http://arxiv.org/abs/2410.17566)

**差分プライバシー学習にはより良いモデル初期化と自己蒸留が必要**

Ivoline C. Ngong, Joseph P. Near, Niloofar Mireshghallah

- 差分プライバシーSGDはプライバシーを守りつつ言語モデルを訓練するが、効用や多様性が低下
- DPRefineという3フェーズ法を提案し、小さな事前学習LMでのデータ合成でモデルを初期化
- DPRefineは、従来の手法より生成テキストの言語エラーを84.0%削減することを示した
- 小型モデルのGPT-2でも有効で、プライバシー保護言語モデルの効率的展開に寄与する可能性

DPRefineが差分プライバシーの問題を解決するなんて面白そう！小さなモデルをうまく活用するのって、エコで未来を感じるよね。プライバシーを守りながらの精度向上、期待しちゃうな！

**Comment:** 18 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, cs.CL, cs.CR, **投稿日時:** 2024-10-23 05:19

- - -

### [Which Client is Reliable?: A Reliable and Personalized Prompt-based Federated Learning for Medical Image Question Answering](http://arxiv.org/abs/2410.17484)

**どのクライアントが信頼できるか？：医療画像質問応答のための信頼性の高いパーソナライズされたプロンプトベースの連合学習**

He Zhu, Ren Togo, Takahiro Ogawa, Miki Haseyama

- 通常の医療AIモデルは、プライバシーの敏感な特徴を扱えず倫理的問題を引き起こす
- パーソナライズされた連合学習(pFL)で医療分野のプライバシー信頼性を改善
- transformerに学習可能なプロンプトを加え、多様な医療データ上で効率的なトレーニングを実現
- デンプスター・シェーファーの証拠理論を用いて予測の不確実性を定量化、モデルの信頼性を向上

医療画像を扱う連合学習で信頼性を重点的に改善するってすごいね！プライバシーを守りながらより正確な医療AIモデルが生まれると、より多くの分野で役立つかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, cs.CL, cs.LG, **投稿日時:** 2024-10-23 00:31

- - -

### [Formal Privacy Guarantees with Invariant Statistics](http://arxiv.org/abs/2410.17468)

**不変統計量を用いた正式なプライバシー保証**

Young Hyun Cho, Jordan Awan

- 差分プライバシーを拡張し、不変量と称される非プライベート統計と差分プライバシー出力の同時リリースを考慮
- 隣接データセット間の識別不可能性を保ちながら、不変量を満たすデータセットにおいて隣接性を再定義するSemi-DPフレームワークを提案
- ガウス機構やランク劣化感度空間の最適$K$-ノルム機構などを含むカスタマイズされた機構を開発
- Semi-DPを用いた2020年米国国勢調査のプライバシー分析で、実際のプライバシー保証が宣伝されているよりも弱いことを明らかに

新しい考え方のSemi-DPってなんだか面白そう！2020年の国勢調査でもプライバシーがもっと守られる可能性があるというのは嬉しいね。セキュリティとか個人情報保護の分野でどんどんこんな技術が浸透していってほしいな〜。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, stat.AP, **投稿日時:** 2024-10-22 22:50

- - -

### [Data Obfuscation through Latent Space Projection (LSP) for Privacy-Preserving AI Governance: Case Studies in Medical Diagnosis and Finance Fraud Detection](http://arxiv.org/abs/2410.17459)

**プライバシー保護AIガバナンスのための潜在空間投影によるデータ難読化：医療診断と金融詐欺検出のケーススタディ**

Mahesh Vaijainthymala Krishnamoorthy

- LSPは機械学習を使ってデータを潜在空間に投影し、データの本質を保ちながら効果的に難読化する技術
- 差分プライバシーや準同型暗号などの従来技術とは異なり、抽象化された低次元形式でデータ処理を実現
- 自動エンコーダーと敵対的訓練を用いてプライバシーとデータ有用性のトレードオフを精密に制御
- LSPは既存のプライバシー方法を上回る性能を示し、AIガバナンスの枠組みとの整合性も強調

新しいプライバシー技術が、医療や金融の分野でめちゃ役立ちそうな予感！それがAIガバナンスにもフィットしてるの、本当に未来感あるよね。これからのAIシステム、ますます楽しみになっちゃう！

**Comment:** 19 pages, 6 figures, submitted to Conference ICADCML2025

**トピック:** [連合学習](fl), [差分プライバシー](dp), [準同型暗号](he), **カテゴリ:** cs.LG, cs.AI, cs.CR, cs.CY, F.2.1; E.3, **投稿日時:** 2024-10-22 22:31

- - -

### [Meta Stackelberg Game: Robust Federated Learning against Adaptive and Mixed Poisoning Attacks](http://arxiv.org/abs/2410.17431)

**メタ・スタッケルベルクゲーム: 適応的および混合的なポイズニング攻撃に対する頑強な連合学習**

Tao Li, Henger Li, Yunian Pan, Tianyi Xu, Zizhan Zheng, Quanyan Zhu

- 連合学習は多様なセキュリティ脅威に脆弱
- 提案手法は、ベイズ・スタッケルベルク・マルコフゲームとして敵対的連合学習を定式化
- 強力な攻撃行動をシミュレートし、適応的攻撃に対抗するメタRLベースの防御を設計
- 理論的に提案手法は決まった点に集まり、多様な攻撃に対して優れた性能を示す

この論文、ポイズニング攻撃への対策としてすごく革新的！ゲーム理論を使って強力な防御ができるとか、実際に試してみたくなるよね。きっとサイバーセキュリティの世界がもっとクールになるはず！

**Comment:** This work has been submitted to the IEEE for possible publication

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.GT, **投稿日時:** 2024-10-22 21:08
