from core.ast import Statement, Expression
from core.errors import ReturnException


class ReturnStatement(Statement):
    def __init__(self, expr: Expression):
        self.expr = expr

    def execute(self):
        raise ReturnException(self.expr.evaluate())
