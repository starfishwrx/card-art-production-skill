# 图片接口适配

这个 skill 不绑定具体图片供应商。项目需要提供一个可被 agent 调用的生图脚本，推荐契约如下：

```bash
python3 scripts/generate_image.py \
  --prompt-file prompt.txt \
  --filename output.png \
  --model <model-name> \
  --size 1024x1536 \
  --timeout 180 \
  --image anchor_000.png \
  --image anchor_060.png
```

要求：

- 无 `--image` 时走文生图，可用于 before。
- 有一个或多个 `--image` 时走图生图，可用于 after/iterate。
- 支持 `--prompt-file`，避免超长 prompt 被 shell 或日志截断。
- 输出文件路径由调用方控制。
- API key 从环境变量或本地 `.env.local` 读取，不写入仓库。
- 失败时返回非零退出码，并保存错误日志。

如果现有接口只能接收一张参考图，可以先用 `front` anchor 模式生产 v1，再在 v2 使用更强的文字约束。若接口支持多图输入，正式候选优先使用 `core` 或 `all`。

不要在公开 skill 仓库里放真实 API key、内部 endpoint token、私有素材或未授权 IP 原图。
