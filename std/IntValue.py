from .Value import Value


class IntValue(Value):
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return self.as_str()

    def as_int(self) -> int:
        return self.value

    def as_float(self) -> float:
        return float(self.value)

    def as_str(self) -> str:
        return str(self.value)
