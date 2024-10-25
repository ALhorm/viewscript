from .Statement import Statement
from viewscript.ast import Expression
from viewscript.std import Variables

class AssignmentStatement(Statement):
    def __init__(self, name: str, expr: Expression):
        self.name = name
        self.expr = expr

    def exec(self):
        if not Variables.is_exists(self.name):
            raise Exception(f'Variable {self.name} does not exist.')

        Variables.set(self.name, self.expr.eval())
