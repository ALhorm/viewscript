from .Statement import Statement
from viewscript.ast import Expression
from viewscript.std import Variables


class LetStatement(Statement):
    def __init__(self, name: str, expr: Expression):
        self.name = name
        self.expr = expr

    def exec(self):
        Variables.set(self.name, self.expr.eval())
