# Codex 改善指示書: 対戦タブ v2
作成: 2026-05-15
対象: 対戦タブ v1 (Claude 初稿) を v3 (ガチャ) / v5 (ショップ) / v7 (所持) / home v2 / opening v2 / more v2 / friend v2 同等の品質に磨く

---

## 状況

- ぽむタウン三部作 (ガチャ v3 / ショップ v5 / 所持 v7)、ホーム v2、開封演出 v2、その他タブ v2、フレンドタブ v2 が完成
- フレンドタブを v3 に改訂し、`room-actions` セクション (新しい部屋を作る + コードで参加) を削除 → 「対戦タブ」の「フレンド対戦」に移管
- 5タブ構成の「対戦」タブ初稿 (v1) を Claude が実装した — **これは BottomNav 中央・主役**
- v1 の細部品質を確立済み品質基準と同等レベルに引き上げる
- これは **対戦動線の中核画面** (BottomNav あり、サブタブ無し、青空背景)
- 仕様根拠: `INFORMATION_ARCHITECTURE.md` v2.2 (Q1 判断更新)

---

## 入力ファイル

| パス | 役割 |
|---|---|
| `~/Desktop/claude/codex_handoff/visual/pomu_battle_v1.html` | **改善対象 (v1・初稿)** |
| `~/Desktop/claude/codex_handoff/visual/pomu_friend_v3.html` | 参考 (LIVE pill / list-card / sky+cloud 背景・直近確定版) |
| `~/Desktop/claude/codex_handoff/visual/pomu_more_v2.html` | 参考 (.profile-card / settings-card / row-icon 統一形) |
| `~/Desktop/claude/codex_handoff/visual/pomu_home_v2.html` | 参考 (mission-card / PRIMARY CTA / アバター・段位表現) |
| `~/Desktop/claude/codex_handoff/visual/pomu_town_v7.html` | 参考 (sky/ink/pomu トークン・device 393x852) |

参照画像 (image inputs):
- `visual/v1_battle_top.png` — 上部 (ヘッダー + ランクマッチ大カード + カジュアル/フレンド対戦タイル)
- `visual/v1_battle_bottom.png` — 下部 (練習セクション + BottomNav)

---

## 画面構造 (変更しない)

```
status-bar
battle-header (タイトル「対戦」 + 右上に「S3 残り 12日」ピル)
screen-body:
  rank-card (主役・3px 金枠):
    rank-card-label "★ RANKED MATCH"
    rank-shield (盾チェックアイコン) + rank-name "プラチナ 3"
                                     + rank-rate "レート 1,247" + rank-delta "+24"
    rank-progress-row "プラチナ 4 まで" + "253 / 400"
    rank-progress (バー、約 63%)
    rank-cta "マッチング開始" (PRIMARY)
  mode-grid (2 カラム):
    mode-tile.casual  (シアン顔アイコン)  "カジュアル"  "レート変動なし / 気軽に対戦"
    mode-tile.friend  (紫人物アイコン)    "フレンド対戦" "部屋を作る / コードで参加"
  section: 練習
    practice-card → practice-row × 2:
      AI 対戦 (シアンロボット, "2 人 / 3 人(近日) ・ レベル選択可")
      FL 練習 (金色王冠, "ファンタジー練習" サブラベル付き, "14/15/16/17 枚 ・ EV 表示で局面研究")
bottom-nav (5タブ・"battle" アクティブ)
```

各行のサイズ感、3px 金枠 (`.rank-card::before` の mask trick)、プログレスバーは構造として維持。

---

## 改善ポイント (★優先度順)

### ★★★ 1. ランクマッチカードの主役感をさらに強化

現状: 3px 金枠 (linear-gradient 135deg) + 内側白カード。よく出来ているが、「中央タブの主役」としてはまだ抑えめ。

具体策:
- 3px 金枠の **グラデを多段化** (`linear-gradient(135deg, #fde68a 0%, #fbbf24 18%, #f59e0b 38%, #b45309 50%, #f59e0b 62%, #fbbf24 82%, #fde68a 100%)`) で立体的に
- カード上端の **inset highlight をより金寄り** に: `inset 0 1px 0 rgba(255, 246, 199, 0.92)` → `inset 0 1px 0 rgba(255, 250, 220, 0.96), inset 0 2px 3px rgba(255, 235, 178, 0.42)`
- カード外側の box-shadow に **金色の薄い光輪** を 1 段追加: `0 0 30px rgba(255, 210, 74, 0.18)` を box-shadow リストに混ぜる
- 全体の重心 (size, padding) は変えない — 「枠の輝きで主役化」する

### ★★★ 2. rank-shield (段位アイコン) の質感洗練

現状: 64×64 の角丸オレンジグラデの盾 + 内部に白い盾チェック SVG。段位を即座に伝えるアイコンだがやや単調。

