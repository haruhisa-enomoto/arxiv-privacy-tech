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

更新: 2024-06-22T04:17:52.015936

- - -

### [Advancing Fine-Grained Classification by Structure and Subject Preserving Augmentation](http://arxiv.org/abs/2406.14551)

**構造と主題を保持する増補による細粒度分類の進展**

Eyal Michaeli, Ohad Fried

- 細粒度の視覚分類は、クラス間の微妙な違いと高いクラス内変異のために困難である
- FGVCデータセットは一般に小規模で収集が難しく、効果的なデータ増強が必要
- SaSPAは実際の画像をガイダンスに使用せず、生成の柔軟性と多様性を高める
- 実験結果から、SaSPAは従来の方法や最近の生成データ増強法を一貫して上回る

差分プライバシーが保たれた新しいデータ生成方法で、扱いづらいデータセットの分類精度が上がりそうでワクワクする！詳細を学ぶのが楽しみだね。

**Comment:** Under review. Code is available at   https://github.com/EyalMichaeli/SaSPA-Aug

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-20 17:58

- - -

### [Unmasking Database Vulnerabilities: Zero-Knowledge Schema Inference Attacks in Text-to-SQL Systems](http://arxiv.org/abs/2406.14545)

**データベースの脆弱性を暴露する：テキストからSQLへのシステムにおけるゼロ知識スキーマ推論攻撃**

Đorđe Klisura, Anthony Rios

- 関係データベースは現代の情報システムの基盤であり、効率的なデータの保存・クエリ・管理に寄与
- 大規模言語モデルの進展により、テキストからSQLへの技術が進化し、プライバシーとセキュリティの懸念が増大
- この研究ではテキストからSQLモデルを用いて、データベーススキーマをゼロ知識フレームワークで抽出
- 特別に作成された質問を使用し、高い精度でテーブル名を再構築、F1スコアはファインチューニングされたモデルで.75、生成モデルでは.96

ゼロ知識フレームワーク使ってこんなに高い精度でテーブル名を見つけるなんてすごい！これからのデータベースセキュリティがさらに大事になってくるね。



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-20 17:54

- - -

### [RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold](http://arxiv.org/abs/2406.14532)

**誤った合成データ上での強化学習がLLMの算数推論の効率を8倍に拡大**

Amrith Setlur, Saurabh Garg, Xinyang Geng, Naman Garg, Virginia Smith, Aviral Kumar

- モデル生成の合成データでのファインチューニングが効果的な場合とそうでない場合の違いを調査
- 合成データによるファインチューニングは性能向上に寄与するが、自己生成データでの再学習が効率を2倍に
- 誤った応答（ネガティブデータ）を活用することで、スプリアスな相関を解消し、トレーニング効率を向上
- 強化学習を活用し、ポジティブデータのみでは得られない安定した性能向上を実現

自己生成データを使って効率が2倍になるとかすごくない？強化学習のアプローチも取り入れてて、未来のAI教育がどんな風に変わるのかワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CL, **投稿日時:** 2024-06-20 17:45

- - -

### [A Benchmarking Study of Kolmogorov-Arnold Networks on Tabular Data](http://arxiv.org/abs/2406.14529)

**表形式データに対するコルモゴロフ・アーノルドネットワークのベンチマーク研究**

Eleonora Poeta, Flavio Giobergia, Eliana Pastor, Tania Cerquitelli, Elena Baralis

- KANsは機械学習の新星で、複雑な関数近似や合成データ処理に注目
- 実際の表形式データでKANsとMLPsを比較し、タスク性能と訓練時間を評価
- 得られた結果から、特に多数のインスタンスを持つデータセットでKANsが優れた精度とF1スコアを示す
- ただし、この性能向上は同等サイズのMLPsと比較して高い計算コストが伴う

KANsってすごく未来感あるけど、逆に実世界でのテストがまだ少ないみたい。その高い計算コストがネックだけど、改良されたら更に広まるかもね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-20 17:41

- - -

### [V-LASIK: Consistent Glasses-Removal from Videos Using Synthetic Data](http://arxiv.org/abs/2406.14510)

