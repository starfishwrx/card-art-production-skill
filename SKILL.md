---
name: card-art-production
description: Card game art production workflow for AI agents. Use when producing or reviewing a coherent card-art set, especially when the task mentions card illustration, character anchors, six-view turnaround, image-to-image generation, v1/v2 iterations, art QA, series consistency, before/after/iterate pipelines, or separating production agents from reviewer agents.
---

# Card Art Production

这个 skill 用于把一组卡牌美术从零散生图变成可审核、可迭代、可定档的生产流程。核心原则：先建立角色六视图 anchor，再用 anchor 做单卡图生图，所有候选都保留 prompt/output/critique，最后由独立 reviewer 做单卡审核和系列一致性审核。

## 工作流

1. 建目录和清单  
   若项目还没有美术产线，先运行 `scripts/init_card_art_project.py <project-root>`。它会创建 `asset_generation/`、`assets/cards/`、`assets/iterations/`、`data/` 和基础模板。

2. 生产角色 anchor  
   每个核心角色必须有六个方向：`anchor_000.png`、`anchor_060.png`、`anchor_120.png`、`anchor_180.png`、`anchor_240.png`、`anchor_300.png`。没有通过审核的六视图，不进入正式卡图生产。

3. 写公共块和单卡块  
   公共块描述角色身份、系列风格、世界观、构图硬规则和负面约束。单卡块只描述这一张卡的动作、效果、道具逻辑和画面语义。详细结构见 `references/prompt_contract.md`。

4. 运行 before / after / iterate  
   `before` 是无 anchor 的对照输出，只用于看模型会怎么跑偏。`after` 是正式 anchor-guided 生成。`iterate` 基于上一轮 critique 继续修。正式候选必须落盘为：
   - `assets/iterations/<card_id>/v1_prompt.txt`
   - `assets/iterations/<card_id>/v1_output.png`
   - `assets/iterations/<card_id>/v1_critique.md`

5. 独立审核  
   生产 agent 只负责生成候选和记录意图。reviewer agent 负责 PASS/FAIL 审核。不要让生成者自己定档。审核规则见 `references/qa_rubric.md`。

6. 系列 cross-check  
   同一阵营或同一角色至少有三张单卡 PASS 后，再做系列一致性审核。单卡 PASS 只说明这一张语义成立，系列 PASS 才能进入最终 `assets/cards/`。

7. 定档  
   只有同时通过单卡 QA 和系列 QA 的图片，才能复制到 `assets/cards/<card_id>.png`，并写入业务数据里的 `image_file` 字段。

## 角色分工

主 agent 做制片和审核：定义目录、拆任务、控制版本、读图审核、定档。  
生产 subagent 做单卡生产：读取公共块和单卡块，调用图片接口生成，写 `vN_prompt.txt` 和 `vN_output.png`。  
审核由主 agent 或独立 reviewer 执行：必须看图，不接受只看 prompt 的审核。

适合并行生产时，把卡牌按角色或阵营切给多个生产 subagent。并行前必须固定公共块，避免每个 agent 自己发明一套美术方向。

## 何时读取参考文件

- 做目录落地或工具适配时，读 `references/pipeline.md`。
- 写 prompt 或拆公共块/单卡块时，读 `references/prompt_contract.md`。
- 审核单卡或系列一致性时，读 `references/qa_rubric.md`。
- 接入具体图片接口或已有生图脚本时，读 `references/image_api_adapter.md`。

## 硬门槛

- 正式卡图必须使用角色 anchor 作为图生图输入。纯文生图只能是 before 对照或实验。
- 候选图、prompt、critique 必须同目录保存。丢失任意一项，就无法定档。
- 审核必须使用 PASS/FAIL。FAIL 要写可见位置，不写“感觉不太好”。
- 表情、动作、道具逻辑是硬门槛。角色像但动作泛化，仍然 FAIL。
- 卡图本体不要生成游戏 UI、卡框、文字、logo、水印。UI 应由前端绘制。
