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

更新: 2024-07-23T04:20:38.606280

- - -

### [A Life-long Learning Intrusion Detection System for 6G-Enabled IoV](http://arxiv.org/abs/2407.15700)

**6G対応IoVのための生涯学習型侵入検知システム**

Abdelaziz Amara korba, Souad Sebaa, Malik Mabrouki, Yacine Ghamri-Doudane, Karima Benatchba

- 6G技術は超高速データレートとシームレスなネットワークカバレッジを持つが、IoVに新たなサイバー脅威をもたらす
- 既存システムでは急速に進化する脅威に動的に適応し学ぶ能力が不足している
- クラスインクリメンタル学習と連合学習を組み合わせた新しい侵入検知システムを提案している
- 包括的な実験結果では、新たなサイバー攻撃パターンの学習で高い適応力、精度、低い誤検知率を示した

この論文、6GのIoVの未来が見える感じがしてすごくエキサイティング！連合学習とクラスインクリメンタル学習の組み合わせがすごいんじゃない？



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-07-22 15:07

- - -

### [TreeSBA: Tree-Transformer for Self-Supervised Sequential Brick Assembly](http://arxiv.org/abs/2407.15648)

**TreeSBA: セルフスーパーヴァイズド連続ブリック組立のためのツリートランスフォーマー**

Mengqi Guo, Chen Li, Yuyang Zhao, Gim Hee Lee

- 幅優先探索（BFS）を用いたLEGO-Tree構造により、連続組立行動を効率的にモデリング
- 入力されたマルチビュー画像から連続組立行動を予測するクラス非依存のツリートランスフォーマーフレームワークを設計
- 合成データからの転移学習を活用し、実データの行動ラベルの必要性を回避
- 実データにおいてアノテーションなしで、既存方法を3D監督データセットで最大11.3%上回る性能を達成

幅優先探索とか転移学習とか難しそうな単語がいっぱいだけど、要はLEGOの組立手順をもっと賢く予測できるってことだね。自分で学習してくれたら、遊ぶのがもっと楽しくなるかも！

**Comment:** ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-22 14:05

- - -

### [A New Theoretical Perspective on Data Heterogeneity in Federated Optimization](http://arxiv.org/abs/2407.15567)

**連合最適化におけるデータ不均一性に関する新しい理論的視点**

Jiayi Wang, Shiqiang Wang, Rong-Rong Chen, Mingyue Ji

- データ不均一性が連合学習の収束率に悪影響を与える
- 提案された新しい仮定は、従来の仮定よりも弱く、実用化が期待できる
- 提案手法で収束上限が大幅に削減されることを示した
- 実験で理論的発見が実証され、具体的な改善が確認された

新しい視点からデータ不均一性にアプローチし、実際のパフォーマンス向上につなげる研究って面白そう！もっと効率的な連合学習が可能になるかもね。

**Comment:** ICML 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.IT, math.IT, math.OC, **投稿日時:** 2024-07-22 11:52

- - -

### [Synthetic Image Learning: Preserving Performance and Preventing Membership Inference Attacks](http://arxiv.org/abs/2407.15526)

**合成画像の学習: 性能保持とメンバーシップ推論攻撃の防止**

Eugenio Lomurno, Matteo Matteucci

- 生成型人工知能がデータの希少性やプライバシー問題を解決
- 知識リサイクル（KR）パイプラインが合成データ生成と分類器訓練を最適化
- 生成知識蒸留（GKD）により高品質な合成データセットの再生成とソフトラベリングを実現
- 実データとの性能ギャップを大幅に減少させ、メンバーシップ推論攻撃に対する免疫力を示す

知識リサイクルとか生成知識蒸留とか、すごい未来感あるよね！合成データで実データより良い結果とか、もう何が本物か分からなくなりそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.CR, cs.LG, **投稿日時:** 2024-07-22 10:31

- - -

### [The Diversity Bonus: Learning from Dissimilar Distributed Clients in Personalized Federated Learning](http://arxiv.org/abs/2407.15464)

**多様性ボーナス：個別連合学習における異なる分散クライアントから学ぶ**

Xinghao Wu, Xuefeng Liu, Jianwei Niu, Guogang Zhu, Shaojie Tang, Xiaotian Li, Jiannong Cao

- 個別連合学習（PFL）はクライアントが個別モデルを共同学習するためのフレームワーク
- これまでの研究は、類似データのクライアント間での利益を前提とした手法を開発
- DiversiFedは異なるデータ分布のクライアントからも利益を得るための新手法を提案
- 実験結果は、DiversiFedが類似データのクライアントを超えて学習効果を向上させることを示した