**V-LASIK: 合成データを用いた動画からの一貫したメガネ除去**

Rotem Shalev-Arkushin, Aharon Azulay, Tavi Halperin, Eitan Richardson, Amit H. Bermano, Ohad Fried

- 既存の方法は、過剰な編集や非現実的なアーティファクトを生成する問題がある
- 弱教師ありのアプローチを採用し、調整された事前学習拡散モデルで合成不完全データを生成
- 元の動画内容を保存しつつ、一貫した編集を実現するモデルを開発
- 他の局所的な動画編集タスクにも適用可能で、顔のステッカー除去にも成功を示す

合成データでこんなことできちゃうんだね！この技術もっと進化したら、映像編集がすごく簡単になりそう♡



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.GR, **投稿日時:** 2024-06-20 17:14

- - -

### [Explicit and Implicit Large Language Model Personas Generate Opinions but Fail to Replicate Deeper Perceptions and Biases](http://arxiv.org/abs/2406.14462)

**明示的および暗示的な大規模言語モデルパーソナが意見を生成するが、より深い認識とバイアスを再現することに失敗する**

Salvatore Giorgi, Tingting Liu, Ankit Aich, Kelsey Isman, Garrick Sherman, Zachary Fried, João Sedoc, Lyle H. Ungar, Brenda Curtis

- LLMsが人間中心の社会科学的タスクで使用される場面が増加
- これらのタスクは主観的であり、環境や信念などの人間因素に依存
- 明示的なプロンプトと暗示的なプロンプトの影響を比較
- LLMsは既知の人間のバイアスを再現するが、暗黙のバイアスを捉えることには失敗する

人間っぽい答えを生成するけど、やっぱり本当の人間の微妙な感情とかバイアスまでは理解できないんだね。でも、このギャップを埋める技術がこれからどう進化するか、すごく気になるな！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-06-20 16:24

- - -

### [CollaFuse: Collaborative Diffusion Models](http://arxiv.org/abs/2406.14429)

**CollaFuse: 協調型拡散モデル**

Simeon Allmendinger, Domenique Zipperling, Lukas Struppek, Niklas Kühl

- 拡散モデルは合成画像生成に有望だが、多くの課題がある
- 放任的学習がクライアントに大きな計算負担を課す問題あり
- 提案方法はクライアントの負担を軽減しつつ分散学習を実現
- CelebAデータセットでの実験で、高いプライバシー保護を証明

拡散モデルを活用する新しい協調学習のあり方なんだね。サーバー側に重い処理を任せることで、クライアントが楽になるのはすごく便利そう！未来のエッジコンピューティングも想像できてワクワクするね。

**Comment:** 13 pages, 7 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CV, **投稿日時:** 2024-06-20 15:54

- - -

### [Communication-efficient Vertical Federated Learning via Compressed Error Feedback](http://arxiv.org/abs/2406.14420)

**圧縮誤差フィードバックによる通信効率の高い垂直連合学習**

Pedro Valdeira, João Xavier, Cláudia Soares, Yuejie Chi

- 連合学習では通信負荷がボトルネックである
- 垂直連合学習では通信圧縮の理解が限られている
- エラーフィードバックによる圧縮誤差で収束速度を向上
- 数値実験により理論結果を確認、従来手法より大幅に改善

垂直連合学習のエラーフィードバックで通信がこんなに効率的になるなんて驚き！今後の研究も楽しみだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, cs.DS, math.OC, **投稿日時:** 2024-06-20 15:40

- - -

### [Communication-Efficient Byzantine-Resilient Federated Zero-Order Optimization](http://arxiv.org/abs/2406.14362)

**通信効率の良いビザンチン耐性を持つ連合ゼロ階最適化**

Afonso de Sá Delgado Neto, Maximilian Egger, Mayank Bakshi, Rawad Bitar

- CYBER-0は、メモリおよび通信効率の高い連合学習のための初のゼロ階最適化アルゴリズム
- MNISTデータセットとRoBERTa-Largeの微調整で、通信とメモリの効率で最新アルゴリズムを上回る
- 理論的に、凸損失関数に対する収束の保証を提供
- サイバー攻撃に耐性があり、高精度を維持

