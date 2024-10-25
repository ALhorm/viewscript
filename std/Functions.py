from .Function import Function

class Functions:
    functions: dict[str, Function] = {}

    @classmethod
    def get(cls, name: str) -> Function:
        if name in cls.functions:
            return cls.functions.get(name)
        raise Exception(f'Function "{name}" does not exist.')

    @classmethod
    def set(cls, name: str, function: Function) -> None:
        cls.functions[name] = function

    @classmethod
    def is_exists(cls, name: str) -> bool:
        return name in cls.functions
