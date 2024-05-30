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

更新: 2024-05-30T04:22:38.388639

- - -

### [Mitigating Disparate Impact of Differential Privacy in Federated Learning through Robust Clustering](http://arxiv.org/abs/2405.19272)

**連合学習における差分プライバシーの不均等影響をロバストクラスタリングで軽減する方法**

Saber Malekmohammadi, Afaf Taik, Golnoosh Farnadi

- 連合学習はデータを局所化し、差分プライバシーを組み合わせるが、少数派グループに対する性能格差が生じる
- 既存のクラスタリング手法はDPノイズの影響で誤差が生じやすく、その改善が必要
- 提案手法はモデル更新とトレーニング損失に基づくクラスタリングで高精度を維持
- 提案手法はGMMと大きなバッチサイズを活用し、ノイズやクラスタリングエラーの影響を緩和する

クラスタリングと連合学習の組み合わせ、すごく期待できそう！ノイズが問題になりやすいDPでも、こういう工夫で公平さを保てるのは最新技術の進歩って感じだね。



**トピック:** [連合学習](fl), [差分プライバシー](dp), **カテゴリ:** cs.LG, cs.CR, cs.DC, **投稿日時:** 2024-05-29 17:03

- - -

### [A Privacy-Preserving Graph Encryption Scheme Based on Oblivious RAM](http://arxiv.org/abs/2405.19259)

**秘密計算に基づくプライバシー保護型グラフ暗号スキーム**

Seyni Kane, Anis Bkakria

- グラフ暗号スキームは、信頼できないサーバー上で暗号化されたグラフに対する安全なクエリを可能にする
- 既存の手法は、グラフ構造やクエリパターンを漏洩する脆弱性があり、セキュリティとプライバシーに脅威をもたらす
- 新たな提案手法は、オブリビアスRAMと信頼できる実行環境の技術を組み合わせ、アクセスパターンとクエリパターンの漏洩を軽減
- 実験により、現実の位置ナビゲーションサービスでの提案手法の効率性が評価された

グラフ暗号といってもけっこう身近な話なんだね！これが実用化されたら、SNSとかでのプライバシーももっと安心できるかも～



**トピック:** [TEE](tee), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-29 16:47

- - -

### [Synthetic Potential Outcomes for Mixtures of Treatment Effects](http://arxiv.org/abs/2405.19225)

**治療効果の混合に対する合成潜在結果**

Bijan Mazaheri, Chandler Squires, Caroline Uhler

- さまざまな人口やデータソースからの大規模データセットに依存する現代のデータ分析
- 潜在的混乱や異質な治療効果（HTE）が因果推論の二大課題
- 条件平均治療効果（CATE）では潜在的異質性による効果の混合を解決できない
- 新手法「合成潜在結果（SPO）」を提案し、異質性を解消、混合効果を識別可能に

新しい「合成潜在結果（SPO）」の提案だって！異質な反応とかどう処理するか、けっこう気になるテーマだよね。これがうまくいけば、データ解析の精度がすごく上がりそうだよね！



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, econ.EM, stat.ME, **投稿日時:** 2024-05-29 16:05

- - -

### [LoByITFL: Low Communication Secure and Private Federated Learning](http://arxiv.org/abs/2405.19217)

**LoByITFL: 低通信で安全かつプライベートな連合学習**

Yue Xia, Christoph Hofmeister, Maximilian Egger, Rawad Bitar

- 連合学習はクライアントデータのプライバシーとビザンチン攻撃に対するセキュリティという課題に直面
- 既存の方法はプライバシーを犠牲にすることが多いが、LoByITFLは犠牲なし
- LoByITFLは小規模で代表的なデータセットを用い、一度限りの信頼できる第三者を使用
- プライバシーとビザンチン耐性の理論的保証と、収束保証や実験結果を提供している

ビザンチン耐性を保ちながら通信の効率化も目指してるところが画期的だね。理論と実験の両方で支えられてるから、注目されそう！



**トピック:** [連合学習](fl), **カテゴリ:** cs.IT, cs.CR, cs.DC, cs.LG, math.IT, **投稿日時:** 2024-05-29 16:00

- - -

