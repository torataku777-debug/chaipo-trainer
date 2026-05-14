# NEXT SESSION HANDOFF — 2026-05-15 v6

前回: `archive/old_docs/NEXT_SESSION_HANDOFF_2026-05-15_v5.md`

---

## 今セッションの成果 (2026-05-15)

**Phase A (視覚仕上げ) 完了**。IA v2.2 の Q1 判断を更新 (フレンド対戦を対戦タブに含める) し、最後の 1 画面「対戦タブ」を v2 まで磨き上げた。フレンドタブも v3 に改訂。

| 画面 | 確定版 | コミット |
|---|---|---|
| ぽむタウン > ガチャ | v3 | (前々セッション) |
| ぽむタウン > ショップ | v5 (統合) | (前々セッション) |
| ぽむタウン > 所持 | v7 | dfb8100 |
| ホーム | v2 | (前々セッション) |
| 開封演出(ガチャ → 開封) | v2 | 94ef239 |
| その他タブ | v2 | 61991e8 |
| フレンドタブ | v2 → v3 | e84369e → **a9f41f7** |
| **対戦タブ** | **v2** | **a9f41f7 (本セッション)** |

**Phase A の 8 画面 (ガチャ / ショップ / 所持 / ホーム / 開封演出 / その他 / フレンド / 対戦) がすべて確定品質に到達。**

---

## IA v2.2 Q1 判断の更新

前回までの Q1 決定:
> 対戦タブにフレンド対戦は含まない (フレンドタブ側で完結)

本セッションでの更新:
> 対戦タブに**フレンド対戦を含める**。フレンドタブから「新しい部屋を作る」「コードで参加」を削除し、対戦タブの副タイルへ移管。

理由:
- 「対戦動線は全部対戦タブで完結」のほうがユーザーの心地よさが高い
- フレンドタブを「社交・履歴」に純化することで役割が明確化
- 練習機能 (AI 対戦 / FL 練習) も「対戦タブの練習セクション」に集約

---

## 対戦タブ v1 → v2 の進化プロセス

```
v1  → Claude 初稿:
       4 セクション構成:
         (1) battle-header  : タイトル「対戦」 + 右上「S3 残り 12日」ピル
         (2) rank-card      : 主役・3px 金枠
                              - "★ RANKED MATCH" キャプション
                              - rank-shield (盾チェックアイコン) + 段位「プラチナ 3」
                              - レート「1,247」 + 直近 "+24" 緑バッジ
                              - "プラチナ 4 まで 253 / 400" プログレスバー (63%)
                              - "マッチング開始" PRIMARY CTA (黄色グラデ + ⚔)
         (3) mode-grid      : 2 カラム並列・副
                              - カジュアル (シアン顔, "レート変動なし / 気軽に対戦")
                              - フレンド対戦 (紫人物, "部屋を作る / コードで参加")
         (4) practice-card  : 練習セクション
                              - AI 対戦 (シアンロボット, "2 人 / 3 人(近日) ・ レベル選択可")
                              - FL 練習 (金色王冠, "ファンタジー練習" + "14/15/16/17 枚 ・ EV 表示")
       新規パターン: rank-card (3px gradient border via CSS mask trick) / rank-shield /
                    rank-progress / mode-grid 2-col tile / practice-row
       Claude 自身が dev-note に Codex 改善ポイント 6 件を残した

v2  → Codex 磨き (gpt-5.5 xhigh, ~7 min):
       ★★★ rank-card 7-stop 金色グラデ枠 + warmer inset + 外側 gold halo で中央タブの主役感
       ★★★ rank-shield 3 段 radial + double edge ring + 3 sparkles + stroke 2.4
       ★★★ progress bar: 9px 高, inset shimmer, 右端 glow point, 横に金色ミニ星, tab-nums
       ★★ mode-tile 差別化: casual=cyan glow / friend=purple glow + plus overlay + corner radial
       ★★ rank-cta: 18px + 0.08em + min-height 60 + +1px press depth
       ★★ season pill: cyan→cloud bg + inset highlight + "12日" orange 強調
       ★ 練習行アイコン洗練 (AI 目内ハイライト, FL 王冠 base+gem, stroke 2.2)
       ★ "ファンタジー練習" inline mini-badge 化
       ★ SVG stroke 統一 (nav 2 / hero 2.4 / mode 2)
       Codex 自身が Nokogiri parse + 構造維持確認 + インライン JS 実行で validation
       ★ 確定 (commit a9f41f7)
```

---

## フレンドタブ v2 → v3 の構造改訂

