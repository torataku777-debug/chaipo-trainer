# NEXT SESSION HANDOFF — 2026-05-14 v3

前回: `archive/old_docs/NEXT_SESSION_HANDOFF_2026-05-14_v2.md`

---

## 今セッションの成果 (2026-05-14 後半 〜 夜)

**視覚仕上げ Phase A & C の主要画面が完成**。IA v2 視覚版の屋台骨が揃った。

| 画面 | 確定版 | コミット |
|---|---|---|
| ぽむタウン > ガチャ | v3 | (前々セッション) |
| ぽむタウン > ショップ | v5 (統合) | (前々セッション) |
| ぽむタウン > 所持 | **v7** | dfb8100 (本セッション) |
| ホーム | v2 | (前々セッション) |
| **開封演出**(ガチャ → 開封) | **v2** | 94ef239 (本セッション) |

参考スクリーンショット (本セッション):
- 所持: `v6_collection_intermediate.png` / `v6_collection_bottom.png` (初稿) ; `v7_collection_intermediate.png` / `v7_collection_bottom.png` (確定版)
- 開封演出: `v1_opening_{intro,reveal_r,reveal_sr,complete}.png` (初稿) ; `v2_opening_{intro,reveal_r,reveal_sr,complete}.png` (確定版)

---

## 開封演出の進化プロセス

```
v1  → Claude 初稿:
       4ステージステートマシン(intro / animating / reveal / complete)
       報酬カード5枚(朝霧N, 夕焼けR, 星空R, 渋谷ナイトSR, 桜並木SR)
       レアリティ3段(N/R/SR)、進捗ドット、デモ切替バー、暗背景

v2  → Codex 磨き:
       (1) intro パック: 大型化 + 二段金グロー + 金粒 + テキストグロー
       (2) animating: 多層フラッシュ + 放射光線 + 波紋リング + 16粒子 + 3段階パック飛散
       (3) reveal カード絵5枚を精細化(光輪・奥行き・空気感・看板等)
       (4) SR 特別演出: 二重金縁 + 金パーティクル + 虹色アクセント + バッジスパークル + 登場時星弾け
       (5) complete: confetti + ミニパックアイコン + サムネ強グロー(SR) + もう一回ボタン強グロー
       (6) 進捗ドット脈動 + 戻るボタンガラス感
       ★ 確定 (commit 94ef239)
```

---

## このセッションで追加された知見

### 開封演出パターンの確立

- **暗背景 + ステートマシン**(`data-stage="intro|animating|reveal|complete"`)で全シーンを 1HTML に集約できる
- **デモ用ステート切替バー** を画面外に置くことで、プロトタイプの確認効率が大幅アップ
- **レアリティ別差別化**(N/R/SR)は box-shadow の多層化と色味で表現可能
  - N: グレー、控えめ
  - R: シアン枠 + 控えめなグロー
  - SR: **金二重縁** + 強グロー + パーティクル + 虹色アクセント
- ポケポケ的「暗→光→報酬」のドラマは、放射光線 + 波紋リング + パーティクルの組み合わせで再現

### Codex 投入の信頼度向上

- 改善点を ★優先度順 + 絶対制約セクションに分離した BRIEF は、Codex の出力品質を大きく上げる
- 1回(10〜15分、20〜30万トークン)で 5〜7 項目すべてに対応可能
- ファイル数:1 BRIEF + 1 prompt + 1 run script(テンプレート踏襲で短時間で量産)

### Chrome MCP の挙動メモ

- `Control Chrome:execute_javascript` は **isolated world** なので page-level 関数(`setStage` 等)を直接呼べない
  - 解決: DOM 経由(`document.querySelector('.demo-btn[...]').click()`)で操作
- スクショは AppleScript の `Google Chrome` を frontmost にしてから `screencapture -R` で撮影

---

## 残作業 (次セッション)

### Phase A: 視覚仕上げ完了に向けて(残3画面)

1. **その他タブ**(設定 / 統計 / プロフィール詳細)
   - 軽い準備運動。確立済みトークンの応用
   - 構造: プロフィール / ゲーム(戦績・ランキング) / 設定(時間/初期点/ハプティック/カードデザイン) / サポート(ルール・お知らせ・お問い合わせ・規約) / ログアウト・バージョン

2. **フレンドタブ**(コミュニティ統合)
   - `COMMUNITY_ROADMAP.md` 参照
   - 構造: マイコード + 段位 + 称号バッジ / 新しい部屋を作る(PRIMARY) / コードで参加 / アクティビティフィード(LIVE) / フレンド一覧(オンライン状態) / 対戦履歴 + シェアボタン