### [Algorithmic Transparency and Participation through the Handoff Lens: Lessons Learned from the U.S. Census Bureau's Adoption of Differential Privacy](http://arxiv.org/abs/2405.19187)

**ハンドオフレンズから見たアルゴリズムの透明性と参加：米国国勢調査局の差分プライバシー採用から得た教訓**

Amina A. Abdu, Lauren M. Chambers, Deirdre K. Mulligan, Abigail Z. Jacobs

- 差分プライバシー採用で社会的、組織的、政治的文脈が変化
- 透明性と参加への努力は、技術設計だけでなく価値と政策に焦点を当てるべき
- ハンドオフモデルは、技術的決定に隠れた価値を明らかにする有用なツール
- 境界オブジェクト単独では不十分で、信頼される専門家が必要

DPを探る技術と価値のバランスが面白そう！どんな専門家が課題を解決するかも知りたいな。

**Comment:** 21 pages, FAccT '24

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CY, **投稿日時:** 2024-05-29 15:29

- - -

### [FedMAP: Unlocking Potential in Personalized Federated Learning through Bi-Level MAP Optimization](http://arxiv.org/abs/2405.19000)

**FedMAP: 二層MAP最適化を通じた個別化連合学習の潜在能力の解放**

Fan Zhang, Carlos Esteve-Yagüe, Sören Dittmer, Carola-Bibiane Schönlieb, Michael Roberts

- 連合学習はデータプライバシーを保ちながら分散データで機械学習モデルを訓練する技術
- 客先データの差異（不均衡や特徴分布の偏り）が大きく、単一のグローバルモデルでは非IIDデータに対応が難しい
- 提案されたバイエシアンPFLフレームワークは、二層最適化を用いてデータ異質性の課題に対処する
- 実データと合成データの評価で、既存手法に比べモデルの正確性と通信効率が大幅に向上

バイエシアンアプローチで個別に適応するってすごく賢いよね！データプライバシーを守りながらも高精度を実現できるなんて、もっと広がるといいな。



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, **投稿日時:** 2024-05-29 11:28

- - -

### [Federated Learning under Partially Class-Disjoint Data via Manifold Reshaping](http://arxiv.org/abs/2405.18983)

**部分的にクラスが分断されたデータにおける連合学習：マニフォールドの再形成によるアプローチ**

Ziqing Fan, Jiangchao Yao, Ruipeng Zhang, Lingjuan Lyu, Ya Zhang, Yanfeng Wang

- 統計的不均一性が連合学習の性能を制限し、その解決策としてFedProxやMOONなどが提案されている
- 従来のアプローチはクライアントごとにほぼすべてのクラスのサンプルが必要であり、部分的なクラス分断は未解決だった
- PCDD（部分的クラス分断データ）の特有の問題として、局所最適化の方向が偏ることが挙げられる
- FedMRは2つの損失関数を追加し、局所トレーニングの特徴空間を調整することで精度と通信効率を向上させる

連合学習の具体的な問題にアプローチしててめっちゃ面白そう！FedMRがどんな風にうまくいくのか、実際にコード使ってみたいなって思った！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-29 10:56

- - -

### [Federated Learning with Bilateral Curation for Partially Class-Disjoint Data](http://arxiv.org/abs/2405.18972)

**部分的にクラスが分離されたデータのための両側キュレーションを伴う連合学習**

Ziqing Fan, Ruipeng Zhang, Jiangchao Yao, Bo Han, Ya Zhang, Yanfeng Wang

- 部分的にクラスが分離されたデータ（PCDD）は連合アルゴリズムの性能を大きく損なう形成
- ローカルクラスの欠如による角度崩壊問題と既存クラスの空間浪費問題を引き起こす
- 総合的な改善を実現する既存の手法は存在しないため、新しいアプローチFedGELAを提案
- FedGELAは平均してFedAvgより3.9％、最良のベースラインより1.5％の性能向上を達成

連合学習でも個々のデータ特性をうまく活かす工夫が必要なんだね。まだまだ新しい発見がありそうでワクワクする！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-29 10:34

- - -

### [Locally Estimated Global Perturbations are Better than Local Perturbations for Federated Sharpness-aware Minimization](http://arxiv.org/abs/2405.18890)

**連合シャープネス意識最適化において局所的推定されたグローバル摂動が局所摂動より優れている**

