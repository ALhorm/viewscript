from .Expression import Expression
from viewscript.std import Value, FloatValue


class BinaryExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression, operation: str) -> None:
        self.expr1 = expr1
        self.expr2 = expr2
        self.operation = operation

    def eval(self) -> Value:
        val1 = self.expr1.eval()
        val2 = self.expr2.eval()

        num1 = val1.as_float()
        num2 = val2.as_float()

        match self.operation:
            case '+':
                return FloatValue(num1 + num2)
            case '-':
                return FloatValue(num1 - num2)
            case '*':
                return FloatValue(num1 * num2)
            case '/':
                return FloatValue(num1 / num2)
