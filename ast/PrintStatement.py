from .Statement import Statement
from viewscript.ast import Expression


class PrintStatement(Statement):
    def __init__(self, expr: Expression):
        self.expr = expr

    def exec(self):
        print(self.expr.eval().as_str())
