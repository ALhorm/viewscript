from core.ast import Expression
from core.datatypes import Value
from core.globals import Globals, Function


class IdentifierExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self) -> Value | Function:
        return Globals.get_var(self.name).value
