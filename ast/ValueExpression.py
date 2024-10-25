from .Expression import Expression
from viewscript.std import *

class ValueExpression(Expression):
    def __init__(self, value) -> None:
        self.value = value

    def eval(self) -> Value:
        if isinstance(self.value, int):
            return IntValue(self.value)
        elif isinstance(self.value, float):
            return FloatValue(self.value)
        elif isinstance(self.value, str):
            return StrValue(self.value)
