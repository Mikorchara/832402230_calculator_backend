\# 832402230 Calculator Backend



计算器项目的后端服务，使用 FastAPI 和 SQLite 实现。



后端负责计算数学表达式，并提供历史记录的保存、查询和删除功能。



\## 功能



\- 支持加、减、乘、除运算

\- 支持小数、括号和复合表达式

\- 使用 AST 解析表达式，不直接使用 `eval()`

\- 自动保存成功的计算记录

\- 查询历史记录

\- 删除指定历史记录

\- 处理非法表达式和除零错误



\## 技术栈



\- Python

\- FastAPI

\- SQLite

\- Pydantic

\- Uvicorn



\## 项目结构



```text

832402230\_calculator\_backend/

├── app/

│   ├── calculator.py

│   ├── database.py

│   └── main.py

├── calculator.db

├── .gitignore

├── PSP.md

├── README.md

└── codestyle.md

```



\## 运行环境



推荐使用 Python 3.9 或更高版本。



安装依赖：



```powershell

pip install fastapi uvicorn

```



启动后端：



```powershell

uvicorn app.main:app --reload

```



默认访问地址：



```text

http://127.0.0.1:8000

```



FastAPI API 文档：



```text

http://127.0.0.1:8000/docs

```



\## API



\### 计算表达式



```text

POST /api/calculate

```



请求示例：



```json

{

&#x20;   "expression": "(1+2)\*3"

}

```



\### 获取历史记录



```text

GET /api/history

```



\### 删除历史记录



```text

DELETE /api/history/{history\_id}

```



\## 数据库



项目使用 SQLite 保存计算历史。



程序启动时会自动创建 `history` 表，因此不需要手动创建数据库表。



历史记录包含：



\- ID

\- 表达式

\- 计算结果

\- 创建时间



\## 前后端连接



本地开发时允许以下前端地址访问后端：



```text

http://127.0.0.1:5500

```



前端和后端需要分别启动。

