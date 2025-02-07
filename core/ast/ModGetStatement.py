from core.ast import Statement, Expression


class ModGetStatement(Statement):
    def __init__(self, expr: Expression):
        self.expr = expr

    def execute(self):
        self.expr.evaluate()
