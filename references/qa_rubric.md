# QA Rubric

每项用 PASS/FAIL。FAIL 必须写可见位置或具体原因。

## 单卡审核

- Official flow：是否来自正式 after/iterate，是否使用 approved anchors。
- Format gate：是否为竖向卡图，主体是否在安全区域，是否适合作为卡面源图。
- Subject count：是否只有一个核心角色。
- Character identity：脸、发型、体型、服装语言是否匹配 anchors。
- Expression fit：表情是否符合卡牌功能。
- Action silhouette：不读标题时，姿态是否先读出该动作。
- Action match：画面是否执行这张卡的具体效果，而不是同角色泛用插画。
- Prop logic：关键道具是否服务效果，是否物理上说得通。
- Anatomy and hands：手、肢体、道具连接是否不会在卡图尺寸下出戏。
- Composition：脸、手、动作方向和核心道具是否清楚。
- Small-card read：缩小到游戏卡面尺寸后是否仍能读出语义。
- Faction style：阵营视觉语言是否明确。
- Leakage：是否有文字、数字、logo、水印、UI、卡框。
- Series fit：亮度、饱和度、背景类型、渲染风格是否与同系列明显不一致。
- Semantic specificity：能否回答：为什么这是这张卡，而不是同角色普通插画？

## 审核模板

```markdown
# <card_id> <version> Critique

Status: PASS / FAIL / CONTENT PASS FORMAT HOLD

## Summary
一句话说明是否可进入下一步。

## Rubric
- Official flow: PASS/FAIL. ...
- Format gate: PASS/FAIL. ...
- Character identity: PASS/FAIL. ...
- Expression fit: PASS/FAIL. ...
- Action silhouette: PASS/FAIL. ...
- Action match: PASS/FAIL. ...
- Prop logic: PASS/FAIL. ...
- Composition: PASS/FAIL. ...
- Leakage: PASS/FAIL. ...
- Series fit: PASS/FAIL/HOLD. ...
- Semantic specificity: PASS/FAIL. ...

## Decision
定档、继续 v2、重开公共块、或等待系列 cross-check。
```

## 系列审核

同角色或同阵营至少三张候选 PASS 后执行。关注：

- 角色身份是否稳定。
- 画面亮度和饱和度是否在同一范围。
- 背景复杂度是否一致。
- 动作卡、支援卡、防御卡是否有可区分的构图语言。
- 是否存在某张漂亮但明显离群的图。

系列审核可以让单卡回炉。单卡 PASS 不是定档豁免。
