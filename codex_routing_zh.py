"""Simplified Chinese translations for the Tkinter and pywebview windows."""

STATUS = {
    "ok": "正常", "OK": "正常", "REROUTED": "模型被替换", "UNSUPPORTED": "账号不支持",
    "ERROR": "错误", "UNKNOWN": "待确认", "NO_DATA": "无数据", "CANCELLED": "已取消",
    "completed": "已完成", "failed": "失败", "in_progress": "进行中",
    "incomplete": "未完成", "cancelled": "已取消", "canceled": "已取消",
}

TK_STRINGS = {
    "model": "模型", "effort": "推理强度", "repeat": "重复次数",
    "wire": "流量捕获模式（mitmproxy）", "no_mitm": "流量捕获模式（未安装 mitmproxy）",
    "codex_btn": "选择 Codex…", "codex_auto": "自动检测", "codex_pick_title": "选择 Codex 可执行文件",
    "check": "检测", "cancel": "取消", "copy": "复制报告", "save_json": "保存 JSON…", "open_logs": "打开日志文件夹",
    "idle": "已就绪。点击「检测」可为每个选定模型发起一个简短的 Codex 回合。",
    "starting": "正在启动 Codex（{version}）…", "running": "正在检测 {i}/{n} · {model}（{effort}）…",
    "done": "已完成，用时 {secs} 秒。原始日志位于 {dir}", "cancelling": "正在取消…", "cancelled": "检测已取消。",
    "failed": "无法启动检测。",
    "col_n": "#", "col_requested": "请求模型", "col_kind": "类型", "col_served": "实际响应模型",
    "col_status": "状态", "col_created": "创建时间（UTC）", "col_verdict": "判定", "col_id": "响应 ID",
    "kind_warmup": "预热", "kind_turn": "回合",
    "banner_idle": "暂无结果", "banner_running": "正在检测…",
    "banner_rerouted": "模型被替换 · {pairs}", "banner_ok": "{models} 按请求响应",
    "banner_error": "无法确认 {models} 的检测结果", "banner_cancelled": "已取消", "banner_fatal": "检测出错",
    "banner_unsupported": "此账号（套餐 {plan}）无法使用 {models}",
    "notes": "详细信息", "account": "账号", "codex": "Codex",
    "codex_hint": "点击「选择 Codex…」指定可执行文件，例如 npm 包中的 codex.exe 或 Codex 桌面版附带的可执行文件。",
    "copied": "报告已复制到剪贴板。", "saved": "已保存到 {path}", "fake": "（离线示例数据）",
    "update_new": "新版 v{new}",
    "update_pip": "v{new} 已发布。安装命令为 pip install -U git+{repo}",
    "update_manual": "v{new} 已发布。点击右下角的版本标签下载。",
    "update_downloading": "正在下载 v{new}（{mb} MB）…",
    "update_restarting": "下载完成，正在重启至 v{new}…",
    "update_failed": "自动更新到 v{new} 失败（{err}）。请点击右下角的版本标签手动下载。",
    "updated": "已更新至 v{current}。",
    "subtitle": "哪个模型实际响应了你的 Codex 请求？",
    "brief": "结果摘要",
    "brief_idle": "点击「检测」会发出一条简短提示词，并从服务器的响应中读取实际响应模型。",
    "brief_running": "正在向 Codex 发送简短的提示词并等待服务器响应…",
    "brief_rerouted": "你请求的是 {models}，共收到 {total} 条响应，其中 {bad} 条由 {served} 响应。",
    "brief_ok": "{models} 按请求响应。",
    "brief_unsupported": "服务器拒绝了 {models} 的请求。此账号（套餐 {plan}）无法使用该模型。",
    "brief_error": "{models} 的检测未完成，服务器返回了错误 {errors}。",
    "brief_nodata": "未收到 {models} 的服务器响应。请查看下方的 Codex 详细信息。",
    "brief_cancelled": "已取消检测，完成了 {n} 次探测。",
    "brief_fatal": "无法启动检测。详细信息见下方（{error}）。",
    "brief_account": "套餐为 {plan}，当前用量周期已使用 {used}%。",
    "brief_not_limit": "检测时账号尚有可用额度。",
    "brief_limit": "用量已达上限，服务器可能改用备用模型。",
    "brief_advice_rerouted": "路由可能随时间变化。可以稍后重试，或暂时改用其他模型。需要反馈时，请复制报告。",
    "brief_advice_ok": "如果之后怀疑响应模型有变化，可以再检测一次。",
    "brief_advice_unsupported": "请选择此账号可用的模型，再点击「检测」。",
    "brief_advice_error": "请稍后重试。服务器容量不足通常是暂时的。",
    "confirm_title": "开始检测？",
    "confirm_body": "应用会通过 Codex 向 {model} 发送一条简短的提示词，要求只回复 \"pong\"，并从服务器响应中读取实际响应模型。",
    "confirm_skip": "下次不再询问", "confirm_ok": "开始检测", "confirm_cancel": "取消",
    "tab_check": "检测", "tab_live": "实时监控（CLI）",
    "live_cfg": "Codex 设置", "live_cfg_value": "模型 {model} · 推理强度 {effort}（{source}）",
    "live_cfg_none": "config.toml 未指定模型，Codex 将使用默认值",
    "live_folder": "工作文件夹", "live_folder_btn": "选择文件夹…", "live_folder_title": "选择 Codex 的工作文件夹",
    "live_start": "开始监控", "live_stop": "停止",
    "live_idle": "监控未启动。点击「开始监控」会打开一个 Codex CLI 窗口。",
    "live_running": "正在通过 127.0.0.1:{port} 监控 Codex（进程 {pid}）。请在 Codex 窗口中照常操作。",
    "live_stopped": "监控已停止。", "live_codex_exit": "Codex 已退出（退出码 {rc}），监控已停止。",
    "live_failed": "无法启动实时监控。",
    "live_needs_crypto": "实时监控需要 cryptography。请运行 pip install cryptography 安装。",
    "live_stop_confirm": "停止监控也会关闭正在监控的 Codex 窗口。现在停止吗？",
    "live_close_confirm": "实时监控正在运行。关闭此应用也会关闭正在监控的 Codex 窗口。现在关闭吗？",
    "live_copy": "复制监控报告", "live_clear": "清空",
    "col_time": "时间",
    "banner_live_idle": "监控未启动",
    "banner_live_waiting": "监控中，正在等待第一个请求",
    "banner_live_ok": "已有 {n} 条响应符合请求",
    "banner_live_rerouted": "模型被替换 · {pairs}（{total} 条响应中有 {bad} 条）",
    "banner_live_unsupported": "此账号无法使用 {models}",
    "banner_live_error": "暂未确认响应（{n} 个错误）",
    "brief_live_idle": "开始监控会打开一个通过本地代理连接的 Codex CLI 窗口。每次请求的实际响应模型都会显示在这里。",
    "brief_live_running": "请在单独的 Codex 窗口中操作。服务器响应后，记录会显示在这里。通信内容不会写入磁盘。",
    "brief_live_waiting": "暂无请求。请在 Codex 窗口中输入内容。",
    "brief_live_rerouted": "Codex 请求了 {requested}。共收到 {total} 条响应，其中 {bad} 条由 {served} 响应。",
    "brief_live_ok": "目前已收到 {n} 条响应，均由 Codex 请求的模型响应。",
    "brief_live_unsupported": "服务器拒绝了请求。此账号无法使用 {models}。",
    "brief_live_error": "目前服务器仅返回了错误（{errors}）。",
    "confirm_live_title": "启动实时监控？",
    "confirm_live_body": "应用会在新终端中打开 Codex CLI。该终端的连接会经过 127.0.0.1 上的本地代理，应用用本次会话专用的证书读取服务器返回的模型名。提示词、文件和回答会直接转发，不作保存。停止监控时也会关闭该 Codex 窗口。",
    "confirm_live_ok": "开始监控",
    "guide_title": "实时监控",
    "guide_heading": "实时监控使用指南",
    "guide_body": (
        "🚀 点击「开始监控」，然后在新开的 Codex CLI 窗口里照常操作。\n\n"
        "🔍 每次收到服务器响应，表格都会列出请求模型、实际响应模型和判定。\n\n"
        "🟢 绿色表示按请求响应。🔴 红色表示模型被替换。\n\n"
        "🧹 Codex 可能把生成对话标题等小任务交给 gpt-5.6-luna 或 gpt-5.6-terra。"
        "只要该行的请求模型和实际响应模型一致，就是正常结果。\n\n"
        "🔒 监控仅在内存里记录模型名、响应 ID 等信息。提示词、文件和回答不会保存。\n\n"
        "💻 实时监控仅支持 Codex CLI。用完后点击「停止」。"
    ),
    "guide_ok": "知道了", "guide_skip": "下次不再显示",
    "panel_options": "选项", "panel_results": "结果", "panel_session": "会话",
    "logs_label": "日志",
    "error_label": "错误",
    "all_files": "所有文件",
    "codex_missing": "找不到 Codex 可执行文件（{how}）。",
    "startup_failed": "{title} 无法启动（{error}）。",
    "language_menu": "界面语言",
}

