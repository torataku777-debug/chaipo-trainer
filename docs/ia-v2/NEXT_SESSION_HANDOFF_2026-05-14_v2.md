# NEXT SESSION HANDOFF — 2026-05-14 v2

前回: `archive/old_docs/NEXT_SESSION_HANDOFF_2026-05-14_v1.md`

---

## 今セッションの成果 (2026-05-14 後半)

**所持サブタブの視覚仕上げ完了**。これでぽむタウン三部作 (ガチャ / ショップ / 所持) が揃った。

| 画面 | 確定版 | 場所 |
|---|---|---|
| ぽむタウン > ガチャ | v3 | `docs/ia-v2/visual/pomu_town_gacha_v3.html` |
| ぽむタウン > ショップ | v5 (統合) | `docs/ia-v2/visual/pomu_town_v5.html` |
| ぽむタウン > 所持 | **v7** ★NEW | `docs/ia-v2/visual/pomu_town_v7.html` |
| ホーム | v2 | `docs/ia-v2/visual/pomu_home_v2.html` |

参考スクリーンショット (本セッション):
- `v6_collection_intermediate.png` / `v6_collection_bottom.png` — 所持タブ Claude 初稿
- `v7_collection_intermediate.png` / `v7_collection_bottom.png` — Codex 磨き後の確定版

---

## 所持サブタブの進化プロセス

```
v6  → Claude 初稿:
       装備中ストリップ(4枠) + フィルタチップ(5個) + 3列グリッド(15セル) + 進捗フッター
       状態: 通常 / 装備中(is-equipped 金枠+✓バッジ) / 未取得(is-locked グレースケール+鍵)
v7  → Codex 磨き:
       (1) フィルタチップ 5列等幅 grid、active を黄色グラデへ
       (2) 装備中ストリップに「EQUIPPED · 装備中」ピル型ゴールドバッジ、スロット下のオレンジドット
       (3) 装備中セルの金グロー強化(v3 is-ready パック並みに)
       (4) 春の桜サムネに花弁・桜の木、空気感アップ
       (5) リングサムネを水紋風の同心円(光輪)へ
       (6) 進捗フッターの「38」拡大、バーに金シャイン、外周グロー
       (7) 未取得鍵オーバーレイ:円グラデ + 太い線 + ゴールドシャックル
       ★ 確定
```

---

## このセッションで追加された知見

### 「ぽむタウン三部作」CG感の共通レシピが確立

1. **カード地**: `cloud-soft` → `cloud-white` の縦グラデ + 上端の白ハイライト + multi-shadow (4px + 1px 多層)
2. **ボタン**: 縦グラデ(`pomu-yellow` → `pomu-orange`) + 上端白ハイライト + 下端暗影 + 内側グロー
3. **状態差**:
   - `is-ready` / `is-equipped` = `--ready-glow-soft` の外周グロー + 上端金シャイン
   - `is-locked` = `saturate(0.4)` + 鍵オーバーレイ(円グラデ + ゴールドシャックル)
4. **装飾**: 空グラデ(`sky-100` → `sky-200`)+ 雲(楕円複数)
5. **アクセントラベル**: ピル型ゴールドバッジ (`SEASON 1 LIMITED` / `EQUIPPED · 装備中` 等)
6. **ぽむアバター**: PNG (`assets/pomu_pose_{1-7}.png`) を `<image>` または `<img>` で埋め込み、SVG手描き禁止

### Codex Brief の構造化が機能している

- 改善点を ★★★/★★/★ 優先度順 + 絶対制約セクションで分離
- 入力スクショに「現状(初稿)」「品質基準(参考)」の両方を入れる
- 出力ファイル名と完了基準のチェックリスト
- 1回の実行(約10分、20万トークン)で完成度の高い磨きが得られる

### ローカルプレビューのスクロール挙動 (備忘)

- `.device` は `min-height: 852px` で、コンテンツが増えると自動拡張する
- ブラウザでは `.screen-body` の `overflow-y: auto` が効かず、window全体がスクロールする
- 実機(Capacitor)では `.device` ラッパーが無いので、`.screen-body` の overflow-y が正しく効く想定

### Codex 投入パイプライン(再確認)

