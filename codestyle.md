\# Backend Code Style



本项目后端使用 Python 和 FastAPI 开发，代码以简洁、清晰和易读为主要原则。



\## 1. 通用规范



\- 文件统一使用 UTF-8 编码。

\- 使用 4 个空格进行缩进。

\- 使用有意义的英文名称命名变量和函数。

\- 保持代码结构清晰，避免不必要的重复代码。

\- 对重要功能添加简单注释。



\## 2. Python 规范



\- 变量和函数使用 snake\_case（下划线命名）。

\- 常量使用大写字母和下划线命名。

\- 每个模块负责相对独立的功能。

\- 使用异常处理处理计算错误和非法输入。



例如：



```python

DATABASE\_PATH = "calculator.db"



def evaluate\_expression(expression: str):

&#x20;   # ...

```



\## 3. 项目模块



后端代码按照功能进行划分：



```text

main.py        FastAPI 应用和 API 路由

calculator.py  数学表达式解析和计算

database.py    SQLite 数据库操作

```



\## 4. API 规范



\- API 路径使用清晰的资源名称。

\- 使用合适的 HTTP 方法表示不同操作。

\- 请求数据使用 Pydantic 模型进行验证。

\- 请求失败时返回合适的 HTTP 状态码。



当前主要 API：



```text

POST   /api/calculate

GET    /api/history

DELETE /api/history/{history\_id}

```



\## 5. Git 提交



提交信息应简洁说明本次修改内容，例如：



```text

Initial backend implementation

Add backend documentation

Fix calculation error handling

```

