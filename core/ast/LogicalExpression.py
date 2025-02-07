from core.ast import Expression
from core.datatypes import Value, Bool


class LogicalExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression, operation: str):
        self.expr1 = expr1
        self.expr2 = expr2
        self.operation = operation

    def evaluate(self) -> Value:
        value1 = self.expr1.evaluate()
        value2 = self.expr2.evaluate()

        match self.operation:
            case '||':
                return value1.or_(value2)
            case '&&':
                return value1.and_(value2)
            case '==':
                return value1.equal(value2)
            case '!=':
                return value1.not_equal(value2)
            case '>':
                return value1.greater(value2)
            case '>=':
                return value1.greater_equal(value2)
            case '<':
                return value1.less(value2)
            case '<=':
                return value1.less_equal(value2)
