from core.datatypes import Value, Void
from core.errors import ReturnException


class Variable:
    def __init__(self, value: Value, is_const: bool):
        self.value = value
        self.typename = value.typename
        self.is_const = is_const

    def __repr__(self):
        return f'({self.value.value}, {self.typename}, {self.is_const})'


class Function:
    def __init__(self, locals_: dict[str, Variable], is_const: bool, statement = ...):
        self.locals = locals_
        self.statement = statement
        self.is_const = is_const

    def get_param(self, name: str) -> Value:
        return self.locals[name].value

    def execute(self):
        Globals.push_vars(self.locals)
        value = Void()

        if self.statement is ...:
            return self.fn_main()

        try:
            self.statement.execute()
        except ReturnException as re:
            value = re.value

        Globals.pop_vars()
        return value

    def fn_main(self):
        ...


class Module:
    def __init__(self, variables: dict[str, Variable], functions: dict[str, Function]):
        self.variables = variables
        self.functions = functions

    def execute_fn(self, name: str, fn_locals: dict[str, Variable]):
        function = self.functions[name]
        function.locals = fn_locals
        return function.execute()

    def evaluate_var(self, name: str) -> Value:
        return self.variables[name].value


class Globals:
    variables = {}
    functions = {}
    modules: dict[str, Module] = {}
    vars_buffer = {}
    fns_buffer = {}

    @classmethod
    def get_var(cls, name: str) -> Variable:
        return cls.variables[name]

    @classmethod
    def get_var_buf(cls, name: str) -> Variable:
        return cls.vars_buffer[name]

    @classmethod
    def get_fn(cls, name: str) -> Function:
        return cls.functions[name]

    @classmethod
    def get_mod(cls, name: str) -> Module:
        return cls.modules[name]

    @classmethod
    def get_var_mod(cls, mod_name: str, var_name: str) -> Variable:
        return cls.modules[mod_name].variables[var_name]

    @classmethod
    def get_fn_mod(cls, mod_name: str, fn_name: str) -> Function:
        return cls.modules[mod_name].functions[fn_name]

    @classmethod
    def set_var(cls, name: str, var: Variable):
        cls.variables[name] = var

    @classmethod
    def set_var_buf(cls, name: str, var: Variable):
        cls.vars_buffer[name] = var

    @classmethod
    def set_fn(cls, name: str, fn: Function):
        cls.functions[name] = fn

    @classmethod
    def set_mod(cls, name: str, mod: Module):
        cls.modules[name] = mod

    @classmethod
    def is_var_exists(cls, name: str) -> bool:
        return name in cls.variables

    @classmethod
    def is_fn_exists(cls, name: str) -> bool:
        return name in cls.functions

    @classmethod
    def push_vars(cls, vars_: dict[str, Variable]):
        cls.vars_buffer = cls.variables.copy()
        cls.variables.update(vars_.copy())

    @classmethod
    def pop_vars(cls) -> dict[str, Variable]:
        cls.variables = cls.vars_buffer.copy()
        cls.vars_buffer.clear()
        return cls.variables.copy()
