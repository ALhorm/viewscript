class Value:
    def as_int(self) -> int:
        raise NotImplementedError

    def as_float(self) -> float:
        raise NotImplementedError

    def as_str(self) -> str:
        raise NotImplementedError
