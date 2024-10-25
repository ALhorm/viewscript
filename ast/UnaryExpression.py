from .Expression import Expression
from viewscript.std import Value, FloatValue

class UnaryExpression(Expression):
    def __init__(self, expr: Expression) -> None:
        self.expr = expr

    def eval(self) -> Value:
        val = self.expr.eval()
        return FloatValue(-val.as_float())
