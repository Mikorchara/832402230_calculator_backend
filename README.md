# 832402230 Calculator Backend

计算器项目的后端服务，使用 FastAPI 和 SQLite 实现。

后端负责数学表达式的最终计算，并提供历史记录的保存、查询和删除功能。

## 在线访问

- 后端 API：https://eight32402230-calculator-backend.onrender.com
- Swagger API 文档：https://eight32402230-calculator-backend.onrender.com/docs
- 在线计算器：https://eight32402230-calculator-frontend.onrender.com
- 前端 GitHub：https://github.com/Mikorchara/832402230_calculator_frontend

> 后端部署在 Render 免费实例上。长时间无访问后实例可能进入休眠状态，因此首次请求可能需要等待一段时间。

## 功能

- 支持加、减、乘、除运算
- 支持小数、括号和复合表达式
- 使用 AST 解析表达式，不直接使用 `eval()`
- 自动保存成功的计算记录
- 查询历史记录
- 删除指定历史记录
- 处理非法表达式和除零错误

## 技术栈

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## 项目结构

```text
832402230_calculator_backend/
├── app/
│   ├── calculator.py
│   ├── database.py
│   └── main.py
├── calculator.db
├── .gitignore
├── PSP.md
├── README.md
├── codestyle.md
└── requirements.txt
```

## 运行环境

推荐使用 Python 3.9 或更高版本。

安装依赖：

```powershell
pip install -r requirements.txt
```

启动后端：

```powershell
uvicorn app.main:app --reload
```

默认访问地址：

```text
http://127.0.0.1:8000
```

本地 FastAPI API 文档：

```text
http://127.0.0.1:8000/docs
```

## API

### 计算表达式

```text
POST /api/calculate
```

请求示例：

```json
{
    "expression": "(1+2)*3"
}
```

响应示例：

```json
{
    "expression": "(1+2)*3",
    "result": 9
}
```

### 获取历史记录

```text
GET /api/history
```

返回已经保存的计算历史记录。

### 删除历史记录

```text
DELETE /api/history/{history_id}
```

删除指定 ID 的历史记录。

## 表达式计算

后端使用 Python `ast` 模块解析数学表达式。

当前支持：

- `+` 加法
- `-` 减法
- `*` 乘法
- `/` 除法
- 正负号
- 小数
- 括号
- 复合表达式

程序不会直接使用 `eval()` 执行用户输入，而是只处理允许的 AST 节点和运算符。

## 数据库

项目使用 SQLite 保存计算历史。

程序启动时会自动创建 `history` 表，因此不需要手动创建数据库表。

历史记录包含：

- ID
- 表达式
- 计算结果
- 创建时间

## 前后端连接

本地开发前端地址：

```text
http://127.0.0.1:5500
```

生产环境前端地址：

```text
https://eight32402230-calculator-frontend.onrender.com
```

后端通过 FastAPI `CORSMiddleware` 允许上述前端访问 API。

## 部署

后端使用 Render Web Service 部署：

```text
https://eight32402230-calculator-backend.onrender.com
```

生产环境使用 Uvicorn 启动 FastAPI：

```text
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

部署代码来源于本仓库的 `main` 分支。

### 关于 SQLite

本项目使用 SQLite 作为课程作业的轻量级数据库。

Render 免费 Web Service 的本地文件系统不适合作为长期持久化存储，因此服务重新部署或重启后，云端历史记录可能发生变化。该限制不影响本项目的计算、历史记录查询和删除功能演示。