```
v2 (room-actions あり) → v3 (room-actions 削除):
  削除:
    .room-actions section (新しい部屋を作る + コードで参加)
    → 対戦タブの「フレンド対戦」副タイルに移管
  維持:
    profile-card / activity-feed (LIVE) / friend-list / history-list
    friend-list 内の招待ボタン ⚔ SVG (将来の動線として)
  メタコメント / dev-note を v3 用に書き直し

  全 v2 ビジュアル品質 (PRIMARY CTA gold, LIVE glow, activity event tags, etc.) は影響なし
```

---

## このセッションで追加された知見

### Codex 投入後の自己 validation の利用

その他タブ v2 / フレンドタブ v2 までは Codex がパッチを当てて終了するだけだったが、対戦タブ v2 では Codex 自身が:
- Nokogiri::HTML5 パース
- 構造維持確認 (`.rank-card`, `.mode-grid`, `.practice-card`, `.bottom-nav` の数を check)
- インライン JS のDOMスタブ実行
を行った後にfinalize する流れに進化。Chrome ヘッドレスは sandbox で拒否されるが、Nokogiri レベルの構造確認だけで十分な信頼性が得られる。

### スクショ撮影フローのハマりどころ

Chrome 内で別タブ (claude.ai 等) がアクティブのままだと `screencapture -R` は背面のアプリ (claude.ai デスクトップ等) を撮ってしまう。対策:

```applescript
tell application "System Events"
  set frontmost of process "Google Chrome" to true
end tell
```

を `tell application "Google Chrome" to activate` の後に追加して **強制最前面化** する。これでアクティブタブ内容が確実に撮れる。

### 一時ファイルとリバートの判断

`git status -s` で `M` が出たら、それは前のコミットで既にトラッキング済みのファイルが上書きされたサイン。今回 sips でリサイズして上書きした v2_more_*.png は意図しない差分扱いだったので `git checkout --` でリバート。new file (`A`) と意図的な modify を区別して扱う運用が定着。

---

## 残作業 (次セッション以降)

### Phase A 補足 (任意・優先度低)

| # | タスク | 優先度 | 所要 |
|---|---|---|---|
| A-3 | 統合ビュー `pomu_app_v1.html` (5 タブ切替を1ファイルで) | 🟢 低 | 30-60 分 |

5 タブすべてのプレビューを1ファイルにまとめる任意作業。Phase B 開始前のチェックポイントとして有用だが、本番 HTML 統合 (Phase B) が始まれば自然に不要になる。

### Phase B: 実機反映 (主要作業)

| # | タスク | 優先度 | 所要 |
|---|---|---|---|
| B-1 | 視覚版 8 画面を `index_backup.html` の `screen-*` 構造に統合 | 🔴 高 | 約 3-4 時間 |
| B-2 | Capacitor ビルド + iPhone 15 Pro Max install で動作確認 | 🔴 高 | 30 分 |
| B-3 | スクリーン間遷移の動作確認 (BottomNav タップ、サブタブ切替) | 🟡 中 | 30 分 |

**B-1 統合対象**:

| 視覚版 | → | 本番 screen 名 |
|---|---|---|
| `pomu_home_v2.html` | → | `screen-home` |
| `pomu_town_gacha_v3.html` | → | `screen-town` (ガチャサブタブ) |
| `pomu_town_v5.html` | → | `screen-town` (ショップサブタブ) |
| `pomu_town_v7.html` | → | `screen-town` (所持サブタブ) |
| `pomu_battle_v2.html` | → | `screen-battle` |
| `pomu_friend_v3.html` | → | `screen-friend` |
| `pomu_more_v2.html` | → | `screen-more` |
| `pomu_pack_opening_v2.html` | → | `screen-pack-opening` (ガチャから遷移) |

**B-1 の制約** (ユーザーの指示「ゲーム体験は変えない」):
- ❌ **触らない**: `screen-game` (カード配置・ジョーカー評価・FL 判定・ファウル判定・スコア計算)
- ❌ **触らない**: オンライン対戦の Supabase Realtime 同期ロジック
- ❌ **触らない**: FL 最適化 (`fl_optimizer/` の Phase α/β/γ)
- ❌ **触らない**: チュートリアル T-0 スケルトン (Session 25 実装)
- ✅ **触る**: BottomNav の 5 タブ構造、各タブのスクリーン HTML/CSS、遷移ロジック、ガチャ→開封演出のフロー

### Phase C: 開封演出フロー接続

| # | タスク | 優先度 | 所要 |
|---|---|---|---|
| C-1 | ガチャ「無料で開ける / 100 コイン」 → `screen-pack-opening` 遷移 | 🔴 高 | 1 時間 |
| C-2 | 開封演出 → 報酬獲得 → 所持タブ反映 | 🟡 中 | 1-2 時間 |
| C-3 | Supabase 連携 (報酬データ永続化) — **保留** | 🟢 低 | 後日課題 |

