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

更新: 2024-07-08T04:21:02.336097

- - -

### [Differentially Private Inductive Miner](http://arxiv.org/abs/2407.04595)

**差分プライバシーを備えた帰納的マイナー**

Max Schulze, Yorck Zisgen, Moritz Kirschte, Esfandiar Mohammadi, Agnes Koschmider

- プロセスマイニングにおけるイベントトレースは、個人の行動を明らかにするため、個人データの保護が難題である
- 従来の匿名化方法（k匿名性やイベントログのサニタイズ）は、十分な背景知識を持つ攻撃者に対して効果が薄い
- 本研究では差分プライバシー（DP）を利用し、イベントトレースからの有用な推論が不可能になるようにプロセスツリーを学習する方法を提案
- 実験結果として、DPIMは個人データを保護しつつ、従来の帰納的マイナーと比較して有用性の損失が少ないプロセスツリーを生成することが示された

この研究、めちゃくちゃ未来っぽい！差分プライバシーで個人情報を守りつつ、精度も犠牲にしないなんて。どんな応用ができるんだろう？考えるだけでワクワクするね。

**Comment:** The first two authors equally contributed to this work

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-07-05 15:42

- - -

### [Smart Sampling: Helping from Friendly Neighbors for Decentralized Federated Learning](http://arxiv.org/abs/2407.04460)

**スマートサンプリング: 分散型連合学習のためのフレンドリーネイバーズからの支援**

Lin Wang, Yang Chen, Yongxin Guo, Xiaoying Tang

- 分散型連合学習は、プライバシーを保ちながら知識を共有し通信コストを削減する
- 分散型FLは中央サーバーを必要とせず、クライアント間の直接通信が可能でリソース節約
- AFIND+アルゴリズムは有益な隣接ノードを識別し、選択するノード数を適応的に調整
- AFIND+は他のサンプリングアルゴリズムより優れた性能を示し、既存の最適化とも互換性あり

分散型の連合学習って、中央サーバーなしで済むからすごく画期的だと思う！友達のネットを通じて良いところを学ぶのってまるで勉強会みたいで、これからもっと普及しそうだね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-05 12:10

- - -

### [Machine Learning for Complex Systems with Abnormal Pattern by Exception Maximization Outlier Detection Method](http://arxiv.org/abs/2407.04248)

**異常パターンを持つ複雑なシステムに対する機械学習: 例外最大化異常検出法によるアプローチ**

Zhikun Zhang, Yiting Duan, Xiangjun Wang, Mingyuan Zhang

- EMODMは確率モデルと統計アルゴリズムを用いて異常パターンを検出
- 二状態ガウス混合モデルに基づきリアルタイムでの確率的異常検出を実現
- 合成データの数値ケースでEMODMの性能を実証
- 実データで三相インバータの短絡パターンやCOVID-19による失業データの異常期間を検出

複雑なシステムの異常検出をリアルタイムで行えるなんてすごい！EMODMの応用範囲が広がれば、いろんな分野で役立ちそうだね。



**トピック:** [合成データ](sd), **カテゴリ:** stat.ML, cs.LG, **投稿日時:** 2024-07-05 04:30

- - -

### [Solutions to Deepfakes: Can Camera Hardware, Cryptography, and Deep Learning Verify Real Images?](http://arxiv.org/abs/2407.04169)

**ディープフェイク対策: カメラハードウェア、暗号技術、深層学習は本物の画像を検証できるか?**

Alexander Vilesov, Yuan Tian, Nader Sehatbakhsh, Achuta Kadambi

- 生成AIの急速な進化が、本物の画像と動画の信頼性に大きな影響を与えている
- 将来的に生成AIで作られたデジタルコンテンツがカメラで撮影されたものと見分けがつかなくなる
- 高品質な生成アルゴリズムが誰でも利用できるようになり、合成画像と本物の画像の割合が大きくなる
- 本物のデータと合成データを高精度で区別する手法の確立が急務である

この論文、最新の技術と暗号学を駆使してディープフェイクを撃退する方法を探るなんて、ワクワクするよね。未来のデジタル世界で本物と偽物を確実に見分ける技術、私たちの生活にどう影響するか楽しみだな！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CV, cs.CR, **投稿日時:** 2024-07-04 22:01

- - -

### [An applied Perspective: Estimating the Differential Identifiability Risk of an Exemplary SOEP Data Set](http://arxiv.org/abs/2407.04084)

**応用の視点: 差分同定リスクの推定 ― 例示的なSOEPデータセットを用いて**

Jonas Allmann, Saskia Nuñez von Voigt, Florian Tschorsch

