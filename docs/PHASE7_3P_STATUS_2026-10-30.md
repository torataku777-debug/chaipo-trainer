# Phase 7 1v1v1 Implementation Status — 2026-10-30

## 実装済み

- 既存1v1から独立した state3 / sessionScore3
- YOU / CPU A / CPU B の3席
- 54枚デッキから最大51枚を重複なく配布
- Dealer 3席ローテーション
- R1 5枚配置
- R2-R5 3枚配布 / 2枚配置 / 1枚捨て
- CPU2人の既存AI流用
- 3組のpairwise得点
  - YOU vs CPU A
  - YOU vs CPU B
  - CPU A vs CPU B
- 3人deltaのゼロサム保証
- 3人累積スコア
- 5ゲーム制
- 3人用結果画面 / 最終順位
- 3人それぞれ独立FL
- 人間17枚FLの操作UI
- CPU FLの自動配置
- 1人 / 2人 / 3人同時FLのエンジン経路
- ホームの「3 人対戦」を有効化
- AI選択画面 btnAI3P を有効化
- 3人専用ゲーム画面を動的生成

## 自動検証

### エンジン
5マッチ x 5ゲーム:
- 5/5終了: PASS
- Dealer 0 -> 1 -> 2: PASS
- 全員13枚完成: PASS
- 重複配布: 0
- delta合計=0: PASS
- deckUsed <= 54: PASS

### FL
- 1人FL: PASS
- 2人FL: PASS
- 3人FL: PASS
- 全員17枚FL (51枚消費): PASS
- 人間17枚FL UI: PASS
  - 17枚配布
  - 13枚配置
  - 4枚自動捨て
  - 結果表示

### UI
430px幅:
- 3人対戦ホームボタン: 有効
- R1-R5人間操作: PASS
- GAME RESULT: PASS
- 5ゲームMATCH RESULT: PASS
- 横スクロールなし: PASS

## 次に残るもの

- CPU盤面公開タイミングの演出調整
- 3人用カードサイズ / 情報密度の実機微調整
- 3人戦FL時の専用演出
- 3人戦ADVICE
- 3人戦のボード履歴 / ログ
- XP / レベルへの3人戦結果接続
- 25ゲーム以上のUI経由耐久テスト
