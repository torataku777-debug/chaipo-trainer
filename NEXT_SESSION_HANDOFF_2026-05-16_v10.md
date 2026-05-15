# チャイポ NEXT SESSION HANDOFF — 2026-05-16 v10

最終更新: 2026-05-16 (Session 26 完全終了時点)
前ハンドオフ: `NEXT_SESSION_HANDOFF_2026-05-15_v9.md`

---

## TL;DR

Session 26 で **Phase D-2** (PLAY → home タブ切替) 完了に加え、**プロジェクトドキュメント構造を全面刷新**。claude.ai Project に 6 ファイル (00_INDEX 〜 05_CURRENT_STATE) を新規配置し、旧 OFC_PROJECT 系を全廃。**F-1 (プライバシーポリシー) の実態判明** — ローカルは v2 で Supabase 開示済み、真の課題は GitHub Pages 公開リポジトリ (`ofc-neighbors-privacy`) が 404 (リポ未作成)。F-2 (組織アカウント移行) 完了まで保留判断。

次セッション候補: **D-1 (Cowork で検証案あり)** / **C-2 (Chat で仕様議論)** / **F-1 公開リポ整備 (F-2 後で OK)**。

---

## Session 26 完了事項

### 1. Phase D-2: PLAY → home タブ切替 (commit `7999a0a`)

- 動画 src 変更: `transition_to_mode_select.mp4` (46.6s) → `transition_to_home.mp4` (1.2s)
- modeSelectButtons 内の 6 ボタン削除 (親 div は JS null 互換のため残置)
- `onPlayClick` の 5 箇所改修 (フォールバック先 'home'、endedHandler で showScreen('home')、setTimeout 47s → 3s、ボタン有効化削除、loopVideo 再生削除)
- 実機動作確認済 (iPhone 15 Pro Max)
- HTML 1,347,385 → 1,345,329 bytes (-2,056)
- バックアップ: `index_latest_pre_phaseD2_20260515_213044.html`

### 2. F-1 実態判明 (実質完了扱い)

- ローカル `~/chaipo/docs/privacy/index.html` は **v2 で Supabase 開示済み** (2026-04-27 改定済)
- README が「fully offline」のまま (v1.0 内容)
- 公開先 `https://torataku777-debug.github.io/ofc-neighbors-privacy/` は **404** (リポジトリ自体未作成)
- 結論: F-2 (組織アカウント移行) 完了まで保留。App Store 申請直前にまとめて公開リポ整備

### 3. プロジェクトドキュメント全面刷新

claude.ai Project に新ドキュメント構造を配置:

| ファイル | 役割 |
|---|---|
| `00_INDEX.md` | 目次・読み順 |
| `01_GAME_SPEC.md` | OFC ルール・FL・戦術定石 |
| `02_TECH_STACK.md` | デプロイ・Python パッチ・MCP の癖 |
| `03_BRAND_SUMMARY.md` | ブランド要約 (フルは Mac 側) |
| `04_WORKFLOW.md` | セッション運用・タブ振り分け |
| `05_CURRENT_STATE.md` | 現状・Phase 進捗・次タスク |

廃止 (claude.ai Project から削除):
- `OFC_PROJECT.md` (v18、古い)
- `OFC_PROJECT_v4.md` (4/6、新構造に統合済)
- `TASKS_2026-04-06.md` (古いバグ追跡)
- `NEXT_PROMPT_2026-04-06.md` (古い別チャット用)
- `Claude.pdf` (3/30 印刷スナップショット)

### 4. メモリ整理

旧 4 件 → 新 3 件構成 (二重管理解消、ポインター中心):
- #1: プロジェクト基本 + 新セッション読み順
- #2: 常設 MD 構造案内 + Phase 体系の二系統注意
- #3: 創作素材ルール + 画像転送ノウハウ

### 5. タブ振り分け運用の確立

Max plan の 3 タブ (Chat / Cowork / Code) について、現実的な振り分け基準を確立:
- 仕様議論・対話判断・画像生成 → Chat
- 機械的実行 (パッチ・ビルド連続) → Cowork (プロンプト生成 → 手動切替)
- 大規模リファクタ・Git 横断 → Code
- 「自動振り分け実行」は不可、Chat から Cowork/Code プロンプトを出して虎谷さんが手動移譲

詳細は `04_WORKFLOW.md` セクション 3。

---

## 直近のタスク候補 (優先順)

### 候補 1: Phase D-1 — デッドコード清掃 (★ Cowork 検証案あり)

**目的**: Phase D-2 で死蔵化したコード・動画を削除 (~16 MB 削減)。

**削除対象**:
- HTML: `<video id="transitionLoopVideo">`、空の `<div id="modeSelectButtons">`
- CSS: `.mode-select-buttons`, `.vmode-btn-*` 一式
- 動画: `transition_to_mode_select.mp4` (8.4 MB × 2)、`transition_loop.mp4` (8.0 MB × 2)

**特徴**: 仕様議論ゼロ、機械的実行、結果検証明確
**推奨**: **Cowork に出す**。これが Cowork タブ運用の初実証ケース。

### 候補 2: Phase C-2 — 報酬獲得 → 所持タブ反映 (★仕様議論必要)

