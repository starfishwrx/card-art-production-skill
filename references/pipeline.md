# 卡牌美术生产流水线

## 目录结构

推荐目录：

```text
asset_generation/
  <character_key>/
    character_description.md
    anchor_000.png
    anchor_060.png
    anchor_120.png
    anchor_180.png
    anchor_240.png
    anchor_300.png
    stage2_audit.md
  card_art/
    common_player.md
    common_enemy.md
    rubric.md
assets/
  cards/
  iterations/
    <card_id>/
      v1_prompt.txt
      v1_output.png
      v1_critique.md
data/
  card_designs.json
```

`asset_generation/archive/` 可以保存废弃脚本和历史 prompt，但正式生产必须明确当前使用哪条 pipeline。不要让生产 agent 在多个遗留脚本之间猜。

## before / after / iterate

`before`：纯文本生成，对照模型在没有 anchor 时会如何漂移。它不能成为最终卡图。

`after`：正式图生图生成。输入必须包括对应角色 anchor，建议优先用 front/core/all 三档：

- `front`：只用 `anchor_000.png`，适合快速首轮。
- `core`：使用 `anchor_000.png`、`anchor_060.png`、`anchor_180.png`，适合正式 v1/v2。
- `all`：使用六视图，适合角色漂移严重或最终关键图。

`iterate`：读取上一轮 prompt 和 critique，修正单卡块或补充迭代说明。除非全局规则确实错了，否则不要改公共块。

## 推荐命令形状

不同项目的脚本名可以不同，但语义要保持：

```bash
python3 asset_generation/generate.py before --card-id <card_id>
python3 asset_generation/generate.py after --card-id <card_id> --version v1 --anchor-set core --size 1024x1536
python3 asset_generation/generate.py iterate <card_id> v2 --anchor-set core --size 1024x1536
```

输出必须可复现到文件：

```text
assets/iterations/<card_id>/<version>_prompt.txt
assets/iterations/<card_id>/<version>_output.png
assets/iterations/<card_id>/<version>_critique.md
```

## 定档规则

单卡候选进入 `assets/cards/` 前必须满足：

1. 来源来自正式 `after` 或 `iterate`，不是 `before`。
2. 使用 approved anchors。
3. 单卡 rubric 全部关键项 PASS。
4. 同系列 cross-check PASS。
5. 文件比例适合作为卡图，通常是竖图，例如 `1024x1536`。

定档动作要小心：复制图片、更新业务数据、提交 git。不要覆盖用户已有定档图，除非明确说明替换原因。

## 常见失控点

- 多个 agent 各自改公共块，导致系列风格分裂。
- 只看角色像不像，不看这张卡的动作是否具体。
- 被漂亮图诱导，把语义不匹配的图定档。
- 把带卡框、文字或 UI 的图当成卡图源文件。
- 没有保留 v1/v2 prompt，后续无法复盘。
