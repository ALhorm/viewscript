from core.ast import Expression, IdentifierExpression, FunctionCallExpression
from core.datatypes import Value
from core.globals import Globals


class ModGetExpression(Expression):
    def __init__(self, mod_name: str, gl_name: str, expr: IdentifierExpression | FunctionCallExpression):
        self.mod_name = mod_name
        self.gl_name = gl_name
        self.expr = expr

    def evaluate(self) -> Value:
        module = Globals.get_mod(self.mod_name)

        if isinstance(self.expr, FunctionCallExpression):
            return module.execute_fn(self.gl_name, self.expr.get_fn(self.mod_name).locals)
        if isinstance(self.expr, IdentifierExpression):
            return module.evaluate_var(self.gl_name)