TK_MENU = {
    "help": "帮助", "usage": "使用方法", "terms": "术语表",
    "about": "关于", "close": "关闭", "guide": "实时监控指南",
}

TK_USAGE = """使用方法

1. 选择要检测的模型。应用会优先读取 ~/.codex/config.toml 中的模型。

2. 点击「检测」。应用会通过 Codex 发送一条简短的提示词，要求只回复 pong。每次检测结束后，表格会填入相应结果。点击「取消」可停止检测。

3. 查看结果。绿色表示请求的模型按预期响应，红色表示服务器改用了其他模型。若账号不支持该模型、服务器报错或未返回完整响应，请查看详细信息。

4. 「复制报告」会把含完整响应 ID 的报告放到剪贴板。「保存 JSON」可导出同一批数据。「打开日志文件夹」可查看原始响应。

选项

推理强度用于本次探测。low 的开销最低。
重复次数可设为 1 到 10，便于观察路由是否随时间变化。
流量捕获模式使用 mitmproxy，需要单独安装。
自动检测找不到 Codex 时，点击「选择 Codex…」指定可执行文件。

实时监控

点击「开始监控」，在新打开的 Codex CLI 窗口中照常工作。结果表会逐条显示请求模型、实际响应模型和判定。「工作文件夹」决定 Codex 从哪里启动。

点击「停止」会同时关闭该 Codex 窗口。直接退出 Codex 也会结束监控。桌面版用户可用「检测」页查看结果。

用量和隐私

单次检测包含预热和正式回合，会计入 Codex 用量。实时监控只观察你在被监控窗口里发出的请求。

检测日志可能包含会话 ID、账号用户 ID 和探测提示词。实时监控只在内存中保留模型名、响应 ID、状态、时间和错误码等诊断信息。本地代理使用会话临时证书，系统证书库保持原样。
"""

