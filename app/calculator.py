import ast
import operator


# 允许使用的二元运算符
BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

# 允许使用的正负号
UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def evaluate_expression(expression: str):
    tree = ast.parse(expression, mode="eval")
    return _evaluate(tree.body)


def _evaluate(node):
    # 数字
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

    # 加减乘除
    if isinstance(node, ast.BinOp):
        operator_type = type(node.op)

        if operator_type not in BINARY_OPERATORS:
            raise ValueError("Unsupported operator")

        left = _evaluate(node.left)
        right = _evaluate(node.right)

        return BINARY_OPERATORS[operator_type](left, right)

    # 正数和负数，例如 -5
    if isinstance(node, ast.UnaryOp):
        operator_type = type(node.op)

        if operator_type not in UNARY_OPERATORS:
            raise ValueError("Unsupported operator")

        value = _evaluate(node.operand)

        return UNARY_OPERATORS[operator_type](value)

    raise ValueError("Invalid expression")