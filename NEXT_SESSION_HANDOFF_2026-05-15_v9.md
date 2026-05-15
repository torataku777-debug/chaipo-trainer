# チャイポ NEXT SESSION HANDOFF — 2026-05-15 v9

最終更新: 2026-05-16 00:30
前ハンドオフ: `NEXT_SESSION_HANDOFF_2026-05-15_v8.md`

---

## TL;DR

**Phase D-2 完了** (PLAY → home タブ切替、modeSelectButtons 廃止)。
Phase B-2 (IA v2 統合) → C-1 (開封演出 JS) → D-2 (動線切替) と 3 連続で完了。

次セッション候補: **C-2 (報酬獲得 → 所持タブ反映)** または **F-1 (プライバシーポリシー v1.1)**。
C-2 は仕様議論あり、F-1 はコード変更なしの文章作業。

---

## 直近完了 (Session 26 / 2026-05-15)

### Phase D-2: PLAY → home タブ切替

**目的**: IA v2 (home/town/battle/friend/more の 5 タブ) を正式動線に昇格させ、modeSelectButtons (6 ボタンオーバーレイ) を廃止。

**実装方針**: (A3) 動画再編集 + 動線切替 — 既に手元にあった `transition_to_home.mp4` (1.2 秒、タイトル → 街並みズーム → CHAIPO TOWN サイン) を採用。元の 6 ボタン用動画 (46.6 秒) は assets/ に残置 (ロールバック保険)。

**変更ファイル** (commit `7999a0a`):
- `dist/index.html`, `ios/App/App/public/index.html` (1,347,385 → 1,345,329 bytes、-2,056 bytes)
- `dist/assets/transition_to_home.mp4` 新規追加
- `ios/App/App/public/assets/transition_to_home.mp4` 新規追加
- `.gitignore` に `index_pre_*.html` 追加

**HTML 変更箇所 (5 patch をアトミック適用)**:

| # | 変更 | 行 |
|---|---|---|
| 1 | video src: `transition_to_mode_select.mp4` → `transition_to_home.mp4` | 12419 |
| 2 | modeSelectButtons 内の 6 ボタンを削除 (親 div は JS null チェック互換のため残置) | 12425 |
| 3 | onPlayClick フォールバック: `showScreen('mode-select')` → `showScreen('home')` | 19373 |
| 4 | endedHandler: loopVideo クロスフェード処理 → `showScreen('home')` + transitionLayer 非表示 | 19389-19401 |
| 5 | setTimeout フォールバック: 200+47000ms → 200+3000ms | 19407 |
| 6 | 2500ms 後の modeSelectButtons.is-active 付与を削除 | 19409 |
| 7 | loopVideo バックグラウンド再生処理を削除 | 19417 |

