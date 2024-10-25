from .Expression import Expression
from .Statement import Statement
from viewscript.std import Function, Functions

class FunctionStatement(Statement):
    def __init__(self, name: str, params: dict[str, Expression | None], statement: Statement):
        self.name = name
        self.params = params
        self.statement = statement

    @staticmethod
    def get_function(params: dict[str, Expression | None], statement: Statement):
        args = {}

        for k, v in params.items():
            arg_value = None

            if isinstance(v, Expression):
                arg_value = v.eval()

            args[k] = arg_value

        return Function(args, statement)

    def exec(self):
        Functions.set(self.name, self.get_function(self.params, self.statement))
