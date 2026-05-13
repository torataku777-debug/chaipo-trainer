# NEXT SESSION HANDOFF — 2026-05-14

前回: `archive/old_docs/NEXT_SESSION_HANDOFF_2026-05-13.md`

---

## 今セッションの成果(2026-05-13 後半 〜 14 早朝)

**視覚仕上げフェーズ Phase A 大幅前進**。確定版3画面を作成:

| 画面 | 確定版 | 場所 |
|---|---|---|
| ぽむタウン > ガチャ | **v3** | `docs/ia-v2/visual/pomu_town_gacha_v3.html` |
| ぽむタウン (ガチャ+ショップ) | **v5** | `docs/ia-v2/visual/pomu_town_v5.html` |
| ホーム | **v2** | `docs/ia-v2/visual/pomu_home_v2.html` |

ぽむキャラクター画像も7ポーズ切り出し済み: `docs/ia-v2/visual/assets/pomu_pose_{1-7}.png`

参考スクリーンショット:
- `gacha_v3_intermediate.png` — ガチャタブ仕上げ
- `v5_shop_intermediate.png` — ショップタブ仕上げ
- `home_v2_intermediate.png` — ホームタブ仕上げ

---

## 確定したデザイン方針

### カラートークン(全画面共通)
```
--sky-100:        #e6f4fb       (背景上端)
--sky-200:        #c5e2f0       (背景下端)
--cloud-white:    #ffffff       (カード地)
--cloud-soft:     #f6fbfd       (カード地グラデ上)
--pomu-yellow:    #fbbf24       (アクセント)
--pomu-orange:    #f59e0b       (アクセント深)
--leaf-green:     #65c466
--ink-900:        #1a1f2c       (主テキスト)
--ink-500:        #6b7280       (サブテキスト)
--ink-300:        #d1d5db
--ready-glow-soft: rgba(255,210,74,0.35)  (準備完了金グロー)
```

### モチーフ確定
- **ぽむパック → カード束**(扇形重ね、トランプ風) ← 巾着袋から方針転換
- **ぽむ本体は絶対変更しない** — PNG (`assets/pomu_pose_*.png`) を `<image>` で埋め込み
- パック種別:
  - 背景パック = 空ブルー裏面 + 雲柄 + 山雲アイコン + pose_6
  - フレームパック = クリーム裏面 + 格子柄 + フレーム枠アイコン + pose_5
  - アバターパック = パイナップル黄裏面 + 葉柄 + ぽむシルエット + pose_7

### CG感の表現(全画面共通)
- カードに `var(--card-shadow)` (4px+1px 多層影)
- ボタンに **上端ハイライト + 下端暗影 + 内側グロー**
- 背景に **空グラデ + 控えめな雲(複数楕円)**
- 状態差: `.is-ready` で金グロー + 揺れアニメ、 `.is-locked` で saturate(0.7) + 時計マーク
- ホームのみ例外: **PRIMARY CTA は紫グラデ**(対戦専用色として認める)

---

## 進化のプロセス記録

### ガチャタブ
```
v1   → SVG手書きぽむ(失敗、本物らしくない)
v1.1 → ぽむをPNG埋め込みに変更(これが正解)
v1.2 → ぽむサイズ48→62px拡大、左上シフト
v2   → Codex磨き: 巾着袋シルエット、CG調ハイライト、上質ボタン、雲立体化
v3   → Codex磨き: 「袋微妙」指摘 → カード束モチーフへ方針転換 ★確定
```

### ショップタブ
```
v4 → Claude初稿: Featured(夜景)/カテゴリ4種/コイン購入カード
v5 → Codex磨き: 夜景ビルバリエ、電光看板、月光輪、ボタン上質化、アイコン精細化 ★確定
```

### ホームタブ
```
v1 → Claude初稿: ヘッダー/CTA動的切替/ガチャリマインダー/ミッション/ボーナス/お知らせ
v2 → Codex磨き: CTA装飾円、ピル型タグ、ぽむアバター上品枠、ミッション完了グロー ★確定
```

---

## 学習: Codex 投入パイプライン(確立済み)

```
1. Claude 初稿を書く(構造とトーンを確立)
2. CODEX_BRIEF_*.md を作成(優先度順の改善ポイント、絶対制約)
3. codex_prompt_*.txt を作成(英語の簡潔な指示)
4. run_codex_*.sh で nohup 起動
5. 22秒間隔でポーリング(ファイルサイズ・ログtail)
6. ファイルサイズ固定 = 書き込み完了
7. Chrome で localhost:8765 確認、screencapture でスクショ
8. 評価して次の iteration へ
```

Codex CLI 設定:
- model: gpt-5.5
- reasoning effort: xhigh
- approval_policy: never (sandbox: workspace-write)
- 所要時間: 5〜15分(画像入力で reasoning が深くなる)
- ファイルサイズ固定後の検証フェーズは長い → kill して進めて良い

---

## 注意点・つまづき

### Filesystem MCP の不安定さ
- 大きいディレクトリの list_directory_with_sizes でタイムアウト発生
- 代替: `osascript` 経由の `ls` で確実に取得
- スコープは `~/Desktop/claude/` のみ。chaipo へは osascript で cp する

### Chrome MCP の document_idle タイムアウト
- アニメーション継続中のページで screenshot が 45秒タイムアウト
- 代替: AppleScript で `screencapture -R` で直接スクショ
- ローカルサーバー必要: `python3 -m http.server 8765` で起動(/tmp/pomu_server.pid)
- file:// プロトコルは Chrome MCP の navigate でうまく扱えない(prefix付与される)