Ziqing Fan, Shengchao Hu, Jiangchao Yao, Gang Niu, Ya Zhang, Masashi Sugiyama, Yanfeng Wang

- 連合学習では、クライアント間のデータ異質性がシャープな最小値を生む
- シャープネス意識最適化(SAM)を局所トレーニングに組み込むのが一般的
- 提案されたFedLESAMはグローバルモデルの差異を利用してグローバル摂動の方向を推定
- FedLESAMは効率性が高く、連合学習において優れた性能を示した

提案された手法がどうやって連合学習の効率を上げてるか気になるね。FedLESAM、試してみたら面白いかも！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.DC, **投稿日時:** 2024-05-29 08:46

- - -

### [Simulation, Modelling and Classification of Wiki Contributors: Spotting The Good, The Bad, and The Ugly](http://arxiv.org/abs/2405.18845)

**Wiki貢献者のシミュレーション、モデリング、分類：良い、悪い、醜いを見極める**

Silvia García Méndez, Fátima Leal, Benedita Malheiro, Juan Carlos Burguillo Rial, Bruno Veloso, Adriana E. Chis, Horacio González Vélez

- データクラウドソーシングはボランティアの貢献者が関連データを供給し、さまざまなサービスを提供するプロセス
- 敵対的環境での悪意あるデータ操作が深刻な懸念を引き起こす
- 人間とボット、善意と悪意の貢献者を自動識別するシミュレーションおよび分類手法を提案
- 実験的なデータセットでの分類精度が92%に達し、分類器の信頼性と品質を大幅に向上

この論文、WikiVoyageを使ってちゃんと評価してるのが面白いよね！悪意あるボットを見分けるって、将来のネット環境にすごく役立ちそう！



**トピック:** [合成データ](sd), **カテゴリ:** cs.CL, cs.AI, cs.LG, **投稿日時:** 2024-05-29 07:56

- - -

### [Enhancing Security and Privacy in Federated Learning using Update Digests and Voting-Based Defense](http://arxiv.org/abs/2405.18802)

**連合学習における更新ダイジェストと投票ベースの防御を用いたセキュリティとプライバシーの強化**

Wenjie Li, Kai Fan, Jingyuan Zhang, Hui Li, Wei Yang Bryan Lim, Qiang Yang

- 連合学習はデータをローカライズしつつ協調してモデルを訓練するが、クライアントとサーバの信頼性が課題
- 提案するFLUDフレームワークは、プライバシー保護とビザンチン攻撃への抵抗を両立
- $LinfSample$メソッドを用いて更新ダイジェストを生成し、サーバが共有距離行列を計算することでSMPCオーバーヘッドを大幅に削減
- プライバシー保護と投票ベースの防御メカニズムを統合し、低通信と実行時間のオーバーヘッドでビザンチン攻撃に対抗

FLUDの方法、めっちゃ興味あるー！通信ラウンドを最適化しながら、セキュリティを向上させるとか未来の連合学習に期待だね。

**Comment:** 14 pages

**トピック:** [連合学習](fl), **カテゴリ:** cs.CR, cs.AI, **投稿日時:** 2024-05-29 06:46

- - -

### [LMO-DP: Optimizing the Randomization Mechanism for Differentially Private Fine-Tuning (Large) Language Models](http://arxiv.org/abs/2405.18776)

**LMO-DP: 微調整のための差分プライバシーランダム化メカニズムの最適化（大規模）言語モデル**

Qin Yang, Meisam Mohammad, Han Wang, Ali Payani, Ashish Kundu, Kai Shu, Yan Yan, Yuan Hong

- DP-SGDは大規模な言語モデルの微調整におけるプライバシーを保証するが、ガウス機構に依存しすぎて精度を低下させる
- LMO-DPは、強いプライバシー条件下でも、正確な微調整を可能にする新しい差分プライバシーメカニズムを提案
- オフライン最適ノイズ探索法により、ノイズの大きさを効率的に削減し、精度を向上させる
- RoBERTa-largeやGPT-2のタスクで精度を大幅に向上させ、Llama-2にも対応

ガウス機構よりも性能がいいって、かなり画期的じゃない？プライバシーに配慮しつつ精度を追求できる未来が待ってるかも！

