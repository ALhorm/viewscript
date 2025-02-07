from core.ast import Statement
from importlib import import_module


class LoadlibStatement(Statement):
    def __init__(self, lib_name: str | None, statements: list[Statement] | None):
        self.lib_name = lib_name
        self.statements = statements

    def execute(self):
        if self.statements is not None:
            for statement in self.statements:
                statement.execute()
            return

        lib = import_module(f'libs.{self.lib_name}.main')
        lib.main()