(#2 は HTML、#3〜7 は JS。アトミックパッチで全 5 箇所が pre/post flight 検証成功)

**動作確認** (実機 iPhone 15 Pro Max):
- ✅ PLAY → 1.2 秒遷移動画 → home タブ自動切替
- ✅ 2 回目以降の PLAY も同様に動作
- ✅ screen-game (実戦) 非リグレッション

**バックアップ**: `~/Desktop/claude/index_latest_pre_phaseD2_20260515_213044.html` (1,347,385 bytes)

---

## デッドコード (Phase D-1 で清掃予定)

D-2 で機能廃止したが、即削除すると差分が大きくロールバック判断を複雑化するため残置。

### CSS (残置)
- `.mode-select-buttons` (line 6787 周辺)
- `.vmode-btn-ai`, `.vmode-btn-fantasy`, `.vmode-btn-friend`, `.vmode-btn-online`, `.vmode-btn-data`, `.vmode-btn-settings`
- 関連サイズ: 約 5KB

### 動画ファイル (残置)
- `assets/transition_to_mode_select.mp4` (8.4 MB) — ロールバック保険
- `assets/transition_loop.mp4` (8.0 MB) — D-2 で参照されなくなった
- HTML 内の `<video id="transitionLoopVideo">` タグも残存

### JS (副作用なし)
- `modeButtons.classList.remove('is-active')` のリセット呼び出し
- `loopVideo` への null チェック付き参照

### Phase D-1 タスク (合計 ~16 MB 削減見込み)
1. CSS ブロック削除
2. 動画ファイル削除
3. `<video id="transitionLoopVideo">` タグ削除
4. JS の loopVideo / modeButtons 参照削除
5. `vmode-btn` を含む全 26 件の残骸チェック (CSS のみと思われる)

優先度は低い (動作上問題なし)。

---

## 次セッション候補

### 候補 1: Phase C-2 — 報酬獲得 → 所持タブ反映 (★仕様議論必要)

**目的**: 開封演出 (Phase C-1) でレアリティ抽選した報酬を、所持タブ (screen-town > collection) に反映。

**未確定の論点 5 軸**:

| 軸 | 選択肢 | Claude の推奨 |
|---|---|---|
| 報酬モデル | 固定リスト / プロシージャル生成 | **固定リスト** (v1.0 で十分) |
| 永続化 | localStorage / IndexedDB / Supabase | **localStorage で開始 → C-3 で Supabase 移行** |
| 既存 collection-grid | テンプレ維持 / 動的化 | **動的化** (静的 SVG とのデュアル構造を回避) |
| 重複時挙動 | 個数表示 / コイン変換 / 排他 | **個数表示** (経済設計未定義のためコイン保留) |
| 装備中スロット連動 | 即時反映 / 別画面 | **別画面** (所持タブに装備変更 UI 統合) |

**所要時間目安**: 1〜2 セッション。仕様議論で 1 セッション使う可能性。

### 候補 2: Phase F-1 — プライバシーポリシー v1.1 (★コード変更なし)

**目的**: Supabase 利用開示を含むプライバシーポリシーに更新。App Store 申請のブロッカー (ただし F-2 組織アカウント移行待ちのため緊急度低)。

**作業内容**:
- 既存 v1.0 の場所特定 (Desktop/claude/ 周辺要調査)
- 追記項目:
  - Supabase 利用 (Tokyo region `ap-northeast-1`)
  - 保存データ: 認証情報、対戦履歴、フレンド関係
  - 第三者送信: なし
  - 削除請求対応窓口
- 文章作業のみ、リスクなし

**所要時間目安**: 30 分〜1 時間。

### 候補 3: Phase D-1 — デッドコード清掃

D-2 で残置したコード/動画 16 MB 削減。優先度低、いつでも挿入可能。

### 候補 4: Phase C-3 — Supabase 永続化 (C-2 完了後)

C-2 で localStorage 実装した報酬データを Supabase に移行。複数デバイスでの所持品同期。

---

## 重要な技術メモ

### Python パッチの落とし穴 (今回発覚)

- `Filesystem:write_file` の出力 `len(s2)` は **Unicode コードポイント数** であって **バイト数ではない**
- 日本語が多い HTML だと実バイト数より小さく出る (今回 79KB の乖離)
- 実サイズは `os.path.getsize(HTML)` または `wc -c` で確認すること

### exact-string パッチでの空白の罠

- `endedHandler` パッチで OLD パターンの中の **空行 1 行を見落とし** → pre-flight 失敗
- 対処: 該当箇所を `sed -n` で抽出 → `Filesystem:read_text_file` で正確なバイト列確認 → パッチに反映
- 教訓: パッチ作成時は、コード読み取りでなく **必ず抽出して正確なバイト列を取得** すること

### osascript の戻り値の癖

- `xcrun devicectl device install` は stderr に "provisioning paramter list" 警告を出すが、これは正常動作
- osascript は stderr 出力 + 非ゼロ終了でエラー扱いになるため、`> log.txt 2>&1` でファイル経由が安全

### Wi-Fi 経由デバッグの不安定さ

- 同一 Wi-Fi でもデバイスが `unavailable` になることが頻繁にある
- 確実なのは **USB 直挿し**。Wi-Fi デバッグはトラブル時に時間を溶かす

### Personal Team の信頼設定

- アプリ再インストール後、起動時に `invalid code signature` エラー
- iPhone 側: 設定 → 一般 → VPNとデバイス管理 → デベロッパAPP → 信頼 が必須
- App Store 申請には Apple Developer Program (年額) 必要

---

## 確定済みの真実 (変更禁止)

- **真の本番 HTML**: `~/Desktop/claude/index_latest.html` (1,345,329 bytes / Phase D-2 適用後)
- `index_backup.html` (170KB) は Session 23 以前の古いバックアップ、絶対に使わない
- 同期先: `~/chaipo/dist/index.html` + `~/chaipo/ios/App/App/public/index.html` (copy_html.sh)
- iOS: bundle ID `com.torataku.chaipo` / iPhone 15 Pro Max (`790A0ABF-CF12-53F0-876B-6BA865407BEF`) + iPhone 16 (`F5E01DF1-BB4D-577E-B2AF-F8DB2012FB69`)
- Git: `~/chaipo/`, branch `ia-v2-redesign`, latest commit `7999a0a` (Phase D-2)
- screen-* 21 個
- Phase B ロールバック: `bash ~/Desktop/claude/rollback_phaseB.sh` (D-2 ロールバックは別途必要なら下記参照)

### Phase D-2 ロールバック方法

```bash
# HTML を Phase D-2 適用前に戻す
cp ~/Desktop/claude/index_latest_pre_phaseD2_20260515_213044.html ~/Desktop/claude/index_latest.html
bash ~/Desktop/claude/copy_html.sh

# Git 履歴で戻す
cd ~/chaipo && git revert 7999a0a
```

(動画 `transition_to_home.mp4` は残しておいて OK、参照されなくなるだけ)

---

## 次セッション開始のスニペット案

```
チャイポの次セッション開始。
ハンドオフ v9 を読んで現状把握から: ~/Desktop/claude/NEXT_SESSION_HANDOFF_2026-05-15_v9.md
Phase B-2 (IA v2) + C-1 (開封演出) + D-2 (PLAY→home 切替) 完了済み。
最新コミット: 7999a0a (ia-v2-redesign ブランチ)
本番 HTML: ~/Desktop/claude/index_latest.html (1.28MB)

次やりたいタスクを決めたい:
- C-2: 報酬獲得 → 所持タブ反映 (仕様議論あり、5 軸の判断必要)
- F-1: プライバシーポリシー v1.1 (Supabase 開示、コード変更なし)
- D-1: D-2 のデッドコード清掃 (~16 MB 削減、優先度低)

論点整理した上で判断したい。
```