多様なクライアントと協力することで予想外の学びがあるなんて面白いね！これから連合学習がより広がっていきそうだね〜

**Comment:** 14 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-07-22 08:24

- - -

### [Resource-Efficient Federated Multimodal Learning via Layer-wise and Progressive Training](http://arxiv.org/abs/2407.15426)

**層ごとの段階的訓練による資源効率的な連合マルチモーダル学習**

Ye Lin Tun, Chu Myaet Thwal, Minh N. H. Nguyen, Choong Seon Hong

- マルチモーダル学習はデータ形式の違いを統合し、複雑なタスクに対応するために重要である
- 従来の連合学習は、マルチモーダルデータに対応するためにリソースが多く必要となる
- LW-FedMMLは層ごとの分割訓練を提案し、メモリと計算リソース、通信コストを大幅に削減
- Prog-FedMMLはリソース効率は劣るが、性能向上の可能性があり、資源制約の少ないシナリオで有用

計算リソースが少ない中でも、大規模なのにちゃんとプライバシーも守れるなんてスゴい！実際のアプリケーションにどう導入されていくのか、未来が楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-22 07:06

- - -

### [Weights Shuffling for Improving DPSGD in Transformer-based Models](http://arxiv.org/abs/2407.15414)

**TransformerベースのモデルにおけるDPSGD改善のための重みシャッフリング**

Jungang Yang, Zhe Ji, Liyao Xiang

- DPメカニズムは高次元設定でプライバシー維持とデータ有用性のバランスが困難
- 提案されたシャッフリングメカニズムがDPSGDの有用性を向上
- 順列不変性によりモデル精度に影響を与えず、追加ランダム性を提供
- シャッフリングがDPSGDのプライバシー保証を理論的に強化するが、正確な追跡は難しい

この研究、めっちゃ面白そう！新しいシャッフリングで精度上がるとか期待できそうだね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-07-22 06:41

- - -

### [Tackling Selfish Clients in Federated Learning](http://arxiv.org/abs/2407.15402)

**連合学習における利己的なクライアントへの対処方法**

Andrea Augello, Ashish Gupta, Giuseppe Lo Re, Sajal K. Das

- 連合学習は、参加者が自分のデータを公開せずに共同でモデルを訓練する分散型機械学習パラダイム
- 利己的なクライアントが意図的にトレーニングプロセスを改ざんし、グローバルモデルを自分のローカルモデルに偏らせる問題を提起
- 提案する新しいロバストな集約戦略（RFL-Self）は、受信した更新情報から真の更新を推定し、自己中心性の影響を緩和
- MNISTとCIFAR-10データセットでの実験結果により、2%の利己的なクライアントが精度を最大36%減少させるが、RFL-Selfはその効果を緩和することができる

利己的なクライアントまで考慮する技術とかすごく未来っぽい！この辺詳細に勉強したら、自分の研究にも役立つかもね。

**Comment:** 10 pages, 16 figures. European Conference on Artificial Intelligence   (ECAI) 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-07-22 06:08

- - -

### [Poisoning with A Pill: Circumventing Detection in Federated Learning](http://arxiv.org/abs/2407.15389)

**ピルを用いた毒物混入：連合学習における検出回避**

Hanxi Guo, Hao Wang, Tao Song, Tianhang Zheng, Yang Hua, Haibing Guan, Xiangyu Zhang

- 連合学習はデータプライバシー保護に強みがあるが分散的で反復的な性質から攻撃に脆い
- 既存の防御策はモデル更新パラメータを均一に操作する攻撃を検出するがより精巧な攻撃には弱い
- 提案するアプローチは既存の攻撃を強化し、検出を回避する「ピル」構造で毒を混入
- 実験結果では、提案手法が全ての一般的な防御策を回避し、エラーレートが最大7倍上昇

連合学習を改善するための新しい防御策を考えないといけないってことでドキドキするね。精巧な攻撃にどう対抗するか、もっと研究が進むと面白そう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-07-22 05:34

- - -

### [Weak-to-Strong Compositional Learning from Generative Models for Language-based Object Detection](http://arxiv.org/abs/2407.15296)

**生成モデルを用いた言語ベースの物体検知における弱から強への構成学習**

Kwanyong Park, Kuniaki Saito, Donghyun Kim

