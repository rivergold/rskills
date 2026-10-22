---
name: hefeng-weather-query
description: 调用和风天气 3 日预报接口，并输出结果
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [python, weather, api]
    category: productivity
    requires_toolsets: [terminal]
---

# Hefeng Weather Skill

## When to Use
- 用户需要查询成都（`location=101270101`）未来 3 天天气。
- 用户希望使用本地 Python 脚本直接调用和风天气 API。

## Procedure
1. 进入技能目录：`rivergold/hefeng_weather/`。
2. 确保 Python 环境可用，并安装依赖 `requests`。
3. 运行脚本 `call_hefeng.py` 调用 API。
4. 读取终端输出，并进行无修改显示。

推荐执行命令：

```zsh
cd hefeng_weather
python3 -m pip install requests
python3 call_hefeng.py
```

## Pitfalls
- 不需要其他输入信息
- 直接返回终端输出，不要进行额外的总结或处理。
- `ModuleNotFoundError: requests`：未安装依赖，执行 `python3 -m pip install requests`。
- `403/401`：API Key 无效或权限不足，需要更新 `call_hefeng.py` 中 `X-QW-Api-Key`。
- 网络超时：检查网络连通性，或稍后重试。
- 输出为空：确认接口返回中存在 `daily` 字段。

## Verification
- 终端输出应至少包含 3 行天气数据。
- 每行应类似：`📅 今天(YYYY-MM-DD) | 🔥 最高温 xx℃ | ❄️ 最低温 xx℃ | ☀️ 白天 xx | 🌙 夜间 xx`。
- 若出现上述格式，表示已成功调用 `call_hefeng.py` 并完成解析输出。