ゼロ階最適化って珍しいよね！これでセキュアな連合学習がもっと広がるといいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-20 14:36

- - -

### [Deblurring Neural Radiance Fields with Event-driven Bundle Adjustment](http://arxiv.org/abs/2406.14360)

**イベント駆動バンドル調整によるニューラルボクセル表現のデブラーリング**

Yunshan Qi, Lin Zhu, Yifan Zhao, Nan Bao, Jia Li

- NeRFは高品質なマルチビュー画像を用いて3D表現学習を行うが、モーションブラーにより再構築品質が低下する
- 既存のNeRFのデブラーリング手法は露光時間中の情報を正確にモデル化できず、困難がある
- バイオインスパイアされたイベントカメラを用いることで、高時間分解能で輝度変化を計測し情報不足を補う
- EBAD-NeRFはイベントデータとRGBデータを活用し、カメラポーズとNeRFパラメータを共同最適化する手法を提案

イベントカメラを使ってNeRFのモーションブラー問題を解決するなんて面白そう！未来の3Dモデル技術がもっと正確でリアルになる期待が高まるよね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-20 14:33

- - -

### [Mind the Privacy Unit! User-Level Differential Privacy for Language Model Fine-Tuning](http://arxiv.org/abs/2406.14322)

**プライバシーユニットを考慮せよ！言語モデルのファインチューニングにおけるユーザーレベル差分プライバシー**

Lynn Chua, Badih Ghazi, Yangsibo Huang, Pritish Kamath, Daogao Liu, Pasin Manurangsi, Amer Sinha, Chiyuan Zhang

- 大規模言語モデル（LLM）のファインチューニングにはプライバシーリスクがあり、特定のユーザーのデータを覚える可能性がある
- 現在のLLM評価は各テキストレコードをプライバシーユニットと見なしているが、これはユーザーごとのプライバシー保証が不均一になる
- 本研究では、ユーザーごとの貢献が均等でない場合に均一なプライバシー保護を確保するため、ユーザー単位の差分プライバシー（DP）を評価
- ユーザーレベルのDPを実現するために、Group Privacyとユーザー単位のDP-SGDの2つのメカニズムを検討し、データ選択戦略やパラメータ調整を探求

従来の方法じゃ個別のレコードばかりだと不安定だよね。でもユーザーレベルでプライバシーを均一に保護するって新しいし、みんなに公平で素敵かも。期待しちゃうね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CL, cs.CR, cs.LG, **投稿日時:** 2024-06-20 13:54

- - -

### [The Fire Thief Is Also the Keeper: Balancing Usability and Privacy in Prompts](http://arxiv.org/abs/2406.14318)

**火の盗人も守護者である：プロンプトにおける操作性とプライバシーのバランス**

Zhili Shen, Zihang Xi, Ying He, Wei Tong, Jingyu Hua, Sheng Zhong

- オンラインチャットボットの急速な普及により、AIが大きく進展したが、プロンプトに含まれる個人情報の漏洩が懸念
- 高い計算コストやシステムの大幅な改変が課題で、これまでの手法では適用が難しい
- 提案されたProSanは、プライバシーを保護しつつ操作性と人間の可読性を維持するフレームワーク
- 計算資源に柔軟対応し、モバイルデバイスでも個人情報を効果的に除去することが実証された

プライバシーを守りながらAIを活用するために欠かせない技術だね！モバイルでも使えるところが未来を感じさせるね～。



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AI, cs.CL, **投稿日時:** 2024-06-20 13:52

- - -

### [FairX: A comprehensive benchmarking tool for model analysis using fairness, utility, and explainability](http://arxiv.org/abs/2406.14281)

**FairX: 公平性、実用性、説明可能性を活用したモデル分析の総合的評価ツール**

Md Fahim Sikder, Resmi Ramachandranpillai, Daniel de Leng, Fredrik Heintz