- 実世界の研究データ利用には、匿名化された形での出版契約が必要。
- データ保護コンプライアンスのため、差分プライバシーのような正式なプライバシー保証が役立つ。
- 本研究では、既存のプライバシーメトリクスを拡張し、基本統計クエリに対するリスクメトリクスを効率的に計算する方法を示す。
- 実世界のデータセットに基づく実証分析により、現実的な条件下でリスク計算する知識を拡充し、多くの課題も浮き彫りにした。

差分プライバシーについての深掘りで新しい視点が得られそう。現実のデータセットでの分析が多くの課題を明らかにしたところが興味深いよね。

**Comment:** Accepted on IWPE 2024

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-04 17:50

- - -

### [Support Vector Based Anomaly Detection in Federated Learning](http://arxiv.org/abs/2407.03920)

**連合学習におけるサポートベクターベースの異常検知**

Massimo Frasson, Dario Malchiodi

- 異常検知はサイバーセキュリティから産業システムまで幅広く重要である
- 従来の中央集約型アプローチはデータプライバシーに課題がある
- 連合学習を利用し、Ensemble SVDDとSupport Vector Electionの2つの新しいアルゴリズムを提案
- 提案アルゴリズムは小規模データセットでも効果的に動作し、計算コストが低い

この研究、異常検知の未来を変える予感がすごいね！簡単なデータでも使えるなら、もっと普及しそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-04 13:32

- - -

### [FedSat: A Statistical Aggregation Approach for Class Imbalaced Clients in Federated Learning](http://arxiv.org/abs/2407.03862)

**FedSat: 連合学習におけるクラス不均衡なクライアントに対する統計的集計アプローチ**

Sujit Chowdhury, Raju Halder

- 連合学習（FL）はプライバシー保護分散機械学習として注目されているが、クライアント間でのデータの不均一性に課題がある
- FedSatはコストに敏感な損失関数と優先クラスに基づく重み付け集約方式を採用し、ラベルの偏りやクラスの欠損、量の偏りに対処
- コストに敏感な損失関数は少数クラスのモデル性能を向上させ、優先クラスに基づく重み付け集約方式は統計的意義と重要クラスでの性能に基づいてクライアントの貢献度を調整
- 多種多様なデータ不均一性環境での実験により、FedSatは最先端手法を大幅に上回る効果を示し、平均1.8%、最も効果の低いベースライン法に対して19.87%の改善を達成、他手法と比べて収束も速いことを実証

FedSatってすごくない？少数派のデータにもちゃんと対応できるなんて、これからの連合学習の可能性めっちゃ広がりそう！一緒にもっと掘り下げて見てみようよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-04 11:50

- - -

### [Google Topics as a way out of the cookie dilemma?](http://arxiv.org/abs/2407.03846)

**Cookieのジレンマを解決するGoogle Topicsの提案**

Marius Köppel, Jan-Philipp Muttach, Gerrit Hornung

- 広告目的で情報や個人データを処理する際、明示的な同意が必要だと強調
- ドイツのTelekommunikation-Telemedien-Datenschutzgesetzにより、情報の保存とアクセスには事前の同意が必要
- Googleの「Privacy Sandbox」戦略の一部である「Federated Learning of Cohorts (FLoC)」は大きな批判を受けた
- 新たなプロジェクト「Google Topics」が導入され、ユーザーを興味グループに分類して広告をパーソナライズ

Googleって常に新しい技術に挑戦してるね！「Google Topics」って、ユーザーにとってもプライバシー守られてて安心だね。



**トピック:** [連合学習](fl), **カテゴリ:** cs.CY, **投稿日時:** 2024-07-04 11:28

- - -

### [Finetuning End-to-End Models for Estonian Conversational Spoken Language Translation](http://arxiv.org/abs/2407.03809)

**エストニア語会話音声翻訳のためのエンドツーエンドモデルの微調整**

Tiia Sildam, Andra Velve, Tanel Alumäe

- エストニア語と英語、エストニア語とロシア語間の会話音声翻訳を対象とした研究
- データ不足を補うために、ウェブスクレイピングと音声認識データセットから合成データを作成
- Whisper、OWSM 3.1、SeamlessM4Tの3つのエンドツーエンドモデルを評価
- 合成データによる微調整で翻訳精度が大幅に向上し、SeamlessM4Tは既存の音声翻訳システムと同等かそれ以上

エストニア語の音声翻訳って珍しくて面白そう！合成データを使う発想、絶対これからの研究でも活かせそうだね。

**Comment:** Accepted to LoResMT 2024 (ACL workshop)

**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, eess.AS, **投稿日時:** 2024-07-04 10:33

