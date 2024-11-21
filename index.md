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

更新: 2024-11-21T04:23:46.905078

- - -

### [Utilizing Large Language Models to Synthesize Product Desirability Datasets](http://arxiv.org/abs/2411.13485)

**大規模言語モデルを活用した製品好感度データセットの合成**

John D. Hastings, Sherri Weitl-Harms, Joseph Doty, Zachary L. Myers, Warren Thompson

- 大規模言語モデルを用いて、製品好感度ツールキットのテスト用合成データセットを生成
- gpt-4o-miniを使用し、3つの方法で1000件の商品レビューを合成した
- 感情の整合性、テキストの多様性、生成コストでデータセットを評価
- 合成データはスケーラブルでコスト効率が高く、柔軟性に富む利点がある

この研究、AIを使ってコストを抑えながらも多様なデータを生成できるんだね。商品レビューとかがさらに分析しやすくなるって魅力的！

**Comment:** 9 pages, 2 figures, 6 tables

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, I.2.7; H.3.3; I.2.6; H.5.2, **投稿日時:** 2024-11-20 17:35

- - -

### [BelHouse3D: A Benchmark Dataset for Assessing Occlusion Robustness in 3D Point Cloud Semantic Segmentation](http://arxiv.org/abs/2411.13251)

**BelHouse3D：3Dポイントクラウドセマンティックセグメンテーションにおける遮蔽の強靭性評価用ベンチマークデータセット**

Umamaheswaran Raman Kumar, Abdur Razzaq Fayjie, Jurgen Hannaert, Patrick Vandewalle

- 3D視覚タスクの進展が遅い理由は、3Dベンチマークデータセットの限られた可用性が要因
- 屋内シーンセマンティックセグメンテーション用の実データセットは、収集困難でラベル付けも高コスト
- 合成データセットは現実条件を再現しにくく、特にポイントクラウドの遮蔽を十分に反映できない
- BelHouse3Dデータセットは、ベルギーの32軒の家を参照し、現実に近い条件と遮蔽を含めて合成された

実際の屋内環境を模したデータセットなんて面白そう！特に遮蔽が考慮されているのがリアルだし、いろんな場面で役立ちそうだよね。ベルギーの家を参考にしたのもなんかおしゃれ！

**Comment:** 20 pages, 6 figures, 3 tables, accepted at ECCV 2024 Workshops

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.AI, cs.LG, cs.RO, **投稿日時:** 2024-11-20 12:09

- - -

### [SONNET: Enhancing Time Delay Estimation by Leveraging Simulated Audio](http://arxiv.org/abs/2411.13179)

**SONNET: シミュレート音声を活用した時間遅れ推定の強化**

Erik Tegler, Magnus Oskarsson, Kalle Åström

- 時間遅れ推定は、音響ローカリゼーションの要であり、到達時間差を求めるタスクである
- 従来の手法GCC-PHATより合成データを基にした学習手法が優れることを示した
- 合成データセットで訓練したSONNETモデルを提供し、再訓練なしで新規データに対応
- モデルを用いることで、自己キャリブレーションのパフォーマンスが大幅に改善

新しい手法が合成データでこんなに効果的なのってスゴイね！音響ローカリゼーション手法にめちゃくちゃ貢献できそうでワクワクするよ。いつか自分のプロジェクトに応用してみたいな。



**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.CV, eess.AS, **投稿日時:** 2024-11-20 10:23

- - -

### [Writing Style Matters: An Examination of Bias and Fairness in Information Retrieval Systems](http://arxiv.org/abs/2411.13173)

**書き方は重要: 情報検索システムにおけるバイアスと公正性の検討**

Hongliu Cao

- 最新のテキスト埋め込みモデルは、特定の文書やクエリの書き方に対してバイアスを持つ
- 多くの埋め込みモデルは、通常よりもカジュアルで感情的なスタイルを軽視する傾向がある
- 合成データで微調整されたモデルは、生成データの特定のスタイルを優先しがち
- RAGシステムでは、多くのモデルがLLMの答えのスタイルにバイアスがある

情報検索システムって、ちゃんとフェアじゃなかったなんてちょっとびっくり！色んな書き方をもっと公平に取り扱ってくれる時代が来るといいね。埋め込みモデルの進化が楽しみ！

**Comment:** In Proceedings of the Eighteenth ACM International Conference on Web   Search and Data Mining (WSDM 25)

**トピック:** [合成データ](sd), **カテゴリ:** cs.IR, cs.AI, **投稿日時:** 2024-11-20 10:17

- - -

### [On-device Content-based Recommendation with Single-shot Embedding Pruning: A Cooperative Game Perspective](http://arxiv.org/abs/2411.13052)

**デバイス上でのコンテンツベースの推薦とシングルショット埋め込みプルーニング：協力ゲームの視点から**

Hung Vinh Tran, Tong Chen, Guanhua Ye, Quoc Viet Hung Nguyen, Kai Zheng, Hongzhi Yin