- VLモデルは複雑な視覚オブジェクトの理解が限定的である
- 従来のアプローチはハードネガティブな合成テキストを使用するが効果は限定的
- 提案手法は構造化された合成データ生成で構成理解を強化
- 合成トリプレットを使用したWSCLによりVLモデルの性能が大幅に向上

視覚と言語のモデルがさらに賢くなるなんてワクワクだね！これからの物体認識の未来がもっと楽しみになっちゃうね😊

**Comment:** ECCV 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CL, cs.LG, **投稿日時:** 2024-07-21 23:43

- - -

### [A Learning-Based Attack Framework to Break SOTA Poisoning Defenses in Federated Learning](http://arxiv.org/abs/2407.15267)

**連合学習における最先端のデータ汚染防御を破る学習ベースの攻撃フレームワーク**

Yuxin Yang, Qiang Li, Chenfei Nie, Yuan Hong, Meng Pang, Binghui Wang

- 連合学習はデータプライバシーを保護するが、データ汚染攻撃に脆弱である
- 多くの防御策は堅牢なアグリゲーターで対策してきたが、全て破られている
- 新しい堅牢なアグリゲーターも設計されるが、特定の攻撃手法により依然脆弱である
- 最適化ベースの攻撃フレームワークを提案し、有効性を複数のデータセットで検証

次々と新しい防御策が登場しても、また新たな攻撃がそれを破ってくるなんて、本当にイタチごっこだよね。でも、それが技術の進歩を促すんだと思うとワクワクするね！

**Comment:** This is an extended version of our CIKM 2024 paper

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-21 21:02

- - -

### [PUFFLE: Balancing Privacy, Utility, and Fairness in Federated Learning](http://arxiv.org/abs/2407.15224)

**PUFFLE: 連合学習におけるプライバシー、ユーティリティ、および公平性のバランス**

Luca Corbucci, Mikko A Heikkila, David Solans Noguero, Anna Monreale, Nicolas Kourtellis

- 公平性、プライバシー、ユーティリティの同時達成は困難であり、しばしば十分に探求されていない
- 多くの取り組みは三要素のうち二つに注力し、残り一つを無視している
- PUFFLEは、連合学習におけるこれら三要素のバランスを探索するための高次パラメータ化アプローチを提案
- データセット、モデル、データ分布の多様性に対応しつつモデル不公平性を最大75%削減し、プライバシーを維持しながら最悪の場合でもユーティリティは最大17%減少に留める

公平性とプライバシーって大事だもんね！みんなが安心して使える技術にするため、PUFFLEのアプローチには期待しちゃう。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CR, cs.CY, **投稿日時:** 2024-07-21 17:22

- - -

### [Privacy-Preserving Multi-Center Differential Protein Abundance Analysis with FedProt](http://arxiv.org/abs/2407.15220)

**プライバシー保護型多施設差分タンパク質量解析のためのFedProt**

Yuliya Burankova, Miriam Abele, Mohammad Bakhtiari, Christine von Törne, Teresa Barth, Lisa Schweizer, Pieter Giesbertz, Johannes R. Schmidt, Stefan Kalkhof, Janina Müller-Deile, Peter A van Veelen, Yassene Mohammed, Elke Hammer, Lis Arend, Klaudia Adamowicz, Tanja Laske, Anne Hartebrodt, Tobias Frisch, Chen Meng, Julian Matschinske, Julian Späth, Richard Röttger, Veit Schwämmle, Stefanie M. Hauck, Stefan Lichtenthaler, Axel Imhof, Matthias Mann, Christina Ludwig, Bernhard Kuster, Jan Baumbach, Olga Zolotareva

- 質量分析によるタンパク質の定量解析がプロテオミクスを革新
- 複数施設からのデータ共有で統計的有意性が向上するが、プライバシーの問題が発生
- FedProtは、連合学習と加法秘密分散を利用して分散データの差分タンパク質量解析をプライバシー保護の下で実現
- FedProtの結果は、既存の手法と同等の精度を達成し、最も正確なメタ解析手法より優れていることが確認された

これはかなりの革新ね！複数の施設が協力できると、もっとデータが有効活用できそうだね！🌸

**Comment:** 52 pages, 16 figures, 12 tables. Last two authors listed are joint   last authors

**トピック:** [連合学習](fl), **カテゴリ:** q-bio.QM, cs.LG, **投稿日時:** 2024-07-21 17:09

- - -