TK_TERMS = """术语表

请求模型是 Codex 客户端在请求中指定的模型。实际响应模型来自服务器响应对象中的 model 字段。

预热是 Codex 在正式回合前自动发出的请求，用于建立连接和预载系统提示词。回合是发送提示词并接收模型回答的正式请求。

推理强度对应 model_reasoning_effort。服务等级对应 service_tier，priority 速度更快，也会消耗更多用量。

响应 ID 是服务器分配的标识（resp_…），反馈问题时可用它定位请求。创建时间是服务器记录的 UTC 时间。

判定

ok · 请求模型按预期响应，回合已完成。
REROUTED · 响应中出现另一个模型。预热或正式回合都可能发生。
UNSUPPORTED · 服务器拒绝了该模型，当前账号无法使用它。
ERROR · 服务器报错，例如 server_is_overloaded 表示容量不足。
UNKNOWN · 缺少确认模型所需的信息，例如正式回合未完成。
NO_DATA · 未读取到 WebSocket 消息。请检查 Codex 登录、网络和连接方式。

检测与监控模式

跟踪模式是默认检测方式，从 Codex 的 WebSocket 跟踪日志读取服务器响应。
流量捕获模式使用本地 mitmproxy 读取请求和响应。
实时监控通过只在 127.0.0.1 监听的会话代理读取响应。
对照模型用于命令行版本，同一轮会额外检测一个模型以比较结果。

账号详情会显示套餐和用量百分比。limit_reached 表示当前用量周期是否已达到上限。
"""