具体策:
- 盾の **背景グラデを 3 段に**: `radial-gradient(circle at 30% 22%, #fff7d6 0%, #fbbf24 42%, #d97706 88%, #92400e 100%)` で内部に光と影を作る
- 盾の **エッジを 2 重に**: 現状の inset shadows に加え `0 0 0 1px rgba(146, 64, 14, 0.36), 0 0 0 2.5px rgba(255, 247, 214, 0.40)` で金縁感を強化
- 内部 SVG の盾チェックを **stroke-width 2.2 → 2.4**, やや太く
- ✦ スパークルを **3 個に増やす** (top-right, top-left, bottom-right) で「最高の段位」感
- スパークルの色をやや金寄りに (`#fff` → `#fff7d6`)

### ★★★ 3. プログレスバーの「ランクアップへの距離」表現を強化

現状: 8px 高、黄色グラデ、`width: 62%` (CSS) / `width: 63%` (HTML)。シンプルだが視覚的に静的。

具体策:
- バー本体に **光沢のシマー** を inset で追加: `inset 0 0 0 1px rgba(255, 250, 220, 0.32), inset 0 -2px 4px rgba(146, 64, 14, 0.18)`
- バーの **右端に微細な光の点** (filled circle SVG or pseudo-element) を置く: 「進行中」を示唆
- 進捗値テキスト `253 / 400` を **font-variant-numeric: tabular-nums + size 12px** に
- 「プラチナ 4 まで」ラベル横にも **次段位の小さな金星アイコン** を追加 (12×12, opacity 0.6)
- height を `8px → 9px` で 1px だけ太く

### ★★ 4. mode-tile (カジュアル / フレンド対戦) の表現力強化

現状: 白カード + アイコン + タイトル + 2行サブ。シンプルだが、左右のタイルが同じ重さに見える。フレンド対戦のほうが「コードを共有して遊ぶ」というアクション性が強いはずなので、ほんの少しだけ差異を出したい。

具体策:
- 両タイル共通:
  - サブテキストの行間を `line-height: 1.36 → 1.40` に
  - mode-icon のサイズ 38 → 40, border-radius 12 → 13
- カジュアル (シアン):
  - mode-icon の背景に **微細な内側シアン glow**: `inset 0 -2px 5px rgba(7, 89, 133, 0.12)` 追加
- フレンド対戦 (紫):
  - mode-icon の背景に **微細な内側紫 glow** + 右上に **小さなプラスマーク** SVG オーバーレイ (12×12, opacity 0.62, 「招待性」を暗示)
  - タイル右下にごく薄い紫ラジアル `radial-gradient(circle at 84% 84%, rgba(168, 85, 247, 0.10), transparent 60%)` を背景に重ねる
- タイル全体の `:hover` 時に **微細にカードが浮く** (現状 active 時の沈み込みのみ): `transform: translateY(-1px); box-shadow ↑`

### ★★ 5. rank-cta「マッチング開始」のヒエラルキー統一

現状: friend_v3 / more_v2 の PRIMARY CTA と同じ造形 (黄色グラデ + inset gold + ⚔)。ただし「マッチング開始」は対戦動線の最重要 CTA なので、わずかに大きく主張させたい。

具体策:
- font-size `17px → 18px`, letter-spacing `0.06em → 0.08em`
- パディング `18px 18px` 維持、ただし `min-height: 60px` を保証
- ⚔ アイコンを **左ではなく右** に配置 (動詞「開始 →」のニュアンス) — または現状の左維持で svg を少し大きく (22 → 24)
- 押下時の沈み込みを `translateY(2px) scale(0.99) → translateY(3px) scale(0.99)` で 1px 深く

### ★★ 6. ヘッダー右の「S3 残り 12日」ピルの質感

現状: シアン小ピル、時計アイコン + テキスト。控えめでよい。