**5 軸の論点 (Claude の推奨)**:
| 軸 | 推奨 |
|---|---|
| 報酬モデル | 固定リスト |
| 永続化 | localStorage で開始 (将来 C-3 で Supabase) |
| 既存 collection-grid | 動的化 |
| 重複時挙動 | 個数表示 |
| 装備中スロット連動 | 別画面で装備変更 UI |

**推奨**: **Chat で進める**。1〜2 セッション。

### 候補 3: Phase F-1 — プライバシーポリシー公開リポ整備

**現状**: ローカル v2 (Supabase 開示済) は完成、公開先 404。

選択肢:
- (α) F-2 完了まで保留 (推奨、App Store 申請時に公開先 URL が必要になる時点でまとめて対応)
- (β) 今 GitHub リポジトリ作成 + Pages 設定 (`gh` CLI 未インストール、虎谷さん手動操作必須)

---

## 確定済みの真実 (変更禁止)

- 本番 HTML: `~/Desktop/claude/index_latest.html` (1,345,329 bytes / Phase D-2 適用後)
- 同期先: `~/chaipo/dist/index.html` + `~/chaipo/ios/App/App/public/index.html` (`copy_html.sh`)
- iOS: bundle ID `com.torataku.chaipo` / iPhone 15 Pro Max (`790A0ABF-CF12-53F0-876B-6BA865407BEF`) + iPhone 16 (`F5E01DF1-BB4D-577E-B2AF-F8DB2012FB69`)
- Git: `~/chaipo/`, branch `ia-v2-redesign`, latest commit `507c46e` (Session 26 ハンドオフ反映)
- 直近の Phase コミット: `7999a0a` (Phase D-2 完了)
- screen-* 21 個
- Phase D-2 ロールバック: `index_latest_pre_phaseD2_20260515_213044.html`
- Phase B 以前のロールバック: `bash ~/Desktop/claude/rollback_phaseB.sh`

---

## 新ドキュメント構造下での運用ルール

### 新セッション開始時の Claude の動き

1. claude.ai Project の `05_CURRENT_STATE.md` を最初に読む
2. Mac 側の最新ハンドオフ (`NEXT_SESSION_HANDOFF_2026-05-16_v10.md` 等) を読む
3. 必要に応じて他の Project MD を参照 (`02_TECH_STACK.md` for デプロイ、`04_WORKFLOW.md` for 運用)
4. 現状把握を冒頭で簡潔に報告

### Phase 完了時の更新範囲

- `05_CURRENT_STATE.md` を更新 (最新 Phase、commit、次候補)
- ハンドオフ v(N+1) を作成
- メモリ更新 (新セッション開始の道標として最低限)
- 旧ハンドオフを `archive/old_docs/` に退避

---

## 次セッション開始のスニペット案

```
チャイポの次セッション開始。
プロジェクト MD (05_CURRENT_STATE.md) と 最新ハンドオフ v10 を読んで現状把握から:
~/Desktop/claude/NEXT_SESSION_HANDOFF_2026-05-16_v10.md

Phase D-2 (PLAY→home 切替) 完了。最新コミット: 507c46e (ia-v2-redesign)
本番 HTML: ~/Desktop/claude/index_latest.html (1.28 MB)

次やるタスクを決めたい:
- D-1: デッドコード清掃 (Cowork で検証ケース、~16MB 削減)
- C-2: 報酬獲得 → 所持タブ反映 (5 軸の仕様議論あり、Chat 向き)
- F-1: 公開リポ整備 (F-2 後で OK の判断あり、優先度低)

論点整理した上で判断したい。
```

---

## Session 26 で得た技術的学び (再掲)

### Python の `len(str)` ≠ バイト数

日本語多めの HTML で `len(s2)` が実バイト数より 79KB 小さく出る現象を確認。
**実サイズ確認は必ず `os.path.getsize()` or `wc -c`**。

### exact-string パッチでの空白の罠

`endedHandler` パッチで OLD パターン内の空行 1 行を見落として pre-flight 失敗。
**対処**: 該当箇所を `sed -n` で抽出 → Filesystem MCP で正確なバイト列確認 → パッチに反映。
**教訓**: パッチ作成時は、コード読み取りでなく **必ず抽出して正確なバイト列を取得**。

### osascript の戻り値の癖

`xcrun devicectl device install` は stderr に "provisioning paramter list" 警告を出すが正常動作。
osascript は stderr 出力 + 非ゼロ終了でエラー扱いになるため、`> log.txt 2>&1` でファイル経由が安全。

### Wi-Fi 経由デバッグの不安定さ

同一 Wi-Fi でも `unavailable` になることが頻繁。**USB 直挿しが圧倒的に確実**。

### Personal Team の信頼設定

アプリ再インストール後、起動時に `invalid code signature` エラー。
iPhone 側: 設定 → 一般 → VPN とデバイス管理 → デベロッパ APP → 信頼 が必須。

### F-1 で判明した GitHub Pages 公開先の状態

- ローカル `~/chaipo/docs/privacy/index.html` (chaipo-trainer リポ内) は v2 で完成
- 公開先リポ `torataku777-debug/ofc-neighbors-privacy` は **GitHub 上に存在しない** (404)
- README の "fully offline" 記載が v1.0 のまま
- App Store 申請時 (F-2 後) に公開リポ作成 + Pages 設定が必要
