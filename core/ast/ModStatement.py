from core.ast import Statement, FunctionLetStatement, LetStatement
from core.globals import Globals, Module


class ModStatement(Statement):
    def __init__(self, name: str, statements: list[Statement]):
        self.name = name
        self.statements = statements

    def execute(self):
        variables = {}
        functions = {}

        for statement in self.statements:
            if isinstance(statement, FunctionLetStatement):
                functions[statement.name] = statement.get_fn()
            if isinstance(statement, LetStatement):
                variables[statement.name] = statement.get_var()

        Globals.set_mod(self.name, Module(variables, functions))
