# チャイポネイバーズ 1v1v1 設計 v1

作成: 2026-10-30
対象: Game v1 Phase 6
方針: 安定済みの1v1を維持したまま、3人AI対戦を独立系として追加する。

## 1. 実装方針

現行コードは playerBoard / oppBoard / sessionScore.you / sessionScore.opp に強く依存している。
これを先に汎用players配列へ全面置換すると、安定化済み1v1・FL・オンライン系へ回帰を持ち込む可能性が高い。

Phase 7では既存1v1を変更せず、3人戦専用の以下を追加する。

- state3
- sessionScore3
- newGame3()
- renderGame3()
- renderOpponents3()
- runCpuTurn3()
- endGame3()
- applyScoreResult3()
- startFL3()

共通利用する既存ロジック:
- makeDeck / shuffle
- eval3 / eval5 / getBestValidEvals
- isFoul
- calcScoreWithJokers
- aiPlace5Rollout
- aiPineappleRollout
- checkFLEntry / checkFLContinue / getFLC

## 2. state3

```js
state3 = {
  mode: '3p-ai',
  phase: 'place5',
  round: 1,
  dealerSeat: 0,
  gameOver: false,
  deck: [],
  deckIdx: 0,
  turnOrder: [1, 2, 0],

  players: [
    {
      id: 'you',
      type: 'human',
      seat: 0,
      board: { top: [], mid: [], bot: [] },
      hand: [],
      discard: [],
      handDiscarded: [],
      placedThisRound: [],
      discardedThisRound: false,
      flMode: false,
      wasFL: false,
      flCards: 0,
      flDiscard: []
    },
    {
      id: 'cpu1',
      type: 'cpu',
      seat: 1,
      board: { top: [], mid: [], bot: [] },
      hand: [],
      discard: [],
      placedThisRound: [],
      discardedThisRound: false,
      flMode: false,
      wasFL: false,
      flCards: 0,
      flDiscard: []
    },
    {
      id: 'cpu2',
      type: 'cpu',
      seat: 2,
      board: { top: [], mid: [], bot: [] },
      hand: [],
      discard: [],
      placedThisRound: [],
      discardedThisRound: false,
      flMode: false,
      wasFL: false,
      flCards: 0,
      flDiscard: []
    }
  ]
}
```

人間専用の選択状態は state3.selectedCard に置いてもよいが、board/FL状態は必ず各playerに閉じ込める。

## 3. デッキと配布

54枚デッキを使用する。

通常プレイヤー1人あたり:
- R1: 5枚
- R2-R5: 3枚 x 4
- 合計17枚消費

3人全員通常でも 17 x 3 = 51枚。
3人全員17枚FLでも 51枚。
よって最大消費51枚で54枚以内。

ゲーム開始時に `dealPlan3` を作り、各seatの全配布カードを先に確保する。
ラウンドごとにそのplanから公開する。

理由:
- CPU処理順でカード内容が変わらない
- 将来オンライン3人戦へ流用できる
- FL混在時も配布順の不整合を防げる

```js
dealPlan3 = {
  0: { r1: [], r2: [], r3: [], r4: [], r5: [], fl: [] },
  1: { ... },
  2: { ... }
}
```

FLプレイヤーは fl に14-17枚。
通常プレイヤーは r1-r5 合計17枚。

## 4. ディーラーと配置順

dealerSeat はゲームごとに 0 -> 1 -> 2 -> 0 と回す。

基本配置順:
```js
turnOrder = [
  (dealerSeat + 1) % 3,
  (dealerSeat + 2) % 3,
  dealerSeat
]
```

ボタンが最後に配置する。

CPUの盤面公開もこの順序に合わせる。
人間より先に置いたCPUだけ見える、人間より後のCPUは確定前は見せない。

## 5. CPU

CPU1/CPU2は同じ評価関数を使うが、それぞれ独立して判断する。

R1:
`aiPlace5Rollout(hand, remainingDeck)`

R2-R5:
`aiPineappleRollout(hand, board, round, remainingDeck)`