具体策:
- 背景濃度を `--season-pill-bg: rgba(143, 200, 224, 0.18) → rgba(230, 244, 251, 0.84)` で雲色寄りに
- 内側に **微細な inset highlight** を追加: `inset 0 1px 0 rgba(255,255,255,0.62)`
- 時計アイコンの **stroke を 2 → 2.2** で 1px シャープに
- 残日数 `12日` 部分のみ **`color: var(--accent-warning)` (#eab308) かオレンジ** に色変更で「カウントダウン感」(他は通常色)
  - 例: `<span>S3 残り <span style="color: var(--pomu-orange); font-weight: 900;">12日</span></span>`

### ★ 7. 練習行 (AI 対戦 / FL 練習) アイコンの洗練

現状: AI 対戦 = ロボット風 (head + アンテナ + 目 + サイドピン)。FL 練習 = 王冠風 (3 山ジグザグ + 下部 V カット)。基本は OK だが、アイコン密度がやや高すぎる/低すぎる。

具体策:
- **AI 対戦**: ロボットを **より四角く** (rx 3 → 2)、目を縦長 dot から **円 + 内側ハイライト** に
  - 例: `<circle cx="9" cy="11" r="1.3" fill="currentColor"/>` + `<circle cx="9" cy="10.6" r="0.5" fill="#fff"/>`
- **FL 練習**: 王冠の **下端ベース** を追加して安定感を出す: `<path d="M5 16 H19" stroke-width="2.4"/>` を最後に追加
  - 王冠の宝石を 1 個追加: 中央山に `<circle cx="12" cy="9" r="1.3" fill="currentColor"/>`
- 両アイコン共通: stroke `2 → 2.2`

### ★ 8. 練習行サブテキストの情報量微調整

現状:
- AI 対戦: 「2 人 / 3 人(近日) ・ レベル選択可」
- FL 練習: 「14 / 15 / 16 / 17 枚 ・ EV 表示で局面研究」

具体策:
- 中黒「・」の前後に **半角スペース** を入れて読みやすく (もう入っているが念のため確認)
- FL 練習の「ファンタジー練習」サブラベルを **タイトル行内の inline-block バッジ風** に格上げ:
  - 例: `<span class="title-sublabel">ファンタジー練習</span>`
  - スタイル: `font-size: 10px; font-weight: 800; letter-spacing: 0.10em; padding: 2px 7px; border-radius: 6px; background: var(--row-icon-bg-warm); color: var(--pomu-gold-deep); margin-left: 6px;`

### ★ 9. SVG アイコンの統一パス

- ナビ icons の stroke-width は **すべて 2**
- ヒーロー級 (rank-cta の対角矢印) のみ **2.4**
- rank-shield 内部の SVG: 2.2 → 2.4
- mode-tile 内部の SVG: 現状 2 維持
- practice-row chevron: 2 維持

---

## 守るべき制約 (絶対変更禁止)

1. **HTML の主要構造**:
   - `.device` 内のレイアウト
   - `.rank-card` の入れ子構造 (label / top / progress-row / progress / cta)
   - `.mode-grid` 内の 2 タイル並列構造
   - `.practice-card` 内の practice-row × 2 構造
   - 5タブ構成の `.bottom-nav`、`battle` アクティブ
2. **JavaScript 機能**:
   - 各ボタンのタップフィードバック JS を維持
3. **データ・テキスト**:
   - 段位「プラチナ 3」、レート「1,247」、直近 +24
   - 進捗「プラチナ 4 まで 253 / 400」
   - シーズン「S3 残り 12日」
   - タイル: 「カジュアル / レート変動なし / 気軽に対戦」「フレンド対戦 / 部屋を作る / コードで参加」
   - 練習: 「AI 対戦 / 2 人 / 3 人(近日) ・ レベル選択可」「FL 練習 / ファンタジー練習 / 14 / 15 / 16 / 17 枚 ・ EV 表示で局面研究」
   - CTA: 「マッチング開始」
4. **既存 CSS 変数** (`:root`) を消さない (新規追加・値変更は OK)
5. **背景トーン**: 青空グラデ + 雲SVG を維持
6. **デバイス幅**: 393 × 852 を維持
7. **rank-card の 3px 金枠**(mask trick) のメカニズム自体は維持(グラデの色だけ強化OK)
8. **rank-shield のスパークルアニメ** を維持 (新規追加もOK)

---

## 出力ファイル

`~/Desktop/claude/codex_handoff/visual/pomu_battle_v2.html`

ファイル冒頭のメタコメントに:
- バージョン: v2
- 改善日
- 改善者: Codex / GPT
- v1 からの変更点 (箇条書き)

末尾の `.dev-note` ブロックは v1 のメモ書きなので、v2 では別の dev-note (Codex 改善点の要約) に差し替え。

---

## 完了基準

- [ ] rank-card の 3px 金枠が多段グラデで立体的に
- [ ] rank-shield が 2 重エッジ + 3 個スパークル + より深いグラデで主役化
- [ ] プログレスバーが光沢 inset + 右端ハイライトで「進行中」感
- [ ] mode-tile の左右で「カジュアル(穏やか) / フレンド対戦(動的)」の差を微表現
- [ ] rank-cta が他画面の PRIMARY と比べて 1 ランク上の存在感
- [ ] ヘッダーの S3 ピルで「12日」部分がオレンジ強調
- [ ] 練習行アイコン (AI / FL) の密度が整い、ファンタジー練習サブラベルが小バッジ化
- [ ] iPhone 393×852 でレイアウト崩れなし
- [ ] JS タップアニメが動作
- [ ] 既存テキスト・データ完全維持

---

**End of Brief**
