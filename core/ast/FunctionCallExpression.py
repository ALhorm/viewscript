from core.ast import Expression
from core.datatypes import Value, Void
from ..errors import ReturnException
from ..globals import Variable, Globals, Function


class FunctionCallExpression(Expression):
    def __init__(self, name: str, args: dict[str | int, Expression]):
        self.name = name
        self.args = args

    def get_fn(self, mod_name: str = ...) -> Function:
        function = Globals.get_fn(self.name) if mod_name is ... else Globals.get_mod(mod_name).functions[self.name]

        for k, v in self.args.items():
            value = v.evaluate()

            if isinstance(k, str) and k in function.locals:
                function.locals[k] = Variable(value, False)
                continue

            name = list(function.locals.keys())[k]
            function.locals[name] = Variable(value, False)

        return function

    def evaluate(self) -> Value:
        return self.get_fn().execute()