- FairXは、モデルの公平性、実用性、説明可能性を統合的に評価するオープンソースのPythonベースツール
- 公平な生成モデルから生成された合成データの評価も可能で、既存の評価ツールではサポートされていない
- 公平な生成モデルをライブラリに追加、合成データの品質評価のための新しい評価指標も提供
- タブレットと画像データセットの両方をサポートし、カスタムデータセットの提供も可能

公平性と実用性、説明可能性を一つのツールで評価できるのはすっごく便利！カスタムデータセットも使えるから、色々試してみたくなるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-20 13:07

- - -

### [NAC-QFL: Noise Aware Clustered Quantum Federated Learning](http://arxiv.org/abs/2406.14236)

**ノイズ対応クラスタ化量子連合学習 (NAC-QFL)**

Himanshu Sahu, Hari Prabhat Gupta

- 量子デバイスのノイズとスケーラビリティがQMLの課題
- ノイズを評価し、クラスタ化して分散QMLタスクを効率的に配分
- 小規模モデルを低ノイズデバイスに割り当て、通信コストを削減
- 実験評価とノイズの影響を示すデータセットを提供

量子コンピューティングの新しい利用法がすごく楽しみ！これが実現したら、色んな技術がもっと速くなって経済的にもリーズナブルになりそうだよね。



**トピック:** [連合学習](fl), **カテゴリ:** quant-ph, cs.DC, **投稿日時:** 2024-06-20 12:00

- - -

### [Defending Against Sophisticated Poisoning Attacks with RL-based Aggregation in Federated Learning](http://arxiv.org/abs/2406.14217)

**連合学習におけるRLベースの集約による高度なポイズニング攻撃の防御**

Yujing Wang, Hainan Zhang, Sijia Wen, Wangjie Qiu, Binghui Guo

- 連合学習は特に精巧なモデルポイズニング攻撃に脆弱である
- 従来の防御手法は手動で作成された短期的な攻撃に対する更新評価やロバスト集約に焦点を当てている
- 本研究では、クライアントのデータ分布の安定性の観察により、悪意のあるクライアントを認識可能であることを見出した
- 提案手法AdaAggRLは、RLベースの適応集約方法を用い、実験で既存の防御モデルを大幅に上回る結果を示した

高度な攻撃にも対応できる手法の話、中身が気になる！これからのセキュリティ対策に革命が起きるかも🎶



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-20 11:33

- - -

### [Self-Supervised Pretext Tasks for Alzheimer's Disease Classification using 3D Convolutional Neural Networks on Large-Scale Synthetic Neuroimaging Dataset](http://arxiv.org/abs/2406.14210)

**アルツハイマー病分類のための大規模合成ニューロイメージングデータセットを用いた3D畳み込みニューラルネットワークの自己教師付きプレテキストタスク**

Chen Zheng

- 構造的MRI研究でADが脳全体に局所的および広範な神経変性変化を引き起こすことが示される
- 分割がないため、CNNベースの分類器を教師あり学習で訓練するのは困難
- AD対CN分類のために複数の自己教師付き手法を評価、3D T1強調MRIデータを使用
- 合成データセットで訓練された特徴抽出器が実データと同等の性能を発揮、合成データの有用性を示す

新しい合成データで本物の脳データに匹敵する研究ができるなんて、未知の世界が広がりそう！ちょっとワクワクするね！



**トピック:** [合成データ](sd), **カテゴリ:** eess.IV, cs.CV, cs.LG, **投稿日時:** 2024-06-20 11:26

- - -

### [SeCTIS: A Framework to Secure CTI Sharing](http://arxiv.org/abs/2406.14102)

**SeCTIS: CTI共有を安全にするためのフレームワーク**

Dincy R. Arikkat, Mert Cihangiroglu, Mauro Conti, Rafidha Rehiman K. A., Serena Nicolazzo, Antonino Nocera, Vinod P

- 近代的な組織がIT依存の運用によりサイバー攻撃の脅威にさらされている
- 現在の情報共有方法にはプライバシー保護が欠けており、データ漏洩のリスクが高い
- Swarm LearningとBlockchain技術を組み合わせたSeCTISフレームワークを設計
- ゼロ知識証明を利用して、データとモデルの品質、参加者の信頼性が評価可能