TK_ABOUT = """Codex Routing Detector v{version}

这个工具读取服务器响应中的模型名，用于核对实际响应的模型。

上游作者于 2026 年 9 月 22 日记录到一次 gpt-6-astra 请求由 gpt-5.6-luna 响应，并据此开发了这个工具。

命令行版本提供更多选项。安装、用法与隐私说明见 README.zh-CN.md。
源码与更新 {repo}
"""

WEB_UI = {
    "subtitle": "哪个模型实际响应了你的请求？",
    "tabCheck": "检测", "tabLive": "实时监控",
    "settings": "检测设置", "session": "会话设置",
    "model": "模型", "effort": "推理强度", "repeat": "重复次数",
    "wire": "流量捕获模式", "wireOff": "流量捕获模式（未安装 mitmproxy）",
    "results": "响应记录", "copy": "复制报告", "json": "保存 JSON", "logs": "日志文件夹",
    "clear": "清空",
    "colKind": "类型", "colRoute": "请求模型 → 实际响应模型", "colStatus": "状态", "colTime": "时间",
    "colId": "响应 ID",
    "empty": "暂无检测记录。", "liveEmpty": "在受监控的 Codex 窗口中发出请求后，响应会显示在这里。",
    "details": "详细信息", "detailsHint": "账号 · Codex 路径 · 日志",
    "detailsHintLive": "代理 · 会话记录", "detailsEmpty": "暂无详细信息。",
    "liveFolder": "工作文件夹",
    "foot": "通过一条简短的请求，读取服务器报告的响应模型。",
    "idleHead": "准备就绪", "runHead": "正在检测…",
    "badHead": "模型被替换", "cancelledHead": "检测已取消",
    "cta": "检测", "ctaAgain": "重新检测", "ctaRun": "检测中…", "cancel": "取消",
    "chipIdle": "待检测", "chipRun": "检测中", "chipOk": "正常", "chipBad": "模型被替换",
    "chipWarn": "待确认",
    "statusIdle": "已就绪", "statusDone": "已完成，用时 {secs} 秒",
    "liveStart": "开始监控", "liveStop": "停止",
    "liveChipOff": "未启动", "liveChipOn": "监控中", "liveChipBad": "模型被替换", "liveChipWarn": "待确认",
    "liveStatusOff": "监控未启动",
    "helpUsage": "使用方法", "helpTerms": "术语表", "helpGuide": "实时监控指南",
    "helpAbout": "关于", "helpTitle": "帮助", "close": "关闭", "ok": "确定",
    "statusPreparing": "正在准备 Codex…", "confirmRepeat": "当前设置会重复检测 {n} 次。",
    "closeTitle": "关闭窗口？",
    "customModel": "手动输入…", "customModelTitle": "输入模型标识",
    "languageMenu": "界面语言",
}

WEB_TEXT = {
    "starting": "正在准备 Codex（{version}）…",
    "cancelling": "正在取消…", "cancelled": "检测已取消。", "failed": "无法启动检测。",
    "copied": "报告已复制。", "saved": "已保存到 {path}", "fake": "（离线示例数据）",
    "codex_hint": "在「检测」页的设置栏右侧点击「codex · 自动检测」，可手动选择 Codex 可执行文件，例如 npm 包中的 codex.exe。",
    "live_needs_crypto": TK_STRINGS["live_needs_crypto"],
    "live_codex_exit": TK_STRINGS["live_codex_exit"],
    "live_stopped": "监控已停止。", "live_cfg_none": "默认",
    "confirm_title": "开始检测？",
    "confirm_body": "应用会通过 Codex 向 **{model}** 发送一条简短的提示词，要求只回复 \"pong\"。"
                    "随后会从服务器响应里读取实际响应模型。检测会消耗少量 Codex 用量。",
    "confirm_skip": "下次不再询问", "confirm_ok": "开始检测", "confirm_cancel": "暂不",
    "confirm_live_title": TK_STRINGS["confirm_live_title"],
    "confirm_live_body": TK_STRINGS["confirm_live_body"],
    "confirm_live_ok": "开始监控",
    "live_stop_confirm": TK_STRINGS["live_stop_confirm"],
    "live_close_confirm": TK_STRINGS["live_close_confirm"],
    "update_pip": "v{new} 已发布。点击左下角的版本标签查看更新。",
    "update_manual": "v{new} 已发布。点击左下角的版本标签下载。",
    "update_downloading": "正在下载 v{new}（{mb} MB）…",
    "update_restarting": TK_STRINGS["update_restarting"],
    "update_failed": "自动更新到 v{new} 失败（{err}）。请点击左下角的版本标签手动下载。",
    "updated": TK_STRINGS["updated"],
}

