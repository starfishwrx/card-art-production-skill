#!/usr/bin/env python3
"""创建一套最小可用的卡牌美术生产目录。"""

from __future__ import annotations

import argparse
from pathlib import Path


COMMON_PLAYER = """# 玩家方公共块

把已审核通过的六视图 anchor 作为角色身份主参考。
在这里描述玩家方角色身份、阵营视觉语言、主色、渲染风格、卡面裁切规则和负面约束。

硬性负面约束：不要文字、logo、水印、游戏 UI、卡框、额外角色。
"""

COMMON_ENEMY = """# 敌方公共块

把已审核通过的六视图 anchor 作为角色身份主参考。
在这里描述敌方角色身份、阵营视觉语言、主色、渲染风格、卡面裁切规则和负面约束。

硬性负面约束：不要文字、logo、水印、游戏 UI、卡框、额外角色。
"""

CARD_DATA = """{
  "cards": [
    {
      "id": "example_card_01",
      "name": "示例卡",
      "side": "player",
      "card_type": "技能",
      "archetype": "示例流派",
      "effect_type": "damage",
      "keywords": ["示例"],
      "description": "造成伤害，并展示一个清晰动作。"
    }
  ]
}
"""


def write_once(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="初始化卡牌美术生产目录")
    parser.add_argument("project_root", type=Path)
    parser.add_argument(
        "--characters",
        nargs="*",
        default=["character_a", "character_b"],
        help="要在 asset_generation 下创建的角色目录名",
    )
    args = parser.parse_args()

    root = args.project_root.resolve()
    for character in args.characters:
        char_dir = root / "asset_generation" / character
        char_dir.mkdir(parents=True, exist_ok=True)
        write_once(
            char_dir / "character_description.md",
            f"# {character}\n\n在这里写稳定的角色身份、服装规则、表情动作边界和负面约束。\n",
        )
        write_once(
            char_dir / "stage2_audit.md",
            "# 六视图审核\n\n- 角度覆盖：TODO\n- 身份一致性：TODO\n- 是否允许进入下游卡图生产：TODO\n",
        )
        for angle in ("000", "060", "120", "180", "240", "300"):
            (char_dir / f"anchor_{angle}.png").touch(exist_ok=True)

    write_once(root / "asset_generation" / "card_art" / "common_player.md", COMMON_PLAYER)
    write_once(root / "asset_generation" / "card_art" / "common_enemy.md", COMMON_ENEMY)
    write_once(root / "asset_generation" / "card_art" / "rubric.md", "# 项目审核规则\n\n在这里复制或改写 skill 的 QA rubric。\n")
    write_once(root / "data" / "card_designs.json", CARD_DATA)
    (root / "assets" / "cards").mkdir(parents=True, exist_ok=True)
    (root / "assets" / "iterations").mkdir(parents=True, exist_ok=True)
    write_once(root / "assets" / "cards" / "README.md", "# 最终卡图\n\n这里只放 reviewer 审核通过并定档的最终图片。\n")

    print(f"已初始化卡牌美术生产目录：{root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