SeCTISの提供するプライバシー保護の方法がすごく気になる。最新技術を使ってどんどんセキュアな情報共有が広がりそうだね！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-20 08:34

- - -

### [FLoCoRA: Federated learning compression with low-rank adaptation](http://arxiv.org/abs/2406.14082)

**FLoCoRA: 低ランク適応による連合学習の圧縮**

Lucas Grativol Ribeiro, Mathieu Leonardon, Guillaume Muller, Virginie Fresse, Matthieu Arzel

- LoRA法を連合学習に適用し、ResNet-8で通信コストを4.8倍削減しつつ精度低下を1％未満に抑制
- Affine量子化スキームを組み合わせ、ResNet-18で通信コストを18.6倍削減、精度低下依然1％未満
- 従来のモデル圧縮手法と比較しても強力なメッセージサイズ削減のベースラインを提示
- 低ランク適応によりトレーニング時のメモリ要件も削減

通信コストの削減がすごいって感じ！これならデータいっぱいあっても効率的に扱えそうだね。とっても未来な気がする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, eess.SP, **投稿日時:** 2024-06-20 07:59

- - -

### [The Elusive Pursuit of Replicating PATE-GAN: Benchmarking, Auditing, Debugging](http://arxiv.org/abs/2406.13985)

**PATE-GANの再現を目指して：ベンチマーク、監査、デバッグの追跡**

Georgi Ganev, Meenatchi Sundaram Muthu Selva Annamalai, Emiliano De Cristofaro

- 差分プライバシーを利用した生成モデル(PATE-GAN)が現実世界の合成データで広く使用されている
- 6つのPATE-GANオープンソース実装を分析し、元の論文のユーティリティ性能を再現できなかった
- 実装のプライバシー監査を行い、意図より多くのプライバシーが漏れていることを示し、17のプライバシー違反と5つのバグを発見
- 研究成果のコードベースは公開されており、今後の改良と検証に役立つ

みんなでプライバシー技術の進化を追いかけていくのって本当にワクワクしちゃうよね！エラーを発見して改善したら、もっと安全で信頼できるデータが使える未来が楽しみ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-06-20 04:25

- - -

### [Privacy-Preserving ECG Data Analysis with Differential Privacy: A Literature Review and A Case Study](http://arxiv.org/abs/2406.13880)

**差分プライバシーを用いたECGデータ解析: 文献レビューとケーススタディ**

Arin Ghazarian, Jianwei Zheng, Cyril Rakovski

- 差分プライバシーは、データベース内の個人のプライバシーを保護しつつ、有用なデータ解析結果を共有する技術である。
- 実際の適用には重要なパラメータの推定が必要であり、明確な解決策やガイドラインが不足している。
- 論文前半では差分プライバシーの主要概念とECG解析への応用に関する文献レビューを行う。
- 後半では、不整脈データベースに対する差分プライバシー付きクエリリリースの実装方法と課題、ガイドラインに言及。

差分プライバシーって安全だけど実装が難しそうな技術だね。でも、それをECG解析に応用するなんて未来のヘルスケアが楽しみだなって思ったよ。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-19 23:17

- - -

### [Bayes' capacity as a measure for reconstruction attacks in federated learning](http://arxiv.org/abs/2406.13569)

**連合学習における再構築攻撃の測定としてのベイズ容量**

Sayan Biswas, Mark Dras, Pedro Faustini, Natasha Fernandes, Annabelle McIver, Catuscia Palamidessi, Parastoo Sadeghi

- 連合学習でも再構築攻撃が懸念されており、攻撃者は重み更新情報を基に訓練データを推測可能
- プライバシーコミュニティは差分プライバシーを用いたDP-SGDを推奨するが、効果は未確立
- 情報理論的枠組みを用いて再構築脅威モデルを形式化し、ベイズ容量を上限として設定
- 実証結果により、再構築脅威に対するメカニズムの効果を比較するための有効な測定法を提示

プライバシー保護しながら連合学習の安全性を向上させるなんて面白い！新しいアプローチが多くの分野で役立つといいね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, cs.CR, cs.IT, math.IT, **投稿日時:** 2024-06-19 13:58

- - -