- - -

### [SRAS: Self-governed Remote Attestation Scheme for Multi-party Collaboration](http://arxiv.org/abs/2407.03745)

**SRAS: 複数関係者協力のための自己管理型リモート認証スキーム**

Linan Tian, Yunke Shen, Zhiqiang Li

- TEE（信頼実行環境）は、クラウド計算資源を使用する際にアプリケーションの機密性と整合性を確保
- 複数関係者のクラウド計算シナリオでは、各関係者のTEEを検証するためのRelying Partyの選定とデータ漏洩の問題が未解決
- SRASを提案、認証と検証機能を含み、TEEと計算資産の信頼性を検証する非中央集権的な統合プラットフォームを実現
- Relying Partyエンクレーブを設計、他の参加者の代わりに地方検証を行い、データ漏洩なしに信頼を確保

複数関係者がクラウドで安全に共同作業できるなんて素敵！これからのクラウド利用が広がりそうだね。



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-04 08:57

- - -

### [Collection, usage and privacy of mobility data in the enterprise and public administrations](http://arxiv.org/abs/2407.03732)

**企業および公共機関におけるモビリティデータの収集、使用およびプライバシー**

Alexandra Kapp

- 人のモビリティデータは都市のモビリティ管理で重要だが、個人情報を含むため匿名化が必要
- 匿名化技術はデータの有用性と利用の制限を引き起こすトレードオフが存在
- 実際の実装に関する情報は少なく、特に大企業外での状況は不明確
- プライバシー保護方法は差分プライバシーの最新基準を満たしておらず、実践的な研究の基盤を提供

モビリティデータの扱いってプライバシーとの両立がすごく難しいんだね。実際の匿名化の実践例をもっと知ることで、将来の標準化に役立ちそうだね！

**Comment:** 17 pages, 1 figure, Privacy Enhancing Technologies Symposium

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-04 08:29

- - -

### [Verifying Peephole Rewriting In SSA Compiler IRs](http://arxiv.org/abs/2407.03685)

**SSAコンパイラIRにおけるピープホールリライトの検証**

Siddharth Bhat, Alex Keizer, Chris Hughes, Andrés Goens, Tobias Grosser

- 現代のコンパイラではドメイン固有の中間表現（IR）の使用が増加している
- インタラクティブ定理証明器（ITP）はコンパイラのエンドツーエンドの検証に強力な保証を提供
- 通常の証明エンジニアリングは高コストだが、Alive peephole verifierのような自動検証ツールが注目されている
- Leanプルーフアシスタントを使ってMLIRのシンタックスを翻訳し、ピープホールリライトの正当性を証明

現代のコンパイラでの変換と検証の進化がわかるね！検証ツールの便利さとITPの強力さを両立させるなんて、エキサイティングな時代が来そう！

**Comment:** accepted at ITP 2024

**トピック:** [準同型暗号](he), **カテゴリ:** cs.PL, cs.LO, **投稿日時:** 2024-07-04 07:16

- - -

### [A Survey of Data Synthesis Approaches](http://arxiv.org/abs/2407.03672)

**データ合成手法の調査**

Hsin-Yu Chang, Pei-Yu Chen, Tun-Hsiang Chou, Chang-Sheng Kao, Hsuan-Yun Yu, Yen-Ting Lin, Yun-Nung Chen

- 合成データ使用の目標は多様性の向上、データバランスの調整、ドメインシフトの解消、エッジケースの解決
- 合成データ技術は専門知識、直接訓練、事前訓練後微調整、ファンデーションモデルに分類される
- 合成データフィルタリングの目標は基本品質、ラベル一貫性、データ分布に分類
- 今後の方向性として、品質重視、合成データの評価、マルチモデルデータ拡張が重要とされる

合成データがどれだけ現実の世界に近づけられるかが興味深いよね。未来の人工知能の進化にワクワク！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.AI, **投稿日時:** 2024-07-04 06:37

- - -

### [MSfusion: A Dynamic Model Splitting Approach for Resource-Constrained Machines to Collaboratively Train Larger Models](http://arxiv.org/abs/2407.03622)

**MSfusion: リソース制約のある機械向けの動的モデル分割アプローチによる協調的学習**

Jin Xie, Songze Li

- 大規模なモデルのトレーニングには、大量のデータと豊富な計算資源が必要
- モデル分割を用いたMSfusionはリソース制約のあるデバイスに適した協調学習フレームワーク
- 各参加者がモデルの一部を持ち寄ることで計算と通信コストを削減
- 画像とNLPのタスクでMSfusionのパフォーマンスと効率性、スケーラビリティの高さを実証

