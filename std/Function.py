from viewscript.ast import Statement
from viewscript.std import Value


class Function:
    def __init__(self, args: dict[str, Value], statement: Statement):
        self.args = args
        self.statement = statement

    def exec(self):
        ...
