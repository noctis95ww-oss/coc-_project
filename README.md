# COC Keeper Copilot

Call of Cthulhu（COC）跑团主持人（Keeper）辅助工具。目标是帮助 Keeper 导入模组、管理故事状态，并借助大语言模型自动生成场景、线索、NPC 台词等内容。

## 当前进度
- ✅ 初始化 FastAPI 后端骨架：
  - 模组管理、跑团会话管理、剧情生成三个核心 API 占位符。
  - 生成服务暂以占位实现返回示例文案，便于与前端联调。
- ✅ 配置管理：使用 `pydantic` 读取 `.env`，支持未来接入 OpenAI 等模型服务。
- ✅ 项目依赖：提供 `pyproject.toml`（Poetry），便于安装与后续添加依赖。

## 快速开始
1. **安装依赖**（推荐使用 [Poetry](https://python-poetry.org/)）：
   ```bash
   cd backend
   poetry install
   ```
2. **启动开发服务器**：
   ```bash
   poetry run uvicorn app.main:app --reload
   ```
3. 浏览 Swagger 文档：`http://127.0.0.1:8000/docs`

## 项目结构
```
backend/
  app/
    api/v1/        # REST API 路由
    core/          # 配置、常量
    schemas/       # Pydantic 数据模型
    services/      # 核心业务逻辑（当前为内存实现）
    main.py        # FastAPI 入口
  pyproject.toml   # Poetry 配置
```

## 后续规划
- [ ] 接入模组解析（PDF/Markdown）与向量检索。
- [ ] 持久化存储（PostgreSQL/Redis）替换当前内存实现。
- [ ] LLM 接入与提示模板系统，输出多种叙事内容。
- [ ] 前端控制台（React / Vue）用于跑团现场操作。
- [ ] 加入单元测试 & 集成测试，保障核心流程稳定。

欢迎贡献想法或 PR，一起把 Keeper 的 AI 助手搭建完善！