3. **対戦タブ**(BottomNav 中央・主役)
   - 仕様確定が前提。`HOME_SCREEN_SPEC.md` などへの依存なし
   - 構造: ランクマッチ(主役・3px枠) / カジュアル(副) / AI対戦(補助・モーダル) / FL練習(補助・モーダル)
   - **注意**: フレンド対戦は含まない(Q1決定済み)

4. **統合ビュー**(任意)
   - 5タブ切替の `pomu_app_v1.html`

推奨順序: **その他タブ → フレンドタブ → 対戦タブ → 統合ビュー(任意)**
(対戦タブは仕様検討と並行で最後)

### Phase B: 実機反映

- 確定版各画面を `~/Desktop/claude/index_backup.html` に統合
- `screen-*` クラスの構造と整合
- Capacitor ビルド → iPhone 15 Pro Max(`790A0ABF-CF12-53F0-876B-6BA865407BEF`)に install

### Phase C: 開封演出からの実機統合(完了済み視覚版)

- 開封演出 v2 を `index_backup.html` のガチャフローに繋ぐ
- 「無料で開ける / 100コイン」ボタン → 開封演出画面遷移
- 報酬データを Supabase 連携(別途課題)

---

## 主要ファイル位置

### 本セッションで追加 (Mac内ローカル)

```
~/Desktop/claude/
├── NEXT_SESSION_HANDOFF_2026-05-14_v3.md  ★本ファイル
├── codex_prompt_collection_v2.txt
├── run_codex_collection_v2.sh
├── codex_prompt_opening_v2.txt
├── run_codex_opening_v2.sh
└── archive/old_docs/
    ├── NEXT_SESSION_HANDOFF_2026-05-14_v1.md
    └── NEXT_SESSION_HANDOFF_2026-05-14_v2.md

~/Desktop/claude/codex_handoff/
├── CODEX_BRIEF_COLLECTION_V2.md
├── CODEX_BRIEF_OPENING_V2.md  ★NEW
└── visual/
    ├── pomu_town_v6.html
    ├── pomu_town_v7.html
    ├── v6_collection_intermediate.png / v6_collection_bottom.png
    ├── v7_collection_intermediate.png / v7_collection_bottom.png
    ├── pomu_pack_opening_v1.html  ★NEW
    ├── pomu_pack_opening_v2.html  ★NEW
    ├── v1_opening_intro.png / v1_opening_reveal_r.png / v1_opening_reveal_sr.png / v1_opening_complete.png  ★NEW
    └── v2_opening_intro.png / v2_opening_reveal_r.png / v2_opening_reveal_sr.png / v2_opening_complete.png  ★NEW
```

### 本セッションで追加 (Git管理下: chaipo)

```
~/chaipo/docs/ia-v2/
├── NEXT_SESSION_HANDOFF_2026-05-14_v3.md  ★本ファイル
├── CODEX_BRIEF_COLLECTION_V2.md  (commit dfb8100)
├── CODEX_BRIEF_OPENING_V2.md     (commit 94ef239)
└── visual/
    ├── pomu_town_v7.html                       (commit dfb8100)
    ├── v7_collection_{intermediate,bottom}.png (commit dfb8100)
    ├── pomu_pack_opening_v{1,2}.html           (commit 94ef239)
    └── v{1,2}_opening_{intro,reveal_r,reveal_sr,complete}.png (commit 94ef239)
```

---

## 状態スナップショット

- **git ブランチ**: `ia-v2-redesign`
- **最新コミット**:
  - `dfb8100` ぽむタウン > 所持サブタブ v7 確定
  - `94ef239` ガチャ開封演出 v2 確定 (Phase C 完成)
- **iPhone デバイスID**: `790A0ABF-CF12-53F0-876B-6BA865407BEF`
- **本番HTML**: 未更新(視覚版はプロトタイプ、本体は `~/Desktop/claude/index_backup.html` のまま)
- **ローカルサーバー**: localhost:8765 稼働中

---

## 次セッション開始のスニペット

```
ハンドオフを読んで、視覚仕上げの残作業に進もう。
完了: ガチャv3 / ショップv5 / 所持v7 / ホームv2 / 開封演出v2。
次の候補: その他タブ、フレンドタブ、対戦タブ(仕様確認必要)、統合ビュー。
```

---

**End of Handoff v3**