WEB_VERDICT = {
    "idleBrief": "点击「检测」，即可通过一条简短的 Codex 请求确认实际响应模型。",
    "runBrief": "正在等待服务器返回响应模型。",
    "okHead": "{model} 按请求响应",
    "okBrief": "请求的模型是 **{model}**，服务器报告的响应模型也是 **{model}**。",
    "badBrief": "请求的模型是 **{requested}**。共收到 {total} 条响应，其中 {bad} 条来自 **{served}**。",
    "badTip": "可以稍后重新检测，或暂时使用其他模型。",
    "unsupportedHead": "此账号无法使用该模型",
    "unsupportedBrief": "服务器拒绝了 **{requested}** 的请求。请换用此账号支持的模型再检测。",
    "errorHead": "检测未完成",
    "errorBrief": "检测 **{requested}** 时，服务器返回了错误（{errors}）。可以稍后重试。",
    "nodataBrief": "检测 **{requested}** 时没有收到完整响应。请查看下方的详细信息。",
    "fatalHead": "无法启动检测",
    "fatalBrief": "请查看下方的详细信息。",
    "cancelledBrief": "本次检测已取消。点击 **重新检测** 可再试一次。",
    "liveIdleHead": "实时监控未启动",
    "liveIdleBrief": "点击「开始监控」会打开一个 Codex CLI 窗口。在其中发出请求后，实际响应模型会逐条显示在这里。",
    "liveWaitHead": "正在监控",
    "liveWaitBrief": "请在新开的 Codex CLI 窗口中发出请求。",
    "livePendingBrief": "Codex 请求了 **{requested}**，正在等待响应结束。",
    "liveOkHead": "目前响应正常",
    "liveOkBrief": "Codex 请求了 **{requested}**。目前的 {n} 条响应均来自 **{requested}**。",
    "liveBadBrief": "Codex 请求了 **{requested}**。共收到 {total} 条响应，其中 {bad} 条来自 **{served}**。",
    "liveUnsupportedBrief": "服务器拒绝了 **{requested}** 的请求。此账号无法使用该模型。",
    "liveErrorHead": "服务器返回了错误",
    "liveErrorBrief": "Codex 请求了 **{requested}**，目前仅收到错误（{errors}）。",
    "liveUnknownHead": "部分响应无法确认",
    "liveUnknownBrief": "Codex 请求了 **{requested}**，目前还没有可确认的完整响应。请查看列表中的状态。",
}