- コンテンツベース推薦システムはストレージのボトルネックが課題で、多くのリソースを必要とする
- 従来のプルーニング法は再訓練が必要であり、計算コストが高く適用が困難
- 提案するShaverはシェイプリー値を用い、貢献度に基づくパラメータの削減を実現
- Shaverは効率的な方法で情報損失を抑え、軽量な推薦モデルで優れた性能を発揮

Shaver、名前がかわいくない？これがあればデータがいっぱい増えても心配ないかも！もっと話題になりそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, cs.LG, **投稿日時:** 2024-11-20 05:56

- - -

### [NCAirFL: CSI-Free Over-the-Air Federated Learning Based on Non-Coherent Detection](http://arxiv.org/abs/2411.13000)

**NCAirFL: 非同期検出に基づくCSIフリーの空中連合学習**

Haifeng Wen, Nicolò Michelusi, Osvaldo Simeone, Hong Xing

- 空中連合学習（AirFL）は多元接続チャネルでの計算を活用する技術
- NCAirFLは、高価なチャネル推定なしでの同期信号整列を可能にする
- バイナリディザリングと長期メモリを用いて誤差補正を行う手法を提案
- 実験では、理想的な通信のある通常のFLと競合する性能を示す

非同期検出でこんなに性能が上がるなんて面白いよね！誤差補正機構が鍵な感じがして、もっと調べてみたくなるね。

**Comment:** 6 pages, 2 figures, submitted for possible publication

**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, cs.LG, eess.SP, math.IT, **投稿日時:** 2024-11-20 02:53

- - -

### [Data driven learning to enhance a kinetic model of distressed crowd dynamics](http://arxiv.org/abs/2411.12974)

**困難な群集の動態を強化するためのデータ駆動型学習法**

Daewa Kim, Demetrio Labate, Kamrun Mily, Annalisa Quaini

- 群集は状況に応じて動き方を変化させるため、数学的モデリングが複雑
- 緊急時の群集の変化をシミュレーションするために、ストレスレベルをパラメータとする運動モデルを考慮
- 逆群集動態問題を解くことで、ストレスレベルの推定を目指す
- 合成データセットを用いた予備結果を提示し、数値現象を解説

群集の中の人の動きって、ストレスで変わっちゃうんだね！逆にそれを解明することで、安全に役立てられるなんて、とっても未来的だと思うな〜。数値シミュレーションでの予備結果も気になるところ！

**Comment:** 31 pages, 18 figures

**トピック:** [合成データ](sd), **カテゴリ:** math.NA, cs.NA, **投稿日時:** 2024-11-20 02:02

- - -

### [Data-to-Model Distillation: Data-Efficient Learning Framework](http://arxiv.org/abs/2411.12841)

**データからモデルへの蒸留: データ効率の良い学習フレームワーク**

Ahmad Sajedi, Samir Khaki, Lucy Z. Liu, Ehsan Amjadian, Yuri A. Lawryshyn, Konstantinos N. Plataniotis

- 大規模データを小さな合成データに集約し、モデル性能を維持することを目指している
- 従来の手法は計算効率や複雑なデータセットのスケーラビリティ、深層アーキの一般化に課題がある
- 提案手法は生成モデルの学習可能なパラメータに知識を蒸留し、異なる蒸留比率に対応可能
- より高解像度でのスケーリングが可能であり、ニューラルアーキテクチャの検索で効果を実証

なんか、データをぎゅっと凝縮して、少ないデータでしっかり学習できるみたい！高解像度でもスイスイ使えるから、未来のIT技術がもっと省エネに進化しそうって感じでワクワクするね！

**Comment:** Accepted in the 18th European Conference on Computer Vision (ECCV   2024), Milan, Italy, September 29 October 4, 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.LG, **投稿日時:** 2024-11-19 20:10

- - -

### [FedCL-Ensemble Learning: A Framework of Federated Continual Learning with Ensemble Transfer Learning Enhanced for Alzheimer's MRI Classifications while Preserving Privacy](http://arxiv.org/abs/2411.12756)

**FedCL-アンサンブル学習: アルツハイマー症MRI分類におけるプライバシー保護を強化した連合継続学習のフレームワーク**

Rishit Kapoor, Jesher Joshua, Muralidharan Vijayarangan, Natarajan B

- 深層学習技術と安全なデータ処理を組み合わせアルツハイマー病の分類に新アプローチを提案
- ResNet、ImageNet、VNetを用いて医用画像データの高次特徴を抽出し、微妙なパターンに微調整
- 連合学習でデータプライバシーを保護しつつ、予測性能を向上させる分類支援策を組み込む
- 暗号化によるデータの輸送と患者情報の機密性を保持し、分類精度とセキュアな医療データ解析を提供する

これってすごく面白そう！アルツハイマー病の分類に連合学習と暗号化を活用して、プライバシーを守りながら精度を上げられるなんて素敵だよね。医療データの解析にもっと安心して使える技術が広がっていくといいなあ。

**Comment:** 6 pages, 4 figures

**トピック:** [連合学習](fl), **カテゴリ:** eess.IV, cs.AI, cs.CV, cs.IR, cs.LG, **投稿日時:** 2024-11-15 13:49
