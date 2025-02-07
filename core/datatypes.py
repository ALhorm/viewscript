from typing import Self
from core.errors import TypeConversionError, MathError


class Value:
    def __init__(self, value):
        self.value = value

    @property
    def typename(self) -> str:
        raise NotImplementedError

    def as_int(self) -> int:
        raise NotImplementedError

    def as_float(self) -> float:
        raise NotImplementedError

    def as_str(self) -> str:
        raise NotImplementedError

    def as_num(self) -> int | float:
        raise NotImplementedError

    def as_bool(self) -> bool:
        raise NotImplementedError

    def add(self, val: Self):
        raise NotImplementedError

    def sub(self, val: Self):
        raise NotImplementedError

    def mul(self, val: Self):
        raise NotImplementedError

    def div(self, val: Self):
        raise NotImplementedError

    def unary(self):
        raise NotImplementedError

    def or_(self, val: Self):
        return Bool(self.value or val.value)

    def and_(self, val: Self):
        return Bool(self.value and val.value)

    def equal(self, val: Self):
        return Bool(self.value == val.value)

    def not_equal(self, val: Self):
        return Bool(self.value != val.value)

    def greater(self, val: Self):
        return Bool(self.value > val.value)

    def greater_equal(self, val: Self):
        return Bool(self.value >= val.value)

    def less(self, val: Self):
        return Bool(self.value < val.value)

    def less_equal(self, val: Self):
        return Bool(self.value <= val.value)


class Int(Value):
    def __init__(self, value):
        super().__init__(int(value))

    @property
    def typename(self) -> str:
        return 'int'

    def as_int(self) -> int:
        return self.value

    def as_float(self) -> float:
        return float(self.value)

    def as_str(self) -> str:
        return str(self.value)

    def as_num(self) -> int | float:
        return int(self.value)

    def as_bool(self) -> bool:
        return bool(self.value)

    def add(self, val: Self):
        return Int(self.value + val.as_int())

    def sub(self, val: Self):
        return Int(self.value - val.as_int())

    def mul(self, val: Self):
        if isinstance(val, Str):
            return Str(self.value * val.as_str())

        return Int(self.value * val.as_int())

    def div(self, val: Self):
        result = self.value / val.as_int()
        return Int(result) if result.is_integer() else Float(result)

    def unary(self):
        return Int(-self.value)


class Float(Value):
    def __init__(self, value):
        super().__init__(float(value))

    @property
    def typename(self) -> str:
        return 'float'

    def as_int(self) -> int:
        return int(self.value)

    def as_float(self) -> float:
        return self.value

    def as_str(self) -> str:
        return str(self.value)

    def as_num(self) -> int | float:
        return float(self.value)

    def as_bool(self) -> bool:
        return bool(self.value)

    def add(self, val: Self):
        return Float(self.value + val.as_float())

    def sub(self, val: Self):
        return Float(self.value - val.as_float())

    def mul(self, val: Self):
        return Float(self.value * val.as_float())

    def div(self, val: Self):
        return Float(self.value / val.as_float())

    def unary(self):
        return Float(-self.value)


def number(value: int | float) -> Int | Float:
    return Int(value) if isinstance(value, int) else Float(value)


class Str(Value):
    def __init__(self, value):
        super().__init__(str(value))

    @property
    def typename(self) -> str:
        return 'str'

    def as_int(self) -> int:
        val = self.value

        try:
            val = int(val)
        except ValueError:
            TypeConversionError().call()

        return val

    def as_float(self) -> float:
        val = self.value

        try:
            val = float(val)
        except ValueError:
            TypeConversionError().call()

        return val

    def as_str(self) -> str:
        return self.value

    def as_num(self) -> int | float:
        return self.as_float() if '.' in self.value else self.as_int()

    def as_bool(self) -> bool:
        return bool(self.value)

    def add(self, val: Self):
        return Str(self.value + val.as_str())

    def sub(self, val: Self):
        MathError().call()

    def mul(self, val: Self):
        return Str(self.value * val.as_int())

    def div(self, val: Self):
        MathError().call()

    def unary(self):
        MathError().call()


class Bool(Value):
    def __init__(self, value):
        super().__init__(bool(value))

    @property
    def typename(self) -> str:
        return 'bool'

    def as_int(self) -> int:
        return int(self.value)

    def as_float(self) -> float:
        return float(self.value)

    def as_str(self) -> str:
        return str(self.value).lower()

    def as_num(self) -> int | float:
        return int(self.value)

    def as_bool(self) -> bool:
        return self.value

    def add(self, val: Self):
        return number(self.as_num() + val.as_num())

    def sub(self, val: Self):
        return number(self.as_num() - val.as_num())

    def mul(self, val: Self):
        return number(self.as_num() * val.as_num())

    def div(self, val: Self):
        return number(self.as_num() / val.as_num())

    def unary(self):
        return number(-self.as_num())


class Void(Value):
    def __init__(self):
        super().__init__(None)

    @property
    def typename(self) -> str:
        return 'void'

    def as_int(self) -> int:
        return 0

    def as_float(self) -> float:
        return 0.0

    def as_str(self) -> str:
        return 'void'

    def as_num(self) -> int | float:
        return 0

    def as_bool(self) -> bool:
        return False

    def add(self, val: Self):
        MathError().call()

    def sub(self, val: Self):
        MathError().call()

    def mul(self, val: Self):
        MathError().call()

    def div(self, val: Self):
        MathError().call()

    def unary(self):
        MathError().call()