### [AGORA: Open More and Trust Less in Binary Verification Service](http://arxiv.org/abs/2407.15062)

**AGORA: バイナリ検証サービスにおける「オープンでより少なく信頼する」アプローチ**

Hongbo Chen, Quan Zhou, Sen Yang, Xing Han, Fan Zhang, Danfeng Zhang, Xiaofeng Wang

- バイナリ検証の重要性と、それを開放的かつ信頼性高くする難題の解消を目指す
- AGORAは、信頼できないエンティティにタスクを委任し、対応する検証者をTCB内に保持
- ブロックチェーンを用いた報奨タスク管理で、定理証明者への信頼を排除する
- ソフトウェアベースのフォルトアイソレーションやサイドチャネル緩和の有効性を実証

安全性のためにブロックチェーンを使うとか、めっちゃ最先端って感じ！みんなで協力できる仕組み、すごい未来的だね。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-21 05:29

- - -

### [Non-Reference Quality Assessment for Medical Imaging: Application to Synthetic Brain MRIs](http://arxiv.org/abs/2407.14994)

**医療画像の非参照品質評価：合成脳MRIへの応用**

Karl Van Eeden Risager, Torkan Gholamalizadeh, Mostafa Mehdipour Ghazi

- 高品質な合成データは、ドメイン適応、データ不足、プライバシー問題の解決に重要
- 既存の画像品質指標は参照画像を必要とし、2D自然画像に最適化されているため医療画像には不向き
- 3D ResNetを訓練して脳MRI品質を非参照で評価、新しいディープラーニング手法を提案
- 実験結果により、複数の視点から画像品質を正確に反映し、最先端の指標と比較して優れた性能を示す

画像の評価が参照画像なしに行えるなんて、すごく役に立ちそう！高品質な合成画像の生成も、医療分野でのデータ問題を解決する未来が楽しみだね。

**Comment:** MICCAI 2024 workshop on Deep Generative Models

**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-07-20 22:05

- - -

### [Addressing Data Heterogeneity in Federated Learning of Cox Proportional Hazards Models](http://arxiv.org/abs/2407.14960)

**連合学習におけるCox比例ハザードモデルのデータ異質性の解決**

Navid Seidi, Satyaki Roy, Sajal K. Das, Ardhendu Tripathy

- 病院間や医療専門家間の疾患プロファイルと治療法の多様性が、患者中心のパーソナライズ戦略の必要性を強調
- 疾患進行の類似性を活かして生存分析の予測モデルを向上させるため、連合学習の枠組みが有効
- Cox比例ハザードモデルにおいてデータの異質性を緩和し、モデル性能を向上させるアプローチを提案
- 特徴ベースのクラスタリングとイベントベースの報告戦略を用いて、モデル精度や適応力を向上させる

連合学習を使って病院のデータをまとめて活用するなんてすごいかも！これで患者さんの予測ももっと正確になるといいね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, stat.AP, stat.ML, **投稿日時:** 2024-07-20 18:34

- - -

### [FedPartWhole: Federated domain generalization via consistent part-whole hierarchies](http://arxiv.org/abs/2407.14792)

**FedPartWhole: 一貫したパート・ホール階層による連合ドメイン一般化**

Ahmed Radwan, Mohamed S. Shehata

- 連合ドメイン一般化は未見のドメインへの一般化とデータプライバシー制約の両立の課題に取り組む
- 提案するアーキテクチャは、背骨モデル構造から問題にアプローチし、パートとホールの階層構造を強調
- 画像解析ツリーの特徴表現を明確に取り入れ、モデル一般化に成功した初の研究
- 比較可能なサイズのCNNより12%以上の性能向上を実現し、インタープリタブルである点が信頼性を高める

独自のバックボーンアプローチで、CNNを超える性能向上だって！とても使いやすそうな技術だから、将来の技術標準になるかもね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-20 07:43

- - -

### [Universal Medical Imaging Model for Domain Generalization with Data Privacy](http://arxiv.org/abs/2407.14719)

**データプライバシーを考慮したドメイン一般化のための普遍的な医療画像モデル**

Ahmed Radwan, Islam Osman, Mohamed S. Shehata

- 医療画像分野におけるドメイン一般化は、公開されているラベル付きデータセットの制約により難しい
- フェデレーテッドラーニングを用い、ローカルデータセットへの直接アクセスを排除しつつ、複数のローカルモデルから知識をグローバルモデルに移行
- グローバルモデルは多様な医療画像タスクを実行可能であり、トレーニングに使用されたプライベートデータセットの機密性も保持
- 8つの異なる医療画像アプリケーションに対して広範な実験を行い、幾つか異なるドメインからのデータ分布の中でマスクされた画像モデリング技術に基づく最新のベースラインを上回る改善を実証