```
1. Claude 初稿(構造とトーンを確立)
2. CODEX_BRIEF_*.md(優先度順の改善点、絶対制約)
3. codex_prompt_*.txt(英語の簡潔な指示)
4. run_codex_*.sh で nohup 起動
5. 22秒間隔でポーリング(ファイルサイズ・ログ行数)
6. ファイルサイズ固定後 → 検証フェーズ → 完了サマリ(`/tmp/codex_final_*.txt`)
7. screencapture でスクショ → 評価 → 次へ
```

Codex CLI 設定:
- model: gpt-5.5, reasoning effort: xhigh, approval_policy: never (sandbox: workspace-write)
- 所要時間: 5〜15分(画像入力で reasoning が深くなる)
- ファイルサイズ固定後の検証フェーズは長い → kill して進めて良い

---

## 残作業 (次セッション)

### Phase A: 視覚仕上げ完了に向けて

1. **開封演出**(Phase C・ガチャ v3 の直系延長)
   - カード束モチーフを引き継ぐ
   - 開封アニメ + 報酬カード登場演出
2. **その他タブ**(設定 / 統計 / プロフィール詳細)
   - 軽い準備運動。確立済みトークンの応用
3. **フレンドタブ**(コミュニティ統合)
   - `COMMUNITY_ROADMAP.md` 参照
   - マイコード + 段位 + 称号バッジ、新しい部屋を作る(PRIMARY)、コードで参加、アクティビティフィード(LIVE)、フレンド一覧、対戦履歴
4. **対戦タブ**(BottomNav 中央・主役)
   - 仕様確定が前提(`HOME_SCREEN_SPEC.md` などへの依存なし)
   - ランクマッチ / カジュアル / AI対戦 / FL練習 の3段ヒエラルキー

**推奨順序**: 開封演出 → その他タブ → フレンドタブ → 対戦タブ
(対戦タブは仕様検討と並行)

### Phase B: 実機反映

- 各画面の確定版を `~/Desktop/claude/index_backup.html` に統合
- `screen-*` クラスの構造と整合
- Capacitor ビルド → iPhone 15 Pro Max に install

### Phase C: 開封演出画面

- ガチャパックを押すと開封アニメ
- v3 のカード束モチーフを継承
- アニメ + 報酬カード登場演出

---

## 主要ファイル位置

### 本セッションで追加 (Mac内ローカル)

```
~/Desktop/claude/
├── NEXT_SESSION_HANDOFF_2026-05-14_v2.md  ★本ファイル
├── codex_prompt_collection_v2.txt
├── run_codex_collection_v2.sh
└── archive/old_docs/
    └── NEXT_SESSION_HANDOFF_2026-05-14_v1.md  (旧版退避)

~/Desktop/claude/codex_handoff/
├── CODEX_BRIEF_COLLECTION_V2.md
└── visual/
    ├── pomu_town_v6.html                 (初稿、参考用)
    ├── pomu_town_v7.html                  ★所持確定版
    ├── v6_collection_intermediate.png
    ├── v6_collection_bottom.png
    ├── v7_collection_intermediate.png     ★
    └── v7_collection_bottom.png           ★
```

### 本セッションで追加 (Git管理下: chaipo)

```
~/chaipo/docs/ia-v2/
├── NEXT_SESSION_HANDOFF_2026-05-14_v2.md  ★本ファイル
├── CODEX_BRIEF_COLLECTION_V2.md            ★
└── visual/
    ├── pomu_town_v7.html                    ★所持確定版
    ├── v7_collection_intermediate.png       ★
    └── v7_collection_bottom.png             ★
```

---

## 状態スナップショット

- **git ブランチ**: `ia-v2-redesign`
- **コミット予定**: 所持サブタブ v7 確定 + ハンドオフ v2
- **iPhone デバイスID**: `790A0ABF-CF12-53F0-876B-6BA865407BEF`
- **本番HTML**: 未更新(視覚版はプロトタイプ、本体は `~/Desktop/claude/index_backup.html` のまま)
- **ローカルサーバー**: localhost:8765 稼働中

---

## 次セッション開始のスニペット

```
ハンドオフを読んで、視覚仕上げの残作業に進もう。
ぽむタウン三部作(ガチャv3 / ショップv5 / 所持v7)と ホーム(v2)完成。
次の候補: 開封演出、その他タブ、フレンドタブ、対戦タブ。
```

---

**End of Handoff v2**
