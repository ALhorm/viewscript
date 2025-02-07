from core.ast import Expression
from core.datatypes import Value


class BinaryExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression, operation: str):
        self.expr1 = expr1
        self.expr2 = expr2
        self.operation = operation

    def evaluate(self) -> Value:
        value1 = self.expr1.evaluate()
        value2 = self.expr2.evaluate()

        match self.operation:
            case '+':
                return value1.add(value2)
            case '-':
                return value1.sub(value2)
            case '*':
                return value1.mul(value2)
            case '/':
                return value1.div(value2)
