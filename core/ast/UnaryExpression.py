from core.ast import Expression
from core.datatypes import Value, number


class UnaryExpression(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def evaluate(self) -> Value:
        return self.expr.evaluate().unary()