リソースが限られたデバイス向けに大規模なモデルを協調して学習するアイデアって面白い！これでみんなのスマホでも高度なAIが動く未来がやってくるかも！

**Comment:** 12 pages, 9 figures

**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-07-04 04:06

- - -

### [Scalable Zero-Knowledge Proofs for Verifying Cryptographic Hashing in Blockchain Applications](http://arxiv.org/abs/2407.03511)

**ブロックチェーンアプリケーションにおける暗号ハッシュの検証のためのスケーラブルなゼロ知識証明**

Oleksandr Kuznetsov, Anton Yezhov, Vladyslav Yusiuk, Kateryna Kuznetsova

- ゼロ知識証明（ZKP）はブロックチェーンのスケーラビリティの課題を解決する有望な手段である
- SHA-256アルゴリズムの計算的整合性を確保するためのZKP生成と検証の方法を提案
- Plonky2フレームワークを用いて、ランダムデータとNEARブロックチェーンの実データブロックで効率性とスケーラビリティを実証
- 実験結果は、異なるデータサイズや種類に対して一貫したパフォーマンスを示し、生成された回路と証明のサイズも現実的

今後さらに他の暗号プリミティブへの適用可能性を評価することが必要だね。これ、実世界の複雑なシナリオでもどうなるか見てみたいな！



**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** cs.CR, **投稿日時:** 2024-07-03 21:19

- - -

### [AgentInstruct: Toward Generative Teaching with Agentic Flows](http://arxiv.org/abs/2407.03502)

**AgentInstruct: エージェントフローによる生成的教育に向けて**

Arindam Mitra, Luciano Del Corro, Guoqing Zheng, Shweti Mahajan, Dany Rouhana, Andres Codas, Yadong Lu, Wei-ge Chen, Olga Vrousgos, Corby Rosset, Fillipe Silva, Hamed Khanpour, Yash Lara, Ahmed Awadallah

- 合成データは、言語モデルの開発に重要であるが、品質と多様性にばらつきがある
- Generative Teachingのために、AgentInstructを提案し、高品質な合成データを自動生成
- 合成データを用いてMistral-7bを後訓練し、多くのベンチマークで大きな改善を確認
- 他のモデルと比較して、Orca-3が大幅に優れた性能を発揮

AgentInstructすごくない？いっぱいデータ作れて、モデルがもっと賢くなっちゃうかも！これが本格化したら、AIの新しいスキルを簡単に教えられる未来が来るかもね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.AI, cs.CL, cs.LG, **投稿日時:** 2024-07-03 21:01

- - -

### [Releasing Large-Scale Human Mobility Histograms with Differential Privacy](http://arxiv.org/abs/2407.03496)

**差分プライバシーによる大規模ヒト移動ヒストグラムの公開**

Christopher Bian, Albert Cheu, Yannis Guzman, Marco Gruteser, Peter Kairouz, Ryan McKenna, Edo Roth

- GoogleのEIE（Environmental Insights Explorer）は、人々の移動統計を約5万の地域で報告
- 移動統計は、炭素排出量の推定や交通政策・インフラの決定に活用される
- 鋭敏なユーザーデータの適切なプライバシー保護が必須であり、連合分析と差分プライバシーを併用
- 提案されたメカニズムは高いプライバシー ($\epsilon \approx 2$-DP) と有用性を両立し、ベースラインより大幅に改善

これって、プライバシー保護しながら交通データを活用するって、未来のスマートシティーの一歩だよね。めっちゃワクワクする！



**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.DB, **投稿日時:** 2024-07-03 20:54

- - -

### [The Role of Privacy Guarantees in Voluntary Donation of Private Data for Altruistic Goals](http://arxiv.org/abs/2407.03451)

**アルトルイスティックな目的のためにプライベートデータを自主的に寄付する際のプライバシー保証の役割**

Ruizhe Wang, Roberta De Viti, Aarushi Dubey, Elissa M. Redmiles

- 医療データの寄付意欲を4つのプライバシー保証（データ有効期限、匿名化、利用制限、アクセス制御）で検討
- プライバシー保証の確認方法として、自己監査と専門家監査を比較
- データ収集主体（営利/非営利組織）によるプライバシー期待の違いを評価
- 非営利組織への期待は高いが、営利組織に対してはプライバシー声明で期待値が上昇

この研究、非営利組織への信頼感って大きいんだね。でも、どうやってユーザーの期待と技術の現実をもっと合わせるかが未来の課題みたい！



**トピック:** [PETs](pets), **カテゴリ:** cs.CR, cs.HC, **投稿日時:** 2024-07-03 18:50
