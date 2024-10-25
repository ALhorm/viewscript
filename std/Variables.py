from . import StrValue, IntValue
from .Value import Value


class Variables:
    vars: dict[str, Value] = {
        'w_title': StrValue('ViewScript Program'),
        'w_width': IntValue(500),
        'w_height': IntValue(700),
    }

    @classmethod
    def get(cls, name: str) -> Value:
        if name in cls.vars:
            return cls.vars.get(name)
        raise Exception(f'Variable "{name}" does not exist.')

    @classmethod
    def set(cls, name: str, value: Value) -> None:
        cls.vars[name] = value

    @classmethod
    def is_exists(cls, name: str) -> bool:
        return name in cls.vars