### [Image Distillation for Safe Data Sharing in Histopathology](http://arxiv.org/abs/2406.13536)

**病理組織学における安全なデータ共有のための画像蒸留**

Zhe Li, Bernhard Kainz

- 病理組織学は、診断精度の向上、予後判定、および治療戦略の立案に役立つ
- 連合学習がデータ共有やプライバシーの問題を解決してきたが、ドメインシフトやバイアスの課題が残る
- 合成データを使ったデータセット蒸留が情報を圧縮し、制約なく共有可能とする方法を提案
- 人の読解可能な合成画像を用いた分類モデルが実データと遜色ない性能を持つことを示した

この研究、むっちゃ興味深いよね！データ共有の未来が広がりそうだし、医療現場での実用化も楽しみ！

**Comment:** accepted at MICCAI 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-06-19 13:19

- - -

### [Certificates of Differential Privacy and Unlearning for Gradient-Based Training](http://arxiv.org/abs/2406.13433)

**差分プライバシーと勾配ベース訓練のためのアンラーン証明書**

Matthew Wicker, Philip Sosnin, Adrianna Janik, Mark N. Müller, Adrian Weller, Calvin Tsay

- モデル所有者が訓練時に個人データのプライバシーを守る必要がある
- 差分プライバシーやアンラーンの技術は性能に悪影響を与える場合がある
- 具体的な予測の公開が$\epsilon=0$のプライバシー保証を満たすことを証明する新しいフレームワークを提案
- 金融サービス、医療画像診断、自然言語処理のタスクでフレームワークの有効性を検証

差分プライバシーだけでなく、アンラーンの証明も視野に入れててすごい！これで、ユーザーのデータ保護がより安心できるね。

**Comment:** 15 pages, 14 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-06-19 10:47

- - -

### [A Resource-Adaptive Approach for Federated Learning under Resource-Constrained Environments](http://arxiv.org/abs/2406.13351)

**リソース制約環境下での連合学習のためのリソース適応型アプローチ**

Ruirui Zhang, Xingze Wu, Yifei Zou, Zhenzhen Xie, Peng Li, Xiuzhen Cheng, Dongxiao Yu

- 複数のクライアントが異なるリソース制約を持つ連合学習問題の研究
- クライアントの計算および通信リソースが不足し、速いローカルトレーニングとリアルタイム知識共有が困難
- 提案手法「Fed-RAA」は、クライアントのリソースに基づいてモデル断片を適応的に割り当てる
- MNIST、CIFAR-10、CIFAR-100のデータセットで数値結果が有利であることを示す

リソースによる不公平をうまく解消する方法なのかな！これが成功すれば、色々なデバイスで効率的な連合学習が進むね。将来が楽しみ♪



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-06-19 08:55

- - -

### [Large-Scale Dataset Pruning in Adversarial Training through Data Importance Extrapolation](http://arxiv.org/abs/2406.13283)

**敵対的訓練におけるデータ重要性外挿による大規模データセットの剪定**

Björn Nieth, Thomas Altstidl, Leo Schwinn, Björn Eskofier

- 敵対的訓練は小さな攻撃に対する有望な防御戦略だが、訓練時間が増加する
- 大規模な合成データの統合により訓練時間がさらに増加する懸念
- データ剪定を用いてサンプル数を減らしつつ、精度とロバスト性を維持する必要性
- データ重要性スコアの外挿による剪定戦略を提案、実証的評価で効果を確認

新しいデータ剪定戦略ってめっちゃ画期的！訓練時間短縮できたら、もっといろんな応用が広がるね。未来のAIモデルがさらに強くなるのが楽しみだなぁ。

**Comment:** 8 pages, 5 figures, 3 tables, to be published in ICML: DMLR workshop

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-06-19 07:23

- - -

### [Enhancing Automated Audio Captioning via Large Language Models with Optimized Audio Encoding](http://arxiv.org/abs/2406.13275)

**大規模言語モデルと最適化された音声エンコーディングによる自動音声キャプションの強化**

Jizhong Liu, Gang Li, Junbo Zhang, Heinrich Dinkel, Yongqing Wang, Zhiyong Yan, Yujun Wang, Bin Wang