remainingDeckは以下をすべて除外する。
- 3人全員の公開済みboard
- 既知のdiscard
- 自分のhand
- ルール上CPUから見えている他プレイヤーのカード

CPU強度は既存のプレイヤーレベル連動をそのまま使う。
Game v1ではCPU1/CPU2で難易度差を付けない。

## 6. 3人戦得点

3人戦は完全なpairwise方式。

組み合わせ:
- YOU vs CPU1
- YOU vs CPU2
- CPU1 vs CPU2

各ペアに既存 `calcScoreWithJokers(A.board, B.board)` を使用する。

```js
pairNet(score) =
  (score.pTotal + score.pRoy)
  - (score.oTotal + score.oRoy)
```

ゲームdelta:
```js
dYou  = net(you,cpu1) + net(you,cpu2)
dCpu1 = -net(you,cpu1) + net(cpu1,cpu2)
dCpu2 = -net(you,cpu2) - net(cpu1,cpu2)
```

必ず:
`dYou + dCpu1 + dCpu2 === 0`

sessionScore3:
```js
{
  scores: { you: 100, cpu1: 100, cpu2: 100 },
  games: 0
}
```

3人戦では1v1の「相手残点を上限にnetを丸める」処理は使わない。
ゲーム終了時に3人分のdeltaを同時適用し、誰かが0以下になった場合はそのゲーム終了後にマッチ終了。
これによりCPU処理順による得点差を防ぐ。

5ゲーム到達でも終了。

## 7. FL

FL状態は3人それぞれ独立。

可能:
- YOUだけFL
- CPU1だけFL
- CPU2だけFL
- 2人同時FL
- 3人同時FL

ゲーム開始時に各playerについて:
1. 前ゲームboardから checkFLContinue
2. 非FLなら checkFLEntry
3. getFLC で14/15/16/17を決定
4. dealPlan3から必要枚数を配布

FLプレイヤーは一括配置。
通常プレイヤーはR1-R5進行。

ゲーム終了条件は3人全員のboardが13枚完成した時点。

5ゲーム目がFLでも sessionScore3.games >= 5 を最優先し、6ゲーム目へ進ませない。

## 8. UI

430px幅を基準にする。

上部:
- CPU1 compact board
- CPU2 compact board

中央:
- スコアバー
  YOU / CPU1 / CPU2
  現在回戦

下部:
- YOU board
- hand
- ADVICE / CONFIRM

CPU盤面を横2列にするとカードが小さくなりすぎるため、縦に2つ並べる。
各CPU boardは既存opp-areaより高さを圧縮する。

CPUヘッダー:
`CPU A  100  [DLR]`
`CPU B  100`

結果画面:
- 3人順位
- 各pairwise結果
- 今ゲームdelta
- 累計score

## 9. 既存1v1との分離

3人ボタン:
`btnAI3P.disabled = false`

入口:
`startAi3MatchWithDealerToss() -> newGame3()`

以下は1v1のまま触らない:
- state
- newGame
- endGame
- sessionScore
- onlineMode
- 1v1 FL経路

3人戦終了時にstateへ変換しない。

## 10. Phase 7 実装順

1. state3 / sessionScore3 / dealPlan3
2. 3人分R1配布
3. CPU2人のR1配置
4. 人間R1配置
5. R2-R5進行
6. pairwise得点計算
7. 3人用結果画面
8. dealer 3席ローテーション
9. 5ゲームマッチ終了
10. 3人FL
11. 3人用UI調整
12. 連続25ゲームテスト

## 11. 完了条件

- 3人全員が毎ゲーム13枚完成する
- 同一カードが2人以上へ重複配布されない
- pairwise delta合計が常に0
- dealerが0→1→2で回る
- 5ゲームで必ず終了
- 5ゲーム目FLでも終了
- 3人同時FLでもデッキ不足なし
- ジョーカー2枚を含むゲームで役判定が破綻しない
- 25ゲーム連続で進行不能0
