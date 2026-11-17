---
name: rivergold-code-architecture-data-model-boundaries
description: Apply Rivergold's module data model boundaries when designing, implementing, refactoring, or reviewing core code, business code, runtime-proto interfaces, or internal types.
---

# 模块数据模型边界

在涉及模块分层、对外协议、核心内部数据模型或两者转换的任务中，先阅读 [设计规范](references/design.md)。以该文档作为规则来源，不在此处维护另一份规则。

执行相关任务时：

1. 根据当前项目的实际结构识别模块的核心与业务部分，不强制套用特定目录名。
2. 检查核心是否依赖 proto，以及模块对外输入和输出是否由业务部分以 proto 表达。需要转换时，在业务部分完成。
3. 判断核心是否需要内部数据类型；按设计规范中的条件决定是否定义 dataclass，不为每个 proto 机械复制一个内部类型。
4. 同一领域概念有两种表示时，尽量保持类型名称相同；同文件使用两者时，给导入的 proto 类型起别名。
5. 实现或评审完成后，说明边界和转换位置；如发现违反规范的地方，指出具体代码及原因。

遵循用户对当前任务的明确要求，并结合项目既有约定选择具体实现。
