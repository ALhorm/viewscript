from .Value import Value

class StrValue(Value):
    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f'"{self.value}"'

    def as_int(self) -> int:
        return int(self.value)

    def as_float(self) -> float:
        return float(self.value)

    def as_str(self) -> str:
        return self.value