データプライバシーを守りながら、いろんな医療分野で使えるモデルを作るなんて面白そう！今後の医療の進化に大いに役立ちそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.CV, **投稿日時:** 2024-07-20 01:24

- - -

### [Differential Privacy of Cross-Attention with Provable Guarantee](http://arxiv.org/abs/2407.14717)

**実証可能な保証を伴うクロスアテンションの差分プライバシー**

Jiuxiang Gu, Yingyu Liang, Zhenmei Shi, Zhao Song, Yufa Zhou

- クロスアテンションは重要なAIアプリケーションで基本モジュールとなっている
- 差分プライバシー（DP）データ構造を設計し、クロスアテンションのプライバシーを理論的に保証
- 計算時間やメモリ消費を一定のパラメータによって評価し、効率的なデータ構造を提案
- 結果は適応型クエリに対しても堅牢で、意図的な攻撃に対する耐性を持つ

この研究でクロスアテンションにおけるプライバシー問題が解決できるなんて、AIの応用範囲も更に広がりそうだね。秘密が守られたまま賢くなっていくAI、楽しみ！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, **投稿日時:** 2024-07-20 01:02

- - -

### [Universally Harmonizing Differential Privacy Mechanisms for Federated Learning: Boosting Accuracy and Convergence](http://arxiv.org/abs/2407.14710)

**連合学習のための普遍的調和差分プライバシー手法: 精度と収束の向上**

Shuya Feng, Meisam Mohammady, Hanbin Hong, Shenao Yan, Ashish Kundu, Binghui Wang, Yuan Hong

- 差分プライバシーを用いた連合学習は、プライバシーを保証しつつモデルを共同で訓練する技術である
- 提案されたUDP-FLは、ガウスモーメント会計手法と任意のランダム化メカニズムを調和させる初の手法
- Rénysi差分プライバシーの概念を介してプライバシー予算を調和させ、モデルの精度と収束を向上
- UDP-FLは最新の手法と比較して、プライバシー保証とモデル性能の両面で優れたパフォーマンスを示す

これって連合学習の未来を変えちゃうかも！？他の手法より優れてるってところが特に気になるよね！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-07-20 00:11

- - -

### [The Collection of a Human Robot Collaboration Dataset for Cooperative Assembly in Glovebox Environments](http://arxiv.org/abs/2407.14649)

**手袋ボックス環境における協力組み立てのためのヒューマンロボット協働データセットの収集**

Shivansh Sharma, Mathew Huang, Sanat Nair, Alan Wen, Christina Petlowany, Juston Moore, Selma Wanna, Mitch Pryor

- Industry 5.0では人間がAI駆動の製造ソリューションの指導者とみなされている
- 既存のデータセットは合成データに依存しており、実際の操作にうまく適用できない
- 提案するHAGSデータセットは、1200の難しい事例を提供し、産業のヒューマンロボット協働シナリオに適している
- データセットと基準モデルは公開されており、手動と手袋のセグメンテーションのリアルタイム評価が可能

データセットが公開されてるから、すぐに試してみたくなるね！AIと人間の協力組み立て、未来の工場ってどんな感じなんだろう？



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-07-19 19:56

- - -

### [Differential Privacy with Multiple Selections](http://arxiv.org/abs/2407.14641)

**複数選択による差分プライバシー**

Ashish Goel, Zhihao Jiang, Aleksandra Korolova, Kamesh Munagala, Sahasrajit Sarmasarkar

- ユーザーがサーバーから勧告を受ける際に差分プライバシーを保持するための「複数選択」アーキテクチャを提案
- ユーザーが一次元の特性を持つ場合、最適なメカニズムが定義され、ラプラス分布が最適ノイズ分布であることを示す
- サーバーが返す結果のセットを決定するアルゴリズムも含め、最適なメカニズムを詳述
- $\mathfrak{h}(.)$ が恒等関数である場合、返される結果の数に反比例する誤差が生じることを実証

複数の推薦から選ぶって、選択肢があってうれしいよね！しかもノイズの扱いがラプラス分布が最適って、科学的なアプローチがかっこいいなぁ。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.DS, cs.CR, **投稿日時:** 2024-07-19 19:34
