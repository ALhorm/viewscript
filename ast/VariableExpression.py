from .Expression import Expression
from viewscript.std import Value, Variables


class VariableExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def eval(self) -> Value:
        return Variables.get(self.name)
