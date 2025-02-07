from core.ast import Expression
from core.datatypes import Value, Int, Float, Str, Bool, Void


class ValueExpression(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self) -> Value:
        if isinstance(self.value, int):
            return Int(self.value)
        if isinstance(self.value, float):
            return Float(self.value)
        if isinstance(self.value, str):
            return Str(self.value)
        if isinstance(self.value, bool):
            return Bool(self.value)

        return Void()
