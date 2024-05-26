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

更新: 2024-05-26T04:17:24.810932

- - -

### [Federated Online Adaptation for Deep Stereo](http://arxiv.org/abs/2405.14873)

**深度ステレオにおける連合オンライン適応**

Matteo Poggi, Fabio Tosi

- 連合学習の原則を活用して、深度ステレオネットワークを共同で適応
- 分散フレームワークを開発し、異なる環境で最適化プロセスをクライアントに分散
- リソース制約のあるデバイスも他のインスタンスの適応プロセスを活用し精度向上
- 実験結果で、連合適応がオンデバイス適応と同等かつ挑戦的な環境でより良好

技術って本当に進んでるんだなぁ。特に、適応プロセスを共有できるのがすごい！未来のデバイスがもっと賢くなりそう。

**Comment:** CVPR 2024. Project page: https://fedstereo.github.io/

**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-23 17:59

- - -

### [Recurrent Early Exits for Federated Learning with Heterogeneous Clients](http://arxiv.org/abs/2405.14791)

**異質なクライアントとの連合学習のための再帰的早期退出**

Royson Lee, Javier Fernandez-Marques, Shell Xu Hu, Da Li, Stefanos Laskaridis, Łukasz Dudziak, Timothy Hospedales, Ferenc Huszár, Nicholas D. Lane

- 連合学習 (FL) は複数のクライアント間でモデルをプライバシーを保ちながら学習する手法
- FLは異なるハードウェア能力を持つクライアントに対応するのが課題
- 提案手法ReeFLではサブモデルの特徴を共有する1つの分類器に融合
- ReeFLは画像と音声分類で既存手法より効果的であることを実証

サブモデルの融合や自己蒸留のアイデアって面白いね！FLの新しい可能性が広がりそう！

