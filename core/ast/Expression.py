from core.datatypes import Value


class Expression:
    def evaluate(self) -> Value:
        raise NotImplementedError