- 統一されたアンサンブル蒸留を用いた事前訓練済み音声エンコーダにより、音響トークンの有効性が向上
- 7Bパラメータを持つLlama 2をデコーダとして使用する利点を検討
- 別の事前訓練済み大規模言語モデルで、不十分な訓練データと注釈の曖昧さに起因するテキストエラーを修正
- -Base (LoRA)により音声エンコーダとテキストデコーダが最適化され、DCASE 2023 Task 6Aの優勝者を上回る33.0 SPIDEr-FLスコアを達成

大規模言語モデルとオーディオエンコードの相乗効果が新しい可能性を引き出しそうでワクワクする！近い将来、この研究が音声認識の質を劇的に向上させるかもしれないね。

**Comment:** Accepted by Interspeech 2024

**トピック:** [連合学習](fl), **カテゴリ:** cs.SD, cs.CL, eess.AS, **投稿日時:** 2024-06-19 07:09

- - -

### [Privacy-Preserving Logistic Regression Training on Large Datasets](http://arxiv.org/abs/2406.13221)

**大規模データセットにおけるプライバシー保護ロジスティック回帰の訓練**

John Chiang

- プライバシー保護機械学習は、秘密計算などの暗号方式を利用し、プライベートでセンシティブなデータの解析を目指す
- 提案された効率的なアルゴリズムは、準同型暗号を使用し、大規模暗号化データ上でロジスティック回帰を訓練
- quadratic gradientの使用により、一階勾配アルゴリズムの加速が期待される
- 実験は42.2万サンプルと200特徴の実際の金融データで行われ、ミニバッチアルゴリズムとフルバッチを比較

差分プライバシーってすごく未来！暗号化に関しても、こんなに大規模なデータが扱えるんだね。プライバシーが保護されながらの高速処理、めっちゃ気になる！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-19 05:19

- - -

### [A Federated Learning Approach for Multi-stage Threat Analysis in Advanced Persistent Threat Campaigns](http://arxiv.org/abs/2406.13186)

**連合学習アプローチによる高度持続型脅威キャンペーンにおける多段階脅威分析**

Florian Nelles, Abbas Yazdinejad, Ali Dehghantanha, Reza M. Parizi, Gautam Srivastava

- APTは新しい攻撃ベクトルを使用し、署名ベースの検出を回避するため検出が困難
- 有効な検出には複数のクライアントからのデータセットを使用する必要があるが、プライバシーの問題が生じる
- 3フェーズの非教師あり連合学習フレームワークを提案し、パターン抽出と分析を効率化
- パイエルの部分準同型暗号を使用してプライバシーを確保しつつSoTM 34データセットでの有効性を証明

最新の攻撃に適応するための新しい連合学習アプローチって面白そう！プライバシーも守れるし、効率的な検出が期待できるね。



**トピック:** [連合学習](fl), [準同型暗号](he), **カテゴリ:** cs.CR, **投稿日時:** 2024-06-19 03:34

- - -

### [Conditional score-based diffusion models for solving inverse problems in mechanics](http://arxiv.org/abs/2406.13154)

**力学の逆問題を解決するための条件付きスコアベース拡散モデル**

Agnimitra Dasgupta, Harisankar Ramaswamy, Javier Murgoitio Esandi, Ken Foo, Runze Li, Qifa Zhou, Brendan Kennedy, Assad Oberai

- ノイズを含む計測データから試料の空間的に変化する材料特性を推論するための枠組みを提案
- スコアネットワークと呼ばれるニューラルネットワークを用いて、計測の複数見積もりのスコア関数を近似する
- 様々な計測データの実現に対して、訓練されたスコアネットワークを再利用可能である
- 合成データや実際のエラストグラフィー実験を含む高次元の逆問題に対して、このアプローチの有効性を実証

このアプローチって、ノイズが入りやすい実際のデータでもかなり有効そうよね。いろんな計測方法に適用できるのは、ほんとに強みだと思うな。



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.AI, cs.LG, **投稿日時:** 2024-06-19 02:09

- - -

