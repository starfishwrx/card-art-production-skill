# Prompt 合约

## 总体结构

每张卡的 prompt 由四段组成：

1. 模式说明：before、after 或 iterate。
2. Image Anchors：列出本轮使用的 anchor 文件。
3. Common Block：角色和系列级约束。
4. Single-Card Block：这一张卡的语义、动作和构图。

公共块稳定，单卡块变化。迭代时优先改单卡块和迭代说明。

## Common Block 应包含

- 角色身份：发型、面部、年龄感、体型、核心服装语言。
- 阵营语言：上城/下城、科技/炼金、色彩、材质、光效。
- 系列风格：渲染方式、清晰度、镜头语言、卡图比例。
- 构图硬规则：单角色、脸和动作可读、竖图、安全区域。
- 负面约束：无文字、无 logo、无水印、无 UI、无卡框、无额外角色。

公共块示例：

```markdown
Use the supplied six-view anchors as the primary identity reference.
Preserve the character's face, hair silhouette, body proportion, outfit language, and signature color cues.
Create a vertical card illustration. The game UI will draw the card frame, so the image itself must not contain card borders, text, numbers, panels, or UI.
```

## Single-Card Block 应包含

- card id 和 card name。
- 角色、阵营、卡牌类型、关键词。
- 规则文本或效果摘要。
- 动作语义：这张卡到底在做什么。
- 表情要求：推演、伏击、防御、爆发、治疗等要有不同表情。
- 道具逻辑：道具必须服务效果，不允许装饰性堆道具。
- 小图可读要求：缩小后脸、手、核心道具、动作方向仍然可读。

单卡块示例：

```markdown
Card id: upper_hex_02
Card name: 99娘·学院推演
Effect: draw and focus.

Show one 99娘 actively performing an upper-city hextech deduction action. She is not posing. Her hands interact with a calculation device, crystal array, or mechanical table that visually explains information retrieval. The image should read as reasoning and drawing information before the title is known.
```

## 迭代说明

迭代说明要从 critique 里提取可执行修正，而不是泛泛加强质量。

弱迭代：

```text
Make it better and more dynamic.
```

强迭代：

```text
v1 failed because the pose read as holding a generic crystal. In v2, make the action a clear deduction scene: one hand adjusts a hextech calculation ring, the other pulls a glowing data thread from the device. Keep the face focused, not smiling.
```

## before 的作用

before 用于暴露模型默认偏差。它可以帮助 reviewer 判断 anchor 是否必要，也可以帮助生产 agent 找到负面约束。before 图不能定档。