WEB_HELP = {
    "usage": [
        {"icon": "🐾", "title": "开始检测", "numbered": True, "items": [
            "在 **检测设置** 中选择模型。应用优先使用 `~/.codex/config.toml` 中的模型。",
            "点击 **检测**。应用会通过 Codex 发出一条简短的提示词，要求只回复 pong。",
            "在结果卡片和 **响应记录** 中查看请求模型与实际响应模型。",
        ]},
        {"icon": "🎨", "title": "结果颜色", "items": [
            {"chip": "模型被替换", "tone": "bad", "text": "服务器报告的响应模型与请求的模型不同。"},
            {"chip": "正常", "tone": "ok", "text": "服务器使用了请求的模型。"},
            {"chip": "待确认", "tone": "warn", "text": "账号无法使用该模型、服务器出错或响应不完整。请查看 **详细信息**。"},
        ]},
        {"icon": "⚙️", "title": "检测选项", "items": [
            {"term": "推理强度", "text": "选择探测请求的推理强度。`low` 的开销最低。"},
            {"term": "重复次数", "text": "可设置 1 至 10 次，便于观察路由是否随时间变化。"},
            {"term": "流量捕获模式", "text": "使用本地 mitmproxy 读取流量，需要安装 `mitmproxy`。"},
            {"term": "选择 Codex", "text": "自动检测找不到 Codex 时，点击设置栏右侧的 `codex · 自动检测` 指定可执行文件。"},
        ]},
        {"icon": "📋", "title": "保存检测证据", "items": [
            "**复制报告** 会复制含完整响应 ID 的诊断报告。",
            "**保存 JSON** 会导出可供程序读取的报告。**日志文件夹** 可打开原始响应日志。",
        ]},
        {"icon": "👀", "title": "实时监控", "items": [
            "点击 **开始监控** 打开 Codex CLI。随后在该窗口中照常工作，服务器响应会逐条出现在监控页。",
            "点击 **停止** 会关闭受监控的 Codex 窗口。退出 Codex 也会结束监控。桌面版用户可使用检测功能。",
        ]},
        {"icon": "🔒", "title": "用量与隐私", "items": [
            "检测中的预热和正式回合会计入 Codex 用量。实时监控只观察你在该会话中发出的请求。",
            "检测日志可能包含请求标识和探测提示词。实时监控仅在内存中保留诊断信息。",
        ]},
    ],
    "terms": [
        {"icon": "🔍", "title": "请求与响应", "items": [
            {"term": "请求模型", "text": "Codex 在请求里指定的模型。"},
            {"term": "实际响应模型", "text": "服务器在响应对象的 `model` 字段中报告的模型。"},
            {"term": "预热 / 回合", "text": "预热由 Codex 自动发起。正式回合会发送提示词并接收模型回答。"},
            {"term": "响应 ID", "text": "服务器分配的 `resp_…` 标识，反馈问题时可用它定位请求。"},
            {"term": "推理强度", "text": "Codex 的 `model_reasoning_effort` 设置。"},
        ]},
        {"icon": "🚦", "title": "报告判定", "items": [
            {"term": "ok / REROUTED", "text": "分别表示按请求响应和模型被替换。"},
            {"term": "UNSUPPORTED / ERROR", "text": "分别表示账号无法使用该模型和服务器错误。"},
            {"term": "UNKNOWN / NO_DATA", "text": "分别表示响应模型无法确认和未读取到 WebSocket 消息。"},
        ]},
        {"icon": "⚙️", "title": "获取数据的方式", "items": [
            {"term": "跟踪模式", "text": "默认方式，从 Codex 的 WebSocket 跟踪日志中读取模型名。"},
            {"term": "流量捕获模式", "text": "通过本地 mitmproxy 读取请求和响应。"},
            {"term": "实时监控", "text": "通过 127.0.0.1 上的本地代理和会话专用证书读取 Codex CLI 响应。"},
            {"term": "对照模型", "text": "命令行版本默认额外检测 `gpt-5.6-sol`。用 `--control` 更换，用 `--no-control` 关闭。"},
        ]},
    ],
    "guide": {
        "heading": "如何使用实时监控",
        "items": [
            {"icon": "🚀", "title": "点击「开始监控」", "text": "在新打开的 Codex CLI 窗口中照常工作。"},
            {"icon": "🔍", "title": "每条响应对应一行", "text": "每行并排显示 Codex 请求的模型和实际响应模型。"},
            {"icon": "🚦", "title": "用颜色查看判定", "text": "绿色表示按请求响应，红色表示模型被替换，橙色表示需要检查状态。"},
            {"icon": "🧹", "title": "会话可能请求小模型", "text": "Codex 可能用 `gpt-5.6-luna` 或 `gpt-5.6-terra` 生成对话标题等。"
             "例如 `gpt-5.6-luna → gpt-5.6-luna` 表示按请求响应。"},
            {"icon": "🔒", "title": "记录保留在本机内存", "text": "监控只保留模型名、响应 ID 等诊断信息。提示词、文件和回答会直接转发。"},
            {"icon": "💻", "title": "适用于 Codex CLI", "text": "使用完毕后点击「停止」。Codex 桌面版可使用检测页。"},
        ],
        "skip": "下次不再显示",
        "ok": "知道了",
    },
    "about": {
        "lead": "查看实际响应你请求的 Codex 模型。",
        "paras": [
            "应用读取服务器响应对象中报告的模型名，让你核对请求模型与实际响应模型。",
            "上游作者在 2026 年 9 月 22 日观察到一次 gpt-6-astra 请求由 gpt-5.6-luna 响应，并据此制作了这个工具。",
            "命令行版本 `codex-routing-detector` 提供更多选项。完整说明见中文 README。",
        ],
        "repo": "在 GitHub 上查看",
    },
}