**Comment:** 18 pages, 15 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** cs.CR, cs.CL, cs.LG, **投稿日時:** 2024-05-29 05:32

- - -

### [GIST: Greedy Independent Set Thresholding for Diverse Data Summarization](http://arxiv.org/abs/2405.18754)

**GIST: グリーディ独立集合しきい値法による多様なデータ要約**

Matthew Fahrbach, Srikumar Ramalingam, Morteza Zadimoghaddam, Sara Ahmadian, Gui Citovsky, Giulia DeSalvo

- 論文では新しいサブセット選択タスクである最小距離多様データ要約（MDDS）を提案
- MDDSはデータサンプリングや特徴選択などの機械学習に幅広く応用可能
- GISTアルゴリズムはMDDSに対して$\frac{2}{3}$の近似保証を実現、最大独立集合問題を近似
- 実証研究で、GISTが合成データおよびImageNetの実世界画像分類実験で既存手法を上回ることを示す

GISTアルゴリズムって、マジで効率的なデータ選択の手助けになるんじゃない？特に、学習データの多様性が重要な場面で光りそうだね！

**Comment:** 15 pages, 1 figure

**トピック:** [合成データ](sd), **カテゴリ:** cs.DS, cs.LG, **投稿日時:** 2024-05-29 04:39

- - -

### [PermLLM: Private Inference of Large Language Models within 3 Seconds under WAN](http://arxiv.org/abs/2405.18744)

**PermLLM: 広域ネットワークで3秒以内に大規模言語モデルのプライベート推論**

Fei Zheng, Chaochao Chen, Zhongxuan Han, Xiaolin Zheng

- LLMの出現によりプライバシー懸念が増加し、ユーザーの問い合わせがモデル提供者に送信される問題がある。
- 従来のMPCに基づく方法ではプライバシーは守られるが、データ転送量が多く時間がかかり実用的ではない。
- PermLLMは安全なランダム置換を用いて非線形関数の評価を高速化し、秘密共有プロトコルや準同型暗号を最適化。
- PermLLMは、実際のネットワーク設定下で従来のMPCソリューションよりもはるかに高速な3秒/トークンの推論を実現。

新しいプライバシー保護技術でスピードが速まるなんて素敵！他のアプリでもこの技術が使われるといいな。



**トピック:** [準同型暗号](he), [秘密計算](mpc), **カテゴリ:** cs.CR, **投稿日時:** 2024-05-29 04:06

- - -

### [FlocOff: Data Heterogeneity Resilient Federated Learning with Communication-Efficient Edge Offloading](http://arxiv.org/abs/2405.18739)

**FlocOff: 通信効率の高いエッジオフロードを用いたデータ異質性に強い連合学習**

Mulei Ma, Chenyu Gong, Liekang Zeng, Yang Yang, Liantao Wu

- 異質なエッジデバイスにより、Non-IIDデータが連合学習の精度を低下させる。
- 従来の手法は適応メカニズムを使用するが、スケーラビリティや計算オーバーヘッドに課題がある。
- FlocOffは計算オフロードによるデータ再構成で、データ異質性とリソース制約を解決する。
- 実験結果で14.3%-32.7%のモデル精度向上とデータ異質性の低減が確認された。

FlocOff、連合学習の問題を新しい視点から解決してて面白いね！実用化が進むと、もっと効率の良いデバイス間の協力が期待できるかも。



**トピック:** [連合学習](fl), **カテゴリ:** cs.NI, eess.SP, **投稿日時:** 2024-05-29 03:53

- - -

### [Adaptive and Parallel Split Federated Learning in Vehicular Edge Computing](http://arxiv.org/abs/2405.18707)

**車両エッジコンピューティングにおける適応的かつ並列なスプリット連合学習**

Xianke Qiang, Zheng Chang, Yun Hu, Lei Liu, Timo Hamalainen

- 車両エッジインテリジェンス (VEI) はAIをエッジで活用し、将来のインテリジェント交通システムを支援する
- 連合学習（FL）は協調モデルのトレーニングとプライバシー保護を可能にするが、車両の多様性に適応できない
- スプリット学習（SL）はモデルの漏洩リスクを軽減し、車両のトレーニング負荷を軽減する
- 提案するASFVスキームは、モデルの分割とトレーニングの並列化により、トレーニング時間を大幅に短縮する

