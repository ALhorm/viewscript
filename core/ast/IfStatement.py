from core.ast import Statement, Expression


class IfStatement(Statement):
    def __init__(self, if_exprs: list[Expression], if_stmts: list[Statement], else_stmt: Statement | None):
        self.if_exprs = if_exprs
        self.if_stmts = if_stmts
        self.else_stmt = else_stmt

    def execute(self):
        for i, v in enumerate(self.if_exprs):
            if v.evaluate().as_bool():
                self.if_stmts[i].execute()
                return

        if self.else_stmt is not None:
            self.else_stmt.execute()
