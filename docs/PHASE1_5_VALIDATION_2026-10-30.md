# Phase 1-5 Validation Report — 2026-10-30

対象ブランチ: home-minimal-v1
基準コミット: 15daa8b

## 結論

現行AI 1v1は Game v1 の基礎として次フェーズへ進める状態。
基本ゲームループ、5ゲーム制、FL練習、主要役判定、ジョーカー、チュートリアルL1-L3に致命的な進行停止は確認されなかった。

## 1. AI 1v1 基本ループ

自動ブラウザ操作で確認。

- R1: 5枚配布 -> 5枚配置 -> CONFIRM
- R2-R5: 3枚配布 -> 2枚配置 -> 1枚自動捨て -> CONFIRM
- 最終13枚完成
- 結果表示
- 次ゲーム遷移
- ボタン / ノンボタン双方を通過

結果: PASS

## 2. 5ゲーム制

5ゲーム連続で実行し、5/5でMATCH結果表示を確認。
6ゲーム目へ進まない。

結果: PASS

## 3. 25ゲーム耐久

5マッチ x 5ゲーム = 25ゲームを連続自動実行。

結果:
- Match 1: 5ゲームで終了
- Match 2: 5ゲームで終了
- Match 3: 5ゲームで終了
- Match 4: 5ゲームで終了
- Match 5: 5ゲームで終了
- 進行不能: 0
- 6ゲーム目突入: 0
- 再戦: 正常
- 最終ホーム復帰: 正常

結果: PASS

## 4. 役 / ファウル / ジョーカー

12ケースの回帰検証。

確認:
- 正常board -> foul false
- TOP > MID -> foul true
- MID > BOT -> foul true
- eval3 / eval3Plain のrankとtopRankScore一致
- AKQハイカード
- 9ペア
- 7トリップス
- A/K/JK のJKがQへ化ける
- calcScoreWithJokersの左右反転対称性
- FL EV 14/15/16/17

12 / 12 PASS

## 5. FL突入

完成した非ファウル盤面で確認。

- TOP QQ -> 14枚
- TOP KK -> 15枚
- TOP AA -> 16枚
- TOP Trips -> 17枚

4 / 4 PASS

## 6. FL練習

14 / 15 / 16 / 17枚を全て実動テスト。

全ケース:
- 正しい枚数配布
- 13枚配置可能
- 残余カード自動捨て
- CONFIRM有効化
- RESULT表示

結果表示までの計測:
- 14枚: 約79ms
- 15枚: 約55ms
- 16枚: 約53ms
- 17枚: 約53ms

旧 findBestFL17 の長時間フリーズ経路は再発せず。

結果: PASS

## 7. FL終了条件

- 5ゲーム目がFL状態でも games=5 でMATCH終了
- FL中にスコアが0になっただけでは、その場でMATCH終了させない既存仕様を維持

結果: PASS

## 8. 修正した不具合

FL練習のevaluateFLBoardで、14/15/16枚でも再FL EVとして17枚用133を固定使用していた。

修正後:
- 14枚 = 25
- 15枚 = 40
- 16枚 = 69
- 17枚 = 133

コミット:
15daa8b Phase 1: FL practice EVを配布枚数別に修正

## 9. チュートリアル

起動確認:
- L1: ようこそ
- L2: 実際に置いてみよう
- L3: 役の強さのルール

L4 / L5は未実装。Phase 5以降の機能タスクとして残す。

## 10. 430 x 932 UI検査

iPhone 15 Pro Max相当のCSS viewportで検査。

- document横幅: 430 / scrollWidth 430
- 横スクロールなし
- 設定: 47 x 47
- CONFIRM: 182 x 48
- ADVICE: 76 x 44
- hand / player board / score bar: viewport内

ホームscreen自体のbottomがviewportより約8px下まで伸びるが、
操作ボタンはすべてviewport内。

現時点ではP0ではない。
3人戦UI実装時にホーム全体の高さも再調整する。

## Phase 1-5 判定

Game v1のAI 1v1基盤: PASS

次:
docs/THREE_PLAYER_DESIGN_v1.md に基づいてPhase 7の1v1v1実装へ進む。
