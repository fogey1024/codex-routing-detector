<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="docs/mascot.png">
    <img src="art/source/mascot_anim.webp" width="190" alt="拿着放大镜挥手的小侦探">
  </picture>
</p>

# Codex Routing Detector

[English](README.md) · [한국어](README.ko.md) · [下载](https://github.com/fogey1024/codex-routing-detector/releases)

查看实际响应 Codex 请求的模型。应用读取服务器响应中的模型名，将它与客户端请求的模型并排显示。可以单次检测，也可以在使用 Codex CLI 时实时查看。

## 安装

应用需要已使用 ChatGPT 账号登录的 Codex CLI 或 Codex 桌面版。实时监控需要 Codex CLI。

- **Windows**。如果 [Releases](https://github.com/fogey1024/codex-routing-detector/releases) 已提供 `codex-routing-detector.exe`，下载后双击即可运行。
- **Python 3.8 或更高版本**。也可以用 pipx 从汉化仓库安装。

  ```shell
  pipx install git+https://github.com/fogey1024/codex-routing-detector.git
  pipx inject codex-routing-detector pywebview
  codex-routing-detector-gui
  ```

从源码运行可以执行 `python codex_routing_webui.py`。安装包和源码入口均支持 `--tk`，用于打开备用窗口。主窗口无法启动时也会回退到备用窗口。

新用户首次启动默认使用简体中文。可在语言选择器中切换到 English 或 한국어，应用会记住选择。也可用 `codex-routing-detector-gui --lang zh-CN` 为本次启动指定语言。

## 检测

1. 在「检测」页选择模型。应用默认读取 `~/.codex/config.toml` 中的模型，也支持手动输入模型标识。
2. 点击「检测」。应用通过 Codex 发送一条简短提示词，请求只回复 `pong`。检测会计入 Codex 用量，其中包括预热和正式回合。
3. 查看结果卡片，再展开「响应记录」和「详细信息」核对请求模型、实际响应模型和响应 ID。

| 界面结果 | 含义 |
| --- | --- |
| 正常 | 服务器报告的响应模型与请求相符。 |
| 模型被替换 | 服务器报告了另一个模型，例如 `gpt-6-astra → gpt-5.6-luna`。 |
| 待确认 | 账号无法使用该模型、服务器返回错误，或应用未收到可确认的完整响应。 |

「推理强度」用于本次检测，`low` 的开销最低。「重复次数」可设为 1 到 10 次，便于观察路由是否随时间变化。自动检测找不到 Codex 时，可以手动指定可执行文件。流量捕获模式需要额外安装 `mitmproxy`。

「复制报告」会保留完整响应 ID，便于反馈问题。「保存 JSON」可导出结构化数据，「日志文件夹」可查看原始响应。诊断报告和命令行输出使用上游格式。

## 实时监控

1. 在「实时监控」页选择工作文件夹，然后点击「开始监控」。
2. 在新打开的 Codex CLI 窗口中照常工作。收到服务器响应后，应用会填入一行请求模型、实际响应模型和状态。
3. 点击「停止」会同时关闭受监控的 Codex CLI 窗口。在终端中执行 `/exit` 也会结束监控。结果保留到点击「清空」或关闭应用。

Codex 可能单独使用较小的模型生成对话标题。例如，`gpt-5.6-luna → gpt-5.6-luna` 表示这条请求按预期完成。实时监控本身不发起额外的 Codex 请求。桌面版用户可以通过「检测」页核对响应模型。

## 常见问题

### 出现容量不足或无法使用模型时怎么处理？

`server_is_overloaded` 表示服务器容量不足，可以稍后重试。`UNSUPPORTED` 表示服务器拒绝当前账号使用该模型，可以改用账号支持的模型。服务器已报告替代模型的响应仍会归为 `REROUTED`，即使该响应之后失败。

### 为什么模型名中的 `openai/` 被去掉了？

Codex 使用不带提供商前缀的模型标识。检测时会使用去掉前缀的模型名，并在详细信息中说明。

### 发现模型被替换时可以提供哪些信息？

可用「复制报告」取得请求模型、实际响应模型、响应 ID、UTC 时间、Codex 版本及套餐和用量信息。分享前请检查其中是否包含希望保留为私密的信息。

### 汉化版如何更新？

图形界面启动时会检查本汉化仓库的 [Releases](https://github.com/fogey1024/codex-routing-detector/releases)。如果有更新且发布了 Windows 可执行文件，安装目录可写时，程序可以在空闲时下载并替换自身。`--no-auto-update` 仅保留更新提示。使用 `--no-update-check` 或设置 `CODEX_ROUTING_DETECTOR_NO_UPDATE=1` 可关闭检查。

## 数据与隐私

- **检测日志**默认保存在临时文件夹，可能包含会话 ID、账号用户 ID、探测提示词和用量信息。请求正文、授权标头和 Cookie 不会写入检测日志。流量捕获模式会保留模型、服务等级和推理强度等路由字段。
- **实时监控**通过仅监听 `127.0.0.1` 的代理读取 Codex CLI 响应。诊断记录保存在内存中，包含模型名、响应 ID、时间、状态和错误码。提示词、文件和回答直接转发。会话证书在监控停止后删除。
- **JSON 报告**可能包含套餐、用量和余额信息。对外分享前，可以移除这些字段。

## 命令行与构建

```shell
codex-routing-detector -m gpt-6-astra
codex-routing-detector -r 3 --json out.json --full-ids
codex-routing-detector --help
```

退出码 `0` 表示检测的模型均按请求响应，`2` 表示发现模型替换，`1` 表示检测或参数出错。完整命令行选项见 [英文说明](README.md)。测试和 Windows 打包步骤见 [开发文档](docs/DEVELOPMENT.md)。

原项目由 [darkdarkcocoa](https://github.com/darkdarkcocoa/codex-routing-detector) 开发，采用 [MIT 许可证](LICENSE)。
