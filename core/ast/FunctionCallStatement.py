from core.ast import Statement, FunctionCallExpression


class FunctionCallStatement(Statement):
    def __init__(self, fn_call_expr: FunctionCallExpression):
        self.fn_call_expr = fn_call_expr

    def execute(self):
        self.fn_call_expr.get_fn().execute()
