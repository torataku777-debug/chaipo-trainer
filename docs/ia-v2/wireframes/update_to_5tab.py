#!/usr/bin/env python3
"""
Update remaining wireframes from 4-tab to 5-tab navigation.
- battle_tab.html: active=battle
- friends_tab.html: active=friends
- more_tab.html: active=more, also remove shop menu (moved to pomu_town)
"""

import re
from pathlib import Path

WIRE_DIR = Path.home() / "Desktop/claude/codex_handoff/wireframes"

# 新しい5タブナビ HTML テンプレート
def make_nav(active_tab):
    tabs = [
        ("home",    "🏠", "ホーム",      ""),
        ("town",    "🎁", "ぽむタウン",  '<span class="nav-badge">1</span>'),
        ("battle",  "⚔",  "対戦",       ""),
        ("friends", "👥", "フレンド",    ""),
        ("more",    "≡",  "その他",      ""),
    ]
    rows = []
    for key, icon, label, badge in tabs:
        active_cls = " nav-tab--active" if key == active_tab else ""
        badge_html = f"\n      {badge}" if badge else ""
        rows.append(f'''    <div class="nav-tab{active_cls}" data-tab="{key}">
      <div class="icon-placeholder">{icon}</div>
      {label}{badge_html}
    </div>''')
    return "  <nav class=\"bottom-nav\">\n" + "\n".join(rows) + "\n  </nav>"


# CSS差分(4タブ → 5タブ: 文字小さく、アイコン小さく、バッジスタイル追加)
CSS_OLD = """    .nav-tab {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 600;
      color: #888;
      cursor: pointer;
      border-right: 1px dashed #ddd;
    }
    .nav-tab:last-child { border-right: none; }
    .nav-tab .icon-placeholder {
      width: 28px;
      height: 28px;"""

CSS_NEW = """    .nav-tab {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 10px;
      font-weight: 600;
      color: #888;
      cursor: pointer;
      border-right: 1px dashed #ddd;
      position: relative;
    }
    .nav-tab:last-child { border-right: none; }
    .nav-tab .icon-placeholder {
      width: 26px;
      height: 26px;"""

# バッジCSS(なければ追加)
BADGE_CSS = """
    .nav-badge {
      position: absolute;
      top: 6px;
      right: 18%;
      width: 14px;
      height: 14px;
      background: #c00;
      color: #fff;
      border-radius: 50%;
      font-size: 9px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1.5px solid #fff;
    }"""

# 各ファイルの更新仕様
TARGETS = {
    "battle_tab.html": {"active": "battle"},
    "friends_tab.html": {"active": "friends"},
    "more_tab.html": {"active": "more"},
}


def update_file(filename, spec):
    path = WIRE_DIR / filename
    content = path.read_text(encoding="utf-8")

    # 1. CSS の nav-tab 部分を更新(5タブ用)
    if CSS_OLD in content:
        content = content.replace(CSS_OLD, CSS_NEW)
        print(f"  ✓ CSS nav-tab updated in {filename}")
    else:
        print(f"  ⚠ CSS nav-tab pattern not found in {filename}")

    # 2. バッジCSS追加(active state CSS の後)
    nav_active_marker = """    .nav-tab--active::after {
      content: "";
      position: absolute;
      top: 0;
      left: 25%;
      right: 25%;
      height: 3px;
      background: #111;
    }"""
    if BADGE_CSS.strip() not in content:
        content = content.replace(nav_active_marker, nav_active_marker + BADGE_CSS)
        print(f"  ✓ Badge CSS added to {filename}")

    # 3. nav HTML 置換(4タブ → 5タブ)
    # 既存の 4タブナビをまるごと正規表現で捕捉
    nav_pattern = re.compile(
        r'<nav class="bottom-nav">.*?</nav>',
        re.DOTALL
    )
    new_nav = make_nav(spec["active"])
    if nav_pattern.search(content):
        content = nav_pattern.sub(new_nav.strip(), content, count=1)
        print(f"  ✓ Nav HTML updated to 5-tab in {filename}")
    else:
        print(f"  ⚠ Nav pattern not found in {filename}")

    path.write_text(content, encoding="utf-8")


def remove_shop_from_more():
    """more_tab.html からショップメニューを削除(ぽむタウンに移動済み)"""
    path = WIRE_DIR / "more_tab.html"
    content = path.read_text(encoding="utf-8")

    shop_row_pattern = re.compile(
        r'<div class="menu-row" data-menu="shop">.*?</div>\s*</div>',
        re.DOTALL
    )
    match = shop_row_pattern.search(content)
    if match:
        # 削除後の前後の空白を整理
        content = shop_row_pattern.sub('', content, count=1)
        # menu-section 内の連続改行を整理
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        path.write_text(content, encoding="utf-8")
        print(f"  ✓ Shop menu removed from more_tab.html")
    else:
        print(f"  ⚠ Shop menu pattern not found in more_tab.html")


print("=== Updating wireframes ===\n")
for filename, spec in TARGETS.items():
    print(f"[{filename}]")
    update_file(filename, spec)
    print()

print("[Extra: Remove shop from more_tab.html]")
remove_shop_from_more()

print("\n=== Done ===")