**Comment:** Accepted at the 41st International Conference on Machine Learning   (ICML 2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, cs.DC, **投稿日時:** 2024-05-23 17:01

- - -

### [A Systematic and Formal Study of the Impact of Local Differential Privacy on Fairness: Preliminary Results](http://arxiv.org/abs/2405.14725)

**ローカル差分プライバシーが公平性に与える影響の体系的かつ形式的な研究: 予備結果**

Karima Makhlouf, Tamara Stefanovic, Heber H. Arcolezi, Catuscia Palamidessi

- 差分プライバシーがMLの公平性にどのように影響するかを体系的に研究
- ローカル差分プライバシーが個別のサブグループに与える影響の矛盾を解明
- データ分布とプライバシーレベルによる公平性の変化を定量的に調査
- 合成データと実データで理論的発見を検証し、特定の属性の影響を評価

予備結果だけど、これは面白いね！公平性とプライバシーのバランスを取るための新しい視点が見つかるかも。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-23 15:54

- - -

### [Leveraging Electric Guitar Tones and Effects to Improve Robustness in Guitar Tablature Transcription Modeling](http://arxiv.org/abs/2405.14679)

**電気ギターの音色とエフェクトを活用したギタースコア転写モデリングのロバスト性向上**

Hegel Pedroza Wallace Abreu, Ryan Corey, Iran Roman

- ギタースコア転写（GTT）はソロギターパフォーマンスから自動的に楽譜を生成する技術
- 小規模なデータセットのため、GTTのロバスト性に限界
- 研究では、実録音のギター音色とエフェクトを使った合成データを提案
- プロのソロギターパフォーマンスを収集した新しい評価データセットでのアプローチ評価

ソロギターってかっこいいじゃん！新しい音色とかエフェクトいっぱい試せそうで、音楽がもっと面白くなるね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, eess.AS, **投稿日時:** 2024-05-23 15:13

- - -

### [Overcoming the Challenges of Batch Normalization in Federated Learning](http://arxiv.org/abs/2405.14670)

**連合学習におけるバッチ正規化の課題克服**

Rachid Guerraoui, Rafael Pinot, Geovani Rizk, John Stephan, François Taiani

- バッチ正規化は学習速度と精度向上に有効だが、データの不均質性が高い連合学習では課題がある
- 主な課題は外部共変量シフトとクライアント間の統計の不一致に起因する
- 論文ではFederated BatchNorm（FBN）を提案し、中央集権的な実行と同様のバッチ正規化を実現
- FBNは外部共変量シフトを低減し、統計が中央集権的な設定に一致する評価性能を提供

連合学習でもバッチ正規化を使えるようにしたんだね！データがバラバラでも統計の一致が図れるのは未来のAIに役立ちそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-23 15:07

- - -

### [PrivCirNet: Efficient Private Inference via Block Circulant Transformation](http://arxiv.org/abs/2405.14569)

**PrivCirNet: ブロック循環変換による効率的なプライベート推論**

Tianshi Xu, Lemeng Wu, Runsheng Wang, Meng Li

- 準同型暗号（HE）を用いたDNN推論はデータとモデルのプライバシーを保護するが、計算の負担が大きい
- DNNの重みを循環行列に変換することで、一般的な行列-ベクトル積を1次元の畳み込みに変換し、HE計算コストを大幅に削減
- PrivCirNetはHEエンコーディングアルゴリズムをカスタマイズし、ブロックサイズに比例して計算遅延を削減
- ResNet-18やVision Transformerでの評価結果、既存技術と比較してレイテンシーを大幅に削減し、精度も向上

既存の方法よりもすごく効率的だから、実用に向けてさらに注目されそうよね。これからの進展が楽しみだな！



**トピック:** [準同型暗号](he), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-05-23 13:44

- - -

### [Towards Privacy-Aware and Personalised Assistive Robots: A User-Centred Approach](http://arxiv.org/abs/2405.14528)

**プライバシー意識とパーソナライズド支援ロボットに向けて: ユーザー中心のアプローチ**

Fernando E. Casado

- 高齢者人口の増加により、負担軽減や生活の質向上のための長期ケアソリューションが必要である
- 支援ロボットは機械学習を利用してパーソナライズされたサポートを提供するが、プライバシー問題がある
- 本研究は連合学習（FL）を用いたプライバシー対応技術を提案し、データ共有を避けることでプライバシーやスケーラビリティ課題に対処
- スマート車椅子支援などのソリューションを開発し、ユーザーの独立性と幸福感を向上させることを目指す

支援ロボットが高齢者の生活をどう変えるか楽しみね！未来のケアがもっとパーソナライズドになると良いな～

**Comment:** RSS Pioneers 2024 Research Statement

**トピック:** [連合学習](fl), **カテゴリ:** cs.RO, cs.HC, cs.LG, **投稿日時:** 2024-05-23 13:14

- - -

### [Hybrid Global Causal Discovery with Local Search](http://arxiv.org/abs/2405.14496)

**局所探索を用いたハイブリッドなグローバル因果発見**

Sujai Hiremath, Jacqueline R. M. A. Maasch, Mengxiao Gao, Promit Ghosal, Kyra Gan

- 未知の因果モデルに対応する有向非巡回グラフの学習は難しいタスク
- トポロジーソートアルゴリズムで階層的な因果順序を確立し、既存の手法より多くの因果情報をエンコード
- ノンパラメトリックな制約ベースのアルゴリズムで局所的な条件集合を検索し、偽のエッジを削除して精度向上
- 理論的な正当性と最悪ケースでの多項式時間複雑性を保証し、合成データで実証

因果関係を探る新しい方法って面白そう！実際のデータでの活用が楽しみだね。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-23 12:28

- - -

### [SolNet: Open-source deep learning models for photovoltaic power forecasting across the globe](http://arxiv.org/abs/2405.14472)

**SolNet: 世界中の太陽光発電予測のためのオープンソースディープラーニングモデル**

Joris Depoortere, Johan Driesen, Johan Suykens, Hussain Syed Kazmi

- 太陽光発電予測に使用されるディープラーニングモデルは多くの高品質データを必要とするが、実際には取得困難
- SolNetは一般的な多変量予測器であり、豊富な合成データからの転移学習を用いてこれらの課題に対処
- オランダ、オーストラリア、ベルギーの実生産データを用いて、データが不足している状況やベースラインモデルよりも予測性能が向上
- 天候データ、季節パターン、合成データの量、ソースロケーションの誤設定が結果に大きな影響を与えると指摘

オープンソースでグローバルに使えるなんてすごいよね！転移学習の部分が特に未来感あって面白そう！

**Comment:** 24 pages, 5 figures

**トピック:** [合成データ](sd), **カテゴリ:** eess.SP, cs.LG, **投稿日時:** 2024-05-23 12:00

- - -

### [Worldwide Federated Training of Language Models](http://arxiv.org/abs/2405.14446)

**言語モデルの世界的な連合学習**

Alex Iacob, Lorenzo Sani, Bill Marino, Preslav Aleksandrov, Nicholas Donald Lane

- 巨大な計算資源と質の低いデータの使用が実践的、法的、倫理的に課題である
- 連合学習は協力組織から未利用のデータを収集できる有望な代替手段である
- WorldLMは連邦の連合体に基づき、各連邦が業界や法域に応じて自律的に運営できる
- WorldLMは参考レイヤーを用いた部分的なモデル局所化で統計的異質性に対処し、優れた性能を示す

気になる！異質なデータをうまく統合する仕組みって、とても将来有望じゃない？きっと多様な応用が見込めそうだね！

**Comment:** 19 pages, 8 figures, Under Review

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.CL, cs.DC, I.2.7, **投稿日時:** 2024-05-23 11:25

- - -

### [JiuZhang3.0: Efficiently Improving Mathematical Reasoning by Training Small Data Synthesis Models](http://arxiv.org/abs/2405.14365)

**JiuZhang3.0: 小規模データ合成モデルの訓練による数学的推論の効率的向上**

Kun Zhou, Beichen Zhang, Jiapeng Wang, Zhipeng Chen, Wayne Xin Zhao, Jing Sha, Zhichao Sheng, Shijin Wang, Ji-Rong Wen

- 数学的推論は大規模言語モデルの重要な能力であり、実世界での応用に必要である
- 従来の手法は大規模な数学関連テキストを収集するか、強力なLLMを使用して大量の数学問題を合成するためコストが高い
- 小規模LLMを訓練し高品質な合成データを生成する効率的な方法を提案し、GPT-4を用いて小規模LLMに合成能力を蒸留
- JiuZhang3.0モデルを用いた実験結果は、複数の数学的推論データセットで最高水準の性能を達成している

小規模なモデルでこんなに成果が出るなんてすごいよね！これなら、もっと効率よく問題解けるようになりそうでワクワクするかも！

**Comment:** 28 pages, SOTA math LLM using Well-trained Data Synthesis LLM

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, **投稿日時:** 2024-05-23 09:43

- - -

### [DeepSeek-Prover: Advancing Theorem Proving in LLMs through Large-Scale Synthetic Data](http://arxiv.org/abs/2405.14333)

**DeepSeek-Prover: 大規模合成データによるLLMでの定理証明の進展**

Huajian Xin, Daya Guo, Zhihong Shao, Zhizhou Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, Xiaodan Liang

- Leanのような証明支援ツールが数学的証明の検証を革新し、高精度と信頼性を提供
- 大規模言語モデル(LLM)は数学的推論に有望だが、訓練データの不足が障害
- 高校・大学レベルの数学競技問題からLean 4証明データを生成し、合成データセットを作成
- DeepSeekMath 7Bモデルを微調整し、GPT-4を超える精度で定理証明を達成

訓練データが不足している問題を、合成データという斬新な方法で解決しているのがすごく面白いね！この成果がさらに深まったら、数理学の教育とか研究がもっと進化しそうな予感がするよ！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, **投稿日時:** 2024-05-23 09:03

- - -

### [Variational Bayes for Federated Continual Learning](http://arxiv.org/abs/2405.14291)

**連合継続学習のための変分ベイズ**

Dezhong Yao, Sanmu Li, Yutong Dai, Zhiqiang Xu, Shengshan Hu, Peilin Zhao, Lichao Sun

- 連合継続学習（FCL）はリアルタイムデータに対処するために注目されている
- ストレージ制限とプライバシー懸念がローカルモデルのデータアクセスを制限
- 「破滅的忘却」を防ぐため、連合ベイズ神経ネットワーク（FedBNN）を導入
- FedBNNは新旧データ分布を統合し、最先端の結果を達成

実際に継続学習の課題を解決するためにベイズドアプローチを取り入れるなんてすごいね！FedBNNが他の方法よりも良い結果を出すなんて、もっと詳しく知りたいな！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-23 08:09

- - -

### [Improving Language Models Trained with Translated Data via Continual Pre-Training and Dictionary Learning Analysis](http://arxiv.org/abs/2405.14277)

**翻訳データを用いた言語モデルの改善：継続的事前学習と辞書学習解析を通じて**

Sabri Boughorbel, MD Rizwan Parvez, Majd Hawasly

- 英語からアラビア語への翻訳データを使用した訓練には、多額のコストと文化的バイアスの問題がある
- 2.2Mの短編ストーリーを翻訳し、1M-33Mのパラメータの異なる物語生成モデルを訓練
- 翻訳による質の低下を補うため、元のデータの1％を占める高品質な合成データで再訓練
- GPT-4と辞書学習解析を用いて、提案手法が翻訳の欠点を解消する実用的手段であることを示す

翻訳データの問題点と、それを改善するための手法が具体的で興味深いね。高品質な合成データの活用がさらに広がるといいな。

**Comment:** 15 pages

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, **投稿日時:** 2024-05-23 07:53

- - -

### [Federated Domain-Specific Knowledge Transfer on Large Language Models Using Synthetic Data](http://arxiv.org/abs/2405.14212)

**大規模言語モデルを使用した連合ドメイン特化型知識伝達に関する合成データ利用**

Haoran Li, Xinyuan Zhao, Dadi Guo, Hanlin Gu, Ziqian Zeng, Yuxing Han, Yangqiu Song, Lixin Fan, Qiang Yang

- 大規模言語モデル（LLMs）は並外れた性能と汎化能力を示し、多くのアプリケーションに統合されている
- 敏感なドメインでは、データのプライバシー規制のため、外部のLLMsを直接使用することが禁止されている
- 既存の手法は公開データやLLMsを活用してデータを生成し、知識を小型モデル（SLMs）に伝達している
- FDKTフレームワークは差分プライバシーを使用して合成されたデータを基に知識を伝達し、SLMsの性能を大幅に向上させる

この論文のアイデアって、差分プライバシーを使って合成データを作り出してるところがすごくない？プライバシーを守って性能向上できるなんて未来的でワクワクするよね！



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.CL, **投稿日時:** 2024-05-23 06:14

- - -

### [Rank Reduction Autoencoders -- Enhancing interpolation on nonlinear manifolds](http://arxiv.org/abs/2405.13980)

**ランクリダクションオートエンコーダー -- 非線形多様体の補間を強化**

Jad Mounayer, Sebastian Rodriguez, Chady Ghnatios, Charbel Farhat, Francisco Chinesta

- 古典的オートエンコーダー（AE）は過適合の問題を抱え、補間能力に「穴」が生じる
- 提案されたランクリダクションオートエンコーダー（RRAE）は、低ランクの潜在空間の利用で正確な予測を実現
- RRAEの潜在空間は十分に大きく、特徴抽出を可能にする
- 提案された2つの具体化（強い形式と弱い形式）で、潜在空間を忠実に表現

へぇー、AEの過適合の問題に対する新しい解決策だね。しかも、MNISTで実験してるのもテンション上がる！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-22 20:33

- - -

### [Rehearsal-free Federated Domain-incremental Learning](http://arxiv.org/abs/2405.13900)

**リハーサルなしの連合ドメインインクリメンタル学習**

Rui Sun, Haoran Duan, Jiahua Dong, Varun Ojha, Tejal Shah, Rajiv Ranjan

- 既存のリソース制約の中での連合学習において、リハーサルなしで破滅的忘却を回避する
- 新たなフレームワーク「RefFiL」を提案し、参加者の異なるドメインからドメイン非依存の知識を学習
- ローカルで生成されるきめ細かなプロンプトを使用し、グローバルで一貫した境界線を維持
- ドメイン適応プロンプトの生成と対比学習損失により、精度と有効性を向上

個々のデバイスのリソースが限られていてもこの方法なら安心。連合学習の新しい可能性が広がりそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CV, **投稿日時:** 2024-05-22 18:13

- - -

### [FACT or Fiction: Can Truthful Mechanisms Eliminate Federated Free Riding?](http://arxiv.org/abs/2405.13879)

**FACTかフィクションか：真実のメカニズムは連合学習でのただ乗りを排除できるか**

Marco Bornstein, Amrit Singh Bedi, Abdirisak Mohamed, Furong Huang

- 連合学習は「ただ乗り」問題があり、参加者がほとんど貢献しなくても訓練済みのモデルを受け取れる
- 過去のメカニズムはただ乗り問題に対処しつつ、真実性を考慮していない
- 提案するFACTは罰則システムを使い、競争環境を提供して真実性を確保
- FACTは非正直な参加者がただ乗りすることを防ぎ、エージェントの損失を4倍以上に減少

罰則システムって新しいね！ちゃんと貢献せずにズルしようとする人が減って、お互いに頑張れる環境になるのがいい感じかな。

**Comment:** 18 pages, 5 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.GT, cs.DC, cs.LG, econ.TH, **投稿日時:** 2024-05-22 17:59

- - -

### [Federated Learning in Healthcare: Model Misconducts, Security, Challenges, Applications, and Future Research Directions -- A Systematic Review](http://arxiv.org/abs/2405.13832)

**ヘルスケアにおける連合学習：モデルの誤用、セキュリティ、課題、応用、将来の研究方向に関する体系的レビュー**

Md Shahin Ali, Md Manjurul Ahsan, Lamia Tasnim, Sadia Afrin, Koushik Biswas, Md Maruf Hossain, Md Mahfuz Ahmed, Ronok Hashan, Md Khairul Islam, Shivakumar Raman

- ヘルスケア分野ではデータのデジタル化によりデータプライバシーの懸念が高まっている
- 連合学習（FL）はデータを共有せずに分散データから学習することでプライバシーを保護する
- 実装には非IIDデータ環境でのモデル収束、通信オーバーヘッド、複数機関の協力管理などの課題がある
- 研究はFLのセキュリティ慣行、課題を評価し、実用的な応用と将来の研究方向を探求している

医療機関がデータをシェアしなくてもコラボできるFLってすごくない？それに、まだまだ改善の余地があって研究のしがいがありそうだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.LG, **投稿日時:** 2024-05-22 16:59

- - -

### [Diffusion-Based Cloud-Edge-Device Collaborative Learning for Next POI Recommendations](http://arxiv.org/abs/2405.13811)

**拡散ベースのクラウド-エッジ-デバイス協調学習による次のPOI推薦**

Jing Long, Guanhua Ye, Tong Chen, Yang Wang, Meng Wang, Hongzhi Yin

- LBSNの発展により、履歴データを基に次のPOIを予測する重要性が増加
- 既存のDNNは性能が高いがプライバシー問題とタイムリーさに限界がある
- 新たなDCPRは拡散モデルを活用し、クラウド-エッジ-デバイス構造で地域別かつ個別の推薦を提供
- 実験では新しいユーザーや地域にも優れた適応性と精度を示し、効率も向上

これ読んで、次の旅行先のおすすめとかもっと賢くなるって想像しちゃった！プライバシーも守ってくれるし、これからのエンドユーザー体験が楽しみだね！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IR, **投稿日時:** 2024-05-22 16:41

- - -

### [Bayesian Inference Under Differential Privacy: Prior Selection Considerations with Application to Univariate Gaussian Data and Regression](http://arxiv.org/abs/2405.13801)

**差分プライバシーにおけるベイズ推定: 単変量ガウスデータと回帰への応用における事前選択の考察**

Zeki Kazan, Jerome P. Reiter

- 差分プライバシーで保護されたガウス分布の平均と分散に対するベイズ推定を記述
- データの境界制約を考慮した事前分布指定の重要性を示す
- 豊富な事前情報がない場合でも有効な推定を提供するデフォルト事前のクラスについて理論的・経験的結果を提供
- 差分プライバシーデータを用いた回帰のベイズ推定への応用方法を論じる

差分プライバシーでの事前分布選択が重要なんだね！ベイズ推定がどんどん進化してる感じ、ワクワクするよね😊

**Comment:** 9-page main document with 5 figures and a 12-page appendix with 4   figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ME, cs.CR, **投稿日時:** 2024-05-22 16:27

- - -

### [Banded Square Root Matrix Factorization for Differentially Private Model Training](http://arxiv.org/abs/2405.13763)

**差分プライバシーを持つモデル訓練のためのバンド付き平方根行列分解**

Nikita Kalinin, Christoph Lampert

- 現行の差分プライバシーモデル訓練法は行列分解技術に基づいており、計算オーバーヘッドが大きい
- 新たにBSRという行列分解アプローチを提案し、計算ボトルネックを克服
- 確率的勾配降下法の重要なシナリオにおいて、BSRにより計算オーバーヘッドをほぼ無視できる
- BSRを使用したモデル訓練は既存の最高の方法と同等の性能を持ちながら、計算オーバーヘッドを完全に回避

BSR、なんか効率すごく良さそうじゃない？計算オーバーヘッド回避できるだけでなく、性能も落ちないなんて夢みたい！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-22 15:47

- - -

### [CG-FedLLM: How to Compress Gradients in Federated Fune-tuning for Large Language Models](http://arxiv.org/abs/2405.13746)

**CG-FedLLM: 大規模言語モデルの連合ファインチューニングにおける勾配の圧縮方法**

Huiwen Wu, Xiaohan Li, Deyi Zhang, Xiaogang Xu, Jiafei Wu, Puning Zhao, Zhe Liu

- 現在の大規模言語モデルは、一元的な学習が中心でプライバシーの脅威がある
- 連合学習は生データではなく勾配を転送するが、通信コストが大きい
- CG-FedLLMは勾配を圧縮し、エンコーダーとデコーダーで通信効率を改善
- 実験で通信コストの削減と性能向上が確認され、重要な特徴を選別する仕組みが有効

このアプローチって、効率も上げつつプライバシーも守れるのが面白いよね！未来の大規模モデルにはこういう技術がもっと増えそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-22 15:32

- - -

### [Naturally Private Recommendations with Determinantal Point Processes](http://arxiv.org/abs/2405.13677)

**デターミナンタルポイントプロセスによる自然なプライベートレコメンデーション**

Jack Fitzsimons, Agustín Freitas Pasqualini, Robert Pisarczyk, Dmitrii Usynin

- 差分プライバシーを遵守するためには、ランダム化メカニズムの導入が一般的
- デターミナンタルポイントプロセス（DPP）は元々暗黙的に差分プライバシーを満たす
- DPPがepsilon-DPを満たすために必要な変更点の導出と感度分析を実施
- プライバシーと効用のトレードオフを改善するためのDPPの単純な代替案を提案

DPPが元々プライバシーを考慮しているのが面白いね！これを応用すれば、もっとスムーズで安全なレコメンデーションが実現できそう。



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-22 14:20

- - -

### [Emulating Full Client Participation: A Long-Term Client Selection Strategy for Federated Learning](http://arxiv.org/abs/2405.13584)

**クライアント全参加のエミュレーション：連合学習の長期的なクライアント選択戦略**

Qingming Li, Juzheng Miao, Puning Zhao, Li Zhou, Shouling Ji, Bowen Zhou, Furui Liu

- クライアント選択はシステム収束効率に影響し、連合学習の重要問題である
- 現行方法は各ラウンドごとの評価に頼り、長期最適化の必要性を見落としている
- 提案手法は全クライアント参加のパフォーマンスをエミュレートする新しい選択戦略である
- 実験では精度と公平性の大幅な向上と最小限の時間オーバーヘッドが示された

提案手法で、今まで難しかった連合学習の最適化が実現できそう！長期的な視点でクライアントを選ぶことで、もっと効率的な学習が期待できるね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-22 12:27

- - -

### [End-to-End Real-World Polyphonic Piano Audio-to-Score Transcription with Hierarchical Decoding](http://arxiv.org/abs/2405.13527)

**エンドツーエンドの実世界のポリフォニックピアノ音声から楽譜への転写と階層的デコード**

Wei Zeng, Xian He, Ye Wang

- ピアノの音声から楽譜への転写（A2S）は音楽作曲や練習、分析にとって重要である
- 既存のA2Sシステムはバー（小節）レベルの情報取得が難しく、合成データでしか訓練されていない
- 階層的デコーダーを持つSeq2Seqモデルを提案し、バーレベルとノートレベルの情報をマルチタスク学習で転写
- 合成データと人間の演奏録音のギャップを埋めるために、2段階の訓練スキームを提案

階層的デコードで複雑な楽譜の構造も対応できるのがすごく有用そう。リアルな録音データを使った初めての実験結果も期待が持てるね！

**Comment:** 8 pages, 5 figures, accepted by IJCAI 2024 - AI, Arts & Creativity   Track

**トピック:** [合成データ](sd), **カテゴリ:** cs.SD, cs.AI, eess.AS, **投稿日時:** 2024-05-22 10:52

- - -

### [Locally Private Estimation with Public Features](http://arxiv.org/abs/2405.13481)

**公開特徴とローカルプライバシー推定**

Yuheng Ma, Ke Jia, Hanfang Yang

- semi-feature LDP（半特徴ローカル差分プライバシー）を定義し、一部の特徴が公開され、残りとラベルが保護される
- semi-feature LDPでは、非パラメトリック回帰のmini-max収束率が古典的LDPと比較して大幅に向上
- 公開とプライベート特徴の情報を最大限に活用する推定手法HistOfTreeを提案。理論的にmini-max最適収束率に達する
- ユーザーが保護する特徴を手動で選択可能なシナリオを探求し、データ駆動型パラメータ調整戦略を提案。理論と実証で同様の結果を達成

公開されている特徴を使うとプライバシーの効率が良くなるんだね！ユーザーが自分で選べるっていうのも、柔軟だし実用的でおもしろいわ！



**トピック:** [差分プライバシー](dp), **カテゴリ:** stat.ML, cs.CR, cs.LG, **投稿日時:** 2024-05-22 09:47

- - -

### [AdaFedFR: Federated Face Recognition with Adaptive Inter-Class Representation Learning](http://arxiv.org/abs/2405.13467)

**AdaFedFR: 適応型インタークラス表現学習による連合顔認識**

Di Qiu, Xinyang Lin, Kaiye Wang, Xiangxiang Chu, Pengfei Yan

- プライバシー保護のため、分散データセットで連合学習を用いる
- 既存の方法はパフォーマンスや通信コストの課題がある
- 公的アイデンティティの特徴表現を学習可能なネガティブ知識として活用
- 3回未満の通信ラウンドで先行アプローチを上回るパフォーマンスを実現

顔認識の連合学習の課題をうまく解決してるところがすごいね! 実用性も高そうだから、これからの顔認識技術がもっと安全に使えるようになるかな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CV, **投稿日時:** 2024-05-22 09:19

- - -

### [A Huber Loss Minimization Approach to Mean Estimation under User-level Differential Privacy](http://arxiv.org/abs/2405.13453)

**ユーザー別差分プライバシー下での平均推定に対するハーバー損失最小化アプローチ**

Puning Zhao, Lifeng Lai, Li Shen, Qingming Li, Jiafei Wu, Zhe Liu

- 分散システムでは、ユーザーの全サンプル貢献のプライバシー保護が重要である
- 既存の二段階方式はバイアスを生むため、特に重い尾を持つ分布では重大
- 大きなサンプルサイズのユーザーが感度を増し、不均衡なユーザーには不適
- 提案するハーバー損失アプローチは、バイアスを減らし、理論解析と数値実験で有効性を示した

新しいアプローチは不均衡なデータに強いってとこが面白そう！これできっともっとプライバシー保護に役立つね！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, **投稿日時:** 2024-05-22 08:46

- - -

### [Task-agnostic Decision Transformer for Multi-type Agent Control with Federated Split Training](http://arxiv.org/abs/2405.13445)

**タスクに依存しない意思決定変換器による連合分割トレーニングとマルチタイプエージェント制御**

Zhiyuan Wang, Bokui Chen, Xiaoyang Qu, Zhenhou Hong, Jing Xiao, Jianzong Wang

- パーソナライズされたエージェントの状態変数と行動空間の変動が連合学習アルゴリズムの課題
- FSDTフレームワークは分散データを活用し、データプライバシーを保ちながらトレーニングを行う
- クライアントエージェントでのローカル埋め込みモデルと予測モデル、サーバーでのグローバルトランスフォーマーデコーダーモデルを使用
- D4RLデータセットを用いた評価で、従来の中央集権的トレーニングと比較して通信量と計算負荷を大幅に削減

FSDTって、分散データで学習するのにプライバシーも守れるのがいいね！未来の自動運転システムとかがどんな風に進化するか楽しみ♡

**Comment:** Accepted by the 2024 International Joint Conference on Neural   Networks (IJCNN 2024)

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-05-22 08:37

- - -

### [Why In-Context Learning Transformers are Tabular Data Classifiers](http://arxiv.org/abs/2405.13396)

**なぜインコンテキスト学習トランスフォーマーが表形式データ分類器なのか**

Felix den Breejen, Sangmin Bae, Stephen Cha, Se-Young Yun

- TabPFNは合成データを用いてインコンテキスト学習トランスフォーマーを事前訓練し、表形式データ分類を行う
- 合成データは実世界のデータと特徴やラベルを共有しないため、その成功の理由は不明
- 研究では、ICLトランスフォーマーが事前訓練中に複雑な決定境界を生成する能力を習得することを示した
- 新規の森林データセット生成器を開発し、これが非現実的だが複雑な決定境界を持つデータセットを生成することを確認

合成データでも効果が出るのすごい！もっと色んなデータで試したら、将来いろんな分野で活用できそうだね。

**Comment:** 9 pages main body, 22 pages total. Preprint under review

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, stat.ML, **投稿日時:** 2024-05-22 07:13

- - -

### [FedCache 2.0: Exploiting the Potential of Distilled Data in Knowledge Cache-driven Federated Learning](http://arxiv.org/abs/2405.13378)

**FedCache 2.0: 知識キャッシュ駆動型連合学習における蒸留データの潜在能力の活用**

Quyang Pan, Sheng Sun, Zhiyuan Wu, Yuwei Wang, Min Liu, Bo Gao

- 連合エッジ学習（FEL）はエッジデバイスがデータプライバシーを保ちながら機械学習モデルを協力して訓練する方法である
- 実際のFEL導入はデバイスの制約やデバイス-サーバー間の相互作用に関連する課題に直面
- FedCache 2.0は、蒸留データと知識キャッシュを利用してこれらの課題を同時に解決する新しいFELアーキテクチャを提案
- FedCache 2.0は通信効率を少なくとも28.6倍向上させることで、驚異的な個別オンデバイスモデルの訓練を実現

FedCache 2.0って、個別のエッジデバイスに最適化できてすごく賢そう！通信効率も大幅にアップするなんて期待大だね🌟

**Comment:** 20 pages, 8 figures, 10 tables

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-22 06:19

- - -

### [Clipped Uniform Quantizers for Communication-Efficient Federated Learning](http://arxiv.org/abs/2405.13365)

**通信効率の高い連合学習のためのクリップドユニフォーム量子化器**

Zavareh Bozorgasl, Hao Chen

- クリップドユニフォーム量子化を連合学習に導入し、通信の効率化を図る
- 最適なクリッピング閾値と適応量子化で通信オーバーヘッドを削減
- 対称クリッピングとユニフォーム量子化がモデル性能に与える影響を評価
- MNISTデータセットでのシミュレーションにより、高精度と通信効率を両立

クリッピングと量子化の複雑なバランスを取りつつ、連合学習の効率を劇的に向上させる方法だね！部活帰りにでも、もう一度議論してみたい！

**Comment:** Work in progress

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.MA, eess.SP, **投稿日時:** 2024-05-22 05:48

- - -

### [Efficient Imitation Learning with Conservative World Models](http://arxiv.org/abs/2405.13193)

**保守的な世界モデルを用いた効率的な模倣学習**

Victor Kolev, Rafael Rafailov, Kyle Hatch, Jiajun Wu, Chelsea Finn

- 報酬関数なしでの専門家のデモからの方策学習問題に取り組む
- 分布シフト、環境の確率性、エラーの累積で方策の適用が失敗することが課題
- 環境のモデルを学習し、合成データを使用するアプローチは追加の分布シフトを引き起こす
- オンライン世界モデルアルゴリズムよりもオフラインRLやファインチューニングに理論的つながりがある

面白そうなポイントは、新しい方針が少ないデモでも高性能を発揮するところかな。特に画像ベースの複雑なタスクを解決できるのはすごいよね。

**Comment:** Oral presentation, L4DC 2024

**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-21 20:53

- - -

### [CausalPlayground: Addressing Data-Generation Requirements in Cutting-Edge Causality Research](http://arxiv.org/abs/2405.13092)

**CausalPlayground: 最先端の因果関係研究におけるデータ生成要件への対応**

Andreas W M Sauter, Erman Acar, Aske Plaat

- 因果効果の研究は、真の効果がある現実のデータセットが不足しているため、合成データに依存している
- 現在のデータ生成ツールはすべての要件を満たさず、即席の方法が使われ、データセットにばらつきが生じ、研究進捗が遅れる
- CausalPlaygroundを導入することで、構造因果モデル（SCM）の生成、サンプリング、および共有の標準化プラットフォームを提供し、細かい制御を可能にする
- Gymnasiumとの統合により、強化学習（RL）環境の標準フレームワークでオンライン対話を実現し、因果関係研究の効率と比較可能性を向上させることを目指す

新しいツールで因果関係の研究がもっとスムーズになるなんて、すごくわくわくする！これを使った研究とか見てみたいなぁ。



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.LG, **投稿日時:** 2024-05-21 12:08

- - -

### [FedASTA: Federated adaptive spatial-temporal attention for traffic flow prediction](http://arxiv.org/abs/2405.13090)

**FedASTA: 交通流予測のための連合学習適応空間-時間アテンション**

Kaiyuan Li, Yihan Zhang, Xinlei Chen

- モバイルデバイスとIoTデバイスから異種空間-時間データが大量に生成されることに対処
- 連合学習（FL）は、オリジナルデータを共有せずにモデル訓練を可能にし、プライバシー問題を軽減
- 提案されたFedASTAフレームワークは、クライアントからの時系列データを用いて動的な空間-時間関係をモデル化
- 実世界の交通流データセットで広範な実験を行い、最先端の性能を達成

動的な空間-時間の関係をモデル化することで、交通流予測がもっと正確にできるようになるかも！データを直接共有しないで済むから、プライバシーの問題にも配慮してる感じがいいね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.DC, **投稿日時:** 2024-05-21 11:44

- - -

### [StatAvg: Mitigating Data Heterogeneity in Federated Learning for Intrusion Detection Systems](http://arxiv.org/abs/2405.13062)

**StatAvg: 侵入検知システム向け連合学習におけるデータ不均一性の軽減**

Pavlos S. Bouzinis, Panagiotis Radoglou-Grammatikis, Ioannis Makris, Thomas Lagkas, Vasileios Argyriou, Georgios Th. Papadopoulos, Panagiotis Sarigiannidis, George K. Karagiannidis

- 連合学習は分散型学習手法で、生データを第三者に開示せずにモデルを構築できる
- サイバーセキュリティ領域での侵入検知システムに連合学習が注目されている
- データの不均一性が連合学習の信頼性に課題をもたらしている
- 提案手法StatAvgは、非独立・非同分布データの影響を軽減し、効率を実証

データのプライバシーを守りつつも、みんなで協力してシステムをより賢くする方法ってすごいね！StatAvgが現実でどれくらい効果があるのか試してみると面白そう！

**Comment:** 10 pages, 8 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, cs.DC, cs.LG, **投稿日時:** 2024-05-20 14:41