### フォローアップ (リリース前)

| # | タスク | 優先度 | 所要 |
|---|---|---|---|
| F-1 | プライバシーポリシー v1.1 更新 (Supabase 利用開示) | 🟡 中 | 30 分 |
| F-2 | App Store 申請戦略 (個人 → 組織アカウント移行) | 🟢 低 | 別件 |
| F-3 | スクリーンショット撮影 (App Store 用) | 🟢 低 | B-2 完了後 |

---

## 推奨実行順序

```
[Session 28] (任意)
  A-3 (~30-60 min) 統合ビュー pomu_app_v1.html
                   → 飛ばして Phase B 直行も可

[Session 28-29]
  B-1 (~3-4 hr) 視覚版 8 画面を index_backup.html へ統合
                ※ screen-game / オンライン対戦 / FL 最適化は触らない
  B-2 (~30 min) Capacitor ビルド + iPhone install
  B-3 (~30 min) 動作確認

[Session 30]
  C-1 (~1 hr)   ガチャ → 開封演出フロー接続
  C-2 (~1-2 hr) 報酬 → 所持タブ反映

[Session 31+]
  F-1, F-2, F-3 リリース準備
```

---

## 主要ファイル位置

### 本セッションで追加 (Mac 内ローカル)

```
~/Desktop/claude/
├── NEXT_SESSION_HANDOFF_2026-05-15_v6.md  ★本ファイル
├── codex_prompt_battle_v1.txt             ★NEW
├── run_codex_battle_v1.sh                 ★NEW
├── s27_friend_v3_strip_rooms.py           ★NEW (フレンド v3 生成スクリプト)
├── .commit_msg_battle_v2.txt              ★NEW (Git コミットメッセージ)
└── archive/old_docs/
    └── NEXT_SESSION_HANDOFF_2026-05-15_v5.md  ★移動

~/Desktop/claude/codex_handoff/
├── CODEX_BRIEF_BATTLE_V1.md   ★NEW
└── visual/
    ├── pomu_friend_v3.html    ★NEW (room-actions 削除版)
    ├── pomu_battle_v1.html    ★NEW (Claude 初稿)
    ├── pomu_battle_v2.html    ★NEW (Codex 確定版)
    ├── v3_friend_{top,middle,bottom}.png  ★NEW
    ├── v1_battle_{top,bottom}.png         ★NEW
    └── v2_battle_top.png                  ★NEW
```

### 本セッションで追加 (Git 管理下: chaipo)

```
~/chaipo/docs/ia-v2/
├── CODEX_BRIEF_BATTLE_V1.md                       (commit a9f41f7)
└── visual/
    ├── pomu_friend_v3.html                        (commit a9f41f7)
    ├── pomu_battle_v1.html                        (commit a9f41f7)
    ├── pomu_battle_v2.html                        (commit a9f41f7)
    ├── v3_friend_{top,middle,bottom}.png          (commit a9f41f7)
    ├── v1_battle_{top,bottom}.png                 (commit a9f41f7)
    └── v2_battle_top.png                          (commit a9f41f7)
```

---

## 状態スナップショット

- **git ブランチ**: `ia-v2-redesign`
- **最新コミット**:
  - `61991e8` その他タブ v2 確定 (Phase D 開始)
  - `cb94a4a` その他タブ v2 ハンドオフ + BRIEF 追加
  - `e84369e` フレンドタブ v2 確定 (Codex 改善版)
  - `0a11636` docs: ハンドオフ v5 追加
  - **`a9f41f7` 対戦タブ v2 + フレンドタブ v3 確定 (Phase A 完了) ← 本セッション**
- **iPhone デバイス ID**: `790A0ABF-CF12-53F0-876B-6BA865407BEF`
- **本番 HTML**: 未更新 (視覚版はプロトタイプ、本体は `~/Desktop/claude/index_backup.html` のまま)
- **ローカルサーバー**: `localhost:8765` 稼働中
  (cwd: `~/Desktop/claude/codex_handoff/visual`, PID 33251)

---

## 次セッション開始のスニペット

```
ハンドオフ v6 を読んで、Phase B (実機反映) に進もう。
Phase A の 8 画面 (ガチャv3/ショップv5/所持v7/ホームv2/開封演出v2/その他v2/フレンドv3/対戦v2) を
index_backup.html の screen-* 構造に統合。
ゲーム体験 (screen-game / オンライン対戦 / FL 最適化 / チュートリアル) は触らない。

[統合視覚版を確認するなら A-3 統合ビュー作成から、直接実機反映なら B-1 から]
```

---

**End of Handoff v6**
