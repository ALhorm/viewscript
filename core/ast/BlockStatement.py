from core.ast import Statement


class BlockStatement(Statement):
    def __init__(self, statements: list[Statement]):
        self.statements = statements

    def execute(self):
        for statement in self.statements:
            statement.execute()