車が走りながらでもエッジで効率よく学習できるなんて、新しい未来って感じでワクワクするね！車のデータが漏れないように工夫されているのも安心でいいなって思ったよ！



**トピック:** [連合学習](fl), **カテゴリ:** cs.LG, cs.AI, cs.NI, **投稿日時:** 2024-05-29 02:34

- - -

### [Differentially-Private Distributed Model Predictive Control of Linear Discrete-Time Systems with Global Constraints](http://arxiv.org/abs/2405.18690)

**差分プライバシーを用いた線形離散時間システムの分散モデル予測制御におけるグローバル制約**

Kaixiang Zhang, Yongqiang Wang, Ziyou Song, Zhaojian Li

- 分散モデル予測制御(DMPC)は、システム制約を明示的に扱い、分散的に最適制御を達成するが、データ共有がプライバシーを侵害する。
- 従来の分散デュアル勾配アルゴリズムはDMPC問題を解決するが、強力なプライバシー保護はできない。
- 盗聴者に対するプライバシー保護のため、DMPCフレームワークに差分プライバシーのノイズ注入機構を組み込み、収束と$\epsilon$-差分プライバシーを両立。
- 閉ループシステムの再帰的な実現可能性と安定性を保証するDMPCの実装戦略を設計し、数値シミュレーションでその有効性を確認。

システムの制約を守りながらプライバシーも保護する仕組みってすごくない？これ、現場で使えるなら未来の制御システムに革命が起きちゃいそう！📈💡

**Comment:** 11 pages, 3 figures

**トピック:** [差分プライバシー](dp), **カテゴリ:** eess.SY, cs.SY, **投稿日時:** 2024-05-29 01:58

- - -

### [Adapting Differentially Private Synthetic Data to Relational Databases](http://arxiv.org/abs/2405.18670)

**リレーショナルデータベースへの差分プライバシー合成データの適用**

Kaveh Alimohammadi, Hao Wang, Ojas Gulati, Akash Srivastava, Navid Azizan

- 現行の差分プライバシー合成データ生成メカニズムは単一のソーステーブルを前提としているが、実際にはデータが複数のテーブルに分散している
- 本研究で初めて、既存の差分プライバシー手法と組み合わせて、リレーショナルデータベースを生成するアルゴリズムを紹介
- アルゴリズムは低次の周辺分布の近似誤差を最小化し、参照整合性を保ちながら個別の合成テーブル間の関係を反復的に修正する
- アルゴリズムには差分プライバシーと理論的な有用性保証が提供されている

実際のデータベースをリアルに模倣しつつプライバシーを守る手法が進化しているんだね。リレーショナルDBでの応用、データサイエンスや企業のデータ運用がもっと変わりそうな予感。



**トピック:** [合成データ](sd), **カテゴリ:** cs.LG, cs.CR, cs.DB, **投稿日時:** 2024-05-29 00:25

- - -

### [A Verifiable Computing Scheme for Encrypted Control Systems](http://arxiv.org/abs/2405.18586)

**暗号化制御システムのための検証可能な計算スキーム**

Francesca Stabile, Walter Lucia, Amr Youssef, Giuseppe Franze

- クラウドコンピューティングの普及により暗号化されたネットワーク制御システムが高性能で遠隔操作可能
- サードパーティのクラウドサービスプロバイダーで制御アルゴリズムが悪意のあるエージェントに変更される恐れ
- 従来の検証方法（ゼロ知識証明など）は計算負荷が高く、リアルタイム制御システムには非適用
- 提案する確率的カット・アンド・チューズアプローチに基づく新しい計算効率の高い検証可能な計算スキーム

これはめちゃくちゃおもしろそう！遠隔操作ロボットのリアルタイム性も考慮されてるし、実用性もありそうだよね。どんな風に現場で使われるか楽しみだなぁ。

**Comment:** Preprint of the manuscript submitted to the IEEE Control Systems   Letters (L-CSS)

**トピック:** [ゼロ知識証明](zkp), **カテゴリ:** eess.SY, cs.CR, cs.SY, **投稿日時:** 2024-05-28 21:06
