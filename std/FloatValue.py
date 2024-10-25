from .Value import Value


class FloatValue(Value):
    def __init__(self, value: float) -> None:
        self.value = value

    def __repr__(self) -> str:
        return self.as_str()

    def as_int(self) -> int:
        return int(self.value)

    def as_float(self) -> float:
        return self.value

    def as_str(self) -> str:
        return str(self.value)
