from core.ast import Expression
from core.datatypes import Value, Str


class RefExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self) -> Value:
        return Str(self.name)