### ぽむPNGの白背景処理
- PIL の `ImageDraw.floodfill` で4隅から透明化
- ぽむ輪郭(黒線)で内部は保護される
- スクリプト: `~/Desktop/claude/transparent_bg.py`

### キャラシ切り出し
- 上段4ポーズ、下段3ポーズ
- 隣ぽむの輪郭が左右で繋がっているため、bboxのxは信頼できない
- 解決: bbox の高さ + cell中心x で正方形化、下段は縦長切り出し+正方形キャンバスペースト
- スクリプト: `~/Desktop/claude/extract_pomu_poses_pil.py`

### ローカルHTTPサーバー
- `cd ~/Desktop/claude/codex_handoff/visual && nohup /usr/bin/python3 -m http.server 8765`
- PID保存: `/tmp/pomu_server.pid`
- 止め方: `kill $(cat /tmp/pomu_server.pid)`

---

## 残作業(次セッション)

### Phase A: 視覚仕上げ完了に向けて
1. **ぽむタウン > 所持タブ**(現状 v5 内では placeholder)
   - 仕様書ベースで装備中アイテム + コレクション一覧
2. **対戦タブ**(BottomNav 中央)
   - ランクマッチ / フリーマッチ / フレンドマッチのメニュー
   - 仕様書: 既存の `HOME_SCREEN_SPEC.md` などに依存しないため新規作成必要
3. **フレンドタブ**
   - フレンド一覧 + コミュニティ(ぽむタウンの活動フィード)
   - 仕様書: `COMMUNITY_ROADMAP.md` を参考
4. **その他タブ**
   - 設定 / 統計 / プロフィール詳細
5. **統合ビュー**(任意)
   - 5タブが切替可能な統合 HTML(`pomu_app_v1.html` 等)

推奨順序: 4 → 1 → 3 → 2(対戦は仕様確定後)。または **対戦タブを先に**(チャイポの本体機能なので最優先という考えも可)。

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

### 作業ディレクトリ(Mac内ローカル)
```
~/Desktop/claude/codex_handoff/
├── POMU_TOWN_GACHA_VISUAL_SPEC.md       — 視覚仕様書(全画面トークン)
├── CODEX_BRIEF_GACHA_V2.md              — Codex指示書(巾着袋へ)
├── CODEX_BRIEF_GACHA_V3.md              — Codex指示書(カード束へ)★転換点
├── CODEX_BRIEF_SHOP_V5.md               — Codex指示書(ショップ磨き)
├── CODEX_BRIEF_HOME_V2.md               — Codex指示書(ホーム磨き)
├── references/
│   ├── pomu_character_sheet.png         — ぽむ7表情の元画像
│   ├── README.md
│   └── IMG_2200.PNG など
└── visual/
    ├── pomu_town_gacha_v{1,1.1,1.2,2,3}.html
    ├── pomu_town_v{4,5}.html
    ├── pomu_home_v{1,2}.html
    ├── gacha_*_screenshot.png
    ├── *_intermediate.png
    └── assets/
        ├── pomu_pose_1.png 〜 pomu_pose_7.png
        ├── _preview_bbox.png(切り出し検証用)
        └── _preview_tiny.png
```

### Git管理下(chaipo)
```
~/chaipo/docs/ia-v2/
├── NEXT_SESSION_HANDOFF_2026-05-14.md   ← 本ファイル
├── POMU_TOWN_GACHA_VISUAL_SPEC.md
├── CODEX_BRIEF_GACHA_V2.md
├── CODEX_BRIEF_GACHA_V3.md
├── CODEX_BRIEF_SHOP_V5.md
├── CODEX_BRIEF_HOME_V2.md
└── visual/
    ├── pomu_town_gacha_v3.html          (★ガチャ確定版)
    ├── pomu_town_v5.html                (★ショップ統合版確定)
    ├── pomu_home_v2.html                (★ホーム確定版)
    ├── gacha_v3_intermediate.png
    ├── v5_shop_intermediate.png
    ├── home_v2_intermediate.png
    └── assets/pomu_pose_{1-7}.png
```

### スクリプト集(Mac内ローカル)
```
~/Desktop/claude/
├── extract_pomu_poses_pil.py            — ぽむキャラシ→7PNG切り出し
├── transparent_bg.py                    — ぽむPNGの白背景透明化
├── make_v4.py                           — v3 + ショップ初稿の統合
├── make_v1.2.py                         — ぽむサイズ拡大
├── run_codex.sh / run_codex_v3.sh / run_codex_v5.sh / run_codex_home_v2.sh
└── codex_prompt*.txt
```

### Codex 実行ログ
```
/tmp/codex_run.log              — gacha v2
/tmp/codex_run_v3.log           — gacha v3
/tmp/codex_run_v5.log           — shop v5
/tmp/codex_run_home_v2.log      — home v2
/tmp/codex_final_*.txt          — 完了サマリ
/tmp/codex*.pid                 — プロセスID
```

---

## 次セッション開始のスニペット

```
ハンドオフを読んで、視覚仕上げの残作業に進もう。
今日完了: ガチャ v3 / ショップ v5 / ホーム v2 の3画面。
次の候補: 対戦タブ、フレンドタブ、所持サブタブ、その他タブ、開封演出。
```

---

## 状態スナップショット

- **git ブランチ**: `ia-v2-redesign`(コミット予定: 本セッション分)
- **iPhone デバイスID**: `790A0ABF-CF12-53F0-876B-6BA865407BEF`
- **本番HTML**: 未更新(視覚版はまだプロトタイプ、本体は `~/Desktop/claude/index_backup.html` のまま)
- **ローカルサーバー**: localhost:8765(Phase B 開始時に再起動推奨)

---

**End of Handoff**
