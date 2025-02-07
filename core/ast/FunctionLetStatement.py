from core.ast import Statement, Expression
from core.datatypes import Void
from core.globals import Variable, Globals, Function


class FunctionLetStatement(Statement):
    def __init__(self, name: str, params: dict[str, Expression | None], statement: Statement, is_const: bool):
        self.name = name
        self.params = params
        self.statement = statement
        self.is_const = is_const

    def get_fn(self) -> Function:
        fn_locals = {}

        for k, v in self.params.items():
            fn_locals[k] = Variable(v.evaluate() if v is not None else Void(), False)

        return Function(fn_locals, self.is_const, self.statement)

    def execute(self):
        Globals.set_fn(self.name, self.get_fn())
