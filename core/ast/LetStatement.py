from core.ast import Statement, Expression
from core.globals import Globals, Variable


class LetStatement(Statement):
    def __init__(self, name: str, expr: Expression, is_const: bool):
        self.name = name
        self.expr = expr
        self.is_const = is_const

    def get_var(self) -> Variable:
        return Variable(self.expr.evaluate(), self.is_const)

    def execute(self):
        Globals.set_var(self.name, self.get_var())