### [Advancing Retail Data Science: Comprehensive Evaluation of Synthetic Data](http://arxiv.org/abs/2406.13130)

**小売データサイエンスの進展：合成データの包括的評価**

Yu Xia, Chi-Hua Wang, Joshua Mabry, Guang Cheng

- 合成データ評価は、小売部門でのデータの正確性が重要
- フレームワークは合成小売データを忠実度、実用性、プライバシーの観点から評価
- 忠実度は安定性と汎用性で測定され、安定性は既知のデータ分布を正確に再現
- 差分プライバシーを使用して、訓練データと保留データセットの間でプライバシーを保障

評価のフレームワークめっちゃ必要かもね！将来の小売業界の合成データ技術がもっと進むといいな。



**トピック:** [合成データ](sd), [差分プライバシー](dp), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-06-19 00:47

- - -

### [Stackelberg Games with -Submodular Function under Distributional Risk-Receptiveness and Robustness](http://arxiv.org/abs/2406.13023)

**分布リスク受容性とロバスト性の下での$k$-部分モジュラー関数を用いたスタッケルベルグゲーム**

Seonghun Park, Manish Bansal

- 逆境下でのサブモジュラー最適化を研究し、敵対者と防御者のスタッケルベルグゲームに焦点を当てる
- 不確実性とデータノイズの影響を考慮し、不完全な確率分布の知識の課題に対処
- リスク回避とリスク受容の2つの問題(DRA $k$-SIPとDRR $k$-SIP)を提案し、収束アルゴリズムを導入
- 特定のコンポーネントを識別し、防御戦略や攻撃戦術のための自信区間のような値を提供

スタッケルベルグゲームに敵対者と防御者の視点で取り組むなんて、本当にスリリング！未来の攻防シナリオを読むようで、わくわくするね。



**トピック:** [合成データ](sd), **カテゴリ:** math.OC, cs.LG, **投稿日時:** 2024-06-18 19:30

- - -

### [Data Plagiarism Index: Characterizing the Privacy Risk of Data-Copying in Tabular Generative Models](http://arxiv.org/abs/2406.13012)

**データコピー指数: 表形式生成モデルにおけるデータコピーのプライバシーリスクの特徴付け**

Joshua Ward, Chi-Hua Wang, Guang Cheng

- 表形式生成モデルの目的は、訓練データセットからの情報漏洩を防ぐ、現実的な合成データを生成すること
- 現在の評価方法は、データコピーの評価においてプライバシー脅威の観点を欠いていることが多い
- 新しい類似性指標とMembership Inference Attackであるデータコピー指数 (DPI) を提案
- DPIによってデータコピーの新しい直感的定義を評価し、プライバシーリスクを特徴付け、対策の必要性を強調

データコピー指数（DPI）の提案、現行の評価方法の欠点を補うってところが興味深いよね。倫理的にも技術的にも、この分野にはまだまだ革新が期待できそうだね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, stat.ML, **投稿日時:** 2024-06-18 19:05

- - -

### [Instruction Data Generation and Unsupervised Adaptation for Speech Language Models](http://arxiv.org/abs/2406.12946)

**音声言語モデルのための指示データ生成と教師なし適応**

Vahid Noroozi, Zhehuai Chen, Somshubra Majumdar, Steve Huang, Jagadeesh Balam, Boris Ginsburg

- マルチモーダルな大規模言語モデルの訓練と評価のために合成データ生成を提案
- 音声とテキストの両モダリティを含むサンプルの不足を解決するため、合成データの生成が重要
- 大規模言語モデルでテキストを生成し、テキストから音声生成システムで音声を生成する手法を利用
- 実験結果により、テキストと音声の統合理解の進展が示され、転写のない音声データを使用しても高品質なサンプルが生成可能であることを確認

マルチモーダルなデータ生成はもっと多言語対応が進みそうで楽しい！音声とテキストの架け橋になって、いろんなアプリケーションができるかも。

**Comment:** Accepted for Interspeech 2024

**トピック:** [合成データ](sd), **カテゴリ:** eess.AS, cs.AI, cs.CL, cs.LG, **投稿日時:** 2024-06-18 08:27
